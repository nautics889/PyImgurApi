from unittest.mock import patch, Mock

from pyimgurapi.endpoints import Image
from pyimgurapi.utils import DynamicResponseData
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
        assert isinstance(res, DynamicResponseData)
        assert res.data.id == img_id

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
        assert urlopen_mock.call_args[0][0].full_url.endswith("/upload")
        assert test_image in urlopen_mock.call_args[0][0].data
        assert isinstance(res, DynamicResponseData)

    @patch("urllib.request.urlopen")
    def test_delete(self, urlopen_mock, imgur_common_200_response):
        urlopen_mock.return_value = imgur_common_200_response
        img_id = get_random_imgur_id()

        image = Image()
        res = image.delete(img_id)

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "DELETE"
        assert img_id in urlopen_mock.call_args[0][0].full_url
        assert isinstance(res, DynamicResponseData)

    @patch("urllib.request.urlopen")
    def test_update(
        self,
        urlopen_mock,
        imgur_common_200_response,
        title_fixture,
        description_fixture,
    ):
        urlopen_mock.return_value = imgur_common_200_response
        img_id = get_random_imgur_id()

        image = Image()
        res = image.update(
            img_id, title=title_fixture, description=description_fixture
        )

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "POST"
        assert img_id in urlopen_mock.call_args[0][0].full_url
        assert (
            title_fixture.encode("utf-8") in urlopen_mock.call_args[0][0].data
        )
        assert (
            description_fixture.encode("utf-8")
            in urlopen_mock.call_args[0][0].data
        )
        assert isinstance(res, DynamicResponseData)

    @patch("urllib.request.urlopen")
    def test_favorite(self, urlopen_mock, imgur_common_200_response):
        urlopen_mock.return_value = imgur_common_200_response
        img_id = get_random_imgur_id()

        image = Image()
        res = image.favorite(img_id)

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "POST"
        assert urlopen_mock.call_args[0][0].full_url.endswith(
            f"{img_id}/favorite"
        )
        assert not urlopen_mock.call_args[0][0].data
        assert isinstance(res, DynamicResponseData)
