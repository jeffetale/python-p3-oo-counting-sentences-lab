#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        count = 0
        in_sentence = False
        for char in self.value:
            if char in '.?!':
                if in_sentence:
                    count += 1
                    in_sentence = False
            else:
                in_sentence = True
        return count

