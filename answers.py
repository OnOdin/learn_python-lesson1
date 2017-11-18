answers = {'привет':'уходи', 'здравствуйте':'Добрый день! Чем могу помочь?', 'йо': 'йо', 'yo':'yo!'}

def get_answer(question):
	return answers.get(question.lower())

inp = input('Напишите что-нибудь: ')

print(get_answer(inp))