from arzeka.payment import ArzekaPayment


def initiate_payment(token, url, **kwargs):
    pay = ArzekaPayment(token=token, url=url)
    return pay.initiate_payment(**kwargs)


def check_payment(token, url, mappedOrderId):
    pay = ArzekaPayment(token=token, url=url)
    return pay.check_payment(mappedOrderId=mappedOrderId)
