from random import randint


#Ill be honest Mr. Robert I'm not sure about the time comlexity of my code. It maybe 0(1) since I iterate based on the length of the list.

def shufflefunction(nlist):
    length_of_list = len(nlist)

    for i in range(length_of_list):
        index_random = randint(i, length_of_list - 1) 
        nlist[i], nlist[index_random] = nlist[index_random], nlist[i]
    return nlist


nlist = [7, 12, 18, 20, 25, 31, 36, 50, 88, 90, 100, 108]
print("Original list Is: ", nlist)


shuffled_list = shufflefunction(nlist)
print("Shuffled List Is: ", shuffled_list)

