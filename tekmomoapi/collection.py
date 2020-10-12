#!/usr/bin/env python3
# Automatically generated file by swagger_to. DO NOT EDIT OR APPEND ANYTHING!
"""Implements the client for collection."""

# pylint: skip-file
# pydocstyle: add-ignore=D105,D107,D401

import contextlib
import json
from typing import Any, BinaryIO, Dict, List, MutableMapping, Optional, cast

import requests
import requests.auth


class ErrorReason:
    def __init__(
        self, code: Optional[str] = None, message: Optional[str] = None
    ) -> None:
        """Initializes with the given values."""
        self.code = code

        self.message = message

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to error_reason_to_jsonable.

        :return: JSON-able representation
        """
        return error_reason_to_jsonable(self)


class TokenPost200ApplicationJsonResponse:
    def __init__(
        self,
        access_token: Optional[str] = None,
        token_type: Optional[str] = None,
        expires_in: Optional[str] = None,
    ) -> None:
        """Initializes with the given values."""
        # A JWT token which can be used to authrize against the other API end-points. The format of the token follows the JWT standard format (see jwt.io for an example). This is the token that should be sent in in the Authorization header when calling the other API end-points.
        self.access_token = access_token

        # The token type.
        self.token_type = token_type

        # The validity time in seconds of the token.
        self.expires_in = expires_in

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to token_post200_application_json_response_to_jsonable.

        :return: JSON-able representation
        """
        return token_post200_application_json_response_to_jsonable(self)


def new_token_post200_application_json_response() -> TokenPost200ApplicationJsonResponse:
    """Generates an instance of TokenPost200ApplicationJsonResponse with default values."""
    return TokenPost200ApplicationJsonResponse()


def token_post200_application_json_response_from_obj(
    obj: Any, path: str = ""
) -> TokenPost200ApplicationJsonResponse:
    """
    Generates an instance of TokenPost200ApplicationJsonResponse from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of TokenPost200ApplicationJsonResponse
    :param path: path to the object used for debugging
    :return: parsed instance of TokenPost200ApplicationJsonResponse
    """
    if not isinstance(obj, dict):
        raise ValueError(
            "Expected a dict at path {}, but got: {}".format(path, type(obj))
        )

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                "Expected a key of type str at path {}, but got: {}".format(
                    path, type(key)
                )
            )

    if "access_token" in obj:
        access_token_from_obj = from_obj(
            obj["access_token"], expected=[str], path=path + ".access_token"
        )  # type: Optional[str]
    else:
        access_token_from_obj = None

    if "token_type" in obj:
        token_type_from_obj = from_obj(
            obj["token_type"], expected=[str], path=path + ".token_type"
        )  # type: Optional[str]
    else:
        token_type_from_obj = None

    if "expires_in" in obj:
        expires_in_from_obj = from_obj(
            obj["expires_in"], expected=[int], path=path + ".expires_in"
        )  # type: Optional[str]
    else:
        expires_in_from_obj = None

    return TokenPost200ApplicationJsonResponse(
        access_token=access_token_from_obj,
        token_type=token_type_from_obj,
        expires_in=expires_in_from_obj,
    )


def token_post200_application_json_response_to_jsonable(
    token_post200_application_json_response: TokenPost200ApplicationJsonResponse,
    path: str = "",
) -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of TokenPost200ApplicationJsonResponse.

    :param token_post200_application_json_response: instance of TokenPost200ApplicationJsonResponse to be JSON-ized
    :param path: path to the token_post200_application_json_response used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if token_post200_application_json_response.access_token is not None:
        res["access_token"] = token_post200_application_json_response.access_token

    if token_post200_application_json_response.token_type is not None:
        res["token_type"] = token_post200_application_json_response.token_type

    if token_post200_application_json_response.expires_in is not None:
        res["expires_in"] = token_post200_application_json_response.expires_in

    return res


class TokenPost401ApplicationJsonResponse:
    def __init__(self, error: Optional[str] = None) -> None:
        """Initializes with the given values."""
        # An error code.
        self.error = error

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to token_post401_application_json_response_to_jsonable.

        :return: JSON-able representation
        """
        return token_post401_application_json_response_to_jsonable(self)


def new_token_post401_application_json_response() -> TokenPost401ApplicationJsonResponse:
    """Generates an instance of TokenPost401ApplicationJsonResponse with default values."""
    return TokenPost401ApplicationJsonResponse()


def token_post401_application_json_response_from_obj(
    obj: Any, path: str = ""
) -> TokenPost401ApplicationJsonResponse:
    """
    Generates an instance of TokenPost401ApplicationJsonResponse from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of TokenPost401ApplicationJsonResponse
    :param path: path to the object used for debugging
    :return: parsed instance of TokenPost401ApplicationJsonResponse
    """
    if not isinstance(obj, dict):
        raise ValueError(
            "Expected a dict at path {}, but got: {}".format(path, type(obj))
        )

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                "Expected a key of type str at path {}, but got: {}".format(
                    path, type(key)
                )
            )

    if "error" in obj:
        error_from_obj = from_obj(
            obj["error"], expected=[str], path=path + ".error"
        )  # type: Optional[str]
    else:
        error_from_obj = None

    return TokenPost401ApplicationJsonResponse(error=error_from_obj)


def token_post401_application_json_response_to_jsonable(
    token_post401_application_json_response: TokenPost401ApplicationJsonResponse,
    path: str = "",
) -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of TokenPost401ApplicationJsonResponse.

    :param token_post401_application_json_response: instance of TokenPost401ApplicationJsonResponse to be JSON-ized
    :param path: path to the token_post401_application_json_response used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if token_post401_application_json_response.error is not None:
        res["error"] = token_post401_application_json_response.error

    return res


class Balance:
    """The available balance of the account"""

    def __init__(
        self, availableBalance: Optional[str] = None, currency: Optional[str] = None
    ) -> None:
        """Initializes with the given values."""
        # The available balance of the account
        self.availableBalance = availableBalance

        # ISO4217 Currency
        self.currency = currency

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to balance_to_jsonable.

        :return: JSON-able representation
        """
        return balance_to_jsonable(self)


def new_balance() -> Balance:
    """Generates an instance of Balance with default values."""
    return Balance()


