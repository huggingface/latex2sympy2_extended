from sympy import And as SympyAnd
from sympy.core.sympify import sympify


def _restore_relation(func, args):
    try:
        return func(*args, evaluate=False)
    except TypeError:
        return func(*args)


def _restore_and(specs):
    return And(*(_restore_relation(func, args) for func, args in specs), evaluate=False)


class And(SympyAnd):
    """
    Patched version of And that keeps the _unsorted_args attribute
    """

    def __new__(cls, *args, **kwargs):
        args = [sympify(arg) for arg in args]
        obj = super().__new__(cls, *args, **kwargs)
        # SymPy drops a true comparison such as 0 < 1 and returns the other
        # relation. That value has no _unsorted_args.
        if isinstance(obj, cls):
            obj._unsorted_args = args
        return obj

    def __reduce_ex__(self, protocol):
        # Relational.__new__ evaluates 0 < 1 to True unless evaluate=False.
        # The default pickle path calls it without that flag.
        specs = tuple((arg.func, tuple(arg.args)) for arg in self._unsorted_args)
        return (_restore_and, (specs,))
