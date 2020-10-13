"""Scaffold API Module.

To simplify usage of the underlying Remote APIs Namely:
- Collections
- Disbursements
- Remittances
- Sandbox User Provisioning.
"""
import json
from .collection import (
    RemoteCaller as Collection,
    RequestToPay as PaymentRequest,
    request_to_pay_from_obj,
    Party as CParty,
)
from .disbursements import (
    RemoteCaller as Disbursement,
    Transfer as DTransfer,
    Party as DParty,
)
from .remittance import (
    RemoteCaller as Remittance,
    Transfer as RTransfer,
    Party as RParty,
)
from .userprovisioning import RemoteCaller as UserProvisioning
from .utils import get_authorization_str, get_random_uuid_str

SANDBOX_BASE_URL = "https://sandbox.momodeveloper.mtn.com"
__all__ = [
    "get_sandbox_test_args",
    "BaseAPI",
    "RemittanceAPI",
    "DisbursementAPI",
    "CollectionAPI",
    "DParty",
    "RParty",
    "CParty",
    "PaymentRequest",
    "DTransfer",
    "RTransfer",
    "get_collection_party_obj",
    "get_disbursement_party_obj",
    "get_remittance_party_obj",
    "get_disbursement_transfer_obj",
    "get_remittance_transfer_obj",
    "get_payment_request_obj",
]


def get_remittance_party_obj(partyIdType: str, partyId: str):
    """Return a Party obj from args and kwargs.

    :param partyIdType: Specifies the type of the party ID.
        Allowed values [msisdn, email, party_code].<br>
    :param partyId: Specifies the party ID, should explicitly be in small letters.
    """
    return RParty(partyIdType, partyId)


def get_disbursement_party_obj(partyIdType: str, partyId: str):
    """Return a Party obj from args and kwargs.

    :param partyIdType: Specifies the type of the party ID.
        Allowed values [msisdn, email, party_code].<br>
    :param partyId: Specifies the party ID, should explicitly be in small letters.
    """
    return DParty(partyIdType, partyId)


def get_collection_party_obj(partyIdType: str, partyId: str):
    """Return a Party obj from args and kwargs.

    :param partyIdType: Specifies the type of the party ID.
        Allowed values [msisdn, email, party_code].<br>
    :param partyId: Specifies the party ID, should explicitly be in small letters.
    """
    return CParty(partyIdType, partyId)


def get_remittance_transfer_obj(
    amount: str,
    currency: str,
    externalId: str,
    payee: RParty,
    payerMessage: str,
    payeeNote: str,
):
    """Return a Transfer obj from args and kwargs.

    :param amount: Amount to Transfer,
    :param currency: Currency Code,
    :param externalId: External Identifier for the transaction,
    :param payee: RParty(partyIdType,partyId),
    :param payerMessage: payer Message,
    :param payeeNote: payee Note,
    """
    obj = locals()
    return RTransfer(**obj)


def get_disbursement_transfer_obj(
    amount: str,
    currency: str,
    externalId: str,
    payee: DParty,
    payerMessage: str,
    payeeNote: str,
):
    """Return a Transfer obj from args and kwargs.

    :param amount: Amount to Transfer,
    :param currency: Currency Code,
    :param externalId: External Identifier for the transaction,
    :param payee: DParty(partyIdType,partyId),
    :param payerMessage: payer Message,
    :param payeeNote: payee Note,
    """
    obj = locals()
    return DTransfer(**obj)


def get_payment_request_obj(
    amount: str,
    currency: str,
    externalId: str,
    payer: CParty,
    payerMessage: str,
    payeeNote: str,
):
    """Return a PaymentRequest obj from args and kwargs.

    :param amount: Amount to Transfer,
    :param currency: Currency Code,
    :param externalId: External Identifier for the transaction,
    :param payer: CParty(partyIdType,partyId),
    :param payerMessage: payer Message,
    :param payeeNote: payee Note,
    """
    obj = locals()
    return request_to_pay_from_obj(obj)


def get_sandbox_test_args(
    subscriptionKey: str, base_url: str = SANDBOX_BASE_URL
) -> dict:
    """Return some sandbox default sane test configuration values.

    :param subscription_key: Your Subscription Key.
    :param base_url: The sandbox base url default *https://sandbox.momodeveloper.mtn.com*.

    :returns: a key,value pair of user_id,base_url,x_target_environment, apiKey,subscriptionKey."
    """
    user_id = get_random_uuid_str()
    userpapi = UserProvisioning(url_prefix=base_url)
    userpapi.post_v1_0_apiuser(subscriptionKey, user_id)
    result = userpapi.post_v1_0_apiuser_apikey(subscriptionKey, user_id)
    apiKey = json.loads(result).get("apiKey")
    return {
        "user_id": user_id,
        "apiKey": apiKey,
        "subscriptionKey": subscriptionKey,
        "base_url": base_url,
        "x_target_environment": "sandbox",
    }


