from pytest import fixture, mark


@mark.usefixtures("setup_and_teardown")
class BaseDriver:
    pass
