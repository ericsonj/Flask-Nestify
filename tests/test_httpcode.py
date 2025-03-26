import flask
from flask_nestify.httpcode import HttpCode, HttpCodeProcessor


class TestHttpCodeProcessor:

    def test_http_code(self):

        @HttpCode(200)
        def test_func():
            pass

        query_proc = HttpCodeProcessor(test_func)
        response = flask.Response()
        query_proc.process({}, response)
        assert response.status_code == 200

    def test_http_code_multiple_decorators(self):

        @HttpCode(200)
        @HttpCode(201)
        def test_func():
            pass

        query_proc = HttpCodeProcessor(test_func)
        response = flask.Response()
        query_proc.process({}, response)
        assert response.status_code == 201
