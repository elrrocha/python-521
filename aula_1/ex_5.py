import requests

DOMAIN_URL = 'https://gen-net.herokuapp.com/api/users/{}'

response = requests.put(DOMAIN_URL)

user_id = input ('Digite seu id: ')
name = input('Digite seu nome: ')
email = input('Digite seu email: ')
password = ('Digite sua senha: ')


payload = {
	'name': name,
	'email': email,
	'password': password
}
response = requests.put(DOMAIN_URL.format(user_id), payload)

if response.status_code ==200:
	print('Usuário atualizado com sucesso')
else:
	print('Erro ao atualizar o usuário')