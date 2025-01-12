from arzeka.payment import ArzekaPayment


def initiate_payment(token: str, url: str, payment_data: dict):
    pay = ArzekaPayment(token=token, url=url)
    return pay.initiate_payment(payment_data)


def check_payment(token: str, url: str, mappedOrderId: int):
    pay = ArzekaPayment(token=token, url=url)
    return pay.check_payment(mappedOrderId=mappedOrderId)
