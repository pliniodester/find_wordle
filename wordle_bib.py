# this contains the necessary functions to check and try guesses based
# on a list of sets called letters that contains the possible letters
# for each position

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
