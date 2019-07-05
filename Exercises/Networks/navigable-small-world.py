import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#np.random.seed(1)
ave_steps = 0
T = 200
n = 10 #number of vertices in one row. total number of vertices will be n ** 2
run_num = 1000 #number of runs for each q value
q_num = 10 #range of the values for q
qrange = range(q_num) #values for q
average_distance = np.zeros(q_num) #average distance for each setting
for q_i, q in enumerate(qrange):
    for run in range(run_num):
        G = nx.generators.navigable_small_world_graph(n, p = 1, q = q , dim = 2)
        #creates a navigable small world network
        #q is the number of extra edges

        u = 0 #index of the first vertex
        v = n ** 2 - 1 #index of the last vertex
        source = list(G)[u]
        position = source
        target = list(G)[v]
    
        dists = []
        for t in range(T):
            if position != target:
                dists =[]
                neighbors = list( nx.neighbors(G, position) )
                for neighbor in neighbors: #finds the most apparently close node
                    apparent_dist = np.sum( np.abs( np.array(neighbor) - np.array(target) ) )
                    #the distance on the grid (not considerng the shortcuts created)
                    dists.append(apparent_dist)
    
                    
                apparent_nearest_ind = np.argmin(dists)
                apparent_nearest = neighbors[apparent_nearest_ind] 
        
                position = apparent_nearest  #move to the new position
                
        
        
            else:
                break            
        
        ave_steps += t
        if not run % 100:
            print('run: ', run)
    
    ave_steps /= run_num
    average_distance[q_i] = ave_steps
    print('average steps number =', ave_steps)

plt.plot(qrange, average_distance ,'--o')