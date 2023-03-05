import pdfplumber

with pdfplumber.open('report.pdf') as f:
    for i in f.pages:
        print(i.extract_tables())