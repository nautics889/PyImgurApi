import json
import urllib.request
from urllib.parse import urljoin


class BaseEndpoint:
    base_url = "https://api.imgur.com/"

    def make_request(self, url_path, data=None, headers=None):
        url = urljoin(self.base_url, url_path)
        request = urllib.request.Request(
            url, data=json.dumps(data).encode("utf-8")
        )
        if isinstance(headers, dict):
            for header, value in headers.items():
                request.add_header(header, value)
        request.add_header("Content-Type", "application/json")

        response = urllib.request.urlopen(request)
        data = json.loads(response.read().decode("utf-8"))
        return data
