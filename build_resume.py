# -*- coding: utf-8 -*-
"""
Build an ATS-optimized, single-column PDF resume for Sumit Kumar Prajapat.
Content sourced from the portfolio website (index.html).

ATS-safe choices:
  - Single column, linear top-to-bottom reading order (no tables/text-boxes/columns)
  - Standard font (Helvetica), selectable/extractable text
  - Standard section headings (Summary, Skills, Experience, Projects, etc.)
  - No images, icons, headers/footers, or graphics
  - Plain-text contact line and URLs
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
import os

INK = HexColor("#111111")
GREY = HexColor("#333333")
LINE = HexColor("#888888")

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "resume", "Sumit_Prajapat_Resume.pdf")


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---- styles ----
name_style = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=20,
                            leading=23, textColor=INK, spaceAfter=2)
title_style = ParagraphStyle("title", fontName="Helvetica", fontSize=11.5,
                             leading=14, textColor=GREY, spaceAfter=4)
contact_style = ParagraphStyle("contact", fontName="Helvetica", fontSize=9.5,
                               leading=13, textColor=GREY, spaceAfter=2)
section_style = ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=11,
                               leading=13, textColor=INK, spaceBefore=11,
                               spaceAfter=3)
body_style = ParagraphStyle("body", fontName="Helvetica", fontSize=9.7,
                            leading=13.5, textColor=INK, alignment=TA_LEFT,
                            spaceAfter=2)
role_style = ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=10,
                            leading=13, textColor=INK, spaceBefore=5, spaceAfter=0)
meta_style = ParagraphStyle("meta", fontName="Helvetica-Oblique", fontSize=9,
                            leading=12, textColor=GREY, spaceAfter=2)
bullet_style = ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.7,
                              leading=13.2, textColor=INK, leftIndent=12,
                              bulletIndent=2, spaceAfter=1)


def section(title):
    flow.append(Paragraph(esc(title), section_style))
    flow.append(HRFlowable(width="100%", thickness=0.6, color=LINE,
                           spaceBefore=1, spaceAfter=4))


def bullet(text):
    flow.append(Paragraph(esc(text), bullet_style, bulletText=u"•"))


flow = []

# ---- header ----
flow.append(Paragraph("Sumit Prajapat", name_style))
flow.append(Paragraph("Data Analyst &amp; BI Developer", title_style))
flow.append(Paragraph(
    "Rajasthan, India (Remote-friendly) &nbsp;|&nbsp; "
    "sumitkprajapat29@gmail.com &nbsp;|&nbsp; "
    "github.com/Skpkush &nbsp;|&nbsp; "
    "linkedin.com/in/sumit-k-prajapat",
    contact_style))
flow.append(HRFlowable(width="100%", thickness=1, color=INK,
                       spaceBefore=6, spaceAfter=2))

# ---- summary ----
section("PROFESSIONAL SUMMARY")
flow.append(Paragraph(
    "Data Analyst and BI Developer with around two years of BFSI (insurance "
    "and financial services) domain experience, building end-to-end analytics "
    "from raw data to business decisions. I ship complete pipelines: extract "
    "with Azure Data Factory, model in PostgreSQL, analyze in Python, and "
    "deliver in Power BI. Certified across the Microsoft data stack and AWS "
    "(5x certified), with hands-on work in data modeling, DAX, ETL, machine "
    "learning, and workflow automation. Seeking a full-time Data Analyst / BI "
    "Developer role to own reporting end to end.", body_style))

# ---- skills ----
section("TECHNICAL SKILLS")
skills = [
    ("Analytics &amp; BI", "Power BI, DAX, Power Query, Data Modeling, Data Visualization, Excel"),
    ("SQL &amp; ETL", "SQL, PostgreSQL, Azure Data Factory, ETL Pipelines, Data Warehousing"),
    ("Programming", "Python, Pandas, NumPy, scikit-learn, Streamlit"),
    ("Cloud", "Microsoft Azure, AWS"),
    ("Machine Learning", "Forecasting (Prophet), Classification, Clustering (KMeans), RFM Analysis"),
    ("Automation", "n8n, Workflow Automation, API Integrations"),
]
for k, v in skills:
    flow.append(Paragraph("<b>%s:</b> %s" % (k, v), body_style))

# ---- experience ----
section("PROFESSIONAL EXPERIENCE")

flow.append(Paragraph("Business Data Analyst &mdash; Financial Services", role_style))
flow.append(Paragraph("[Start Date] &ndash; Present &nbsp;|&nbsp; Remote, India", meta_style))
bullet("Build and maintain dashboards, data models, and reporting that run day-to-day operations for a financial-services business.")
bullet("Develop n8n workflow automations and API integrations to streamline manual reporting and data-collection tasks.")
bullet("Translate raw operational data into decision-ready insights for business stakeholders.")

flow.append(Paragraph("Python &amp; Computer Science Instructor / School Administrator", role_style))
flow.append(Paragraph("[Start Date] &ndash; [End Date]", meta_style))
bullet("Taught Python programming and computer science fundamentals to students.")
bullet("Ran day-to-day school operations and administration end to end.")

flow.append(Paragraph("Marketing Executive &mdash; Shriram General Insurance", role_style))
flow.append(Paragraph("[Start Date] &ndash; [End Date]", meta_style))
bullet("Worked at ground level across insurance products, customers, and claims, building the BFSI domain knowledge I now analyze.")
bullet("Supported customer acquisition and product communication for general insurance offerings.")

# ---- projects ----
section("KEY PROJECTS")

flow.append(Paragraph("Healthcare Provider Fraud Detection", role_style))
flow.append(Paragraph("Python, scikit-learn, Azure Data Factory, PostgreSQL, Power BI", meta_style))
bullet("Built fraud analytics across 558K+ Medicare claims with an Azure Data Factory pipeline loading into PostgreSQL.")
bullet("Developed a scikit-learn fraud-detection model and a Power BI dashboard for investigating flagged providers.")
bullet("github.com/Skpkush/Healthcare-Insurance-Claims-Analytics")

flow.append(Paragraph("Mutual Fund Analytics Platform", role_style))
flow.append(Paragraph("Python, Streamlit, Prophet, Azure, PostgreSQL, Power BI", meta_style))
bullet("Built a live analytics platform on Yahoo Finance and AMFI data with automated ETL.")
bullet("Implemented Prophet-based return forecasting plus fund performance and risk dashboards; deployed as a Streamlit web app.")
bullet("github.com/Skpkush/mf-analytics-platform")

flow.append(Paragraph("Olist E-Commerce Analytics", role_style))
flow.append(Paragraph("SQL, PostgreSQL, Azure, Power BI, DAX", meta_style))
bullet("Designed a star-schema warehouse (4 dimensions + 1 fact table, 112,650 rows) fed by Azure Blob to ADF to PostgreSQL.")
bullet("Delivered a Power BI report with 40+ DAX measures, AI visuals, and what-if pricing simulation.")
bullet("github.com/Skpkush/Olist-E-Commerce-Analytics-Dashboard")

flow.append(Paragraph("Customer Segmentation", role_style))
flow.append(Paragraph("Python, KMeans, RFM, Streamlit", meta_style))
bullet("Built RFM scoring and KMeans clustering on transaction data to identify and target customer segments.")
bullet("Shipped as an interactive Streamlit app for exploring segments.")
bullet("github.com/Skpkush/Customer-Segmentation")

# ---- certifications ----
section("CERTIFICATIONS")
for c in [
    "Microsoft Certified: Power BI Data Analyst Associate (PL-300)",
    "Microsoft Certified: Azure Fundamentals (AZ-900)",
    "Microsoft Certified: Azure Data Fundamentals (DP-900)",
    "AWS Certified Cloud Practitioner (CLF-C02)",
    "CFA Institute - Investment Foundations",
]:
    bullet(c)

# ---- education ----
section("EDUCATION")
flow.append(Paragraph("Bachelor of Commerce (B.Com)", role_style))
flow.append(Paragraph("University of Calcutta", meta_style))

# ---- build ----
os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc = SimpleDocTemplate(
    OUT, pagesize=letter,
    leftMargin=0.7 * inch, rightMargin=0.7 * inch,
    topMargin=0.6 * inch, bottomMargin=0.6 * inch,
    title="Sumit Prajapat - Resume",
    author="Sumit Prajapat",
    subject="Data Analyst & BI Developer Resume",
)
doc.build(flow)
print("OK ->", OUT)