def balance_from_obj(obj: Any, path: str = "") -> Balance:
    """
    Generates an instance of Balance from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of Balance
    :param path: path to the object used for debugging
    :return: parsed instance of Balance
    """
    if not isinstance(obj, dict):
        raise ValueError(
            "Expected a dict at path {}, but got: {}".format(path, type(obj))
        )

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                "Expected a key of type str at path {}, but got: {}".format(
                    path, type(key)
                )
            )

    if "availableBalance" in obj:
        availableBalance_from_obj = from_obj(
            obj["availableBalance"],
            expected=[str],
            path=path + ".availableBalance",
        )  # type: Optional[str]
    else:
        availableBalance_from_obj = None

    if "currency" in obj:
        currency_from_obj = from_obj(
            obj["currency"], expected=[str], path=path + ".currency"
        )  # type: Optional[str]
    else:
        currency_from_obj = None

    return Balance(
        availableBalance=availableBalance_from_obj, currency=currency_from_obj
    )


def balance_to_jsonable(balance: Balance, path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of Balance.

    :param balance: instance of Balance to be JSON-ized
    :param path: path to the balance used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if balance.availableBalance is not None:
        res["availableBalance"] = balance.availableBalance

    if balance.currency is not None:
        res["currency"] = balance.currency

    return res


class Party:
    """Party identifies a account holder in the wallet platform. Party consists of two parameters, type and partyId. Each type have its own validation of the partyId<br> MSISDN - Mobile Number validated according to ITU-T E.164. Validated with IsMSISDN<br> EMAIL - Validated to be a valid e-mail format. Validated with IsEmail<br> PARTY_CODE - UUID of the party. Validated with IsUuid"""

    def __init__(
        self, partyIdType: Optional[str] = None, partyId: Optional[str] = None
    ) -> None:
        """Initializes with the given values."""
        self.partyIdType = partyIdType

        self.partyId = partyId

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to party_to_jsonable.

        :return: JSON-able representation
        """
        return party_to_jsonable(self)


def new_party() -> Party:
    """Generates an instance of Party with default values."""
    return Party()


def party_from_obj(obj: Any, path: str = "") -> Party:
    """
    Generates an instance of Party from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of Party
    :param path: path to the object used for debugging
    :return: parsed instance of Party
    """
    if not isinstance(obj, dict):
        raise ValueError(
            "Expected a dict at path {}, but got: {}".format(path, type(obj))
        )

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                "Expected a key of type str at path {}, but got: {}".format(
                    path, type(key)
                )
            )

    if "partyIdType" in obj:
        partyIdType_from_obj = from_obj(
            obj["partyIdType"], expected=[str], path=path + ".partyIdType"
        )  # type: Optional[str]
    else:
        partyIdType_from_obj = None

    if "partyId" in obj:
        partyId_from_obj = from_obj(
            obj["partyId"], expected=[str], path=path + ".partyId"
        )  # type: Optional[str]
    else:
        partyId_from_obj = None

    return Party(partyIdType=partyIdType_from_obj, partyId=partyId_from_obj)


def party_to_jsonable(party: Party, path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of Party.

    :param party: instance of Party to be JSON-ized
    :param path: path to the party used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if party.partyIdType is not None:
        res["partyIdType"] = party.partyIdType

    if party.partyId is not None:
        res["partyId"] = party.partyId

    return res


class PreApproval:
    def __init__(
        self,
        payer: Optional[Party] = None,
        payerCurrency: Optional[str] = None,
        payerMessage: Optional[str] = None,
        validityTime: Optional[str] = None,
    ) -> None:
        """Initializes with the given values."""
        self.payer = payer

        # ISO4217 Currency
        self.payerCurrency = payerCurrency

        # The mesage that is shown to the approver.
        self.payerMessage = payerMessage

        # The request validity time of the pre-approval
        self.validityTime = validityTime

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to pre_approval_to_jsonable.

        :return: JSON-able representation
        """
        return pre_approval_to_jsonable(self)


def new_pre_approval() -> PreApproval:
    """Generates an instance of PreApproval with default values."""
    return PreApproval()


def pre_approval_from_obj(obj: Any, path: str = "") -> PreApproval:
    """
    Generates an instance of PreApproval from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of PreApproval
    :param path: path to the object used for debugging
    :return: parsed instance of PreApproval
    """
    if not isinstance(obj, dict):
        raise ValueError(
            "Expected a dict at path {}, but got: {}".format(path, type(obj))
        )

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                "Expected a key of type str at path {}, but got: {}".format(
                    path, type(key)
                )
            )

    if "payer" in obj:
        payer_from_obj = from_obj(
            obj["payer"], expected=[Party], path=path + ".payer"
        )  # type: Optional[Party]
    else:
        payer_from_obj = None

    if "payerCurrency" in obj:
        payerCurrency_from_obj = from_obj(
            obj["payerCurrency"], expected=[str], path=path + ".payerCurrency"
        )  # type: Optional[str]
    else:
        payerCurrency_from_obj = None

    if "payerMessage" in obj:
        payerMessage_from_obj = from_obj(
            obj["payerMessage"], expected=[str], path=path + ".payerMessage"
        )  # type: Optional[str]
    else:
        payerMessage_from_obj = None

    if "validityTime" in obj:
        validityTime_from_obj = from_obj(
            obj["validityTime"], expected=[str], path=path + ".validityTime"
        )  # type: Optional[str]
    else:
        validityTime_from_obj = None

    return PreApproval(
        payer=payer_from_obj,
        payerCurrency=payerCurrency_from_obj,
        payerMessage=payerMessage_from_obj,
        validityTime=validityTime_from_obj,
    )


def pre_approval_to_jsonable(
    pre_approval: PreApproval, path: str = ""
) -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of PreApproval.

    :param pre_approval: instance of PreApproval to be JSON-ized
    :param path: path to the pre_approval used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if pre_approval.payer is not None:
        res["payer"] = to_jsonable(
            pre_approval.payer, expected=[Party], path="{}.payer".format(path)
        )

    if pre_approval.payerCurrency is not None:
        res["payerCurrency"] = pre_approval.payerCurrency

    if pre_approval.payerMessage is not None:
        res["payerMessage"] = pre_approval.payerMessage

    if pre_approval.validityTime is not None:
        res["validityTime"] = pre_approval.validityTime

    return res


