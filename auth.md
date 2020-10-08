- SubscriptionKey
- API User and API key for Oauth 2.0


Subscription key is used to give access to APIs in the API Manager Portal. A
user is assigned a subscription key as and when the user subscribes to products
in the API manager portal.


The API user and API key are used to gant access to the wallet system in a
specific country. API user and Key are wholly managed by the merchant through
the Partner portal.

Mechants ar allowed to generate/revoke API keys via the Patner Portal.
On a sandbox environment a provisioning api key is exposed to enable developers
generate their own API User and API Key for testing purposes only.


## Subscription Key
Part of the header of all requests sent to the API Manager.

```python

headers={
    "Ocp-Apim-Subscription-Key": SubscriptionKey,
}

```

part of the header.


# API User and API Key Provisioning.
## Sandbox Provisioning
#### Create API User
1. The Provider sends a POST {baseURL}/apiuser request to Wallet platform.

2. The Provider specifies the UUID Reference ID in the request Header and the subscription Key.

3. Reference ID will be used as the User ID for the API user to be created.

4. Wallet Platform creates the User and responds with 201

Example
Request:

POST {baseURL}/apiuser HTTP/1.1

Host: momodeveloper.mtn.com

X-Reference-Id: c72025f5-5cd1-4630-99e4-8ba4722fad56

Ocp-Apim-Subscription-Key: d484a1f0d34f4301916d0f2c9e9106a2{"providerCallbackHost": "clinic.com"}

Response:

201 Created
#### Create API Key
1. The Provider sends a POST {baseURL}/apiuser/{APIUser}/apikey request to Wallet platform.

2. The Provider specifies the API User in the URL and subscription Key in the header.

3. Wallet Platform creates the API Key and responds with 201 Created with the newly Created API Key in the Body.

4. Provider now has both API User and API Key created.

Example
Request:

POST {baseURL}/apiuser/c72025f5-5cd1-4630-99e4-8ba4722fad56/apikey HTTP/1.1

Host: momodeveloper.mtn.com

Ocp-Apim-Subscription-Key: d484a1f0d34f4301916d0f2c9e9106a2

Response:

```
HTTP/1.1 201 Created
date: Wed, 10 Oct 2018 09:16:15 GMT
content-type: application/json;charset=utf-8
content-length: 45
{
    "apiKey": "f1db798c98df4bcf83b538175893bbf0"
}
```

## GET API User Details
It is possible to fetch API user details such as Call Back Host. However, it is not possible to fetch the API key.

Provider shall be required to generate a new Key should they lose the existing one.

#### Get API User Details
a) The Provider sends a GET {baseURL}/apiuser/{APIUser} request to Wallet platform.

b) The Provider specifies the API User in the URL and subscription Key in the header.

c) Wallet Platform responds with 200 Ok and details of the user.

d) TargetEnvironment is preconfigured to sandbox in the Sandbox environment, therefore Providers will not have the option of setting it to a different parameter.

Example
GET {baseURL}/apiuser/ c72025f5-5cd1-4630-99e4-8ba4722fad56

Host: momodeveloper.mtn.com

Ocp-Apim-Subscription-Key: d484a1f0d34f4301916d0f2c9e9106a2

Response:

```
HTTP/1.1 200 Accepted
        date: Wed, 10 Oct 2018 09:16:15 GMT
        {
        "providerCallbackHost": "clinic.com",
        "targetEnvironment": "sandbox"
        }
```

# Oauth 2.0

1. Provider system requests an access token using the API Key and API user as authentication.
2. Wallet platform authenticates credentials and responds with the access token
3. Provider system will use the access token for any request that is sent to Wallet Platform, e.g. POST /requesttopay


Note: The same token shall be used if it is not expired.


PUT method is used on the provided callback_urls in a POST Request.

From Server PUT /callback_url
