from unittest import TestCase

from tests.compat import mock
from mbq import tokens


class DecoderTest(TestCase):

    def test_init_public_key_required(self):
        with self.assertRaises(tokens.TokenError):
            tokens.Decoder(allowed_audiences=[])

    def test_init_allowed_audiences(self):
        with self.assertRaises(tokens.TokenError):
            tokens.Decoder(public_key='test', allowed_audiences='test')

        with self.assertRaises(tokens.TokenError):
            tokens.Decoder(public_key='test', allowed_audiences=[1, 2, 3])

        audiences = ['test1', 'test2', 'test3']
        tokens.Decoder(public_key='test', allowed_audiences=set(audiences))
        tokens.Decoder(public_key='test', allowed_audiences=list(audiences))
        tokens.Decoder(public_key='test', allowed_audiences=tuple(audiences))

    def test_decode(self):
        pass

    def test_decode_header_bad_header(self):
        decoder = tokens.Decoder(public_key='test', allowed_audiences={'test'})
        decoder.decode = mock.MagicMock()

        with self.assertRaises(tokens.TokenError):
            decoder.decode_header(None)
        self.assertEqual(decoder.decode.call_count, 0)

        with self.assertRaises(tokens.TokenError):
            decoder.decode_header('test')
        self.assertEqual(decoder.decode.call_count, 0)

        with self.assertRaises(tokens.TokenError):
            decoder.decode_header('test test test')
        self.assertEqual(decoder.decode.call_count, 0)

        with self.assertRaises(tokens.TokenError):
            # doesn't start with Bearer
            decoder.decode_header('test test')
        self.assertEqual(decoder.decode.call_count, 0)

    def test_decode_header_extra_whitespace(self):
        decoder = tokens.Decoder(public_key='test', allowed_audiences={'test'})
        decoder.decode = mock.MagicMock()

        decoder.decode_header('   Bearer     test  ')
        args, kwargs = decoder.decode.call_args
        self.assertEqual(args[0], 'test')

    def test_decode_header_case_insensitive_bearer(self):
        decoder = tokens.Decoder(public_key='test', allowed_audiences={'test'})
        decoder.decode = mock.MagicMock()

        decoder.decode_header('bearer test')
        args, kwargs = decoder.decode.call_args
        self.assertEqual(args[0], 'test')
