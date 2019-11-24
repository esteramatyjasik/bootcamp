
name = input('What is your name?: ')
length = len(name)

print(f'Hello {name} \U0001F642')
print(length)


expected = 'Jana III Sobieskiego'
text = 'UL. jana 3 \nSOBiesKIEGO'

text = text.title()
text = text.replace('\n', '')
text = text.replace('3', 'III')
text = text.replace('Ul.', '')
text = text.strip()

print(f'{text == expected}\t"{text}"')


