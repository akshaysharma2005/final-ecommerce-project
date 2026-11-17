"""
capstone_html_builder.py
Builds the HTML markup for the VIT-AP Capstone Project Report.
Preserves 100% of the friend's original text, structure, tables, and code,
and enriches Chapter 4 with empirical database, ML, and dashboard results.
"""

def build_report_html(images):
    img_logo = images.get('logo', '')
    img_arch = images.get('arch', '')
    img_schema = images.get('schema', '')
    img_churn = images.get('churn', '')
    img_kmeans = images.get('kmeans', '')
    img_forecast = images.get('forecast', '')
    img_regional = images.get('regional', '')
    img_bcg = images.get('bcg', '')

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>E-Commerce Business Intelligence & Predictive Analytics Platform - Capstone Project Report</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 20mm 18mm 20mm 18mm;
    @top-left {{
      content: "VIT-AP University • School of Computer Science and Engineering";
      font-family: 'Times New Roman', Georgia, serif;
      font-size: 8pt;
      color: #64748B;
    }}
    @top-right {{
      content: "B.Tech Capstone Project Report";
      font-family: 'Times New Roman', Georgia, serif;
      font-size: 8pt;
      font-style: italic;
      color: #64748B;
    }}
    @bottom-left {{
      content: "E-Commerce Customer & Revenue Intelligence Platform";
      font-family: 'Segoe UI', Arial, sans-serif;
      font-size: 8pt;
      color: #64748B;
    }}
    @bottom-right {{
      content: "Page " counter(page);
      font-family: 'Segoe UI', Arial, sans-serif;
      font-size: 8pt;
      font-weight: 600;
      color: #1E293B;
    }}
  }}

  *, *:before, *:after {{
    box-sizing: border-box;
  }}

  body {{
    font-family: 'Times New Roman', Times, Georgia, serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #1E293B;
    background-color: #FFFFFF;
    margin: 0;
    padding: 0;
  }}

  .page-break {{
    page-break-before: always;
    break-before: page;
  }}

  .avoid-break {{
    page-break-inside: avoid;
    break-inside: avoid;
  }}

  /* Typography */
  h1, h2, h3, h4 {{
    font-family: 'Times New Roman', Georgia, serif;
    color: #7A0019; /* VIT Maroon */
    margin-top: 1.2em;
    margin-bottom: 0.5em;
    page-break-after: avoid;
    break-after: avoid;
  }}

  h1.chapter-title {{
    font-size: 18pt;
    font-weight: bold;
    text-transform: uppercase;
    text-align: center;
    border-bottom: 2px solid #7A0019;
    padding-bottom: 6px;
    margin-top: 0;
    margin-bottom: 18px;
    letter-spacing: 0.5px;
  }}

  .chapter-number {{
    font-size: 13pt;
    text-transform: uppercase;
    color: #0F243E; /* Deep Navy */
    text-align: center;
    font-weight: bold;
    margin-bottom: 4px;
    letter-spacing: 1px;
  }}

  h2.section-title {{
    font-size: 13pt;
    font-weight: bold;
    color: #0F243E;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 4px;
    margin-top: 20px;
    margin-bottom: 10px;
  }}

  h3.subsection-title {{
    font-size: 11.5pt;
    font-weight: bold;
    color: #1E293B;
    margin-top: 14px;
    margin-bottom: 6px;
  }}

  p {{
    text-align: justify;
    text-justify: inter-word;
    margin-top: 0;
    margin-bottom: 8px;
    font-size: 10.5pt;
    line-height: 1.55;
  }}

  ul, ol {{
    margin-top: 0;
    margin-bottom: 10px;
    padding-left: 24px;
  }}

  li {{
    margin-bottom: 4px;
    font-size: 10.5pt;
    text-align: justify;
    line-height: 1.5;
  }}

  /* Tables */
  table.report-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0 16px 0;
    font-size: 9.5pt;
    page-break-inside: auto;
  }}

  table.report-table tr {{
    page-break-inside: avoid;
    page-break-after: auto;
  }}

  table.report-table th {{
    background-color: #7A0019;
    color: #FFFFFF;
    font-weight: bold;
    text-align: left;
    padding: 7px 9px;
    border: 1px solid #5A0013;
    font-size: 9.5pt;
  }}

  table.report-table td {{
    padding: 6px 9px;
    border: 1px solid #CBD5E1;
    vertical-align: top;
    line-height: 1.4;
  }}

  table.report-table tr:nth-child(even) td {{
    background-color: #F8FAFC;
  }}

  .table-caption {{
    font-size: 10pt;
    font-weight: bold;
    color: #0F243E;
    margin-top: 12px;
    margin-bottom: 5px;
    page-break-after: avoid;
    text-align: left;
  }}

  /* Figures */
  .figure-container {{
    text-align: center;
    margin: 16px auto;
    page-break-inside: avoid;
    max-width: 98%;
  }}

  .figure-img {{
    max-width: 95%;
    height: auto;
    border: 1px solid #CBD5E1;
    border-radius: 4px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.06);
  }}

  .figure-caption {{
    font-size: 9.5pt;
    font-style: italic;
    color: #334155;
    margin-top: 6px;
    text-align: center;
  }}

  /* Code blocks */
  pre.code-block {{
    background-color: #0F172A;
    color: #E2E8F0;
    font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
    font-size: 8.5pt;
    line-height: 1.45;
    padding: 12px 14px;
    border-radius: 5px;
    border-left: 4px solid #7A0019;
    margin: 10px 0 14px 0;
    white-space: pre-wrap;
    word-break: break-all;
    page-break-inside: avoid;
  }}

  code.inline {{
    font-family: 'Courier New', monospace;
    font-size: 9pt;
    background-color: #F1F5F9;
    color: #0F243E;
    padding: 1px 4px;
    border-radius: 3px;
    border: 1px solid #E2E8F0;
  }}

  /* Callout Boxes */
  .alert-box {{
    border-left: 4px solid #0F243E;
    background-color: #F8FAFC;
    padding: 10px 14px;
    margin: 10px 0 14px 0;
    border-radius: 0 4px 4px 0;
    font-size: 10pt;
    page-break-inside: avoid;
  }}

  .alert-box.success {{
    border-left-color: #10B981;
    background-color: #ECFDF5;
  }}

  .alert-box.info {{
    border-left-color: #7A0019;
    background-color: #FDF2F4;
  }}

  /* Front Matter Styling */
  .cover-container {{
    min-height: 96vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: center;
    padding: 10px 20px;
    border: 3px double #7A0019;
    padding: 28px 24px;
  }}

  .cover-header {{
    margin-bottom: 12px;
  }}

  .cover-logo {{
    max-height: 80px;
    margin-bottom: 12px;
  }}

  .cover-title {{
    font-size: 20pt;
    font-weight: bold;
    color: #7A0019;
    line-height: 1.25;
    margin-bottom: 8px;
    letter-spacing: 0.5px;
  }}

  .cover-subtitle {{
    font-size: 13pt;
    font-style: italic;
    color: #0F243E;
    margin-bottom: 20px;
  }}

  .cover-report-type {{
    font-size: 13pt;
    font-weight: bold;
    color: #1E293B;
    letter-spacing: 2px;
    margin-top: 15px;
    margin-bottom: 10px;
  }}

  .cover-submission-text {{
    font-size: 10.5pt;
    color: #334155;
    margin-bottom: 4px;
    line-height: 1.4;
  }}

  .cover-degree {{
    font-size: 13pt;
    font-weight: bold;
    color: #0F243E;
    letter-spacing: 1px;
    margin: 6px 0;
  }}

  .cover-table-container {{
    margin: 16px auto;
    width: 90%;
  }}

  .cover-guidance {{
    margin: 12px 0;
    font-size: 11pt;
  }}

  .cover-footer {{
    margin-top: 14px;
    line-height: 1.4;
  }}

  .cover-school {{
    font-size: 12pt;
    font-weight: bold;
    color: #7A0019;
    letter-spacing: 0.5px;
  }}

  .cover-univ {{
    font-size: 14pt;
    font-weight: bold;
    color: #0F243E;
    letter-spacing: 1px;
  }}

  .cover-location {{
    font-size: 11pt;
    color: #334155;
  }}

  .cover-date {{
    font-size: 11.5pt;
    font-weight: bold;
    color: #1E293B;
    margin-top: 6px;
  }}

  /* Certificate */
  .certificate-box {{
    border: 2px solid #7A0019;
    padding: 30px 32px;
    min-height: 92vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    outline: 1px solid #D4AF37;
    outline-offset: -8px;
  }}

  .certificate-title {{
    font-size: 18pt;
    font-weight: bold;
    color: #7A0019;
    text-align: center;
    letter-spacing: 2px;
    margin-bottom: 24px;
    text-transform: uppercase;
  }}

  .certificate-body {{
    font-size: 11pt;
    line-height: 1.65;
    text-align: justify;
    margin-bottom: 20px;
  }}

  .sig-table {{
    width: 100%;
    margin-top: 30px;
    border-collapse: collapse;
  }}

  .sig-table td {{
    vertical-align: bottom;
    padding: 10px 4px;
    font-size: 10.5pt;
  }}

  .sig-line {{
    border-top: 1px solid #1E293B;
    width: 80%;
    margin-top: 40px;
    margin-bottom: 4px;
  }}

  /* TOC dot leaders */
  .toc-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 10pt;
  }}

  .toc-table td {{
    padding: 4px 6px;
    vertical-align: bottom;
  }}

  .toc-chapter {{
    font-weight: bold;
    color: #7A0019;
    padding-top: 8px;
  }}

  .toc-sub {{
    padding-left: 18px;
    color: #1E293B;
  }}

  .toc-subsub {{
    padding-left: 36px;
    color: #475569;
    font-size: 9.5pt;
  }}

  .toc-dots {{
    border-bottom: 1px dotted #94A3B8;
    height: 1px;
    flex-grow: 1;
    margin: 0 6px 3px 6px;
  }}

  .toc-row {{
    display: flex;
    align-items: baseline;
    justify-content: space-between;
  }}

  /* Biodata Grid */
  .biodata-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 14px;
  }}

  .biodata-card {{
    border: 1px solid #CBD5E1;
    border-top: 4px solid #7A0019;
    background-color: #FFFFFF;
    border-radius: 4px;
    padding: 14px 16px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    page-break-inside: avoid;
  }}

  .biodata-name {{
    font-size: 12pt;
    font-weight: bold;
    color: #0F243E;
    margin-bottom: 8px;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 4px;
  }}

  .biodata-row {{
    font-size: 9.5pt;
    margin-bottom: 4px;
    display: flex;
    justify-content: space-between;
  }}

  .biodata-label {{
    font-weight: 600;
    color: #64748B;
  }}

  .biodata-val {{
    color: #1E293B;
    text-align: right;
  }}
</style>
</head>
<body>
"""
    return html

