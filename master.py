import os, csv

def make_csv_file_list():
	csv_files = []
	for file in os.listdir():
		if file.endswith('.csv'):# ignore non csv files
			csv_files.append(file)
	csv_files.sort()
	return csv_files

def make_csv_rows(lst):
	csv_rows = []
	for file in lst:
		 open_file = open(file)
		 file_reader = csv.reader(open_file)
		 for row in file_reader:
		 	if file_reader.line_num == 1: #removing header
		 		if file != lst[0]:# keeping header of first file
		 			continue
		 	csv_rows.append(row)
	return csv_rows
def make_master_workbook(lst):
	masterCSV = open('master_workbook.csv','w', newline = '')
	file_writer = csv.writer(masterCSV)
	for line in lst:
		file_writer.writerow(line)

fileList = make_csv_file_list()
print('step 1 done')
csv_row_list = make_csv_rows(fileList)
print('step 2 done')

delete = input('want to keep previos files(Y/N):')
if delete.lower() == 'n':
	for file in fileList:
		os.remove(file)

masterCSVfile = make_master_workbook(csv_row_list)
print("done")
