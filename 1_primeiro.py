import requests

endpoint = requests.get('https://aprendendoapi-2b6f3-default-rtdb.firebaseio.com/.json')
print(endpoint)
print(endpoint.json())

informacoes = '{"Nome": "Julia", "Sobrenome": "Laurindo", "Idade": "19"}'
endpoint = requests.post('https://aprendendoapi-2b6f3-default-rtdb.firebaseio.com/.json', data = informacoes)
print(endpoint)
print(endpoint.json())

informacoes = '{"Nome": "Julia", "Sobrenome": "Roberts", "Idade": "19"}'
endpoint = requests.patch('https://aprendendoapi-2b6f3-default-rtdb.firebaseio.com/-OUfISFNX0VDtyZ5O_k8/.json', data = informacoes)
print(endpoint)
print(endpoint.json())

endpoint = requests.delete('https://aprendendoapi-2b6f3-default-rtdb.firebaseio.com/-OUfISFNX0VDtyZ5O_k8/.json')
print(endpoint)