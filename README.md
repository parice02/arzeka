# ARZEKA Mobile Money Payment API (Burkina Faso)

API non officiel pour les paiements mobiles le moyen de paiement ARZEKA au Burkina Faso


## Avant l'installation

1. Obtenir un compte API avec Arzeka Money (token, ....)
2. Installer les certificats fournis par l'opérateur s'il y'en a


## Dépendances

- python = "^3.9"
- requests = "^2.31.0"

## Installation

```bash
pip install git+https://github.com/parice02/arzeka.git # with pip
poetry add git+https://github.com/parice02/arzeka.git # with poetry
```


## Cas d'utilisation

### Exemple d'initialisation d'un paiement

```python
from arzeka import initiate_payment


token = "<Your arzeka token>"
api_url = "<arzeka API URL>"
msisdn = "<client phone number in international format without '+'>"
amount = "<payment amount>"
merchantid = "<the merchant id>"
mappedOrderId = "<ID for this transaction>"
linkForUpdateStatus = "<URL to call when transaction status change>"
linkBackToCallingWebsite = "<URL to call at the end of paiement process>"

# See Arzeka API document documentation for more detail


payment_data = {
    "msisdn": msisdn,
    "amount": amount,
    "merchantid": merchantid,
    "mappedOrderId": mappedOrderId,
    "linkForUpdateStatus": linkForUpdateStatus,
    "linkBackToCallingWebsite": linkBackToCallingWebsite,
}

response = initiate_payment(token, api_url, **data)
print(response)
```

### Exemple de vérification de paiement

## Contribution

Les contributions sont libres.


## Reste à faire

1. Implémenter des tests
2. Écrire une documentation
3. Publier sur pypi
