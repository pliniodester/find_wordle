import wordle_bib as wb

# select the N-letters words and the maximum number of guesses
N_letters = 5
N_guesses = 6

# the answer
answer = 'robot'

# builds the dictionary of words with N letters
words = set()
with open('wordle.txt','r') as f:
    lines = f.readlines()
for word in lines:
    if len(word) == N_letters + 1:
        words.add(word[:-1])

letters = []
for k in range(N_letters):
    letters.append({'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'\
    ,'p','q','r','s','t','u','v','w','x','y','z'})
# this set is reserved for the mandatory letters that we do not know the position
letters.append(set())

# code to check a quality of initial guess
for guess in {'ariot', 'irate', 'oater', 'orate', 'ratio', 'retia', 'roate', 'terai', 'tiare'}:
    if wb.check_word(guess,letters):
        count = 0
        for ans_aux in words:
            letters_aux = []
            for m in range(len(letters)):
                letters_aux.append(letters[m].copy())
            wb.try_word(guess,ans_aux,letters_aux)
            for guess_aux in words:
                if wb.check_word(guess_aux,letters_aux):
                    count += 1
        print(guess,count/len(words)/len(words))
