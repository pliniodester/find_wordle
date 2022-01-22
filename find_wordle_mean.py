import wordle_bib as wb

# select the N-info words and the maximum number of guesses
N_letters = 5
N_guesses = 6

# the answer
answer = 'prick'

# builds the dictionary of words with N info
words = set()
with open('wordle.txt','r') as f:
    lines = f.readlines()
for word in lines:
    if len(word) == N_letters + 1:
        words.add(word[:-1])

info = []
for k in range(N_letters):
    info.append({'a','b','c','d','e','f','g','h','i','j','k','l','m','n',\
    'o','p','q','r','s','t','u','v','w','x','y','z'})
# this set is reserved for the mandatory info we do not know the position
info.append(set())

# code for optimized (heuristic) choice - NORMAL MODE
guess = 'rales' # initial guess is always the same
print(1,guess)
wb.try_word(guess,answer,info)
words_left = words.copy()
for k in range(2,N_guesses+1):
    count_min = len(words)*len(words)
    for guess in words_left.copy():
        if not(wb.check_word(guess,info)):
            words_left.remove(guess)
    print('- Candidates:',len(words_left))
    for guess in words:
        count = 0
        for ans_aux in words_left:
            info_aux = []
            for m in range(len(info)):
                info_aux.append(info[m].copy())
            wb.try_word(guess,ans_aux,info_aux)
            for guess_aux in words_left:
                if wb.check_word(guess_aux,info_aux):
                    count += 1
                    if count > count_min: # optimization
                        break
            if count > count_min: # optimization
                break
        if count < count_min:
            count_min = count
            best_guess = guess
            print('~',guess,count/len(words_left)/len(words_left))
    if len(words_left) < 3:
        best_guess = words_left.pop()
    print(k,best_guess)
    words_left.discard(best_guess)
    if wb.try_word(best_guess,answer,info):
        print('Congrats!')
        break
