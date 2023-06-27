import json

import faker
import pytest

from .utils import get_template, load_data_from_file, get_random_imgur_id


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
def imgur_common_200_response():
    content = load_data_from_file("common_200_response.json").encode("utf-8")
    return ResponseFixture(status=200, reason="OK", content=content)


@pytest.fixture
def imgur_image_get_200_response():
    template = get_template("imgur_image_get_200.json.j2")
    content = template.render(id=get_random_imgur_id()).encode("utf-8")
    return ResponseFixture(status=200, reason="OK", content=content)


@pytest.fixture
def imgur_image_post_200_response():
    template = get_template("imgur_image_post_200.json.j2")
    content = template.render(id=get_random_imgur_id()).encode("utf-8")
    return ResponseFixture(status=200, reason="OK", content=content)


@pytest.fixture
def imgur_comment_get_200_response():
    template = get_template("imgur_comment_get_200.json.j2")
    content = template.render(
        album_cover_id=get_random_imgur_id(), image_id=get_random_imgur_id()
    ).encode("utf-8")
    return ResponseFixture(status=200, reason="OK", content=content)


@pytest.fixture
def imgur_comment_post_200_response():
    template = get_template("imgur_comment_post_200.json.j2")
    content = template.render().encode("utf-8")
    return ResponseFixture(status=200, reason="OK", content=content)


@pytest.fixture
def imgur_comment_delete_200_response():
    template = get_template("imgur_comment_delete_200.json.j2")
    content = template.render().encode("utf-8")
    return ResponseFixture(status=200, reason="OK", content=content)


@pytest.fixture
def imgur_replies_get_200_response():
    fake = faker.Faker()
    template = get_template("imgur_comment_replies_get.json.j2")
    content = template.render(
        album_cover=get_random_imgur_id(),
        username=fake.user_name(),
        image_id=get_random_imgur_id(),
    ).encode("utf-8")
    return ResponseFixture(status=200, reason="OK", content=content)


@pytest.fixture
def general_json_dict():
    data = load_data_from_file("general_valid_json.json")
    return json.loads(data)


@pytest.fixture
def test_image():
    with open("tests/fixtures/assets/cat1.jpg", "rb") as image:
        return image.read()


@pytest.fixture
def title_fixture():
    fake = faker.Faker()
    return " ".join(fake.words(2)).capitalize()


@pytest.fixture
def description_fixture():
    fake = faker.Faker()
    return fake.text()
