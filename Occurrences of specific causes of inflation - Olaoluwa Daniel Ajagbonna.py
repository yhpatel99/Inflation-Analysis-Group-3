import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import string

nltk.download('punkt')

def clean_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Open the file in read mode
with open('C:/Users/danie/Downloads/School/Info/Inflation_Info.txt', 'r') as file:
    # Read the text of the file
    text = file.read()

# Clean the text
cleaned_text = clean_text(text)

# Tokenize the cleaned text
tokens = word_tokenize(cleaned_text)
token_counts = Counter(tokens)

causes_of_inflation = ["demand-pull inflation", "cost-push inflation", "built-in inflation", "the housing market", "expansionary monetary and fiscal policy", "monetary devaluation"]

for cause in causes_of_inflation:
    # Clean the cause of inflation
    cleaned_cause = clean_text(cause)
    # Count the occurrences of each cause of inflation
    cause_tokens = word_tokenize(cleaned_cause)
    count = sum(token_counts[token] for token in cause_tokens)
    print(f"{cause}: {count}")