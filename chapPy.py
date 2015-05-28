# Based on Natural Language Toolkit: Eliza from NLTK Project
# by Steven Bird <stevenbird1@gmail.com>
# and Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# Author: Dheepan <idheepan@gmail.com>
# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <mailto:jez@jezuk.co.uk>.

# a translation table used to convert things you say into things the
# computer says back, e.g. "I am" --> "you are"

from __future__ import print_function
from chatbot import Chat, reflections

# a table of response pairs, where each pair consists of a
# regular expression, and a list of possible responses,
# with group-macros labelled as %1, %2. This the part that
# will make your bot intelligent or dumb

pairs = (
    (r'good morning', ("Hello", "Hi")),
    (r'import (.*) from (.*)',
     ("Why do you need %2?",
      "Would it really help you if i import %1?",
      "Are you sure you need %2?")),
    (r'(.*) is equal to(.*)',
     ("%1 eq %2"))
)

chatbot = Chat(pairs, reflections)


def chap_chat(text):
    return chatbot.converse(str=text)


def demo():
    greeting = "hello"
    chap_chat(greeting)


if __name__ == "__main__":
    demo()
