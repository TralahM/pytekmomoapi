.. pytekmomoapi documentation master file, created by
   sphinx-quickstart on Tue Oct 13 04:30:53 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Getting Started <contents.rst>
   API Reference <api.rst>


.. role:: pycode(code)
   :language: python

pytekmomoapi Documentation!
========================================
An Opinionated Python SDK for the for the MTN Mobile Money API.
The goal of this SDK library is to enable python developers implement
MTN Mobile Money APIs in a flexible, yet consistent manner.

The Open API is a JSON REST API that is used by Partner systems to access services in the Wallet platform.
The Open API exposes services that are used by e.g. online merchants for managing payments and other financial services.

Getting Started
--------------------
1. Signup for An Account `Here <https://momodeveloper.mtn.com/signup/>`
2. Subscribe to the Products
   On the Products page on our developer portal you should see 4 items you can subscribe to:
   - Collection Widget
   - Collections
   - Disbursements
   - Remittances
3. Manage Your Subscriptions
   Developers are issued a Primary Key and Secondary Key for every product.
   Both primary and secondary Subscription key provides access to the API.
   Without one of them a developer cannot access any of the APIs.
   Subscriptions are stored under the user profile and have no expiry.
4. Generate API User and API Key
   The next thing we need to do is to Provision the API User and API Key using the Sandbox Provisioning API.


Read the `MoMo API Documentation <https://momodeveloper.mtn.com/api-documentation/>` for
more details.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
