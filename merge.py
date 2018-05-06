import pandas as pandas

idlist = pd.read_excel("DataFile.xlsx", 'json_clean', index = False)
info = pd.read_excel("DataFile.xlsx", 'csv_clean', index = False)
all_data_st = pd.merge(idlist, info, how='left')
all_data_st.to_excel('DataFile.xlsx', sheet_name='processed', index = False)
print("Finished!")
