import os
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Extracts and cleans text from a PDF file.
    
    Args:
        pdf_path (str): The file path to the PDF.
        
    Returns:
        str: The full extracted text, or None if an error occurs.
    """
    try:
        reader = PdfReader(pdf_path)
        full_text = ""
        
        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
                
        # Basic cleaning: remove excessive newlines and whitespace
        cleaned_text = " ".join(full_text.split())
        return cleaned_text
    
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

# --- TEST BLOCK ---
# This block only runs if you execute this file directly (not when imported)
if __name__ == "__main__":
    # Define the path to your resumes
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    resume_dir = os.path.join(base_path, "data", "resumes")
    
    print(f"Scanning directory: {resume_dir}...\n")

    # Loop through the directory and test the function
    try:
        files = os.listdir(resume_dir)
        for filename in files:
            if filename.endswith(".pdf"):
                path = os.path.join(resume_dir, filename)
                print(f"--- Parsing: {filename} ---")
                content = extract_text_from_pdf(path)
                
                # Print the first 200 characters to verify it works
                print(f"Preview: {content[:200]}...\n")
    except FileNotFoundError:
        print("Error: Directory not found. Did you create the 'data/resumes' folder?")