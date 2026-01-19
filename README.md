# Norstop: Fast Norwegian Stopword Remover

**Norstop** is a lightweight, zero-dependency Python library designed to remove Norwegian stopwords from text with high speed and accuracy.

Unlike generic NLP libraries, Norstop handles Norwegian-specific nuances like:

- **Inflections:** Handles _har, hadde, hatt_ and _min, mi, mine_.
- **Dialects:** Includes common Nynorsk and Bokmål variations.
- **Punctuation:** Smart stripping ensures words like `«Hei,»` are processed correctly without destroying sentence structure.
- **Speed:** Uses optimized set lookups (`O(1)`) and avoids slow regex compilation.

## 🚀 Installation

You can install this library directly from GitHub using `pip`. No need to download files manually.

```bash
pip install git+https://github.com/vidito/norstop.git
```

## 📖 Usage

```python
from norstop import remove_stopwords

# Basic example
text = "Jeg er en gutt som liker å kode."
clean_text = remove_stopwords(text)
print(clean_text)
# Output: "gutt liker kode."

# Handling punctuation and quotes
quote = "Han sa: «Det er viktig»."
clean_quote = remove_stopwords(quote)
print(clean_quote)
# Output: "sa: viktig»."

```

## ⚡ Performance

Norstop is built for speed:

1. **No Dependencies:** Pure Python, no heavy frameworks like NLTK or SpaCy.
2. **Frozenset Lookups:** Checking if a word is a stopword happens instantly.
3. **Memory Efficient:** Stopwords are loaded as bytecode, not parsed from text files at runtime.

## 🤝 Contributing

We welcome contributions! The list of stopwords is maintained in a Python file for performance.

### How to add new stopwords:

1. Fork this repository.
2. Open the file `src/norstop/const.py`.
3. Add the new word to the `NORWEGIAN_STOPWORDS` set.

- **Please keep the list alphabetical.**
- Add all common inflections (e.g., if adding a verb, add past/present tense).

4. Submit a Pull Request.

### Development & Testing

To run the tests locally:

```bash
# Install in editable mode
pip install -e .

# Run the test suite
python -m unittest discover tests

```

```

```
