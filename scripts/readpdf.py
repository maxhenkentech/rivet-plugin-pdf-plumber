import sys
import argparse
import os

# Adjust the Python path to include the local 'libs' folder
current_dir = os.path.dirname(os.path.realpath(__file__))
libs_dir = os.path.join(current_dir, 'libs')
sys.path.append(libs_dir)

# Now, import pdfplumber from the local directory
import pdfplumber

# Argument parser for command line arguments
parser = argparse.ArgumentParser(description='Extract text from a PDF file.')
parser.add_argument('pdf_path', type=str, help='The path to the PDF file')
args = parser.parse_args()

# Open the PDF file and extract text
with pdfplumber.open(args.pdf_path) as pdf:
    full_text = ''
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            full_text += text + '\n'

    # Print the extracted text
    print(full_text)
