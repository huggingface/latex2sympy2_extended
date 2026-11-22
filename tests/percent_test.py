from sympy import Integer, Mul, Rational, UnevaluatedExpr

from latex2sympy2_extended.antlr_parser import PSParser
from tests.context import assert_equal


def test_percent_with_parser_generated_before_func_gamma(monkeypatch):
    # The 1.11.0 wheel ships antlr 4.9.3 and 4.11 parsers generated before FUNC_GAMMA joined `atom`.
    monkeypatch.delattr(PSParser.AtomContext, "FUNC_GAMMA", raising=False)
    assert_equal("20\\%", Mul(Integer(20), UnevaluatedExpr(Rational(1, 100)), evaluate=False))
