import io
import mimetypes
import uuid

ENCODING = "utf-8"
EOL = "\r\n"


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
            (b"--", self.boundary.encode(ENCODING), EOL.encode(ENCODING))
        )

        for field in self.fields:
            buffer.write(boundary_bytes)
            buffer.write("Content-Disposition: form-data; ".encode(ENCODING))
            buffer.write(f'name="{field.field_name}"{EOL}'.encode(ENCODING))
            buffer.write(EOL.encode(ENCODING))
            buffer.write(field.value.encode(ENCODING))
            buffer.write(EOL.encode(ENCODING))

        for file in self.files:
            buffer.write(boundary_bytes)
            buffer.write("Content-Disposition: form-data; ".encode(ENCODING))
            buffer.write(f'name="{file.field_name}"; '.encode(ENCODING))
            buffer.write(f'filename="{file.name}"{EOL}'.encode(ENCODING))
            buffer.write(EOL.encode(ENCODING))
            buffer.write(file.data)
            buffer.write(EOL.encode(ENCODING))
            buffer.write(boundary_bytes)

        return buffer.getvalue()

    def get_content_type(self):
        return f"multipart/form-data; boundary={self.boundary}"
