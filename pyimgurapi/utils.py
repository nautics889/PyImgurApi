import io
import itertools
import json
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


class DynamicResponseData:
    def __init__(self, source_dict, name="data"):
        self._source_dict = source_dict
        self._name = name

    def __getattr__(self, item):
        if isinstance(self._source_dict, (list, tuple)):
            raise AttributeError(
                f"'{self._name}' object represents an array, use the "
                f"subscript notation (`[]`)"
            )

        if item in self._source_dict:
            value = self._source_dict[item]
            if isinstance(value, (list, tuple, dict)):
                return self.__class__(self._source_dict[item], name=item)
            return value
        raise AttributeError(
            f"'{self._name}' object does not have '{item}' attribute"
        )

    def __getitem__(self, key):
        try:
            if isinstance(self._source_dict[key], (list, tuple, dict)):
                return self.__class__(
                    self._source_dict[key],
                    name=f"'{key}' item of '{self._name}'",
                )

            return self._source_dict[key]
        except IndexError as exc:
            raise IndexError(
                f"Unable to get item by index '{key}' of array '{self._name}'"
            ) from exc
        except AttributeError as exc:
            raise AttributeError(
                f"Unable to get item by key '{key}' of object '{self._name}'"
            ) from exc

    def __dir__(self):
        return itertools.chain(super().__dir__(), self._source_dict.keys())

    def __str__(self):
        return json.dumps(self._source_dict, indent=2)

    def __repr__(self):
        obj = f"{self.__class__.__module__}.{self.__class__.__name__}"
        attrs = f"name='{self._name}', content={json.dumps(self._source_dict)}"
        return f"<{obj} object at {hex(id(self))} ({attrs})>"

    def as_dict(self):
        return self._source_dict
