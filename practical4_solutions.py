from itertools import product

def find_solutions(n, C):
    """
    Find all non-negative integer solutions to x1 + x2 + ... + xn = C
    using brute force strategy.
    """
    solutions = []
    # Each xi can range from 0 to C
    for combo in product(range(C + 1), repeat=n):
        if sum(combo) == C:
            solutions.append(combo)
    return solutions

def main():
    n = int(input("Enter the number of variables (n): "))
    C = int(input("Enter the constant C (C <= 10): "))

    if C > 10:
        print("C must be <= 10 as per the problem constraint.")
        return

    solutions = find_solutions(n, C)

    var_names = [f"x{i+1}" for i in range(n)]
    equation   = " + ".join(var_names) + f" = {C}"
    print(f"\nAll non-negative integer solutions of {equation}:")
    print(f"({'  ,  '.join(var_names)})")
    print("-" * 40)
    for sol in solutions:
        print(sol)
    print(f"\nTotal solutions: {len(solutions)}")

if __name__ == "__main__":
    main()
