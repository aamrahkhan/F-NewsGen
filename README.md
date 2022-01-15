# F-NewsGen

A fake news classifier

## Apr 18, 2021 at 18:40

    1. Inspected the dataset and identified parts which needed cleaning and pre-processing
    2. Removed extraneous variables
    3. Cleaned non-English special characters from the fake news dataset

_Next Steps:_
Replicate on True dataset. Split dataset into train + test + validation. Analyse and process more of the text using NLP techniques.

## Apr 25, 2021 at 14:23

    1. Removed extra columns from the true news dataset

## May 23, 2021 at 18:00

    1. Removed duplicates from the main dataset
    2. Solved problem with shallow copy and used df.copy
    3. Randomised the main dataset and extracted 10% of the rows separately as a test dataset

_Next Steps:_
Tokenise the dataset and implement Bag-of-Words, a basic logistic regression model, and create a function to evaluate model metrics

# Dec 3, 2021 at 21:18

    1. Find a way to remove typed.js object on form submit action