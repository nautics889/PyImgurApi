from pyimgurapi.base_endpoint import BaseEndpoint


class Account(BaseEndpoint):
    def generate_access_token(
        self, refresh_token=None, client_id=None, client_secret=None
    ):
        url_path = "/oauth2/token"

        data = dict()
        if refresh_token:
            data.update(refresh_token=refresh_token)
        if client_id and client_secret:
            data.update(client_id=client_id, client_secret=client_secret)
        data.update(grant_type="refresh_token")

        headers = {"Content-Type": "application/json"}

        return self.make_request(url_path, data=data, headers=headers)
