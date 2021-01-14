# importing required modules 
import PyPDF2 
  
# creating a pdf file object 
pdfFileObj = open('../doc/AmazonAtlas_v1.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print(pdfReader.numPages) 
  
# creat the addresss record file.
checkSumfh = open("address.txt", 'a')

# Split 
print("Get all server indicate ID:")
servKey = []
for i in range(3):
    pageObj = pdfReader.getPage(i)
    # extracting text from page 
    for line in pageObj.extractText().split('\n'):
        if line and (line[0] == 'o' or line[0] == '*'):
            data = line.split(' ')
            if str(data[2]).isupper():
                servKey.append(data[2])

addressList = []
addressStr = ''
serchIdx = 0
startFlg = False
for i in range(20):
    pageObj = pdfReader.getPage(i)
    for line in pageObj.extractText().split('\n'):
        checkSumfh.write(line+ "\n")
checkSumfh.close()

#print(servKey)
# closing the pdf file object 
pdfFileObj.close() 
exit()

for i in range(2, 20):
    pageObj = pdfReader.getPage(i)
    # extracting text from page 
    for line in pageObj.extractText().split('\n'):
        if line:
            data = line.split(' ')
            title = data[0]
            if title == servKey[serchIdx]:
                checkSumfh.write( title+ "\n")
                serchIdx += 1
                addressStr = ''
            elif title == "Contact:":
                addressStr = ''
                startFlg = True
            elif title == "Address:":
                addressStr = ''
                startFlg = True
                addressStr += line
            if startFlg:
                addressStr += line
        else:
            if addressStr:
                checkSumfh.write( addressStr+ "\n")
                addressStr = ''
                startFlg = False
                
