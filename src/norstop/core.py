from .const import NORWEGIAN_STOPWORDS

# using text.split() is faster than regex for this specific task.


def remove_stopwords(text: str) -> str:
    """
    Removes Norwegian stopwords from a string.

    Strategy:
    1. Split by whitespace (fastest tokenization).
    2. Strip punctuation from the edges of words.
    3. Check against the frozenset.
    4. Join back together.
    """
    if not text:
        return ""

    # We strip a wide range of punctuation so "Hei," matches "Hei"
    # and "(og)" matches "og".
    return " ".join(
        word
        for word in text.split()
        if word.lower().strip(".,!?:;\"'()[]{}«»-") not in NORWEGIAN_STOPWORDS
    )
