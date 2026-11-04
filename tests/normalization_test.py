from latex2sympy2_extended.math_normalization import NormalizationConfig, normalize_latex


def test_command_shorthand_is_one_argument():
    config = NormalizationConfig(
        basic_latex=True,
        units=True,
        malformed_operators=True,
        nits=True,
        boxed="all",
        equations=False,
    )

    assert normalize_latex(r"\frac\pi4", config) == r"\frac{\pi}{4}"
    assert normalize_latex(r"\frac \pi4", config) == r"\frac{\pi}{4}"
    assert normalize_latex(r"\frac\pi 4", config) == r"\frac{\pi}{4}"
    assert normalize_latex(r"\frac 1\pi", config) == r"\frac{1}{\pi}"
    assert normalize_latex(r"\frac\pi\pi", config) == r"\frac{\pi}{\pi}"
    assert normalize_latex(r"\sqrt\pi", config) == r"\sqrt{\pi}"
    assert normalize_latex(r"\sqrt \pi", config) == r"\sqrt{\pi}"
    assert normalize_latex(r"\frac12", config) == r"\frac{1}{2}"
    assert normalize_latex(r"\frac1{2}", config) == r"\frac{1}{2}"
    assert normalize_latex(r"\frac{3}{4}", config) == r"\frac{3}{4}"
    assert normalize_latex(r"\sqrt3", config) == r"\sqrt{3}"
    assert normalize_latex(r"\sqrt{3}", config) == r"\sqrt{3}"
    assert normalize_latex(r"\frac\pi4+\frac12", config) == r"\frac{\pi}{4}+\frac{1}{2}"


def test_units_normalization():
    config = NormalizationConfig(
        basic_latex=False,
        units=True,
        malformed_operators=False,
        nits=False,
        boxed="none",
        equations=False
    )

    # Test basic unit removal
    assert normalize_latex("865 \\mbox{ inches}^2", config) == "865"
    assert normalize_latex("\\mbox{hello}", config) == "\\mbox{hello}"
    assert normalize_latex("1cm", config) == "1"
    assert normalize_latex("\\frac{1}{2} cm", config) == "\\frac{1}{2}"
    assert normalize_latex("\\frac{1}{2}cm", config) == "\\frac{1}{2}"
    assert normalize_latex("1 < ms < 2", config) == "1 < ms < 2"
    assert normalize_latex("3s", config) == "3"

def test_boxed_normalization():
    config = NormalizationConfig(
        basic_latex=False,
        units=False,
        malformed_operators=False,
        nits=False,
        equations=False,
        boxed="all"
    )

    assert normalize_latex("\\boxed{\\left( 3, \\frac{\\pi}{2} \\right)}.", config) == "\\left( 3, \\frac{\\pi}{2} \\right)"
