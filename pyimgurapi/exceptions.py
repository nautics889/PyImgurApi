class PyImgurApiError(Exception):
    def __init__(self, reason="", body=None, headers=None):
        super(PyImgurApiError, self).__init__(reason)
        self.reason = reason
        self.headers = headers
        self.body = body

    def __str__(self):
        return str(self.reason)


class PyImgurApiNotFound(PyImgurApiError):
    pass


class PyImgurApiUnauthorized(PyImgurApiError):
    pass


HTTP_CODES_ERRORS_MAP = {403: PyImgurApiUnauthorized, 404: PyImgurApiNotFound}
