from flask_nestify.core import binding
from flask_nestify.decorator import Controller, Injectable
from flask_nestify.globals import controllers


class TestCore:

    def test_binding_simple_dependency(self):

        @Injectable
        class TestClass:
            def __init__(self):
                self.test = "test"

        object = binding(TestClass)
        assert object is not None
        assert isinstance(object, TestClass)
        assert object.test == "test"

    def test_binding_compose_dependency(self):

        @Injectable
        class TestClass:
            def __init__(self):
                self.test = "test"

        @Injectable
        class TestClass2:
            def __init__(self, test: TestClass):
                self.test = test

        object = binding(TestClass2)
        assert object is not None
        assert isinstance(object, TestClass2)
        assert object.test is not None
        assert isinstance(object.test, TestClass)
        assert object.test.test == "test"

    def test_binding_unknown_dependency(self):

        class TestClass:
            def __init__(self):
                self.test = "test"

        @Injectable
        class TestClass2:
            def __init__(self, test: TestClass):
                self.test = test

        object = binding(TestClass2)
        assert object is None

    def test_binding_with_default_value(self):

        @Injectable
        class TestClass:
            def __init__(self, test="value"):
                self.test = test

        object = binding(TestClass)
        assert object is not None
        assert isinstance(object, TestClass)
        assert object.test == "value"

    def test_binding_with_default_value_and_dependency(self):

        @Injectable
        class TestClass:
            def __init__(self):
                self.test = "test"

        @Injectable
        class TestClass2:
            def __init__(self, test: TestClass, value="value"):
                self.test = test
                self.value = value

        object = binding(TestClass2)
        assert object is not None
        assert isinstance(object, TestClass2)
        assert object.test is not None
        assert isinstance(object.test, TestClass)
        assert object.test.test == "test"
        assert object.value == "value"

    def test_binding_with_default_dependency_class(self):

        @Injectable
        class TestClass:
            def __init__(self, test="value"):
                self.test = test

        @Injectable
        class TestClass2:
            def __init__(self, test1: TestClass, test2=TestClass("custom")):
                self.test1 = test1
                self.test2 = test2

        object = binding(TestClass2)
        assert object is not None
        assert isinstance(object, TestClass2)
        assert object.test1 is not None
        assert isinstance(object.test1, TestClass)
        assert object.test1.test == "value"
        assert object.test2 is not None
        assert isinstance(object.test2, TestClass)
        assert object.test2.test == "custom"

    def test_controller_decorator(self):

        @Controller("unit-test", {"version": "v2/api"})
        class ControllerTest:
            pass

        controller = controllers[-1]
        assert controller is not None
        assert controller["name"] == "unit-test"
        assert controller["version"] == "v2/api"
        assert controller["class"] is not None

    def test_controller_decorator_without_name(self):

        @Controller({"version": "v2/api"})
        class ControllerTest:
            pass

        controller = controllers[-1]
        assert controller is not None
        assert controller["name"] == "controllertest"
        assert controller["version"] == "v2/api"
        assert controller["class"] is not None

    def test_controller_decorator_without_version(self):

        @Controller("unit-test")
        class ControllerTest:
            pass

        controller = controllers[-1]
        assert controller is not None
        assert controller["name"] == "unit-test"
        assert controller["version"] is None
        assert controller["class"] is not None

    def test_controller_decorator_without_name_and_version(self):

        @Controller()
        class ControllerTest:
            pass

        controller = controllers[-1]
        assert controller is not None
        assert controller["name"] == "controllertest"
        assert controller["version"] is None
        assert controller["class"] is not None

    def test_controller_decorator_using_kwargs(self):

        @Controller(path="unit-test", version="v2/api")
        class ControllerTest:
            pass

        controller = controllers[-1]
        assert controller is not None
        assert controller["name"] == "unit-test"
        assert controller["version"] == "v2/api"
        assert controller["class"] is not None

    def test_controller_decorator_bad_arguments(self):

        @Controller("unit-test", "v2/api")
        class ControllerTest:
            pass

        controller = controllers[-1]
        assert controller is not None
        assert controller["name"] == "controllertest"
        assert controller["version"] is None
        assert controller["class"] is not None
