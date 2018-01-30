import base64

from braintreehttp import Environment


class PayPalEnvironment(Environment):

    LIVE = "https://api.paypal.com"
    SANDBOX = "https://api.sandbox.paypal.com"

    def __init__(self, client_id, client_secret, mode):
        super(PayPalEnvironment, self).__init__(mode)
        self.client_id = client_id
        self.client_secret = client_secret
        self.web_url = mode.replace('api', 'www')

    def authorization_string(self):
        return "Basic {0}".format(base64.b64encode((self.client_id + ":" + self.client_secret).encode()).decode())


class SandboxEnvironment(PayPalEnvironment):

    def __init__(self, client_id, client_secret):
        super(SandboxEnvironment, self).__init__(client_id, client_secret, PayPalEnvironment.SANDBOX)


class LiveEnvironment(PayPalEnvironment):

    def __init__(self, client_id, client_secret):
        super(LiveEnvironment, self).__init__(client_id, client_secret, PayPalEnvironment.LIVE)
