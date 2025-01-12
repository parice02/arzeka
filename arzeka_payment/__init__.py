from arzeka.payment import ArzekaPayment


def initiate_payment(token, url, payment_data):
    pay = ArzekaPayment(token=token, url=url)
    return pay.initiate_payment(payment_data)


def check_payment(token, url, mappedOrderId):
    pay = ArzekaPayment(token=token, url=url)
    return pay.check_payment(mappedOrderId=mappedOrderId)
