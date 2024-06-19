#Question 1: Design a function that reverses the digits of an integer. For example, 50 should become 5 and -12 should become -21.

def reverse_integer(x):
    s = str(x)
    if s[0] == '-':
        reversed_s = '-' + s[:0:-1]
    else:
        reversed_s = s[::-1]
    reversed_x = int(reversed_s)
    return reversed_x
num1 = 50
num2 = -12
print(f"Reversed integer of {num1}: {reverse_integer(num1)}")
print(f"Reversed integer of {num2}: {reverse_integer(num2)}")


#Question 2: Write a recursive function to calculate the factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = 5
print(f"The factorial of {num} is {factorial(num)}")

    
#Question 3:Design a function that takes a string or sequence of characters as input and returns the character that appears most frequently.
#//Eg 11189 => '1'
#//hello => l
def most_frequent_char(input_str):
    if not input_str:
        return None 
    char_count = {}
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    max_char = None
    max_count = 0
    
    for char, count in char_count.items():
        if count > max_count:
            max_char = char
            max_count = count
    
    return max_char
input_str1 = "hello world"
input_str2 = "testing the function"
print(f"The most frequent character in '{input_str1}' is '{most_frequent_char(input_str1)}'")
print(f"The most frequent character in '{input_str2}' is '{most_frequent_char(input_str2)}'")




#Question 4:Design a function that determines whether a given string is a pangram. A pangram is a sentence or phrase containing every letter of the alphabet atleast once. Punctuation and case are typically ignored. For example, thestring "The quick brown fox jumps over the lazy dog" is a pangram, while "Hello, world!" is not.

def is_pangram(input_str):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    input_str_set = set(input_str.lower())

    return alphabet.issubset(input_str_set)

pangram1 = "The quick brown fox jumps over the lazy dog"
pangram2 = "This is not a pangram"

print(f'"{pangram1}" is a pangram: {is_pangram(pangram1)}')
print(f'"{pangram2}" is a pangram: {is_pangram(pangram2)}')

#Question 5:Design a function that takes a list of integers as input. The function shouldreturn True if the list contains two consecutive threes (3 next to a 3) anywhere the list. Otherwise, it should return False. For example, the function should return True for [1, 3, 3] and False for [1, 3, 1, 3].


def has_two_consecutive_threes(nums):
 
    for i in range(len(nums) - 1):  
        if nums[i] == 3 and nums[i + 1] == 3:
            return True 

    return False  
list1 = [1, 3, 4, 1, 2]
list2 = [1, 1, 2, 3, 3]
list3 = [1, 5, 2]
print(f"List {list1}: {has_two_consecutive_threes(list1)}")
print(f"List {list2}: {has_two_consecutive_threes(list2)}")
print(f"List {list3}: {has_two_consecutive_threes(list3)}")

#Question 6:Master Yoda, a renowned Jedi Master from the Star Wars universe, is known for his unique way of speaking. He often reverses the order of words in his sentences. For example, instead of saying "I am home" he might say "Home am I" Design a function that takes a sentence as input and returns a new sentence with the words reversed in the same order that Master Yoda would use.

def yoda_speak(sentence):
 
  words = sentence.split()
  reversed_words = words[::-1]
  reversed_sentence = ' '.join(reversed_words)
  
  return reversed_sentence

sentence = "I am home "
print(yoda_speak(sentence))



