import base64

import requests  # TODO replace with urllib3


class BasePayment(object):
    """ """

    def __init__(self, token: str = ""):
        if token is None or not isinstance(token, str):
            raise ValueError("value 'token' must be type of 'str'")

        self._token = token

    def headers(self):
        return {
            "content-type": "application/json",
            "user-agent": "app-payment",
            "accept-language": "en-GB,fr-FR;q=0.8,fr;q=0.6,en;q=0.4",
        }

    def post(self, url, **kwargs) -> requests.Response:
        headers = kwargs.pop("headers", {})
        headers_ = self.headers()
        headers_.update(headers)

        response = requests.post(url, headers=headers_, json=kwargs)

        return response

    def get(self, url, **kwargs) -> requests.Response:
        headers = kwargs.pop("headers", {})
        headers_ = self.headers()
        headers_.update(headers)

        response = requests.get(url, headers=headers_, params=kwargs)
        return response

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value: str):
        self._token = value

    @token.deleter
    def token(self):
        del self._token


class ArzekaPayment(BasePayment):
    def __init__(self, token: str, url: str = ""):
        super().__init__(token)

        if not isinstance(url, str):
            raise ValueError("value 'url' must be type of 'str'")

        self._url = url if url.endswith("/") else url + "/"

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value: str):
        self._url = value

    @url.deleter
    def url(self):
        del self._url

    def initiate_payment(self, payment_data: dict):
        if not set(
            [
                "msisdn",
                "amount",
                "merchantid",
                "mappedOrderId",
                "linkForUpdateStatus",
                "linkBackToCallingWebsite",
            ]
        ).issubset(set(payment_data.keys())):
            raise KeyError("you must give all parameters ")

        payment_data.update(
            {
                "securedAccessToken": self.token,
                "linkForUpdateStatus": str(
                    base64.urlsafe_b64encode(
                        bytes(payment_data.get("linkForUpdateStatus"), encoding="utf8")
                    )
                ),
                "linkBackToCallingWebsite": str(
                    base64.urlsafe_b64encode(
                        bytes(
                            payment_data.get("linkBackToCallingWebsite"),
                            encoding="utf8",
                        )
                    )
                ),
            }
        )

        return self.get(self.url + "validorder", **payment_data)

    def check_payment(self, mappedOrderId):
        kwargs = {"headers": {"authorization": self.token}}

        return self.post(
            self.url
            + "getThirdPartyMapInfo?mappedOrderId=%(value)s" % (mappedOrderId,),
            kwargs=kwargs,
        )
