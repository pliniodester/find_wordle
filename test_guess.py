import wordle_bib as wb
import numpy as np

# select the N-letters words and the maximum number of guesses
N_letters = 5
N_guesses = 6

# builds the dictionary of words with N letters
words = set()
with open('wordle.txt','r') as f:
    lines = f.readlines()
for word in lines:
    if len(word) == N_letters + 1:
        words.add(word[:-1])

letters = []
for k in range(N_letters):
    letters.append({'a','b','c','d','e','f','g','h','i','j','k','l','m','n',\
    'o','p','q','r','s','t','u','v','w','x','y','z'})
# this set is reserved for the mandatory letters we do not know the position
letters.append(set())

# code to check a quality of initial guess
for guess in {'adieu', 'aesir', 'raise'}: # 'rales', 'soare', 'rathe', 'serai'
    remaining = [];
    for ans_aux in words:
        count = 0
        letters_aux = []
        for m in range(len(letters)):
            letters_aux.append(letters[m].copy())
        wb.try_word(guess,ans_aux,letters_aux)
        for guess_aux in words:
            if wb.check_word(guess_aux,letters_aux):
                count += 1
        remaining.append(count)
    print(guess,\
    "μ = {:.5f},".format(np.mean(remaining)/len(words)),\
    "σ = {:.5f},".format(np.std(remaining)/len(words)),\
    "max = {:.5f}.".format(np.amax(remaining)/len(words)) )
