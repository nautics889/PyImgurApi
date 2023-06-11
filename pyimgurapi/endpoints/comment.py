from .base_endpoint import BaseEndpoint
from ..form_factories import get_comment_form, get_comment_report_form


class Comment(BaseEndpoint):
    def get_comment(self, comment_id):
        url_path = f"/{self.api_version}/comment/{comment_id}"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def create(self, image_id, comment):
        url_path = f"/{self.api_version}/comment"

        form = get_comment_form(image_id, comment)

        headers = self.get_headers(form=form)

        return self.make_request(
            url_path, data=bytes(form), headers=headers, method="POST"
        )

    def delete(self, image_hash):
        url_path = f"/{self.api_version}/image/{image_hash}"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers, method="DELETE")

    def replies(self, comment_id):
        url_path = f"/{self.api_version}/comment/{comment_id}/replies"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def create_reply(self, image_id, comment_id, comment):
        url_path = f"/{self.api_version}/comment/{comment_id}"

        form = get_comment_form(image_id, comment)

        headers = self.get_headers(form=form)

        return self.make_request(
            url_path, data=bytes(form), headers=headers, method="POST"
        )

    def vote(self, comment_id, vote="up"):
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
        url_path = f"/{self.api_version}/comment/{comment_id}/report"

        form = get_comment_report_form(reason)

        headers = self.get_headers(form=form)

        return self.make_request(
            url_path, data=bytes(form) or None, headers=headers, method="POST"
        )

    def __call__(self, comment_id):
        return self.get_comment(comment_id)
