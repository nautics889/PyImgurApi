from unittest.mock import patch, Mock

from pyimgurapi.endpoints import Image
from tests.utils import get_random_imgur_id


class TestImage:
    @patch("urllib.request.urlopen")
    def test_get_image(self, urlopen_mock, imgur_image_get_200_response):
        urlopen_mock.return_value = imgur_image_get_200_response
        img_id = imgur_image_get_200_response.json().get("data", {}).get("id")

        image = Image()
        res = image.get_image(img_id)

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "GET"
        assert img_id in urlopen_mock.call_args[0][0].full_url
        assert isinstance(res, dict)
        assert res.get("data", {}).get("id") == img_id

    @patch("urllib.request.urlopen")
    def test_upload(
        self, urlopen_mock, imgur_image_post_200_response, test_image
    ):
        urlopen_mock.return_value = imgur_image_post_200_response
        image_file = Mock()
        image_file.read.return_value = test_image

        image = Image()
        res = image.upload(image_file, "test_img.jpg")

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "POST"
        assert urlopen_mock.call_args[0][0].full_url.endswith("/3/upload")
        assert test_image in urlopen_mock.call_args[0][0].data
        assert isinstance(res, dict)

    @patch("urllib.request.urlopen")
    def test_delete(self, urlopen_mock, imgur_common_200_response):
        urlopen_mock.return_value = imgur_common_200_response
        img_id = get_random_imgur_id()

        image = Image()
        res = image.delete(img_id)

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "DELETE"
        assert img_id in urlopen_mock.call_args[0][0].full_url
        assert isinstance(res, dict)
