from .endpoints import Account, Album, Comment, Image


class ImgurAPI:
    """Representation of Imgur API"""

    def __init__(self, refresh_token=None, client_id=None, client_secret=None):
        """
        Initialize Imgur API object.

        Args:
            refresh_token (str, optional): OAuth2 refresh token.
            client_id (str, optional): Imgur client ID.
            client_secret (str, optional): Imgur client Secret.

        Notes:
            - To make authorized requests each of `refresh_token`,
            `client_id` and `client_secret` together must be provided

        """
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None

        self.endpoints = dict(
            account=Account,
            album=Album,
            comment=Comment,
            image=Image,
        )

    def auth(self):
        """
        Authenticate an API-object.

        The credentials for authentication are represented by
        `self.client_id`, `self.client_secret` and `self.access_token`.

        See https://apidocs.imgur.com/#authorization-and-oauth

        Returns:
            (DynamicResponseData): Response from Imgur.

        Examples:
        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> response = api.auth()
        >>> print(response)
        {
          "access_token": "693f426bfc2547229de2fd01e4297ab2693f426b",
          "expires_in": 315360000,
          "token_type": "bearer",
          "scope": null,
          "refresh_token": "28b662d883b6d76fd96e4ddc5e9ba780df85615f",
          "account_id": 63193032,
          "account_username": "tester123"
        }
        """
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
