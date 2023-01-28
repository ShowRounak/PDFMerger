import os
import logging
from main import pdf_merge


def pdf_exist():
    """ This function checks if PDF files are present in a directory"""
    try:
        logging.info("Taking all pdfs from the directory")
        pdfs = []
        for filename in os.listdir():
            if filename.endswith(".pdf"):
                pdfs.append(filename)
            else:
                None
        pdf_merge(pdfs)
        logging.info("Taking of pdfs is successful")
    except Exception as e:
        logging.exception("Exception occurred: ", str(e))


pdf_exist()
