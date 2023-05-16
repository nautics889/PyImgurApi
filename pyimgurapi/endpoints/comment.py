from .base_endpoint import BaseEndpoint
from ..utils import MultipartForm, Field


class Comment(BaseEndpoint):
    def get_comment(self, comment_id):
        url_path = f"/3/comment/{comment_id}"

        headers = {
            "Content-Type": "application/json",
        }
        headers.update(**self.get_auth_header())

        return self.make_request(url_path, headers=headers)

    def create(self, image_id, comment):
        url_path = "/3/comment"

        fields = [
            Field(field_name="image_id", value=image_id),
            Field(field_name="comment", value=comment),
        ]
        file_form = MultipartForm(fields=fields)

        data = bytes(file_form)

        headers = {
            "Content-Type": file_form.get_content_type(),
            "Content-length": str(len(data)),
        }
        headers.update(**self.get_auth_header())

        return self.make_request(
            url_path, data=data, headers=headers, method="POST"
        )

    def delete(self, image_hash):
        url_path = f"/3/image/{image_hash}"

        headers = {
            "Content-Type": "application/json",
        }
        headers.update(**self.get_auth_header())

        return self.make_request(url_path, headers=headers, method="DELETE")

    def replies(self, comment_id):
        url_path = f"/3/comment/{comment_id}/replies"

        headers = {
            "Content-Type": "application/json",
        }
        headers.update(**self.get_auth_header())

        return self.make_request(url_path, headers=headers)

    def create_reply(self, image_id, comment_id, comment):
        url_path = f"/3/comment/{comment_id}"

        fields = [
            Field(field_name="image_id", value=image_id),
            Field(field_name="comment", value=comment),
        ]
        file_form = MultipartForm(fields=fields)

        data = bytes(file_form)

        headers = {
            "Content-Type": file_form.get_content_type(),
            "Content-length": str(len(data)),
        }
        headers.update(**self.get_auth_header())

        return self.make_request(
            url_path, data=data, headers=headers, method="POST"
        )

    def vote(self, comment_id, vote_value="up"):
        vote_values = ("up", "down", "veto")
        if vote_value not in vote_values:
            raise ValueError(
                f"Inappropriate value for `vote_value`: '{vote_value}', "
                f"currently supported: {vote_values}"
            )

        url_path = f"/3/comment/{comment_id}/vote/{vote_value}"

        headers = {"Content-Type": "application/json"}
        headers.update(**self.get_auth_header())

        return self.make_request(url_path, headers=headers, method="POST")

    def report(self, comment_id, reason):
        possible_reasons = ("1", "2", "3", "4", "5")
        if str(reason) not in possible_reasons:
            raise ValueError(
                f"Inappropriate value for `reason`: '{reason}', "
                f"currently supported: {possible_reasons}"
            )

        url_path = f"/3/comment/{comment_id}/report"

        headers = {"Content-Type": "application/json"}
        headers.update(**self.get_auth_header())

        return self.make_request(url_path, headers=headers, method="POST")

    def __call__(self, comment_id):
        return self.get_comment(comment_id)
