import ocrmypdf
import os
import re
from pdf_processing.paths import RAW_REPORTS_PATH, PDF_A_REPORTS_PATH

class PdfProcessor():
    def process_pdf(self, input_file: str, output_file: str) -> None:
        ocrmypdf.ocr(input_file=input_file, output_file=output_file)
    
    def process_sample_reports_raw(self):
        print("--- Running PdfProcessor on all raw sample reports ---")
        for file in os.listdir(RAW_REPORTS_PATH):
            if file.endswith(".pdf"):
                input_file = RAW_REPORTS_PATH + file
                output_file = re.sub(RAW_REPORTS_PATH, PDF_A_REPORTS_PATH, input_file)
                self.process_pdf(input_file, output_file)      
