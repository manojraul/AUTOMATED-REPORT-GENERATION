import csv
import numpy as np
from fpdf import FPDF

# Function to read data from a CSV file and return it as a list of rows
def read_data(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            # Only add the second column (Game Length) as a float for analysis
            data.append(float(row[1]))  # Game Length is in the second column
    return data

# Function to perform analysis (like calculating averages for numeric columns)
def analyze_data(data):
    # Calculate the average (mean) of the game lengths
    average_game_length = np.mean(data)
    return average_game_length

# Function to generate a PDF report
def generate_pdf_report(average_game_length, output_pdf_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Data Analysis Report", ln=True, align='C')

    # Line break
    pdf.ln(10)
    
    # Analysis Results
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Average Game Length: {average_game_length:.2f}", ln=True)

    # Save the PDF
    pdf.output(output_pdf_path)

# Main function
def main():
    input_file = r'C:\Users\dasta\Downloads\sample-csv-files-sample3.csv'  # Provide the correct file path here
    output_pdf = 'analysis_report.pdf'
    
    # Read data from CSV
    data = read_data(input_file)
    
    # Perform analysis
    average_game_length = analyze_data(data)
    
    # Generate and save PDF report
    generate_pdf_report(average_game_length, output_pdf)
    print(f"Report generated: {output_pdf}")

if __name__ == "__main__":
    main()
