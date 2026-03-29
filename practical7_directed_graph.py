def compute_degrees(matrix, n):
    """
    For a DIRECTED graph represented as an adjacency matrix:
      - Out-degree of vertex i = sum of row i   (edges going OUT from i)
      - In-degree  of vertex i = sum of column i (edges coming IN  to i)
    """
    in_degree  = [0] * n
    out_degree = [0] * n

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                out_degree[i] += 1   # edge i -> j
                in_degree[j]  += 1   # edge i -> j reaches j

    return in_degree, out_degree

def display_matrix(matrix, n):
    print("\nAdjacency Matrix (Directed Graph):")
    print("     " + "  ".join(f"v{j}" for j in range(n)))
    for i in range(n):
        print(f"v{i}  " + "   ".join(map(str, matrix[i])))

def main():
    print("=== In-degree & Out-degree of Directed Graph ===")
    n = int(input("Enter number of vertices: "))

    print(f"Enter {n}×{n} adjacency matrix row by row.")
    print("(matrix[i][j]=1 means directed edge from vertex i to vertex j)")
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Row v{i}: ").split()))
        if len(row) != n:
            print(f"Error: expected {n} values.")
            return
        matrix.append(row)

    display_matrix(matrix, n)

    in_deg, out_deg = compute_degrees(matrix, n)

    print("\n" + "-"*35)
    print(f"{'Vertex':<10} {'In-degree':<15} {'Out-degree'}")
    print("-"*35)
    for i in range(n):
        print(f"v{i:<9} {in_deg[i]:<15} {out_deg[i]}")
    print("-"*35)
    print(f"{'Total':<10} {sum(in_deg):<15} {sum(out_deg)}")
    print("\nNote: Total in-degree == Total out-degree == Total number of edges")

if __name__ == "__main__":
    main()
