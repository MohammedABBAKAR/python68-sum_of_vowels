
# todo Sum of v0w3ls
# ? Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers.

# Vowel	Number
# A	4
# E	3
# I	1
# O	0
# U	0
# ? Examples
# ? sum_of_vowels("Let\'s test this function.") ➞ 8

# sum_of_vowels("Do I get the correct output?") ➞ 10

# sum_of_vowels("I love edabit!") ➞ 12
# Notes
# Vowels are case-insensitive (e.g. A = 4 and a = 4).

def sum_of_vowels(sentence):
    v0w3ls = {
        'A': 4, 
        'E': 3,
        'I': 1,
        'O': 0,
        'U': 0
    }
    summ = 0
    # Convert the string to uppercase for case-insensitive matching
    for char in sentence.upper():
        if char in v0w3ls:
            summ += v0w3ls[char]
    return summ

# Test the function
print(sum_of_vowels("Do I get the correct output"))  # ➞ 10



def sum_of_vowels(string):
    # Define the vowel to number mapping
    vowel_mapping = {'A': 4, 'E': 3, 'I': 1, 'O': 0, 'U': 0}
    
    # Convert the string to uppercase and calculate the sum of vowel values
    return sum(vowel_mapping.get(char.upper(), 0) for char in string if char.upper() in vowel_mapping)

# Test cases
test_cases = [
    "Let's test this function.",
    "Do I get the correct output?",
    "I love edabit!"
]

# Apply the function to the test cases
results = {test: sum_of_vowels(test) for test in test_cases}
results
