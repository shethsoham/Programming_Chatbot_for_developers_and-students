# Natural Language Toolkit: Chatbot Utilities
#
# Copyright (C) 2001-2023 NLTK Project
# Authors: Steven Bird <stevenbird1@gmail.com>
# URL: <https://www.nltk.org/>
# For license information, see LICENSE.TXT

# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <jez@jezuk.co.uk>.

# Customizations done to library
# 1. Updated respond method
# 2. Added generateGeneralResponse method
# 3. Added translateTarget method
# 4. Added getGroupRegex method

'''
Team Contributions:
                    Bester: Worked on Chat.py
                    Ethan: Worked on main.py
                    Soham: Worked on  Pairs.py
                    Akshay: Worked on Pairs.py
'''

# import tensorflow
# from transformers import pipeline
import random
import re
from Pairs import intents

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}

class Chat:
    def __init__(self, reflections={}):
        """
        Initialize the chatbot.  Pairs is a list of patterns and responses.  Each
        pattern is a regular expression matching the user's statement or question,
        e.g. r'I like (.*)'.  For each such pattern a list of possible responses
        is given, e.g. ['Why do you like %1', 'Did you ever dislike %1'].  Material
        which is matched by parenthesized sections of the patterns (e.g. .*) is mapped to
        the numbered positions in the responses, e.g. %1.

        :type pairs: list of tuple
        :param pairs: The patterns and responses
        :type reflections: dict
        :param reflections: A mapping between first and second person expressions
        :rtype: None
        """

        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in intents["generalConversation"]["rules"]]
        self._generalPairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in intents["generalConversation"]["rules"]]
        self._reflections = reflections
        self._regex = self._compile_reflections()


    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections, key=len, reverse=True)
        return re.compile(
            r"\b({})\b".format("|".join(map(re.escape, sorted_refl))), re.IGNORECASE
        )

    def _substitute(self, str):
        """
        Substitute words in the string, according to the specified reflections,
        e.g. "I'm" -> "you are"

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        return self._regex.sub(
            lambda mo: self._reflections[mo.string[mo.start() : mo.end()]], str.lower()
        )

    def _wildcards(self, response, match):
        pos = response.find("%")
        while pos >= 0:
            num = int(response[pos + 1 : pos + 2])
            response = (
                response[:pos]
                + self._substitute(match.group(num))
                + response[pos + 2 :]
            )
            pos = response.find("%")
        return response

    def respond(self,obj, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """
        objmet = False
        objRegex = intents[obj]["targetRegex"]
        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in intents[obj]["rules"]]
        resp = ""
        for (pattern, response) in self._pairs:
            match = pattern.match(str)
            targetMatch = re.compile(objRegex, re.IGNORECASE).match(str)
            targetVal = ""
            # did the pattern match?  4827382
            if match:
                resp = random.choice(response)  # pick a random response
                resp = self._wildcards(resp, match)  # process wildcards

                # did the target match?
                if targetMatch:
                    targetVal = self.getGroupRegex(objRegex, str, intents[obj]["targetGroup"])
                    objmet = True
                    break

        if resp == "":
            resp = self.getGeneralResponse(str)


        return resp, objmet, targetVal

    def getGeneralResponse(self, text):
        for (pattern, response) in self._generalPairs:
            match = pattern.match(text)
            # did the pattern match?
            if match:
                resp = random.choice(response)  # pick a random response
                resp = self._wildcards(resp, match)  # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == "?.":
                    resp = resp[:-2] + "."
                if resp[-2:] == "??":
                    resp = resp[:-2] + "?"
                break

        return resp

    # Hold a conversation with a chatbot

    def converse(self, quit="quit"):
        user_input = ""
        while user_input != quit:
            user_input = quit
            try:
                user_input = input(">")
            except EOFError:
                print(user_input)
            if user_input:
                while user_input[-1] in "!.":
                    user_input = user_input[:-1]

                    print(self.respond(user_input))

    def getGroupRegex(self, regex, text, group):
        synaxErrorRegex = re.compile(regex, re.IGNORECASE)
        if synaxErrorRegex.match(text):
            result = re.search(regex, text, re.IGNORECASE)
            return result.group(group).lower()
        else:
            return ""

    def translateTarget(self, str, obj):
        for (pattern, result) in intents[obj]["targetTranslator"]:
            match = re.compile(pattern, re.IGNORECASE).match(str)
            if match:
                return result

        return ""