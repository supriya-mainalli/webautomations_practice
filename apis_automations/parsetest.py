import json

courses = '{"language" :["java", "Python"]}'
print(type(courses))
data = json.loads(courses)
print(data['language'][1])

with open('demo1.json') as file:
    data = json.load(file)
    print(data)
    for item in data:
        if item['last_name'] == 'Bea':
            print(item['last_name'])
            break