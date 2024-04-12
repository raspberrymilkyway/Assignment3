#created common methods to calculate weights and to check if pattern is valid or not
from problem_1 import calculate_wts, is_valid 
import math


'''
generate graph where 0th index contains center which is 1 by default

after every index is the list say [a,b,c....nth_elements]
a is the node conncted to center
and rest other nodes b,c... are connected to a

returns list 
'''
def generate_graph(n,m):
    lables = [1, [1]]
    wts = [2]
    v = m*n + 1
    d = math.ceil(v/2) / (n - 1) # 2.272727 in our case

    # generate edges connected to center
    for i in range(1,n):
        value = math.floor(d*i)
        lables.append([value])
        wts.append(value + 1)
    
    # generate pendent lables
    for i in range(n):
        assumed_label = min(wts) # wts[i] # this condition looks bad so i changed it to minimum value of weight in wts array

        for j in range(m-1):
            while (lables[i+1][0] + assumed_label) in wts:
                assumed_label += 1
            wts.append(lables[i+1][0] + assumed_label)
            lables[i+1].append(assumed_label)
    
    return lables , wts



# main
if __name__ == "__main__": 
    m = 4
    n = 12
    k = math.ceil((m*n + 1)/2)
    labels,wts = generate_graph(n,m)
    print('k value',k)
    print('labels :',labels)
    print('weights :',calculate_wts(labels))
    print('is valid lables:',is_valid(labels,k))