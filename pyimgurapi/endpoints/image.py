from .base_endpoint import BaseEndpoint
from ..utils import FileForm


class Image(BaseEndpoint):
    def get_image(self, image_hash):
        url_path = f"/3/image/{image_hash}"

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

        return self.make_request(url_path, headers=headers)

    def upload(self, file, filename):
        url_path = "/3/upload"

        file_form = FileForm(filelike_object=file, filename=filename)

        data = bytes(file_form)

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": file_form.get_content_type(),
            "Content-length": str(len(data)),
        }

        return self.make_request(
            url_path, data=data, headers=headers, method="POST"
        )

    def delete(self, image_hash):
        url_path = f"/3/image/{image_hash}"

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

        return self.make_request(url_path, headers=headers, method="DELETE")

    def __call__(self, image_hash):
        return self.get_image(image_hash)
