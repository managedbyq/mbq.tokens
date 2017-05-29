import jwt
import six

from . import exceptions


class Decoder:
    def __init__(self, public_key=None, allowed_audiences=None):
        if not public_key:
            raise exceptions.TokenError('`public_key` must be a valid public key')

        err_msg = '`allowed_audiences` must be a list, tuple, or set of strings'
        if not isinstance(allowed_audiences, (list, tuple, set)):
            raise exceptions.TokenError(err_msg)

        if any(not isinstance(aud, six.string_types) for aud in allowed_audiences):
            raise exceptions.TokenError(err_msg)

        self._public_key = public_key
        self._allowed_audiences = set(allowed_audiences)

    def decode(self, token):
        try:
            decoded_token = jwt.decode(
                token,
                key=self._public_key,
                options={'verify_aud': False},
                algorithms=['RS256'],
            )
        except:
            raise exceptions.TokenError('`token` could not be decoded')

        if decoded_token['aud'] not in self._allowed_audiences:
            raise exceptions.TokenError('`aud` claim is not in allowed_audiences')

        return decoded_token

    def decode_header(self, header):
        err_msg = '`header` must be a string in the form "Bearer <token>"'

        if not isinstance(header, six.string_types):
            raise exceptions.TokenError(err_msg)

        try:
            bearer, token = header.strip().split()
        except ValueError:
            raise exceptions.TokenError(err_msg)

        if bearer.lower() != 'bearer':
            raise exceptions.TokenError(err_msg)

        return self.decode(token)
