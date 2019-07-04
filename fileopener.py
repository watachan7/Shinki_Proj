#import module1
#import importlib
import linecache

# 対象ファイル
texts="texts/testidiom.txt"

# ファイルを開く
test_data = open(texts, "r")

# ファイルの中身を複数の行に変換
lines = test_data.readlines()

# ファイル内の１行の要素数を取得
elements = len(linecache.getline(texts, 1).split(':'))

# 収納するための配列
array = [[0 for i in range(elements)] for j in range(sum(1 for line in open(texts)))]

count_indexs = 0

for line in lines:
	row = line.split(':')
	for index, item in enumerate(row):
		array[count_indexs][index] = item

	count_indexs += 1

# 開いたファイルを閉じる
test_data.close()

