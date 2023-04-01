
def binarySearchFunc(list, term):
    start = 0
    high = len(list) - 1 
    
    while start <= high:
        middle = int((start + high) / 2) # divides the length and returns the middle of the list / 2.
        guess = list[middle]
        if guess < term:  
            start = middle + 1
        elif guess > term:
            high = middle - 1
        else:
            return True
    return False


array1 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81] 

array3 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"] 


print(binarySearchFunc(array1, 31))
print(binarySearchFunc(array1, 77))
print(binarySearchFunc(array3, "Delta"))