class BaseAPI:
    """Base API Handler Scaffold."""

    remote_caller_class = None

    def __init__(
        self,
        subscriptionKey: str,
        base_url: str,
        user_id: str,
        apiKey: str,
        *args,
        **kwargs,
    ):
        """Initialize BaseAPIScaffold.

        @param subscription_key : Ocm-Apim-Subscription-Key,
        @param url_prefix : base_url prefix for either sandbox or production,
        @param user_id : user uuid4 identifier,
        @param apiKey : user apiKey,
        """
        self.subscription_key = subscriptionKey
        self.url_prefix = base_url
        self.user_id = user_id
        self.api_key = apiKey
        self.remote_caller = self.remote_caller_class(base_url)

    @property
    def basic_auth_str(self):
        """Get Authorization String of type Basic."""
        return get_authorization_str(self.user_id, self.api_key)

    def get_access_token(self):
        """Get Access Token From RemoteCaller Token API."""
        tokenResult = self.remote_caller.token_POST(
            self.subscription_key,
            authorization=self.basic_auth_str,
        )
        return tokenResult.to_jsonable().get("access_token")

    @property
    def bearer_auth_str(self):
        """Get Authorization String of type Bearer."""
        return "Bearer " + self.get_access_token()

    def get_account_balance(self, x_target_environment="sandbox"):
        """
        Get the balance of the account.

        :param x_target_environment: The identifier of the EWP system where the transaction shall be processed.
            This parameter is used to route the request to the EWP system that will initiate the transaction.

        :returns: Balance obj.
        """
        balance = self.remote_caller.get_v1_0_account_balance(
            self.subscription_key,
            x_target_environment,
            authorization=self.bearer_auth_str,
        )
        return balance.to_jsonable()

    def is_account_active(
        self,
        account_uuid,
        account_type,
        x_target_environment="sandbox",
    ):
        """
        Operation is used  to check if an account holder is registered and active in the system.

        :param account_uuid: The party number.
            Validated according to the party ID type (case Sensitive).
            <br> msisdn - Mobile Number validated according to ITU-T E.164.
            Validated with IsMSISDN<br>
            email - Validated to be a valid e-mail format.
            Validated with IsEmail
            <br> party_code - UUID of the party. Validated with IsUuid
        :param account_type: Specifies the type of the party ID.
            Allowed values [msisdn, email, party_code].
            <br> accountHolderId should explicitly be in small letters.
        :param x_target_environment: The identifier of the EWP system where the transaction shall be processed.
            This parameter is used to route the request to the EWP system that will initiate the transaction.

        :returns: True if account holder is registered and active,
            False if the account holder is not active or not found
        """
        accresult = self.remote_caller.get_v1_0_accountholder_accountholderidtype_accountholderid_active(
            self.subscription_key,
            account_uuid,
            account_type,
            x_target_environment,
            authorization=self.bearer_auth_str,
        )
        return json.loads(accresult).get("result")


class RemittanceAPI(BaseAPI):
    """Remittance API Handler."""

    remote_caller_class = Remittance

    def transfer(
        self,
        x_reference_id,
        transfer_obj,
        x_callback_url="",
        x_target_environment="sandbox",
    ):
        r"""
        Transfer operation is used to transfer an amount from the own account to a payee account.

        <br> Status of the transaction can validated by using the GET /transfer/\{referenceId\}

        :param x_reference_id: Format - UUID. Recource ID of the created request to pay transaction.
            This ID is used, for example validating the status of the request. ‘Universal Unique ID’ for the transaction generated using UUID version 4.
        :param x_target_environment: The identifier of the EWP system where the transaction shall be processed.
            This parameter is used to route the request to the EWP system that will initiate the transaction.
        :param x_callback_url: URL to the server where the callback should be sent.
        :param transfer:

        :return:
        """
        res = self.remote_caller.transfer_POST(
            self.subscription_key,
            x_reference_id=x_reference_id,
            x_target_environment=x_target_environment,
            x_callback_url=x_callback_url,
            transfer=transfer_obj,
            authorization=self.bearer_auth_str,
        )
        return res

    def get_transfer_status(
        self,
        reference_id,
        x_target_environment="sandbox",
    ):
        """
        Get This operation is used to get the status of a transfer.

        X-Reference-Id that was passed in the post is used as reference to the request.

        :param reference_id: UUID of transaction to get result.
            Reference id  used when creating the request to pay.
        :param x_target_environment: The identifier of the EWP system where the transaction shall be processed.
            This parameter is used to route the request to the EWP system that will initiate the transaction.

        :return: OK. Note that a failed transfer will be returned with this status too.
            The 'status' of the TransferResult can be used to determine the outcome of the request.
            The 'reason' field can be used to retrieve a cause in case of failure.
        """
        result = self.remote_caller.transfer_referenceId_GET(
            self.subscription_key,
            reference_id=reference_id,
            x_target_environment=x_target_environment,
            authorization=self.bearer_auth_str,
        )
        return result.to_jsonable()


