from unittest.mock import patch

from pyimgurapi.endpoints import Comment
from tests.utils import get_random_imgur_id


class TestComment:
    @patch("urllib.request.urlopen")
    def test_get_comment(self, urlopen_mock, imgur_comment_get_200_response):
        urlopen_mock.return_value = imgur_comment_get_200_response
        comment_id = (
            imgur_comment_get_200_response.json().get("data", {}).get("id")
        )

        comment = Comment()
        res = comment.get_comment(comment_id)

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "GET"
        assert str(comment_id) in urlopen_mock.call_args[0][0].full_url
        assert isinstance(res, dict)
        assert res.get("data", {}).get("id") == comment_id

    @patch("urllib.request.urlopen")
    def test_post_comment(
        self,
        urlopen_mock,
        imgur_comment_post_200_response,
        description_fixture,
    ):
        urlopen_mock.return_value = imgur_comment_post_200_response
        image_id = get_random_imgur_id()

        comment = Comment()
        res = comment.create(image_id, description_fixture)

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "POST"
        assert isinstance(res, dict)
        assert image_id in urlopen_mock.call_args[0][0].data.decode("utf-8")
        assert description_fixture in urlopen_mock.call_args[0][0].data.decode(
            "utf-8"
        )
