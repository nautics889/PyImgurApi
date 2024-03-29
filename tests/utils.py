import logging
import os.path
import random
import string

from jinja2 import Environment, FileSystemLoader

logger = logging.getLogger(__name__)

FIXTURES_DIR = "tests/fixtures"


def get_random_imgur_id():
    return "".join(
        random.choice(string.digits + string.ascii_letters) for _ in range(7)
    )


def get_random_imgur_digit_id(a=1 * 10**6, b=9.99 * 10**9):
    return str(random.randint(a, b))


def load_data_from_file(filename):
    try:
        with open(os.path.join(FIXTURES_DIR, filename)) as fp:
            return fp.read()
    except FileNotFoundError:
        logger.error(
            "Unable to read fixtures data from %s (`FIXTURES_DIR`: %s)",
            filename,
            FIXTURES_DIR,
        )
        raise


def get_template(template_name):
    env = Environment(
        loader=FileSystemLoader(os.path.join(FIXTURES_DIR, "templates"))
    )
    return env.get_template(template_name)
