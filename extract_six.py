from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from io import StringIO
import sys, io
import codecs

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)

    fp = open(path, 'rb')

    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()



    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        # 使用页面解释器来读取
        interpreter.process_page(page)

        # # 使用聚合器获取内容
    text = retstr.getvalue()


    # text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    with codecs.open('./book.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    f.close()

# path_of_the_pdf_file = r'./PRACTICAL_LINUX_SECURITY_COOKBOOK.pdf'

# convert_pdf_to_txt(path_of_the_pdf_file)
