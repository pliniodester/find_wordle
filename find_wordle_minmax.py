import wordle_bib as wb

# select the N-letters words
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

# code for optimized (heuristic) choice - NORMAL MODE
guess = 'rales' # initial guess is always the same
print(1,guess)
wb.try_word(guess,answer,letters)
words_left = words.copy()
for k in range(2,N_guesses+1):
    count_min = len(words)*len(words)
    for guess in words_left.copy():
        if not(wb.check_word(guess,letters)):
            words_left.remove(guess)
    print('- Candidates:',len(words_left))
    count_minmax = len(words_left)
    for guess in words:
        count_max = 0
        for ans_aux in words_left:
            count = 0
            letters_aux = []
            for m in range(len(letters)):
                letters_aux.append(letters[m].copy())
            wb.try_word(guess,ans_aux,letters_aux)
            for guess_aux in words_left:
                if wb.check_word(guess_aux,letters_aux):
                    count += 1
            if count_max < count:
                count_max = count
                worst_ans = ans_aux
        if count_max < count_minmax:
            count_minmax = count_max
            best_guess = guess
            print('~',guess,count_max/len(words_left))
    if len(words_left) < 3:
        best_guess = words_left.pop()
    print(k,best_guess)
    words_left.discard(best_guess)
    if wb.try_word(best_guess,answer,letters):
        print('Congrats!')
        break
