#coding: utf-8
import speech_recognition

print('Please input your message.\nIf you want to exit, please enter "exit".')

while True:
	user_message = input('>> ')

	# exitが入力された時、プログラム終了
	if ( user_message == "exit" ):
		break

	result_message = user_message
	print(result_message)

print("program ends.")
