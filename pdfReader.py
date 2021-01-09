#! python3
# Convert from PDF to csv
# 一括でFileを変更させる方法を模索中

import tabula
tabula.convert_into("FolderName1.pdf","FolderName1.csv",lattice=True,output_format="csv",pages='all')
tabula.convert_into("FolderName2.pdf","FolderName2.csv",lattice=True,output_format="csv",pages='all')
tabula.convert_into("FolderName3.pdf","FolderName3.csv",lattice=True,output_format="csv",pages='all')
tabula.convert_into("FolderName4.pdf","FolderName4.csv",lattice=True,output_format="csv",pages='all')

# import glob
# invoice = glob.glob('invoice/*.pdf')