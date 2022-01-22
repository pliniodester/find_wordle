import wordle_bib as wb

# function with the mean heuritic
# hard = True or False (normal or hard mode)
def find_wordle_mean(answer, guess, info, words, hard):
    guesses = [guess]
    if wb.try_word(guess,answer,info):
        return guesses
    words_left = words.copy()
    for k in range(2,10):
        count_min = len(words)*len(words)
        for guess in words_left.copy():
            if not(wb.check_word(guess,info)):
                words_left.remove(guess)
        # print('- Candidates:',len(words_left))
        if hard:
            words = words_left
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
                # print('~',guess,count/len(words_left)/len(words_left))
        if len(words_left) < 3:
            best_guess = words_left.pop()
        guesses.append(best_guess)
        if wb.try_word(best_guess,answer,info):
            return [k, guesses]

# function with the minmax heuritic
# hard = True or False (normal or hard mode)
def find_wordle_minmax(answer, guess, info, words, hard):
    guesses = [guess]
    if wb.try_word(guess,answer,info):
        return guesses
    words_left = words.copy()
    for k in range(2,9):
        count_min = len(words)*len(words)
        for guess in words_left.copy():
            if not(wb.check_word(guess,info)):
                words_left.remove(guess)
        # print('- Candidates:',len(words_left))
        count_minmax = len(words_left)
        if hard:
            words = words_left
        for guess in words:
            count_max = 0
            for ans_aux in words_left:
                count = 0
                info_aux = []
                for m in range(len(info)):
                    info_aux.append(info[m].copy())
                wb.try_word(guess,ans_aux,info_aux)
                for guess_aux in words_left:
                    if wb.check_word(guess_aux,info_aux):
                        count += 1
                    if count > count_minmax: # optimization
                        break
                if count_max < count:
                    count_max = count
                    worst_ans = ans_aux
                if count > count_minmax: # optimization
                    break
            if count_max < count_minmax:
                count_minmax = count_max
                best_guess = guess
                # print('~',guess,count_max/len(words_left))
        if len(words_left) < 3:
            best_guess = words_left.pop()
        guesses.append(best_guess)
        if wb.try_word(best_guess,answer,info):
            return guesses
    guesses.append(answer)
    return guesses

def find_wordle_mine(answer, guess, info, words):
    guesses = [guess]
    if wb.try_word(guess,answer,info):
        return guesses
    words_left = words.copy()
    for k in range(2,9):
        count_min = len(words)*len(words)
        for guess in words_left.copy():
            if not(wb.check_word(guess,info)):
                words_left.remove(guess)
        # print('- Candidates:',len(words_left))
        count_minmax = len(words_left)
        if k in {3,6}:
            words_aux = words_left
        else:
            words_aux = words
        for guess in words_aux:
            count_max = 0
            for ans_aux in words_left:
                count = 0
                info_aux = []
                for m in range(len(info)):
                    info_aux.append(info[m].copy())
                wb.try_word(guess,ans_aux,info_aux)
                for guess_aux in words_left:
                    if wb.check_word(guess_aux,info_aux):
                        count += 1
                    if count > count_minmax: # optimization
                        break
                if count_max < count:
                    count_max = count
                    worst_ans = ans_aux
                if count > count_minmax: # optimization
                    break
            if count_max < count_minmax:
                count_minmax = count_max
                best_guess = guess
                # print('~',guess,count_max/len(words_left))
        if len(words_left) < 3:
            best_guess = words_left.pop()
        guesses.append(best_guess)
        if wb.try_word(best_guess,answer,info):
            return guesses
    guesses.append(answer)
    return guesses

# select the N-info words and the maximum number of guesses
N_letters = 5

# builds the dictionary of words with N info
words = set()
with open('wordle.txt','r') as f:
    lines = f.readlines()
for word in lines:
    if len(word) == N_letters + 1: # +1 for the special char at the end of line
        words.add(word[:-1])

info = []
for k in range(N_letters):
    info.append({'a','b','c','d','e','f','g','h','i','j','k','l','m','n',\
    'o','p','q','r','s','t','u','v','w','x','y','z'})
# this set is reserved for the mandatory info we do not know the position
info.append(set())

# guess  = 'serai' # initial guess
# answer = 'prick'
# print('mean algo:  ',\
#  find_wordle_mean(answer,guess,info.copy(),words.copy()) )
# print('minmax algo:',\
#  find_wordle_minmax(answer,guess,info.copy(),words.copy()) )

guess = 'serai'
hist = [0] * 10
k = 0
for answer in words: # words
    info_aux = []
    for m in range(len(info)):
        info_aux.append(info[m].copy())
    guesses = find_wordle_mine(answer,guess,info_aux,words.copy())
    n = len(guesses)
    print(n, guesses)
    hist[n]+=1
    print(hist)
    k += 1
    if k == 1000:
        break
