import os
import shutil
from playwright.sync_api import sync_playwright

project_dir = "/Users/makshaysharma/Desktop/ecommerce-intelligence"
fig_dir = os.path.join(project_dir, "paper", "figures")

with open(os.path.join(project_dir, "scripts", "paper_template.html"), "r", encoding="utf-8") as f:
    html_content = f.read()

html_content = html_content.replace("__FIG_DIR__", fig_dir)

html_path = os.path.join(project_dir, "paper", "ieee_research_paper.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

pdf_output_path = os.path.join(project_dir, "paper", "IEEE_Research_Paper_NEXUS_AI.pdf")
docs_pdf_path = os.path.join(project_dir, "docs", "IEEE_Research_Paper_NEXUS_AI.pdf")
artifact_pdf_path = "/Users/makshaysharma/.gemini/antigravity/brain/2ff68dc2-9f13-45a4-b203-0adb4a579794/IEEE_Research_Paper_NEXUS_AI.pdf"

print("Compiling full multi-page PDF via Playwright...")
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file://{html_path}")
    page.wait_for_load_state("networkidle")
    page.pdf(
        path=pdf_output_path,
        format="Letter",
        scale=0.86,
        print_background=True,
        margin={"top": "0.70in", "bottom": "0.70in", "left": "0.55in", "right": "0.55in"},
        display_header_footer=True,
        header_template='<div style="font-size: 8pt; font-family: Times New Roman, serif; width: 100%; text-align: center; color: #555; padding-top: 5px;">IEEE B.Tech Capstone Conference Paper &mdash; SCOPE, VIT-AP University, Fall 2026&ndash;27</div>',
        footer_template='<div style="font-size: 8pt; font-family: Times New Roman, serif; width: 100%; display: flex; justify-content: space-between; padding-left: 0.55in; padding-right: 0.55in; color: #444; padding-bottom: 5px;"><span style="color: #666;">NEXUS.AI: Enterprise E-Commerce Customer &amp; Revenue Intelligence Platform</span><span style="font-weight: bold;">Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
    )
    browser.close()

shutil.copyfile(pdf_output_path, docs_pdf_path)
shutil.copyfile(pdf_output_path, artifact_pdf_path)
print(f"PDF successfully written to: {pdf_output_path}, {docs_pdf_path}, and {artifact_pdf_path}")
print(f"File size: {os.path.getsize(pdf_output_path)} bytes")
