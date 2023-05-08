import io
import mimetypes
import uuid


class FileForm:
    def __init__(self, filelike_object, filename=None, fieldname="image"):
        self.boundary = uuid.uuid4().hex
        self.file_data = filelike_object.read()
        self.filename = filename
        if filename:
            self.mimetype = (
                mimetypes.guess_type(filename)[0] or "application/octet-stream"
            )
        self.fieldname = fieldname

    def __bytes__(self):
        buffer = io.BytesIO()

        boundary_bytes = b"".join(
            (b"--", self.boundary.encode("utf-8"), b"\r\n")
        )

        buffer.write(boundary_bytes)
        buffer.write("Content-Disposition: form-data; ".encode("utf-8"))
        buffer.write(
            f'name="{self.fieldname}"; filename="{self.filename}"\r\n'.encode(
                "utf-8"
            )
        )
        buffer.write(b"\r\n")
        buffer.write(self.file_data)
        buffer.write(b"\r\n")
        buffer.write(boundary_bytes)

        return buffer.getvalue()

    def get_content_type(self):
        return f"multipart/form-data; boundary={self.boundary}"
