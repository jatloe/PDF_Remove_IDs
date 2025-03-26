import pymupdf

# Open the pdf
doc = pymupdf.open('./USAMO_Scan_With_IDs.pdf')
for page in doc:
    # For every page, draw a rectangle on coordinates (1,1)(100,100)
    page.draw_rect([1,1,150,40],  color = (0, 0, 0), width = 40)

lengths = [2,4,2,2,4,5]

doc.delete_pages([sum(lengths[:i])+i for i in range(6)])

# Save pdf
# doc.save('./Without_IDs.pdf')

resolution_parameter = 300
for ind,page in enumerate(doc):  # iterate through the pages
    pix = page.get_pixmap(dpi = resolution_parameter)  # render page to an image
    pix.save("pages/page-%i.png" % page.number)  # store image as a PNG

    print(f"Processed page {ind}")

import os
import PySimpleGUI as psg  # for showing a progress bar
doc = pymupdf.open()  # PDF with the pictures
imgdir = "pages"  # where the pics are
imglist = os.listdir(imgdir)  # list of them
imgcount = len(imglist)  # pic count

for i, f in enumerate(imglist):
    img = pymupdf.open(os.path.join(imgdir, f))  # open pic as document
    rect = img[0].rect  # pic dimension
    pdfbytes = img.convert_to_pdf()  # make a PDF stream
    img.close()  # no longer needed
    imgPDF = pymupdf.open("pdf", pdfbytes)  # open stream as PDF
    page = doc.new_page(width = rect.width,  # new page with ...
                       height = rect.height)  # pic dimension
    page.show_pdf_page(rect, imgPDF, 0)  # image fills the page
    # psg.EasyProgressMeter("Import Images",  # show our progress
        # i+1, imgcount)

doc.save("USAMO_Scan_Without_IDs.pdf")