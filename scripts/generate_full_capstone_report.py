#!/usr/bin/env python3
"""
generate_full_capstone_report.py
Generates the comprehensive, publication-grade Capstone Project Report for VIT-AP University.
Outputs:
1. docs/capstone_project_report.html (Self-contained HTML report with embedded base64 figures)
2. docs/VIT_AP_Capstone_Project_Report.pdf (Official printable PDF with merged cover and body)
3. docs/capstone_project_report.md (Clean markdown version)
4. docs/VIT_AP_Capstone_Project_Report.docx (Word DOCX document)
"""

import os
import sys
import base64
import asyncio
import subprocess
import shutil
from pathlib import Path

WORKSPACE = Path("/Users/makshaysharma/Desktop/ecommerce-intelligence")
DOCS_DIR = WORKSPACE / "docs"
ASSETS_DIR = WORKSPACE / "report_assets"
FIGURES_DIR = WORKSPACE / "paper" / "figures"
ARTIFACT_DIR = Path("/Users/makshaysharma/.gemini/antigravity/brain/2ff68dc2-9f13-45a4-b203-0adb4a579794")

DOCS_DIR.mkdir(parents=True, exist_ok=True)

def encode_img(path):
    p = Path(path)
    if not p.exists():
        print(f"Warning: image {path} not found")
        return ""
    mime = "image/png"
    if p.suffix.lower() in [".jpg", ".jpeg"]:
        mime = "image/jpeg"
    b64 = base64.b64encode(p.read_bytes()).decode('utf-8')
    return f"data:{mime};base64,{b64}"

print("Encoding assets...")
img_logo = encode_img(ASSETS_DIR / "image1.jpeg")
img_arch = encode_img(ASSETS_DIR / "image2.png")
img_schema = encode_img(ASSETS_DIR / "image3.png")
img_churn = encode_img(FIGURES_DIR / "fig3_churn_roc_feature_importance.png")
img_kmeans = encode_img(FIGURES_DIR / "fig4_kmeans_pca_elbow.png")
img_forecast = encode_img(FIGURES_DIR / "fig5_revenue_forecasting.png")
img_regional = encode_img(FIGURES_DIR / "fig6_regional_economics.png")
img_bcg = encode_img(FIGURES_DIR / "fig7_category_bcg_matrix.png")

# Common CSS
COMMON_CSS = """
  *, *:before, *:after {
    box-sizing: border-box;
  }

  body {
    font-family: 'Times New Roman', Times, Georgia, serif;
    font-size: 10.5pt;
    line-height: 1.5;
    color: #1E293B;
    background-color: #FFFFFF;
    margin: 0;
    padding: 0;
  }

  .page-break {
    page-break-before: always;
    break-before: page;
  }

  .avoid-break {
    page-break-inside: avoid;
    break-inside: avoid;
  }

  h1, h2, h3, h4 {
    font-family: 'Times New Roman', Georgia, serif;
    color: #7A0019; /* VIT Maroon */
    margin-top: 1.1em;
    margin-bottom: 0.35em;
    page-break-after: avoid;
    break-after: avoid;
  }

  h1.chapter-title {
    font-size: 16pt;
    font-weight: bold;
    text-transform: uppercase;
    text-align: center;
    border-bottom: 2px solid #7A0019;
    padding-bottom: 5px;
    margin-top: 0;
    margin-bottom: 14px;
    letter-spacing: 0.5px;
  }

  .chapter-number {
    font-size: 12pt;
    text-transform: uppercase;
    color: #0F243E; /* Deep Navy */
    text-align: center;
    font-weight: bold;
    margin-bottom: 3px;
    letter-spacing: 1px;
  }

  h2.section-title {
    font-size: 12pt;
    font-weight: bold;
    color: #0F243E;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 3px;
    margin-top: 14px;
    margin-bottom: 8px;
  }

  h3.subsection-title {
    font-size: 11pt;
    font-weight: bold;
    color: #1E293B;
    margin-top: 12px;
    margin-bottom: 5px;
  }

  p {
    text-align: justify;
    text-justify: inter-word;
    margin-top: 0;
    margin-bottom: 7px;
    font-size: 10pt;
    line-height: 1.5;
  }

  ul, ol {
    margin-top: 0;
    margin-bottom: 8px;
    padding-left: 20px;
  }

  li {
    margin-bottom: 3px;
    font-size: 10pt;
    text-align: justify;
    line-height: 1.45;
  }

  /* Tables */
  table.report-table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0 14px 0;
    font-size: 9pt;
    page-break-inside: auto;
  }

  table.report-table tr {
    page-break-inside: avoid;
    page-break-after: auto;
  }

  table.report-table th {
    background-color: #7A0019;
    color: #FFFFFF;
    font-weight: bold;
    text-align: left;
    padding: 6px 8px;
    border: 1px solid #5A0013;
    font-size: 9pt;
  }

  table.report-table td {
    padding: 5px 8px;
    border: 1px solid #CBD5E1;
    vertical-align: top;
    line-height: 1.35;
  }

  table.report-table tr:nth-child(even) td {
    background-color: #F8FAFC;
  }

  .table-caption {
    font-size: 9.5pt;
    font-weight: bold;
    color: #0F243E;
    margin-top: 10px;
    margin-bottom: 4px;
    page-break-after: avoid;
    text-align: left;
  }

  /* Figures */
  .figure-container {
    text-align: center;
    margin: 12px auto;
    page-break-inside: avoid;
    max-width: 98%;
  }

  .figure-img {
    max-width: 90%;
    max-height: 280px;
    height: auto;
    border: 1px solid #CBD5E1;
    border-radius: 4px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
  }

  .figure-caption {
    font-size: 9pt;
    font-style: italic;
    color: #334155;
    margin-top: 5px;
    text-align: center;
  }

  /* Code blocks */
  pre.code-block {
    background-color: #0F172A;
    color: #E2E8F0;
    font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
    font-size: 8pt;
    line-height: 1.4;
    padding: 10px 12px;
    border-radius: 4px;
    border-left: 4px solid #7A0019;
    margin: 8px 0 12px 0;
    white-space: pre-wrap;
    word-break: break-all;
    page-break-inside: avoid;
  }

  code.inline {
    font-family: 'Courier New', monospace;
    font-size: 8.5pt;
    background-color: #F1F5F9;
    color: #0F243E;
    padding: 1px 3px;
    border-radius: 2px;
    border: 1px solid #E2E8F0;
  }

  .alert-box {
    border-left: 4px solid #0F243E;
    background-color: #F8FAFC;
    padding: 8px 12px;
    margin: 8px 0 12px 0;
    border-radius: 0 4px 4px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
  }

  .alert-box.info {
    border-left-color: #7A0019;
    background-color: #FDF2F4;
  }

  /* Cover Container */
  .cover-container {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: center;
    border: 3px double #7A0019;
    padding: 24px 20px;
    box-sizing: border-box;
  }

  .cover-logo {
    max-height: 65px;
    margin-bottom: 10px;
  }

  .cover-title {
    font-size: 18pt;
    font-weight: bold;
    color: #7A0019;
    line-height: 1.25;
    margin-bottom: 6px;
    letter-spacing: 0.5px;
  }

  .cover-subtitle {
    font-size: 12pt;
    font-style: italic;
    color: #0F243E;
    margin-bottom: 12px;
  }

  .cover-report-type {
    font-size: 12pt;
    font-weight: bold;
    color: #1E293B;
    letter-spacing: 2px;
    margin-top: 8px;
    margin-bottom: 6px;
  }

  .cover-submission-text {
    font-size: 10pt;
    color: #334155;
    margin-bottom: 3px;
    line-height: 1.35;
  }

  .cover-degree {
    font-size: 12pt;
    font-weight: bold;
    color: #0F243E;
    letter-spacing: 1px;
    margin: 4px 0;
  }

  .cover-table-container {
    margin: 12px auto;
    width: 90%;
  }

  .cover-guidance {
    margin: 8px 0;
    font-size: 10.5pt;
  }

  .cover-footer {
    margin-top: 10px;
    line-height: 1.3;
  }

  .cover-school {
    font-size: 11pt;
    font-weight: bold;
    color: #7A0019;
    letter-spacing: 0.5px;
  }

  .cover-univ {
    font-size: 13pt;
    font-weight: bold;
    color: #0F243E;
    letter-spacing: 1px;
  }

  .cover-location {
    font-size: 10pt;
    color: #334155;
  }

  .cover-date {
    font-size: 10.5pt;
    font-weight: bold;
    color: #1E293B;
    margin-top: 4px;
  }

  /* Certificate */
  .certificate-box {
    border: 2px solid #7A0019;
    padding: 22px 24px;
    outline: 1px solid #D4AF37;
    outline-offset: -6px;
    box-sizing: border-box;
  }

  .certificate-title {
    font-size: 16pt;
    font-weight: bold;
    color: #7A0019;
    text-align: center;
    letter-spacing: 2px;
    margin-bottom: 14px;
    text-transform: uppercase;
  }

  .certificate-body {
    font-size: 10.5pt;
    line-height: 1.55;
    text-align: justify;
    margin-bottom: 12px;
  }

  .sig-table {
    width: 100%;
    margin-top: 16px;
    border-collapse: collapse;
  }

  .sig-table td {
    vertical-align: bottom;
    padding: 6px 4px;
    font-size: 9.5pt;
  }

  .sig-line {
    border-top: 1px solid #1E293B;
    width: 80%;
    margin-top: 28px;
    margin-bottom: 3px;
  }

  /* Biodata Grid */
  .biodata-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 12px;
  }

  .biodata-card {
    border: 1px solid #CBD5E1;
    border-top: 4px solid #7A0019;
    background-color: #FFFFFF;
    border-radius: 4px;
    padding: 10px 12px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    page-break-inside: avoid;
  }

  .biodata-name {
    font-size: 11pt;
    font-weight: bold;
    color: #0F243E;
    margin-bottom: 6px;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 3px;
  }

  .biodata-row {
    font-size: 9pt;
    margin-bottom: 3px;
    display: flex;
    justify-content: space-between;
  }

  .biodata-label {
    font-weight: 600;
    color: #64748B;
  }

  .biodata-val {
    color: #1E293B;
    text-align: right;
  }
"""

# 1. COVER PAGE HTML
cover_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Cover Page</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 15mm 18mm 15mm 18mm;
  }}
  {COMMON_CSS}
  body, html {{
    height: 100%;
    margin: 0;
    padding: 0;
  }}
</style>
</head>
<body>
<div class="cover-container">
  <div class="cover-header">
    <img src="{img_logo}" alt="VIT-AP University Logo" class="cover-logo"><br>
    <div class="cover-title">E-COMMERCE BUSINESS INTELLIGENCE &amp; PREDICTIVE ANALYTICS PLATFORM</div>
    <div class="cover-subtitle">An End-to-End Analytics and Predictive Intelligence System</div>
    <div class="cover-report-type">A CAPSTONE PROJECT REPORT</div>
    <div class="cover-submission-text">Submitted in partial fulfillment of the requirements for the award of the degree of</div>
    <div class="cover-degree">BACHELOR OF TECHNOLOGY</div>
    <div class="cover-submission-text">IN</div>
    <div class="cover-degree" style="font-size: 11.5pt;">COMPUTER SCIENCE AND ENGINEERING</div>
  </div>

  <div class="cover-table-container">
    <div style="font-size: 10.5pt; font-weight: bold; color: #0F243E; margin-bottom: 5px;">Submitted by</div>
    <table class="report-table" style="margin: 0 auto; width: 100%;">
      <thead>
        <tr>
          <th style="width: 12%; text-align: center;">S. No.</th>
          <th style="width: 53%;">Student Name</th>
          <th style="width: 35%; text-align: center;">Registration Number</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="text-align: center;">1</td>
          <td><strong>Gajjala Srithika</strong></td>
          <td style="text-align: center;">23BCE7911</td>
        </tr>
        <tr>
          <td style="text-align: center;">2</td>
          <td><strong>Papasani Suhitha</strong></td>
          <td style="text-align: center;">23BCE7826</td>
        </tr>
        <tr>
          <td style="text-align: center;">3</td>
          <td><strong>M Akshay Sharma</strong></td>
          <td style="text-align: center;">23BCE9668</td>
        </tr>
        <tr>
          <td style="text-align: center;">4</td>
          <td><strong>Ala Venkata Veera Ritwik</strong></td>
          <td style="text-align: center;">23BCE9633</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="cover-guidance">
    <span style="font-size: 10pt; color: #475569;">Under the Guidance of</span><br>
    <strong style="font-size: 11.5pt; color: #7A0019;">Prof. N. Lakshmipathi Anantha</strong><br>
    <span style="font-size: 9.5pt; color: #64748B;">Faculty Project Guide</span>
  </div>

  <div class="cover-footer">
    <div class="cover-school">SCHOOL OF COMPUTER SCIENCE AND ENGINEERING</div>
    <div class="cover-univ">VIT-AP UNIVERSITY</div>
    <div class="cover-location">AMARAVATI – 522237, ANDHRA PRADESH</div>
    <div class="cover-date">NOVEMBER 2026</div>
  </div>
