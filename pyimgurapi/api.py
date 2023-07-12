from .endpoints import Account, Album, Comment, Feed, Gallery, Image


class ImgurAPI:
    def __init__(self, refresh_token=None, client_id=None, client_secret=None):
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None

        self.endpoints = dict(
            account=Account,
            album=Album,
            comment=Comment,
            feed=Feed,
            gallery=Gallery,
            image=Image,
        )

    def auth(self):
        auth_response = self.account.generate_access_token(
            refresh_token=self.refresh_token,
            client_id=self.client_id,
            client_secret=self.client_secret,
        )
        token = auth_response.access_token
        self.access_token = token
        return auth_response

    def __getattr__(self, item):
        if item in self.endpoints:
            return self.endpoints[item](
                client_id=self.client_id, access_token=self.access_token
            )
        raise NotImplementedError(
            f"Endpoint {item} is not supported or is not implemented yet."
        )
