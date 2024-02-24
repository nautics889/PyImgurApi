from unittest.mock import patch

from pyimgurapi.endpoints import Album
from pyimgurapi.utils import DynamicResponseData
from tests.utils import get_random_imgur_id


class TestAlbum:
    @patch("urllib.request.urlopen")
    def test_get_album(self, urlopen_mock, imgur_album_get_200_response):
        urlopen_mock.return_value = imgur_album_get_200_response
        album_id = (
            imgur_album_get_200_response.json().get("data", {}).get("id")
        )

        album = Album()
        res = album.get_album(album_id)

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "GET"
        assert album_id in urlopen_mock.call_args[0][0].full_url
        assert isinstance(res, DynamicResponseData)
        assert res.data.id == album_id

    @patch("urllib.request.urlopen")
    def test_create(
        self,
        urlopen_mock,
        imgur_album_post_200_response,
        title_fixture,
        description_fixture,
    ):
        urlopen_mock.return_value = imgur_album_post_200_response

        album = Album()
        res = album.create(
            title=title_fixture, description=description_fixture
        )

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "POST"
        assert urlopen_mock.call_args[0][0].full_url.endswith("/album")
        assert isinstance(res, DynamicResponseData)
        assert title_fixture in urlopen_mock.call_args[0][0].data.decode(
            "utf-8"
        )
        assert description_fixture in urlopen_mock.call_args[0][0].data.decode(
            "utf-8"
        )

    @patch("urllib.request.urlopen")
    def test_get_album_image(self, urlopen_mock, imgur_image_get_200_response):
        urlopen_mock.return_value = imgur_image_get_200_response
        album_id = get_random_imgur_id()
        image_id = (
            imgur_image_get_200_response.json().get("data", {}).get("id")
        )

        album = Album()
        res = album.album_image(album_id, image_id)

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "GET"
        assert f"album/{album_id}" in urlopen_mock.call_args[0][0].full_url
        assert f"image/{image_id}" in urlopen_mock.call_args[0][0].full_url
        assert isinstance(res, DynamicResponseData)
        assert res.data.id == image_id