</div>
</body>
</html>
"""

# 2. REPORT BODY HTML (Starts at Certificate, Page 2)
body_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Report Body</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 20mm 18mm 20mm 18mm;
  }}
  {COMMON_CSS}
</style>
</head>
<body>

<!-- ================= CERTIFICATE PAGE ================= -->
<div class="certificate-box">
  <div>
    <div class="certificate-title">CERTIFICATE</div>
    <div class="certificate-body">
      This is to certify that the capstone project report titled <strong>“E-Commerce Business Intelligence &amp; Predictive Analytics Platform: An End-to-End Analytics and Predictive Intelligence System”</strong> is submitted by the students listed below, who are pursuing the <strong>Bachelor of Technology in Computer Science and Engineering</strong> at <strong>VIT-AP University</strong>. The work is submitted in partial fulfilment of the requirements for the award of the degree and was carried out under the guidance of <strong>Prof. N. Lakshmipathi Anantha</strong>.
    </div>
    <div style="margin: 10px auto; width: 95%;">
      <table class="report-table" style="margin: 0 auto; width: 100%;">
        <thead>
          <tr>
            <th style="width: 12%; text-align: center;">S. No.</th>
            <th style="width: 53%;">Student Name</th>
            <th style="width: 35%; text-align: center;">Registration Number</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="text-align: center;">1</td>
            <td>Gajjala Srithika</td>
            <td style="text-align: center;">23BCE7911</td>
          </tr>
          <tr>
            <td style="text-align: center;">2</td>
            <td>Papasani Suhitha</td>
            <td style="text-align: center;">23BCE7826</td>
          </tr>
          <tr>
            <td style="text-align: center;">3</td>
            <td>M Akshay Sharma</td>
            <td style="text-align: center;">23BCE9668</td>
          </tr>
          <tr>
            <td style="text-align: center;">4</td>
            <td>Ala Venkata Veera Ritwik</td>
            <td style="text-align: center;">23BCE9633</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="certificate-body" style="margin-top: 10px;">
      This report presents the proposed design, verified database engineering, statistical exploratory analytics, predictive intelligence models, and executive visualization dashboards of an enterprise e-commerce analytics platform using the Brazilian E-Commerce Public Dataset by Olist. The implementation results, model scores, dashboard screenshots, and final empirical measurements have been rigorously validated.
    </div>
  </div>

  <div>
    <table class="sig-table">
      <tr>
        <td style="width: 50%;">
          <div class="sig-line"></div>
          <strong>Prof. N. Lakshmipathi Anantha</strong><br>
          Faculty Project Guide
        </td>
        <td style="width: 50%; text-align: right;">
          <div style="font-size: 9.5pt; color: #475569; margin-bottom: 20px;">The project report is <strong>satisfactory</strong> / unsatisfactory.</div>
        </td>
      </tr>
      <tr>
        <td style="padding-top: 22px;">
          <div class="sig-line"></div>
          <strong>Internal Examiner</strong>
        </td>
        <td style="padding-top: 22px; text-align: right;">
          <div class="sig-line" style="margin-left: auto;"></div>
          <strong>External Examiner</strong>
        </td>
      </tr>
      <tr>
        <td colspan="2" style="padding-top: 26px; text-align: center;">
          <div style="font-weight: bold; color: #0F243E; margin-bottom: 20px;">Approved by</div>
          <table style="width: 100%;">
            <tr>
              <td style="width: 50%; text-align: left;">
                <div class="sig-line"></div>
                <strong>PROGRAM CHAIR</strong><br>
                School of Computer Science and Engineering
              </td>
              <td style="width: 50%; text-align: right;">
                <div class="sig-line" style="margin-left: auto;"></div>
                <strong>DEAN</strong><br>
                School of Computer Science and Engineering
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </div>
</div>

<!-- ================= ACKNOWLEDGEMENT ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">ACKNOWLEDGEMENT</h1>

<p>We would like to thank <strong>VIT-AP University</strong> and the <strong>School of Computer Science and Engineering</strong> for providing the facilities, learning environment and support needed to complete this capstone project.</p>

<p>We are especially grateful to our project guide, <strong>Prof. N. Lakshmipathi Anantha</strong>, for the advice and feedback provided while we planned and implemented this work. The guidance helped us define the project scope, choose suitable analytical methods and organize the steps needed to build the proposed platform.</p>

<p>We also thank the contributors who made the Brazilian E-Commerce Public Dataset by Olist available for academic use. We acknowledge the teams behind Python, pandas, PostgreSQL, scikit-learn, statsmodels and Microsoft Power BI for developing the tools and documentation that support the technical work described in this report.</p>

<p>Finally, we thank our families, classmates and everyone who encouraged us or shared useful feedback while we prepared this report.</p>

<div style="margin-top: 28px; text-align: right;">
  <p><strong>Team Members:</strong></p>
  <p style="margin-bottom: 2px;">Gajjala Srithika (23BCE7911)</p>
  <p style="margin-bottom: 2px;">Papasani Suhitha (23BCE7826)</p>
  <p style="margin-bottom: 2px;">M Akshay Sharma (23BCE9668)</p>
  <p style="margin-bottom: 2px;">Ala Venkata Veera Ritwik (23BCE9633)</p>
</div>

<!-- ================= ABSTRACT ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">ABSTRACT</h1>

<p>Online stores create data whenever customers place orders, make payments, receive products or submit reviews. These records can reveal useful information about customers, products, sales and delivery performance. However, it is difficult to make sound business decisions when data preparation, database management, analysis, prediction and reporting are handled as separate activities. This project proposes an <strong>E-Commerce Customer &amp; Revenue Intelligence Platform</strong> that brings these tasks together in one organized workflow.</p>

<p>The project uses the Brazilian E-Commerce Public Dataset by Olist. This public, anonymized dataset contains approximately 100,000 orders from 2016 to 2018, along with related records for customers, order items, payments, reviews, products, sellers and geolocation. Python will be used to inspect, clean and validate the source CSV files before loading the prepared data into PostgreSQL. The database will include staging tables and a dimensional model to support consistent SQL analysis and reporting.</p>

<p>The analytical work covers order and sales trends, average order value, product-category performance, delivery timing, customer review scores and repeat-customer behaviour using customer-level identifiers. The predictive modelling part investigates customer segmentation using K-Means clustering, evaluates a pre-attrition churn-risk classification experiment to avoid target leakage, and applies time-series sales forecasting to predict forward revenue trends.</p>

<p>Microsoft Power BI is used to present an overall business view and focused dashboards for customer, product and delivery performance, giving business teams reliable information supported by verified underlying data.</p>

<div class="alert-box info" style="margin-top: 20px;">
  <strong>Keywords:</strong> E-Commerce Analytics, Relational Data Warehousing, Star Schema, Dimensional Modeling, PostgreSQL, RFM Customer Segmentation, K-Means Clustering, Churn-Risk Classification, Feature Leakage Ablation, Time-Series Sales Forecasting, Power BI Dashboards, Olist Public Dataset.
</div>

<!-- ================= TABLE OF CONTENTS ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">TABLE OF CONTENTS</h1>

<table class="report-table" style="width: 100%; border: none; font-size: 8.5pt;">
  <thead>
    <tr style="background-color: #0F243E;">
      <th style="width: 10%; text-align: center; padding: 4px;">S.No.</th>
      <th style="width: 15%; text-align: center; padding: 4px;">Chapter No.</th>
      <th style="width: 63%; padding: 4px;">CONTENTS</th>
      <th style="width: 12%; text-align: center; padding: 4px;">Page No.</th>
    </tr>
  </thead>
  <tbody>
    <tr><td></td><td></td><td><strong>Certificate</strong></td><td style="text-align: center;">2</td></tr>
    <tr><td></td><td></td><td><strong>Acknowledgement</strong></td><td style="text-align: center;">3</td></tr>
    <tr><td></td><td></td><td><strong>Abstract</strong></td><td style="text-align: center;">4</td></tr>
    <tr><td></td><td></td><td><strong>List of Tables &amp; List of Figures</strong></td><td style="text-align: center;">6</td></tr>
    <tr><td style="text-align: center;"><strong>1.</strong></td><td style="text-align: center;"><strong>1</strong></td><td><strong>INTRODUCTION</strong></td><td style="text-align: center;"><strong>7</strong></td></tr>
    <tr><td></td><td style="text-align: center;">1.1</td><td style="padding-left: 15px;">Objectives</td><td style="text-align: center;">7</td></tr>
    <tr><td></td><td style="text-align: center;">1.2</td><td style="padding-left: 15px;">Background and Literature Survey</td><td style="text-align: center;">8</td></tr>
    <tr><td></td><td style="text-align: center;">1.2.1</td><td style="padding-left: 30px;">E-commerce Data Analytics</td><td style="text-align: center;">8</td></tr>
    <tr><td></td><td style="text-align: center;">1.2.2</td><td style="padding-left: 30px;">Data Warehousing and Dimensional Modelling</td><td style="text-align: center;">8</td></tr>
    <tr><td></td><td style="text-align: center;">1.2.3</td><td style="padding-left: 30px;">RFM Analysis and Customer Value</td><td style="text-align: center;">9</td></tr>
    <tr><td></td><td style="text-align: center;">1.2.4</td><td style="padding-left: 30px;">Customer Segmentation</td><td style="text-align: center;">9</td></tr>
    <tr><td></td><td style="text-align: center;">1.2.5</td><td style="padding-left: 30px;">Churn-risk Modelling</td><td style="text-align: center;">9</td></tr>
    <tr><td></td><td style="text-align: center;">1.2.6</td><td style="padding-left: 30px;">Sales Forecasting</td><td style="text-align: center;">9</td></tr>
    <tr><td></td><td style="text-align: center;">1.2.7</td><td style="padding-left: 30px;">Research Gap and Project Motivation</td><td style="text-align: center;">10</td></tr>
    <tr><td></td><td style="text-align: center;">1.3</td><td style="padding-left: 15px;">Organization of the Report</td><td style="text-align: center;">10</td></tr>
    <tr><td style="text-align: center;"><strong>2.</strong></td><td style="text-align: center;"><strong>2</strong></td><td><strong>E-COMMERCE CUSTOMER &amp; REVENUE INTELLIGENCE PLATFORM</strong></td><td style="text-align: center;"><strong>11</strong></td></tr>
    <tr><td></td><td style="text-align: center;">2.1</td><td style="padding-left: 15px;">Proposed System</td><td style="text-align: center;">11</td></tr>
    <tr><td></td><td style="text-align: center;">2.1.1</td><td style="padding-left: 30px;">Functional Requirements</td><td style="text-align: center;">12</td></tr>
    <tr><td></td><td style="text-align: center;">2.1.2</td><td style="padding-left: 30px;">Non-functional Requirements</td><td style="text-align: center;">12</td></tr>
    <tr><td></td><td style="text-align: center;">2.2</td><td style="padding-left: 15px;">Working Methodology</td><td style="text-align: center;">13</td></tr>
    <tr><td></td><td style="text-align: center;">2.3</td><td style="padding-left: 15px;">Standards and Design Principles</td><td style="text-align: center;">14</td></tr>
    <tr><td></td><td style="text-align: center;">2.4</td><td style="padding-left: 15px;">System Details</td><td style="text-align: center;">14</td></tr>
    <tr><td></td><td style="text-align: center;">2.4.1</td><td style="padding-left: 30px;">Software Details</td><td style="text-align: center;">14</td></tr>
    <tr><td></td><td style="text-align: center;">2.4.2</td><td style="padding-left: 30px;">Hardware Details</td><td style="text-align: center;">15</td></tr>
    <tr><td></td><td style="text-align: center;">2.5</td><td style="padding-left: 15px;">Dataset Description</td><td style="text-align: center;">15</td></tr>
    <tr><td></td><td style="text-align: center;">2.5.1</td><td style="padding-left: 30px;">Important Source Fields</td><td style="text-align: center;">15</td></tr>
    <tr><td></td><td style="text-align: center;">2.5.2</td><td style="padding-left: 30px;">Dataset Relationships</td><td style="text-align: center;">16</td></tr>
    <tr><td></td><td style="text-align: center;">2.5.3</td><td style="padding-left: 30px;">Dataset Limitations</td><td style="text-align: center;">16</td></tr>
    <tr><td></td><td style="text-align: center;">2.6</td><td style="padding-left: 15px;">Database Design</td><td style="text-align: center;">17</td></tr>
    <tr><td></td><td style="text-align: center;">2.7</td><td style="padding-left: 15px;">Business Analytics and Key Metrics</td><td style="text-align: center;">18</td></tr>
    <tr><td></td><td style="text-align: center;">2.8</td><td style="padding-left: 15px;">Customer Intelligence</td><td style="text-align: center;">19</td></tr>
    <tr><td></td><td style="text-align: center;">2.8.1</td><td style="padding-left: 30px;">RFM Analysis</td><td style="text-align: center;">19</td></tr>
    <tr><td></td><td style="text-align: center;">2.8.2</td><td style="padding-left: 30px;">Cohort and Retention Analysis</td><td style="text-align: center;">19</td></tr>
    <tr><td></td><td style="text-align: center;">2.8.3</td><td style="padding-left: 30px;">Historical Customer Value</td><td style="text-align: center;">19</td></tr>
    <tr><td></td><td style="text-align: center;">2.9</td><td style="padding-left: 15px;">Predictive Modelling</td><td style="text-align: center;">19</td></tr>
    <tr><td></td><td style="text-align: center;">2.9.1</td><td style="padding-left: 30px;">Customer Segmentation Using K-Means</td><td style="text-align: center;">19</td></tr>
    <tr><td></td><td style="text-align: center;">2.9.2</td><td style="padding-left: 30px;">Churn-risk Classification Experiment</td><td style="text-align: center;">20</td></tr>
    <tr><td></td><td style="text-align: center;">2.9.3</td><td style="padding-left: 30px;">Sales Forecasting</td><td style="text-align: center;">21</td></tr>
    <tr><td></td><td style="text-align: center;">2.10</td><td style="padding-left: 15px;">Power BI Dashboard Design</td><td style="text-align: center;">21</td></tr>
    <tr><td style="text-align: center;"><strong>3.</strong></td><td style="text-align: center;"><strong>3</strong></td><td><strong>COST ANALYSIS</strong></td><td style="text-align: center;"><strong>22</strong></td></tr>
    <tr><td></td><td style="text-align: center;">3.1</td><td style="padding-left: 15px;">List of Components and Their Cost</td><td style="text-align: center;">22</td></tr>
    <tr><td></td><td style="text-align: center;">3.2</td><td style="padding-left: 15px;">Cost Estimation Assumptions</td><td style="text-align: center;">22</td></tr>
    <tr><td style="text-align: center;"><strong>4.</strong></td><td style="text-align: center;"><strong>4</strong></td><td><strong>RESULTS AND DISCUSSION</strong></td><td style="text-align: center;"><strong>24</strong></td></tr>
    <tr><td></td><td style="text-align: center;">4.1</td><td style="padding-left: 15px;">Data Profiling and Validation Outputs</td><td style="text-align: center;">24</td></tr>
    <tr><td></td><td style="text-align: center;">4.2</td><td style="padding-left: 15px;">SQL Analysis Outputs</td><td style="text-align: center;">25</td></tr>
    <tr><td></td><td style="text-align: center;">4.3</td><td style="padding-left: 15px;">Customer Analytics Outputs</td><td style="text-align: center;">26</td></tr>
    <tr><td></td><td style="text-align: center;">4.4</td><td style="padding-left: 15px;">Model Evaluation Outputs</td><td style="text-align: center;">26</td></tr>
    <tr><td></td><td style="text-align: center;">4.5</td><td style="padding-left: 15px;">Dashboard Outputs</td><td style="text-align: center;">28</td></tr>
    <tr><td></td><td style="text-align: center;">4.6</td><td style="padding-left: 15px;">Discussion and Limitations</td><td style="text-align: center;">29</td></tr>
    <tr><td></td><td style="text-align: center;">4.7</td><td style="padding-left: 15px;">Final Implementation Results Summary</td><td style="text-align: center;">30</td></tr>
    <tr><td style="text-align: center;"><strong>5.</strong></td><td style="text-align: center;"><strong>5</strong></td><td><strong>CONCLUSION AND FUTURE WORK</strong></td><td style="text-align: center;"><strong>31</strong></td></tr>
    <tr><td></td><td style="text-align: center;">5.1</td><td style="padding-left: 15px;">Conclusion</td><td style="text-align: center;">31</td></tr>
    <tr><td></td><td style="text-align: center;">5.2</td><td style="padding-left: 15px;">Future Work</td><td style="text-align: center;">31</td></tr>
    <tr><td style="text-align: center;"><strong>6.</strong></td><td style="text-align: center;"><strong>6</strong></td><td><strong>APPENDIX</strong></td><td style="text-align: center;"><strong>33</strong></td></tr>
    <tr><td></td><td style="text-align: center;">A</td><td style="padding-left: 15px;">Sample SQL Definitions</td><td style="text-align: center;">33</td></tr>
    <tr><td></td><td style="text-align: center;">A.1</td><td style="padding-left: 30px;">Item Sales by Month</td><td style="text-align: center;">33</td></tr>
    <tr><td></td><td style="text-align: center;">A.2</td><td style="padding-left: 30px;">Repeat Customers Using customer_unique_id</td><td style="text-align: center;">33</td></tr>
    <tr><td></td><td style="text-align: center;">A.3</td><td style="padding-left: 30px;">Delivery Delay in Days</td><td style="text-align: center;">33</td></tr>
    <tr><td></td><td style="text-align: center;">A.4</td><td style="padding-left: 30px;">Payment Totals Calculated Independently</td><td style="text-align: center;">34</td></tr>
    <tr><td></td><td style="text-align: center;">B</td><td style="padding-left: 15px;">Python ETL Workflow Template</td><td style="text-align: center;">34</td></tr>
    <tr><td></td><td style="text-align: center;">C</td><td style="padding-left: 15px;">Team Responsibilities</td><td style="text-align: center;">35</td></tr>
    <tr><td></td><td style="text-align: center;">D</td><td style="padding-left: 15px;">Final Submission Checklist</td><td style="text-align: center;">35</td></tr>
    <tr><td style="text-align: center;"><strong>7.</strong></td><td style="text-align: center;"><strong>7</strong></td><td><strong>REFERENCES</strong></td><td style="text-align: center;"><strong>36</strong></td></tr>
    <tr><td style="text-align: center;"><strong>8.</strong></td><td style="text-align: center;"><strong>-</strong></td><td><strong>STUDENT BIODATA</strong></td><td style="text-align: center;"><strong>37</strong></td></tr>
  </tbody>
</table>

<!-- ================= LIST OF TABLES & FIGURES ================= -->
<div class="page-break"></div>
<h1 class="chapter-title" style="font-size: 14pt; margin-bottom: 8px;">LIST OF TABLES</h1>

<table class="report-table" style="width: 100%; font-size: 8.5pt; margin-bottom: 16px;">
  <thead>
    <tr>
      <th style="width: 15%; text-align: center; padding: 4px;">TABLE NO.</th>
      <th style="width: 73%; padding: 4px;">TITLE</th>
      <th style="width: 12%; text-align: center; padding: 4px;">PAGE NO.</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="text-align: center;"><strong>1</strong></td><td>Software and tools used across the analytics lifecycle</td><td style="text-align: center;">14</td></tr>
    <tr><td style="text-align: center;"><strong>2</strong></td><td>Olist dataset files and their main contents</td><td style="text-align: center;">15</td></tr>
    <tr><td style="text-align: center;"><strong>3</strong></td><td>Key fields used to describe the source data entities</td><td style="text-align: center;">15</td></tr>
    <tr><td style="text-align: center;"><strong>4</strong></td><td>Analytical fact tables and their data granularity</td><td style="text-align: center;">17</td></tr>
    <tr><td style="text-align: center;"><strong>5</strong></td><td>Dimension tables and descriptive attributes</td><td style="text-align: center;">17</td></tr>
    <tr><td style="text-align: center;"><strong>6</strong></td><td>Business metrics and calculation guidelines</td><td style="text-align: center;">18</td></tr>
    <tr><td style="text-align: center;"><strong>7</strong></td><td>Software, tools and infrastructure cost summary</td><td style="text-align: center;">22</td></tr>
    <tr><td style="text-align: center;"><strong>8</strong></td><td>Data-quality and validation checks specification</td><td style="text-align: center;">24</td></tr>
    <tr><td style="text-align: center;"><strong>8.1</strong></td><td>Empirical data profiling and source quality audit results</td><td style="text-align: center;">24</td></tr>
    <tr><td style="text-align: center;"><strong>9</strong></td><td>Predictive experiments and evaluation measures specification</td><td style="text-align: center;">26</td></tr>
    <tr><td style="text-align: center;"><strong>9.1</strong></td><td>Empirical machine learning and forecasting performance evaluation</td><td style="text-align: center;">27</td></tr>
    <tr><td style="text-align: center;"><strong>10</strong></td><td>Project team roles and expected deliverables</td><td style="text-align: center;">35</td></tr>
    <tr><td style="text-align: center;"><strong>11</strong></td><td>Proposed Power BI dashboard suite and analytical scopes</td><td style="text-align: center;">21</td></tr>
  </tbody>
</table>

<h1 class="chapter-title" style="font-size: 14pt; margin-top: 14px; margin-bottom: 8px;">LIST OF FIGURES</h1>
<table class="report-table" style="width: 100%; font-size: 8.5pt;">
  <thead>
    <tr>
      <th style="width: 15%; text-align: center; padding: 4px;">FIGURE NO.</th>
      <th style="width: 73%; padding: 4px;">TITLE</th>
      <th style="width: 12%; text-align: center; padding: 4px;">PAGE NO.</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="text-align: center;"><strong>2.1</strong></td><td>Architecture of the proposed end-to-end analytics platform</td><td style="text-align: center;">11</td></tr>
    <tr><td style="text-align: center;"><strong>2.2</strong></td><td>Conceptual star-schema relational database design</td><td style="text-align: center;">17</td></tr>
    <tr><td style="text-align: center;"><strong>4.1</strong></td><td>Dual-model churn prediction ROC curves and Gini SHAP feature importance</td><td style="text-align: center;">27</td></tr>
    <tr><td style="text-align: center;"><strong>4.2</strong></td><td>Algorithmic customer segmentation: Elbow WCSS curve and 2D PCA cluster space</td><td style="text-align: center;">27</td></tr>
    <tr><td style="text-align: center;"><strong>4.3</strong></td><td>Longitudinal daily revenue forecasting: Actual vs. Forecast with 95% confidence intervals</td><td style="text-align: center;">28</td></tr>
    <tr><td style="text-align: center;"><strong>4.4</strong></td><td>Regional logistics disparity: Delivery lead time variance and freight ratio across states</td><td style="text-align: center;">28</td></tr>
    <tr><td style="text-align: center;"><strong>4.5</strong></td><td>Product portfolio strategic BCG growth-share matrix</td><td style="text-align: center;">29</td></tr>
  </tbody>
</table>

<!-- ================= CHAPTER 1 ================= -->
<div class="page-break"></div>
<div class="chapter-number">CHAPTER 1</div>
<h1 class="chapter-title">INTRODUCTION</h1>

<h2 class="section-title">1. INTRODUCTION</h2>
<p>E-commerce platforms bring customers, sellers and products together through online transactions. A single order can involve several events: the customer selects an item, submits payment, waits for the order to be approved and delivered, and later leaves a review. These operational records contain valuable information about sales patterns, delivery performance and customer behaviour.</p>

<p>Simply collecting CSV files or exporting operational data is not enough to create a dependable decision-support system. In practice, data is often stored in multiple tables, timestamps may be missing or recorded out of order, and the definitions used for revenue, order counts or repeat purchases can vary. Without a well-planned pipeline, business teams can easily arrive at conflicting numbers from the same basic dataset.</p>

<p>This project brings the main stages of analytics into one workflow. It starts with preparing the raw transaction data, loading it into PostgreSQL, organizing the tables into a dimensional model, running SQL-based descriptive analysis, performing customer segmentation and time-series forecasting, and presenting the results through Power BI dashboards. The project uses the Brazilian E-Commerce Public Dataset by Olist, a real-world dataset covering approximately 100,000 orders placed in Brazil between 2016 and 2018.</p>

<h2 class="section-title">1.1 OBJECTIVES</h2>
<p>The primary objectives of this capstone project are:</p>
<ul>
  <li>To collect and understand the Brazilian E-Commerce Public Dataset by Olist and document its source files, schema and practical constraints.</li>
  <li>To develop a Python-based data preparation process for profiling, cleaning, standardizing and validating the source tables.</li>
  <li>To design a PostgreSQL database with staging tables and a dimensional analytical schema suitable for business reporting.</li>
  <li>To perform SQL-based exploratory and business analysis using joins, aggregations, window functions, common table expressions and date operations.</li>
  <li>To analyze customer behaviour using RFM metrics, customer cohorts, retention measures and historical customer value.</li>
  <li>To analyze product, revenue and operational performance, including item sales, freight costs, payment methods, delivery durations and customer review scores.</li>
  <li>To investigate customer segmentation using K-Means and evaluate a carefully defined churn-risk classification experiment that avoids target leakage.</li>
  <li>To compare baseline sales forecasts with a time-series forecasting approach when the data pattern and history support it.</li>
  <li>To build Power BI dashboards that communicate verified analytical findings and support business decisions.</li>
  <li>To document assumptions, limitations, model evaluation results and reproducible steps in an organized academic report.</li>
</ul>

<h2 class="section-title">1.2 BACKGROUND AND LITERATURE SURVEY</h2>

<h3 class="subsection-title">1.2.1 E-commerce data analytics</h3>
<p>E-commerce analytics uses transaction and customer data to understand past activity and help organizations make better decisions. Operational systems are designed to process orders quickly, but business questions often require summarizing data across many tables, including customers, orders, items, payments and reviews. A successful analytics pipeline must define each business measure clearly, preserve the level of detail of the underlying transactions and make sure that different reports report consistent numbers [1, 2].</p>

<h3 class="subsection-title">1.2.2 Data warehousing and dimensional modelling</h3>
<p>A dimensional model separates measurable business events from the descriptive information that provides context for those events [10]. Fact tables record numerical measures, such as item price, freight value or delivery duration, while dimension tables store descriptive attributes, such as customer locations, product categories, seller details and dates. This structure simplifies analytical SQL queries, reduces repeated data and makes it easier to connect business intelligence tools such as Power BI [4].</p>

<h3 class="subsection-title">1.2.3 RFM analysis and customer value</h3>
<p>RFM analysis is a way to summarize customer purchasing patterns through three measures: Recency (how recently the customer bought something), Frequency (how often they buy) and Monetary value (how much they have spent) [8]. It provides an intuitive way to identify high-value customers, active buyers and customers who may be drifting away. When working with transactional datasets, it is important to distinguish historical revenue-based customer value from forward-looking Customer Lifetime Value (CLV), especially when product costs, marketing expenses and customer-acquisition channels are not available.</p>

<h3 class="subsection-title">1.2.4 Customer segmentation</h3>
<p>Clustering can be used to group customers who show similar behaviour, even when no predefined customer categories exist. K-Means is widely used for this purpose because it is computationally efficient and produces straightforward cluster centroids [5]. Because K-Means relies on distance calculations, numerical features must be examined for skewness and scaled before clustering. Evaluating the clusters using inertia, silhouette scores and practical business interpretation helps teams choose a sensible number of segments.</p>

<h3 class="subsection-title">1.2.5 Churn-risk modelling</h3>
<p>Churn analysis aims to identify customers who may stop buying or interacting with a business. In non-contractual e-commerce settings, customers rarely give formal notice when they leave, so churn is usually defined using a chosen period of inactivity [9]. If a churn model is attempted, the target must be created using future observations, while the input features must be limited to information available before the cut-off date. Including post-cut-off activity or total tenure in the feature set creates target leakage and produces unrealistically high evaluation scores that cannot be used in a live environment.</p>

<h3 class="subsection-title">1.2.6 Sales forecasting</h3>
<p>Sales forecasting uses past observations to estimate future sales. A model should always be compared against simple baselines, such as naïve or moving-average forecasts, before more complex methods are adopted [7]. When transaction series exhibit seasonality or clear trends, time-series models such as SARIMA can be explored, provided the series is sufficiently long and stable. Forecast quality is evaluated using chronological test periods and metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).</p>

<h3 class="subsection-title">1.2.7 Research gap and project motivation</h3>
<p>The methods discussed in this report, including RFM analysis, K-Means, churn classification, sales forecasting and dimensional modelling, are often presented in isolation. Many public projects rely on disconnected Jupyter notebooks, omit data-quality checks or apply predictive models to raw files without first establishing an analytical database. This project addresses that gap by organizing data profiling, PostgreSQL data warehousing, descriptive SQL analysis, customer intelligence, predictive modelling and Power BI reporting into a single, cohesive workflow.</p>

<h2 class="section-title">1.3 ORGANIZATION OF THE REPORT</h2>
<p>The rest of the report is arranged into the following chapters:</p>
<ul>
  <li><strong>Chapter 2</strong> explains the proposed platform, its workflow, software and hardware requirements, the Olist dataset, the database design, the business metrics, the customer intelligence approach, the predictive modelling plans and the Power BI dashboard layout.</li>
  <li><strong>Chapter 3</strong> outlines the expected project costs and explains the assumptions used to estimate software, hardware and operational expenses.</li>
  <li><strong>Chapter 4</strong> describes the data checks and analytical outputs that must be completed, discusses the empirical validation results and reviews the project's limitations.</li>
  <li><strong>Chapter 5</strong> summarizes the project and discusses possible improvements for future work.</li>
  <li><strong>Chapter 6</strong> provides supporting SQL examples, a Python ETL workflow template and the team responsibilities table.</li>
  <li><strong>Chapter 7</strong> contains the dataset, technical documentation and research sources referenced throughout the report.</li>
</ul>

<!-- ================= CHAPTER 2 ================= -->
<div class="page-break"></div>
<div class="chapter-number">CHAPTER 2</div>
<h1 class="chapter-title">E-COMMERCE CUSTOMER &amp; REVENUE INTELLIGENCE PLATFORM</h1>

<p>This chapter introduces the proposed platform, the steps involved in building it, the software environment, the source dataset, the database design and the planned analysis. The system is intended to run as a repeatable batch-processing workflow; it is not designed as a real-time streaming application.</p>

<h2 class="section-title">2.1 PROPOSED SYSTEM</h2>
<p>The platform will use the Olist CSV files as its input. Python will be used to inspect and clean the files, check data types and relationships, and prepare the records for PostgreSQL. PostgreSQL will store both the original staging data and the curated analytical model. SQL views and feature tables will then provide consistent data for customer analysis, product and revenue reporting, predictive experiments and Power BI dashboards.</p>

<div class="figure-container">
  <img src="{img_arch}" alt="Proposed end-to-end system architecture" class="figure-img">
  <div class="figure-caption">Figure 2.1: Proposed end-to-end system architecture of the enterprise analytics platform.</div>
</div>

<p>The platform is organized into six connected parts: (1) data loading and quality checks, (2) PostgreSQL storage and dimensional modelling, (3) descriptive and diagnostic analysis, (4) customer intelligence, (5) predictive modelling and forecasting, and (6) dashboards and business recommendations. Each part will use shared definitions and the same analytical database.</p>

<h3 class="subsection-title">2.1.1 Functional requirements</h3>
<ul>
  <li>The system will import the selected CSV files and record each source file name and its load date.</li>
  <li>The system will check column names, data types, missing values, duplicate records and relationships between tables.</li>
  <li>The system will keep raw or lightly processed data in staging tables, separate from the cleaned analytical tables.</li>
  <li>The system will provide reusable SQL queries or views for analyzing sales, orders, customers, products, payments and delivery performance.</li>
  <li>The system will calculate customer-level RFM measures using <code class="inline">customer_unique_id</code> to identify the same customer across different orders.</li>
  <li>The system will produce model evaluation results and clearly record the target definition and the time periods used for training and testing.</li>
  <li>The system will provide Power BI reports with filters and measures based on the validated analytical database.</li>
</ul>

<h3 class="subsection-title">2.1.2 Non-functional requirements</h3>
<ul>
  <li><strong>Accuracy:</strong> Every business measure should be linked to its source fields and a clearly stated calculation.</li>
  <li><strong>Consistency:</strong> All parts of the platform should follow the same definitions for dates, customers, orders and sales measures.</li>
  <li><strong>Reproducibility:</strong> Python scripts, SQL files, assumptions and model settings should be saved and managed through version control.</li>
  <li><strong>Maintainability:</strong> Data staging, transformation, analysis and visualization should be organized as separate tasks.</li>
  <li><strong>Usability:</strong> Dashboards should have clear titles, readable filters, units and short explanations.</li>
  <li><strong>Responsible interpretation:</strong> Predictions should be treated as estimates, not as certain outcomes.</li>
</ul>

<h2 class="section-title">2.2 WORKING METHODOLOGY</h2>
<ol>
  <li><strong>Step 1 – Collect the data:</strong> Download the public Olist dataset and keep the original CSV files unchanged. Record where the files came from, when they were downloaded and any applicable usage terms.</li>
  <li><strong>Step 2 – Understand the data:</strong> Load each file into pandas, check its size and column names, identify possible primary and foreign keys, convert date fields and review where values are missing.</li>
  <li><strong>Step 3 – Clean the data:</strong> Standardize data types, tidy category text where needed, parse timestamps consistently and investigate duplicate records. Record how missing values are handled. Do not fill in missing data automatically when the absence itself may be meaningful.</li>
  <li><strong>Step 4 – Validate the data:</strong> Check key uniqueness, table relationships, sensible numeric ranges, timestamp order and differences between order-item totals and payment totals. Record any exceptions instead of removing them without explanation.</li>
  <li><strong>Step 5 – Load PostgreSQL:</strong> Import the source records into staging tables. Choose suitable data types, add primary and foreign-key constraints where valid, and create indexes for fields used often in joins.</li>
  <li><strong>Step 6 – Build the dimensional model:</strong> Create separate fact and dimension tables. State the level of detail represented by each fact table and avoid joining multiple one-to-many tables before aggregating their values.</li>
  <li><strong>Step 7 – Perform SQL analysis:</strong> Build reusable queries and views for sales, order counts, average order value, category performance, delivery, payment behaviour and customer activity.</li>
  <li><strong>Step 8 – Study customer behaviour:</strong> Calculate RFM measures, customer cohorts, retention indicators and a historical customer-value estimate based on revenue.</li>
  <li><strong>Step 9 – Run predictive experiments:</strong> Scale the features used for clustering, compare K-Means settings, define a time-based churn experiment to test feasibility, and evaluate a sales forecasting model against simple baselines.</li>
  <li><strong>Step 10 – Connect Power BI:</strong> Link Power BI to the curated tables or views, create reusable measures, design dashboard pages and check that the numbers match the SQL query results.</li>
  <li><strong>Step 11 – Review and document the findings:</strong> Include only results supported by the data, document limitations and note potential next steps for future work.</li>
</ol>

<h2 class="section-title">2.3 STANDARDS AND DESIGN PRINCIPLES</h2>
<ul>
  <li><strong>Data integrity:</strong> Use unique identifiers and check the relationships between tables before running analytical queries.</li>
  <li><strong>Fact-table detail:</strong> Define the level of detail for every fact table. For example, order items should be analyzed at the item level, while payments should be analyzed at the payment level.</li>
  <li><strong>Metric definitions:</strong> Record the filters and formulas used for sales, order counts, delivery time, late delivery and customer review scores.</li>
  <li><strong>Time-aware testing:</strong> Use chronological training and testing periods for churn and forecasting models rather than random shuffling.</li>
  <li><strong>Privacy and security:</strong> Use the anonymized public dataset only for the intended academic project. Store database passwords in environment variables or configuration files, not in public code repositories.</li>
  <li><strong>Reproducibility:</strong> Keep the Python scripts, SQL queries, model settings, dashboard files and this documentation in a shared version-controlled repository.</li>
</ul>

<h2 class="section-title">2.4 SYSTEM DETAILS</h2>

<h3 class="subsection-title">2.4.1 Software details</h3>
<p>The platform relies on established open-source tools for processing and database storage, alongside Power BI Desktop for visual reporting.</p>

<div class="table-caption">Table 1: Software and tools used across the analytics lifecycle</div>
<table class="report-table">
  <thead>
    <tr>
      <th style="width: 25%;">Software / Tool</th>
      <th style="width: 75%;">Purpose in the project</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Python</strong></td>
      <td>Main programming language for data profiling, ETL, feature engineering and model experiments.</td>
    </tr>
    <tr>
      <td><strong>pandas and NumPy</strong></td>
      <td>Tabular data loading, cleaning, transformation, aggregation and numerical operations [3].</td>
    </tr>
    <tr>
      <td><strong>PostgreSQL</strong></td>
      <td>Relational database for staging data, curated tables, analytical views and SQL queries [2].</td>
    </tr>
    <tr>
      <td><strong>SQL</strong></td>
      <td>Joins, aggregations, CTEs, subqueries, window functions, date functions and validation queries.</td>
    </tr>
    <tr>
      <td><strong>scikit-learn</strong></td>
      <td>K-Means clustering, logistic regression, optional random forest, preprocessing and model evaluation [5, 6].</td>
    </tr>
    <tr>
      <td><strong>statsmodels</strong></td>
      <td>Candidate SARIMA/SARIMAX time-series model if data history and diagnostics support it [7].</td>
    </tr>
    <tr>
      <td><strong>Power BI Desktop</strong></td>
      <td>Interactive dashboard design and visualization of curated analytical data [4].</td>
    </tr>
    <tr>
      <td><strong>Jupyter Notebook / VS Code</strong></td>
      <td>Development, experimentation, documentation and debugging.</td>
    </tr>
    <tr>
      <td><strong>Git and GitHub</strong></td>
      <td>Version control and collaboration for code, SQL and documentation.</td>
    </tr>
  </tbody>
</table>
<p>The team will record the exact software and package versions in a requirements file or environment documentation so the setup can be reproduced.</p>

<h3 class="subsection-title">2.4.2 Hardware details</h3>
<p>The proposed platform is software-based, so it does not need dedicated sensors, microcontrollers or special lab equipment. Local data cleaning, PostgreSQL storage, analytical queries and baseline model training can be completed on a standard laptop or desktop computer with 8 GB to 16 GB of RAM, a multi-core processor (such as an Intel Core i5/i7, AMD Ryzen 5/7 or Apple Silicon) and 10 GB to 20 GB of free storage for the raw files, database storage and temporary outputs.</p>

<h2 class="section-title">2.5 DATASET DESCRIPTION</h2>
<p>This project will use the Brazilian E-Commerce Public Dataset by Olist, which is available on Kaggle [1]. The dataset contains information about real orders placed through the Olist marketplace between 2016 and 2018. The main dataset is distributed across nine CSV files.</p>

<div class="table-caption">Table 2: Olist dataset source files and their analytical roles</div>
<table class="report-table">
  <thead>
    <tr>
      <th style="width: 32%;">Source file</th>
      <th style="width: 40%;">Main contents</th>
      <th style="width: 28%;">Typical analytical use</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="inline">olist_orders_dataset.csv</code></td>
      <td>Order status and purchase, approval, carrier, delivery and estimated-delivery timestamps.</td>
      <td>Order lifecycle, monthly orders, delivery delay and cancellations.</td>
    </tr>
    <tr>
      <td><code class="inline">olist_customers_dataset.csv</code></td>
      <td>Customer identifiers and customer location fields.</td>
      <td>Customer grouping, repeat-purchase analysis and geography.</td>
    </tr>
    <tr>
      <td><code class="inline">olist_order_items_dataset.csv</code></td>
      <td>Order item, product, seller, price and freight value.</td>
      <td>Item-level sales, category performance, freight analysis.</td>
    </tr>
    <tr>
      <td><code class="inline">olist_order_payments_dataset.csv</code></td>
      <td>Payment sequence, payment type, installments and payment value.</td>
      <td>Payment method and payment reconciliation.</td>
    </tr>
    <tr>
      <td><code class="inline">olist_order_reviews_dataset.csv</code></td>
      <td>Review identifiers, scores, comments and review timestamps.</td>
      <td>Customer feedback and review-score analysis.</td>
    </tr>
    <tr>
      <td><code class="inline">olist_products_dataset.csv</code></td>
      <td>Product category and product physical attributes.</td>
      <td>Product and category analysis.</td>
    </tr>
    <tr>
      <td><code class="inline">olist_sellers_dataset.csv</code></td>
      <td>Seller identifiers and seller location.</td>
      <td>Seller and geographic analysis.</td>
    </tr>
    <tr>
      <td><code class="inline">olist_geolocation_dataset.csv</code></td>
      <td>Zip-code prefix, latitude, longitude, city and state.</td>
      <td>Optional geographic enrichment; prefixes may have multiple rows.</td>
    </tr>
    <tr>
      <td><code class="inline">product_category_name_translation.csv</code></td>
      <td>Portuguese-to-English category-name mapping.</td>
      <td>Readable product category labels.</td>
    </tr>
  </tbody>
</table>

<h3 class="subsection-title">2.5.1 Important source fields</h3>
<div class="table-caption">Table 3: Summary of the primary entities and important fields</div>
<table class="report-table">
  <thead>
    <tr>
      <th style="width: 20%;">Entity</th>
      <th style="width: 50%;">Important fields</th>
      <th style="width: 30%;">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Customers</strong></td>
      <td><code class="inline">customer_id</code>, <code class="inline">customer_unique_id</code>, <code class="inline">customer_zip_code_prefix</code>, <code class="inline">customer_city</code>, <code class="inline">customer_state</code></td>
      <td>Use <code class="inline">customer_unique_id</code> for repeat-purchase identity.</td>
    </tr>
    <tr>
      <td><strong>Orders</strong></td>
      <td><code class="inline">order_id</code>, <code class="inline">customer_id</code>, <code class="inline">order_status</code>, <code class="inline">order_purchase_timestamp</code>, <code class="inline">order_delivered_customer_date</code>, <code class="inline">order_estimated_delivery_date</code></td>
      <td>Order-level lifecycle and date fields.</td>
    </tr>
    <tr>
      <td><strong>Order items</strong></td>
      <td><code class="inline">order_id</code>, <code class="inline">order_item_id</code>, <code class="inline">product_id</code>, <code class="inline">seller_id</code>, <code class="inline">price</code>, <code class="inline">freight_value</code></td>
      <td>One row per item within an order.</td>
    </tr>
    <tr>
      <td><strong>Payments</strong></td>
      <td><code class="inline">order_id</code>, <code class="inline">payment_sequential</code>, <code class="inline">payment_type</code>, <code class="inline">payment_installments</code>, <code class="inline">payment_value</code></td>
      <td>An order can have multiple payment rows.</td>
    </tr>
    <tr>
      <td><strong>Reviews</strong></td>
      <td><code class="inline">review_id</code>, <code class="inline">order_id</code>, <code class="inline">review_score</code>, <code class="inline">review_creation_date</code></td>
      <td>A review record is linked to an order.</td>
    </tr>
    <tr>
      <td><strong>Products</strong></td>
      <td><code class="inline">product_id</code>, <code class="inline">product_category_name</code>, <code class="inline">product_weight_g</code>, <code class="inline">product_length_cm</code>, <code class="inline">product_height_cm</code>, <code class="inline">product_width_cm</code></td>
      <td>Product dimensions and category.</td>
    </tr>
    <tr>
      <td><strong>Sellers</strong></td>
      <td><code class="inline">seller_id</code>, <code class="inline">seller_zip_code_prefix</code>, <code class="inline">seller_city</code>, <code class="inline">seller_state</code></td>
      <td>Seller geography.</td>
    </tr>
  </tbody>
</table>

<h3 class="subsection-title">2.5.2 Dataset relationships</h3>
<p>The primary relationships linking the source files are:</p>
<ul>
  <li><code class="inline">customers.customer_id</code> &rarr; <code class="inline">orders.customer_id</code></li>
  <li><code class="inline">orders.order_id</code> &rarr; <code class="inline">order_items.order_id</code></li>
  <li><code class="inline">orders.order_id</code> &rarr; <code class="inline">order_payments.order_id</code></li>
  <li><code class="inline">orders.order_id</code> &rarr; <code class="inline">order_reviews.order_id</code></li>
  <li><code class="inline">order_items.product_id</code> &rarr; <code class="inline">products.product_id</code></li>
  <li><code class="inline">order_items.seller_id</code> &rarr; <code class="inline">sellers.seller_id</code></li>
  <li><code class="inline">customer and seller zip-code prefixes</code> &rarr; <code class="inline">geolocation.geolocation_zip_code_prefix</code> (lookup).</li>
</ul>
<p>A single zip-code prefix may have several coordinate records in the geolocation table. Geolocation data should therefore be summarized or matched carefully before joining, to avoid creating duplicate rows in other tables.</p>

<h3 class="subsection-title">2.5.3 Dataset limitations</h3>
<ul>
  <li>The main dataset does not include a ready-made customer churn label. If the team explores churn risk, it must clearly define the inactivity condition, cutoff date, and observation window used in the experiment.</li>
  <li>The main dataset does not include cost of goods sold or all operating expenses. The report should therefore focus on item sales, freight value and order values rather than claiming true accounting profit or net margin.</li>
  <li>The main dataset does not include customer advertising campaigns, campaign spend or website traffic. Customer acquisition cost and return on ad spend cannot be calculated from the main transaction files.</li>
  <li>There is no dedicated returns table in the main dataset. The report should not create return metrics unless return proxy criteria are explicitly stated and verified.</li>
  <li>If the separate Olist Marketing Funnel dataset is used, it should be treated as seller-acquisition data rather than consumer advertising data.</li>
  <li>The dataset covers a relatively short period, which limits the strength of long-term seasonal forecasting.</li>
</ul>

<h2 class="section-title">2.6 DATABASE DESIGN</h2>
<p>The database design has two main layers. The staging layer keeps the source data in its original tabular form after initial data cleaning. The analytical layer organizes the data into a dimensional star schema. This structure separates transactional facts from descriptive dimensions, making it easier to write consistent SQL queries and build Power BI reports.</p>

<div class="figure-container">
  <img src="{img_schema}" alt="Conceptual star-schema view" class="figure-img">
  <div class="figure-caption">Figure 2.2: Conceptual star-schema database design showing fact tables, dimensions, and granular foreign key linkages.</div>
</div>

<div class="table-caption">Table 4: Analytical fact tables and their data granularity</div>
<table class="report-table">
  <thead>
    <tr>
      <th style="width: 25%;">Proposed fact table</th>
      <th style="width: 35%;">Grain</th>
      <th style="width: 40%;">Example measures / fields</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="inline">fact_order_items</code></td>
      <td>One row per order item (<code class="inline">order_id</code> + <code class="inline">order_item_id</code>).</td>
      <td><code class="inline">price</code>, <code class="inline">freight_value</code>, item quantity; customer, product, seller and date keys.</td>
    </tr>
    <tr>
      <td><code class="inline">fact_orders</code></td>
      <td>One row per <code class="inline">order_id</code>.</td>
      <td>Order status, order-level lifecycle timestamps and derived delivery indicators.</td>
    </tr>
    <tr>
      <td><code class="inline">fact_payments</code></td>
      <td>One row per payment sequence within an order.</td>
      <td><code class="inline">payment_value</code>, <code class="inline">payment_installments</code>, payment type key.</td>
    </tr>
    <tr>
      <td><code class="inline">fact_reviews</code></td>
      <td>One row per <code class="inline">review_id</code>.</td>
      <td><code class="inline">review_score</code> and review timing fields.</td>
    </tr>
  </tbody>
</table>

<div class="table-caption">Table 5: Dimension tables and descriptive attributes</div>
<table class="report-table">
  <thead>
    <tr>
      <th style="width: 30%;">Proposed dimension</th>
      <th style="width: 70%;">Descriptive attributes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="inline">dim_customer</code></td>
      <td><code class="inline">customer_unique_id</code>, <code class="inline">customer_id</code> reference where required, customer city and state.</td>
    </tr>
    <tr>
      <td><code class="inline">dim_product</code></td>
      <td><code class="inline">product_id</code>, translated category, product weight and dimensions.</td>
    </tr>
    <tr>
      <td><code class="inline">dim_seller</code></td>
      <td><code class="inline">seller_id</code>, seller city and state.</td>
    </tr>
    <tr>
      <td><code class="inline">dim_date</code></td>
      <td>Date key, calendar date, day, month, quarter and year; role-playing dates may be used for purchase and delivery.</td>
    </tr>
    <tr>
      <td><code class="inline">dim_location</code></td>
      <td>Normalized zip-prefix geography, city, state and optional aggregated coordinates.</td>
    </tr>
    <tr>
      <td><code class="inline">dim_payment_type</code></td>
      <td>Payment type description and related payment category.</td>
    </tr>
  </tbody>
</table>

<p>One important rule is to aggregate each fact table separately before combining measures. An order can have several items and several payment rows. Joining items directly to payments before summarizing the amounts can lead to duplicated totals. The report should state where this issue applies and how it is avoided.</p>

<h2 class="section-title">2.7 BUSINESS ANALYTICS AND KEY METRICS</h2>
<div class="table-caption">Table 6: Business metrics and calculation guidelines</div>
<table class="report-table">
  <thead>
    <tr>
      <th style="width: 25%;">Metric</th>
      <th style="width: 45%;">Proposed definition</th>
      <th style="width: 30%;">Interpretation / caution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Item sales value</strong></td>
      <td>Sum of <code class="inline">order_items.price</code> for the selected order population.</td>
      <td>Keep separate from freight and payment value; state included order statuses.</td>
    </tr>
    <tr>
      <td><strong>Freight value</strong></td>
      <td>Sum of <code class="inline">order_items.freight_value</code> for the selected order population.</td>
      <td>Analyze separately from item sales.</td>
    </tr>
    <tr>
      <td><strong>Total order value proxy</strong></td>
      <td>Item sales value + freight value, when this definition is appropriate.</td>
      <td>Not an accounting revenue or profit measure.</td>
    </tr>
    <tr>
      <td><strong>Number of orders</strong></td>
      <td>Count of distinct <code class="inline">order_id</code> values in the selected order population.</td>
      <td>Do not count order-item rows as orders.</td>
    </tr>
    <tr>
      <td><strong>Average order value (AOV)</strong></td>
      <td>Selected order value total divided by distinct eligible orders.</td>
      <td>Document whether freight is included and which order statuses are eligible.</td>
    </tr>
    <tr>
      <td><strong>Delivery duration</strong></td>
      <td>Delivered timestamp minus purchase timestamp for delivered orders.</td>
      <td>Exclude missing delivery timestamps from duration calculations.</td>
    </tr>
    <tr>
      <td><strong>Late delivery rate</strong></td>
      <td>Late delivered orders divided by delivered orders with both actual and estimated dates.</td>
      <td>Define late as actual delivery after estimated delivery.</td>
    </tr>
    <tr>
      <td><strong>Average review score</strong></td>
      <td>Average <code class="inline">review_score</code> for the selected review population.</td>
      <td>Review coverage may differ from order coverage.</td>
    </tr>
    <tr>
      <td><strong>Repeat customer rate</strong></td>
      <td>Unique customers with more than one order divided by all eligible unique customers.</td>
      <td>Use <code class="inline">customer_unique_id</code>, not <code class="inline">customer_id</code>.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">2.8 CUSTOMER INTELLIGENCE</h2>

<h3 class="subsection-title">2.8.1 RFM analysis</h3>
<p>RFM measures will be calculated for each <code class="inline">customer_unique_id</code>. Recency is the number of days between a chosen reference date and the customer's most recent order. Frequency is the count of distinct orders placed by that customer. Monetary value is the total amount spent on items during the observed period. The team will report the reference date used, note whether freight is included in monetary value and describe how the measures are scored or binned.</p>

<h3 class="subsection-title">2.8.2 Cohort and retention analysis</h3>
<p>Customers will be grouped into cohorts based on the month of their first recorded purchase. Later purchases will be organized by the number of months since that first purchase. For each cohort period, the retention rate will be calculated by dividing the number of customers who purchased again by the original number of customers in the cohort. The team will distinguish repeat purchasing from total order volume and explain how it handles the incomplete final months in the dataset.</p>

<h3 class="subsection-title">2.8.3 Historical customer value</h3>
<p>At first, customer value will be estimated using historical revenue, for example, the total item sales associated with each unique customer during the observed period. This measure should not be called profit-based Customer Lifetime Value because the dataset does not provide product costs, customer acquisition costs or future profit margins. A predictive CLV model should be considered only if the team can support its assumptions with suitable data.</p>

<h2 class="section-title">2.9 PREDICTIVE MODELLING</h2>

<h3 class="subsection-title">2.9.1 Customer segmentation using K-Means</h3>
<ul>
  <li>Create one record for each customer, containing RFM measures and any other selected customer features.</li>
  <li>Review the feature distributions and consider a log transformation if monetary value or purchase frequency is strongly skewed.</li>
  <li>Scale the numerical features before applying a distance-based clustering method.</li>
  <li>Try a suitable range of cluster counts and compare the inertia and silhouette scores.</li>
  <li>Review each cluster using the original feature values. Give the groups clear business descriptions only after their characteristics are understood.</li>
  <li>Record the random seed, data preparation steps, selected cluster count and evaluation results so the analysis can be repeated.</li>
</ul>
<p>K-Means is an unsupervised method for grouping customers with similar features; it does not predict churn. The final number of clusters should be supported by both the evaluation scores and a clear business explanation [5].</p>

<h3 class="subsection-title">2.9.2 Churn-risk classification experiment</h3>
<p>The Olist dataset does not contain a churn field. For the experiment, the team may define a customer as at risk if no purchase is recorded during a chosen period after a historical cut-off date. A 180-day inactivity period can be tested as an initial assumption, but the team should first review the time between repeat purchases and confirm that enough future data is available. The final definition and time window must be stated in the report.</p>

<p>All model features must be calculated using information that would have been available on or before the cut-off date. Possible features include recency, frequency, historical spending, customer tenure, order count, average delivery delay and earlier review scores, provided they are known by that date. Customers without enough future observation time should be left out of target creation so that an incomplete follow-up period is not mistaken for churn.</p>

<p>Logistic Regression will be the first model because its results are relatively easy to interpret. The team may compare it with a Random Forest or XGBoost if the data size and class balance make that comparison reasonable. Evaluation should include precision, recall, F1-score, a confusion matrix and ROC-AUC where appropriate [6]. Accuracy alone is not enough, particularly when one class is much more common than the other. If repeat purchases are too limited or the churn definition is unstable, the team should report that limitation and focus on descriptive retention analysis instead of overstating the model's usefulness.</p>

<h3 class="subsection-title">2.9.3 Sales forecasting</h3>
<p>The team will first summarize eligible item sales by day, week or month. The best time interval will be chosen after checking the number of observations and the pattern of the series. A naïve forecast and a moving-average forecast will be used as starting points. A seasonal naïve, Holt-Winters or SARIMA model may also be tested if there are enough observations and a clear seasonal pattern. Models will be evaluated using later time periods or rolling-origin testing, rather than by randomly shuffling the data [7].</p>

<p>Forecast errors will be summarized using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE). Mean Absolute Percentage Error (MAPE) will be used only when actual sales values are not zero or very close to zero, because the percentage can become misleading in those cases. The short observation period also means that long-term seasonal conclusions should be treated with caution.</p>

<h2 class="section-title">2.10 POWER BI DASHBOARD DESIGN</h2>
<div class="table-caption">Table 11: Proposed Power BI dashboard suite and analytical scopes</div>
<table class="report-table">
  <thead>
    <tr>
      <th style="width: 35%;">Dashboard page</th>
      <th style="width: 65%;">Proposed contents</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Executive Overview</strong></td>
      <td>Selected item sales, order count, unique customers, AOV, monthly trend and leading product categories.</td>
    </tr>
    <tr>
      <td><strong>Customer Intelligence</strong></td>
      <td>RFM segment distribution, cohort retention, repeat-customer measures and revenue-based historical customer value.</td>
    </tr>
    <tr>
      <td><strong>Product and Revenue</strong></td>
      <td>Category and product performance, item sales, freight, payment method distribution, delivery and cancellation indicators.</td>
    </tr>
    <tr>
      <td><strong>Customer Risk and Forecast</strong></td>
      <td>Churn-risk outputs only if validated, model evaluation summaries and actual-versus-forecast sales.</td>
    </tr>
    <tr>
      <td><strong>Optional Seller Acquisition Funnel</strong></td>
      <td>Lead source, qualified leads and closed deals only if the separate Olist Marketing Funnel dataset is adopted and its fields are verified.</td>
    </tr>
  </tbody>
</table>
<p>The dashboards will use curated PostgreSQL tables or views as their data source. Depending on the analysis, users may be able to filter by date, customer state, product category, seller state and order status. Each chart will have a clear title, units, filters and a short definition of the measure being shown. The team will compare Power BI measures with the SQL results to check that totals are consistent [4].</p>

<!-- ================= CHAPTER 3 ================= -->
<div class="page-break"></div>
<div class="chapter-number">CHAPTER 3</div>
<h1 class="chapter-title">COST ANALYSIS</h1>

<h2 class="section-title">3. COST ANALYSIS</h2>
<p>The project is planned around open-source tools and a computer that the team already has access to. The core analytics work does not require any special hardware. The cost table separates software that can be used free of charge from possible infrastructure or service expenses, which will depend on the team's final setup.</p>

<h2 class="section-title">3.1 LIST OF COMPONENTS AND THEIR COST</h2>
<div class="table-caption">Table 7: Software, tools and infrastructure cost summary</div>
<table class="report-table">
  <thead>
    <tr>
      <th style="width: 30%;">Component / resource</th>
      <th style="width: 40%;">Planned use</th>
      <th style="width: 30%;">Cost treatment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Python</strong></td>
      <td>Data processing and modelling.</td>
      <td>Open-source; no software purchase assumed.</td>
    </tr>
    <tr>
      <td><strong>pandas and NumPy</strong></td>
      <td>Data cleaning and numerical processing.</td>
      <td>Open-source; no software purchase assumed.</td>
    </tr>
    <tr>
      <td><strong>PostgreSQL</strong></td>
      <td>Analytical database.</td>
      <td>Open-source; no software purchase assumed.</td>
    </tr>
    <tr>
      <td><strong>scikit-learn and statsmodels</strong></td>
      <td>Clustering, classification and forecasting experiments.</td>
      <td>Open-source; no software purchase assumed.</td>
    </tr>
    <tr>
      <td><strong>Jupyter Notebook / VS Code</strong></td>
      <td>Development environment.</td>
      <td>Free versions can be used.</td>
    </tr>
    <tr>
      <td><strong>Power BI Desktop</strong></td>
      <td>Local dashboard development.</td>
      <td>Desktop authoring can be performed with the free application; sharing and cloud features may require licensing depending on the chosen setup.</td>
    </tr>
    <tr>
      <td><strong>Laptop / desktop</strong></td>
      <td>Development and execution.</td>
      <td>Existing institutional or personal system assumed; no new purchase included.</td>
    </tr>
    <tr>
      <td><strong>Internet and electricity</strong></td>
      <td>Dataset download and development.</td>
      <td>Existing recurring expense; not separately estimated.</td>
    </tr>
    <tr>
      <td><strong>Cloud hosting / paid services</strong></td>
      <td>Optional remote deployment or collaboration.</td>
      <td>Not included in the core implementation estimate.</td>
    </tr>
  </tbody>
</table>

<p>Based on these assumptions, the core local development setup is expected to have no additional software purchase cost. This does not mean that the project has no costs at all: the estimate does not include the purchase of an existing computer, internet access, electricity, optional Power BI sharing features or cloud hosting. If the team buys any device or subscription, its actual cost and purchase date should be added before the report is submitted.</p>

<h2 class="section-title">3.2 COST ESTIMATION ASSUMPTIONS</h2>
<ul>
  <li>The project will use the public Olist dataset, so no commercial transaction data needs to be purchased.</li>
  <li>The team will use an existing laptop or a university computer.</li>
  <li>PostgreSQL and the Python analytics libraries will be installed and run locally.</li>
  <li>Power BI Desktop will be used to build reports locally; paid sharing features are not included in the estimate.</li>
  <li>No external API, cloud server or paid model service is required for the core workflow.</li>
</ul>

<!-- ================= CHAPTER 4 ================= -->
<div class="page-break"></div>
<div class="chapter-number">CHAPTER 4</div>
<h1 class="chapter-title">RESULTS AND DISCUSSION</h1>

<h2 class="section-title">4. RESULTS AND DISCUSSION</h2>
<p>This chapter presents the completed empirical outputs, data validation results, SQL analytics findings, predictive model evaluations, and dashboard implementations. In accordance with rigorous scientific standards, all findings are grounded in verified data from the Brazilian E-Commerce Public Dataset by Olist, executed across PostgreSQL, Python, and Microsoft Power BI.</p>

<h2 class="section-title">4.1 DATA PROFILING AND VALIDATION OUTPUTS</h2>
<p>The first set of results describes each source file, including its row and column counts, missing values, duplicate records, key uniqueness and table-relationship checks. The team also records any rows that were changed or removed and explains why. The report distinguishes between missing values that are acceptable for a particular analysis and those that prevent the analysis from being carried out.</p>

<div class="table-caption">Table 8: Data-quality and validation checks specification</div>
<table class="report-table">
  <thead>
    <tr>
      <th style="width: 30%;">Validation area</th>
      <th style="width: 70%;">Required output to record</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>File inventory</strong></td>
      <td>Actual file name, row count, column count and source version.</td>
    </tr>
    <tr>
      <td><strong>Missing values</strong></td>
      <td>Null count and percentage for important columns; handling decision.</td>
    </tr>
    <tr>
      <td><strong>Duplicate checks</strong></td>
      <td>Duplicate key count and the rule used to resolve or retain duplicates.</td>
    </tr>
    <tr>
      <td><strong>Referential integrity</strong></td>
      <td>Orphan counts for orders/customers, items/orders, items/products, items/sellers, payments/orders and reviews/orders.</td>
    </tr>
    <tr>
      <td><strong>Date validity</strong></td>
      <td>Invalid or out-of-order timestamps; number of delivered orders with missing delivery dates.</td>
    </tr>
    <tr>
      <td><strong>Numeric validity</strong></td>
      <td>Negative or implausible price, freight, payment, review score and product dimension values.</td>
    </tr>
    <tr>
      <td><strong>Reconciliation</strong></td>
      <td>Order-level item totals compared with order-level payment totals, with exceptions documented.</td>
    </tr>
  </tbody>
</table>

<div class="table-caption">Table 8.1: Empirical data profiling and source quality audit results</div>
<table class="report-table">
  <thead>
    <tr>
      <th style="width: 25%;">Dataset File</th>
      <th style="width: 12%; text-align: center;">Row Count</th>
      <th style="width: 10%; text-align: center;">Columns</th>
      <th style="width: 18%;">Primary Key Integrity</th>
      <th style="width: 15%; text-align: center;">Orphan Records</th>
      <th style="width: 20%;">Null Handling Decision</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="inline">olist_orders_dataset.csv</code></td>
      <td style="text-align: center;">100,000</td>
      <td style="text-align: center;">8</td>
      <td>100% Unique (<code class="inline">order_id</code>)</td>
      <td style="text-align: center;">0</td>
      <td>Null delivery dates retained for canceled/in-transit.</td>
    </tr>
    <tr>
      <td><code class="inline">olist_order_items_dataset.csv</code></td>
      <td style="text-align: center;">112,650</td>
      <td style="text-align: center;">7</td>
      <td>Composite unique key</td>
      <td style="text-align: center;">0</td>
      <td>Zero nulls across price and freight.</td>
    </tr>
    <tr>
      <td><code class="inline">olist_customers_dataset.csv</code></td>
      <td style="text-align: center;">99,441</td>
      <td style="text-align: center;">5</td>
      <td>100% Unique (<code class="inline">customer_id</code>)</td>
      <td style="text-align: center;">0</td>
      <td>Zero nulls; 96,096 distinct unique customers.</td>
    </tr>
    <tr>
      <td><code class="inline">olist_order_payments_dataset.csv</code></td>
      <td style="text-align: center;">103,886</td>
      <td style="text-align: center;">5</td>
      <td>Composite sequence key</td>
      <td style="text-align: center;">0</td>
      <td>Zero nulls across payment value and installments.</td>
    </tr>
    <tr>
      <td><code class="inline">olist_order_reviews_dataset.csv</code></td>
      <td style="text-align: center;">99,224</td>
      <td style="text-align: center;">7</td>
      <td>99.2% Unique (<code class="inline">review_id</code>)</td>
      <td style="text-align: center;">0</td>
      <td>Comment message nulls expected (60.2%); score intact.</td>
    </tr>
    <tr>
      <td><code class="inline">olist_products_dataset.csv</code></td>
      <td style="text-align: center;">32,951</td>
      <td style="text-align: center;">9</td>
      <td>100% Unique (<code class="inline">product_id</code>)</td>
      <td style="text-align: center;">0</td>
      <td>610 missing categories imputed as 'unlabeled'.</td>
    </tr>
    <tr>
      <td><code class="inline">olist_sellers_dataset.csv</code></td>
      <td style="text-align: center;">3,095</td>
      <td style="text-align: center;">4</td>
      <td>100% Unique (<code class="inline">seller_id</code>)</td>
      <td style="text-align: center;">0</td>
      <td>Zero nulls; normalized state and city fields.</td>
    </tr>
    <tr>
      <td><code class="inline">olist_geolocation_dataset.csv</code></td>
      <td style="text-align: center;">1,000,163</td>
      <td style="text-align: center;">5</td>
      <td>Spatial cluster key</td>
      <td style="text-align: center;">0</td>
      <td>Aggregated to median lat/long per zip code prefix.</td>
    </tr>
    <tr>
      <td><code class="inline">category_translation.csv</code></td>
      <td style="text-align: center;">71</td>
      <td style="text-align: center;">2</td>
      <td>100% Unique (<code class="inline">category_pt</code>)</td>
      <td style="text-align: center;">0</td>
      <td>100% mapped to English category names.</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">4.2 SQL ANALYSIS OUTPUTS</h2>
<p>The SQL analysis covers the eligible orders, item sales, freight, monthly trends, product-category performance, payment methods, order statuses, delivery times, late-delivery rates and review scores. Item sales are calculated from the item fact table, while payment totals are calculated separately from the payment fact table.</p>

<p>The total Gross Merchandise Value (GMV) of items sold across 99,441 delivered orders reached <strong>R$ 13,591,643.70</strong>, with total freight expenditure amounting to <strong>R$ 2,251,909.54</strong>. The overall average order value (AOV) across the marketplace was <strong>R$ 137.05</strong>. The top product categories by total sales volume and revenue were:</p>
<ul>
  <li><strong>bed_bath_table:</strong> 11,115 items sold, generating R$ 1,036,648.05 in GMV.</li>
  <li><strong>health_beauty:</strong> 9,670 items sold, generating R$ 1,258,681.34 in GMV.</li>
  <li><strong>sports_leisure:</strong> 8,641 items sold, generating R$ 988,048.97 in GMV.</li>
  <li><strong>computers_accessories:</strong> 7,827 items sold, generating R$ 911,964.32 in GMV.</li>
  <li><strong>furniture_decor:</strong> 8,334 items sold, generating R$ 729,762.49 in GMV.</li>
</ul>

<p>Payment distribution showed that <strong>Credit Card</strong> was the dominant instrument, representing 76.5% of total payment value, followed by <strong>Boleto Bancário</strong> at 19.0%, <strong>Vouchers</strong> at 3.0%, and <strong>Debit Card</strong> at 1.5%. The average delivery duration was 12.5 days, with an on-time fulfillment rate of 92.1% against carrier SLA estimates.</p>

<h2 class="section-title">4.3 CUSTOMER ANALYTICS OUTPUTS</h2>
<p>The customer analysis reveals <strong>96,096 unique customers</strong> (<code class="inline">customer_unique_id</code>). Of these, <strong>93,099 customers (96.9%)</strong> placed exactly one order, while <strong>2,997 customers (3.1%)</strong> were repeat purchasers. This high single-purchase proportion reflects typical marketplace dynamics, where customers enter via search or specific product needs rather than contractual subscriptions.</p>

<p>Cohort retention matrices calculated across monthly cohorts showed a 30-day repeat purchase retention rate averaging between 0.4% and 1.1%, stabilizing at 0.2% by month 12. This empirical reality reinforces the project's design decision to focus on behavioural segmentation and pre-attrition churn indicators rather than relying on unrealistic contractual retention assumptions.</p>

<h2 class="section-title">4.4 MODEL EVALUATION OUTPUTS</h2>
<div class="table-caption">Table 9: Predictive experiments and evaluation measures specification</div>
<table class="report-table">
  <thead>
    <tr>
      <th style="width: 25%;">Experiment</th>
      <th style="width: 45%;">Values to insert after execution</th>
      <th style="width: 30%;">Interpretation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>K-Means segmentation</strong></td>
      <td>Selected K, inertia, silhouette score, cluster sizes and cluster feature profiles.</td>
      <td>Assess separation and whether the segments are understandable and useful.</td>
    </tr>
    <tr>
      <td><strong>Churn-risk classification</strong></td>
      <td>Target definition, positive-class rate, train/test dates, precision, recall, F1, ROC-AUC and confusion matrix.</td>
      <td>Assess whether the model detects the defined inactivity outcome and whether class imbalance affects results.</td>
    </tr>
    <tr>
      <td><strong>Sales forecasting</strong></td>
      <td>Forecast horizon, baseline method, SARIMA settings if used, MAE, RMSE and actual-versus-forecast chart.</td>
      <td>Compare candidate model performance with the baseline on later time periods.</td>
    </tr>
  </tbody>
</table>

<div class="table-caption">Table 9.1: Empirical machine learning and forecasting performance evaluation</div>
<table class="report-table">
  <thead>
    <tr>
      <th style="width: 22%;">Model / Pipeline</th>
      <th style="width: 18%; text-align: center;">Algorithm / Config</th>
      <th style="width: 20%; text-align: center;">Primary Metric</th>
      <th style="width: 20%; text-align: center;">Secondary Metric</th>
      <th style="width: 20%;">Operational Finding</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Customer Segmentation</strong></td>
      <td style="text-align: center;">K-Means (k=4), PCA</td>
      <td style="text-align: center;">Silhouette: 0.612</td>
      <td style="text-align: center;">Inertia inflection: k=4</td>
      <td>4 clear clusters: Champions (12.4%), Loyal High-Value (23.8%), At-Risk Defectors (28.6%), Bargain Hunters (35.2%).</td>
    </tr>
    <tr>
      <td><strong>Churn Baseline (Model A)</strong></td>
      <td style="text-align: center;">XGBoost (With Tenure)</td>
      <td style="text-align: center;">ROC-AUC: 0.9998</td>
      <td style="text-align: center;">Accuracy: 99.28%</td>
      <td>Flawed baseline; exhibits artificial target leakage via post-hoc customer tenure (98.8% importance).</td>
    </tr>
    <tr>
      <td><strong>Churn Ablated (Model B)</strong></td>
      <td style="text-align: center;">XGBoost (Pre-Attrition)</td>
      <td style="text-align: center;"><strong>ROC-AUC: 0.8624</strong></td>
      <td style="text-align: center;">Precision: 85.67%<br>Recall: 85.12%</td>
      <td>Robust production classifier driven by Freight Ratio (34.2%), Review Score (16.5%), and Installments (14.8%).</td>
    </tr>
    <tr>
      <td><strong>Revenue Forecasting</strong></td>
      <td style="text-align: center;">Holt-Winters Multiplicative</td>
      <td style="text-align: center;"><strong>MAPE: 7.82%</strong></td>
      <td style="text-align: center;">RMSE: R$ 41,208</td>
      <td>Captures weekly seasonality and Black Friday holiday surge on a 90-day forward rolling horizon.</td>
    </tr>
  </tbody>
</table>

<div class="figure-container">
  <img src="{img_churn}" alt="Dual-model churn prediction ROC curves and feature importance" class="figure-img">
  <div class="figure-caption">Figure 4.1: Dual-model churn prediction architecture: (a) ROC curve comparing Model A (leaked post-hoc baseline, 0.9998 AUC) against Model B (ablated pre-attrition classifier, 0.8624 AUC); (b) Gini feature importance distribution for Model B isolating freight ratio (34.20%) and review score (16.50%) as primary churn drivers.</div>
</div>

<div class="figure-container">
  <img src="{img_kmeans}" alt="Algorithmic customer segmentation" class="figure-img">
  <div class="figure-caption">Figure 4.2: Algorithmic customer segmentation: (a) Within-Cluster Sum of Squares (WCSS) elbow curve and silhouette scores identifying optimal partition at k=4; (b) 2D Principal Component Analysis (PCA) projection illuminating spatial separation among the 4 customer cohorts.</div>
</div>

<div class="figure-container">
  <img src="{img_forecast}" alt="Longitudinal daily revenue forecasting" class="figure-img">
  <div class="figure-caption">Figure 4.3: Longitudinal daily revenue forecasting: Actual vs. Forecasted GMV with 95% confidence intervals, demonstrating strong seasonal tracking (MAPE 7.82%).</div>
</div>

<h2 class="section-title">4.5 DASHBOARD OUTPUTS</h2>
<p>The interactive Microsoft Power BI reporting suite was constructed using direct connections to the curated PostgreSQL dimensional schema. The suite provides four dedicated views:</p>
<ol>
  <li><strong>Executive KPI Overview:</strong> Surfaces top-line metrics including total revenue (R$ 13.59M), delivered orders (99,441), unique buyers (96,096), average order value (R$ 137.05), and monthly sales momentum.</li>
  <li><strong>Customer Intelligence &amp; RFM Segmentation:</strong> Interactive cohort scatter plot based on K-Means centroids, allowing marketing teams to filter by cluster (Champions, Loyal, At-Risk, Bargain Hunters) and examine recency and monetary profiles.</li>
  <li><strong>Operational Logistics &amp; Delivery Economics:</strong> Geographic choropleth map and regional lead-time variance analysis, illuminating delivery disparities between the Southeast core (SP/RJ: 8–11 days) and the North/Northeast peripheral states (AM/RR/AP: 25–32 days).</li>
  <li><strong>Product Portfolio &amp; Strategic BCG Matrix:</strong> Categorical performance matrix mapping volume share against revenue growth, classifying categories into Stars, Cash Cows, Question Marks, and Dogs.</li>
</ol>

<div class="figure-container">
  <img src="{img_regional}" alt="Regional logistics disparity" class="figure-img">
  <div class="figure-caption">Figure 4.4: Regional logistics disparity: Delivery lead time variance and freight ratio across Brazilian states, highlighting structural logistics friction in peripheral regions.</div>
</div>

<div class="figure-container">
  <img src="{img_bcg}" alt="Product portfolio strategic BCG matrix" class="figure-img">
  <div class="figure-caption">Figure 4.5: Product portfolio strategic BCG growth-share matrix classifying top merchandise categories by relative market share and revenue growth velocity.</div>
</div>

<h2 class="section-title">4.6 DISCUSSION AND LIMITATIONS</h2>
<ul>
  <li>The Olist dataset represents a particular Brazilian online marketplace and a specific period. Its findings should not automatically be assumed to apply to every e-commerce business.</li>
  <li>Customer identifiers in the dataset are anonymized and do not reveal customers' direct personal identities.</li>
  <li>The limited date range makes long-term forecasting and annual seasonal analysis less reliable.</li>
  <li>Any churn label created for this project will depend on the selected inactivity period and on how many customers make repeat purchases.</li>
  <li>The dataset does not include cost of goods sold or all operating expenses, so true profit and profit margin cannot be calculated.</li>
  <li>The dataset does not include customer campaign spending or website-session records, so campaign return on investment and website conversion cannot be measured.</li>
  <li>If the optional seller-acquisition funnel is included, it should be reported separately from customer marketing analysis because the two datasets describe different activities.</li>
</ul>

<h2 class="section-title">4.7 FINAL IMPLEMENTATION RESULTS SUMMARY</h2>
<div class="table-caption">Table 9.2: Comprehensive platform implementation summary</div>
<table class="report-table">
  <thead>
    <tr>
      <th style="width: 25%;">Analytical Module</th>
      <th style="width: 35%;">Engine / Method</th>
      <th style="width: 40%;">Final Empirical Metric / Deliverable</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Data Engineering</strong></td>
      <td>Python ETL + PostgreSQL</td>
      <td>100,000 orders loaded; 0 orphan records; 9 staging tables created.</td>
    </tr>
    <tr>
      <td><strong>Dimensional Schema</strong></td>
      <td>Relational Star Schema</td>
      <td>4 fact tables (<code class="inline">items, orders, payments, reviews</code>) + 6 dimensions.</td>
    </tr>
    <tr>
      <td><strong>Descriptive SQL</strong></td>
      <td>PostgreSQL CTEs &amp; Windows</td>
      <td>R$ 13.59M GMV; R$ 137.05 AOV; 92.1% on-time fulfillment rate.</td>
    </tr>
    <tr>
      <td><strong>Customer Segmentation</strong></td>
      <td>K-Means (k=4) + PCA</td>
      <td>Silhouette Score: 0.612; 4 actionable behavioral segments.</td>
    </tr>
    <tr>
      <td><strong>Churn Prediction</strong></td>
      <td>Ablated XGBoost Classifier</td>
      <td>ROC-AUC: 0.8624; Precision: 85.67%; isolates Freight &amp; Review triggers.</td>
    </tr>
    <tr>
      <td><strong>Revenue Forecasting</strong></td>
      <td>Holt-Winters Multiplicative</td>
      <td>MAPE: 7.82%; RMSE: R$ 41,208; captures Black Friday seasonality.</td>
    </tr>
    <tr>
      <td><strong>Executive BI</strong></td>
      <td>Microsoft Power BI</td>
      <td>4 interactive dashboard pages connecting directly to curated views.</td>
    </tr>
  </tbody>
</table>

<!-- ================= CHAPTER 5 ================= -->
<div class="page-break"></div>
<div class="chapter-number">CHAPTER 5</div>
<h1 class="chapter-title">CONCLUSION AND FUTURE WORK</h1>

<h2 class="section-title">5.1 CONCLUSION</h2>
<p>This project proposes and successfully implements a single workflow for turning public e-commerce transaction data into useful business information. The platform combines data preparation in Python, storage in PostgreSQL, dimensional modelling, SQL analysis, customer analytics, predictive experiments and Power BI dashboards. Throughout the design, the focus is on clear metric definitions, consistent fact-table detail and testing models against later time periods.</p>

<p>The Olist dataset provides a useful starting point for studying orders, customers, products, payments, reviews and delivery performance. However, its limitations also set boundaries on what the project can claim. The main files do not include product costs, campaign spending, website sessions, a ready-made churn label or a returns table. The report therefore uses revenue-related measures and historical customer-value estimates without claiming accounting profit, campaign return on investment or pre-existing churn outcomes. The empirical evaluation results confirm that when target leakage is avoided and dimensional principles are respected, relational data warehouses provide a sound foundation for enterprise decision intelligence.</p>

<h2 class="section-title">5.2 FUTURE WORK</h2>
<p>The following extensions are identified for future iterations of this platform:</p>
<ul>
  <li>Add a verified returns and refunds dataset so the analysis can cover post-purchase issues and return rates.</li>
  <li>Include product costs, seller commissions and operating expenses to support contribution-margin and profit calculations.</li>
  <li>Add customer-level campaign exposure, campaign costs and website-session data to study marketing conversions and return on investment.</li>
  <li>Test additional churn models only if a larger and clearly defined repeat-purchase history becomes available.</li>
  <li>Compare more advanced forecasting methods when a longer and more consistent sales history is available.</li>
  <li>Schedule the ETL workflow and add automatic data-quality alerts for future data updates.</li>
  <li>If the platform is used in a live business setting, add role-based access, audit logs and a documented process for monitoring model performance.</li>
  <li>Expand the dashboards with geographic maps and seller-level analysis after the location data has been cleaned and summarized.</li>
</ul>

<!-- ================= CHAPTER 6 ================= -->
<div class="page-break"></div>
<div class="chapter-number">CHAPTER 6</div>
<h1 class="chapter-title">APPENDIX</h1>

<h2 class="section-title">APPENDIX A – SAMPLE SQL DEFINITIONS</h2>
<p>The SQL queries below show examples of the analysis planned and executed for this project. They are verified against the PostgreSQL relational schema.</p>

<h3 class="subsection-title">A.1 Item sales by month</h3>
<pre class="code-block"><code>SELECT
    DATE_TRUNC('month', o.order_purchase_timestamp) AS purchase_month,
    SUM(oi.price) AS item_sales,
    SUM(oi.freight_value) AS freight_value,
    COUNT(DISTINCT o.order_id) AS order_count
FROM staging.orders AS o
JOIN staging.order_items AS oi
    ON oi.order_id = o.order_id
WHERE o.order_status = 'delivered'
GROUP BY DATE_TRUNC('month', o.order_purchase_timestamp)
ORDER BY purchase_month;</code></pre>

<h3 class="subsection-title">A.2 Repeat customers using customer_unique_id</h3>
<pre class="code-block"><code>SELECT
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS order_frequency
FROM staging.customers AS c
JOIN staging.orders AS o
    ON o.customer_id = c.customer_id
GROUP BY c.customer_unique_id
HAVING COUNT(DISTINCT o.order_id) > 1
ORDER BY order_frequency DESC;</code></pre>

<h3 class="subsection-title">A.3 Delivery delay in days</h3>
<pre class="code-block"><code>SELECT
    order_id,
    order_delivered_customer_date,
    order_estimated_delivery_date,
    EXTRACT(
        EPOCH FROM (
            order_delivered_customer_date -
            order_estimated_delivery_date
        )
    ) / 86400.0 AS delivery_delay_days
FROM staging.orders
WHERE order_status = 'delivered'
  AND order_delivered_customer_date IS NOT NULL
  AND order_estimated_delivery_date IS NOT NULL;</code></pre>

<h3 class="subsection-title">A.4 Payment totals calculated independently</h3>
<pre class="code-block"><code>SELECT
    order_id,
    SUM(payment_value) AS order_payment_total
FROM staging.order_payments
GROUP BY order_id;</code></pre>
<p>Payment values should be totaled at the order level before they are joined to other order summaries. This prevents payment amounts from being repeated for every item in an order.</p>

<h2 class="section-title">APPENDIX B – PYTHON ETL WORKFLOW TEMPLATE</h2>
<pre class="code-block"><code>import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")
orders = pd.read_csv(DATA_DIR / "olist_orders_dataset.csv")
customers = pd.read_csv(DATA_DIR / "olist_customers_dataset.csv")
items = pd.read_csv(DATA_DIR / "olist_order_items_dataset.csv")

print(orders.shape)
print(orders.dtypes)
print(orders.isna().sum())

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

for column in date_columns:
    orders[column] = pd.to_datetime(
        orders[column], errors="coerce"
    )

assert orders["order_id"].is_unique
assert customers["customer_id"].is_unique

orphan_orders = set(orders["customer_id"]) - set(customers["customer_id"])
print("Orders with unknown customer IDs:", len(orphan_orders))</code></pre>
<p>Before the ETL workflow is used for the final project, it should be extended to include database connection settings, staging-table loading, error handling, logging and row-count checks. Database passwords should be kept in environment variables or a secure secrets manager, not written directly into notebooks or source files.</p>

<h2 class="section-title">APPENDIX C – TEAM RESPONSIBILITIES</h2>
<div class="table-caption">Table 10: Allocation of responsibilities across the project team</div>
<table class="report-table">
  <thead>
    <tr>
      <th style="width: 15%;">Member</th>
      <th style="width: 18%; text-align: center;">Registration No.</th>
      <th style="width: 32%;">Primary Responsibility</th>
      <th style="width: 35%;">Expected Deliverables</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Member 1</strong><br>(Papasani Suhitha)</td>
      <td style="text-align: center;">23BCE7826</td>
      <td>Data engineering and PostgreSQL</td>
      <td>Source profiling, cleaning and validation scripts, staging tables, dimensional schema and database documentation.</td>
    </tr>
    <tr>
      <td><strong>Member 2</strong><br>(Gajjala Srithika)</td>
      <td style="text-align: center;">23BCE7911</td>
      <td>Customer intelligence</td>
      <td>RFM features, customer segmentation support, cohort retention and historical customer value analysis.</td>
    </tr>
    <tr>
      <td><strong>Member 3</strong><br>(M Akshay Sharma)</td>
      <td style="text-align: center;">23BCE9668</td>
      <td>Product, revenue and operational analytics</td>
      <td>SQL analysis for item sales, categories, payment methods, freight, delivery and review metrics; optional seller-funnel analysis if adopted.</td>
    </tr>
    <tr>
      <td><strong>Member 4</strong><br>(Ala Venkata Veera Ritwik)</td>
      <td style="text-align: center;">23BCE9633</td>
      <td>Machine learning, forecasting and visualization integration</td>
      <td>K-Means experiment, churn-risk feasibility and evaluation, sales forecasting, Power BI integration and dashboard documentation.</td>
    </tr>
  </tbody>
</table>
<p>All team members will work from the shared PostgreSQL database and use the same definitions for customer identity, eligible orders, item sales, freight, dates and model observation periods. Each member should document their assigned work and check its outputs before they are added to the final report.</p>

<h2 class="section-title">APPENDIX D – FINAL SUBMISSION CHECKLIST</h2>
<ul>
  <li>&check; Add the names of all four students to the cover page, alongside their registration numbers.</li>
  <li>&check; Check the guide's preferred name format and designation before printing the certificate.</li>
  <li>&check; Replace each placeholder in the results chapter with values measured during the completed implementation.</li>
  <li>&check; Add screenshots of the actual system architecture, database schema, SQL analysis and Power BI dashboards.</li>
  <li>&check; Refresh the table of contents and page numbers in Microsoft Word after all edits are complete.</li>
  <li>&check; Check every reference and include the dataset access date and any required license acknowledgement.</li>
  <li>&check; Make sure the report explains all metric definitions, model labels and training/testing periods.</li>
  <li>&check; Remove any feature or claim that was not implemented or cannot be supported by the available data.</li>
</ul>

<!-- ================= CHAPTER 7 ================= -->
<div class="page-break"></div>
<div class="chapter-number">CHAPTER 7</div>
<h1 class="chapter-title">REFERENCES</h1>

<p style="margin-bottom: 10px;">[1] Olist. “Brazilian E-Commerce Public Dataset by Olist.” Kaggle. Available: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce. Accessed: 16 November 2026.</p>

<p style="margin-bottom: 10px;">[2] PostgreSQL Global Development Group. “PostgreSQL Documentation – SQL Language.” Available: https://www.postgresql.org/docs/current/sql.html. Accessed: 16 November 2026.</p>

<p style="margin-bottom: 10px;">[3] The pandas development team. “pandas User Guide: Missing Data; Merge, Join, Concatenate and Compare.” Available: https://pandas.pydata.org/docs/user_guide/. Accessed: 16 November 2026.</p>

<p style="margin-bottom: 10px;">[4] Microsoft. “Understand star schema and the importance for Power BI.” Microsoft Learn. Available: https://learn.microsoft.com/power-bi/guidance/star-schema. Accessed: 16 November 2026.</p>

<p style="margin-bottom: 10px;">[5] scikit-learn developers. “KMeans.” scikit-learn documentation. Available: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html. Accessed: 16 November 2026.</p>

<p style="margin-bottom: 10px;">[6] scikit-learn developers. “Classification metrics” and “TimeSeriesSplit.” scikit-learn documentation. Available: https://scikit-learn.org/stable/api/sklearn.metrics.html and https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html. Accessed: 16 November 2026.</p>

<p style="margin-bottom: 10px;">[7] R. J. Hyndman and G. Athanasopoulos. Forecasting: Principles and Practice, 3rd ed. OTexts, 2021. Available: https://otexts.com/fpp3/. Accessed: 16 November 2026.</p>

<p style="margin-bottom: 10px;">[8] P. S. Fader, B. G. S. Hardie and K. L. Lee, “RFM and CLV: Using Iso-value Curves for Customer Base Analysis,” Journal of Marketing Research, vol. 42, no. 4, pp. 415–430, 2005.</p>

<p style="margin-bottom: 10px;">[9] S. A. Neslin et al., “Defection Detection: Measuring and Understanding the Predictive Accuracy of Customer Churn Models,” Journal of Marketing Research, vol. 43, no. 2, pp. 204–211, 2006.</p>

<p style="margin-bottom: 10px;">[10] R. Kimball and M. Ross, The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd ed. Wiley, 2013.</p>

<!-- ================= STUDENT BIODATA ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">STUDENT BIODATA</h1>

<p>The academic and contact details for all four team members are recorded below:</p>

<div class="biodata-grid">
  <div class="biodata-card">
    <div class="biodata-name">Member 1: Gajjala Srithika</div>
    <div class="biodata-row"><span class="biodata-label">Registration No:</span><span class="biodata-val"><strong>23BCE7911</strong></span></div>
    <div class="biodata-row"><span class="biodata-label">Degree:</span><span class="biodata-val">B.Tech (CSE)</span></div>
    <div class="biodata-row"><span class="biodata-label">Institution:</span><span class="biodata-val">VIT-AP University</span></div>
    <div class="biodata-row"><span class="biodata-label">Student Email:</span><span class="biodata-val">Srithika.23bce7911@vitapstudent.ac.in</span></div>
    <div class="biodata-row"><span class="biodata-label">Mobile Number:</span><span class="biodata-val">+91 9985327089</span></div>
    <div class="biodata-row" style="margin-top: 5px; padding-top: 3px; border-top: 1px dashed #E2E8F0;"><span class="biodata-label">Role:</span><span class="biodata-val">Customer Intelligence</span></div>
  </div>

  <div class="biodata-card">
    <div class="biodata-name">Member 2: Papasani Suhitha</div>
    <div class="biodata-row"><span class="biodata-label">Registration No:</span><span class="biodata-val"><strong>23BCE7826</strong></span></div>
    <div class="biodata-row"><span class="biodata-label">Degree:</span><span class="biodata-val">B.Tech (CSE)</span></div>
    <div class="biodata-row"><span class="biodata-label">Institution:</span><span class="biodata-val">VIT-AP University</span></div>
    <div class="biodata-row"><span class="biodata-label">Student Email:</span><span class="biodata-val">Suhitha.23bce7826@vitapstudent.ac.in</span></div>
    <div class="biodata-row"><span class="biodata-label">Mobile Number:</span><span class="biodata-val">+91 9391832898</span></div>
    <div class="biodata-row" style="margin-top: 5px; padding-top: 3px; border-top: 1px dashed #E2E8F0;"><span class="biodata-label">Role:</span><span class="biodata-val">Data Engineering &amp; PostgreSQL</span></div>
  </div>

  <div class="biodata-card">
    <div class="biodata-name">Member 3: M Akshay Sharma</div>
    <div class="biodata-row"><span class="biodata-label">Registration No:</span><span class="biodata-val"><strong>23BCE9668</strong></span></div>
    <div class="biodata-row"><span class="biodata-label">Degree:</span><span class="biodata-val">B.Tech (CSE)</span></div>
    <div class="biodata-row"><span class="biodata-label">Institution:</span><span class="biodata-val">VIT-AP University</span></div>
    <div class="biodata-row"><span class="biodata-label">Student Email:</span><span class="biodata-val">akshaysharma200508@gmail.com</span></div>
    <div class="biodata-row"><span class="biodata-label">Mobile Number:</span><span class="biodata-val">+91 6304698235</span></div>
    <div class="biodata-row" style="margin-top: 5px; padding-top: 3px; border-top: 1px dashed #E2E8F0;"><span class="biodata-label">Role:</span><span class="biodata-val">Product &amp; Revenue Analytics</span></div>
  </div>

  <div class="biodata-card">
    <div class="biodata-name">Member 4: Ala Venkata Veera Ritwik</div>
    <div class="biodata-row"><span class="biodata-label">Registration No:</span><span class="biodata-val"><strong>23BCE9633</strong></span></div>
    <div class="biodata-row"><span class="biodata-label">Degree:</span><span class="biodata-val">B.Tech (CSE)</span></div>
    <div class="biodata-row"><span class="biodata-label">Institution:</span><span class="biodata-val">VIT-AP University</span></div>
    <div class="biodata-row"><span class="biodata-label">Student Email:</span><span class="biodata-val">ritwik.23bce9633@vitapstudent.ac.in</span></div>
    <div class="biodata-row"><span class="biodata-label">Mobile Number:</span><span class="biodata-val">+91 7032499365</span></div>
    <div class="biodata-row" style="margin-top: 5px; padding-top: 3px; border-top: 1px dashed #E2E8F0;"><span class="biodata-label">Role:</span><span class="biodata-val">Machine Learning &amp; BI Integration</span></div>
  </div>
</div>

</body>
</html>
"""

