# -*- coding: utf-8 -*-
"""
week1
"""

import comp_prob_inference

comp_prob_inference.flip_fair_coin()
flips = comp_prob_inference.flip_fair_coins(100)
comp_prob_inference.plot_discrete_histogram(flips)
comp_prob_inference.plot_discrete_histogram(flips, frequency=True)

# Next, let's plot the fraction of heads as a function of the number of flips 
# (going up to 100,000 flips).
n = 100000
heads_so_far = 0
fraction_of_heads = []
for i in range(n):
    if comp_prob_inference.flip_fair_coin() == 'heads':
        heads_so_far += 1
    fraction_of_heads.append(heads_so_far / (i+1))

# Note that fraction_of_heads[i] tells us what the fraction of heads is after 
# the first i tosses. Then to actually plot the fraction of heads vs the number 
# of tosses, enter the following:

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 4))
plt.plot(range(1, n+1), fraction_of_heads)
plt.xlabel('Number of flips')
plt.ylabel('Fraction of heads')

