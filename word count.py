#WRITE A FUNCTION THAT TAKES SENTENCE AS INPUT AND RETURNS A DICTIONARY WITH A COUNT OF WORD IN SENTENCE
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
