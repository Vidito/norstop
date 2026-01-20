from .const import NORWEGIAN_STOPWORDS

EDGE_CHARS: str = """.,!?:;\"'()[]{}«»…–—''""„"""


def remove_stopwords(text: str) -> str:
    """
    Removes Norwegian stopwords from text while preserving punctuation.

    Fast, dependency-free implementation using walrus operator for efficiency.
    """
    if not text:
        return ""

    return " ".join(
        word
        for word in text.split()
        if (core := word.strip(EDGE_CHARS)) and core.lower() not in NORWEGIAN_STOPWORDS
    )
