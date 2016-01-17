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


def get_pattern(language):
    return {
        'pl': 'ur. ([0-9]{1,2}\D*[0-9]{4}.*?)(\) –|-)',
        'en': '\((.*;)?(.*?)\)',
    }.get(language, 'error')


def wiki_parser(text, language):
    pattern = get_pattern(language)
    if language == 'pl':
        return re.search(pattern, text).group(1).split(',')
    elif language == 'en':
        return re.search(pattern, text).group(2).split('–')


def wiki_helper(name):
    try:
        result = wikipedia.summary(name)
    except wikipedia.exceptions.DisambiguationError as e:
        sys.exit("Search Error!")
    return result

def wiki_search(name, language='pl'):
    wikipedia.set_lang(language)
    result = ''
    try:
        result = wikipedia.summary(name)
    except wikipedia.exceptions.DisambiguationError as e:
        print (e.options)
        for record in e.options:
            if name in record:
                print(record)
                result = wiki_helper(record)
                break
                # return wiki_parser(result, language)
        pass
        # sys.exit("Search Error!")
    return wiki_parser(result, language)


def wolfram_search(name):
    print('\n******* WolframAlpha Result *******\n')
    wolfram = AskWolfram(name)
    wolfram.start()


def main():
    language = 'pl'
    sentence = input('Hey, please ask me a question.\n')
    name = SentenceParser.parse(sentence)
    print('Ok, here is what i found for ' + name.strip() + '.\n')
    result = wiki_search(name,language)
    if language == 'en':
        if len(result) > 1:
            print('Born: ' + str(result[0]).strip())
            print('Death: ' + str(result[1]).strip())
        else:
            print('Born: ' + str(result[0]))
    else: #PL
        if len(result) > 1:
            print('Data Urodzenia: ' + str(result[0]).strip())
            print('Data Śmierci: ' + str(result[1])[4:].strip())
        else:
            print('Data Urodzenia: ' + str(result[0]))

    wolfram_search(name)


# start program
main()
