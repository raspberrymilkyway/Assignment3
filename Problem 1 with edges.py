import math

def edge_irregular_labeling(n):
    k = (3*n + 1) // 2  # Calculate k value
    labels = {}  # Dictionary to store vertex labels
    weights = {} # Dictionary to store edge weights

    if n % 4 == 0 or n % 4 == 2 or n % 4 == 3:
        #centroid vertices
        for i in range(1, n + 1):
            if i <= math.floor(n/4) + 1:
                labels[i] = 3*i - 2
            else:
                labels[i] = 2*math.floor(n/4) + i

        #pendant vertices
        for i in range(1, n + 1):
            if i <= math.floor(n/4):
                for j in range(1, 3):
                    labels[(i, j)] = j + 1
            else:
                for j in range(1, 3):
                    labels[(i, j)] = n + i + j - 1 - 2*math.floor(n/4)

        #edge weights
        for i in range(1, n+1):
            #center-most vertex is at index 0 and has a label of 1
            weights[(0, i)] = 1 + labels[i]

            for j in range(1, 3):
                weights[(i, (i, j))] = labels[i] + labels[(i, j)]


        return (labels, weights)
    else:
        return "Invalid n value for the given conditions"

# Example usage
n_value = 8  # Adjust n value here
labels, weights = edge_irregular_labeling(n_value)
if isinstance(labels, dict):
    print("Vertex labels for S_{},3:".format(n_value))
    print("\tCentroid vertex labels:")
    for vertex, label in labels.items():
        if isinstance(vertex, int):
            print("\t\tCentroid {}: Label {}".format(vertex, label))
    print("\n\tPendant vertex labels:")
    for pendant, label in labels.items():
        if isinstance(pendant, tuple):
            print("\t\tPendant {}: Label {}".format(pendant, label))
else:
    print(labels)

if isinstance(weights, dict):
    print("\nEdge labels for S_{},3:".format(n_value))
    print("\tCentroid edge labels:")
    for vertex, label in weights.items():
        vertex1, vertex2 = vertex
        if isinstance(vertex2, int):
            print("\t\tEdge {}: Weight {}".format(vertex, label))
    print("\n\tPendant edge labels:")
    for pendant, label in weights.items():
        vertex1, vertex2 = pendant
        if isinstance(vertex2, tuple):
            print("\t\tEdge {}: Weight {}".format(pendant, label))
else:
    print(weights)