.. role:: pycode(code)
   :language: python

Quickstart
=================


Installation
-------------

.. code-block:: console

   pip install pytekmomoapi



Sandbox User Provisioning
------------------------------
We have provided a convenient function, :pycode:`tekmomoapi.get_user_id_and_api_key` ,
to help you quickly provision and get the required credentials i.e
the :strong:`user_id` and :strong:`apiKey` on the sandbox environment.

The Library also provided a utility function to get a random :pycode:`uuid.uuid4`
string, this is quite useful because the remote Momo Developer API heavily uses
uuid4s for identification and referencing, i.e during user provisioning, financial
transactions, party identification and referencing.
The function :pycode:`tekmomoapi.get_random_uuid_str` provides that convenience.

This reduces the amount of boilerplate code that would be otherwise required.

Example
^^^^^^^^^

.. code-block:: python

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


::
   >>> user = tekmomoapi.get_user_id_and_api_key(creds.get("remittance_subscription_key"))
   >>> print(user)
   {'user_id': 'fcbf0091-2dbe-4f37-9131-46a2a0dcda9e', 'apiKey': 'cb196acfa75b4bf1858b5dccdbb605a6'}


Authentication and Authorization
------------------------------------
OAuth Token is generated from the merchants’ API Key and Secret.
The API Key and API Secret can be obtained through the provisioning API in Sandbox.

We have built-in the authentication and authorization processes so you dont have
to worry about base64 encodings, whether to user Bearer or Basic Authentication,
enabling you to focus on more important details i.e your business logic
implementation and other more fun stuff.

You can obtain the authentication header string anytime if you wish to do so by
using the top level :pycode:`tekmomoapi.scaffold.BaseAPI` and its subclassess :pycode:`tekmomoapi.scaffold.BaseAPI.basic_auth_str` or the
:pycode:`tekmomoapi.scaffold.BaseAPI.bearer_auth_str` property methods.

Example
^^^^^^^^^

.. code-block:: python

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


Account Balance and Account Holder Validation
----------------------------------------------
All Subclasses of :pycode:`tekmomoapi.scaffold.BaseAPI` provide a method for checking the
account balance of the respective concrete API as well a method for checking
whether an account id or :strong:`PartyId` is active and valid.

Example
^^^^^^^^^

.. code-block:: python

    print(
        f"ColAPI.get_account_balance: {ColAPI.get_account_balance('sandbox')}")
    rembal=RemAPI.get_account_balance()
    disbal=DisAPI.get_account_balance(x_target_environment="sandbox")
    # print(rembal)
    # print(disbal)
    # Check if Account is Active

.. code-block:: console

   ColAPI.get_account_balance: {'availableBalance': '1000', 'currency': 'EUR'}


::
    >>> tmsisdn = "22997108557"
    >>> ColAPI.is_account_active(tmsisdn, 'msisdn', 'sandbox')
    True
    >>> RemAPI.is_account_active(tmsisdn, 'msisdn', 'sandbox')
    True
    >>> DisAPI.is_account_active(tmsisdn, 'msisdn', 'sandbox')
    True



Collections API
------------------------
The :strong:`CollectionAPI` provides a method for requesting payments from customers as
well as a method for checking the status of a payment request in addition to the
aforementioned account balance and validation methods defined in the :strong:`BaseAPI`
base class.

The CollectionAPI uses the :strong:`CParty` and :strong:`PaymentRequest` types
for its PaymentRequest and Party object arguments.

The :pycode:`tekmomoapi.get_collection_party_obj` and
:pycode:`tekmomoapi.get_payment_request_obj` provide convenience function to
create the required Party and Transfer objects.


Example
^^^^^^^^^
Create a Collection PaymentRequest Object using the convenience functions.

.. code-block:: python

   payment_request_obj = tekmomoapi.get_payment_request_obj(
       amount="100",
       currency="EUR",
       externalId=get_random_uuid_str(),
       payer=tekmomoapi.get_collection_party_obj(
           "msisdn", "22997108557").to_jsonable(),
       payerMessage="Payment Request Message Here",
       payeeNote="Customer Note Here",
   )

