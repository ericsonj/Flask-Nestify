import flask
from flask_nestify.exception import InternalServerErrorException
from flask_nestify.response import (
    DefaultResponse,
    Response,
    ResponseProcessor,
)


class TestResponse:

    def test_response_middleware_return_str(self):
        default_response = DefaultResponse()
        response = flask.Response()
        response = default_response.get_response(response, "test")
        assert str(response.response) == "test"

    def test_response_middleware_return_int(self):
        default_response = DefaultResponse()
        response = flask.Response()
        response = default_response.get_response(response, 200)
        assert response.content_type == "text/html; charset=utf-8"
        assert int(response.data) == 200

    def test_response_middleware_return_dict(self):
        default_response = DefaultResponse()
        response = flask.Response()
        response = default_response.get_response(response, {"test": "test"})
        assert response.content_type == "application/json"
        assert response.json == {"test": "test"}

    def test_response_middleware_return_dict_with_object(self):
        default_response = DefaultResponse()
        response = flask.Response()

        class TestClass:
            def __init__(self, test):
                self.test = test

        test = TestClass("test")

        response = default_response.get_response(
            response, {"test": "test", "object": test}
        )
        assert response.content_type == "application/json"
        assert response.json == {"test": "test", "object": {"test": "test"}}

    def test_response_middleware_return_list(self):
        default_response = DefaultResponse()
        response = flask.Response()
        response = default_response.get_response(response, ["test"])
        assert response.content_type == "application/json"
        assert response.json == ["test"]

    def test_response_middleware_return_list_with_object(self):
        default_response = DefaultResponse()
        response = flask.Response()

        class TestClass:
            def __init__(self, test):
                self.test = test

        test = TestClass("test")

        response = default_response.get_response(response, ["test", test])
        assert response.content_type == "application/json"
        assert response.json == ["test", {"test": "test"}]

    def test_response_middleware_return_object_list(self):
        default_response = DefaultResponse()
        response = flask.Response()
        response = default_response.get_response(response, [{"test": "test"}])
        assert response.content_type == "application/json"
        assert response.json == [{"test": "test"}]

    def test_response_middleware_return_tuple(self):
        default_response = DefaultResponse()
        response = flask.Response()
        response = default_response.get_response(response, ("test", 201))
        assert response.content_type == "text/html; charset=utf-8"
        assert str(response.response) == "test"
        assert response.status_code == 201

    def test_response_middleware_return_tuple_with_tuple(self):
        default_response = DefaultResponse()
        response = flask.Response()
        response = default_response.get_response(response, (("a", "b"), 201))
        assert response.content_type == "text/html; charset=utf-8"
        assert str(response.response) == "('a', 'b')"
        assert response.status_code == 201

    def test_response_middleware_return_flask_response(self):
        default_response = DefaultResponse()
        response = flask.Response()
        response = default_response.get_response(response, flask.Response())
        assert response.content_type == "text/html; charset=utf-8"
        assert response.status_code == 200

    def test_response_middleware_return_object(self):
        default_response = DefaultResponse()
        response = flask.Response()

        class TestObject:
            def __init__(self, test):
                self.test = test

            def to_json(self):
                return {"test": self.test}

        response = default_response.get_response(response, TestObject("test"))
        assert response.content_type == "application/json"

        assert response.json == {"test": "test"}

    def test_response_middleware_return_object_with_toJSON(self):
        default_response = DefaultResponse()
        response = flask.Response()

        class TestObject:
            def __init__(self, test):
                self.test = test

            def toJSON(self):
                return {"test": self.test}

        response = default_response.get_response(response, TestObject("test"))
        assert response.content_type == "application/json"
        assert response.json == {"test": "test"}

    def test_response_middleware_return_object_not_serializable(self):
        default_response = DefaultResponse()
        response = flask.Response()

        class TestObject:
            def __init__(self, test):
                self.test = test

        response = default_response.get_response(response, TestObject("test"))
        assert response.content_type == "application/json"
        assert response.json == {"test": "test"}

    def test_response_middleware_return_response_unknown(self):
        default_response = DefaultResponse()
        response = flask.Response()

        try:
            default_response.get_response(response, 12j)
            assert False
        except InternalServerErrorException as e:
            assert str(e) == "Unknown response type"

    def test_response_decorator(self):

        @Response("response")
        def test_fun(response):
            pass

        response_processor = ResponseProcessor(test_fun)
        kwargs = {}
        response = flask.Response()
        response_processor.process(kwargs, response)
        assert kwargs["response"] == response

    def test_response_decorator_multiple_definitions(self):

        @Response("response")
        @Response("response")
        def test_fun(response):
            pass

        response_processor = ResponseProcessor(test_fun)
        kwargs = {}
        response = flask.Response()
        response_processor.process(kwargs, response)
        assert kwargs["response"] == response
