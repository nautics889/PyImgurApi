# PyImgurAPI

[![PyPI](https://img.shields.io/pypi/v/pyimgurapi.svg)](https://pypi.org/project/pyimgurapi/)
[![Python Version](https://img.shields.io/pypi/pyversions/pyimgurapi.svg)](https://pypi.org/project/pyimgurapi/)

A Python SDK for the Imgur API.

## Overview

The package is supposed to be in strict accordance with the [Imgur's documentation](https://apidocs.imgur.com/), i.e. description for any endpoint implemented in the SDK can also be found there.

The package does not have any third-party dependencies; it requires only Python 3.8+.

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

See the [contributing guidelines](CONTRIBUTING.md).

## License

[MIT](https://choosealicense.com/licenses/mit/)
