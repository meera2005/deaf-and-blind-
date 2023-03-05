import camelot

from dictionary import *
from chat import opppen

# Open the PDF file
def file_read(filename):
    # pdf_file = "report.pdf"
# Create a PDF table object using Camelot
    tables = camelot.read_pdf(filename)
    print(tables)


    strings=[]
# Loop through each table and extract its contents

    for table in tables:
    # Extract the table as a DataFrame
       df = table.df
    
       str1=[]
       contents=''
       for index, row in df.iterrows():
       
          line_contents = ' '.join(row.astype(str))
          contents=contents+" "+line_contents+" "
          #print('hai')
          str1=line_contents.split(' ', 1)[0]
          print(line_contents)
          if 'Haemoglobin(HB)' in line_contents:
           #print('hai')
           
            str2=line_contents.split('\n')
            strings.append(str2[0]+':'+str2[1]+',')
          elif 'TC-Total WBC Count' in line_contents:
            str2=line_contents.split('\n')
            strings.append(str2[0]+':'+str2[1]+',')
          elif 'Sugar (Urine)' in line_contents:
           str2=line_contents.split(' ')
           strings.append(str2[0]+':'+str2[1]+',')
    return contents      
           
def main():
   strings=file_read()
   print(strings) 

   string2=opppen(strings)
   print(string2)             
               
if __name__ == "__main__":
    main()    
       
       
           

       
        #    flag1=1
        #    str="Haemoglobin(HB)"
           
           

#print(d)



           
           
       
           




       

