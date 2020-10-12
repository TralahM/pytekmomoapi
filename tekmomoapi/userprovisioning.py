#!/usr/bin/env python3
# Automatically generated file by swagger_to. DO NOT EDIT OR APPEND ANYTHING!
"""Implements the client for userprovisioning."""

# pylint: skip-file
# pydocstyle: add-ignore=D105,D107,D401

import contextlib
import json
from typing import Any, BinaryIO, Dict, List, MutableMapping, Optional, cast

import requests
import requests.auth


class TargetEnvironment:
    def __init__(self, apiKey: Optional[str] = None) -> None:
        """Initializes with the given values."""
        # The target environment
        self.apiKey = apiKey

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to target_environment_to_jsonable.

        :return: JSON-able representation
        """
        return target_environment_to_jsonable(self)


class PaymentServerUrl:
    def __init__(self, apiKey: Optional[str] = None) -> None:
        """Initializes with the given values."""
        # The payment server URL
        self.apiKey = apiKey

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to payment_server_url_to_jsonable.

        :return: JSON-able representation
        """
        return payment_server_url_to_jsonable(self)


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


class ApiUser:
    """The create API user information"""

    def __init__(self, providerCallbackHost: Optional[str] = None) -> None:
        """Initializes with the given values."""
        # The provider callback host
        self.providerCallbackHost = providerCallbackHost

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to api_user_to_jsonable.

        :return: JSON-able representation
        """
        return api_user_to_jsonable(self)


def new_api_user() -> ApiUser:
    """Generates an instance of ApiUser with default values."""
    return ApiUser()


def api_user_from_obj(obj: Any, path: str = "") -> ApiUser:
    """
    Generates an instance of ApiUser from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of ApiUser
    :param path: path to the object used for debugging
    :return: parsed instance of ApiUser
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

    if "providerCallbackHost" in obj:
        providerCallbackHost_from_obj = from_obj(
            obj["providerCallbackHost"],
            expected=[str],
            path=path + ".providerCallbackHost",
        )  # type: Optional[str]
    else:
        providerCallbackHost_from_obj = None

    return ApiUser(providerCallbackHost=providerCallbackHost_from_obj)


