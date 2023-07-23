# PyImgurAPI

[![PyPI](https://img.shields.io/pypi/v/pyimgurapi.svg)](https://pypi.org/project/pyimgurapi/)
[![Python Version](https://img.shields.io/pypi/pyversions/pyimgurapi.svg)](https://pypi.org/project/pyimgurapi/)

A Python SDK for the Imgur API.

## Overview
The package is supposed to be in strict accordance with the [Imgur's documentation](https://apidocs.imgur.com/), i.e. description for any endpoint implemented in the SDK can also be found there.

The package does not have any third-party dependencies; it requires only Python 3.7+.

### Alternatives:
* [PyImgur](https://github.com/Damgaard/PyImgur) was originally an official client for Imgur, but it seems to be deprecated now.
* [imgur-python](https://github.com/faustocarrera/imgur-python) a relevant unofficial SDK for Imgur.

## Installation

Using pip:

```bash
$ pip install pyimgurapi
```

## First authentication

1. [Register your application](https://api.imgur.com/oauth2/addclient) to get `client_id` and `client_secret`.
2. Open the next URL in a browser:
`https://api.imgur.com/oauth2/authorize?client_id=<your_client_id>&response_type=token`
_(replace `<your_client_id>` with the actual ID)_
3. Allow authentication for a client.
4. Copy the `refresh_token` value from the URL field.
5. Then you can authenticate your client:
```python
from pyimgurapi import ImgurAPI


api = ImgurAPI(
    refresh_token="<refresh_token>",
    client_id="<client_id>",
    client_secret="<client_secret>",
)
api.auth()
```
## Basic usage
Getting info about an image:
```python
from pyimgurapi import ImgurAPI


api = ImgurAPI(
    refresh_token="<refresh_token>",
    client_id="<client_id>",
    client_secret="<client_secret>",
)
api.auth()

meme_image = api.image.get_image("6yHmlwT")
```
Then you can access attributes of the response using a dot-notation:
```python
print(meme_image.data.link)
```
or using a subscript-notation:
```python
print(meme_image["data"]["link"])
```
Uploading a new image:
```python
from pyimgurapi import ImgurAPI


api = ImgurAPI(
    refresh_token="<refresh_token>",
    client_id="<client_id>",
    client_secret="<client_secret>",
)
api.auth()

filename = "cat1.jpg"
with open(filename, 'rb') as f:
    new_image = api.image.upload(
        f,
        filename,
        title="New image",  # optional
        description="Absolutely new image"  # optional
    )
```
Then you can access attributes of the new image as well:
```python
print(new_image.data.link)
```

## Contributing

Pull requests are always welcome. For major changes, please open an issue first
to discuss what you would like to implement/change.

### Set up the development environment

1. _(Preferred)_ Install [poetry](https://python-poetry.org/docs/#installation).
2. Install development dependencies:
```bash
$ poetry install --with dev
```

### Running tests
```bash
$ poetry run pytest
```

### Linting and formatting

Formatting your code with black:
```bash
$ black . --line-length 79
```
Linting with flake8:
```bash
$ poetry run flake8 . --max-doc-length 72 --show-source
```

## Roadmap

Here's a table which illustrates current progress of endpoints implementation:

| Endpoint                                                                                           | Implementation | Tests       | Documentation |
|:---------------------------------------------------------------------------------------------------|:---------------|:------------|:--------------|
| [Account](https://api.imgur.com/endpoints/account)                                                 | In progress    | In progress | In progress   |
| [Album](https://api.imgur.com/endpoints/album)                                                     | Done ✓         | Not impl.   | Not impl.     |
| [Comment](https://api.imgur.com/endpoints/comment)                                                 | Done ✓         | Done ✓      | In progress   |
| Feed                                                                                               | Not impl.      | Not impl.   | Not impl.     |
| [Gallery](https://api.imgur.com/endpoints/gallery)                                                 | Not impl.      | Not impl.   | Not impl.     |
| [Image](https://api.imgur.com/endpoints/image)                                                     | Done ✓         | Done ✓      | Done ✓        |
| [Memegen](https://api.imgur.com/endpoints/memegen)                                                 | Not impl.      | Not impl.   | Not impl.     |
| [Notification](https://api.imgur.com/endpoints/notification)                                       | Not impl.      | Not impl.   | Not impl.     |

Additionally, there are some preferable features that would be great to implement in the package:
* Method for bulk uploading images (e.g. from directory).
* Pagination with `__next__()` in some methods of `Account` endpoint.

## License

[MIT](https://choosealicense.com/licenses/mit/)
