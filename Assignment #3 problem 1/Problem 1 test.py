def edge_irregular_labeling(n):
    k = (3*n + 1) // 2  # Calculate k value
    labels = {}  # Dictionary to store vertex labels

    # Assign labels to vertices
    for i in range(1, 3*n + 2):
        vertex_label = min(i, 2*n + 1 - i)
        labels[i] = vertex_label

    # Assign labels to edges
    edge_labels = {}
    for i in range(1, 3*n + 1):
        for j in range(i + 1, 3*n + 2):
            edge_labels[(i, j)] = (labels[i] + labels[j]) % k

    return edge_labels

# Example usage
n_value = 8
edge_labels = edge_irregular_labeling(n_value)
print("Edge labels for S_{},3:".format(n_value))
for edge, label in edge_labels.items():
    print("Edge {}: Label {}".format(edge, label))
