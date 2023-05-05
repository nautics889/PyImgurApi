from pyimgurapi.base_endpoint import BaseEndpoint


class Image(BaseEndpoint):

    def get_image(self, image_hash, token=None):
        url_path = f'/3/image/{image_hash}'
        headers = {'Authorization': f'Bearer {token}'}
        return self.make_request(url_path, headers=headers)
