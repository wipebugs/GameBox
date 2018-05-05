import pandas as pd

# Converts json data from steamspy.json to excel sheet in DataFile.xlsx
def json_to_xlsx_pd():
	# Read and write the data to xlsx file
    json_data = pd.read_json('steamspy.json', encoding='utf-8').transpose()
    json_data.to_excel('DataFile.xlsx', sheet_name='json_data')
    print("Finished!")

if __name__ == '__main__':
    json_to_xlsx_pd()