import json
import random
import string

import pytest

from .utils import get_template, load_data_from_file


class ResponseFixture:
    FIXTURE_DIR = "tests/fixtures/"

    def __init__(self, status=200, reason="OK", content=b""):
        self.status = status
        self.reason = reason
        self.content = content

    def read(self):
        return self.content

    def json(self):
        return json.loads(self.content.decode("utf-8"))


@pytest.fixture
def imgur_image_get_200_response():
    template = get_template("imgur_image_get_200.json.j2")
    content = template.render(
        id="".join(
            random.choice(string.digits + string.ascii_letters)
            for _ in range(7)
        )
    ).encode("utf-8")
    return ResponseFixture(status=200, reason="OK", content=content)


@pytest.fixture
def imgur_image_post_200_response():
    template = get_template("imgur_image_post_200.json.j2")
    content = template.render(
        id="".join(
            random.choice(string.digits + string.ascii_letters)
            for _ in range(7)
        )
    ).encode("utf-8")
    return ResponseFixture(status=200, reason="OK", content=content)


@pytest.fixture
def general_json_dict():
    data = load_data_from_file("general_valid_json.json")
    return json.loads(data)
