import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
n = 100
runNum = 100

mrange = np.arange(0.10, 4, 0.25) #range for m parameter used in lognormal distribution
connect_array = np.zeros(len(mrange)) #stores the connectivity probability for graphs

for j, m in enumerate(mrange):
    for i in range( runNum ):

        degrees = np.rint(np.random.lognormal(mean  = m, size = n))
        #degrees should be a set of integer values
        degrees = degrees.astype(int)
        degrees *= 2 #sum of degrees should be even.
        G = nx.configuration_model( degrees ) #creates a graph with 
                                              #the given set of degrees

        connect_array[j] += nx.is_connected(G) #returns 1 if graph is connected


plt.xlabel('$m$')
plt.ylabel('connectivity probability')
plt.title('connected probability vs $m$')
plt.plot( mrange, connect_array ,'--o')