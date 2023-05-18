from .base_endpoint import BaseEndpoint


class Album(BaseEndpoint):
    def get_album(self, album_hash):
        url_path = f"/3/album/{album_hash}"

        headers = {
            "Content-Type": "application/json",
        }
        headers.update(**self.get_auth_header())

        return self.make_request(url_path, headers=headers)

    def album_images(self, album_hash):
        url_path = f"/3/album/{album_hash}/images"

        headers = {
            "Content-Type": "application/json",
        }
        headers.update(**self.get_auth_header())

        return self.make_request(url_path, headers=headers)

    def __call__(self, album_hash):
        return self.get_album(album_hash)
