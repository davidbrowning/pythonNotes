############################################################################################################################
#  Supervised v unsupervised learning
# Supervised algo's work on categorized data (emails as spam, chars with labels, etc)
# Why unsupervised?
#   latent variables
#       (not directly observable)
# Why Supervised?
#   lots of categorized data, used to predict answers for new/unseen values.
# Example: # server hits == 10000
# Example: predicting prices of new cars from prices of sold cars
#
# How do you test how good your supervised model is?
#  split the data into training and test.
#
#
# Use training to train, and test to test. (Lots of data? 50%50 not so much? 70%30)
# Fallible. (Small sample size, Overfitting, train/test could be too similar)
#
# K-fold Cross Validation
#  Split data into K segments. 1 fold for testing, use the others for training.
# Repeat.
#
#
############################################################################################################################
