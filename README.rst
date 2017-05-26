mbq.tokens: fool-proof token decoding
=====================================

Installation
------------

.. code-block:: bash

    $ pip install mbq.tokens
    🚀✨

Guaranteed fresh.


Getting started
---------------

.. code-block:: python

    from mbq import tokens

    tokens.init(
        public_key=settings.PUBLIC_KEY,
        allowed_audiences=set(settings.ALLOWED_AUDIENCES),
    )

    try:
        decoded_token = tokens.decode(token)
    except tokens.TokenError:
        # will only ever raise TokenError
        logger.exception('Failed to decode token')

    decoded_token = tokens.decode_header(request.META['HTTP_AUTHORIZATION'])
