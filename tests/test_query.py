from flask_nestify.decorator import Query
from flask_nestify.query import QueryProcessor
from . import app


class TestQueryProcessor:

    def test_query(self):

        @Query(name="a")
        def test_func(a: str):
            pass

        test_url = "/test/url?a=test"
        with app.test_request_context(test_url):
            query_proc = QueryProcessor(test_func)
            kwargs = {}
            query_proc.process(kwargs)
            assert kwargs["a"] == "test"

    def test_query_no_args(self):

        @Query(name="a")
        def test_func():
            pass

        test_url = "/test/url"
        with app.test_request_context(test_url):
            query_proc = QueryProcessor(test_func)
            kwargs = {}
            query_proc.process(kwargs)
            assert "a" not in kwargs

    def test_query_with_default_value(self):

        @Query(name="sortBy")
        def test_func(sortBy: str = "default"):
            pass

        test_url = "/test/url"
        with app.test_request_context(test_url):
            query_proc = QueryProcessor(test_func)
            kwargs = {}
            query_proc.process(kwargs)
            assert kwargs["sortBy"] == "default"

    def test_query_multiple_queries(self):

        @Query(name="a")
        @Query(name="b")
        def test_func(a: str, b: str):
            pass

        test_url = "/test/url?a=a&b=b"
        with app.test_request_context(test_url):
            query_proc = QueryProcessor(test_func)
            kwargs = {}
            query_proc.process(kwargs)
            assert "a" in kwargs
            assert "b" in kwargs
            assert kwargs["a"] == "a"
            assert kwargs["b"] == "b"