class PreApprovalResult:
    def __init__(
        self,
        payer: Optional[Party] = None,
        payerCurrency: Optional[str] = None,
        payerMessage: Optional[str] = None,
        validityTime: Optional[str] = None,
        status: Optional[str] = None,
        reason: Optional[ErrorReason] = None,
    ) -> None:
        """Initializes with the given values."""
        self.payer = payer

        # ISO4217 Currency
        self.payerCurrency = payerCurrency

        # The mesage that is shown to the approver.
        self.payerMessage = payerMessage

        # The request validity time of the pre-approval
        self.validityTime = validityTime

        self.status = status

        self.reason = reason

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to pre_approval_result_to_jsonable.

        :return: JSON-able representation
        """
        return pre_approval_result_to_jsonable(self)


def new_pre_approval_result() -> PreApprovalResult:
    """Generates an instance of PreApprovalResult with default values."""
    return PreApprovalResult()


def pre_approval_result_from_obj(obj: Any, path: str = "") -> PreApprovalResult:
    """
    Generates an instance of PreApprovalResult from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of PreApprovalResult
    :param path: path to the object used for debugging
    :return: parsed instance of PreApprovalResult
    """
    if not isinstance(obj, dict):
        raise ValueError(
            "Expected a dict at path {}, but got: {}".format(path, type(obj))
        )

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                "Expected a key of type str at path {}, but got: {}".format(
                    path, type(key)
                )
            )

    if "payer" in obj:
        payer_from_obj = from_obj(
            obj["payer"], expected=[Party], path=path + ".payer"
        )  # type: Optional[Party]
    else:
        payer_from_obj = None

    if "payerCurrency" in obj:
        payerCurrency_from_obj = from_obj(
            obj["payerCurrency"], expected=[str], path=path + ".payerCurrency"
        )  # type: Optional[str]
    else:
        payerCurrency_from_obj = None

    if "payerMessage" in obj:
        payerMessage_from_obj = from_obj(
            obj["payerMessage"], expected=[str], path=path + ".payerMessage"
        )  # type: Optional[str]
    else:
        payerMessage_from_obj = None

    if "validityTime" in obj:
        validityTime_from_obj = from_obj(
            obj["validityTime"], expected=[str], path=path + ".validityTime"
        )  # type: Optional[str]
    else:
        validityTime_from_obj = None

    if "status" in obj:
        status_from_obj = from_obj(
            obj["status"], expected=[str], path=path + ".status"
        )  # type: Optional[str]
    else:
        status_from_obj = None

    if "reason" in obj:
        reason_from_obj = from_obj(
            obj["reason"], expected=[ErrorReason], path=path + ".reason"
        )  # type: Optional[ErrorReason]
    else:
        reason_from_obj = None

    return PreApprovalResult(
        payer=payer_from_obj,
        payerCurrency=payerCurrency_from_obj,
        payerMessage=payerMessage_from_obj,
        validityTime=validityTime_from_obj,
        status=status_from_obj,
        reason=reason_from_obj,
    )


def pre_approval_result_to_jsonable(
    pre_approval_result: PreApprovalResult, path: str = ""
) -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of PreApprovalResult.

    :param pre_approval_result: instance of PreApprovalResult to be JSON-ized
    :param path: path to the pre_approval_result used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if pre_approval_result.payer is not None:
        res["payer"] = to_jsonable(
            pre_approval_result.payer, expected=[
                Party], path="{}.payer".format(path)
        )

    if pre_approval_result.payerCurrency is not None:
        res["payerCurrency"] = pre_approval_result.payerCurrency

    if pre_approval_result.payerMessage is not None:
        res["payerMessage"] = pre_approval_result.payerMessage

    if pre_approval_result.validityTime is not None:
        res["validityTime"] = pre_approval_result.validityTime

    if pre_approval_result.status is not None:
        res["status"] = pre_approval_result.status

    if pre_approval_result.reason is not None:
        res["reason"] = to_jsonable(
            pre_approval_result.reason,
            expected=[ErrorReason],
            path="{}.reason".format(path),
        )

    return res


class RequestToPay:
    def __init__(
        self,
        amount: Optional[str] = None,
        currency: Optional[str] = None,
        externalId: Optional[str] = None,
        payer: Optional[Party] = None,
        payerMessage: Optional[str] = None,
        payeeNote: Optional[str] = None,
    ) -> None:
        """Initializes with the given values."""
        # Amount that will be debited from the payer account.
        self.amount = amount

        # ISO4217 Currency
        self.currency = currency

        # External id is used as a reference to the transaction. External id is used for reconciliation. The external id will be included in transaction history report. <br>External id is not required to be unique.
        self.externalId = externalId

        self.payer = payer

        # Message that will be written in the payer transaction history message field.
        self.payerMessage = payerMessage

        # Message that will be written in the payee transaction history note field.
        self.payeeNote = payeeNote

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to request_to_pay_to_jsonable.

        :return: JSON-able representation
        """
        return request_to_pay_to_jsonable(self)


def new_request_to_pay() -> RequestToPay:
    """Generates an instance of RequestToPay with default values."""
    return RequestToPay()


def request_to_pay_from_obj(obj: Any, path: str = "") -> RequestToPay:
    """
    Generates an instance of RequestToPay from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of RequestToPay
    :param path: path to the object used for debugging
    :return: parsed instance of RequestToPay
    """
    if not isinstance(obj, dict):
        raise ValueError(
            "Expected a dict at path {}, but got: {}".format(path, type(obj))
        )

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                "Expected a key of type str at path {}, but got: {}".format(
                    path, type(key)
                )
            )

    if "amount" in obj:
        amount_from_obj = from_obj(
            obj["amount"], expected=[str], path=path + ".amount"
        )  # type: Optional[str]
    else:
        amount_from_obj = None

    if "currency" in obj:
        currency_from_obj = from_obj(
            obj["currency"], expected=[str], path=path + ".currency"
        )  # type: Optional[str]
    else:
        currency_from_obj = None

    if "externalId" in obj:
        externalId_from_obj = from_obj(
            obj["externalId"], expected=[str], path=path + ".externalId"
        )  # type: Optional[str]
    else:
        externalId_from_obj = None

    if "payer" in obj:
        payer_from_obj = from_obj(
            obj["payer"], expected=[Party], path=path + ".payer"
        )  # type: Optional[Party]
    else:
        payer_from_obj = None

    if "payerMessage" in obj:
        payerMessage_from_obj = from_obj(
            obj["payerMessage"], expected=[str], path=path + ".payerMessage"
        )  # type: Optional[str]
    else:
        payerMessage_from_obj = None

    if "payeeNote" in obj:
        payeeNote_from_obj = from_obj(
            obj["payeeNote"], expected=[str], path=path + ".payeeNote"
        )  # type: Optional[str]
    else:
        payeeNote_from_obj = None

    return RequestToPay(
        amount=amount_from_obj,
        currency=currency_from_obj,
        externalId=externalId_from_obj,
        payer=payer_from_obj,
        payerMessage=payerMessage_from_obj,
        payeeNote=payeeNote_from_obj,
    )


