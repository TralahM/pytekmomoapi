#!/usr/bin/env python
"""Scaffold."""
# import pdb
from yaml import load
import tekmomoapi
from tekmomoapi import get_random_uuid_str

# import json

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

with open("test_credentials.yml", "r") as f:
    creds = load(f, Loader=Loader)

test_msisdns = {
    "failed": "46733123450",
    "rejected": "46733123451",
    "timeout": "46733123452",
    "ongoing": "46733123453",
    "pending": "46733123454",
}

dtransfer_obj = tekmomoapi.get_disbursement_transfer_obj(
    amount="100",
    currency="EUR",
    externalId=get_random_uuid_str(),
    payee=tekmomoapi.get_disbursement_party_obj(
        "msisdn", test_msisdns.get("ongoing", "")
    ),  # .to_jsonable(),
    payerMessage="Disbursement Transfer Message Here",
    payeeNote="Payee Business Note Here",
)
transfer_obj = tekmomoapi.get_remittance_transfer_obj(
    amount="100",
    currency="EUR",
    externalId=get_random_uuid_str(),
    payee=tekmomoapi.get_remittance_party_obj(
        "msisdn", test_msisdns.get("pending", "")
    ),  # .to_jsonable(),
    payerMessage="Remittance Transfer Message Here",
    payeeNote="Payee Business Note Here",
)
payment_request_obj = tekmomoapi.get_payment_request_obj(
    amount="100",
    currency="EUR",
    externalId=get_random_uuid_str(),
    payer=tekmomoapi.get_collection_party_obj(
        "msisdn", "22997108557").to_jsonable(),
    payerMessage="Payment Request Message Here",
    payeeNote="Customer Note Here",
)

cuser = tekmomoapi.get_user_id_and_api_key(
    creds.get("collection_subscription_key"))
duser = tekmomoapi.get_user_id_and_api_key(
    creds.get("disbursement_subscription_key"),
)
ruser = tekmomoapi.get_user_id_and_api_key(
    creds.get("remittance_subscription_key"),
)
user = {
    "user_id": "891a3dcc-f5cf-44ec-b6fe-3f74fe560add",
    "apiKey": "555a5fc2893d4091bfcce301362f1d82",
}

print(cuser)
print(duser)
print(ruser)
print(user)
print()

ColAPI = tekmomoapi.CollectionAPI(
    creds.get("collection_subscription_key"),
    base_url=tekmomoapi.SANDBOX_BASE_URL,
    **cuser,
)
DisAPI = tekmomoapi.DisbursementAPI(
    creds.get("disbursement_subscription_key"),
    base_url=tekmomoapi.SANDBOX_BASE_URL,
    **duser,
)
RemAPI = tekmomoapi.RemittanceAPI(
    creds.get("remittance_subscription_key"),
    base_url=tekmomoapi.SANDBOX_BASE_URL,
    **user,
)

try:
    tmsisdn = test_msisdns.get("ongoing")
    # print(f"DisAPI.basic_auth_str: {DisAPI.basic_auth_str}")
    # print(f"DisAPI.bearer_auth_str: {DisAPI.bearer_auth_str}")
    print(
        f"DisAPI.get_account_balance: {
            DisAPI.get_account_balance('sandbox')}"
    )
    print()
except Exception as e:
    print(f"Error: DisAPI.get_account_balance: {e}")
    # pdb.set_trace()
    print()
    pass

try:
    tmsisdn = test_msisdns.get("pending")
    print(
        f"DisAPI.is_account_active: {
            DisAPI.is_account_active(tmsisdn, 'msisdn', 'sandbox')}"
    )
    print()
except Exception as e:
    print(f"Error: DisAPI.is_account_active: {e}")
    # pdb.set_trace()
    print()
    pass

try:
    dtres = DisAPI.transfer(
        dtransfer_obj.externalId,
        dtransfer_obj,
        x_callback_url=None,
        x_target_environment="sandbox",
    )
    print("DisAPI.transfer: ", dtres)
    print()
except Exception as e:
    print(f"Error: DisAPI.transfer: {e}")
    # pdb.set_trace()
    print()
    pass

try:
    print(
        "DisAPI.get_transfer_status: ",
        DisAPI.get_transfer_status(dtransfer_obj.externalId),
    )
    print()
except Exception as e:
    print(f"Error: DisAPI.get_transfer_status: {e}")
    # pdb.set_trace()
    print()
    pass

try:
    tmsisdn = "22997108557"
    print(
        f"RemAPI.get_account_balance: {
            RemAPI.get_account_balance('sandbox')}"
    )
    print()
except Exception as e:
    print(f"Error: RemAPI.get_account_balance: {e}")
    # pdb.set_trace()
    print()
    pass

try:
    tmsisdn = "22997108557"
    print(
        f"RemAPI.is_account_active: {
            RemAPI.is_account_active(tmsisdn, 'msisdn', 'sandbox')}"
    )
    print()
except Exception as e:
    print(f"Error: RemAPI.is_account_active: {e}")
    # pdb.set_trace()
    print()
    pass

try:
    tres = RemAPI.transfer(
        transfer_obj.externalId,
        transfer_obj,
        x_callback_url=None,
        x_target_environment="sandbox",
    )
    print("RemAPI.transfer: ", tres)
    print()
except Exception as e:
    print(f"Error: RemAPI.transfer: {e}")
    # pdb.set_trace()
    print()
    pass

try:
    print(
        "RemAPI.get_transfer_status: ",
        RemAPI.get_transfer_status(transfer_obj.externalId),
    )
    print()
except Exception as e:
    print(f"Error: RemAPI.get_transfer_status: {e}")
    # pdb.set_trace()
    print()
    pass


try:
    tmsisdn = "22997108557"
    print(
        f"ColAPI.get_account_balance: {
            ColAPI.get_account_balance('sandbox')}"
    )
    print()
except Exception as e:
    print(f"Error: ColAPI.get_account_balance: {e}")
    # pdb.set_trace()
    print()
    pass

try:
    tmsisdn = "22997108557"
    print(
        f"ColAPI.is_account_active: {
            ColAPI.is_account_active(tmsisdn, 'msisdn', 'sandbox')}"
    )
    print()
except Exception as e:
    print(f"Error: ColAPI.is_account_active: {e}")
    # pdb.set_trace()
    print()
    pass

try:
    pres = ColAPI.request_payment(
        payment_request_obj.externalId,
        payment_request_obj,
        x_callback_url=None,
        x_target_environment="sandbox",
    )
    print("ColAPI.request_payment: ", pres)
    print()
except Exception as e:
    print(f"Error: ColAPI.request_payment: {e}")
    # pdb.set_trace()
    print()
    pass

try:
    print(
        "ColAPI.get_payment_request_status: ",
        ColAPI.get_payment_request_status(payment_request_obj.externalId),
    )
    print()
except Exception as e:
    print(f"Error: ColAPI.get_payment_request_status: {e}")
    # pdb.set_trace()
    print()
    pass
