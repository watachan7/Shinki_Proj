# coding: utf-8
import mixa

print('Talk Start.')

while True:
	user_message = input('-> ')

	if ( user_message == 'exit' ):
		break

	result_message = mixa.say(user_message)
	print(result_message)

print('program ends.')
