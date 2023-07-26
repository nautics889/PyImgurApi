from .base_endpoint import BaseEndpoint
from ..form_factories import get_comment_form, get_comment_report_form


class Comment(BaseEndpoint):
    def get_comment(self, comment_id):
        """
        Fetch info about comment.

        See
        https://apidocs.imgur.com/#fba2b4a0-a0b9-47e0-80ae-f2f41201f2c3

        Args:
            comment_id (str|int): Unique ID representing the comment.

        Returns:
            (DynamicResponseData): Response from Imgur.

        Examples:

        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> response = api.comment(632941205)
        >>> print(response)
        {
          "data": {
            "id": 632941205,
            "image_id": "3MvMVho",
            "comment": "Lorem ipsum dolor sit amet",
            "author": "tester",
            "author_id": 63193032,
            "on_album": false,
            "album_cover": null,
            "ups": 20,
            "downs": 0,
            "points": 20,
            "datetime": 1461424345,
            "parent_id": 0,
            "deleted": false,
            "vote": null,
            "platform": "iphone",
            "has_admin_badge": false,
            "children": []
          },
          "success": true,
          "status": 200
        }

        """
        url_path = f"/{self.api_version}/comment/{comment_id}"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def create(self, image_id, comment):
        """
        Create comment under a specific publication.

        See
        https://apidocs.imgur.com/#01dce1de-f332-4a14-88fa-25f97cc13613

        Args:
            image_id (str|int): Unique ID representing the image.
            comment (str): Content of the comment.

        Returns:
            (DynamicResponseData): Response from Imgur.

        Examples:

        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> response = api.comment.create("3MvMVho", "Lorem ipsum")
        >>> print(response)
        {
          "data": {
            "id": 632941205
          },
          "status": 200,
          "success": true
        }

        Notes:
            - Use `create_reply()` method instead of this for creating
            a reply to the comment.

        """
        url_path = f"/{self.api_version}/comment"

        form = get_comment_form(image_id, comment)

        headers = self.get_headers(form=form)

        return self.make_request(
            url_path, data=bytes(form), headers=headers, method="POST"
        )

    def delete(self, comment_id):
        """
        Delete a comment.

        See
        https://apidocs.imgur.com/#946e326e-47ba-4da7-a7fb-026c727e28ac

        Args:
            comment_id (str|int): Unique ID representing the comment.

        Returns:
            (DynamicResponseData): Response from Imgur.

        Examples:

        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> response = api.comment.delete(632941205)
        >>> print(response)
        {
          "data": {
            "id": 632941205
          },
          "status": 200,
          "success": true
        }

        """
        url_path = f"/{self.api_version}/comment/{comment_id}"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers, method="DELETE")

    def replies(self, comment_id):
        """
        Fetch replies to a specific comment.

        See
        https://apidocs.imgur.com/#8d5f32eb-64e1-436e-a0e1-2f9db82e7e67

        Args:
            comment_id (str|int): Unique ID representing the comment.

        Returns:
            (DynamicResponseData): Response from Imgur.

        Examples:

        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> response = api.comment.replies(632941205)
        >>> print(response)
        {
          "data": {
            "id": 632941205,
            "image_id": "3MvMVho",
            "comment": "Lorem ipsum",
            "author": "tester1",
            "author_id": 63193032,
            "on_album": true,
            "album_cover": null,
            "ups": 5,
            "downs": 0,
            "points": 5,
            "datetime": 1687062012,
            "parent_id": 0,
            "deleted": false,
            "vote": null,
            "platform": "iphone",
            "has_admin_badge": false,
            "children": [
              {
                "id": 632941206,
                "image_id": "3MvMVho",
                "comment": "Lorem ipsum dolor",
                "author": "tester2",
                "author_id": 63193033,
                "on_album": true,
                "album_cover": null,
                "ups": 5,
                "downs": 0,
                "points": 5,
                "datetime": 1687062015,
                "parent_id": 632941205,
                "deleted": false,
                "vote": null,
                "platform": "android",
                "has_admin_badge": false,
                "children": []
              },
              {
                "id": 632941207,
                "image_id": "3MvMVho",
                "comment": "Lorem ipsum dolor sit amet",
                "author": "tester3",
                "author_id": 63193034,
                "on_album": true,
                "album_cover": null,
                "ups": 5,
                "downs": 0,
                "points": 5,
                "datetime": 1687062025,
                "parent_id": 632941205,
                "deleted": false,
                "vote": null,
                "platform": "android",
                "has_admin_badge": false,
                "children": []
              }
            ]
          },
          "success": true,
          "status": 200
        }

        """
        url_path = f"/{self.api_version}/comment/{comment_id}/replies"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def create_reply(self, image_id, comment_id, comment):
        """
        Create reply for a specific comment.

        See
        https://apidocs.imgur.com/#d7aea8ae-eb82-4ead-bb51-7a2f6b209fac

        Args:
            image_id (str): Unique ID representing the image
                            (publication).
            comment_id (str|int): Unique ID representing the comment
                                  which the reply will be created for.
            comment (str): Content of the comment.

        Returns:
            (DynamicResponseData): Response from Imgur.

        Examples:

        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> response = api.comment.create_reply(
        ...     "3MvMVho", 632941205, "Lorem ipsum dolor"
        ... )
        >>> print(response)
        {
          "data": {
            "id": 632941206
          },
          "status": 200,
          "success": true
        }

        """
        url_path = f"/{self.api_version}/comment/{comment_id}"

        form = get_comment_form(image_id, comment)

        headers = self.get_headers(form=form)

        return self.make_request(
            url_path, data=bytes(form), headers=headers, method="POST"
        )

    def vote(self, comment_id, vote="up"):
        """
        Set a vote for a specific comment.

        See
        https://apidocs.imgur.com/#2d9d6c7b-7ff1-499d-ab7f-1b488063dc62

        Args:
            comment_id (str|int): Unique ID representing the comment.
            vote (str, optional): Value of the vote. Possible values:
                                  "up", "down", "veto". Defaults to
                                  "up".
        Returns:
            (DynamicResponseData): Response from Imgur.

        Examples:

        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> response = api.comment.vote(632941205, "up")
        >>> print(response)
        {
          "data": true,
          "status": 200,
          "success": true
        }

        """
        possible_vote_values = ("up", "down", "veto")
        if vote not in possible_vote_values:
            raise ValueError(
                f"Inappropriate value for `vote_value`: '{vote}', "
                f"currently supported: {possible_vote_values}"
            )

        url_path = f"/{self.api_version}/comment/{comment_id}/vote/{vote}"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers, method="POST")

    def report(self, comment_id, reason=None):
        """
        Report a comment.

        See
        https://apidocs.imgur.com/#174c15ca-66f9-4c37-8ff5-da36c15a0fbd

        Args:
            comment_id (str|int): Unique ID representing the comment.
            reason (str, optional): Represents a reason for report.
                                    Possible values: None, "1", "2",
                                    "3", "4", "5". Defaults to None.
        Returns:
            (DynamicResponseData): Response from Imgur.

        Examples:

        >>> from pyimgurapi import ImgurAPI
        >>> api = ImgurAPI(
        ...     refresh_token="***",
        ...     client_id="***",
        ...     client_secret="***"
        ... )
        >>> response = api.comment.report(632941205, "1")
        >>> print(response)
        {
          "data": true,
          "status": 200,
          "success": true
        }

        """
        url_path = f"/{self.api_version}/comment/{comment_id}/report"

        form = get_comment_report_form(reason)

        headers = self.get_headers(form=form)

        return self.make_request(
            url_path, data=bytes(form) or None, headers=headers, method="POST"
        )

    def __call__(self, comment_id):
        return self.get_comment(comment_id)
