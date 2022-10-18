"""Для отклика на эту вакансию необходимо ответить на несколько вопросов работодателя.
Вопросы взяты из каждодневной практики, по ним вы можете оценить рабочие задачи. Ожидается, что вы вложите
разумные усилия в их выполнение.

Нашей компании нужно сгруппировать клиентов для АБ-тестов. Алгоритм группировки очень простой - взять id_c клиента
(состоит из 5-7 цифр, например 7412567) и найти сумму всех его цифр. Получившееся число и является номером группы,
в которую входит данный клиент. Для того, чтобы понять, насколько хорош такой простой алгоритм, тебе нужно написать
следующие диагностические функции:

1) Функция, которая подсчитывает число покупателей, попадающих в каждую группу, если нумерация id_c сквозная и начинается с 0.
На вход функция получает целое число n_customers (количество клиентов).

2)Функция, аналогичная первой, если id_c начинается с произвольного числа.
На вход функция получает целые числа: n_customers (количество клиентов) и n_first_id_c
(первый id_c в последовательности).

Напишите код функций на Python и оформите его в репозиторий Github. В форму ответа вставьте ссылку на репозиторий,
убедитесь, что он публичный.

Дополнительно к работоспособности оценим: читабельность и аккуратность кода;производительность кода."""


class Clients:
	__CLIENTS_GROUP = {}

	@classmethod
	def __group_clients(cls, id_c):
		"""The method sorts the client into groups according to its ID"""
		nomber_of_group = sum([int(n) for n in str(id_c)])

		if nomber_of_group not in cls.__CLIENTS_GROUP:
			cls.__CLIENTS_GROUP.setdefault(nomber_of_group, [])

		cls.__CLIENTS_GROUP[nomber_of_group].append(id_c)

	@classmethod
	def count_customers(cls, n_customers, n_first_id_c=0):
		"""The method counts customers in groups"""
		if n_first_id_c < n_customers:
			[cls.__group_clients(id_c) for id_c in range(n_first_id_c, n_customers + 1)]

			return map(lambda key: f'\nВ группе №{key} клиентов: {len(cls.__CLIENTS_GROUP[key])}', cls.__CLIENTS_GROUP)
			# print(*(map(lambda key: f'\nВ группе №{key} клиентов: {len(cls.__CLIENTS_GROUP[key])}', cls.__CLIENTS_GROUP)))


d = Clients()
d.count_customers(500, 450)
