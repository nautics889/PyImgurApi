from .base_endpoint import BaseEndpoint
from ..form_factories import get_image_form


class Image(BaseEndpoint):
    """Image management"""

    def get_image(self, image_hash):
        """
        Fetch info about image.

        See
        https://apidocs.imgur.com/#2078c7e0-c2b8-4bc8-a646-6e544b087d0f

        Args:
            image_hash (str): Unique ID representing the image.

        Returns:
            (DynamicResponseData): Response from Imgur.

        Examples:

        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> response = api.image("3MvMVho")
        >>> print(response)
        {
          "data": {
            "id": "3MvMVho",
            "title": "cat_image",
            "description": "lorem ipsum dolor sit amet",
            "datetime": 1624131938,
            "type": "image/jpeg",
            "animated": false,
            "width": 800,
            "height": 695,
            "size": 66952,
            "views": 0,
            "bandwidth": 2638377,
            "vote": null,
            "favorite": true,
            "nsfw": false,
            "section": null,
            "account_url": null,
            "account_id": 63193032,
            "is_ad": false,
            "in_most_viral": false,
            "has_sound": false,
            "tags": [],
            "ad_type": 0,
            "ad_url": "",
            "edited": "0",
            "in_gallery": false,
            "deletehash": "abcdefghijklmno",
            "name": "7.jpg",
            "link": "https://i.imgur.com/3MvMVho.jpg",
            "ad_config": {
              "safeFlags": [
                "not_in_gallery",
                "share"
              ],
              "highRiskFlags": [],
              "unsafeFlags": [
                "sixth_mod_unsafe",
                "onsfw_mod_unsafe"
              ],
              "wallUnsafeFlags": [
                "onsfw_mod_unsafe_wall"
              ],
              "showsAds": false,
              "showAdLevel": 0,
              "safe_flags": [
                "not_in_gallery",
                "share"
              ],
              "high_risk_flags": [],
              "unsafe_flags": [
                "sixth_mod_unsafe",
                "onsfw_mod_unsafe"
              ],
              "wall_unsafe_flags": [
                "onsfw_mod_unsafe_wall"
              ],
              "show_ads": false,
              "show_ad_level": 0,
              "nsfw_score": 0
            }
          },
          "success": true,
          "status": 200
        }

        """
        url_path = f"/{self.api_version}/image/{image_hash}"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def upload(
        self, file_obj, filename, title=None, description=None, album=None
    ):
        """
        Upload an image.

        Sends an image file to the server along with optional metadata
        such as title, description, and album information.

        See
        https://apidocs.imgur.com/#c85c9dfc-7487-4de2-9ecd-66f727cf3139

        Args:
            file_obj (BufferedReader): File-like object containing
                                       the image data to be uploaded.
            filename (str): Filename of the image being uploaded.
            title (str, optional): Title or caption for the
                                   uploaded image. Defaults to None.
            description (str, optional): Description of the uploaded
                                         image. Defaults to None.
            album (str, optional): ID of the album to which the image
                                   will be added. Defaults to None.

        Returns:
            (DynamicResponseData): Response from Imgur.

        Examples:

        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> api.auth()
        >>> with open("image.jpg", "rb") as file:
        ...     response = api.image.upload(
        ...         file, "image.jpg", title="cat_image",
        ...         description="lorem ipsum dolor sit amet"
        ...     )
        >>> print(response)
        {
          "status": 200,
          "success": true,
          "data": {
            "id": "3MvMVho",
            "deletehash": "abcdefghijklmno",
            "account_id": 63193032,
            "account_url": "tester123",
            "ad_type": null,
            "ad_url": null,
            "title": "cat_image",
            "description": "lorem ipsum dolor sit amet",
            "name": "",
            "type": "image/jpeg",
            "width": 800,
            "height": 695,
            "size": 66952,
            "views": 0,
            "section": null,
            "vote": null,
            "bandwidth": 0,
            "animated": false,
            "favorite": false,
            "in_gallery": false,
            "in_most_viral": false,
            "has_sound": false,
            "is_ad": false,
            "nsfw": null,
            "link": "https://i.imgur.com/3MvMVho.jpeg",
            "tags": [],
            "datetime": 1690046994,
            "mp4": "",
            "hls": ""
          }
        }
        >>> print(response.status_code)
        200
        """
        url_path = f"/{self.api_version}/upload"

        form = get_image_form(
            file_obj,
            filename,
            title=title,
            description=description,
            album=album,
        )

        headers = self.get_headers(form=form)

        return self.make_request(
            url_path, data=bytes(form), headers=headers, method="POST"
        )

    def delete(self, image_hash):
        """
        Delete an image from Imgur using image ID or deleteHash.

        The deleteHash can be used instead of image ID for
        non-authorized deletion.

        See
        https://apidocs.imgur.com/#ca48883b-6964-4ab8-b87f-c274e32a970d

        Args:
            image_hash (str): The unique ID representing the image
                              or deleteHash.

        Returns:
            (DynamicResponseData): Response from Imgur.

        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> api.auth()
        >>> response = api.image.delete("3MvMVho")
        >>> print(response)
        {
          "status": 200,
          "success": true,
          "data": true
        }
        """
        url_path = f"/{self.api_version}/image/{image_hash}"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers, method="DELETE")

    def update(self, image_hash, title=None, description=None, album=None):
        """
        Update an image on Imgur using image ID or deleteHash.

        The deleteHash can be used instead of image ID for
        non-authorized updating.

        See
        https://apidocs.imgur.com/#7db0c13c-bf70-4e87-aecf-047abc65686d

        Args:
            image_hash (str): Unique ID representing the image
                              or deleteHash.
            title (str, optional): New title for the  image.
                                   Defaults to None.
            description (str, optional): New description of the image.
                                         Defaults to None.
            album (str, optional): ID of the album to which the image
                                   will be added. Defaults to None.

        Returns:
            (DynamicResponseData): Response from Imgur.

        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> response = api.image.update("3MvMVho", title="New title")
        >>> print(response)
        {
          "status": 200,
          "success": true,
          "data": true
        }
        """
        url_path = f"/{self.api_version}/image/{image_hash}"

        form = get_image_form(
            title=title, description=description, album=album
        )

        headers = self.get_headers(form=form)

        return self.make_request(
            url_path, data=bytes(form) or None, headers=headers, method="POST"
        )

    def favorite(self, image_hash):
        """
        Add an image to favorite list.

        See
        https://apidocs.imgur.com/#5dd1c471-a806-43cb-9067-f5e4fc8f28bd

        Args:
            image_hash (str): Unique ID representing the image.

        Returns:
            (DynamicResponseData): Response from Imgur.

        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> response = api.image.favorite("3MvMVho")
        >>> print(response)
        {
          "status": 200,
          "success": true,
          "data": "favorited"
        }
        """
        url_path = f"/{self.api_version}/image/{image_hash}/favorite"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers, method="POST")

    def __call__(self, image_hash):
        return self.get_image(image_hash)
