from tabula import read_pdf
df = read_pdf("invoice1.pdf", stream = True)
print(len(df))
print(df)