#importing required modules
import pandas as pd
import pdfquery
import xml.etree.ElementTree as ET

#read the PDF
pdf = pdfquery.PDFQuery('horas.pdf')
pdf.load()


#convert the pdf to XML
pdf.tree.write('horas.xml', pretty_print = True)
pdf

#parsing the .xml file just created
tree = ET.parse('horas.xml')
root = tree.getroot()

#create a list to store all texts of the XML
texts = []
for box in root.iter('LTTextBoxHorizontal'):
    texts.append(box.text)
 

#Printing the results of the index after the TOTAL, which corresponds to the credit of debit hours from this month.
print(texts[texts.index('Total ')+1])