# coding: utf-8
import ark_brain

print('Talk Start.')

while True:
	user_message = input('-> ')

	if ( user_message == 'exit' ):
		break

	result_message = ark_brain.main(user_message)
	print(result_message)

print('program ends.')
