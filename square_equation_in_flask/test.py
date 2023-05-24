import requests
from json import loads
from square_equation_in_flask.jsongenerator import JSONGenerator


def main():
    json_generator = JSONGenerator(count=5)
    json_test = loads(json_generator.generate_json())
    req = requests.post(url='http://127.0.0.1:5000/compute', json=json_test)
    print(f'Отправляем json формат:{json_test}')
    print(f'Результат в json:{req.json()}')
    with open('result_flask', 'w') as f:
        f.write(str(req.json()))


if __name__ == '__main__':
    main()
