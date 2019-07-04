import linecache

#def file_opener(file_address):
#	file = open(file_address, "r")
#    return file

#def file_closer(open_files):
#	open_files.close()

def textfile_wordfile_creator(file_name):
	# ファイルを開く
	file_data = open(file_name, "r")

	# ファイルの中身を複数の行に変換
	lines = file_data.readlines()

	# ファイル内の１行の要素数を取得
	elements = len(linecache.getline(file_name, 1).split(':'))

	# 収納するための配列
	array = [[0 for i in range(elements)] for j in range(sum(1 for line in open(file_name)))]

	count_indexs = 0

	for line in lines:
		row = line.split(':')
		for index, item in enumerate(row):
			array[count_indexs][index] = item

		count_indexs += 1

	file_data.close()
	return array
