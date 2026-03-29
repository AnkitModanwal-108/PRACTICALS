from itertools import permutations, product

def permutations_without_repetition(digits, r=None):
    """All permutations of `digits` choosing r at a time (no repetition)."""
    if r is None:
        r = len(digits)
    result = list(permutations(digits, r))
    return result

def permutations_with_repetition(digits, r):
    """All permutations of `digits` of length r WITH repetition."""
    result = list(product(digits, repeat=r))
    return result

def main():
    raw = input("Enter the set of digits (space-separated): ").split()
    try:
        digits = [int(x) for x in raw]
    except ValueError:
        digits = raw

    print("\n1. Permutations WITHOUT repetition")
    print("2. Permutations WITH repetition")
    choice = input("Choose (1/2): ").strip()

    if choice == '1':
        r = input(f"Choose r (length of permutation, max {len(digits)}) [press Enter for full]: ").strip()
        r = int(r) if r else len(digits)
        perms = permutations_without_repetition(digits, r)
        print(f"\nP({len(digits)},{r}) = {len(perms)} permutations:")
        for p in perms:
            print(list(p))

    elif choice == '2':
        r = int(input("Choose r (length of permutation): "))
        perms = permutations_with_repetition(digits, r)
        print(f"\n{len(digits)}^{r} = {len(perms)} permutations:")
        for p in perms:
            print(list(p))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
