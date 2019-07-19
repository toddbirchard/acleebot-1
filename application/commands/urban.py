import requests


def urban_dictionary_defintion(word):
    params = {'term': word}
    req = requests.get('http://api.urbandictionary.com/v0/define', params=params)
    if len(req.json()['list']):
        definition = str(req.json()['list'][0]['definition'])
        example = str(req.json()['list'][0]['example'])
        word = req.json()['list'][0]['word'].upper()
        return f"{word}: {definition}. EXAMPLE: '{example}'"[0:500]
    else:
        return 'word not found :('
