#! python3
# Rename.py
# Rename the filenames in order 
import camelot
tables = camelot.read_pdf('1.pdf', flavor="stream", pages=all)
--------------
<TableList n=2>
tables[1] #indexing starts from 0
<Table shape=(28, 4)>
tables[1].parsing_report
{'accuracy': 100.0, 'whitespace': 44.64, 'order': 2, 'page': 1}
tables[1].df.head()
tables.export('table.csv')