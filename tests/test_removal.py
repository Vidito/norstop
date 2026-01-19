import unittest
from norstop.core import remove_stopwords


class TestNorwegianStopwords(unittest.TestCase):

    def test_basic_removal(self):
        """Test simple sentences with common stopwords."""
        text = "jeg er en gutt og jeg liker mat"
        # 'jeg', 'er', 'en', 'og' should be removed. 'gutt', 'liker', 'mat' remain.
        expected = "gutt liker mat"
        self.assertEqual(remove_stopwords(text), expected)

    def test_capitalization(self):
        """Test that capitalization doesn't affect removal."""
        text = "Jeg Er en Gutt"
        # 'Jeg' and 'Er' and 'en' should be removed.
        expected = "Gutt"
        self.assertEqual(remove_stopwords(text), expected)

    def test_punctuation_stripping(self):
        """
        Crucial test: Ensure stopwords attached to punctuation are removed,
        but non-stopwords keep their punctuation.
        """
        # "og," should be removed. "mat." should stay.
        text = "ost, skinke, og, mat."
        expected = "ost, skinke, mat."
        self.assertEqual(remove_stopwords(text), expected)

    def test_norwegian_characters(self):
        """Test handling of Æ, Ø, Å."""
        text = "det er en blåbær på bordet"
        # 'det', 'er', 'en', 'på' are stopwords.
        expected = "blåbær bordet"
        self.assertEqual(remove_stopwords(text), expected)

    def test_quotes_and_brackets(self):
        """Test Norwegian guillemets (« ») and standard quotes."""
        text = "Han sa: «Det er viktig»."
        # 'Han' (stop), 'sa:' (keep), '«Det' (strip->Det->stop), 'er' (stop), 'sant».' (keep)
        # Note: logic removes the whole token if the stripped core is a stopword.
        expected = "sa: viktig»."
        self.assertEqual(remove_stopwords(text), expected)

    def test_inflections(self):
        """Test that inflected forms we added (hatt, gikk) are caught."""
        text = "vi har hatt en fin dag"
        # 'vi', 'har', 'hatt', 'en' should go.
        expected = "fin dag"
        self.assertEqual(remove_stopwords(text), expected)

    def test_empty_input(self):
        """Test edge cases with empty strings."""
        self.assertEqual(remove_stopwords(""), "")
        self.assertEqual(remove_stopwords(None), "")

    def test_only_stopwords(self):
        """Test a string that consists ONLY of stopwords."""
        text = "jeg er den som er i"
        self.assertEqual(remove_stopwords(text), "")


if __name__ == "__main__":
    unittest.main()
