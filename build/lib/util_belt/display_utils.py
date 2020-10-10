from termcolor import colored
import numpy as np
colors = ['blue','red', 'cyan','green', 'yellow', 'magenta', 'cyan', 'white','grey',]
color = ''
def pretty_array(arr,colorify= False,axis=0):
    if len(arr.shape)==2:
        arr=arr.reshape(1,arr.shape[0],arr.shape[1])
    elif len(arr.shape)==1:
        arr=arr.reshape(1,1,arr.shape[0])
    for index_1,i in enumerate(np.flip(arr,axis = 0)):
        if axis == 0:
            color = colors[index_1%len(colors)]
        for index_2, j in enumerate(np.flip(i,axis = 0)):
            if axis==1:
                color = colors[index_2%len(colors)]
            print(" " * (len(i) - 1 - index_2) + " / ", end="") 
            for index_3, k in enumerate(j):
                if axis==2:
                    color = colors[index_3%len(colors)]
                if colorify == False:
                    color = None
                print(colored(str(k).ljust( (len(str(np.amax(arr)))) + 1),color), end="") 
            print("/") 
        print()