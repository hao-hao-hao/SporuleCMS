import re


class Helper():
    @staticmethod
    def is_None(obj):
        return obj is None

    @staticmethod
    def slugify(strings, separator="-", to_lower=True):
        # use regex to replace all the special character to '-'
        strings = re.sub("[^a-zA-Z0-9\n\.]", separator, strings)
        strings = separator.join(filter(None, strings))
        if to_lower:
            strings = strings.lower()
        return strings
