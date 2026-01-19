# Norstop: Fast Norwegian Stopword Remover

**Norstop** is a lightweight, zero-dependency Python library designed to remove Norwegian stopwords from text with high speed and accuracy.

Unlike generic NLP libraries, Norstop handles Norwegian-specific nuances like:

- **Inflections:** Handles _har, hadde, hatt_ and _min, mi, mine_.
- **Dialects:** Includes common Nynorsk and Bokmål variations.
- **Punctuation:** Smart stripping ensures words like `«Hei,»` are processed correctly without destroying sentence structure.
- **Speed:** Uses optimized set lookups (`O(1)`) and avoids slow regex compilation.

## 🚀 Installation

First create a Virtual Environment in a folder of your choice.

```bash
python -m venv venv
```

Then Activate it:

```bash
# Windows
venv\Scripts\activate
# MacOS
source venv/bin/activate
```

Then you can install this library directly from GitHub using `pip`. No need to download files manually.

```bash
pip install git+https://github.com/vidito/norstop.git
```

You can also reinstall it using:

```bash
pip install --force-reinstall git+https://github.com/vidito/norstop.git
```

## 📖 Usage

After installing the library you can create a python file like main.py with the following:

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

and run it in the terminal:

```bash
python main.py
```

## ⚡ Performance

Norstop is built for speed:

1. **No Dependencies:** Pure Python, no heavy frameworks like NLTK or SpaCy.
2. **Frozenset Lookups:** Checking if a word is a stopword happens instantly.
3. **Memory Efficient:** Stopwords are loaded as bytecode, not parsed from text files at runtime.

Here’s a clean, beginner‑friendly version that directly references **your actual repository** at `https://github.com/Vidito/norstop.git` and guides contributors step by step.

---

## 🤝 Contributing

Thank you for helping improve **norstop**!  
Follow these simple steps to add new Norwegian stopwords.

### 1. Fork the repository

Go to the project page:  
**https://github.com/Vidito/norstop.git**  
Click **Fork** to create your own copy.

### 2. Clone your fork

Download your fork to your computer:

```bash
git clone <your-fork-url>
cd norstop
```

### 3. Open the stopwords file

Navigate to:

```
src/norstop/const.py
```

Inside, you’ll find the `NORWEGIAN_STOPWORDS` set.

### 4. Add your stopword

- Add your new word to the set.
- Keep the list **alphabetical**.
- Add **common inflections** (for example, for verbs: present, past, participle).

### 5. Save and test

If the project has tests or examples, run them to ensure everything still works.

### 6. Commit your changes

```bash
git add src/norstop/const.py
git commit -m "Added (a number) new Norwegian stopwords"
```

### 7. Push and open a Pull Request

```bash
git push origin main
```

Then visit your fork on GitHub and click **New Pull Request**.

---

### Development & Testing

To run the tests locally:

```bash
# Install in editable mode
pip install -e .

# Run the test suite
python -m unittest discover tests

```
