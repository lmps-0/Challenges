# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 18:17:14 2021

@author: Lucas Manassés
"""

#%%

# She has N rooms -> numbered from 1 to N

# She has N descendants (each descendant is also numbered from 1 to N)

#%%
N=1
while (N != 0):

    N = input("\nTell me the number of Rooms: ")
    
    N = int(N) # number_of_rooms
    
    list_number_of_rooms = []
    
    for i in range(N):
        list_number_of_rooms.append(False)   # False -> Door closed
        # print(list_number_of_rooms)
    
     
    # print(list_number_of_rooms)
    
    for i in range(N): # i new entering 
        # print(i+1)
        for j in range(N): # j room
            # print(j+1)
            if ((j+1)%(i+1)) == 0:
                # print("Change state")
                if list_number_of_rooms[j] == True:
                    state = False
                if list_number_of_rooms[j] == False:
                    state = True
                # update
                list_number_of_rooms[j] = state
                # print(list_number_of_rooms)
                  
    for t in range(N):
        if list_number_of_rooms[t] == True: # Door Open
            print(t+1,end=" ")

#%%   