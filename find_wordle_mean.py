# the answer
answer = 'point'
# select the N-letters words
N_letters = 5
N_guesses = 6
words = set()

# function that updates list of possible letters for a given guess
# letters is a list of N_letters sets containing the possible letters for each
# one of the spaces of the wordle
# Analogous to updating the information after a guess in wordle
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
                letters[k].discard(guess[k])
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

# code for optimized (heuristic) choice - NORMAL MODE
guess = 'soare' # initial guess, otherwise it takes too long
print(1,guess)
try_word(guess,answer,letters)
words_left = words.copy()
for k in range(2,N_guesses+1):
    count_min = len(words)*len(words)
    for guess in words_left.copy():
        if not(check_word(guess,letters)):
            words_left.remove(guess)
    print('Candidates:',len(words_left))
    for guess in words:
        count = 0
        for ans_aux in words_left:
            letters_aux = []
            for m in range(len(letters)):
                letters_aux.append(letters[m].copy())
            try_word(guess,ans_aux,letters_aux)
            for guess_aux in words_left:
                if check_word(guess_aux,letters_aux):
                    count += 1
                    if count > count_min:
                        break
        if count < count_min:
            count_min = count
            best_guess = guess
            print('~',guess,count/len(words_left)/len(words_left))
    if len(words_left) < 3:
        print(words_left)
        best_guess = words_left.pop()
    print(k,best_guess)
    words_left.discard(best_guess)
    if try_word(best_guess,answer,letters):
        print('Congrats!')
        break

# # code to check a quality of a guess
# guess = 'rathe' # audio, soare, rathe
# if check_word(guess,letters):
#     count = 0
#     for ans_aux in words:
#         letters_aux = []
#         for m in range(len(letters)):
#             letters_aux.append(letters[m].copy())
#         try_word(guess,ans_aux,letters_aux)
#         for guess_aux in words:
#             if check_word(guess_aux,letters_aux):
#                 count += 1
#     print(guess,count/len(words)/len(words))