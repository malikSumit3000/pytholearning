from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)

    y1 = 26

    # Document the page
    for i in range(35):
        y1 = y1 + 7
        pdf.line(10, y1, 200, y1)

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

    for page in range(row["Pages"] - 1):
        pdf.add_page()

        y1 = 26
        # Document the page
        for i in range(35):
            y1 = y1 + 7
            pdf.line(10, y1, 200, y1)

        # Set the footer
        pdf.ln(276)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=5, txt=row["Topic"], align="R", ln=1)

pdf.output("exercise_output.pdf")
