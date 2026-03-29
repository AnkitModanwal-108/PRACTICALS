def evaluate_polynomial(coefficients, n):
    """
    Evaluate polynomial stored as an array of coefficients.
    coefficients[i] corresponds to the coefficient of n^i.
    Example: f(n) = 4n^2 + 2n + 9  -> coefficients = [9, 2, 4]
    """
    result = 0
    for power, coeff in enumerate(coefficients):
        result += coeff * (n ** power)
    return result

def poly_to_string(coefficients):
    """Convert coefficient array to human-readable polynomial string."""
    terms = []
    degree = len(coefficients) - 1
    for power in range(degree, -1, -1):
        coeff = coefficients[power]
        if coeff == 0:
            continue
        if power == 0:
            terms.append(str(coeff))
        elif power == 1:
            terms.append(f"{coeff}n")
        else:
            terms.append(f"{coeff}n^{power}")
    return " + ".join(terms) if terms else "0"

def main():
    print("=== Polynomial Evaluator ===")
    print("Enter coefficients from LOWEST to HIGHEST degree.")
    print("Example: for 4n^2 + 2n + 9, enter: 9 2 4\n")

    raw = input("Enter coefficients (space-separated): ").split()
    coefficients = [int(x) for x in raw]

    poly_str = poly_to_string(coefficients)
    print(f"\nPolynomial: f(n) = {poly_str}")

    n = int(input("Enter value of n: "))
    result = evaluate_polynomial(coefficients, n)
    print(f"f({n}) = {result}")

if __name__ == "__main__":
    main()
