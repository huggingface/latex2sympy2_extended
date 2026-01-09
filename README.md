![Logo](https://picgo-1258602555.cos.ap-nanjing.myqcloud.com/icon.png)

# [latex2sympy2_extended](https://github.com/hynky1999/latex2sympy2_extended)

## About

`latex2sympy2_extended` parses **LaTeX math expressions** and converts it into the equivalent **SymPy form**. The latex2sympy2_extended is adapted from [OrangeX4/latex2sympy](https://github.com/OrangeX4/latex2sympy).

[ANTLR](http://www.antlr.org/) 4.13.1 is used to generate the parser.
## Features


* **Arithmetic:** Add (+), Sub (-), Dot Mul (·), Cross Mul (×), Frac (/), Power (^), Abs (|x|), Sqrt (√), etc...
* **Alphabet:** a - z, A - Z, α - ω, Subscript (x_1), Accent Bar(ā), etc...
* **Common Functions:** gcd, lcm, floor, ceil, max, min, log, ln, exp, sin, cos, tan, csc, sec, cot, arcsin, sinh, arsinh, etc...
* **Function Symbol:** f(x), f(x-1,), g(x,y), etc...
* **Calculous:** Limit ($lim_{n\to\infty}$), Derivation ($\frac{d}{dx}(x^2+x)$), Integration ($\int xdx$), etc...
* **Linear Algebra:** Matrix, Determinant, Transpose, Inverse, Elementary Transformation, etc...
* **Set:** Union (∪), Intersection (∩), etc...
* **Other:** Binomial...

**NOTICE:** It will do some irreversible calculations when converting determinants, transposed matrixes and elementary transformations...

**NOTICE:** comma separated numbers are only supported in standalone form: `1,233`, not in expressions: `1,233x`.

## Installation
Current version supports 3 runtimes:
- 4.9.3
- 4.11.0
- 4.13.2


Use the following command to install with the runtime you need:
```
pip install latex2sympy2_extended[antlr4_13_2]
```

**Requirements:** `sympy` and `antlr4-python3-runtime` packages.

## Usage

### Basic

In Python:

```python
from latex2sympy2_extended import latex2sympy

tex = r"\frac{d}{dx}(x^{2}+x)"
latex2sympy(tex)
# => "Derivative(x**2 + x, x)"
```

### Examples

|LaTeX|Converted SymPy|Calculated Latex|
|-----|-----|---------------|
|`x^{3}` $x^{3}$| `x**3`|`x^{3}` $x^{3}$|
|`\frac{d}{dx} tx` $\frac{d}{dx}tx$|`Derivative(x*t, x)`|`t` $t$|
|`\sum_{i = 1}^{n} i` $\sum_{i = 1}^{n} i$|`Sum(i, (i, 1, n))`|`\frac{n \left(n + 1\right)}{2}` $\frac{n \left(n + 1\right)}{2}$|
|`\int_{a}^{b} \frac{dt}{t}`|`Integral(1/t, (t, a, b))`|`-\log{(a)} + \log{(b)}` $-\log{(a)} + \log{(b)}$|
|`(2x^3 - x + z)|_{x=3}` $(2x^3 - x + z)\|_{x=3}$|`z + 51`| `z + 51` $z + 51$ |


### Eval At

``` latex
# Before
(x+2)|_{x=y+1}

# After
y + 3
```

### Matrix

#### Determinant

``` python
from latex2sympy2 import latex2sympy

tex = r"\begin{vmatrix} x & 0 & 0 \\ 0 & x & 0 \\ 0 & 0 & x \end{vmatrix}"
latex2sympy(tex)
# => "x^{3}"
```

#### Transpose

``` python
from latex2sympy2 import latex2sympy

tex = r"\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}^T"
# Or you can use "\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix}'"
latex2sympy(tex)
# => "Matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]])"
```

#### Elementary Transformation

``` python
from latex2sympy2 import latex2sympy

matrix = r'''
    \begin{pmatrix}
        1 & 2 & 3 \\ 
        4 & 5 & 6 \\
        7 & 8 & 9 \\ 
    \end{pmatrix}
'''

# Scale the row with grammar "\xrightarrow{kr_n}"
tex = matrix + r'\xrightarrow{3r_1}'
latex2sympy(tex)
# => "Matrix([[3, 6, 9], [4, 5, 6], [7, 8, 9]])"

# Swap the cols with grammar "\xrightarrow{c_1<=>c_2}"
# Of course, you can use "\leftrightarrow" to replace "<=>" 
tex = matrix + r'\xrightarrow{c_1<=>c_2}'
latex2sympy(tex)
# => "Matrix([[2, 1, 3], [5, 4, 6], [8, 7, 9]])"

# Scale the second row and add it to the first row
# with grammar "\xrightarrow{r_1+kr_2}"
tex = matrix + r'\xrightarrow{r_1+kr_2}'
latex2sympy(tex)
# => "Matrix([[4*k + 1, 5*k + 2, 6*k + 3], [4, 5, 6], [7, 8, 9]])"

# You can compose the transform with comma ","
# and grammar "\xrightarrow[4r_3]{2r_1, 3r_2}"
# Remember the priority of "{}" is higher than "[]"
tex = matrix + r'\xrightarrow[4r_3]{2r_1, 3r_2}'
latex2sympy(tex)
# => "Matrix([[2, 4, 6], [12, 15, 18], [28, 32, 36]])"
```

### Complex Number Support

``` python
from latex2sympy2 import set_real

set_real(False)
```


## Contributing

If you want to add a new grammar, you can fork the code from [hynky1999/latex2sympy2_extended](https://github.com/hynky1999/latex2sympy2_extended).

* To modify parser grammar, view the existing structure in `src/latex2sympy2_extended/PS.g4`.
* To modify the action associated with each grammar, look into `src/latex2sympy2_extended/latex2sympy2.py`.

Contributors are welcome! Feel free to open a pull request or an issue.