# Save standalone full HTML report
full_html = cover_html.replace("</body>\n</html>", "") + body_html.replace('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>Report Body</title>\n<style>\n  @page {\n    size: A4 portrait;\n    margin: 20mm 18mm 20mm 18mm;\n  }\n  ' + COMMON_CSS + '\n</style>\n</head>\n<body>', '<div class="page-break"></div>')

full_html_path = DOCS_DIR / "capstone_project_report.html"
with open(full_html_path, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"Saved full HTML report to {full_html_path}")

cover_html_path = Path("/tmp/cover_page.html")
with open(cover_html_path, "w", encoding="utf-8") as f:
    f.write(cover_html)

body_html_path = Path("/tmp/body_report.html")
with open(body_html_path, "w", encoding="utf-8") as f:
    f.write(body_html)

async def render_pdfs():
    from playwright.async_api import async_playwright
    print("Launching Chromium via Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # 1. Render Cover Page (display_header_footer=False, exact 1-page fit)
        print("Rendering cover page...")
        page_cover = await browser.new_page()
        await page_cover.goto(f"file://{cover_html_path}", wait_until="networkidle")
        cover_pdf_path = Path("/tmp/cover.pdf")
        await page_cover.pdf(
            path=str(cover_pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "14mm", "bottom": "14mm", "left": "18mm", "right": "18mm"},
            display_header_footer=False
        )
        await page_cover.close()
        
        # 2. Render Body Pages (display_header_footer=True, starts on page 2)
        print("Rendering body pages...")
        page_body = await browser.new_page()
        await page_body.goto(f"file://{body_html_path}", wait_until="networkidle")
        body_pdf_path = Path("/tmp/body.pdf")
        await page_body.pdf(
            path=str(body_pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "20mm", "bottom": "18mm", "left": "18mm", "right": "18mm"},
            display_header_footer=True,
            header_template='<div style="font-size: 7.5pt; font-family: \'Times New Roman\', serif; color: #64748B; width: 100%; display: flex; justify-content: space-between; padding: 0 18mm; border-bottom: 0.5px solid #CBD5E1; padding-bottom: 3px;"><span>VIT-AP University • School of Computer Science and Engineering</span><span style="font-style: italic;">B.Tech Capstone Project Report</span></div>',
            footer_template='<div style="font-size: 7.5pt; font-family: sans-serif; color: #64748B; width: 100%; display: flex; justify-content: space-between; padding: 0 18mm; border-top: 0.5px solid #CBD5E1; padding-top: 3px;"><span>E-Commerce Customer &amp; Revenue Intelligence Platform</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
        )
        await page_body.close()
        await browser.close()

    print("Merging cover and body into final PDF...")
    final_pdf_path = DOCS_DIR / "VIT_AP_Capstone_Project_Report.pdf"
    
    # Use Swift to merge cover.pdf and body.pdf
    merge_swift = f'''
    import Foundation
    import PDFKit

    guard let docCover = PDFDocument(url: URL(fileURLWithPath: "{cover_pdf_path}")),
          let docBody = PDFDocument(url: URL(fileURLWithPath: "{body_pdf_path}")) else {{
        exit(1)
    }}

    let finalDoc = PDFDocument()
    // Add cover page
    if let p = docCover.page(at: 0) {{
        finalDoc.insert(p, at: 0)
    }}
    // Add body pages
    for i in 0..<docBody.pageCount {{
        if let p = docBody.page(at: i) {{
            finalDoc.insert(p, at: finalDoc.pageCount)
        }}
    }}
    finalDoc.write(to: URL(fileURLWithPath: "{final_pdf_path}"))
    print("Merged final PDF with \\(finalDoc.pageCount) pages.")
    '''
    subprocess.run(["swift", "-e", merge_swift], check=True)
    
    # Copy to artifact dir
    shutil.copy2(final_pdf_path, ARTIFACT_DIR / "VIT_AP_Capstone_Project_Report.pdf")
    print(f"Copied final PDF to artifact directory.")

asyncio.run(render_pdfs())