class DisbursementAPI(BaseAPI):
    """Disbursement API Handler."""

    remote_caller_class = Disbursement

    def transfer(
        self,
        x_reference_id,
        transfer_obj,
        x_callback_url="",
        x_target_environment="sandbox",
    ):
        r"""
        Transfer operation is used to transfer an amount from the own account to a payee account.

        <br> Status of the transaction can validated by using the GET /transfer/\{referenceId\}

        :param x_reference_id: Format - UUID. Recource ID of the created request to pay transaction.
            This ID is used, for example validating the status of the request. ‘Universal Unique ID’ for the transaction generated using UUID version 4.
        :param x_target_environment: The identifier of the EWP system where the transaction shall be processed.
            This parameter is used to route the request to the EWP system that will initiate the transaction.
        :param x_callback_url: URL to the server where the callback should be sent.
        :param transfer:

        :return:
        """
        res = self.remote_caller.transfer_POST(
            self.subscription_key,
            x_reference_id=x_reference_id,
            x_target_environment=x_target_environment,
            x_callback_url=x_callback_url,
            transfer=transfer_obj,
            authorization=self.bearer_auth_str,
        )
        return res

    def get_transfer_status(
        self,
        reference_id,
        x_target_environment="sandbox",
    ):
        """
        Get This operation is used to get the status of a transfer.

        X-Reference-Id that was passed in the post is used as reference to the request.

        :param reference_id: UUID of transaction to get result.
            Reference id  used when creating the request to pay.
        :param x_target_environment: The identifier of the EWP system where the transaction shall be processed.
            This parameter is used to route the request to the EWP system that will initiate the transaction.

        :return: OK. Note that a failed transfer will be returned with this status too.
            The 'status' of the TransferResult can be used to determine the outcome of the request.
            The 'reason' field can be used to retrieve a cause in case of failure.
        """
        result = self.remote_caller.transfer_referenceId_GET(
            self.subscription_key,
            reference_id=reference_id,
            x_target_environment=x_target_environment,
            authorization=self.bearer_auth_str,
        )
        return result.to_jsonable()


class CollectionAPI(BaseAPI):
    """Collection API Handler."""

    remote_caller_class = Collection

    def request_payment(
        self,
        x_reference_id: str,
        payment_request: PaymentRequest,
        x_callback_url="",
        x_target_environment="sandbox",
    ):
        r"""
        Get This operation is used to request a payment from a consumer (Payer). The payer will be asked to authorize the payment. The transaction will be executed once the payer has authorized the payment. The requesttopay will be in status PENDING until the transaction is authorized or declined by the payer or it is timed out by the system.

         Status of the transaction can be validated by using the GET /requesttopay/\<resourceId\>

        :param x_reference_id: Format - UUID. Recource ID of the created request to pay transaction. This ID is used, for example, validating the status of the request. ‘Universal Unique ID’ for the transaction generated using UUID version 4.
        :param payment_request:
        :param x_callback_url: URL to the server where the callback should be sent.
        :param x_target_environment: The identifier of the EWP system where the transaction shall be processed. This parameter is used to route the request to the EWP system that will initiate the transaction.

        :return:
        """
        returnv = self.remote_caller.requesttopay_POST(
            self.subscription_key,
            x_reference_id=x_reference_id,
            x_target_environment=x_target_environment,
            authorization=self.bearer_auth_str,
            x_callback_url=x_callback_url,
            request_to_pay=payment_request,
        )
        return returnv

    def get_payment_request_status(
        self,
        reference_id,
        x_target_environment="sandbox",
    ):
        """Get Payment Request Status."""
        return self.remote_caller.requesttopay_referenceId_GET(
            self.subscription_key,
            reference_id=reference_id,
            x_target_environment=x_target_environment,
            authorization=self.bearer_auth_str,
        ).to_jsonable()
