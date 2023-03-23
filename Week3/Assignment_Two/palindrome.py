from stack import Stack
from queue import Queue


def isPalindrome(wordString: str) -> None:
    strStack = Stack()
    strQueue = Queue()

    for letter in wordString:
        strStack.push(letter)
        strQueue.enqueue(letter)

    for letter in wordString:
        equalOrNot = False
        if(strStack.pop() == strQueue.dequeue()):
            equalOrNot = True
        else:
            equalOrNot = False
    print(equalOrNot)


isPalindrome('racecar')
isPalindrome('noon')
isPalindrome('python')
isPalindrome('madam')
