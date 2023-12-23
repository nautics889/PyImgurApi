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

### Running pre-commit

To install pre-commit hooks:

```bash
$ pre-commit install
```

Then you can run it manually:

```bash
$ pre-commit
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
