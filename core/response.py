class APIResponse:
    def __init__(self, response):
        self._response = response

    @property
    def status(self):
        return self._response.status_code

    @property
    def body(self):
        return self._response.json()

    @property
    def data(self):
        return self.body.get("data")

    def json(self):
        return self.body