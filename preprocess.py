import os
import PyPDF2
from pathlib import Path

def pdf_to_text(input_folder, output_folder):
    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_path = os.path.join(output_folder, txt_filename)

            # Open the PDF file
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ''

                # Extract text from each page
                for page in pdf_reader.pages:
                    text += page.extract_text()

            # Write the extracted text to a new text file
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)

            print(f"Converted {filename} to {txt_filename}")

def concatenate_txt_files(input_folder, output_file):
    # Ensure the output directory exists
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Iterate through all files in the input folder
        for filename in os.listdir(input_folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(input_folder, filename)
                
                # Write the filename as a header
                outfile.write(f"File: {filename}\n\n")
                
                # Read and write the contents of each file
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                
                # Add separator after each file
                outfile.write("\n\n---\n\n")
        
        print(f"All text files have been concatenated into {output_file}")

if __name__=='__main__':
    pdf_folder = 'hume_papers_pdf'
    txt_folder = 'hume_papers_txt'
    output_file = 'hume_papers_all.txt'
    # pdf_to_text(pdf_folder, txt_folder)
    concatenate_txt_files(txt_folder, output_file)