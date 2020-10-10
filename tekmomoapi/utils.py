import base64
import uuid


def get_authorization_str(api_user_id: str, api_user_key: str) -> str:
    bytestr = base64.b64encode(bytes(api_user_id + ":" + api_user_key, "utf8"))
    return "Basic " + bytestr.decode("utf8")


def get_random_uuid_str():
    return str(uuid.uuid4())
