from .base_endpoint import BaseEndpoint
from ..form_factories import get_album_form


class Album(BaseEndpoint):
    def get_album(self, album_hash):
        url_path = f"/3/album/{album_hash}"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def album_images(self, album_hash):
        url_path = f"/3/album/{album_hash}/images"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def album_image(self, album_hash, image_hash):
        url_path = f"/3/album/{album_hash}/image/{image_hash}"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers)

    def create(
        self,
        image_ids=None,
        delete_hashes=None,
        title=None,
        description=None,
        privacy=None,
        layout=None,
        cover=None,
    ):
        url_path = "/3/album"

        form = get_album_form(
            image_ids=image_ids,
            delete_hashes=delete_hashes,
            title=title,
            description=description,
            privacy=privacy,
            layout=layout,
            cover=cover,
        )

        headers = self.get_headers(form=form)

        return self.make_request(
            url_path, data=bytes(form) or None, headers=headers, method="POST"
        )

    def update(
        self,
        album_hash,
        image_ids=None,
        delete_hashes=None,
        title=None,
        description=None,
        privacy=None,
        layout=None,
        cover=None,
    ):
        url_path = f"/3/album/{album_hash}"

        form = get_album_form(
            image_ids=image_ids,
            delete_hashes=delete_hashes,
            title=title,
            description=description,
            privacy=privacy,
            layout=layout,
            cover=cover,
        )

        headers = self.get_headers(form=form)

        return self.make_request(
            url_path, data=bytes(form) or None, headers=headers, method="POST"
        )

    def delete(self, album_hash):
        url_path = f"/3/album/{album_hash}"

        headers = {
            "Content-Type": "application/json",
        }
        headers.update(**self.get_headers())

        return self.make_request(url_path, headers=headers, method="DELETE")

    def favorite(self, album_hash):
        url_path = f"/3/album/{album_hash}/favorite"

        headers = self.get_headers()

        return self.make_request(url_path, headers=headers, method="POST")

    def set_images(self, album_hash, image_ids=None, delete_hashes=None):
        url_path = f"/3/album/{album_hash}"

        form = get_album_form(image_ids=image_ids, delete_hashes=delete_hashes)

        headers = self.get_headers(form=form)

        return self.make_request(
            url_path, data=bytes(form) or None, headers=headers, method="POST"
        )

    def add(self, album_hash, image_ids=None, delete_hashes=None):
        url_path = f"/3/album/{album_hash}/add"

        form = get_album_form(image_ids=image_ids, delete_hashes=delete_hashes)

        headers = self.get_headers(form=form)

        return self.make_request(
            url_path, data=bytes(form) or None, headers=headers, method="POST"
        )

    def remove_images(self, album_hash, image_ids):
        url_path = f"/3/album/{album_hash}/remove_images"

        form = get_album_form(image_ids=image_ids)

        headers = self.get_headers(form=form)

        return self.make_request(
            url_path, data=bytes(form) or None, headers=headers, method="POST"
        )

    def __call__(self, album_hash):
        return self.get_album(album_hash)
