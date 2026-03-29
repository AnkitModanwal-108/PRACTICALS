def is_complete_graph(matrix, n):
    """
    A graph is COMPLETE if every pair of distinct vertices is connected.
    In the adjacency matrix: all off-diagonal entries must be 1,
    and diagonal entries must be 0 (no self-loops).
    """
    for i in range(n):
        for j in range(n):
            if i == j:
                if matrix[i][j] != 0:   # self-loop found
                    return False
            else:
                if matrix[i][j] != 1:   # missing edge
                    return False
    return True

def display_matrix(matrix, n):
    print("\nAdjacency Matrix:")
    print("  " + " ".join(str(j) for j in range(n)))
    for i in range(n):
        print(f"{i} " + " ".join(map(str, matrix[i])))

def main():
    print("=== Complete Graph Checker ===")
    n = int(input("Enter number of vertices: "))

    print(f"Enter {n}×{n} adjacency matrix row by row (space-separated 0s and 1s):")
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Row {i}: ").split()))
        if len(row) != n:
            print(f"Error: expected {n} values in row {i}.")
            return
        matrix.append(row)

    display_matrix(matrix, n)

    if is_complete_graph(matrix, n):
        print(f"\nResult: The graph IS a Complete Graph (K{n}).")
        print(f"  Expected edges: {n*(n-1)//2}")
    else:
        # Count actual edges
        edge_count = sum(matrix[i][j] for i in range(n) for j in range(i+1, n))
        print(f"\nResult: The graph is NOT a Complete Graph.")
        print(f"  Actual edges  : {edge_count}")
        print(f"  Required edges: {n*(n-1)//2}")

if __name__ == "__main__":
    main()
