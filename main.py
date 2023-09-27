import re
import pymorphy2
import nltk


class Belinskiy(object):
    def __init__(self, text):
        self.text = text
        self.tokens = self.to_tokens(self.text)
        self.sentences = self.to_sent(self.text)
        self.morph = pymorphy2.MorphAnalyzer()

    @staticmethod
    def to_tokens(text):
        return nltk.word_tokenize(text)

    @staticmethod
    def to_sent(text):
        return nltk.sent_tokenize(text)

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

        if 'plur' in form.tag and 'NOUN' in form.tag:
            return True
        else:
            return False

    def find_plural_nouns(self, tokens):
        plural_nouns = []
        for token in self.tokens:
            if self.is_plur_noun(token):
                plural_nouns.append(token)

        return plural_nouns