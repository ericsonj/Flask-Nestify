import base64
from typing import Tuple
from flask_nestify.decorator import BasicAuth
from flask_nestify.core import WrapperFunc
from flask_nestify.exception import BadRequestException
from . import app


class TestBasicAuth:

    def test_basic_auth_decorator(self):

        basic_auth = base64.b64encode(b"test:test").decode("utf-8")

        def validation(username, password):
            assert username == "test"
            assert password == "test"
            return (username, password)

        class Test:
            @BasicAuth("user", validation)
            def test_func(self, user: Tuple[str, str]):
                assert user[0] == "test"
                assert user[1] == "test"
                return "", 200

        with app.test_request_context(headers={"Authorization": f"Basic {basic_auth}"}):
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            wrapper_func()

    def test_basic_auth_decorator_no_auth(self):

        def validation(username, password):
            return None

        class Test:
            @BasicAuth("user", validation)
            def test_func(self, user: Tuple[str, str]):
                assert user is None
                return "", 200

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            wrapper_func()

    def test_basic_auth_decorator_invalid_auth(self):

        def validation(username, password):
            return None

        class Test:
            @BasicAuth("user", validation)
            def test_func(self, user: Tuple[str, str]):
                assert user is None
                return "", 200

        with app.test_request_context(headers={"Authorization": "Basic"}):
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except BadRequestException as e:
                assert True
                assert str(e) == "Invalid Authorization header"
