#WRITE A FUNCTION THAT TAKES SENTENCE AS A INPUT AND THEN RETURNS DICTIONARY WITH A COUNT OF EACH LETTER IN THE SENTENCE 
def count_letters(sentence):
    letter_count = {}
    for char in sentence:
        if char.isalpha():
            char = char.lower() 
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

user_input = input("Enter a sentence: ")
result = count_letters(user_input)
print("Letter counts in the sentence:", result)
