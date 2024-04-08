def m_ary_labeling(m, h):
    # Step 1
    V = (m**(h+1) - 1) // (m - 1)
    labels = {}

    # Step 2
    labels[1] = 1

    # Step 3
    TArray = [[0] * (m * (m**(h - 1)) + 1) for _ in range(2)]
    TArray[0][1] = 1
    TArray[1][1] = 2

    # Step 4
    d = V // (2 * (m - 1))

    # Step 5-9
    for j in range(2, m + 1):
        TArray[0][j] = TArray[0][j-1] + d
        TArray[1][j] = TArray[0][j] + 1

    # Step 10-14
    def recursive_call(parent, level, start_weight, decrease):
        nonlocal V
        if level > h:
            return
        weight = start_weight
        for i in range(1, m + 1):  # Iterate over all children
            child_index = parent * m + i
            if child_index < len(TArray[0]):  # Check if child index is within TArray range
                # Step 11 or 15
                if decrease:
                    weight -= 1
                else:
                    weight += 1

                if weight <= V and weight >= 3:  # Avoid edge weights out of range
                    TArray[0][child_index] = parent
                    TArray[1][child_index] = weight
                    labels[child_index] = weight
                    recursive_call(child_index, level + 1, weight, decrease)

    recursive_call(1, 2, V, False)  # First call for increasing weights
    recursive_call(1, 2, V, True)   # Second call for decreasing weights

    return labels

# Example usage
m_value = 3
h_value = 3
labels = m_ary_labeling(m_value, h_value)
print("Vertex labels:")
for vertex, label in labels.items():
    print("Vertex {}: Label {}".format(vertex, label))

