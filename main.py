import wikipedia
import re
import sys
from wolfram_client import AskWolfram

pattern_pl = "ur. (([0-9]{1,2}\D*[0-9]{4}.*?)(,.zm|\)))"
pattern_pl_2 = "ur. ([0-9]{1,2}\D*[0-9]{4}.*?)(\) –|-)"
name = input("Kiedy urodził się ")

# Let's try in polish, maybe famous?
print (wikipedia.languages()['pl'])
wikipedia.set_lang("pl")

# result_pl = wikipedia.summary(name)
# print(result_pl)
# print(result.group(1).strip())

result_pl = ""
result_en = ""
try:
    result_pl = wikipedia.summary(name)
except wikipedia.exceptions.DisambiguationError as e:
    try:
        # Let's try in eng
        wikipedia.set_lang("en")
        result_en = wikipedia.summary(name)
    except wikipedia.exceptions.DisambiguationError as ee:
        print (e.options)
        print(ee.options)
        sys.exit("Search Error!")
if result_pl != "":
    result = re.search(pattern_pl_2,result_pl)
    # print(result_pl)
    print(result.group(1))
elif result_en != "":
    result = re.search(pattern_pl,result_pl) #TODO Tu inny pattern
    print(result.group(1))

# print (wikipedia.summary(name))

re.search(pattern_pl,result_pl)
# print (wikipedia.search("Madonna (entertainer)"))

# Print wolfram
print('\n******* WolframAlpha Result *******\n')
wolfram = AskWolfram(name)
wolfram.start()