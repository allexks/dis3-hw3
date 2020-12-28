"""62136."""

from math import factorial as fac

def F(x, iterations=5):
    """
    Taylor series expansion of integral of e^(-x/2).
    https://en.wikipedia.org/wiki/Error_function#Taylor_series
    """
    return sum(
        ((-1)**n) * x**(2*n+1) / (fac(n) * (2*n+1))
        for n in range(iterations)
    )

if __name__ == "__main__":
    upper = F(1/4)
    lower = F(0)
    result = upper - lower
    print(f"The definite integral of e^(-x/2) from 0 to 1/4 is rounded to {result:.4f}.")


