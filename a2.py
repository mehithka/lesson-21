country_code = {'India' : '0091',
                'Australia':'0025',
                'Nepal':'00977'}
print(country_code)

print('country code for india: ')
print(country_code.get('India','Not Found'))

print('Country code for japan - ')
print(country_code.get('Japan', 'Not Found'))