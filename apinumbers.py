import requests

url = 'http://numbersapi.com/{number}/{type}'
type = 'math'
params = {'json' : 'true'}

with open('set1.txt') as inf:
    for number in inf:
        number = number.rstrip()
        r = requests.get(url.format(number = number, type = type), params, timeout = 30)
        #print(r.status_code)
        data = r.json()
        if data['found']:
            print('Interesting')
        else:
            print('Boring')
