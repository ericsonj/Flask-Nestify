from flask_nestify.decorator import Pipe
from flask_nestify.pipe import ParseInt, PipeProcessor


class TestPipeProcessor:

    def test_pipe_parse_int_from_str(self):

        @Pipe(name="a", pipe_cls=ParseInt)
        def test_func(a: int):
            pass

        query_proc = PipeProcessor(test_func)
        kwargs = {"a": "1"}
        query_proc.process(kwargs)
        assert kwargs["a"] == 1

    def test_pipe_parse_int_from_int(self):

        @Pipe(name="a", pipe_cls=ParseInt)
        def test_func(a: int):
            pass

        query_proc = PipeProcessor(test_func)
        kwargs = {"a": 1}
        query_proc.process(kwargs)
        assert kwargs["a"] == 1

    def test_pipe_parse_int_from_str_error(self):

        @Pipe("a", ParseInt)
        def test_func(a: int):
            pass

        query_proc = PipeProcessor(test_func)
        kwargs = {"a": 1.1}
        try:
            query_proc.process(kwargs)
            assert False
        except Exception as e:
            assert True