def request_to_pay_to_jsonable(
    request_to_pay: RequestToPay, path: str = ""
) -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of RequestToPay.

    :param request_to_pay: instance of RequestToPay to be JSON-ized
    :param path: path to the request_to_pay used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if request_to_pay.amount is not None:
        res["amount"] = request_to_pay.amount

    if request_to_pay.currency is not None:
        res["currency"] = request_to_pay.currency

    if request_to_pay.externalId is not None:
        res["externalId"] = request_to_pay.externalId

    if request_to_pay.payer is not None:
        res["payer"] = to_jsonable(
            request_to_pay.payer, expected=[
                Party], path="{}.payer".format(path)
        )

    if request_to_pay.payerMessage is not None:
        res["payerMessage"] = request_to_pay.payerMessage

    if request_to_pay.payeeNote is not None:
        res["payeeNote"] = request_to_pay.payeeNote

    return res


class RequestToPayResult:
    def __init__(
        self,
        amount: Optional[str] = None,
        currency: Optional[str] = None,
        financialTransactionId: Optional[str] = None,
        externalId: Optional[str] = None,
        payer: Optional[Party] = None,
        payerMessage: Optional[str] = None,
        payeeNote: Optional[str] = None,
        status: Optional[str] = None,
        reason: Optional[ErrorReason] = None,
    ) -> None:
        """Initializes with the given values."""
        # Amount that will be debited from the payer account.
        self.amount = amount

        # ISO4217 Currency
        self.currency = currency

        # Financial transactionIdd from mobile money manager.<br> Used to connect to the specific financial transaction made in the account
        self.financialTransactionId = financialTransactionId

        # External id provided in the creation of the requestToPay transaction.
        self.externalId = externalId

        self.payer = payer

        # Message that will be written in the payer transaction history message field.
        self.payerMessage = payerMessage

        # Message that will be written in the payee transaction history note field.
        self.payeeNote = payeeNote

        self.status = status

        self.reason = reason

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to request_to_pay_result_to_jsonable.

        :return: JSON-able representation
        """
        return request_to_pay_result_to_jsonable(self)


def new_request_to_pay_result() -> RequestToPayResult:
    """Generates an instance of RequestToPayResult with default values."""
    return RequestToPayResult()


def request_to_pay_result_from_obj(obj: Any, path: str = "") -> RequestToPayResult:
    """
    Generates an instance of RequestToPayResult from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of RequestToPayResult
    :param path: path to the object used for debugging
    :return: parsed instance of RequestToPayResult
    """
    if not isinstance(obj, dict):
        raise ValueError(
            "Expected a dict at path {}, but got: {}".format(path, type(obj))
        )

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                "Expected a key of type str at path {}, but got: {}".format(
                    path, type(key)
                )
            )

    if "amount" in obj:
        amount_from_obj = from_obj(
            obj["amount"], expected=[str], path=path + ".amount"
        )  # type: Optional[str]
    else:
        amount_from_obj = None

    if "currency" in obj:
        currency_from_obj = from_obj(
            obj["currency"], expected=[str], path=path + ".currency"
        )  # type: Optional[str]
    else:
        currency_from_obj = None

    if "financialTransactionId" in obj:
        financialTransactionId_from_obj = from_obj(
            obj["financialTransactionId"],
            expected=[str],
            path=path + ".financialTransactionId",
        )  # type: Optional[str]
    else:
        financialTransactionId_from_obj = None

    if "externalId" in obj:
        externalId_from_obj = from_obj(
            obj["externalId"], expected=[str], path=path + ".externalId"
        )  # type: Optional[str]
    else:
        externalId_from_obj = None

    if "payer" in obj:
        payer_from_obj = from_obj(
            obj["payer"], expected=[Party], path=path + ".payer"
        )  # type: Optional[Party]
    else:
        payer_from_obj = None

    if "payerMessage" in obj:
        payerMessage_from_obj = from_obj(
            obj["payerMessage"], expected=[str], path=path + ".payerMessage"
        )  # type: Optional[str]
    else:
        payerMessage_from_obj = None

    if "payeeNote" in obj:
        payeeNote_from_obj = from_obj(
            obj["payeeNote"], expected=[str], path=path + ".payeeNote"
        )  # type: Optional[str]
    else:
        payeeNote_from_obj = None

    if "status" in obj:
        status_from_obj = from_obj(
            obj["status"], expected=[str], path=path + ".status"
        )  # type: Optional[str]
    else:
        status_from_obj = None

    if "reason" in obj:
        reason_from_obj = from_obj(
            obj["reason"], expected=[ErrorReason], path=path + ".reason"
        )  # type: Optional[ErrorReason]
    else:
        reason_from_obj = None

    return RequestToPayResult(
        amount=amount_from_obj,
        currency=currency_from_obj,
        financialTransactionId=financialTransactionId_from_obj,
        externalId=externalId_from_obj,
        payer=payer_from_obj,
        payerMessage=payerMessage_from_obj,
        payeeNote=payeeNote_from_obj,
        status=status_from_obj,
        reason=reason_from_obj,
    )


def request_to_pay_result_to_jsonable(
    request_to_pay_result: RequestToPayResult, path: str = ""
) -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of RequestToPayResult.

    :param request_to_pay_result: instance of RequestToPayResult to be JSON-ized
    :param path: path to the request_to_pay_result used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if request_to_pay_result.amount is not None:
        res["amount"] = request_to_pay_result.amount

    if request_to_pay_result.currency is not None:
        res["currency"] = request_to_pay_result.currency

    if request_to_pay_result.financialTransactionId is not None:
        res["financialTransactionId"] = request_to_pay_result.financialTransactionId

    if request_to_pay_result.externalId is not None:
        res["externalId"] = request_to_pay_result.externalId

    if request_to_pay_result.payer is not None:
        res["payer"] = to_jsonable(
            request_to_pay_result.payer, expected=[
                Party], path="{}.payer".format(path)
        )

    if request_to_pay_result.payerMessage is not None:
        res["payerMessage"] = request_to_pay_result.payerMessage

    if request_to_pay_result.payeeNote is not None:
        res["payeeNote"] = request_to_pay_result.payeeNote

    if request_to_pay_result.status is not None:
        res["status"] = request_to_pay_result.status

    if request_to_pay_result.reason is not None:
        res["reason"] = to_jsonable(
            request_to_pay_result.reason,
            expected=[ErrorReason],
            path="{}.reason".format(path),
        )

    return res


class Transfer:
    def __init__(
        self,
        amount: Optional[str] = None,
        currency: Optional[str] = None,
        externalId: Optional[str] = None,
        payee: Optional[Party] = None,
        payerMessage: Optional[str] = None,
        payeeNote: Optional[str] = None,
    ) -> None:
        """Initializes with the given values."""
        # Amount that will be debited from the payer account.
        self.amount = amount

        # ISO4217 Currency
        self.currency = currency

        # External id is used as a reference to the transaction. External id is used for reconciliation. The external id will be included in transaction history report. <br>External id is not required to be unique.
        self.externalId = externalId

        self.payee = payee

        # Message that will be written in the payer transaction history message field.
        self.payerMessage = payerMessage

        # Message that will be written in the payee transaction history note field.
        self.payeeNote = payeeNote

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to transfer_to_jsonable.

        :return: JSON-able representation
        """
        return transfer_to_jsonable(self)


