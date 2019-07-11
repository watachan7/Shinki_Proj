import zipfile

zip = zipfile.ZipFile('C:\\pg\\zip.zip')

# ZIPを解凍
zip.extractall('C:\\pg\\data')

# ZIPファイルをクローズ
zip.close()