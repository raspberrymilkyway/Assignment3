import math

def edge_irregular_labeling(n):
    k = (3*n + 1) // 2  # Calculate k value
    labels = {}  # Dictionary to store vertex labels

    if n % 4 == 0 or n % 4 == 2 or n % 4 == 3:
        for i in range(1, n + 1):
            if i <= math.floor(n/4) + 1:
                labels[i] = 3*i - 2
            else:
                labels[i] = 2*math.floor(n/4) + i

        for i in range(1, n + 1):
            if i <= math.floor(n/4):
                for j in range(1, 3):
                    labels[(i, j)] = j + 1
            else:
                for j in range(1, 3):
                    labels[(i, j)] = n + i + j - 1 - 2*math.floor(n/4)

        return labels
    else:
        return "Invalid n value for the given conditions"

# Example usage
n_value = 8  # Adjust n value here
labels = edge_irregular_labeling(n_value)
if isinstance(labels, dict):
    print("Vertex and Edge labels for S_{},3:".format(n_value))
    print("Vertex labels:")
    for vertex, label in labels.items():
        if isinstance(vertex, int):
            print("Vertex {}: Label {}".format(vertex, label))
    print("\nEdge labels:")
    for edge, label in labels.items():
        if isinstance(edge, tuple):
            print("Edge {}: Label {}".format(edge, label))
else:
    print(labels)

