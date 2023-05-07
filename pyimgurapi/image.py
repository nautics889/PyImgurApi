from pyimgurapi.base_endpoint import BaseEndpoint


class Image(BaseEndpoint):
    def get_image(self, image_hash, access_token=None):
        url_path = f"/3/image/{image_hash}"
        headers = {"Authorization": f"Bearer {access_token}"}
        return self.make_request(url_path, headers=headers)
