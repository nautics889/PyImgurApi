import json
from unittest.mock import patch

import pytest

from pyimgurapi.endpoints.base_endpoint import BaseEndpoint


class TestBaseEndpoint:
    @patch("urllib.request.urlopen")
    def test_make_request_get(
        self, urlopen_mock, imgur_image_get_200_response
    ):
        urlopen_mock.return_value = imgur_image_get_200_response

        base_endpoint = BaseEndpoint()
        res = base_endpoint.make_request("/test/url")

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "GET"
        assert urlopen_mock.call_args[0][0].full_url.endswith("/test/url")
        assert res == imgur_image_get_200_response.json()

    @patch("urllib.request.urlopen")
    def test_make_request_post_valid_dict_payload(
        self, urlopen_mock, imgur_image_post_200_response, general_json_dict
    ):
        urlopen_mock.return_value = imgur_image_post_200_response

        base_endpoint = BaseEndpoint()
        res = base_endpoint.make_request(
            "/test/url", data=general_json_dict, method="POST"
        )

        urlopen_mock.assert_called_once()
        passed_request = urlopen_mock.call_args[0][0]
        assert passed_request.method == "POST"
        assert passed_request.full_url.endswith("/test/url")
        assert json.loads(passed_request.data.decode()) == general_json_dict
        assert res == imgur_image_post_200_response.json()

    @patch("urllib.request.urlopen")
    def test_make_request_post_invalid_type_payload(
        self, urlopen_mock, imgur_image_post_200_response, general_json_dict
    ):
        urlopen_mock.return_value = imgur_image_post_200_response
        invalid_type_data = ...

        base_endpoint = BaseEndpoint()
        with pytest.raises(TypeError):
            base_endpoint.make_request(
                "/test/url", data=invalid_type_data, method="POST"
            )

        urlopen_mock.assert_not_called()
