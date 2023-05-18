from .base_endpoint import BaseEndpoint
from ..utils import MultipartForm, File, Field


class Image(BaseEndpoint):
    def get_image(self, image_hash):
        url_path = f"/3/image/{image_hash}"

        headers = {
            "Content-Type": "application/json",
        }
        headers.update(**self.get_auth_header())

        return self.make_request(url_path, headers=headers)

    def upload(self, file_obj, filename, **kwargs):
        url_path = "/3/upload"

        fields = [
            Field(field_name=field_name, value=str(kwargs.get(field_name)))
            for field_name in ("title", "description", "album")
            if kwargs.get(field_name) is not None
        ]
        file_data = file_obj.read()
        file = File(name=filename, data=file_data, field_name="image")
        form = MultipartForm(
            fields=fields,
            files=[
                file,
            ],
        )

        data = bytes(form)

        headers = {
            "Content-Type": form.get_content_type(),
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

    def update(self, image_hash, **kwargs):
        url_path = f"/3/image/{image_hash}"

        fields = [
            Field(field_name=field_name, value=str(kwargs.get(field_name)))
            for field_name in ("title", "description", "album")
            if kwargs.get(field_name) is not None
        ]
        form = MultipartForm(fields=fields)

        data = bytes(form) or None

        headers = dict()
        if data:
            headers["Content-Type"] = form.get_content_type()
            headers["Content-length"] = str(len(data))
        headers.update(**self.get_auth_header())

        return self.make_request(
            url_path, data=data, headers=headers, method="POST"
        )

    def favorite(self, image_hash):
        url_path = f"/3/image/{image_hash}/favorite"

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

        return self.make_request(url_path, headers=headers, method="POST")

    def __call__(self, image_hash):
        return self.get_image(image_hash)
