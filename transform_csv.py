import pandas as pd

# Converts data from idlist.csv to excel sheet in DataFile.xlsx
def csv_to_xlsx_pd():
	# Read and write the data to xlsx file
    csv = pd.read_csv('idlist.csv', encoding='utf-8')
    csv.to_excel('DataFile.xlsx', sheet_name='data', index = False)
    print("Finished!")

if __name__ == '__main__':
    csv_to_xlsx_pd()