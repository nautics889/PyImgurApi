import io
import mimetypes
import uuid


# @TODO: consider dataclasses
class Field:
    def __init__(self, field_name, value):
        self.field_name = field_name
        self.value = value


class File:
    def __init__(self, name, data, field_name):
        self.name = name
        self.data = data
        self.field_name = field_name
        self.mimetype = (
            mimetypes.guess_type(name)[0] or "application/octet-stream"
        )


class MultipartForm:
    def __init__(self, fields=None, files=None):
        self.boundary = uuid.uuid4().hex
        self.fields = fields or []
        self.files = files or []

    def __bytes__(self):
        buffer = io.BytesIO()

        boundary_bytes = b"".join(
            (b"--", self.boundary.encode("utf-8"), b"\r\n")
        )

        for field in self.fields:
            buffer.write(boundary_bytes)
            buffer.write("Content-Disposition: form-data; ".encode("utf-8"))
            buffer.write(f'name="{field.field_name}"\r\n'.encode("utf-8"))
            buffer.write(b"\r\n")
            buffer.write(field.value.encode("utf-8"))
            buffer.write(b"\r\n")

        for file in self.files:
            buffer.write(boundary_bytes)
            buffer.write("Content-Disposition: form-data; ".encode("utf-8"))
            buffer.write(
                f'name="{file.field_name}"; filename="{file.name}"\r\n'.encode(
                    "utf-8"
                )
            )
            buffer.write(b"\r\n")
            buffer.write(file.data)
            buffer.write(b"\r\n")
            buffer.write(boundary_bytes)

        return buffer.getvalue()

    def get_content_type(self):
        return f"multipart/form-data; boundary={self.boundary}"
