from pyimgurapi.base_endpoint import BaseEndpoint
from pyimgurapi.utils import FileForm


class Image(BaseEndpoint):
    def get_image(self, image_hash, access_token=None):
        url_path = f"/3/image/{image_hash}"

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        return self.make_request(url_path, headers=headers)

    def upload(self, access_token, file, filename):
        url_path = "/3/upload"

        file_form = FileForm(filelike_object=file, filename=filename)

        data = bytes(file_form)

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": file_form.get_content_type(),
            "Content-length": str(len(data)),
        }

        return self.make_request(url_path, data=data, headers=headers)

    def __call__(self, image_hash, access_token):
        return self.get_image(image_hash, access_token=access_token)
