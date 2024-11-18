import json
def task() -> float:
    filename = 'input.json'
    with open(filename) as file:
        data = json.load(file)
    a =[ i['score'] * i['weight'] for i in data]
    return round(sum(a), 3)
print(task())
