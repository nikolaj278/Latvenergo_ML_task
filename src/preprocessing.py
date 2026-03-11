import re

def basic_prep(text, rem_punct=False):
    """
    Do basic preprocessment by normalising
    punctuation and whitespaces

    Args:
        text (str): text to preprocess
        rem_punkt (bool): remove punctuation or normalise it

    Returns:
        text (str): preprocessed text
    """

    replacements = {
        "“": '"', "”": '"',
        "‘": "'", "’": "'",
        "—": "-", "–": "-",
        "…": "..."
    }
    if rem_punct:
        text = re.sub(r"[^\w\s]", "", text) # remove punctuation
    else:
        for a, b in replacements.items():
            text = text.replace(a, b) # normalise punctuation
    
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text) # whitespaces
    
    return text 