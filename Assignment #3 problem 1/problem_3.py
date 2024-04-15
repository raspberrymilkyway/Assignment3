#created common method to check if pattern is valid or not
from problem_1 import is_valid 
import math


'''
generate graph where 0th index contains center which is k by default

after every index is the list say [a,b,c....nth_elements]
a is the node conncted to center
and rest other nodes b,c... are connected to a 
(not including the connections between the centroid vertices, since they'd be labelled twice)

returns list 
'''
def generate_trampoline(n,m,k,e): # (rename according to the algorithm name we pick)
    labels = [k]
    used_weights = []

    
    used_weights = [False] * (e + 1)

    # generate labels and edges connected to center
    # first half of graph; work forwards from 0 to midpoint (inclusive)
    mid = math.ceil(n/2)
    prev = -1
    for i in range(1,mid+1):
        for j in range(i, k):
            if not used_weights[j + k] and (i == 1 or (i != 1 and not used_weights[prev + j])):
                labels.append([j])
                used_weights[j + k] = True
                if (prev != -1):
                    used_weights[j + prev] = True
                prev = j
                break
    
    # second half of graph; work backwords from n to midpoint (exclusive)
    prev = labels[1][0]
    for i in range(n, mid, -1):
        for j in range(k-1, i-1, -1):
            if not used_weights[j + k] and not used_weights[prev + j]:
                if i != mid+1 or (i == mid+1 and not used_weights[labels[mid][0] + j]):
                    labels.insert(mid+1,[j])
                    used_weights[j + k] = True
                    used_weights[j + prev] = True
                    if i == mid+1:
                        used_weights[labels[mid][0] + j] = True
                    prev = j
                    break
    
    # generate pendent labels
    prev = 2
    for i in range(n):
        for j in range(m-1):
            #run through all available edges; pull the lowest out and use it on the next pendant
            low_avail = -1
            for z in range(prev,e):
                if not used_weights[z]:
                    low_avail = z
                    prev = low_avail + 1
                    break
            if low_avail == -1: # error; not all weights could be used
                return labels, used_weights
            
            #find pendant vertex value
            calc = low_avail - labels[i+1][0]
            used_weights[low_avail] = True
            labels[i+1].append(calc)
            
    
    return labels , used_weights

'''
returns: 
    1. wt array -  as same as previous problems
    2. cent - cycle wts in formate [actual_wt , (label_left , label_right)]
'''
def calculate_wts(arr):
    #normal weights -- those found in this problem, without edges between the centroid vertices
    wt = []
    for label in arr[1:]:
        temp = [arr[0]+label[0]]
        for num in label[1:]:
            temp.append(label[0] + num)
        wt.append(temp)

    #centroid edge weights
    # left a second method of printing in 
    # currently is just an array of edges -- [edge,...]
    # commented out is an array of arrays with a tuple containing the vertices used -- [[(vertex, vertex),edge],...]
    cent = []
    prev = arr[1][0]
    for label in arr[2:]:
        temp = prev + label[0]
        # temp = [(prev, label[0]), prev + label[0]]
        cent.append([temp , (prev , label[0])])
        prev = label[0]
    cent.append(arr[-1][0] + arr[1][0], (arr[-1][0], arr[1][0]))
    # cent.append([(arr[-1][0], arr[1][0]), arr[-1][0] + arr[1][0]])
    return wt, cent


# main
if __name__ == "__main__": 
    m = 3
    n = 8
    k = math.ceil(((m+1)*n + 1)/2)
    e = (m+1)*n + 1 # to find total no of edges including centroid
    # v = m*n + 1 # total no of vertex in graph
    labels,wts = generate_trampoline(n,m,k,e)
    print('k value:\t',k)
    print('labels:\t\t',labels)
    standard, centroid_cycle = calculate_wts(labels)
    print('weights:\t',standard)
    print('cycle weights:\t', centroid_cycle)
    print('is valid labels:',is_valid(labels,k))
