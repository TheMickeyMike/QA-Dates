import wolframalpha


class AskWolfram():

    __person = ""
    __app_id = 'TAHKHP-UR2RGWHQV9'


    def __init__(self,name):
        self.__person = name

    def start(self):
        client = wolframalpha.Client(self.__app_id)
        res = client.query(self.__person)

        assert len(res.pods) > 0
        results = list(res.results)
        for pod in res.pods:
            if pod.title == 'Basic information':
                groups = [s.strip() for s in pod.text.splitlines()]
                for x in groups:
                    if 'date of birth' in x:
                        print("Data urodzenia:" + str(x.split('|')[1]))
                    elif 'place of birth' in x:
                        print("Miejsce urodzenia:" + str(x.split('|')[1]))
                    elif 'date of death' in x:
                        print("Data śmierci:" + str(x.split('|')[1]))
                    elif 'place of death' in x:
                        print("Miejsce śmierci:" + str(x.split('|')[1]))

            elif pod.title == 'Input interpretation':
                print("Osoba:" + pod.text)

#     print(groups)
#  print(str(pod.title) + "  " + str(pod.text))
# print(next(res.results).text)
