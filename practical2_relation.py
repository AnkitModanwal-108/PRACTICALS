class RELATION:
    def __init__(self, n, matrix):
        """
        n      : number of elements in the set
        matrix : n×n list of lists (0/1)
        """
        self.n = n
        self.M = matrix

    def display(self):
        print("Relation Matrix:")
        print("  " + " ".join(str(j+1) for j in range(self.n)))
        for i in range(self.n):
            print(f"{i+1} " + " ".join(map(str, self.M[i])))

    # Reflexive: M[i][i] == 1 for all i
    def is_reflexive(self):
        return all(self.M[i][i] == 1 for i in range(self.n))

    # Symmetric: M[i][j] == M[j][i] for all i, j
    def is_symmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.M[i][j] != self.M[j][i]:
                    return False
        return True

    # Anti-symmetric: if M[i][j]==1 and M[j][i]==1 then i==j
    def is_antisymmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.M[i][j] == 1 and self.M[j][i] == 1:
                    return False
        return True

    # Transitive: if M[i][j]==1 and M[j][k]==1 then M[i][k]==1
    def is_transitive(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.M[i][j] == 1:
                    for k in range(self.n):
                        if self.M[j][k] == 1 and self.M[i][k] == 0:
                            return False
        return True

    def classify(self):
        R  = self.is_reflexive()
        S  = self.is_symmetric()
        AS = self.is_antisymmetric()
        T  = self.is_transitive()

        print(f"\nReflexive    : {R}")
        print(f"Symmetric    : {S}")
        print(f"Antisymmetric: {AS}")
        print(f"Transitive   : {T}")

        if R and S and T:
            print("\n=> EQUIVALENCE RELATION")
        elif R and AS and T:
            print("\n=> PARTIAL ORDER RELATION")
        else:
            print("\n=> NONE (neither Equivalence nor Partial Order)")


def main():
    n = int(input("Enter number of elements in the set: "))
    print(f"Enter {n}×{n} relation matrix row by row (space-separated 0s and 1s):")
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    rel = RELATION(n, matrix)
    rel.display()
    rel.classify()


if __name__ == "__main__":
    main()
