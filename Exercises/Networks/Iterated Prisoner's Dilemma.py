import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats



t = 1.5
run_num = 10000

win_lose_table = np.array( [ [[0, 0] , [1.5, 0]], [[0, 1.5], [1, 1]] ] )
def calc_score( a, b ):
    return win_lose_table[a, b]

def act( strategy, player ):
    if(strategy == 'random'):
        return np.random.randint(2)
    elif(strategy == 'coop'):
        return 1
    elif(strategy == 'defect'):
        return 0
    elif (strategy == 'tit for tat'):
        if(i >= 1):        
            otherplayer = (player + 1) % 2
            return actions[i-1, otherplayer]
        else:
            return 1
    elif (strategy == 'win stay lose shift'):
        if(i >= 1):
            if ( calc_score( actions[i-1,0], actions[i-1,1] )[player] == 0 ):
                return (actions[i-1, player] + 1) % 2
            else:
                return actions[i - 1, player]
        else:
            return 1

strategies = ['defect', 'coop', 'random', 'tit for tat', 'win stay lose shift']
results = pd.DataFrame(index = strategies, columns = strategies)

for strategy1 in strategies:
    for strategy2 in strategies:
        #print (strategy1, "vs.", strategy2)
        actions = np.zeros( (run_num, 2), int )
        score = np.zeros(2)
        for i, action in enumerate(actions):
            actions[i] = np.array([act(strategy1, 0), act(strategy2, 1)])
            score += calc_score( actions[i,0], actions[i,1] ) 
        results[strategy1][strategy2] = score[1] / run_num
        """
        if(score[0] > score[1]):
            print(strategy1 , "has won!!!" + '\n')
        elif(score[1] > score[0]):
            print(strategy2 , "has won!!!" + '\n')
        else:
            print("it's a draw!!!" + '\n')
            #print(score)
        """ 
#print(results)

for i in range( len(results) ):
    label = results.iloc[i].name 
    plt.plot(results.iloc[i], '--o', label = label)


plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
plt.grid()
plt.suptitle('score average for each strategy against other strategies', y = 0)
plt.show()