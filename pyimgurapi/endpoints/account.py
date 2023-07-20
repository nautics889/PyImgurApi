from urllib.parse import urljoin

from .base_endpoint import BaseEndpoint


class Account(BaseEndpoint):
    """Account management"""

    def generate_access_token(self, refresh_token, client_id, client_secret):
        """
        Generate access token for an application.

        See
        https://apidocs.imgur.com/#3f80c836-8f49-4fb1-95a7-a4b058265d72

        Args:
            refresh_token (str, optional): OAuth2 refresh token.
            client_id (str, optional): Imgur client ID.
            client_secret (str, optional): Imgur client Secret.

        Returns:
            (DynamicResponseData): Response from Imgur.

        Examples:

        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> response = api.account.generate_access_token(
        ...     refresh_token=api.refresh_token,
        ...     client_id=api.client_id,
        ...     client_secret=api.client_secret
        ... )
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
        url_path = "/oauth2/token"

        data = dict()
        if refresh_token:
            data.update(refresh_token=refresh_token)
        if client_id and client_secret:
            data.update(client_id=client_id, client_secret=client_secret)
        data.update(grant_type="refresh_token")

        headers = {"Content-Type": "application/json"}

        return self.make_request(
            url_path, data=data, headers=headers, method="POST"
        )

    def base(self, username="me"):
        """
        Fetch base information about account.

        See
        https://apidocs.imgur.com/#c94c8719-fe68-4854-b96d-70735dd8b2bc

        Args:
            username (str, optional): Account ID for which information
                                      will be fetched. Defaults to "me"
                                      meaning the current account
                                      (supposing the application works
                                      in authorized mode).

        Returns:
            (DynamicResponseData): Response from Imgur.

        Examples:

        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> response = api.account.generate_access_token(
        ...     refresh_token=api.refresh_token,
        ...     client_id=api.client_id,
        ...     client_secret=api.client_secret
        ... )
        >>> print(response)
        {
          "data": {
            "id": 63193032,
            "url": "tester123",
            "bio": null,
            "avatar": null,
            "avatar_name": null,
            "cover": null,
            "cover_name": null,
            "reputation": 0,
            "reputation_name": "Neutral",
            "created": 1502138950,
            "pro_expiration": false,
            "user_follow": {
              "status": false
            },
            "is_blocked": false
          },
          "success": true,
          "status": 200
        }

        """
        url_path = f"/{self.api_version}/account/{username}"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def gallery_favorites(self, username="me", page=None, sort=None):
        url_path = f"/{self.api_version}/account/{username}/gallery_favorites"

        if page is not None:
            url_path = urljoin(f"{url_path}/", str(page))

        if sort is not None:
            url_path = urljoin(f"{url_path}/", str(sort))

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def favorites(self, username="me", page=None, favorite_sort=None):
        url_path = f"/{self.api_version}/account/{username}/favorites"

        if page is not None:
            url_path = urljoin(f"{url_path}/", str(page))

        if favorite_sort is not None:
            url_path = urljoin(f"{url_path}/", str(favorite_sort))

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def images(self, username="me", page=None):
        url_path = f"/{self.api_version}/account/{username}/images"

        if page is not None:
            url_path = urljoin(f"{url_path}/", str(page))

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def image(self, image_hash, username="me"):
        url_path = f"/{self.api_version}/account/{username}/image/{image_hash}"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def image_ids(self, username="me", page=None):
        url_path = f"/{self.api_version}/account/{username}/images/ids/{page}"

        if page is not None:
            url_path = urljoin(f"{url_path}/", str(page))

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def image_count(self, username="me"):
        url_path = f"/{self.api_version}/account/{username}/images/count"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def image_delete(self, delete_hash, username="me"):
        url_path = (
            f"/{self.api_version}" f"/account/{username}/image/{delete_hash}"
        )

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers, method="DELETE")

    def replies(self, username="me"):
        url_path = (
            f"/{self.api_version}/account/{username}" f"/notifications/replies"
        )

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)
