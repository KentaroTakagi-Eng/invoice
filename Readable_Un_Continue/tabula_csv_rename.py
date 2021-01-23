#! python3
# Rename.py
# Rename the filenames in order 
'''発生した問題：
os.path.dirname(__file__) がフォルダ名を認識しない
'''

import os
import glob
import tabula # Tabula

# folder name
folder_name = os.path.dirname(__file__)
'''__file__  実行中のファイルを指示'''
'''os.pass.dirname  実行中の相対パスを取得'''
'''os.path.join(A,B) AとBとをつなげる ---　今回は使っていない'''

# Search pdf/csv file
pdf_file = "*.pdf"
csv_file = "*.csv"

file_list = glob.glob(pdf_file)
print("Current File Name")
print(file_list)
'''glob.glob(AA) --- CWDにある検索条件AAのファイルをリスト化'''

i = 1
for file in file_list:
    os.renames(file, folder_name + str(i) + ".pdf" )
    i += 1
''''os.rename(file,B) --- file名をBに変更する'''

j = 1
renamed_file_list = glob.glob(pdf_file)
for x in renamed_file_list:
    tabula.convert_into(x, folder_name + str(j) + ".csv", lattice=True, output_format = "csv", pages = 'all')
    j += 1

renamed_file_list = glob.glob(pdf_file)
convert_file_list = glob.glob(csv_file)
print("Renamed and Convert Files")
print(renamed_file_list)
print(convert_file_list)
