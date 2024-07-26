import pandas as pd
import numpy as np
import os

# Tentukan jumlah baris dan kolom
num_rows = 100
num_cols = 5

# Buat data dummy dengan nilai acak
data = np.random.randn(num_rows, num_cols)

# Buat DataFrame dengan data dummy
df = pd.DataFrame(data, columns=['Column_{}'.format(i+1) for i in range(num_cols)])

# Tampilkan beberapa baris pertama dari DataFrame
print(df.head())

# Simpan DataFrame ke dalam file CSV
file_name = 'data_dummy.csv'
df.to_csv(file_name, index=False)

# Dapatkan lokasi file CSV
file_location = os.path.join(os.getcwd(), file_name)
print(f'File CSV disimpan di: {file_location}')
