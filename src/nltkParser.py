import nltk
from nltk.tokenize import word_tokenize

# Function to convert words to their POS types
def words_to_pos_types(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    # Tag each word with its part of speech
    tagged_words = nltk.pos_tag(words)
    
    # Map NLTK's POS tags to a more readable format or type
    pos_map = {
        'NN': 'Noun', 'NNS': 'Noun', 'NNP': 'Proper noun', 'NNPS': 'Proper noun',
        'VB': 'Verb', 'VBD': 'Verb', 'VBG': 'Verb', 'VBN': 'Verb', 'VBP': 'Verb', 'VBZ': 'Verb',
        'JJ': 'Adjective', 'JJR': 'Adjective', 'JJS': 'Adjective',
        'RB': 'Adverb', 'RBR': 'Adverb', 'RBS': 'Adverb',
        'IN': 'Preposition', 'DT': 'Determiner', 'PRP': 'Pronoun', 'PRP$': 'Possessive pronoun',
        'CC': 'Conjunction', 'CD': 'Cardinal number', 'EX': 'Existential there', 'FW': 'Foreign word',
        'MD': 'Modal', 'PDT': 'Predeterminer', 'POS': 'Possessive ending', 'RP': 'Particle',
        'SYM': 'Symbol', 'TO': 'To', 'UH': 'Interjection', 'WDT': 'Wh-determiner',
        'WP': 'Wh-pronoun', 'WP$': 'Possessive wh-pronoun', 'WRB': 'Wh-adverb', 
        ',': 'Comma', '.': 'Dot', ':': 'Colon', ';': 'Semicolon', '``': 'DoubleQuote',
        "''": 'DoubleQuote', '`': 'Quote', "'": 'Quote',
        '-LRB-': 'Punctuation', '-RRB-': 'Punctuation',  # These are for '(' and ')'
        '-LSB-': 'Punctuation', '-RSB-': 'Punctuation',  # These are for '[' and ']'
        '-LCB-': 'Punctuation', '-RCB-': 'Punctuation',  # These are for '{' and '}'
        'OTHER': 'Other'
    }

    # Replace each word with its POS type based on the mapping
    pos_types = [pos_map.get(tag, 'Other') for word, tag in tagged_words]
    return ', '.join(pos_types)


