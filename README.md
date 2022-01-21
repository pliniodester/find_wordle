# find_wordle

This is a tentative of developing algorithms to solve the popular game Wordle (https://www.powerlanguage.co.uk/wordle/) efficiently.

In find_wordle_mean.py we try a mean approach, i.e., we guess a word for which we have the least expected number of possible words for the next guess

In find_wordle_minmax.py we try a minmax approach, i.e., we guess a word for which we have the best worst-case scenario for the next guess


**Insights:**

The following words, if used as initial guesses, invalidate the majority of the words.
The mean (expected) and standard deviation of the proportion of remaining words are

- RALES => 2.25% ± 1.82% remains
- SOARE => 2.34% ± 1.79% remains
