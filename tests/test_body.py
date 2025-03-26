from flask_nestify.body import BodyProcessor
from flask_nestify.decorator import Body, Dto
from . import app


class TestBodyProcessor:

    def test_body_processor_with_dto(self):

        @Dto()
        class TestDto:
            def __init__(self, a: int, b: str):
                self.a = a
                self.b = b

        @Body("a")
        def test_func(a: TestDto):
            pass

        with app.test_request_context(json={"a": 1, "b": "test"}):
            body_proc = BodyProcessor(test_func)
            kwargs = {}
            body_proc.process(kwargs)
            assert kwargs["a"].a == 1
            assert kwargs["a"].b == "test"

    def test_body_processor_with_str_body(self):

        @Body("a")
        def test_func(a: str):
            pass

        with app.test_request_context(data="string body"):
            body_proc = BodyProcessor(test_func)
            kwargs = {}
            body_proc.process(kwargs)
            assert kwargs["a"] == "string body"

    def test_body_processor_with_int_body(self):

        @Body("a")
        def test_func(a: int):
            pass

        with app.test_request_context(data="1"):
            body_proc = BodyProcessor(test_func)
            kwargs = {}
            body_proc.process(kwargs)
            assert kwargs["a"] == 1

    def test_body_processor_with_dict_type(self):

        @Body("a")
        def test_func(a: dict):
            pass

        with app.test_request_context(json={"value": 1}):
            body_proc = BodyProcessor(test_func)
            kwargs = {}
            body_proc.process(kwargs)
            assert kwargs["a"] == {"value": 1}

    def test_body_processor_with_body_decorator_multiple_definition(self):

        @Body("a")
        @Body("b")
        def test_func2(b: str):
            pass

        with app.test_request_context(data="string body"):
            body_proc = BodyProcessor(test_func2)
            kwargs = {}
            body_proc.process(kwargs)
            assert kwargs["b"] == "string body"