def new_transfer() -> Transfer:
    """Generates an instance of Transfer with default values."""
    return Transfer()


def transfer_from_obj(obj: Any, path: str = "") -> Transfer:
    """
    Generates an instance of Transfer from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of Transfer
    :param path: path to the object used for debugging
    :return: parsed instance of Transfer
    """
    if not isinstance(obj, dict):
        raise ValueError(
            "Expected a dict at path {}, but got: {}".format(path, type(obj))
        )

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                "Expected a key of type str at path {}, but got: {}".format(
                    path, type(key)
                )
            )

    if "amount" in obj:
        amount_from_obj = from_obj(
            obj["amount"], expected=[str], path=path + ".amount"
        )  # type: Optional[str]
    else:
        amount_from_obj = None

    if "currency" in obj:
        currency_from_obj = from_obj(
            obj["currency"], expected=[str], path=path + ".currency"
        )  # type: Optional[str]
    else:
        currency_from_obj = None

    if "externalId" in obj:
        externalId_from_obj = from_obj(
            obj["externalId"], expected=[str], path=path + ".externalId"
        )  # type: Optional[str]
    else:
        externalId_from_obj = None

    if "payee" in obj:
        payee_from_obj = from_obj(
            obj["payee"], expected=[Party], path=path + ".payee"
        )  # type: Optional[Party]
    else:
        payee_from_obj = None

    if "payerMessage" in obj:
        payerMessage_from_obj = from_obj(
            obj["payerMessage"], expected=[str], path=path + ".payerMessage"
        )  # type: Optional[str]
    else:
        payerMessage_from_obj = None

    if "payeeNote" in obj:
        payeeNote_from_obj = from_obj(
            obj["payeeNote"], expected=[str], path=path + ".payeeNote"
        )  # type: Optional[str]
    else:
        payeeNote_from_obj = None

    return Transfer(
        amount=amount_from_obj,
        currency=currency_from_obj,
        externalId=externalId_from_obj,
        payee=payee_from_obj,
        payerMessage=payerMessage_from_obj,
        payeeNote=payeeNote_from_obj,
    )


def transfer_to_jsonable(
    transfer: Transfer, path: str = ""
) -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of Transfer.

    :param transfer: instance of Transfer to be JSON-ized
    :param path: path to the transfer used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if transfer.amount is not None:
        res["amount"] = transfer.amount

    if transfer.currency is not None:
        res["currency"] = transfer.currency

    if transfer.externalId is not None:
        res["externalId"] = transfer.externalId

    if transfer.payee is not None:
        res["payee"] = to_jsonable(
            transfer.payee, expected=[Party], path="{}.payee".format(path)
        )

    if transfer.payerMessage is not None:
        res["payerMessage"] = transfer.payerMessage

    if transfer.payeeNote is not None:
        res["payeeNote"] = transfer.payeeNote

    return res


