
def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

def loop1Rec(num, odd_sum = 0):
    # Duplicate the loop1 function using recursion
    if(num <= 0):
        return odd_sum
    if(num % 2) == 1:
        odd_sum += num
        num -= 1
        return loop1Rec(num, odd_sum)
    else:
        num -= 1
        return loop1Rec(num, odd_sum)
    

def loop2Rec(num,even_sum = 0):
    # Duplicate the loop2 function using recursion
    if(num <= 2):
        return even_sum
    if(num % 2) == 0:
        num -= 2
        even_sum += num
        return loop2Rec(num, even_sum)
    else:
        num -= 2
        return loop2Rec(num, even_sum)

print("Sum of odds between 1 and 20 using 'for' loop =", loop1())
print("Sum of odds between 1 and 20 using recursion =",loop1Rec(20))
print("Sum of evens between 1 and 20 using 'while' loop =",loop2())
print("Sum of evens between 1 and 20 using recursion=",loop2Rec(20))
