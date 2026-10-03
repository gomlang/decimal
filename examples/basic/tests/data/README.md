# Independent reference vectors

The decoded `reference.jsonl` fixture contains 3,072 deterministic cases, one JSON object per line with `input` and `expected` fields. Source: CPython 3.12 `decimal.Context` at precisions 1–50, all seven rounding modes, exact input decimal strings, and both Rounded/Inexact status flags. Seed: 20260921. Errors are independently obtained by catching DecimalException.

These values were exported once from the independent reference implementation used by `ecosystem/decimal/interop.py` at repository revision `27f8b1649561504bbe61d5247500e7cadc6eef42`, before removing that helper. No expected arithmetic or rendering result was captured from the GoML implementation under test. The reference source remains available in that historical revision for provenance; running these tests needs neither Python nor NumPy nor a downloaded reference runtime.

SHA-256 of this vector file: `4f3f317b2ed3805573ca3b3824e22d6d94e9e2e73237456e1b584fee59fd6878`.

Run `goml test --example basic` from the library root after resolving its development dependencies. `tests/reference_test.goml` evaluates each case directly through the GoML example API and asserts both the case count and results. New behavior should receive independently calculated expected values or a small native reference model; do not regenerate expectations from the implementation being tested.

## Integral quotient and remainder vectors

`div_rem.tsv` contains 192 fixed exact-integer reference cases generated using
CPython integer arithmetic, seed 20261004. Columns are dividend, divisor,
normalized truncating quotient, and normalized remainder. Generation aligns
integer coefficients to the larger scale, calculates `abs(a) // abs(b)`, restores
the quotient sign, and subtracts `q*b` from `a`. No floating point or GoML output
is used. Inputs include both signs, zero, up to 79 coefficient digits and scales
from -50 through 50. `div_rem_test.goml` checks both value and representation
through the installed consumer dependency. Python is not required to run tests.

SHA-256: `af06fb0f7cd388d40117053eabeb296aa7fa0c07a300e194a805fb7b87143493`.