class TransferResult:
    def __init__(
        self,
        amount: Optional[str] = None,
        currency: Optional[str] = None,
        financialTransactionId: Optional[str] = None,
        externalId: Optional[str] = None,
        payee: Optional[Party] = None,
        payerMessage: Optional[str] = None,
        payeeNote: Optional[str] = None,
        status: Optional[str] = None,
        reason: Optional[ErrorReason] = None,
    ) -> None:
        """Initializes with the given values."""
        # Amount that will be debited from the payer account.
        self.amount = amount

        # ISO4217 Currency
        self.currency = currency

        # Financial transactionIdd from mobile money manager.<br> Used to connect to the specific financial transaction made in the account
        self.financialTransactionId = financialTransactionId

        # External id is used as a reference to the transaction. External id is used for reconciliation. The external id will be included in transaction history report. <br>External id is not required to be unique.
        self.externalId = externalId

        self.payee = payee

        # Message that will be written in the payer transaction history message field.
        self.payerMessage = payerMessage

        # Message that will be written in the payee transaction history note field.
        self.payeeNote = payeeNote

        self.status = status

        self.reason = reason

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to transfer_result_to_jsonable.

        :return: JSON-able representation
        """
        return transfer_result_to_jsonable(self)


def new_transfer_result() -> TransferResult:
    """Generates an instance of TransferResult with default values."""
    return TransferResult()


def transfer_result_from_obj(obj: Any, path: str = "") -> TransferResult:
    """
    Generates an instance of TransferResult from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of TransferResult
    :param path: path to the object used for debugging
    :return: parsed instance of TransferResult
    """
    if not isinstance(obj, dict):
        raise ValueError(
            "Expected a dict at path {}, but got: {}".format(path, type(obj))
        )

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                "Expected a key of type str at path {}, but got: {}".format(
                    path, type(key)
                )
            )

    if "amount" in obj:
        amount_from_obj = from_obj(
            obj["amount"], expected=[str], path=path + ".amount"
        )  # type: Optional[str]
    else:
        amount_from_obj = None

    if "currency" in obj:
        currency_from_obj = from_obj(
            obj["currency"], expected=[str], path=path + ".currency"
        )  # type: Optional[str]
    else:
        currency_from_obj = None

    if "financialTransactionId" in obj:
        financialTransactionId_from_obj = from_obj(
            obj["financialTransactionId"],
            expected=[str],
            path=path + ".financialTransactionId",
        )  # type: Optional[str]
    else:
        financialTransactionId_from_obj = None

    if "externalId" in obj:
        externalId_from_obj = from_obj(
            obj["externalId"], expected=[str], path=path + ".externalId"
        )  # type: Optional[str]
    else:
        externalId_from_obj = None

    if "payee" in obj:
        payee_from_obj = from_obj(
            obj["payee"], expected=[Party], path=path + ".payee"
        )  # type: Optional[Party]
    else:
        payee_from_obj = None

    if "payerMessage" in obj:
        payerMessage_from_obj = from_obj(
            obj["payerMessage"], expected=[str], path=path + ".payerMessage"
        )  # type: Optional[str]
    else:
        payerMessage_from_obj = None

    if "payeeNote" in obj:
        payeeNote_from_obj = from_obj(
            obj["payeeNote"], expected=[str], path=path + ".payeeNote"
        )  # type: Optional[str]
    else:
        payeeNote_from_obj = None

    if "status" in obj:
        status_from_obj = from_obj(
            obj["status"], expected=[str], path=path + ".status"
        )  # type: Optional[str]
    else:
        status_from_obj = None

    if "reason" in obj:
        reason_from_obj = from_obj(
            obj["reason"], expected=[ErrorReason], path=path + ".reason"
        )  # type: Optional[ErrorReason]
    else:
        reason_from_obj = None

    return TransferResult(
        amount=amount_from_obj,
        currency=currency_from_obj,
        financialTransactionId=financialTransactionId_from_obj,
        externalId=externalId_from_obj,
        payee=payee_from_obj,
        payerMessage=payerMessage_from_obj,
        payeeNote=payeeNote_from_obj,
        status=status_from_obj,
        reason=reason_from_obj,
    )


def transfer_result_to_jsonable(
    transfer_result: TransferResult, path: str = ""
) -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of TransferResult.

    :param transfer_result: instance of TransferResult to be JSON-ized
    :param path: path to the transfer_result used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if transfer_result.amount is not None:
        res["amount"] = transfer_result.amount

    if transfer_result.currency is not None:
        res["currency"] = transfer_result.currency

    if transfer_result.financialTransactionId is not None:
        res["financialTransactionId"] = transfer_result.financialTransactionId

    if transfer_result.externalId is not None:
        res["externalId"] = transfer_result.externalId

    if transfer_result.payee is not None:
        res["payee"] = to_jsonable(
            transfer_result.payee, expected=[
                Party], path="{}.payee".format(path)
        )

    if transfer_result.payerMessage is not None:
        res["payerMessage"] = transfer_result.payerMessage

    if transfer_result.payeeNote is not None:
        res["payeeNote"] = transfer_result.payeeNote

    if transfer_result.status is not None:
        res["status"] = transfer_result.status

    if transfer_result.reason is not None:
        res["reason"] = to_jsonable(
            transfer_result.reason,
            expected=[ErrorReason],
            path="{}.reason".format(path),
        )

    return res


def new_error_reason() -> ErrorReason:
    """Generates an instance of ErrorReason with default values."""
    return ErrorReason()


def error_reason_from_obj(obj: Any, path: str = "") -> ErrorReason:
    """
    Generates an instance of ErrorReason from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of ErrorReason
    :param path: path to the object used for debugging
    :return: parsed instance of ErrorReason
    """
    if not isinstance(obj, dict):
        raise ValueError(
            "Expected a dict at path {}, but got: {}".format(path, type(obj))
        )

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                "Expected a key of type str at path {}, but got: {}".format(
                    path, type(key)
                )
            )

    if "code" in obj:
        code_from_obj = from_obj(
            obj["code"], expected=[str], path=path + ".code"
        )  # type: Optional[str]
    else:
        code_from_obj = None

    if "message" in obj:
        message_from_obj = from_obj(
            obj["message"], expected=[str], path=path + ".message"
        )  # type: Optional[str]
    else:
        message_from_obj = None

    return ErrorReason(code=code_from_obj, message=message_from_obj)


def error_reason_to_jsonable(
    error_reason: ErrorReason, path: str = ""
) -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of ErrorReason.

    :param error_reason: instance of ErrorReason to be JSON-ized
    :param path: path to the error_reason used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if error_reason.code is not None:
        res["code"] = error_reason.code

    if error_reason.message is not None:
        res["message"] = error_reason.message

    return res


class BooleanResult:
    def __init__(self, result: Optional[bool] = None) -> None:
        """Initializes with the given values."""
        self.result = result

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to boolean_result_to_jsonable.

        :return: JSON-able representation
        """
        return boolean_result_to_jsonable(self)


def new_boolean_result() -> BooleanResult:
    """Generates an instance of BooleanResult with default values."""
    return BooleanResult()


def boolean_result_from_obj(obj: Any, path: str = "") -> BooleanResult:
    """
    Generates an instance of BooleanResult from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of BooleanResult
    :param path: path to the object used for debugging
    :return: parsed instance of BooleanResult
    """
    if not isinstance(obj, dict):
        raise ValueError(
            "Expected a dict at path {}, but got: {}".format(path, type(obj))
        )

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                "Expected a key of type str at path {}, but got: {}".format(
                    path, type(key)
                )
            )

    if "result" in obj:
        result_from_obj = from_obj(
            obj["result"], expected=[bool], path=path + ".result"
        )  # type: Optional[bool]
    else:
        result_from_obj = None

    return BooleanResult(result=result_from_obj)


def boolean_result_to_jsonable(
    boolean_result: BooleanResult, path: str = ""
) -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of BooleanResult.

    :param boolean_result: instance of BooleanResult to be JSON-ized
    :param path: path to the boolean_result used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if boolean_result.result is not None:
        res["result"] = boolean_result.result

    return res


