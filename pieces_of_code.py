# def check_word(yellow_list, green, word):
#     for k in range(len(word)):  #verify green letters
#         if (green[k]!='0')&(word[k]!=green[k]):
#             return False
#     for yellow in yellow_list: #verify yellow letters
#         for k in range(len(word)):
#             if yellow[k]!='0':
#                 letter = yellow[k]
#             if yellow[k]==word[k]:
#                 return False
#         flag = 0
#         for k in range(len(word)):
#             if word[k]==letter:
#                 flag = 1
#         if flag == 0:
#             return False
#     return True

# def try_word(word,answer):
#     result = []
#     for k in range(len(word)):
#         if answer[k]==word[k]:
#             result.append('g')
#         else:
#             for j in range(len(word)):
#                 if answer[k]
#     return str(result)

# # simple working code
# for k in range(N_guesses):
#     for guess in words:
#         if check_word(guess,letters):
#             break
#     print(guess)
#     if try_word(guess,answer,letters):
#         break

# # code for optimized (heuristic) choice - HARD MODE
# guess = 'soare'
# print(1,guess)
# try_word(guess,answer,letters)
# for k in range(2,N_guesses+1):
#     count_min = len(words)*len(words)
#     count = 0
#     print(len(words))
#     for guess in words.copy():
#         if check_word(guess,letters):
#             count += 1
#         else:
#             words.remove(guess)
#     print('Candidates:',count)
#     for guess in words:
#         count = 0
#         for ans_aux in words:
#             letters_aux = []
#             for m in range(len(letters)):
#                 letters_aux.append(letters[m].copy())
#             try_word(guess,ans_aux,letters_aux)
#             for guess_aux in words:
#                 if check_word(guess_aux,letters_aux):
#                     count += 1
#                     if count > count_min:
#                         break
#         if count < count_min:
#             count_min = count
#             best_guess = guess
#         print(guess,count/len(words))
#     print(k,best_guess)
#     if try_word(best_guess,answer,letters):
#         break
