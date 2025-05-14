
#!/usr/bin/env python3


class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            print("The value must be a string.")
            self.value = ''
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        import re
        sentences = re.split(r'[.!?]', self.value)
        filtered = [s.strip() for s in sentences if s.strip()]
        return len(filtered)


msg = MyString("Hello! How are you? I'm fine.")
print(msg.count_sentences())  # Output: 3
# Test cases
msg1 = MyString("Hello! How are you? I'm fine.")
msg2 = MyString("Hello! How are you? I'm fine.")
print(msg1.is_sentence())  # Output: False
print(msg2.is_question())  # Output: False
print(msg1.is_exclamation())  # Output: True    
# True
# True