Request Payment
^^^^^^^^^^^^^^^^^^
Using the :strong:`payment_request_obj` in the example above, we can request payment
from a customer using the :pycode:`tekmomoapi.CollectionAPI.request_payment` function.

.. code-block:: python

    ColAPI.request_payment(
        payment_request_obj.externalId,
        payment_request_obj,
        x_callback_url=None,
        x_target_environment="sandbox",
    )
    # Check Payment Request Status
    print(ColAPI.get_payment_request_status(payment_request_obj.externalId))


.. code-block:: json

   {"amount": "100", "currency": "EUR", "financialTransactionId": "454621636",
   "externalId": "8b2e92fd-a9a6-48e1-bae5-099d5d3ad4c8", "payer": {"partyIdType":
   "MSISDN", "partyId": "22997108557"}, "payerMessage": "Payer Message Here",
   "payeeNote": "Payee Note Here", "status": "SUCCESSFUL"}


Disbursements API
--------------------
The :strong:`DisbursementAPI` provides a method for initiating transfers from the
business to other parties as well as a method for checking the status of a
transfer request in addition to the account balance and validation methods
defined in the base class :strong:`BaseAPI`.The DisbursementAPI uses the :strong:`DTransfer` and
:strong:`DParty` classes to specify its Party and Transfer object arguments.

The :pycode:`tekmomoapi.get_disbursement_obj` and :pycode:`tekmomoapi.get_disbursement_party_obj`
provide convenience functions to create the correct and desired Transfer and
Party objects.

Example
^^^^^^^^^
Create a Disbursement Transfer Object using the convenience functions.

.. code-block:: python

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

Transfer Funds
^^^^^^^^^^^^^^^^^^
Using the :strong:`dtransfer_obj` in the example above, we can transfer funds
using the :pycode:`tekmomoapi.DisbursementAPI.transfer` function.

.. code-block:: python

    dtres = DisAPI.transfer(
        dtransfer_obj.externalId,
        dtransfer_obj,
        x_callback_url=None,
        x_target_environment="sandbox",
    )
    # Check Transaction Status
    print(DisAPI.get_transfer_status(dtransfer_obj.externalId))


.. code-block:: json

   {"amount": "100", "currency": "EUR", "financialTransactionId": "1501780124",
   "externalId": "f832c026-fd6a-4414-9660-df3080471bdf",
   "payee": {"partyIdType": "MSISDN", "partyId": "22997108557"},
   "payerMessage": "Disbursement Transfer Message Here",
   "payeeNote": "Payee Business Note Here", "status": "SUCCESSFUL"}



Remittance API
--------------------
The :strong:`RemittanceAPI` is almost identical to the :strong:`DisbursementAPI`, the methods
provided by each are the same and are used in a similar fashion.
The difference is the type of Transfer and Party objects passed to their
parameters. To Distinguish between the two the RemittanceAPI uses :strong:`RTransfer`
and :strong:`RParty` classes.

The :pycode:`tekmomoapi.get_remittance_obj` and :pycode:`tekmomoapi.get_remittance_party_obj`
provide convenience functions to create the correct and desired Transfer and
Party objects.


Example
^^^^^^^^^
Create a Remittance Transfer Object using the convenience functions.

.. code-block:: python

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


Transfer Funds
^^^^^^^^^^^^^^^^^^
Using the :strong:`transfer_obj` in the example above, we can transfer funds
using the :pycode:`tekmomoapi.RemittanceAPI.transfer` function.

.. code-block:: python

    tres = RemAPI.transfer(
        transfer_obj.externalId,
        transfer_obj,
        x_callback_url=None,
        x_target_environment="sandbox",
    )
    # Check Transaction Status
    print(RemAPI.get_transfer_status(transfer_obj.externalId))

.. code-block:: json

  {"amount": "100", "currency": "EUR", "financialTransactionId": "2105998992",
  "externalId": "566ee525-c60a-4aac-9fb2-0c9dc24dd290", "payee": {"partyIdType":
  "MSISDN", "partyId": "22997108557"}, "payerMessage": "Remittance Transfer Message Here",
  "payeeNote": "Payee Business Note Here", "status": "SUCCESSFUL"}
