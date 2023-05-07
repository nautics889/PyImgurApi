import json
import logging
import urllib.request
from urllib.parse import urljoin

logger = logging.getLogger(__name__)


class BaseEndpoint:
    base_url = "https://api.imgur.com/"

    def make_request(self, url_path, data=None, headers=None):
        url = urljoin(self.base_url, url_path)

        request_object_params = dict()
        request_object_params.update(url=url)
        if data is not None:
            try:
                serialized_data = json.dumps(data).encode("utf-8")
            except TypeError:
                logger.error("")
                raise
            request_object_params.update(data=serialized_data)

        request = urllib.request.Request(**request_object_params)

        if isinstance(headers, dict):
            for header, value in headers.items():
                request.add_header(header, value)
        request.add_header("Content-Type", "application/json")

        response = urllib.request.urlopen(request)
        raw_response_data = response.read()
        json_response_data = json.loads(raw_response_data.decode("utf-8"))
        return json_response_data
