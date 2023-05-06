from pyimgurapi.account import Account
from pyimgurapi.image import Image


class ImgurAPI:
    def __init__(self, refresh_token=None, client_id=None, client_secret=None):
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None

        self.account = Account()
        self.image = Image()

    def auth(self):
        auth_response_data = self.account.generate_access_token(
            refresh_token=self.refresh_token,
            client_id=self.client_id,
            client_secret=self.client_secret,
        )
        self.access_token = auth_response_data.get("access_token")
        return auth_response_data
