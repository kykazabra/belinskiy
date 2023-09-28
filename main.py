import re
import pymorphy2
import nltk


class Belinskiy(object):
    def __init__(self, text):
        self.text = text
        self.morph = pymorphy2.MorphAnalyzer()
        self.tokens = self.to_tokens(self.text)
        self.sentences = self.to_sent(self.text)
        self.words = self.parse_words(self.tokens)
        #nltk.download('words')
        self.body()

    @staticmethod
    def to_tokens(text):
        return nltk.word_tokenize(text)

    @staticmethod
    def to_sent(text):
        return nltk.sent_tokenize(text)

    @staticmethod
    def parse_words(tokens):
        words = []
        for token in tokens:
            if token not in string.punctuation:
                words.append(token)

        return words
    @staticmethod
    def find_abbr(text):
        abbr = r'([A-ZА-Я]{2,})'
        abbr_with_exp = r'([A-ZА-Я]{2,})[ -]\((.*)\)'
        return re.findall(abbr, text), re.findall(abbr_with_exp, text)

    @staticmethod
    def find_shorts(text):
        short = r'([а-я]+\.)'
        short_with_exp = r'([а-я]+\.)+[ -]\((.*)\)'

        return re.findall(short, text), re.findall(short_with_exp, text)

    def is_plur_noun(self, word):
        form = self.morph.parse(word)[0]

        return 'plur' in form.tag and 'NOUN' in form.tag

    def find_plural_nouns(self, tokens):
        plural_nouns = []
        for token in self.words:
            if self.is_plur_noun(token):
                plural_nouns.append(token)

        return plural_nouns

    @staticmethod
    def is_english(word):
        return word in nltk.corpus.words.words()

    def find_english(self, words):
        eng_words = []
        for word in words:
            if self.is_english(word):
                eng_words.append(word)

        return eng_words

    def has_simple_synonym(self, token):
        pass

    def find_digits(self, text):
        digit = r'\d+'

        return list(map(int, re.findall(digit, text)))
    def body(self):
        print(self.find_digits(self.text))