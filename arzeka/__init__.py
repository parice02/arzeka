from arzeka.payment import ArzekaPayment


def initiate_payment(token: str, url: str, payment_data: dict):
    """initialize payment

    Args:
        - token (str): your token obtained at arzeka
        - url (str): arzeka payment url
        - payment_data (dict): payment data:
            - msisdn (str): the customer phone number in international format without `+`
            - amount (int): transaction amount
            - merchantid (int): the merchant identifier
            - mappedOrderId (str): your own transaction ID
            - linkForUpdateStatus (str):
            - linkBackToCallingWebsite (str):

    Returns:
        _type_: _description_
    """
    pay = ArzekaPayment(token=token, url=url)
    return pay.initiate_payment(payment_data)


def check_payment(token: str, url: str, mappedOrderId: int):
    """_summary_

    Args:
        token (str): _description_
        url (str): _description_
        mappedOrderId (int): _description_

    Returns:
        _type_: _description_
    """
    pay = ArzekaPayment(token=token, url=url)
    return pay.check_payment(mappedOrderId=mappedOrderId)
