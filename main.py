import re
import sys
import nltk
import wikipedia
from wolfram_client import AskWolfram


class SentenceParser():
    def parse(sentence):
        name = ''
        entities = nltk.chunk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence)))
        for st in entities.subtrees(filter=lambda x: x.label() == "PERSON"):
            for leave in st.leaves():
                name = name + leave[0] + ' '
        return name


def wiki_parser(text):
    # Patterns
    # pattern_pl = "ur. (([0-9]{1,2}\D*[0-9]{4}.*?)(,.zm|\)))"
    pattern_pl = "ur. ([0-9]{1,2}\D*[0-9]{4}.*?)(\) –|-)"
    return re.search(pattern_pl, text).group(1)

def wiki_search(name):
    wikipedia.set_lang("pl")
    result_pl = ''
    try:
        result_pl = wikipedia.summary(name)
    except wikipedia.exceptions.DisambiguationError as e:
        sys.exit("Search Error!")
    return wiki_parser(result_pl)

def wolfram_search(name):
    print('\n******* WolframAlpha Result *******\n')
    wolfram = AskWolfram(name)
    wolfram.start()

def main():
    sentence = input('Hey, please ask me a question.\n')
    name = SentenceParser.parse(sentence)
    print('Ok, this is what i found.\n' + wiki_search(name))
    wolfram_search(name)


# start program
main()




