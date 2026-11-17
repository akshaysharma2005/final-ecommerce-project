#!/usr/bin/env python3
"""
generate_capstone_report.py
Generates the comprehensive, publication-grade Capstone Project Report for VIT-AP University.
Outputs:
1. docs/capstone_project_report.html (Self-contained HTML report with embedded base64 figures)
2. docs/VIT_AP_Capstone_Project_Report.pdf (Official printable PDF rendered via Playwright)
3. docs/capstone_project_report.md (Clean markdown version)
4. docs/VIT_AP_Capstone_Project_Report.docx (Word DOCX document)
"""

import os
import sys
import base64
import asyncio
from pathlib import Path

# Paths
WORKSPACE = Path("/Users/makshaysharma/Desktop/ecommerce-intelligence")
DOCS_DIR = WORKSPACE / "docs"
ASSETS_DIR = WORKSPACE / "report_assets"
FIGURES_DIR = WORKSPACE / "paper" / "figures"
ARTIFACT_DIR = Path("/Users/makshaysharma/.gemini/antigravity/brain/2ff68dc2-9f13-45a4-b203-0adb4a579794")

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

print("Encoding images to base64...")
IMG_LOGO = encode_img(ASSETS_DIR / "image1.jpeg")
IMG_ARCH = encode_img(ASSETS_DIR / "image2.png")
IMG_SCHEMA = encode_img(ASSETS_DIR / "image3.png")
IMG_CHURN = encode_img(FIGURES_DIR / "fig3_churn_roc_feature_importance.png")
IMG_KMEANS = encode_img(FIGURES_DIR / "fig4_kmeans_pca_elbow.png")
IMG_FORECAST = encode_img(FIGURES_DIR / "fig5_revenue_forecasting.png")
IMG_REGIONAL = encode_img(FIGURES_DIR / "fig6_regional_economics.png")
IMG_BCG = encode_img(FIGURES_DIR / "fig7_category_bcg_matrix.png")
print("Images encoded successfully.")

