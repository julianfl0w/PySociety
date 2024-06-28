import random
import string

def laffLLM(mean_length, word_count):
    sentence = []
    for _ in range(word_count):
        word_length = int(random.gauss(mean_length, 2))  # Generate word length from normal distribution
        if word_length < 1:
            word_length = 1  # Ensure word length is at least 1
        word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        sentence.append(word)
    # Optionally, add a period at the end
    sentence = ' '.join(sentence) + '.'
    return sentence

# Generate a sentence with words up to 10 characters long, total of 5 words
random_sentence = laffLLM(6, 5)
print(random_sentence)
