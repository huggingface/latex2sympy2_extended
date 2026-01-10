# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.11.0]

### Added
- Support for gamma function / constant parsing (`\Gamma` and `\gamma`)
- Improvements to percentage parsing (better handling of spaces and deduplication)

### Fixed
- Typo fixes in documentation

## [1.10.2]
- Improve boxed handling

## [1.10.1]
- Ensure that 0,xxx is parsed as a float
- Remove TimeoutException handling

## [1.0.9]
- Created proxy And class that keeps the _unsorted_args attribute
- Add unary \\pm support
- Fixed antlr4 runtime incorrect placement
- Minor fix to how and are processed in normalization
- Deprecated `equations` parameter in `NormalizationConfig`, as it is now handled by the parser

## [1.0.8]
- Fixed bug with imports of antlr4 runtime

## [1.0.7]
- Added support for multiple antlr4 runtimes:
    - `antlr4-python3-runtime==4.13.2`
    - `antlr4-python3-runtime==4.11.0`
    - `antlr4-python3-runtime==4.9.3`

## [1.0.6]
- Improved boxed normalization

## [1.0.5]
- Fixed bugged with boxed normalization

## [1.0.4]
- Remove empty excepts, so that KeyboardInterrupt is not caught


## [1.0.3]

- Reverted back the code for identification of assignment relations to use `is_assignment_symbol` instead of `is_expr_of_only_symbols`.
- Changed `FiniteSet` to be translated to `latex2sympy2_extended.sets.FiniteSet`. This is to keep an order of elements in the set.

## [1.0.2]

### Changed
- Changed `is_assignment_symbol` to disallow x+y to be an assignment symbol

## [1.0.1]

### Changed
- Changed `boxed` parameter in `NormalizationConfig` to be a string parameter with values "all", "none", or "only". "all" means that all boxed elements will be extracted, "none" means that no boxed elements will be extracted, and "only" means that only boxed elements will be extracted.

## [1.0.0]

### Added
- Support for `E` notation and `E` symbol in expressions
- Support for number subscripts in expressions
- Support for chained inequalities (e.g. `a < b < c`)
- Support for multiple boxed elements in normalization
- Support for "and"/"or" text conversion to semicolons in set notation
- Helper function `convert_elements_to_set_or_tuple()` to handle set/tuple conversion
- Added `is_expr_of_only_symbols` to public API
- Added docstring for `interpret_contains_as_eq` in ConversionConfig

### Changed
- Made `ConversionConfig` frozen dataclass
- Changed default behavior of `interpret_simple_eq_as_assignment` to `False`
- Updated set membership handling to use `Eq()` instead of direct assignment
- Made `NormalizationConfig` fields have default values
- Improved handling of boxed content in normalization
- Refactored set element parsing to be more consistent
- Updated handling of matrix operations with tuples
- Simplified grammar rules for `semicolon_elements` and `comma_elements` to be more linear

### Fixed
- Fixed handling of empty text in normalization
- Fixed handling of matrix transpose operations
- Added proper exception handling for timeouts
- Fixed handling of "and"/"or" text in set notation
- Fixed handling of E notation and E symbol
- Fixed handling of number subscripts

### Tests
- Added tests for boxed normalization
- Added tests for set operations with and/or
- Added tests for E notation and symbols
- Added more comprehensive set relation tests
- Disabled some linalg placeholder tests temporarily 