from PyPDF2 import PdfMerger
import logging
import os

logging.basicConfig(filename="log_pdf_merging.log", level=logging.DEBUG, format="%(asctime)s, %(levelname)s, "
                                                                                "%(message)s")


def pdf_merge(a):
    """ This function merge all PDFs into a single PDF file"""
    logging.info(f"This is the start of PDF merging, it is taking input {a}")
    try:
        merger = PdfMerger()
        for pdf in a:
            merger.append(pdf)
        merger.write("MergedPDF.pdf")
        merger.close()
        logging.info("Execution successful")
    except Exception as x:
        logging.error("Error occurred")
        logging.exception("Exception is: ", str(x))



