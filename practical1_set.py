class SET:
    def __init__(self, elements=None):
        self.elements = list(set(elements)) if elements else []

    def display(self):
        return "{" + ", ".join(map(str, self.elements)) + "}" if self.elements else "{}"

    # a. Check if element is a member
    def is_member(self, x):
        return x in self.elements

    # b. Power set
    def powerset(self):
        result = [[]]
        for elem in self.elements:
            result += [subset + [elem] for subset in result]
        return [SET(s) for s in result]

    # c. Subset check
    def subset(self, other):
        return all(e in other.elements for e in self.elements)

    # d. Union and Intersection
    def union(self, other):
        return SET(self.elements + [e for e in other.elements if e not in self.elements])

    def intersection(self, other):
        return SET([e for e in self.elements if e in other.elements])

    # e. Complement (universal set provided by user)
    def complement(self, universal):
        return SET([e for e in universal.elements if e not in self.elements])

    # f. Set difference and Symmetric difference
    def difference(self, other):
        return SET([e for e in self.elements if e not in other.elements])

    def symmetric_difference(self, other):
        return SET([e for e in self.elements if e not in other.elements] +
                   [e for e in other.elements if e not in self.elements])

    # g. Cartesian Product
    def cartesian_product(self, other):
        return [(a, b) for a in self.elements for b in other.elements]


# ── Menu-driven program ──────────────────────────────────────────────────────
def input_set(prompt):
    raw = input(prompt + " (space-separated): ").split()
    try:
        return SET([int(x) for x in raw])
    except ValueError:
        return SET(raw)

def main():
    print("=== SET Operations ===")
    A = input_set("Enter elements of Set A")
    B = input_set("Enter elements of Set B")
    U = input_set("Enter elements of Universal Set U")

    while True:
        print("""
--- Menu ---
1. is_member
2. powerset of A
3. subset (A ⊆ B?)
4. union (A ∪ B)
5. intersection (A ∩ B)
6. complement of A
7. set difference (A - B)
8. symmetric difference (A Δ B)
9. cartesian product (A × B)
0. Exit""")
        choice = input("Choice: ").strip()

        if choice == '1':
            x = input("Element to check: ")
            try: x = int(x)
            except ValueError: pass
            print(f"{x} ∈ A? {A.is_member(x)}")

        elif choice == '2':
            ps = A.powerset()
            print(f"Power set of A ({len(ps)} elements):")
            for s in ps:
                print(" ", s.display())

        elif choice == '3':
            print(f"A ⊆ B? {A.subset(B)}")

        elif choice == '4':
            print(f"A ∪ B = {A.union(B).display()}")

        elif choice == '5':
            print(f"A ∩ B = {A.intersection(B).display()}")

        elif choice == '6':
            print(f"A' = {A.complement(U).display()}")

        elif choice == '7':
            print(f"A - B = {A.difference(B).display()}")

        elif choice == '8':
            print(f"A Δ B = {A.symmetric_difference(B).display()}")

        elif choice == '9':
            cp = A.cartesian_product(B)
            print(f"A × B = {{ {', '.join(map(str, cp))} }}")

        elif choice == '0':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
