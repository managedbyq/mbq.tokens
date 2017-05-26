import jwt

from . import exceptions


class Decoder:
    def __init__(self, public_key=None, allowed_audiences=None):
        if not public_key:
            raise exceptions.TokenError('`public_key` must be a valid public key')

        if not isinstance(allowed_audiences, (list, tuple, set)):
            raise exceptions.TokenError('`allowed_audiences` must be a list, tuple, or set')

        # TODO what other heuristcs should we have to prevent people
        # from doing bad things?
        self._public_key = public_key
        self._allowed_audiences = allowed_audiences

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
        bearer, token = header.strip().split()

        if bearer.lower != 'bearer':
            raise exceptions.TokenError('`header` must be in the form "Bearer <token>"')

        return self.decode(token)
