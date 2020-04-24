import pytesseract as pt
from PIL import Image
import PyPDF2 as pp

img_text = (pt.image_to_string(Image.open('testfiles/img/test0.png')))
pdf_text = (pp.PdfFileReader('testfiles/pdf/test0.pdf').getPage(0).extractText())