from checkio_referee import RefereeRank
from checkio_referee import representations


import settings_env
from tests import TESTS

cover = """def cover(func, data):
    result = func(tuple(data))
    if not isinstance(result, (list, tuple)):
        raise TypeError("The result should be a list or a tuple")
    return result
"""


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "absolute_sorting"
    FUNCTION_NAMES = {
        "javascript": "absoluteSorting"
    }
    CALLED_REPRESENTATIONS = {
        "python_3": representations.py_tuple_representation
    }
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": None
    }
