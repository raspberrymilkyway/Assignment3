import networkx as nx
import matplotlib.pyplot as plt
import math


'''
    returns [a,b,c]
    were a is connect to center
    a and b are connected
    a and c are connected

    this is one of the nth sub tree star
'''
def generate_star(i , n):
    star = []
    if n % 4 == 1:
        if 1 <= i <= math.ceil(n/4):
            star.append(3*i - 2)
        elif math.ceil(n/4) + 1 <= i <= n:
            star.append(2*(math.ceil(n/4)) + i - 1)
        else:
            print('for center of star case not satisfy - 1')
        
        for i in range(1,3):
            if 1 <= i <= math.ceil(n/4) - 1:
                star.append(j+2)
            elif i == math.ceil(n/4) and j == 1:
                star.append(2)
            elif i == math.ceil(n/4) and j == 2:
                star.append(n - (math.ceil(n/4)) + 3)
            elif math.ceil(n/4) + 1 <= i <= n:
                star.append(n+i+j-2*(math.ceil(n/4)))
            else:
                print('invalid pendent parameters')
    else:
        if 1 <= i <= math.ceil(n/4) + 1:
            star.append(3*i - 2)
        elif math.ceil(n/4) + 2 <= i <= n:
            star.append(2*(math.ceil(n/4)) + i)
        else:
            print('for center of star case not satisfy - 2')
        
        for j in range(1,3):
            if 1 <= i <= math.ceil(n/4):
                star.append(j+1)
            elif math.ceil(n/4) + 1 <= i <= n:
                star.append(n+i+j-1-2*(math.ceil(n/4)))
            else:
                print('invalid pendent label')

    return star


'''
generate whole graph

lables = [1, [a,b,c] . [d,e,f] .....]
where 1 is the center and after that every first element in the triplets is connected to center 

d <---- 1 ----> a like this
and
b <----- a ----> c like this in sub tree as explained above

'''
def generate_graph(n):
    lables = [1]
    if n < 3:
        print('invalid args n = ',n)
        return lables

    for i in range(1,n+1):
        lables.append(generate_star(i,n))
    
    return lables


'''
returns wts array : [[x,y,z] , [p,q,r] ...] ,
returns repeated flag : to check weather there is some repeated wts or not

here, 

x - edge wt of center to center of star
y - edge wt of local center of start to pendent
z - another edge wt of local center of start to pendent

'''
def calculate_wts(arr):
    wt = []
    wt_set = []
    for a, b, c in arr[1:]:
        wt.append([a + 1, a + b, a + c])
        wt_set.extend([a + 1, a + b, a + c])
    return wt , len(wt_set) == len(set(wt_set))


vertex = generate_graph(10)
print(vertex)
print('weights')
wts , non_repeated = calculate_wts(vertex)
print(wts)
print('non repeated valuee flag :',non_repeated)




'''
plots not to show (not forming as expected)

'''
# def plot_star(labels):
#     G = nx.Graph()
#     center_node = labels[0]

#     for lst in labels[1:]:
#         G.add_edge(center_node, lst[0])
#         # G.add_edge(lst[0], lst[1])
#         # G.add_edge(lst[0], lst[2])


#     # # Add edges to the graph
#     # for label in labels:
#     #     center_node = label[0]
#     #     connected_nodes = label[1]
#     #     for node in connected_nodes[1:]:
#     #         G.add_edge(center_node, node)

#     # Draw the graph
#     pos = nx.spring_layout(G)  # positions for all nodes

#     nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")
#     plt.title("Star Graph")
#     plt.show()

# def plot_star_graph(n):
#     G = nx.star_graph(n)
#     pos = nx.spring_layout(G)
#     nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")
#     plt.title("Star Graph")
#     plt.show()

# Example: Plot a star graph with 10 nodes
# plot_star_graph(10)

# calculate k value

    
