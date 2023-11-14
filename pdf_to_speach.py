import pyttsx3,PyPDF2,PyPDF4
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
info = pdfreader.getDocumentInfo()
speaker = pyttsx3.init()

for page_num in range (pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_Text = text.strip().replace('\n',' ')
    print(clean_Text)
speaker.save_to_file(clean_Text,'voice.mp3')
speaker.runAndWait()
print(pdfreader.documentInfo)

speaker.stop()