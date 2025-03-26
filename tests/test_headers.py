from flask_nestify.core import WrapperFunc
from flask_nestify.headers import Headers, HeadersProcessor, HeadersV2
from . import app


class TestHeadersProcessor:

    def test_header_decorator(self):

        @Headers(name="headers")
        def test_func(headers: dict):
            pass

        with app.test_request_context(
            headers={
                "User-Agent": "Mozilla/5.0",
            }
        ):
            headers_proc = HeadersProcessor(test_func)
            kwargs = {}
            headers_proc.process(kwargs)
            assert kwargs["headers"]["User-Agent"] == "Mozilla/5.0"

    def test_header_decorator_double_definition(self):

        @Headers(name="headers")
        @Headers(name="headers")
        def test_func(headers: dict):
            pass

        with app.test_request_context(
            headers={
                "User-Agent": "Mozilla/5.0",
            }
        ):
            headers_proc = HeadersProcessor(test_func)
            kwargs = {}
            headers_proc.process(kwargs)
            assert kwargs["headers"]["User-Agent"] == "Mozilla/5.0"

    def test_header_v2_decorator(self):

        class Test:
            @HeadersV2(name="request_headers")
            def test_func(self, request_headers):
                assert request_headers["User-Agent"] == "Mozilla/5.0"
                return "", 200

        with app.test_request_context(
            headers={
                "User-Agent": "Mozilla/5.0",
            }
        ):
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            wrapper_func()
