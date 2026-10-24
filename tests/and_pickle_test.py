import pickle

import pytest
from latex2sympy2_extended import latex2sympy
from sympy.core.relational import Relational


@pytest.mark.parametrize(
    "latex",
    [
        r"0 < 1 < x",
        r"1 = 1 = x",
        r"x > 3 > 1",
        r"1 < x < 3",
    ],
)
def test_chained_relation_survives_pickle(latex):
    parsed = latex2sympy(latex)
    restored = pickle.loads(pickle.dumps(parsed))

    assert isinstance(restored, type(parsed))
    assert [type(arg) for arg in restored._unsorted_args] == [
        type(arg) for arg in parsed._unsorted_args
    ]
    assert all(isinstance(arg, Relational) for arg in restored._unsorted_args)
    assert restored._unsorted_args == parsed._unsorted_args
