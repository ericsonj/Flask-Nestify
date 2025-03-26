from flask_nestify.core import WrapperFunc
from flask_nestify.exception import (
    BadRequestException,
    NotFoundException,
    UnauthorizedException,
    ForbiddenException,
    NotAcceptableException,
    RequestTimeoutException,
    ConflictException,
    GoneException,
    HttpVersionNotSupportedException,
    PayloadTooLargeException,
    UnsupportedMediaTypeException,
    UnprocessableEntityException,
    InternalServerErrorException,
    NotImplementedException,
    ImATeapotException,
    MethodNotAllowedException,
    BadGatewayException,
    ServiceUnavailableException,
    GatewayTimeoutException,
    PreconditionFailedException,
)
from . import app


class TestException:

    def test_response_request_with_not_found_exception(self):

        class Test:
            def test_func(self):
                raise NotFoundException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except NotFoundException as e:
                assert True
                e.status_code == 404
                e.message == "Not Found"

    def test_response_request_with_bad_request_exception(self):

        class Test:
            def test_func(self):
                raise BadRequestException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except BadRequestException as e:
                assert True
                e.status_code == 400
                e.message == "Bad Request"

    def test_response_request_with_unauthorized_exception(self):

        class Test:
            def test_func(self):
                raise UnauthorizedException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except UnauthorizedException as e:
                assert True
                e.status_code == 401
                e.message == "Unauthorized"

    def test_response_request_with_forbidden_exception(self):

        class Test:
            def test_func(self):
                raise ForbiddenException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except ForbiddenException as e:
                assert True
                e.status_code == 403
                e.message == "Forbidden"

    def test_response_request_with_not_acceptable_exception(self):

        class Test:
            def test_func(self):
                raise NotAcceptableException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except NotAcceptableException as e:
                assert True
                e.status_code == 406
                e.message == "Not Acceptable"

    def test_response_request_with_request_timeout_exception(self):

        class Test:
            def test_func(self):
                raise RequestTimeoutException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except RequestTimeoutException as e:
                assert True
                e.status_code == 408
                e.message == "Request Timeout"

    def test_response_request_with_conflict_exception(self):

        class Test:
            def test_func(self):
                raise ConflictException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except ConflictException as e:
                assert True
                e.status_code == 409
                e.message == "Conflict"

    def test_response_request_with_gone_exception(self):

        class Test:
            def test_func(self):
                raise GoneException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except GoneException as e:
                assert True
                e.status_code == 410
                e.message == "Gone"

    def test_response_request_with_http_version_not_supported_exception(self):

        class Test:
            def test_func(self):
                raise HttpVersionNotSupportedException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except HttpVersionNotSupportedException as e:
                assert True
                e.status_code == 505
                e.message == "HTTP version not supported"

    def test_response_request_with_payload_too_large_exception(self):

        class Test:
            def test_func(self):
                raise PayloadTooLargeException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except PayloadTooLargeException as e:
                assert True
                e.status_code == 413
                e.message == "Payload too large"

    def test_response_request_with_unsupported_media_type_exception(self):

        class Test:
            def test_func(self):
                raise UnsupportedMediaTypeException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except UnsupportedMediaTypeException as e:
                assert True
                e.status_code == 415
                e.message == "Unsupported media type"

    def test_response_request_with_unprocessable_entity_exception(self):

        class Test:
            def test_func(self):
                raise UnprocessableEntityException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except UnprocessableEntityException as e:
                assert True
                e.status_code == 422
                e.message == "Unprocessable Entity"

    def test_response_request_with_internal_server_error_exception(self):

        class Test:
            def test_func(self):
                raise InternalServerErrorException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except InternalServerErrorException as e:
                assert True
                e.status_code == 500
                e.message == "Internal Server Error"

    def test_response_request_with_not_implemented_exception(self):

        class Test:
            def test_func(self):
                raise NotImplementedException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except NotImplementedException as e:
                assert True
                e.status_code == 501
                e.message == "Not Implemented"

    def test_response_request_with_im_a_teapot_exception(self):

        class Test:
            def test_func(self):
                raise ImATeapotException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except ImATeapotException as e:
                assert True
                e.status_code == 418
                e.message == "I'm a teapot"

    def test_response_request_with_method_not_allowed_exception(self):

        class Test:
            def test_func(self):
                raise MethodNotAllowedException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except MethodNotAllowedException as e:
                assert True
                e.status_code == 405
                e.message == "Method Not Allowed"

    def test_response_request_with_bad_gateway_exception(self):

        class Test:
            def test_func(self):
                raise BadGatewayException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except BadGatewayException as e:
                assert True
                e.status_code == 502
                e.message == "Bad Gateway"

    def test_response_request_with_service_unavailable_exception(self):

        class Test:
            def test_func(self):
                raise ServiceUnavailableException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except ServiceUnavailableException as e:
                assert True
                e.status_code == 503
                e.message == "Service Unavailable"

    def test_response_request_with_gateway_timeout_exception(self):

        class Test:
            def test_func(self):
                raise GatewayTimeoutException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except GatewayTimeoutException as e:
                assert True
                e.status_code == 504
                e.message == "Gateway Timeout"

    def test_response_request_with_precondition_failed_exception(self):

        class Test:
            def test_func(self):
                raise PreconditionFailedException()

        with app.test_request_context():
            test = Test()
            wrapper_func = WrapperFunc(test, Test.test_func).wrapper_func()
            try:
                wrapper_func()
                assert False
            except PreconditionFailedException as e:
                assert True
                e.status_code == 412
                e.message == "Precondition Failed"
