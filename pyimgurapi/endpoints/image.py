from .base_endpoint import BaseEndpoint
from ..form_factories import get_image_form


class Image(BaseEndpoint):
    def get_image(self, image_hash):
        url_path = f"/{self.api_version}/image/{image_hash}"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def upload(
        self, file_obj, filename, title=None, description=None, album=None
    ):
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
        url_path = f"/{self.api_version}/image/{image_hash}"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers, method="DELETE")

    def update(self, image_hash, title=None, description=None, album=None):
        url_path = f"/{self.api_version}/image/{image_hash}"

        form = get_image_form(
            title=title, description=description, album=album
        )

        headers = self.get_headers(form=form)

        return self.make_request(
            url_path, data=bytes(form) or None, headers=headers, method="POST"
        )

    def favorite(self, image_hash):
        url_path = f"/{self.api_version}/image/{image_hash}/favorite"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers, method="POST")

    def __call__(self, image_hash):
        return self.get_image(image_hash)
