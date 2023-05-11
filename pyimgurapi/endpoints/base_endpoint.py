import json
import logging
import urllib.error
import urllib.request
from urllib.parse import urljoin

from ..exceptions import HTTP_CODES_ERRORS_MAP

logger = logging.getLogger(__name__)


class BaseEndpoint:
    base_url = "https://api.imgur.com/"

    def __init__(self, client_id=None, access_token=None):
        self.client_id = client_id
        self.access_token = access_token

    def get_auth_header(self):
        if self.access_token:
            return {"Authorization": f"Bearer {self.access_token}"}
        return {"Authorization": f"Client-ID {self.access_token}"}

    def make_request(self, url_path, data=None, headers=None, method="GET"):
        url = urljoin(self.base_url, url_path)

        request_object_params = dict()
        request_object_params.update(url=url)
        if isinstance(data, dict):
            try:
                serialized_data = json.dumps(data).encode("utf-8")
            except TypeError:
                logger.error(f"Invalid data passed: {data}")
                raise
            request_object_params.update(data=serialized_data)
        elif isinstance(data, bytes):
            request_object_params.update(data=data)
        elif data is not None:
            raise TypeError(
                f"Invalid type of `data` parameter: "
                f"{data.__class__.__module__}.{data.__class__.__name__}; "
                f"Expected bytes or dict."
            )
        request_object_params.update(method=method)

        request = urllib.request.Request(**request_object_params)

        if isinstance(headers, dict):
            for header, value in headers.items():
                request.add_header(header, value)

        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            if e.code in HTTP_CODES_ERRORS_MAP:
                raise HTTP_CODES_ERRORS_MAP[e.code](e.reason)
            raise e
        raw_response_data = response.read()
        json_response_data = json.loads(raw_response_data.decode("utf-8"))
        return json_response_data
