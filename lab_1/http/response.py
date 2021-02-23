class Response:
    def __init__(self, status, reason, headers={}, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body