class RemoteCaller:
    """Executes the remote calls to the server."""

    def __init__(
        self, url_prefix: str, auth: Optional[requests.auth.AuthBase] = None
    ) -> None:
        self.url_prefix = url_prefix
        self.auth = auth

    def token_POST(
        self, ocp_apim_subscription_key: str, authorization: str
    ) -> TokenPost200ApplicationJsonResponse:
        """
        This operation is used to create an access token which can then be used to authorize and authenticate towards the other end-points of the API.

        :param ocp_apim_subscription_key: Subscription key which provides access to this API.
        :param authorization: Basic authentication header containing API user ID and API key. Should be sent in as B64 encoded.

        :return: OK
        """
        url = self.url_prefix + "/collection/token/"

        headers = {}  # type: Dict[str, str]

        headers["Ocp-Apim-Subscription-Key"] = ocp_apim_subscription_key

        headers["Authorization"] = authorization

        resp = requests.request(
            method="post",
            url=url,
            headers=headers,
            auth=self.auth,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(), expected=[TokenPost200ApplicationJsonResponse]
            )

    def get_v1_0_account_balance(
        self,
        ocp_apim_subscription_key: str,
        x_target_environment: str,
        authorization: Optional[str] = None,
    ) -> Balance:
        """
        Get the balance of the account.

        :param ocp_apim_subscription_key: Subscription key which provides access to this API.
        :param x_target_environment: The identifier of the EWP system where the transaction shall be processed. This parameter is used to route the request to the EWP system that will initiate the transaction.
        :param authorization: Authorization header used for Basic authentication and oauth. Format of the header parameter follows the standard for Basic and Bearer. Oauth uses Bearer authentication type where the credential is the received access token.

        :return: Ok
        """
        url = self.url_prefix + "/collection/v1_0/account/balance"

        headers = {}  # type: Dict[str, str]

        headers["Ocp-Apim-Subscription-Key"] = ocp_apim_subscription_key

        if authorization is not None:
            headers["Authorization"] = authorization

        headers["X-Target-Environment"] = x_target_environment

        resp = requests.request(
            method="get",
            url=url,
            headers=headers,
            auth=self.auth,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(obj=resp.json(), expected=[Balance])

    def get_v1_0_accountholder_accountholderidtype_accountholderid_active(
        self,
        ocp_apim_subscription_key: str,
        account_holder_id: str,
        account_holder_id_type: str,
        x_target_environment: str,
        authorization: Optional[str] = None,
    ) -> bytes:
        """
        Operation is used  to check if an account holder is registered and active in the system.

        :param ocp_apim_subscription_key: Subscription key which provides access to this API.
        :param account_holder_id: The party number. Validated according to the party ID type (case Sensitive). <br> msisdn - Mobile Number validated according to ITU-T E.164. Validated with IsMSISDN<br> email - Validated to be a valid e-mail format. Validated with IsEmail<br> party_code - UUID of the party. Validated with IsUuid
        :param account_holder_id_type: Specifies the type of the party ID. Allowed values [msisdn, email, party_code].  <br> accountHolderId should explicitly be in small letters.
        :param x_target_environment: The identifier of the EWP system where the transaction shall be processed. This parameter is used to route the request to the EWP system that will initiate the transaction.
        :param authorization: Authorization header used for Basic authentication and oauth. Format of the header parameter follows the standard for Basic and Bearer. Oauth uses Bearer authentication type where the credential is the received access token.

        :return: Ok. True if account holder is registered and active, false if the account holder is not active or not found
        """
        url = "".join(
            [
                self.url_prefix,
                "/collection/v1_0/accountholder/",
                str(account_holder_id_type),
                "/",
                str(account_holder_id),
                "/active",
            ]
        )

        headers = {}  # type: Dict[str, str]

        headers["Ocp-Apim-Subscription-Key"] = ocp_apim_subscription_key

        if authorization is not None:
            headers["Authorization"] = authorization

        headers["X-Target-Environment"] = x_target_environment

        resp = requests.request(
            method="get",
            url=url,
            headers=headers,
            auth=self.auth,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return resp.content

    def requesttopay_POST(
        self,
        ocp_apim_subscription_key: str,
        x_reference_id: str,
        x_target_environment: str,
        authorization: Optional[str] = None,
        x_callback_url: Optional[str] = None,
        request_to_pay: Optional[RequestToPay] = None,
    ) -> bytes:
        r"""
        This operation is used to request a payment from a consumer (Payer). The payer will be asked to authorize the payment. The transaction will be executed once the payer has authorized the payment. The requesttopay will be in status PENDING until the transaction is authorized or declined by the payer or it is timed out by the system.
         Status of the transaction can be validated by using the GET /requesttopay/\<resourceId\>

        :param ocp_apim_subscription_key: Subscription key which provides access to this API.
        :param x_reference_id: Format - UUID. Recource ID of the created request to pay transaction. This ID is used, for example, validating the status of the request. ‘Universal Unique ID’ for the transaction generated using UUID version 4.
        :param x_target_environment: The identifier of the EWP system where the transaction shall be processed. This parameter is used to route the request to the EWP system that will initiate the transaction.
        :param authorization: Authorization header used for Basic authentication and oauth. Format of the header parameter follows the standard for Basic and Bearer. Oauth uses Bearer authentication type where the credential is the received access token.
        :param x_callback_url: URL to the server where the callback should be sent.
        :param request_to_pay:

        :return:
        """
        url = self.url_prefix + "/collection/v1_0/requesttopay"

        headers = {}  # type: Dict[str, str]

        headers["Ocp-Apim-Subscription-Key"] = ocp_apim_subscription_key

        if authorization is not None:
            headers["Authorization"] = authorization

        if x_callback_url is not None:
            headers["X-Callback-Url"] = x_callback_url

        headers["X-Reference-Id"] = x_reference_id

        headers["X-Target-Environment"] = x_target_environment

        data = None  # type: Optional[Any]
        if request_to_pay != None:
            data = to_jsonable(request_to_pay, expected=[RequestToPay])

        resp = requests.request(
            method="post",
            url=url,
            headers=headers,
            json=data,
            auth=self.auth,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return resp.content

    def requesttopay_referenceId_GET(
        self,
        ocp_apim_subscription_key: str,
        reference_id: str,
        x_target_environment: str,
        authorization: Optional[str] = None,
    ) -> RequestToPayResult:
        """
        This operation is used to get the status of a request to pay. X-Reference-Id that was passed in the post is used as reference to the request.

        :param ocp_apim_subscription_key: Subscription key which provides access to this API.
        :param reference_id: UUID of transaction to get result. Reference id  used when creating the request to pay.
        :param x_target_environment: The identifier of the EWP system where the transaction shall be processed. This parameter is used to route the request to the EWP system that will initiate the transaction.
        :param authorization: Authorization header used for Basic authentication and oauth. Format of the header parameter follows the standard for Basic and Bearer. Oauth uses Bearer authentication type where the credential is the received access token.

        :return: OK. Note that a  failed request to pay will be returned with this status too. The 'status' of the RequestToPayResult can be used to determine the outcome of the request. The 'reason' field can be used to retrieve a cause in case of failure.
        """
        url = "".join(
            [self.url_prefix, "/collection/v1_0/requesttopay/",
                str(reference_id)]
        )

        headers = {}  # type: Dict[str, str]

        headers["Ocp-Apim-Subscription-Key"] = ocp_apim_subscription_key

        if authorization is not None:
            headers["Authorization"] = authorization

        headers["X-Target-Environment"] = x_target_environment

        resp = requests.request(
            method="get",
            url=url,
            headers=headers,
            auth=self.auth,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(obj=resp.json(), expected=[RequestToPayResult])


def from_obj(obj: Any, expected: List[type], path: str = "") -> Any:
    """
    Checks and converts the given obj along the expected types.

    :param obj: to be converted
    :param expected: list of types representing the (nested) structure
    :param path: to the object used for debugging
    :return: the converted object
    """
    if not expected:
        raise ValueError(
            "`expected` is empty, but at least one type needs to be specified."
        )

    exp = expected[0]

    if exp == float:
        if isinstance(obj, int):
            return float(obj)

        if isinstance(obj, float):
            return obj

        raise ValueError(
            "Expected object of type int or float at {!r}, but got {}.".format(
                path, type(obj)
            )
        )

    if exp in [bool, int, str, list, dict]:
        if not isinstance(obj, exp) or not isinstance(obj, expected[-1]):
            raise ValueError(
                "Expected object of type {} at {!r}, but got {}.".format(
                    exp, path, type(obj)
                )
            )

    if exp in [bool, int, float, str]:
        return obj

    if exp == list:
        lst = []  # type: List[Any]
        for i, value in enumerate(obj):
            lst.append(
                from_obj(
                    value, expected=expected[1:], path="{}[{}]".format(path, i))
            )

        return lst

    if exp == dict:
        adict = dict()  # type: Dict[str, Any]
        for key, value in obj.items():
            if not isinstance(key, str):
                raise ValueError(
                    "Expected a key of type str at path {!r}, got: {}".format(
                        path, type(key)
                    )
                )

            adict[key] = from_obj(
                value, expected=expected[1:], path="{}[{!r}]".format(path, key)
            )

        return adict

    if exp == TokenPost200ApplicationJsonResponse:
        return token_post200_application_json_response_from_obj(obj, path=path)

    if exp == TokenPost401ApplicationJsonResponse:
        return token_post401_application_json_response_from_obj(obj, path=path)

    if exp == Balance:
        return balance_from_obj(obj, path=path)

    if exp == Party:
        return party_from_obj(obj, path=path)

    if exp == PreApproval:
        return pre_approval_from_obj(obj, path=path)

    if exp == PreApprovalResult:
        return pre_approval_result_from_obj(obj, path=path)

    if exp == RequestToPay:
        return request_to_pay_from_obj(obj, path=path)

    if exp == RequestToPayResult:
        return request_to_pay_result_from_obj(obj, path=path)

    if exp == Transfer:
        return transfer_from_obj(obj, path=path)

    if exp == TransferResult:
        return transfer_result_from_obj(obj, path=path)

    if exp == ErrorReason:
        return error_reason_from_obj(obj, path=path)

    if exp == BooleanResult:
        return boolean_result_from_obj(obj, path=path)

    raise ValueError("Unexpected `expected` type: {}".format(exp))


def to_jsonable(obj: Any, expected: List[type], path: str = "") -> Any:
    """
    Checks and converts the given object along the expected types to a JSON-able representation.

    :param obj: to be converted
    :param expected: list of types representing the (nested) structure
    :param path: path to the object used for debugging
    :return: JSON-able representation of the object
    """
    if not expected:
        raise ValueError(
            "`expected` is empty, but at least one type needs to be specified."
        )

    exp = expected[0]
    if not isinstance(obj, exp):
        raise ValueError(
            "Expected object of type {} at path {!r}, but got {}.".format(
                exp, path, type(obj)
            )
        )

    # Assert on primitive types to help type-hinting.
    if exp == bool:
        assert isinstance(obj, bool)
        return obj

    if exp == int:
        assert isinstance(obj, int)
        return obj

    if exp == float:
        assert isinstance(obj, float)
        return obj

    if exp == str:
        assert isinstance(obj, str)
        return obj

    if exp == list:
        assert isinstance(obj, list)

        lst = []  # type: List[Any]
        for i, value in enumerate(obj):
            lst.append(
                to_jsonable(
                    value, expected=expected[1:], path="{}[{}]".format(path, i))
            )

        return lst

    if exp == dict:
        assert isinstance(obj, dict)

        adict = dict()  # type: Dict[str, Any]
        for key, value in obj.items():
            if not isinstance(key, str):
                raise ValueError(
                    "Expected a key of type str at path {!r}, got: {}".format(
                        path, type(key)
                    )
                )

            adict[key] = to_jsonable(
                value, expected=expected[1:], path="{}[{!r}]".format(path, key)
            )

        return adict

    if exp == TokenPost200ApplicationJsonResponse:
        assert isinstance(obj, TokenPost200ApplicationJsonResponse)
        return token_post200_application_json_response_to_jsonable(obj, path=path)

    if exp == TokenPost401ApplicationJsonResponse:
        assert isinstance(obj, TokenPost401ApplicationJsonResponse)
        return token_post401_application_json_response_to_jsonable(obj, path=path)

    if exp == Balance:
        assert isinstance(obj, Balance)
        return balance_to_jsonable(obj, path=path)

    if exp == Party:
        assert isinstance(obj, Party)
        return party_to_jsonable(obj, path=path)

    if exp == PreApproval:
        assert isinstance(obj, PreApproval)
        return pre_approval_to_jsonable(obj, path=path)

    if exp == PreApprovalResult:
        assert isinstance(obj, PreApprovalResult)
        return pre_approval_result_to_jsonable(obj, path=path)

    if exp == RequestToPay:
        assert isinstance(obj, RequestToPay)
        return request_to_pay_to_jsonable(obj, path=path)

    if exp == RequestToPayResult:
        assert isinstance(obj, RequestToPayResult)
        return request_to_pay_result_to_jsonable(obj, path=path)

    if exp == Transfer:
        assert isinstance(obj, Transfer)
        return transfer_to_jsonable(obj, path=path)

    if exp == TransferResult:
        assert isinstance(obj, TransferResult)
        return transfer_result_to_jsonable(obj, path=path)

    if exp == ErrorReason:
        assert isinstance(obj, ErrorReason)
        return error_reason_to_jsonable(obj, path=path)

    if exp == BooleanResult:
        assert isinstance(obj, BooleanResult)
        return boolean_result_to_jsonable(obj, path=path)

    raise ValueError("Unexpected `expected` type: {}".format(exp))


# Automatically generated file by swagger_to. DO NOT EDIT OR APPEND ANYTHING!
