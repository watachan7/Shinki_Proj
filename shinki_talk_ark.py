
shinki_name_data = open('Shinki/shinki_list.txt', 'r')

print('Please choose youre shinki.')

while True:
	request_shinki_name = input('-> ')

	# exitが入力された時、プログラム終了
	if ( request_shinki_name == 'exit' ):
		break

	lines = shinki_name_data.readlines()

	for line in lines:
		print(line)
		if line != request_shinki_name:
			print('There is no such shinki name.')

	result_message = request_shinki_name
	print(result_message)

print('program ends.')
shinki_name_data.close()
