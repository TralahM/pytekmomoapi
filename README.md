
[![Build Status](https://travis-ci.com/TralahM/pytekmomoapi.svg?branch=master)](https://travis-ci.com/TralahM/pytekmomoapi)
[![Build status](https://ci.appveyor.com/api/projects/status/yvvmq5hyf7hj743a/branch/master?svg=true)](https://ci.appveyor.com/project/TralahM/pytekmomoapi/branch/master)
[![Documentation Status](https://readthedocs.org/projects/pytekmomoapi/badge/?version=latest)](https://pytekmomoapi.readthedocs.io/en/latest/?badge=latest)
[![License: GPLv3](https://img.shields.io/badge/License-GPLV2-green.svg)](https://opensource.org/licenses/GPLV2)
[![Organization](https://img.shields.io/badge/Org-TralahTek-blue.svg)](https://github.com/TralahTek)
[![Views](http://hits.dwyl.io/TralahM/pytekmomoapi.svg)](http://dwyl.io/TralahM/pytekmomoapi)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat-square)](https://github.com/TralahM/pytekmomoapi/pull/)
[![GitHub pull-requests](https://img.shields.io/badge/Issues-pr-red.svg?style=flat-square)](https://github.com/TralahM/pytekmomoapi/pull/)
[![Language](https://img.shields.io/badge/Language-python-3572A5.svg)](https://github.com/TralahM)
<img title="Watching" src="https://img.shields.io/github/watchers/TralahM/pytekmomoapi?label=Watchers&color=blue&style=flat-square">
<img title="Stars" src="https://img.shields.io/github/stars/TralahM/pytekmomoapi?color=red&style=flat-square">
<img title="Forks" src="https://img.shields.io/github/forks/TralahM/pytekmomoapi?color=green&style=flat-square">

# pytekmomoapi.

An Opinionated Python SDK for the for the MTN Mobile Money API.
The goal of this SDK library is to enable python developers implement
MTN Mobile Money APIs in a flexible, yet consistent manner.

The Open API is a JSON REST API that is used by Partner systems to access services in the Wallet platform.
The Open API exposes services that are used by e.g. online merchants for managing payments and other financial services.

[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-black.svg?style=for-the-badge&logo=github)](https://github.com/TralahTek)
[![TralahM](https://img.shields.io/badge/Engineer-TralahM-blue.svg?style=for-the-badge&logo=github)](https://github.com/TralahM)
[![TralahM](https://img.shields.io/badge/Maintainer-TralahM-green.svg?style=for-the-badge&logo=github)](https://github.com/TralahM)

# Documentation
More Documentation can be found on readthedocs below:


[![Documentation](https://img.shields.io/badge/Docs-pytekmomoapi-blue.svg?style=for-the-badge)](https://pytekmomoapi.readthedocs.io)

# How to Install
```bash
# In terminal do:
$ pip install pytekmomoapi
```

## Building from Source for Developers

```console
$ git clone https://github.com/TralahM/pytekmomoapi.git
$ cd pytekmomoapi
$ python setup.py install
```

Quickstart
==========

Installation
------------

``` console
pip install pytekmomoapi
```

Sandbox User Provisioning
-------------------------

We have provided a convenient function,
`tekmomoapi.get_user_id_and_api_key` , to help you
quickly provision and get the required credentials i.e the **user_id**
and **apiKey** on the sandbox environment.

The Library also provided a utility function to get a random
`uuid.uuid4` string, this is quite useful because the
remote Momo Developer API heavily uses uuid4s for identification and
referencing, i.e during user provisioning, financial transactions, party
identification and referencing. The function
`tekmomoapi.get_random_uuid_str` provides that
convenience.

This reduces the amount of boilerplate code that would be otherwise
required.

### Example

``` python
import tekmomoapi
creds=dict(
   collection_subscription_key="3265aef9928c259a31b44faf812dc2da",
   remittance_subscription_key="928c259a31b44faf812dc2da3265aef9",
   disbursement_subscription_key="31b44faf812dc2da928c259a3265aef9",
)
cuser = tekmomoapi.get_user_id_and_api_key(
    creds.get("collection_subscription_key"))

duser = tekmomoapi.get_user_id_and_api_key(
    creds.get("disbursement_subscription_key"))

user = tekmomoapi.get_user_id_and_api_key(
   creds.get("remittance_subscription_key"))
```

```python
    user = tekmomoapi.get_user_id_and_api_key(creds.get("remittance_subscription_key"))
    print(user)
    {'user_id': 'fcbf0091-2dbe-4f37-9131-46a2a0dcda9e', 'apiKey': 'cb196acfa75b4bf1858b5dccdbb605a6'}
```

Authentication and Authorization
--------------------------------

OAuth Token is generated from the merchants' API Key and Secret. The API
Key and API Secret can be obtained through the provisioning API in
Sandbox.

We have built-in the authentication and authorization processes so you
dont have to worry about base64 encodings, whether to user Bearer or
Basic Authentication, enabling you to focus on more important details
i.e your business logic implementation and other more fun stuff.

You can obtain the authentication header string anytime if you wish to
do so by using the top level `tekmomoapi.scaffold.BaseAPI`{.pycode
.python} and its subclassess
`tekmomoapi.scaffold.BaseAPI.basic_auth_str` or the
`tekmomoapi.scaffold.BaseAPI.bearer_auth_str` property
methods.

### Example

``` python
RemAPI = tekmomoapi.RemittanceAPI(
    creds.get("remittance_subscription_key"),
    base_url=tekmomoapi.SANDBOX_BASE_URL,
    **user,
)
DisAPI = tekmomoapi.DisbursementAPI(
    creds.get("disbursement_subscription_key"),
    base_url=tekmomoapi.SANDBOX_BASE_URL,
    **duser,
)
ColAPI = tekmomoapi.CollectionAPI(
    creds.get("collection_subscription_key"),
    base_url=tekmomoapi.SANDBOX_BASE_URL,
    **cuser,
)
print("Remittance Basic Auth str: ",RemAPI.basic_auth_str)
print("Collection Bearer Auth str: ",ColAPI.bearer_auth_str)
print("Disbursement Basic Auth str: ",DisAPI.basic_auth_str)
print("Disbursement Bearer Auth str: ",DisAPI.bearer_auth_str)
```

Account Balance and Account Holder Validation
---------------------------------------------

All Subclasses of `tekmomoapi.scaffold.BaseAPI` provide
a method for checking the account balance of the respective concrete API
as well a method for checking whether an account id or **PartyId** is
active and valid.

### Example

``` python
print(
    f"ColAPI.get_account_balance: {ColAPI.get_account_balance('sandbox')}")
rembal=RemAPI.get_account_balance()
disbal=DisAPI.get_account_balance(x_target_environment="sandbox")
# print(rembal)
# print(disbal)
# Check if Account is Active
tmsisdn = "22997108557"
ColAPI.is_account_active(tmsisdn, 'msisdn', 'sandbox')
True
RemAPI.is_account_active(tmsisdn, 'msisdn',
'sandbox')
True
DisAPI.is_account_active(tmsisdn, 'msisdn', 'sandbox')
True
```

``` console
ColAPI.get_account_balance: {'availableBalance': '1000', 'currency': 'EUR'}
```


Collections API
---------------

The **CollectionAPI** provides a method for requesting payments from
customers as well as a method for checking the status of a payment
request in addition to the aforementioned account balance and validation
methods defined in the **BaseAPI** base class.

The CollectionAPI uses the **CParty** and **PaymentRequest** types for
its PaymentRequest and Party object arguments.

The `tekmomoapi.get_collection_party_obj` and
`tekmomoapi.get_payment_request_obj` provide
convenience function to create the required Party and Transfer objects.

### Example

Create a Collection PaymentRequest Object using the convenience
functions.

``` python
payment_request_obj = tekmomoapi.get_payment_request_obj(
    amount="100",
    currency="EUR",
    externalId=get_random_uuid_str(),
    payer=tekmomoapi.get_collection_party_obj(
        "msisdn", "22997108557").to_jsonable(),
    payerMessage="Payment Request Message Here",
    payeeNote="Customer Note Here",
)
```

### Request Payment

Using the **payment_request_obj** in the example above, we can request
payment from a customer using the
`tekmomoapi.CollectionAPI.request_payment` function.

``` python
ColAPI.request_payment(
    payment_request_obj.externalId,
    payment_request_obj,
    x_callback_url=None,
    x_target_environment="sandbox",
)
# Check Payment Request Status
print(ColAPI.get_payment_request_status(payment_request_obj.externalId))
```

``` json
{"amount": "100", "currency": "EUR", "financialTransactionId": "454621636",
"externalId": "8b2e92fd-a9a6-48e1-bae5-099d5d3ad4c8", "payer": {"partyIdType":
"MSISDN", "partyId": "22997108557"}, "payerMessage": "Payer Message Here",
"payeeNote": "Payee Note Here", "status": "SUCCESSFUL"}
```

Disbursements API
-----------------

The **DisbursementAPI** provides a method for initiating transfers from
the business to other parties as well as a method for checking the
status of a transfer request in addition to the account balance and
validation methods defined in the base class **BaseAPI**.The
DisbursementAPI uses the **DTransfer** and **DParty** classes to specify
its Party and Transfer object arguments.

The `tekmomoapi.get_disbursement_obj` and
`tekmomoapi.get_disbursement_party_obj` provide
convenience functions to create the correct and desired Transfer and
Party objects.

### Example

Create a Disbursement Transfer Object using the convenience functions.

``` python
dtransfer_obj = tekmomoapi.get_disbursement_transfer_obj(
    amount="100",
    currency="EUR",
    externalId=get_random_uuid_str(),
    payee=tekmomoapi.get_disbursement_party_obj(
        "msisdn", "22997108557"
    ),  # .to_jsonable(),
    payerMessage="Disbursement Transfer Message Here",
    payeeNote="Payee Business Note Here",
)
```

### Transfer Funds

Using the **dtransfer_obj** in the example above, we can transfer funds
using the `tekmomoapi.DisbursementAPI.transfer`
function.

``` python
dtres = DisAPI.transfer(
    dtransfer_obj.externalId,
    dtransfer_obj,
    x_callback_url=None,
    x_target_environment="sandbox",
)
# Check Transaction Status
print(DisAPI.get_transfer_status(dtransfer_obj.externalId))
```

``` json
{"amount": "100", "currency": "EUR", "financialTransactionId": "1501780124",
"externalId": "f832c026-fd6a-4414-9660-df3080471bdf",
"payee": {"partyIdType": "MSISDN", "partyId": "22997108557"},
"payerMessage": "Disbursement Transfer Message Here",
"payeeNote": "Payee Business Note Here", "status": "SUCCESSFUL"}
```

Remittance API
--------------

The **RemittanceAPI** is almost identical to the **DisbursementAPI**,
the methods provided by each are the same and are used in a similar
fashion. The difference is the type of Transfer and Party objects passed
to their parameters. To Distinguish between the two the RemittanceAPI
uses **RTransfer** and **RParty** classes.

The `tekmomoapi.get_remittance_obj` and
`tekmomoapi.get_remittance_party_obj` provide
convenience functions to create the correct and desired Transfer and
Party objects.

### Example

Create a Remittance Transfer Object using the convenience functions.

``` python
transfer_obj = tekmomoapi.get_remittance_transfer_obj(
    amount="100",
    currency="EUR",
    externalId=get_random_uuid_str(),
    payee=tekmomoapi.get_remittance_party_obj(
        "msisdn", "22997108557"
    ),  # .to_jsonable(),
    payerMessage="Remittance Transfer Message Here",
    payeeNote="Payee Business Note Here",
)
```

### Transfer Funds

Using the **transfer_obj** in the example above, we can transfer funds
using the `tekmomoapi.RemittanceAPI.transfer` function.

``` python
tres = RemAPI.transfer(
    transfer_obj.externalId,
    transfer_obj,
    x_callback_url=None,
    x_target_environment="sandbox",
)
# Check Transaction Status
print(RemAPI.get_transfer_status(transfer_obj.externalId))
```

``` json
{"amount": "100", "currency": "EUR", "financialTransactionId": "2105998992",
"externalId": "566ee525-c60a-4aac-9fb2-0c9dc24dd290", "payee": {"partyIdType":
"MSISDN", "partyId": "22997108557"}, "payerMessage": "Remittance Transfer Message Here",
"payeeNote": "Payee Business Note Here", "status": "SUCCESSFUL"}
```
# Contributing
[See the Contributing File](CONTRIBUTING.rst)


[See the Pull Request File](PULL_REQUEST_TEMPLATE.md)


# Support

# LICENCE

[Read the license here](LICENSE)


# Self-Promotion

[![](https://img.shields.io/badge/Github-TralahM-green?style=for-the-badge&logo=github)](https://github.com/TralahM)
[![](https://img.shields.io/badge/Twitter-%40tralahtek-red?style=for-the-badge&logo=twitter)](https://twitter.com/TralahM)
[![TralahM](https://img.shields.io/badge/Kaggle-TralahM-purple.svg?style=for-the-badge&logo=kaggle)](https://kaggle.com/TralahM)
[![TralahM](https://img.shields.io/badge/LinkedIn-TralahM-red.svg?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/TralahM)


[![Blog](https://img.shields.io/badge/Blog-tralahm.tralahtek.com-blue.svg?style=for-the-badge&logo=rss)](https://tralahm.tralahtek.com)

[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-cyan.svg?style=for-the-badge)](https://org.tralahtek.com)


