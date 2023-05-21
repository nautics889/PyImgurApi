from .base_endpoint import BaseEndpoint
from ..utils import Field, MultipartForm


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

    def album_image(self, album_hash, image_hash):
        url_path = f"/3/album/{album_hash}/image/{image_hash}"

        headers = {
            "Content-Type": "application/json",
        }
        headers.update(**self.get_auth_header())

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
        possible_privacy_values = ("public", "hidden", "secret")
        if privacy is not None and privacy not in possible_privacy_values:
            raise ValueError(
                f"Inappropriate value for `privacy`: '{privacy}', "
                f"currently supported: {possible_privacy_values}"
            )
        possible_layout_reason = ("blog", "grid", "horizontal", "vertical")
        if layout is not None and layout not in possible_layout_reason:
            raise ValueError(
                f"Inappropriate value for `layout`: '{layout}', "
                f"currently supported: {possible_layout_reason}"
            )

        url_path = "/3/album"

        fields = list()
        if image_ids is not None:
            for image_id in image_ids:
                fields.append(Field(field_name="ids[]", value=image_id))
        if delete_hashes is not None:
            for delete_hash in delete_hashes:
                fields.append(
                    Field(field_name="deletehashes[]", value=delete_hash)
                )
        if title is not None:
            fields.append(Field(field_name="title", value=title))
        if description is not None:
            fields.append(Field(field_name="description", value=description))
        if privacy is not None:
            fields.append(Field(field_name="privacy", value=privacy))
        if cover is not None:
            fields.append(Field(field_name="cover", value=cover))
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
        possible_privacy_values = ("public", "hidden", "secret")
        if privacy is not None and privacy not in possible_privacy_values:
            raise ValueError(
                f"Inappropriate value for `privacy`: '{privacy}', "
                f"currently supported: {possible_privacy_values}"
            )
        possible_layout_reason = ("blog", "grid", "horizontal", "vertical")
        if layout is not None and layout not in possible_layout_reason:
            raise ValueError(
                f"Inappropriate value for `layout`: '{layout}', "
                f"currently supported: {possible_layout_reason}"
            )

        url_path = f"/3/album/{album_hash}"

        fields = list()
        if image_ids is not None:
            for image_id in image_ids:
                fields.append(Field(field_name="ids[]", value=image_id))
        if delete_hashes is not None:
            for delete_hash in delete_hashes:
                fields.append(
                    Field(field_name="deletehashes[]", value=delete_hash)
                )
        if title is not None:
            fields.append(Field(field_name="title", value=title))
        if description is not None:
            fields.append(Field(field_name="description", value=description))
        if privacy is not None:
            fields.append(Field(field_name="privacy", value=privacy))
        if cover is not None:
            fields.append(Field(field_name="cover", value=cover))
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

    def delete(self, album_hash):
        url_path = f"/3/album/{album_hash}"

        headers = {
            "Content-Type": "application/json",
        }
        headers.update(**self.get_auth_header())

        return self.make_request(url_path, headers=headers, method="DELETE")

    def favorite(self, album_hash):
        url_path = f"/3/album/{album_hash}/favorite"

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

        return self.make_request(url_path, headers=headers, method="POST")

    def set_images(self, album_hash, image_ids=None, delete_hashes=None):
        url_path = f"/3/album/{album_hash}"

        fields = list()
        if image_ids is not None:
            for image_id in image_ids:
                fields.append(Field(field_name="ids[]", value=image_id))
        if delete_hashes is not None:
            for delete_hash in delete_hashes:
                fields.append(
                    Field(field_name="deletehashes[]", value=delete_hash)
                )
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

    def add(self, album_hash, image_ids=None, delete_hashes=None):
        url_path = f"/3/album/{album_hash}/add"

        fields = list()
        if image_ids is not None:
            for image_id in image_ids:
                fields.append(Field(field_name="ids[]", value=image_id))
        if delete_hashes is not None:
            for delete_hash in delete_hashes:
                fields.append(
                    Field(field_name="deletehashes[]", value=delete_hash)
                )
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

    def remove_images(self, album_hash, image_ids):
        url_path = f"/3/album/{album_hash}/add"

        fields = list()
        for image_id in image_ids:
            fields.append(Field(field_name="ids[]", value=image_id))
        form = MultipartForm(fields=fields)

        data = bytes(form)

        headers = dict()
        if data:
            headers["Content-Type"] = form.get_content_type()
            headers["Content-length"] = str(len(data))
        headers.update(**self.get_auth_header())

        return self.make_request(
            url_path, data=data, headers=headers, method="POST"
        )

    def __call__(self, album_hash):
        return self.get_album(album_hash)
