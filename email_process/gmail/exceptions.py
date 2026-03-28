class TokenExpiredError(RuntimeError):
    def __init__(self):
        super().__init__(
            "OAuth token has been expired or revoked. "
            "Delete token.json and re-run to authenticate again."
        )
