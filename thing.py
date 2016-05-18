# HOW TO USE:
# from thing import do_your_thing # import this function to your module
# xml = do_your_thing('input.txt', 'ru') # get xml result

def do_your_thing(input, language, approach='textrank', window=2):

    import argparse
    import requests

    # SPECIFY ENCODING ACCORDINGLY
    text = open(input, 'r').read()

    params = {}
    params['text'] = requests.utils.quote(text)
    params['language'] = requests.utils.quote(language)
    params['approach'] = 'textrank'
    params['window'] = str(window)

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/plain'
    }

    response = requests.post('http://tesuck.eveel.ru/extract.graphml', params, headers)
    data = response.text

    return data