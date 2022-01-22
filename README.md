# find_wordle

This is a study of the popular game Wordle (https://www.powerlanguage.co.uk/wordle/).

In find_wordle_mean.py we try a mean approach, i.e., we guess a word for which we have the least expected number of possible words for the next guess

In find_wordle_minmax.py we try a minmax approach, i.e., we guess a word for which we have the best worst-case scenario for the next guess


**Insights:**

The following words, if used as initial guesses, invalidate the majority of the words.

- RALES: μ = 0.02251, σ = 0.01817, max = 0.06407,
- SERAI: μ = 0.02429, σ = 0.01739, max = 0.05374,
- SOARE: μ = 0.02342, σ = 0.01786, max = 0.05929,

where the object being measured is the proportion of words that remained.
As usual, μ is the mean, σ is the standard deviation, and max is the worst case.
