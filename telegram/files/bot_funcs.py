import random

def smoking_test_result(age, sex):
	if sex == 'My gender is female' and '<' in age:
		result = 'Don\'t even think about cigarets'
	elif sex == 'My gender is female' and '>' in age:
		result = 'I don\'t fucking know, maby 1 cigaret per second'
	elif sex == 'My gender is male' and '<' in age:
		result = 'You\'d better ask your biology teacher'       
	else:
		result = 'You should try cocaine'
	return result

def stupid_questions_reply(text):
	
	feeling_answers = [
		'I am ok', 
		'Not ok', 
		'мальчик', 
		['And you?', 'Joke! I don\'t give a fuck about you'],
		'Flor gang'
	]

	if text == 'How are you?': 
		message = random.choice(feeling_answers)
	elif text == 'Кто такой Влад Стефанович?':
		message = [
			'Влад?',
			'Он... он просто',
			'как обЪяснить...?',
			'Честно',
			'Я и сам до конца не знаю',
			'Он либо Бог',
			'Либо дурак',
			'Истинный ответ знает только он сам',
			'Для других он хороший друг',
			'Я знаю что он умный',
			'И сильный',
			'И хороший',
			'И что он никогда никого не обидит',
			'Наверно...'
		]
	elif text == 'Кто такой Иван Пигуль?':
		message = [
			'Его характеристики:',
			'Хуй 2 метра',
			'100 кг веса',
			'3 метра роста',
			'Стон исланд на левой руке',
			'Боевая машина',
			'Боевой вертолет',
			'Шїри украинец',
			'Сын маминой подруги',
			'Православный славянин',
			'Машинист экскаватора',
			'Справжня людына',
			'Чоловїк',
			'Герой АТО',
			'Герой Майдана 2013-2014',
			'Член политической партии Эврлпейскї майбутнї',
			'Машина',
			'Просто машина ебать',
		]
	elif text == 'Кто такой Кирилл Журов?':
		message = [
			'Рама',
			'Керил',
			'Программист-ананист',
			'Самый искренний человек на свете',
			'180/63'
		]
	else:
		message = 'I don\'t fucking know'
	return message