def api_user_to_jsonable(api_user: ApiUser, path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of ApiUser.

    :param api_user: instance of ApiUser to be JSON-ized
    :param path: path to the api_user used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if api_user.providerCallbackHost is not None:
        res["providerCallbackHost"] = api_user.providerCallbackHost

    return res


class ApiUserResult:
    """The API user information"""

    def __init__(
        self,
        providerCallbackHost: Optional[str] = None,
        paymentServerUrl: Optional[PaymentServerUrl] = None,
        targetEnvironment: Optional[TargetEnvironment] = None,
    ) -> None:
        """Initializes with the given values."""
        # The provider callback host
        self.providerCallbackHost = providerCallbackHost

        self.paymentServerUrl = paymentServerUrl

        self.targetEnvironment = targetEnvironment

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to api_user_result_to_jsonable.

        :return: JSON-able representation
        """
        return api_user_result_to_jsonable(self)


def new_api_user_result() -> ApiUserResult:
    """Generates an instance of ApiUserResult with default values."""
    return ApiUserResult()


def api_user_result_from_obj(obj: Any, path: str = "") -> ApiUserResult:
    """
    Generates an instance of ApiUserResult from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of ApiUserResult
    :param path: path to the object used for debugging
    :return: parsed instance of ApiUserResult
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

    if "providerCallbackHost" in obj:
        providerCallbackHost_from_obj = from_obj(
            obj["providerCallbackHost"],
            expected=[str],
            path=path + ".providerCallbackHost",
        )  # type: Optional[str]
    else:
        providerCallbackHost_from_obj = None

    if "paymentServerUrl" in obj:
        paymentServerUrl_from_obj = from_obj(
            obj["paymentServerUrl"],
            expected=[PaymentServerUrl],
            path=path + ".paymentServerUrl",
        )  # type: Optional[PaymentServerUrl]
    else:
        paymentServerUrl_from_obj = None

    if "targetEnvironment" in obj:
        targetEnvironment_from_obj = from_obj(
            obj["targetEnvironment"],
            expected=[TargetEnvironment],
            path=path + ".targetEnvironment",
        )  # type: Optional[TargetEnvironment]
    else:
        targetEnvironment_from_obj = None

    return ApiUserResult(
        providerCallbackHost=providerCallbackHost_from_obj,
        paymentServerUrl=paymentServerUrl_from_obj,
        targetEnvironment=targetEnvironment_from_obj,
    )


def api_user_result_to_jsonable(
    api_user_result: ApiUserResult, path: str = ""
) -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of ApiUserResult.

    :param api_user_result: instance of ApiUserResult to be JSON-ized
    :param path: path to the api_user_result used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if api_user_result.providerCallbackHost is not None:
        res["providerCallbackHost"] = api_user_result.providerCallbackHost

    if api_user_result.paymentServerUrl is not None:
        res["paymentServerUrl"] = to_jsonable(
            api_user_result.paymentServerUrl,
            expected=[PaymentServerUrl],
            path="{}.paymentServerUrl".format(path),
        )

    if api_user_result.targetEnvironment is not None:
        res["targetEnvironment"] = to_jsonable(
            api_user_result.targetEnvironment,
            expected=[TargetEnvironment],
            path="{}.targetEnvironment".format(path),
        )

    return res


class ApiUserKeyResult:
    def __init__(self, apiKey: Optional[str] = None) -> None:
        """Initializes with the given values."""
        # The created API user key
        self.apiKey = apiKey

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to api_user_key_result_to_jsonable.

        :return: JSON-able representation
        """
        return api_user_key_result_to_jsonable(self)


def new_api_user_key_result() -> ApiUserKeyResult:
    """Generates an instance of ApiUserKeyResult with default values."""
    return ApiUserKeyResult()


def api_user_key_result_from_obj(obj: Any, path: str = "") -> ApiUserKeyResult:
    """
    Generates an instance of ApiUserKeyResult from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of ApiUserKeyResult
    :param path: path to the object used for debugging
    :return: parsed instance of ApiUserKeyResult
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

    if "apiKey" in obj:
        apiKey_from_obj = from_obj(
            obj["apiKey"], expected=[str], path=path + ".apiKey"
        )  # type: Optional[str]
    else:
        apiKey_from_obj = None

    return ApiUserKeyResult(apiKey=apiKey_from_obj)


def api_user_key_result_to_jsonable(
    api_user_key_result: ApiUserKeyResult, path: str = ""
) -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of ApiUserKeyResult.

    :param api_user_key_result: instance of ApiUserKeyResult to be JSON-ized
    :param path: path to the api_user_key_result used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if api_user_key_result.apiKey is not None:
        res["apiKey"] = api_user_key_result.apiKey

    return res


def new_payment_server_url() -> PaymentServerUrl:
    """Generates an instance of PaymentServerUrl with default values."""
    return PaymentServerUrl()


def payment_server_url_from_obj(obj: Any, path: str = "") -> PaymentServerUrl:
    """
    Generates an instance of PaymentServerUrl from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of PaymentServerUrl
    :param path: path to the object used for debugging
    :return: parsed instance of PaymentServerUrl
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

    if "apiKey" in obj:
        apiKey_from_obj = from_obj(
            obj["apiKey"], expected=[str], path=path + ".apiKey"
        )  # type: Optional[str]
    else:
        apiKey_from_obj = None

    return PaymentServerUrl(apiKey=apiKey_from_obj)


def payment_server_url_to_jsonable(
    payment_server_url: PaymentServerUrl, path: str = ""
) -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of PaymentServerUrl.

    :param payment_server_url: instance of PaymentServerUrl to be JSON-ized
    :param path: path to the payment_server_url used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if payment_server_url.apiKey is not None:
        res["apiKey"] = payment_server_url.apiKey

    return res


def new_target_environment() -> TargetEnvironment:
    """Generates an instance of TargetEnvironment with default values."""
    return TargetEnvironment()


def target_environment_from_obj(obj: Any, path: str = "") -> TargetEnvironment:
    """
    Generates an instance of TargetEnvironment from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of TargetEnvironment
    :param path: path to the object used for debugging
    :return: parsed instance of TargetEnvironment
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

    if "apiKey" in obj:
        apiKey_from_obj = from_obj(
            obj["apiKey"], expected=[str], path=path + ".apiKey"
        )  # type: Optional[str]
    else:
        apiKey_from_obj = None

    return TargetEnvironment(apiKey=apiKey_from_obj)


def target_environment_to_jsonable(
    target_environment: TargetEnvironment, path: str = ""
) -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of TargetEnvironment.

    :param target_environment: instance of TargetEnvironment to be JSON-ized
    :param path: path to the target_environment used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    if target_environment.apiKey is not None:
        res["apiKey"] = target_environment.apiKey

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


class RemoteCaller:
    """Executes the remote calls to the server."""

    def __init__(
        self, url_prefix: str, auth: Optional[requests.auth.AuthBase] = None
    ) -> None:
        self.url_prefix = url_prefix
        self.auth = auth

    def post_v1_0_apiuser(
        self,
        ocp_apim_subscription_key: str,
        x_reference_id: str,
        api_user: Optional[ApiUser] = None,
    ) -> bytes:
        """
        Used to create an API user in the sandbox target environment.

        :param ocp_apim_subscription_key: Subscription key which provides access to this API.
        :param x_reference_id: Format - UUID. Recource ID for the API user to be created. UUID version 4 is required.
        :param api_user:

        :return:
        """
        url = self.url_prefix + "/v1_0/apiuser"

        headers = {}  # type: Dict[str, str]

        headers["Ocp-Apim-Subscription-Key"] = ocp_apim_subscription_key

        headers["X-Reference-Id"] = x_reference_id
        headers["Content-Type"] = "application/json"

        # data = None  # type: Optional[Any]
        if api_user != None:
            data = to_jsonable(api_user, expected=[ApiUser])
        else:
            data = {"providerCallbackHost": "localhost"}

        resp = requests.post(
            url=url,
            headers=headers,
            data=str(data),
            # auth=self.auth,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return resp.content

    def post_v1_0_apiuser_apikey(
        self, ocp_apim_subscription_key: str, x_reference_id: str
    ) -> bytes:
        """
        Use to create an API key for an API user in the sandbox target environment.

        :param ocp_apim_subscription_key: Subscription key which provides access to this API.
        :param x_reference_id: Format - UUID. Recource ID for the API user to be created. UUID version 4 is required.

        :return:
        """
        url = self.url_prefix + f"/v1_0/apiuser/{x_reference_id}/apikey"

        headers = {}  # type: Dict[str, str]

        headers["Ocp-Apim-Subscription-Key"] = ocp_apim_subscription_key

        resp = requests.request(
            method="post",
            url=url,
            headers=headers,
            auth=self.auth,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return resp.content

    def get_v1_0_apiuser(
        self, ocp_apim_subscription_key: str, x_reference_id: str
    ) -> dict:
        """
        Used to get API user information.

        :param ocp_apim_subscription_key: Subscription key which provides access to this API.
        :param x_reference_id: Format - UUID. Recource ID for the API user to be created. UUID version 4 is required.

        :return: Ok
        """
        url = self.url_prefix + f"/v1_0/apiuser/{x_reference_id}"

        headers = {}  # type: Dict[str, str]

        headers["Ocp-Apim-Subscription-Key"] = ocp_apim_subscription_key

        resp = requests.request(
            method="get",
            url=url,
            headers=headers,
            auth=self.auth,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return json.loads(resp.content)


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
        if not isinstance(obj, exp):
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

    if exp == ApiUser:
        return api_user_from_obj(obj, path=path)

    if exp == ApiUserResult:
        return api_user_result_from_obj(obj, path=path)

    if exp == ApiUserKeyResult:
        return api_user_key_result_from_obj(obj, path=path)

    if exp == PaymentServerUrl:
        return payment_server_url_from_obj(obj, path=path)

    if exp == TargetEnvironment:
        return target_environment_from_obj(obj, path=path)

    if exp == ErrorReason:
        return error_reason_from_obj(obj, path=path)

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

    if exp == ApiUser:
        assert isinstance(obj, ApiUser)
        return api_user_to_jsonable(obj, path=path)

    if exp == ApiUserResult:
        assert isinstance(obj, ApiUserResult)
        return api_user_result_to_jsonable(obj, path=path)

    if exp == ApiUserKeyResult:
        assert isinstance(obj, ApiUserKeyResult)
        return api_user_key_result_to_jsonable(obj, path=path)

    if exp == PaymentServerUrl:
        assert isinstance(obj, PaymentServerUrl)
        return payment_server_url_to_jsonable(obj, path=path)

    if exp == TargetEnvironment:
        assert isinstance(obj, TargetEnvironment)
        return target_environment_to_jsonable(obj, path=path)

    if exp == ErrorReason:
        assert isinstance(obj, ErrorReason)
        return error_reason_to_jsonable(obj, path=path)

    raise ValueError("Unexpected `expected` type: {}".format(exp))


# Automatically generated file by swagger_to. DO NOT EDIT OR APPEND ANYTHING!
