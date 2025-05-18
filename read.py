import pandas as pd
ID = int(input("ใส่รหัสนักเรียน:"))
filename = str(input("ใส่ชื่อไฟล์:"))
df = pd.read_csv(f"storecsv/{filename}.csv")
if filename:
    pass
else:
    print("ไม่พบไฟล์")
    exit()

if (df.iloc[0,:] == ID).any():
    print(df[df.iloc[:, 0] == ID])