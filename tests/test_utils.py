from flask_nestify.utils import dict_2_obj, get_class_key


class TestClass:
    pass


class TestUtils:

    def test_get_class_key_in_file(self):
        key = get_class_key(TestClass)
        assert key == "tests.test_utils.TestClass"

    def test_get_class_key_defined_in_function(self):
        class TestClass:
            pass

        key = get_class_key(TestClass)
        assert (
            key
            == "tests.test_utils.TestUtils.test_get_class_key_defined_in_function.<locals>.TestClass"
        )
        assert key != "tests.test_utils.TestClass"

    def test_dict_2_obj(self):
        class TestClass:
            def __init__(self, a: int, b: str, c: float, d: bool, e: list, f: dict):
                self.a = a
                self.b = b
                self.c = c
                self.d = d
                self.e = e
                self.f = f

        obj_dict = {
            "a": 1,
            "b": "value",
            "c": 3.0,
            "d": True,
            "e": [1, 2, 3],
            "f": {"a": 1, "b": 2},
        }
        obj = dict_2_obj(obj_dict, TestClass)
        assert obj.a == 1
        assert obj.b == "value"
        assert obj.c == 3.0
        assert obj.d is True
        assert obj.e == [1, 2, 3]
        assert obj.f == {"a": 1, "b": 2}

    def test_dict_2_obj_with_nested_object(self):
        class NestedClass:
            def __init__(self, a: int):
                self.a = a

        class TestClass:
            def __init__(self, a: int, b: NestedClass):
                self.a = a
                self.b = b

        obj_dict = {"a": 1, "b": {"a": 2}}
        try:
            dict_2_obj(obj_dict, TestClass)
            assert False
        except Exception as e:
            assert True
            assert str(e) == "Unimplemented type yet"
