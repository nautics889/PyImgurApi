from unittest.mock import patch

import pytest

from pyimgurapi.endpoints import Comment
from pyimgurapi.utils import EOL, DynamicResponseData
from tests.utils import get_random_imgur_id, get_random_imgur_digit_id


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
        assert isinstance(res, DynamicResponseData)
        assert res.data.id == comment_id

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
        assert isinstance(res, DynamicResponseData)
        passed_form_data = urlopen_mock.call_args[0][0].data.decode("utf-8")
        assert f"{EOL}{image_id}{EOL}" in passed_form_data
        assert f"{EOL}{description_fixture}{EOL}" in passed_form_data

    @patch("urllib.request.urlopen")
    def test_delete_comment(
        self, urlopen_mock, imgur_comment_delete_200_response
    ):
        urlopen_mock.return_value = imgur_comment_delete_200_response
        comment_id = (
            imgur_comment_delete_200_response.json().get("data", {}).get("id")
        )

        comment = Comment()
        res = comment.delete(comment_id)

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "DELETE"
        assert str(comment_id) in urlopen_mock.call_args[0][0].full_url
        assert isinstance(res, DynamicResponseData)

    @patch("urllib.request.urlopen")
    def test_get_replies(self, urlopen_mock, imgur_replies_get_200_response):
        urlopen_mock.return_value = imgur_replies_get_200_response
        comment_id = (
            imgur_replies_get_200_response.json().get("data", {}).get("id")
        )

        comment = Comment()
        res = comment.replies(comment_id)

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "GET"
        assert str(comment_id) in urlopen_mock.call_args[0][0].full_url
        assert isinstance(res, DynamicResponseData)

    @patch("urllib.request.urlopen")
    def test_create_reply(
        self,
        urlopen_mock,
        imgur_comment_post_200_response,
        description_fixture,
    ):
        urlopen_mock.return_value = imgur_comment_post_200_response
        image_id = get_random_imgur_id()
        comment_id = get_random_imgur_digit_id()

        comment = Comment()
        res = comment.create_reply(image_id, comment_id, description_fixture)

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "POST"
        assert isinstance(res, DynamicResponseData)
        assert comment_id in urlopen_mock.call_args[0][0].full_url
        passed_form_data = urlopen_mock.call_args[0][0].data.decode("utf-8")
        assert f"{EOL}{image_id}{EOL}" in passed_form_data
        assert f"{EOL}{description_fixture}{EOL}" in passed_form_data

    @pytest.mark.parametrize("vote_value", ["up", "down", "veto"])
    @patch("urllib.request.urlopen")
    def test_vote(self, urlopen_mock, imgur_common_200_response, vote_value):
        urlopen_mock.return_value = imgur_common_200_response
        comment_id = get_random_imgur_digit_id()

        comment = Comment()
        res = comment.vote(comment_id, vote_value)

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "POST"
        assert isinstance(res, DynamicResponseData)
        assert comment_id in urlopen_mock.call_args[0][0].full_url
        assert vote_value in urlopen_mock.call_args[0][0].full_url

    @patch("urllib.request.urlopen")
    def test_vote_unknown_value(
        self,
        urlopen_mock,
        imgur_common_200_response,
    ):
        urlopen_mock.return_value = imgur_common_200_response
        comment_id = get_random_imgur_digit_id()
        vote_value = "unknown"

        comment = Comment()
        with pytest.raises(ValueError):
            comment.vote(comment_id, vote_value)

        urlopen_mock.assert_not_called()

    @pytest.mark.parametrize("reason", ["1", "2", "3", "4", "5"])
    @patch("urllib.request.urlopen")
    def test_report(self, urlopen_mock, imgur_common_200_response, reason):
        urlopen_mock.return_value = imgur_common_200_response
        comment_id = get_random_imgur_digit_id()

        comment = Comment()
        res = comment.report(comment_id, reason)

        urlopen_mock.assert_called_once()
        assert urlopen_mock.call_args[0][0].method == "POST"
        assert isinstance(res, DynamicResponseData)
        assert comment_id in urlopen_mock.call_args[0][0].full_url
        passed_form_data = urlopen_mock.call_args[0][0].data.decode("utf-8")
        assert f"{EOL}{reason}{EOL}" in passed_form_data

    @patch("urllib.request.urlopen")
    def test_report_unknown_reason(
        self, urlopen_mock, imgur_common_200_response
    ):
        urlopen_mock.return_value = imgur_common_200_response
        comment_id = get_random_imgur_digit_id()
        reason = "999"

        comment = Comment()
        with pytest.raises(ValueError):
            comment.report(comment_id, reason)

        urlopen_mock.assert_not_called()
