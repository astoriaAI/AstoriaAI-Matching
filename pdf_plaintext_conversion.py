# pip install pdfminer.six

from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def pdf_to_text(file_path):
    output_string = StringIO()
    with open(file_path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    return output_string.getvalue()


####### Trying to extract hyperlink from pdf #######
# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfpage import PDFTextExtractionNotAllowed
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.layout import LAParams
# from pdfminer.converter import PDFPageAggregator

# def new_pdf_to_text(file_path):
#     output_string = StringIO()
#     with open(file_path, 'rb') as in_file:
#         parser = PDFParser(in_file)
#         doc = PDFDocument(parser)
#         codec = 'utf-8'
#         rsrcmgr = PDFResourceManager()
#         device = TextConverter(rsrcmgr, output_string, codec=codec, laparams=LAParams())
#         interpreter = PDFPageInterpreter(rsrcmgr, device)
#         for page in PDFPage.create_pages(doc):
#             interpreter.process_page(page)
#     return output_string.getvalue()


# def new_pdf_to_text(file_path):
#     with open(file_path, 'rb') as in_file:
#         parser = PDFParser(in_file)
#         document = PDFDocument(parser)
#         if not document.is_extractable:
#             raise PDFTextExtractionNotAllowed
#         resource_manager = PDFResourceManager()
#         laparams = LAParams()
#         device = PDFPageAggregator(resource_manager, laparams=laparams)
#         interpreter = PDFPageInterpreter(resource_manager, device)
#         for page in PDFPage.create_pages(document):
#             interpreter.process_page(page)
#             layout = device.get_result()
#             for element in layout:
#                 temp = getOverlappingLink(annotationList(page), element)
#                 if temp:
#                     print(temp)
#     return



# def annotationList(page):
#     annotationList = []
#     if page.annots:
#         for annotation in page.annots.resolve():
#             annotationDict = annotation.resolve()
#             if str(annotationDict["Subtype"]) != "/Link":
#                 # Skip over any annotations that are not links
#                 continue
#             position = annotationDict["Rect"]
#             uriDict = annotationDict["A"].resolve()
#             # This has always been true so far.
#             assert str(uriDict["S"]) == "/URI"
#             # Some of my URI's have spaces.
#             uri = uriDict["URI"].replace(" ", "%20")
#             annotationList.append((position, uri))

# def getOverlappingLink(annotationList, element):
#     if annotationList:
#         for (x0, y0, x1, y1), url in annotationList:
#             if x0 > element.x1 or element.x0 > x1:
#                 continue
#             if y0 > element.y1 or element.y0 > y1:
#                 continue
#             return url
#         else:
#             return None