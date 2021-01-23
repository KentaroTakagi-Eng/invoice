from tabula import read_pdf
df = read_pdf("1_Error.pdf", stream = True)
print(len(df))
print(df)
    