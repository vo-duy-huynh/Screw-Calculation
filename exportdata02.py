import pandas as pd
import json

excel_file = r'./TRIỂN KHAI CODE PHẦN MỀM v1.xlsx'

sheet_name = 'DATA 02' 

# Đọc từ dòng 3 (bỏ 2 dòng đầu), lấy cột từ B đến M (tức là 12 cột)
df = pd.read_excel(
    excel_file,
    sheet_name=sheet_name,
    skiprows=2,
    usecols='B:M',
    engine='openpyxl'
)

# Xem thử
print(df.head())

# Xuất ra JSON
df.to_json('data02.json', orient='records', force_ascii=False, indent=4)
print("Xuất file JSON thành công!")
