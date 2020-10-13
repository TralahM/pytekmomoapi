"""Momo Developer APIs SDK."""
import json
from . import scaffold
from .scaffold import (
    RemittanceAPI,
    CollectionAPI,
    DisbursementAPI,
    UserProvisioning as UserProvisioningAPI,
    get_collection_party_obj,
    get_disbursement_party_obj,
    get_remittance_party_obj,
    get_disbursement_transfer_obj,
    get_remittance_transfer_obj,
    get_payment_request_obj,
    get_sandbox_test_args,
    DParty,
    RParty,
    CParty,
)
from .utils import get_authorization_str, get_random_uuid_str

SANDBOX_BASE_URL = "https://sandbox.momodeveloper.mtn.com"


def get_user_id_and_api_key(
    subscriptionKey: str, base_url: str = SANDBOX_BASE_URL
) -> dict:
    """Return a key,value pair of user_id and apiKey."""
    user_id = get_random_uuid_str()
    userpapi = UserProvisioningAPI(url_prefix=base_url)
    userpapi.post_v1_0_apiuser(subscriptionKey, user_id)
    result = userpapi.post_v1_0_apiuser_apikey(subscriptionKey, user_id)
    apiKey = json.loads(result).get("apiKey")
    return {
        "user_id": user_id,
        "apiKey": apiKey,
    }


__all__ = [
    "CollectionAPI",
    "RemittanceAPI",
    "DisbursementAPI",
    "UserProvisioningAPI",
    "get_authorization_str",
    "get_random_uuid_str",
    "get_user_id_and_api_key",
    "get_collection_party_obj",
    "get_disbursement_party_obj",
    "get_remittance_party_obj",
    "get_disbursement_transfer_obj",
    "get_remittance_transfer_obj",
    "get_payment_request_obj",
    "get_sandbox_test_args",
    "DParty",
    "RParty",
    "CParty",
    "scaffold",
    "SANDBOX_BASE_URL",
]
