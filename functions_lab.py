# CALCULATE THE CUBE
def cube(n):
    return n**3
result=cube
re= cube(3)
print(re)
print(result(3))

#EXAMPLES OF LOCAL &GLOBAL VARIABLE
num_1=100 #GLOBAL VARIABLE(AS DECLARED OUTSIDE THE BLOCK)
def func_1():
    num_1=40 #LOCAL VARIABLE(AS DECLARED INSIDE THE BLOCK)
    print(num_1)

def func_2():
    print(num_1)

func_1()
func_2()

#THROUGH LIST
List_1=[1,2,3,4,5]#GLOBAL VARIABLE
def func_1():
    del List_1[0]
    print(List_1)

def func_2():
    List_1.append(25)
    print(List_1)

func_1()
func_2()

#WRITE A PYTHON PROGRAM THAT TAKES SENTENCE AS INPUT AND RETURNS DICTIONARY WITH THE COUNT OF EACH WORD
def word_count(sentence):
    word_count = {}
    words = sentence.split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    words_1=word_count
    return words_1

user_sentence = input("Enter a sentence:\n ")
word_counts = word_count(user_sentence)
print("Sentence:", user_sentence)
print("Word Counts:", word_counts)
    


#WRITE A PYTHON CALCULATE THE FREQUENCY OF EACH WORD IN THE SENTENCE
def word_and_letter_count(sentence):
    word_count = {}
    letter_count = {}

    words = sentence.split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

        for letter in word:
            letter_count[letter] = letter_count.get(letter, 0) + 1

    return word_count, letter_count

user_sentence = input("Enter a sentence:\n")

word_counts, letter_counts = word_and_letter_count(user_sentence)

print("Sentence:", user_sentence)
print("Word Counts:", word_counts)
print("Letter Counts:", letter_counts)