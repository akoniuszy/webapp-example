
class EmbedConfig:

    tokenId = None
    accessToken = None
    tokenExpiry = None
    reportConfig = None

    def __init__(self, token_id, access_token, token_expiry, report_config):
        self.tokenId = token_id
        self.accessToken = access_token
        self.tokenExpiry = token_expiry
        self.reportConfig = report_config