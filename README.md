# Introduction

As a Data Scientist you are working on a supervised regression model and you have faced the issue of an imbalanced training set. 
You want to utilize the knowledge of the expected distribution of the output values.

# Problem statement

Implement the `process` function in the `Sampler` class. The method accepts two parameters: input sequence `x` and the expected output distribution `distr`. The input sequence is a list of float values. The distribution is the expected normalized histogram of the output sequence.

Your task is to create the output sequence `y` that fulfills the following conditions:

1. `y` contains elements from `x`.
1. `y` may contain duplicates, but only if necessary.
1. `y` does not need to contain all elements from `x`.
1. A normalized histogram calculated on `y` and equal-width bins is equal to `distr` with tolerance `atol = rtol = 1 / len(x)`,
defined as in `numpy.allclose`.
1. The size of `y` is close to the size of `x`, meaning `abs(len(x) - len(y)) <= len(distr)`.

Additionally, the function needs to do the following:

1. Prior to generating `y`, remove any outliers from `x`, that is elements distanced more than two standard deviations from the mean.
1. Randomly shuffle the output sequence.

Hint: you can use `numpy.digitize`.

# Example

```python
x = [5, 4, 100, 6, 3, 2, 10, 1, -80, 12, 14, 9]
distr = [0.3, 0.5, 0.2]

output = [9, 6, 9, 6, 4, 5, 12, 6, 10, 3]
```

## Environment setup for git/zip modes

To execute all unit tests, use:

    pip install -q -e . && python3 setup.py pytest
