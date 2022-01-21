# select the N-letters words
N_letters = 5
N_guesses = 6
words = set()

# function that updates list of possible letters for a given guess
# letters is a list of N_letters sets containing the possible letters for each
# one of the spaces of the wordle
# It represents updating the information after a guess in wordle
def try_word(guess,answer,letters):
    flag = True
    for k in range(len(guess)):
        if guess[k]==answer[k]:
            letters[k] = {guess[k]}
        else:
            flag = False
            letters[k].discard(guess[k])
            y_flag = False
            for m in range(len(guess)):
                if guess[k]==answer[m]:
                    y_flag = 1
            if y_flag:
                letters[-1].add(guess[k])
            else:
                for m in range(len(guess)):
                    letters[m].discard(guess[k])
    if flag:
        return True
    else:
        return False

# function that checks if a word is plausible given a list of possible letters
def check_word(word,letters):
    for k in range(len(word)):
        if not(word[k] in letters[k]):
            return False
    for letter in letters[-1]: # letters[-1] has the mandatory letters
        flag = 0
        for k in range(len(word)):
            if word[k] == letter:
                flag = 1
        if flag==0:
            return False
    return True

# builds the dictionary of words with N letters
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
    if check_word(guess,letters):
        count = 0
        for ans_aux in words:
            letters_aux = []
            for m in range(len(letters)):
                letters_aux.append(letters[m].copy())
            try_word(guess,ans_aux,letters_aux)
            for guess_aux in words:
                if check_word(guess_aux,letters_aux):
                    count += 1
        print(guess,count/len(words)/len(words))
