import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    filename = Path(filepath).stem
    invoice_nr = filename.split('-')[0]
    date = filename.split('-')[1]

    pdf = FPDF(orientation='P', unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")

    # Add invoice number
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", align="L", ln=1)

    # Add date
    pdf.cell(w=50, h=8, txt=f"Date: {date}", align="L", ln=1)

    # Add Headers
    columns = list(df.columns)
    columns = [items.replace('_', ' ').title() for items in columns]
    pdf.set_font(family="Times", size=10, style='B')
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=60, h=8, txt=columns[1], border=1)
    pdf.cell(w=32, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    # Add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=60, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=32, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)

    # Add sum of total prices
    total_sum = df["total_price"].sum()

    pdf.set_font(family="Times", size=10)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=60, h=8, txt='', border=1)
    pdf.cell(w=32, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # Add total sum sentence
    pdf.set_font(family="Times", size=10, style='B')
    pdf.cell(w=50, h=8, txt=f"The total price is {total_sum}", ln=1)

    # Add company name and logo
    pdf.set_font(family="Times", size=14, style='B')
    pdf.cell(w=30, h=8, txt=f"malik-python")
    pdf.image("malik-python.png", w=10)

    pdf.output(f"PDFs/{filename}.pdf")
