import webbrowser
from datetime import datetime
from random import randint

from arzeka import check_payment, initiate_payment

dev_url = "https://pgw-test.faso-arzeka.com/AvepayPaymentGatewayUI/avepaypayment/app/"
prod_url = "https://pgw.faso-arzeka.com/AvepayPaymentGatewayUI/avepay-payment/app/"
test_token = "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI1UzNaOVQ4MzAxIiwiaWF0IjoxNzIwMDA4ODI5LCJzdWIiOiIyMjYwMDAwMDAxNiIsImlzcyI6ImFyemVrYSIsIlBBWUxPQUQiOiJhY2Nlc3NfdG9rZW4iLCJleHAiOjE3ODMwODA4Mjl9.BZRA8xd0nh_H8JfyTteXTrtmjPT2hWKmTsZavRYQSJoDFW97ik5rR5SyhLmTr9nzmDQ2MHA24qGbtgH9djK4Lg"

today = datetime.now()

trans_id = f"GCOB{(today.year)}{today.month}{today.day}.{today.hour}{today.minute}{today.second}.C{randint(5, 100000)}"


data = {
    "msisdn": 22664712648,
    "amount": 100,
    "merchantid": 1,
    "mappedOrderId": trans_id,
    "linkForUpdateStatus": "http://localhost:8000",
    "linkBackToCallingWebsite": "http://localhost:8000",
    "headers": {"user-agent": "gcob-decoration-payment"},
}

response = initiate_payment(test_token, dev_url, **data)

print(
    response.request.url,
    "\n\n\n",
    response.request.headers,
    "\n\n\n",
    response.request.body,
    "\n\n\n",
    response.text,
)
