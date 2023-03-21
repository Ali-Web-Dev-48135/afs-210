from stack import Stack
from queue import Queue


def isPalindrome(wordString: str) -> None:
    wordLetters = list(reversed(wordString))
    joinedBackWord = ''.join(wordLetters)
    print(joinedBackWord == wordString)


isPalindrome('racecar')
isPalindrome('noon')
isPalindrome('python')
isPalindrome('madam')
