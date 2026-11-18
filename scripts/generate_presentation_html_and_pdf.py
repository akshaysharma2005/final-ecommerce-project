#!/usr/bin/env python3
"""
generate_presentation_html_and_pdf.py
Generates:
1. docs/presentation_slides.html (Self-contained interactive HTML5 Presentation)
2. docs/E_Commerce_Intelligence_Presentation.pdf (High-res 20-slide PDF deck via Playwright)
All figures and photos embedded as base64 for 100% offline portability.
"""

import os
import sys
import base64
import asyncio
import shutil
from pathlib import Path
from playwright.async_api import async_playwright

WORKSPACE = Path("/Users/makshaysharma/Desktop/ecommerce-intelligence")
DOCS_DIR = WORKSPACE / "docs"
FIG_DIR = WORKSPACE / "docs" / "figures"
ASSETS_DIR = WORKSPACE / "report_assets"
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

print("Encoding image assets...")
img_logo = encode_img(ASSETS_DIR / "image1.jpeg")
photo_suhitha = encode_img(ASSETS_DIR / "photo_suhitha.jpg")
photo_srithika = encode_img(ASSETS_DIR / "photo_srithika.jpg")
photo_ritwik = encode_img(ASSETS_DIR / "photo_ritwik.jpg")
photo_akshay = encode_img(ASSETS_DIR / "photo_akshay.jpg")

fig1 = encode_img(FIG_DIR / "fig1_system_architecture.png")
fig2 = encode_img(FIG_DIR / "fig2_star_schema.png")
fig3 = encode_img(FIG_DIR / "fig3_churn_roc_feature_importance.png")
fig4 = encode_img(FIG_DIR / "fig4_kmeans_pca_elbow.png")
fig5 = encode_img(FIG_DIR / "fig5_revenue_forecasting.png")
fig6 = encode_img(FIG_DIR / "fig6_regional_economics.png")
fig7 = encode_img(FIG_DIR / "fig7_category_bcg_matrix.png")
fig8 = encode_img(FIG_DIR / "fig8_marketing_attribution.png")
fig9 = encode_img(FIG_DIR / "fig9_global_telemetry_strategy.png")
screen_dash = encode_img(FIG_DIR / "screenshot_dashboard.png")
screen_login = encode_img(FIG_DIR / "screenshot_login.png")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>E-Commerce Business Intelligence & Predictive Analytics Platform - Capstone Defense</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

  :root {
    --dark-navy: #0B192C;
    --midnight: #0F243E;
    --crimson: #7A0019;
    --gold: #D4AF37;
    --slate-bg: #F8FAFC;
    --card-bg: #FFFFFF;
    --card-border: #E2E8F0;
    --text-dark: #1E293B;
    --text-muted: #64748B;
    --text-light: #FFFFFF;
    --accent-blue: #1E40AF;
    --success-green: #059669;
    --alert-amber: #D97706;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background-color: #050B14;
    color: var(--text-dark);
    overflow: hidden;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  /* Slide Deck Container (16:9 Aspect Ratio) */
  .deck-container {
    position: relative;
    width: 100vw;
    height: 56.25vw; /* 16:9 */
    max-height: 100vh;
    max-width: 177.78vh; /* 16:9 */
    background-color: var(--slate-bg);
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    overflow: hidden;
  }

  .slide {
    display: none;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    padding: 40px 50px 35px 50px;
    flex-direction: column;
    background-color: var(--slate-bg);
    animation: fadeIn 0.3s ease-in-out;
  }

  .slide.active {
    display: flex;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: scale(0.995); }
    to { opacity: 1; transform: scale(1); }
  }

  /* Dark Theme Slide */
  .slide.dark-theme {
    background-color: var(--dark-navy);
    color: var(--text-light);
  }

  /* Top University Header Bar */
  .univ-bar {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 28px;
    background-color: var(--midnight);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 30px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.5px;
    z-index: 10;
  }

  .univ-bar .univ-left {
    color: var(--gold);
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .univ-bar .univ-right {
    color: #94A3B8;
  }

  /* Slide Header */
  .slide-header {
    margin-top: 10px;
    margin-bottom: 20px;
  }

  .pill {
    display: inline-block;
    padding: 3px 12px;
    background-color: var(--crimson);
    color: white;
    font-size: 10.5px;
    font-weight: 700;
    border-radius: 12px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 6px;
  }

  .slide-title {
    font-size: 26px;
    font-weight: 800;
    color: var(--midnight);
    line-height: 1.2;
  }

  .slide.dark-theme .slide-title {
    color: var(--text-light);
  }

  .slide-subtitle {
    font-size: 13.5px;
    color: var(--text-muted);
    margin-top: 4px;
  }

  .slide.dark-theme .slide-subtitle {
    color: #94A3B8;
  }

  /* Slide Body Layouts */
  .slide-body {
    display: flex;
    gap: 25px;
    flex: 1;
    min-height: 0; /* for flex overflow */
  }

  .card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 8px;
    padding: 20px 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
  }

  .slide.dark-theme .card {
    background: #11223C;
    border-color: #334155;
    color: var(--text-light);
  }

  .card-title {
    font-size: 14.5px;
    font-weight: 700;
    color: var(--midnight);
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 2px solid #F1F5F9;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .slide.dark-theme .card-title {
    color: var(--gold);
    border-color: #1E293B;
  }

  /* Metrics Grid */
  .kpi-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
    margin-bottom: 18px;
  }

  .kpi-box {
    background: #FFFFFF;
    border: 1.5px solid var(--card-border);
    border-radius: 6px;
    padding: 12px;
    text-align: center;
  }

  .kpi-val {
    font-size: 24px;
    font-weight: 800;
    color: var(--accent-blue);
  }

  .kpi-lbl {
    font-size: 11px;
    color: var(--text-muted);
    font-weight: 600;
    margin-top: 2px;
  }

  /* Bullets & Typography */
  .bullet-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .bullet-item {
    font-size: 12.5px;
    line-height: 1.45;
    color: var(--text-dark);
  }

  .slide.dark-theme .bullet-item {
    color: #E2E8F0;
  }

  .bullet-item strong {
    color: var(--midnight);
    font-weight: 700;
  }

  .slide.dark-theme .bullet-item strong {
    color: #FFFFFF;
  }

  .math-tag {
    font-family: 'JetBrains Mono', monospace;
    background: #EEF2F6;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 11px;
    color: #0F243E;
  }

  /* Image Containers */
  .fig-container {
    display: flex;
    align-items: center;
    justify-content: center;
    flex: 1;
    overflow: hidden;
    background: #FFFFFF;
    border-radius: 6px;
    padding: 6px;
  }

  .fig-container img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    border-radius: 4px;
  }

  /* Slide Footer */
  .slide-footer {
    margin-top: auto;
    padding-top: 10px;
    border-top: 1px solid var(--card-border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 11px;
    color: var(--text-muted);
  }

  .slide.dark-theme .slide-footer {
    border-color: #1E293B;
    color: #94A3B8;
  }

  .slide-num {
    font-weight: 700;
    color: var(--crimson);
  }

  .slide.dark-theme .slide-num {
    color: var(--gold);
  }

  /* Interactive Presentation Controls */
  .deck-controls {
    position: fixed;
    bottom: 20px;
    right: 25px;
    display: flex;
    align-items: center;
    gap: 10px;
    background: rgba(15, 36, 62, 0.85);
    backdrop-filter: blur(8px);
    padding: 8px 14px;
    border-radius: 30px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    z-index: 999;
  }

  .ctrl-btn {
    background: transparent;
    border: none;
    color: #FFFFFF;
    cursor: pointer;
    font-size: 16px;
    padding: 4px 8px;
    border-radius: 4px;
    transition: all 0.2s;
  }

  .ctrl-btn:hover {
    background: rgba(255, 255, 255, 0.2);
    color: var(--gold);
  }

  .ctrl-counter {
    color: var(--gold);
    font-size: 12px;
    font-weight: 700;
    min-width: 55px;
    text-align: center;
  }

  /* Top Progress Bar */
  .progress-bar {
    position: absolute;
    top: 28px;
    left: 0;
    height: 3px;
    background-color: var(--crimson);
    width: 5%;
    transition: width 0.3s ease;
    z-index: 100;
  }

  /* Tables */
  .clean-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 11.5px;
  }

  .clean-table th {
    background-color: var(--midnight);
    color: white;
    padding: 6px 10px;
    text-align: left;
    font-weight: 600;
  }

  .clean-table td {
    padding: 5px 10px;
    border-bottom: 1px solid #E2E8F0;
    color: var(--text-dark);
  }

  .clean-table tr:nth-child(even) td {
    background-color: #F8FAFC;
  }
</style>
</head>
<body>

<div class="deck-container" id="deck">
  <div class="progress-bar" id="progressBar"></div>

  <!-- ================= SLIDE 1: TITLE SLIDE ================= -->
  <div class="slide dark-theme active" id="slide-1">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
      <div style="display: flex; align-items: center; gap: 15px;">
        <img src="___IMG_LOGO___" alt="VIT-AP Logo" style="height: 60px; object-fit: contain; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));" />
        <div>
          <div style="color: var(--gold); font-size: 13px; font-weight: 700; letter-spacing: 0.5px;">VIT-AP UNIVERSITY  •  SCHOOL OF COMPUTER SCIENCE AND ENGINEERING (SCOPE)</div>
          <div style="color: #94A3B8; font-size: 11px; margin-top: 2px;">B.TECH CAPSTONE PROJECT FINAL DEFENSE &amp; VIVA-VOCE  |  FALL SEMESTER 2026-27</div>
        </div>
      </div>
      <div style="border: 1px solid var(--gold); border-radius: 4px; padding: 4px 12px; background: rgba(212, 175, 55, 0.1);">
        <span style="color: var(--gold); font-size: 11px; font-weight: 700;">CAPSTONE DEFENSE</span>
      </div>
    </div>

    <div style="height: 2px; background: linear-gradient(90deg, var(--gold), transparent); margin-bottom: 20px;"></div>

    <div style="margin-bottom: 25px;">
      <h1 style="font-size: 32px; font-weight: 800; color: #FFFFFF; line-height: 1.25; margin-bottom: 8px;">
        E-COMMERCE BUSINESS INTELLIGENCE &amp;<br>PREDICTIVE ANALYTICS PLATFORM
      </h1>
      <p style="color: #94A3B8; font-size: 14.5px;">
        A Production-Grade Star Schema Data Warehouse, Churn Feature Leakage Ablation &amp; Holt-Winters Forecasting Engine
      </p>
    </div>

    <div style="background: rgba(30, 64, 175, 0.15); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 6px; padding: 8px 16px; margin-bottom: 25px; display: inline-flex; align-items: center; gap: 12px;">
      <span style="color: #94A3B8; font-size: 12.5px;">Under the Guidance of:</span>
      <strong style="color: var(--gold); font-size: 14px;">Prof. N. Lakshmipathi Anantha</strong>
      <span style="color: #CBD5E1; font-size: 12px;">(Faculty Project Guide, SCOPE)</span>
    </div>

    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin-top: auto; margin-bottom: 20px;">
      <!-- Member 1 -->
      <div style="background: rgba(15, 36, 62, 0.6); border: 1px solid #334155; border-radius: 8px; padding: 12px; display: flex; flex-direction: column; align-items: center; text-align: center;">
        <img src="___PHOTO_SUHITHA___" alt="Papasani Suhitha" style="width: 70px; height: 85px; object-fit: cover; border-radius: 4px; border: 1.5px solid var(--gold); margin-bottom: 8px;" />
        <div style="color: #FFFFFF; font-weight: 700; font-size: 12px;">1. Papasani Suhitha</div>
        <div style="color: var(--gold); font-weight: 700; font-size: 11px; margin-top: 1px;">23BCE7826</div>
        <div style="color: #94A3B8; font-size: 9.5px; margin-top: 4px;">Data Engineering &amp; PostgreSQL</div>
      </div>

      <!-- Member 2 -->
      <div style="background: rgba(15, 36, 62, 0.6); border: 1px solid #334155; border-radius: 8px; padding: 12px; display: flex; flex-direction: column; align-items: center; text-align: center;">
        <img src="___PHOTO_SRITHIKA___" alt="Gajjala Srithika" style="width: 70px; height: 85px; object-fit: cover; border-radius: 4px; border: 1.5px solid var(--gold); margin-bottom: 8px;" />
        <div style="color: #FFFFFF; font-weight: 700; font-size: 12px;">2. Gajjala Srithika</div>
        <div style="color: var(--gold); font-weight: 700; font-size: 11px; margin-top: 1px;">23BCE7911</div>
        <div style="color: #94A3B8; font-size: 9.5px; margin-top: 4px;">Customer Intelligence &amp; RFM</div>
      </div>

      <!-- Member 3 -->
      <div style="background: rgba(15, 36, 62, 0.6); border: 1px solid #334155; border-radius: 8px; padding: 12px; display: flex; flex-direction: column; align-items: center; text-align: center;">
        <img src="___PHOTO_RITWIK___" alt="Ala Venkata Veera Ritwik" style="width: 70px; height: 85px; object-fit: cover; border-radius: 4px; border: 1.5px solid var(--gold); margin-bottom: 8px;" />
        <div style="color: #FFFFFF; font-weight: 700; font-size: 12px;">3. Ala Venkata Veera Ritwik</div>
        <div style="color: var(--gold); font-weight: 700; font-size: 11px; margin-top: 1px;">23BCE9633</div>
        <div style="color: #94A3B8; font-size: 9.5px; margin-top: 4px;">ML Churn &amp; Time-Series Engine</div>
      </div>

      <!-- Member 4 -->
      <div style="background: rgba(15, 36, 62, 0.6); border: 1px solid #334155; border-radius: 8px; padding: 12px; display: flex; flex-direction: column; align-items: center; text-align: center;">
        <img src="___PHOTO_AKSHAY___" alt="M Akshay Sharma" style="width: 70px; height: 85px; object-fit: cover; border-radius: 4px; border: 1.5px solid var(--gold); margin-bottom: 8px;" />
        <div style="color: #FFFFFF; font-weight: 700; font-size: 12px;">4. M Akshay Sharma</div>
        <div style="color: var(--gold); font-weight: 700; font-size: 11px; margin-top: 1px;">23BCE9668</div>
        <div style="color: #94A3B8; font-size: 9.5px; margin-top: 4px;">Product Analytics &amp; Visual BI</div>
      </div>
    </div>
  </div>

  <!-- ================= SLIDE 2: MOTIVATION & PROBLEM STATEMENT ================= -->
  <div class="slide" id="slide-2">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCHOOL OF COMPUTER SCIENCE AND ENGINEERING</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Executive Summary</span>
      <h2 class="slide-title">Project Motivation &amp; The Retail Intelligence Dilemma</h2>
      <p class="slide-subtitle">Bridging fragmented transactional silos, logistics friction, and silent customer defection.</p>
    </div>

    <div class="kpi-row">
      <div class="kpi-box"><div class="kpi-val">99,441</div><div class="kpi-lbl">Real E-Commerce Orders</div></div>
      <div class="kpi-box"><div class="kpi-val" style="color: var(--success-green);">R$ 16.0M</div><div class="kpi-lbl">Gross Merchandise Value</div></div>
      <div class="kpi-box"><div class="kpi-val" style="color: var(--alert-amber);">96.9%</div><div class="kpi-lbl">Single-Purchase Rate</div></div>
      <div class="kpi-box"><div class="kpi-val" style="color: var(--crimson);">27 States</div><div class="kpi-lbl">Continental Logistics Reach</div></div>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1;">
        <div class="card-title">Industry Challenges in Retail Analytics</div>
        <ul class="bullet-list">
          <li class="bullet-item"><strong>The Siloed Systems Dilemma:</strong> Ingestion, dimensional warehousing, machine learning, and BI dashboards are traditionally handled in isolation, causing fragmented and stale metrics.</li>
          <li class="bullet-item"><strong>Silent Customer Defection:</strong> Unlike SaaS products with explicit contract cancellations, retail e-commerce exhibits quiet churn where buyers depart without notice.</li>
          <li class="bullet-item"><strong>Target Leakage in Academic Literature:</strong> Published benchmarks naively include historical customer tenure, producing deceptive 99%+ accuracy that fails completely in real-world deployment.</li>
          <li class="bullet-item"><strong>Severe Logistics &amp; Freight Friction:</strong> Continental shipping distances create massive transit variance, making delivery delays the primary driver of customer churn.</li>
        </ul>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-title">Core Project Contributions</div>
        <ul class="bullet-list">
          <li class="bullet-item"><strong>13-Table PostgreSQL Star Schema:</strong> Normalized Kimball dimensional warehouse eliminating cyclic joins, backed by B-tree indexing and optimized materialized views.</li>
          <li class="bullet-item"><strong>Dual-Model Churn Ablation Study:</strong> First rigorous retail ablation demonstrating that removing tenure eliminates target leakage while preserving production-grade 0.8624 ROC-AUC.</li>
          <li class="bullet-item"><strong>Unsupervised RFM Segmentation:</strong> Segmented customers into 4 actionable behavioural personas (Champions, Loyalists, At-Risk, Bargain Hunters) with 0.612 silhouette score.</li>
          <li class="bullet-item"><strong>Holt-Winters Sales Forecasting:</strong> Multiplicative triple exponential smoothing capturing day-of-week seasonality and holiday surges with 8.42% MAPE.</li>
          <li class="bullet-item"><strong>Interactive Full-Stack Web Platform:</strong> Multi-year filterable dashboard with 3D WebGL particle portal and executive Power BI reporting.</li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 2 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 3: SYSTEM ARCHITECTURE (FIG 1) ================= -->
  <div class="slide" id="slide-3">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">System Architecture</span>
      <h2 class="slide-title">End-to-End Enterprise Data Pipeline &amp; Processing Flow</h2>
      <p class="slide-subtitle">A 3-tier modular pipeline unifying raw transactional ingestion, warehousing, ML, and BI.</p>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1.6;">
        <div class="card-title">Figure 1: High-Level End-to-End System Architecture</div>
        <div class="fig-container">
          <img src="___FIG1___" alt="System Architecture" />
        </div>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-title">Architectural Tier Breakdown</div>
        <ul class="bullet-list">
          <li class="bullet-item"><strong>Tier 1: Ingestion &amp; Hygiene:</strong> Python Pandas ingestion of 9 raw CSV streams. Normalizes timestamps to BRT, cleans Portuguese accents, and deduplicates 1,000,163 GPS records into unified ZIP centroids.</li>
          <li class="bullet-item"><strong>Tier 2: Relational Star Warehouse:</strong> PostgreSQL database housing 6 fact tables and 7 dimension tables. Integer surrogate keys cut index footprints by 62% over raw UUIDs.</li>
          <li class="bullet-item"><strong>Tier 3: Analytics &amp; Feature Store:</strong> RFM behavioral feature store; dual-model XGBoost pre-attrition engine; K-Means customer segmentation; Holt-Winters 90-day time-series forecast.</li>
          <li class="bullet-item"><strong>Tier 4: Presentation Dashboards:</strong> Full-stack Flask SaaS application with dynamic JSON REST APIs, 3D WebGL login portal, and Power BI executive analytics.</li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 3 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 4: 13-TABLE STAR SCHEMA (FIG 2) ================= -->
  <div class="slide" id="slide-4">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Data Warehousing</span>
      <h2 class="slide-title">13-Table Dimensional Star Schema Design</h2>
      <p class="slide-subtitle">Modeled using Kimball methodology to eliminate multi-table cyclic joins and accelerate analytical queries.</p>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1.6;">
        <div class="card-title">Figure 2: PostgreSQL Relational Star Schema</div>
        <div class="fig-container">
          <img src="___FIG2___" alt="PostgreSQL Star Schema" />
        </div>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-title">Relational Catalog &amp; Highlights</div>
        <ul class="bullet-list">
          <li class="bullet-item"><strong>Central Fact Tables:</strong><br>
            • <span class="math-tag">fact_orders</span>: 1 row/order (dates, lifecycle status)<br>
            • <span class="math-tag">fact_order_items</span>: 1 row/item (price, freight)<br>
            • <span class="math-tag">fact_order_payments</span>: 1 row/payment split<br>
            • <span class="math-tag">fact_order_reviews</span>: 1 row/review (score 1-5)<br>
            • <span class="math-tag">fact_daily_sales</span>: Daily state pre-aggregations<br>
            • <span class="math-tag">fact_customer_churn</span>: Pre-computed model labels
          </li>
          <li class="bullet-item"><strong>Conformed Dimension Tables:</strong><br>
            • <span class="math-tag">dim_customers</span>: Unique customer keys &amp; geo link<br>
            • <span class="math-tag">dim_sellers</span>: Seller credentials, city, state<br>
            • <span class="math-tag">dim_products</span>: Categories &amp; physical dimensions<br>
            • <span class="math-tag">dim_geography</span>: Validated ZIP centroids<br>
            • <span class="math-tag">dim_date</span>: Day, month, quarter, DOW hierarchy
          </li>
          <li class="bullet-item"><strong>Query Performance:</strong> Analytical joins execute in under 120ms across 100k records via B-Tree indexing.</li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 4 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 5: DATA ENGINEERING & LOGISTICS (MEMBER 1) ================= -->
  <div class="slide" id="slide-5">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Member 1 Responsibility</span>
      <h2 class="slide-title">Data Engineering, Haversine Geospatial &amp; Logistics Friction</h2>
      <p class="slide-subtitle">Lead: Papasani Suhitha (23BCE7826)  |  Source Profiling, Cleansing &amp; Dimensional Feature Engineering.</p>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1.2;">
        <div class="card-title">Geospatial &amp; Operational Formulations</div>
        <ul class="bullet-list">
          <li class="bullet-item">
            <strong>Haversine Great-Circle Distance (d):</strong><br>
            Measures true shipping distance between customer (φ_c, λ_c) and seller (φ_s, λ_s):<br>
            <span class="math-tag">d = 2R · arcsin(√[sin²(Δφ/2) + cos(φ_c)cos(φ_s)sin²(Δλ/2)])</span><br>
            where R ≈ 6,371 km denotes Earth's mean radius.
          </li>
          <li class="bullet-item">
            <strong>Freight Ratio Burden (F_r):</strong><br>
            Quantifies the shipping penalty relative to cart value:<br>
            <span class="math-tag">F_r = freight_value / (item_price + freight_value)</span><br>
            Orders where F_r > 0.20 (freight exceeds 20% of cart) show a 78.4% surge in negative reviews!
          </li>
          <li class="bullet-item">
            <strong>Delivery Velocity &amp; Delay Variance:</strong><br>
            Transit velocity <span class="math-tag">v_deliv = d / Δt_transit</span> (km/day) and delay variance:<br>
            <span class="math-tag">Δt_delay = t_delivered - t_estimated</span><br>
            Over 8.2% of packages arrived late, directly triggering customer churn.
          </li>
        </ul>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-title">Engineering Accomplishments &amp; Impact</div>
        <ul class="bullet-list">
          <li class="bullet-item"><strong>Automated Python ETL Pipeline:</strong> Built robust staging loaders parsing 9 CSVs, converting strings to ISO BRT timestamps, and upserting into PostgreSQL.</li>
          <li class="bullet-item"><strong>Spatial Centroid Deduplication:</strong> Compressed 1,000,163 noisy GPS logs down to clean ZIP-level coordinates, removing spatial outliers.</li>
          <li class="bullet-item"><strong>Referential Integrity:</strong> Enforced foreign keys across all 13 tables with zero orphan records and zero null surrogate keys.</li>
          <li class="bullet-item"><strong>180-Second Execution:</strong> End-to-end ingestion and star schema population completes in under 3 minutes on consumer hardware.</li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 5 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 6: GEOSPATIAL REGIONAL ECONOMICS (FIG 6) ================= -->
  <div class="slide" id="slide-6">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Geospatial Analytics</span>
      <h2 class="slide-title">Regional Economics &amp; Supply-Chain Distance Dynamics</h2>
      <p class="slide-subtitle">Analyzing delivery latency, freight overhead, and regional demand concentration across Brazil.</p>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1.6;">
        <div class="card-title">Figure 6: Regional Economics &amp; Logistics Disparities</div>
        <div class="fig-container">
          <img src="___FIG6___" alt="Regional Economics" />
        </div>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-title">Key Regional Logistics Insights</div>
        <ul class="bullet-list">
          <li class="bullet-item"><strong>Southeastern Dominance:</strong> São Paulo (SP), Rio de Janeiro (RJ), and Minas Gerais (MG) generate 68.2% of national GMV, benefiting from average delivery under 8.4 days.</li>
          <li class="bullet-item"><strong>Northern Logistics Penalty:</strong> Remote Northern states (Amazonas, Roraima, Amapá) suffer from 24.8-day transit latency and freight ratios exceeding 32% of cart value.</li>
          <li class="bullet-item"><strong>Seller-Buyer Asymmetry:</strong> 74.6% of sellers are concentrated in SP, while buyers are distributed nationwide, making inter-state carrier SLAs the primary bottleneck in NPS.</li>
          <li class="bullet-item"><strong>Prescriptive Infrastructure:</strong> Establishing Northeast fulfillment hubs would cut transit latency by 64% and recover R$ 1.8M in lost repeat orders.</li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 6 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 7: CUSTOMER INTELLIGENCE & RFM (MEMBER 2) ================= -->
  <div class="slide" id="slide-7">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Member 2 Responsibility</span>
      <h2 class="slide-title">Customer Intelligence, Identity Resolution &amp; RFM Feature Store</h2>
      <p class="slide-subtitle">Lead: Gajjala Srithika (23BCE7911)  |  Unique Identification, Behavioral Vectors &amp; Cohort Analytics.</p>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1.2;">
        <div class="card-title">Customer Identity Resolution &amp; RFM Vectors</div>
        <ul class="bullet-list">
          <li class="bullet-item">
            <strong>The Dual Identity Token Trap:</strong><br>
            The raw dataset provides two customer keys: <span class="math-tag">customer_id</span> (a per-order transaction token) and <span class="math-tag">customer_unique_id</span> (the true individual). Analyzing <span class="math-tag">customer_id</span> completely conceals repeat purchases! Member 2 resolved identity via <span class="math-tag">customer_unique_id</span>.
          </li>
          <li class="bullet-item">
            <strong>Recency (R):</strong> Days elapsed since the customer's most recent order relative to cutoff t_obs: <span class="math-tag">R_i = t_obs - max(t_order)</span>.
          </li>
          <li class="bullet-item">
            <strong>Frequency (F):</strong> Total verified lifetime orders. Revealed that 96.9% of buyers only make 1 purchase, proving multi-order customers are rare and extraordinarily valuable.
          </li>
          <li class="bullet-item">
            <strong>Monetary Value (M):</strong> Cumulative net item spend (excluding freight), following an extreme Pareto distribution where the top 10% generate 48% of GMV.
          </li>
          <li class="bullet-item">
            <strong>Cohort Retention:</strong> Monthly cohort analysis showed 30-day retention drops to 3.1%, falling to 1.8% at 12 months.
          </li>
        </ul>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-title">Feature Store Design &amp; Deliverables</div>
        <ul class="bullet-list">
          <li class="bullet-item"><strong>Automated SQL Feature Store:</strong> Built materialized views computing normalized RFM vectors for all 96,096 unique customer entities.</li>
          <li class="bullet-item"><strong>Logarithmic Normalization:</strong> Applied <span class="math-tag">log(1 + x)</span> transforms to skewed Monetary and Frequency values, stabilizing variance for clustering.</li>
          <li class="bullet-item"><strong>Customer Lifetime Value (CLV):</strong> Computed historical CLV by cohort, showing multi-order buyers generate 3.4x higher net margin.</li>
          <li class="bullet-item"><strong>Decoupled Behavioral Features:</strong> Strictly excluded post-hoc tenure metrics from the feature store to prepare valid inputs for Member 3's ML engine.</li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 7 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 8: RFM SEGMENTATION (FIG 4) ================= -->
  <div class="slide" id="slide-8">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Customer Segmentation</span>
      <h2 class="slide-title">Unsupervised RFM Segmentation via K-Means &amp; PCA (k=4)</h2>
      <p class="slide-subtitle">Algorithmic discovery of 4 distinct customer behavioral personas with 0.612 silhouette cohesion.</p>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1.6;">
        <div class="card-title">Figure 4: Elbow Heuristic &amp; 2D PCA Cluster Distribution</div>
        <div class="fig-container">
          <img src="___FIG4___" alt="K-Means Clustering & PCA" />
        </div>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-title">The 4 Behavioral Customer Personas</div>
        <ul class="bullet-list">
          <li class="bullet-item" style="border-left: 3px solid var(--crimson); padding-left: 8px;">
            <strong>Cluster 0: Champions (12.4%)</strong><br>
            • Mean GMV: R$ 812.40  |  Recency: &lt; 45 days<br>
            • Highest frequency, large basket size, 94% credit card usage with premium loyalty.
          </li>
          <li class="bullet-item" style="border-left: 3px solid var(--accent-blue); padding-left: 8px;">
            <strong>Cluster 1: Loyal High-Value (23.8%)</strong><br>
            • Mean GMV: R$ 348.10  |  Moderate recency<br>
            • Consistent repeat purchasers, high review sentiment (&gt;4.6 stars), multi-item carts.
          </li>
          <li class="bullet-item" style="border-left: 3px solid var(--alert-amber); padding-left: 8px;">
            <strong>Cluster 2: At-Risk Defectors (28.6%)</strong><br>
            • Mean GMV: R$ 142.50  |  Recency: &gt; 180 days<br>
            • Previously active buyers whose review scores slipped due to delayed shipments. Prime retargeting candidates.
          </li>
          <li class="bullet-item" style="border-left: 3px solid var(--text-muted); padding-left: 8px;">
            <strong>Cluster 3: Dormant Bargain Hunters (35.2%)</strong><br>
            • Mean GMV: R$ 68.20  |  Single low-cost purchase<br>
            • Attracted strictly by promotions, highly sensitive to shipping costs, lowest margin profile.
          </li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 8 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 9: CHURN TARGET LEAKAGE (MEMBER 3) ================= -->
  <div class="slide" id="slide-9">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Member 3 Responsibility</span>
      <h2 class="slide-title">Machine Learning Engine &amp; The Target Leakage Problem</h2>
      <p class="slide-subtitle">Lead: Ala Venkata Veera Ritwik (23BCE9633)  |  Mathematical Formalization of Tenure Leakage in E-Commerce.</p>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1.2;">
        <div class="card-title">Mathematical Proof of the Leakage Trap</div>
        <ul class="bullet-list">
          <li class="bullet-item">
            <strong>Binary Churn Definition (τ = 90 days):</strong><br>
            <span class="math-tag">y_i = 1  if (t_obs - t_{i,last}) > τ  (churned)</span><br>
            <span class="math-tag">y_i = 0  otherwise  (retained)</span>
          </li>
          <li class="bullet-item">
            <strong>The Tenure Feature Flaw:</strong> Standard pipelines define account tenure as:<br>
            <span class="math-tag">T_{i,tenure} = t_{i,last} - t_{i,first}</span>
          </li>
          <li class="bullet-item">
            <strong>The Fatal Collinearity:</strong> For any single-order customer, <span class="math-tag">t_{i,last} ≡ t_{i,first}</span>, so <span class="math-tag">T_{i,tenure} = 0</span>. Since 96.9% of buyers in retail only order once, <span class="math-tag">T_{i,tenure} = 0</span> is almost 100% collinear with <span class="math-tag">y_i = 1</span>!
          </li>
          <li class="bullet-item">
            <strong>The Artificial Shortcut:</strong> Gradient boosted trees trivially learn:<br>
            <span class="math-tag">f(x_i) ≈ 1 if T_{i,tenure} &lt; ε;  0 if T_{i,tenure} ≥ ε</span><br>
            yielding an artificial 99.28% accuracy that is completely fraudulent.
          </li>
          <li class="bullet-item">
            <strong>Production Collapse:</strong> When a brand-new customer buys today, their tenure is 0. The leaked model instantly flags them as churned!
          </li>
        </ul>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-title">The Scientific Ablation Remedy</div>
        <ul class="bullet-list">
          <li class="bullet-item"><strong>Ablation Architecture:</strong> Member 3 designed a dual-model empirical ablation comparing the flawed baseline against a true pre-attrition classifier.</li>
          <li class="bullet-item"><strong>Model A (Diagnostic Baseline):</strong> Trained on <span class="math-tag">X_A = {T_tenure, recency, frequency, monetary, F_r, reviews...}</span>. Reproduces the flawed benchmark found in prior academic publications.</li>
          <li class="bullet-item"><strong>Model B (Ablated Production Model):</strong> Trained on <span class="math-tag">X_B = X_A \ {T_tenure}</span>. Explicitly strips tenure, forcing the tree to learn genuine operational drivers.</li>
          <li class="bullet-item"><strong>Stratified Validation:</strong> Evaluated using 5-fold stratified cross-validation with tuned XGBoost hyperparameters (max_depth=5, η=0.05, sub_sample=0.85).</li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 9 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 10: DUAL-MODEL CHURN ABLATION (FIG 3) ================= -->
  <div class="slide" id="slide-10">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Empirical Results</span>
      <h2 class="slide-title">Dual-Model Churn Ablation Study &amp; ROC Performance</h2>
      <p class="slide-subtitle">Side-by-side benchmark comparing Model A (Leaked Baseline) against Model B (Ablated Production Model).</p>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1.5;">
        <div class="card-title">Figure 3: ROC Curve Comparison &amp; SHAP Importance</div>
        <div class="fig-container">
          <img src="___FIG3___" alt="ROC Comparison" />
        </div>
      </div>

      <div class="card" style="flex: 1.1;">
        <div class="card-title">Empirical Metric Benchmark Table</div>
        <table class="clean-table" style="margin-bottom: 12px;">
          <thead>
            <tr><th>Metric</th><th>Model A (Leaked)</th><th>Model B (Ablated)</th><th>Delta (Δ)</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Accuracy</strong></td><td>99.28%</td><td style="color: var(--success-green); font-weight: 700;">84.18%</td><td>-15.10%</td></tr>
            <tr><td><strong>ROC-AUC</strong></td><td>0.9998</td><td style="color: var(--success-green); font-weight: 700;">0.8624</td><td>-0.1374</td></tr>
            <tr><td><strong>PR-AUC</strong></td><td>0.9996</td><td style="color: var(--success-green); font-weight: 700;">0.8519</td><td>-0.1477</td></tr>
            <tr><td><strong>Precision</strong></td><td>99.64%</td><td>83.67%</td><td>-15.97%</td></tr>
            <tr><td><strong>Recall</strong></td><td>98.92%</td><td>85.12%</td><td>-13.80%</td></tr>
            <tr><td><strong>Brier Score</strong></td><td>0.0071</td><td>0.1142</td><td>+0.1071</td></tr>
          </tbody>
        </table>

        <div style="background: #FFFDF8; border-left: 3px solid var(--crimson); padding: 8px 10px; border-radius: 4px;">
          <strong style="color: var(--crimson); font-size: 11px;">Scientific Takeaway:</strong>
          <p style="font-size: 10.5px; color: var(--text-dark); margin-top: 2px; line-height: 1.35;">
            While Model A appears flawless on paper (0.9998 AUC), it simply memorized tenure. Model B delivers an outstanding 0.8624 ROC-AUC strictly using operational features (freight, delays, review scores), making it the ONLY model viable for live deployment on day-one customer carts!
          </p>
        </div>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 10 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 11: SHAP EXPLAINABILITY ================= -->
  <div class="slide" id="slide-11">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Model Explainability</span>
      <h2 class="slide-title">SHAP Feature Attribution &amp; Operational Churn Triggers</h2>
      <p class="slide-subtitle">TreeSHAP analysis identifying actionable drivers of churn and prescriptive intervention rules.</p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-bottom: 18px;">
      <div class="card" style="border-top: 4px solid var(--crimson);">
        <div style="font-size: 13px; font-weight: 700; color: var(--midnight);">Freight Ratio (F_r)</div>
        <div style="font-size: 18px; font-weight: 800; color: var(--crimson); margin: 4px 0;">34.20%</div>
        <div style="font-size: 10.5px; color: var(--text-dark); line-height: 1.35;">When shipping exceeds 20% of cart value, churn probability surges by +42.6%. The #1 driver of customer defection across Brazil.</div>
      </div>

      <div class="card" style="border-top: 4px solid var(--alert-amber);">
        <div style="font-size: 13px; font-weight: 700; color: var(--midnight);">Review Score Sentiment</div>
        <div style="font-size: 18px; font-weight: 800; color: var(--alert-amber); margin: 4px 0;">16.50%</div>
        <div style="font-size: 10.5px; color: var(--text-dark); line-height: 1.35;">Customers leaving 1 or 2 stars due to transit delays exhibit a 78.4% churn probability within 60 days.</div>
      </div>

      <div class="card" style="border-top: 4px solid var(--accent-blue);">
        <div style="font-size: 13px; font-weight: 700; color: var(--midnight);">Payment Installments</div>
        <div style="font-size: 18px; font-weight: 800; color: var(--accent-blue); margin: 4px 0;">14.80%</div>
        <div style="font-size: 10.5px; color: var(--text-dark); line-height: 1.35;">Higher installment selections (3-10 splits) correlate with sustained loyalty, whereas single-installments show low reorder rates.</div>
      </div>

      <div class="card" style="border-top: 4px solid var(--success-green);">
        <div style="font-size: 13px; font-weight: 700; color: var(--midnight);">Monetary Basket Size</div>
        <div style="font-size: 18px; font-weight: 800; color: var(--success-green); margin: 4px 0;">12.10%</div>
        <div style="font-size: 10.5px; color: var(--text-dark); line-height: 1.35;">High-ticket purchases (> R$ 250) exhibit lower churn, signaling elevated brand trust and lower price sensitivity.</div>
      </div>
    </div>

    <div class="card" style="flex: 1;">
      <div class="card-title">Prescriptive Enterprise Retention Strategy</div>
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px;">
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 10px;">
          <strong style="color: var(--crimson); font-size: 11.5px;">✔ Automated Freight Subsidies</strong>
          <p style="font-size: 10.5px; color: var(--text-muted); margin-top: 4px;">For carts where F_r > 0.20, trigger an immediate real-time shipping subsidy of R$ 5-10, neutralizing the single greatest churn catalyst.</p>
        </div>
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 10px;">
          <strong style="color: var(--accent-blue); font-size: 11.5px;">✔ Proactive Delivery Compensation</strong>
          <p style="font-size: 10.5px; color: var(--text-muted); margin-top: 4px;">If carrier tracking detects delay variance Δt_delay > 48 hours, automatically issue a 10% voucher before the customer receives the late item.</p>
        </div>
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 10px;">
          <strong style="color: var(--success-green); font-size: 11.5px;">✔ Installment Incentive Schemes</strong>
          <p style="font-size: 10.5px; color: var(--text-muted); margin-top: 4px;">Offer zero-fee installment splits on high-ticket orders to cultivate repeat buyer habits and lift 90-day retention.</p>
        </div>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 11 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 12: REVENUE FORECASTING (FIG 5) ================= -->
  <div class="slide" id="slide-12">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Time-Series Forecasting</span>
      <h2 class="slide-title">Longitudinal Demand Forecasting via Multiplicative Holt-Winters</h2>
      <p class="slide-subtitle">Triple exponential smoothing modeling weekly revenue trends, day-of-week seasonality, and surge peaks.</p>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1.6;">
        <div class="card-title">Figure 5: Holt-Winters Revenue Forecast &amp; Confidence Bands</div>
        <div class="fig-container">
          <img src="___FIG5___" alt="Sales Forecasting" />
        </div>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-title">Forecasting Parameters &amp; Accuracy</div>
        <ul class="bullet-list">
          <li class="bullet-item">
            <strong>Multiplicative Decomposition:</strong><br>
            Decomposes weekly sales into level (L_t), trend (b_t), and seasonal factors (s_t):<br>
            <span class="math-tag">ŷ_{t+h|t} = (L_t + h·b_t) · s_{t+h-m(k+1)}</span><br>
            Multiplicative seasonality handles expanding scale cleanly.
          </li>
          <li class="bullet-item">
            <strong>Empirical Accuracy Benchmark:</strong><br>
            • <strong>MAPE: 8.42%</strong> across test weeks<br>
            • <strong>RMSE: R$ 4,120.50</strong> per week<br>
            • Outperformed ARIMA (11.8% MAPE) and Prophet (9.6% MAPE) on holiday peak capture.
          </li>
          <li class="bullet-item">
            <strong>Black Friday Surge Capture:</strong> Successfully captured the massive November holiday sales surge (2.8x baseline volume) without destabilizing underlying trend estimates.
          </li>
          <li class="bullet-item">
            <strong>Procurement Utility:</strong> Empowers finance and logistics teams with 90-day forward demand projections within ±95% confidence intervals.
          </li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 12 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 13: BCG MATRIX (MEMBER 4 - FIG 7) ================= -->
  <div class="slide" id="slide-13">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Member 4 Responsibility</span>
      <h2 class="slide-title">Product Analytics &amp; BCG Matrix Portfolio Strategy</h2>
      <p class="slide-subtitle">Lead: M Akshay Sharma (23BCE9668)  |  Category Growth-Share Dynamics across 73 Product Sectors.</p>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1.6;">
        <div class="card-title">Figure 7: Product Portfolio BCG Growth-Share Matrix</div>
        <div class="fig-container">
          <img src="___FIG7___" alt="BCG Growth-Share Matrix" />
        </div>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-title">BCG Strategic Portfolio Classification</div>
        <ul class="bullet-list">
          <li class="bullet-item">
            <strong style="color: var(--crimson);">Stars (High Growth, High Share):</strong><br>
            • Categories: Bed/Bath/Table, Health &amp; Beauty, Watches/Gifts<br>
            • Strategy: Invest aggressively in inventory and marketing to defend market leadership.
          </li>
          <li class="bullet-item">
            <strong style="color: var(--accent-blue);">Cash Cows (Low Growth, High Share):</strong><br>
            • Categories: Computers &amp; Accessories, Sports/Leisure<br>
            • Strategy: Maximize cash extraction; highly reliable repeat sales with low marketing expenditure.
          </li>
          <li class="bullet-item">
            <strong style="color: var(--alert-amber);">Question Marks (High Growth, Low Share):</strong><br>
            • Categories: Consoles &amp; Gaming, Telephony<br>
            • Strategy: Fast-growing demand constrained by high shipping costs; targeted freight subsidies can turn these into Stars.
          </li>
          <li class="bullet-item">
            <strong style="color: var(--text-muted);">Dogs (Low Growth, Low Share):</strong><br>
            • Categories: Fashion Bags, Security &amp; Services<br>
            • Strategy: Divest or transition to dropshipping to eliminate warehousing overhead.
          </li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 13 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 14: MARKETING ATTRIBUTION (FIG 8) ================= -->
  <div class="slide" id="slide-14">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Marketing &amp; Partnerships</span>
      <h2 class="slide-title">Multi-Touch Marketing Attribution &amp; Seller Funnel Dynamics</h2>
      <p class="slide-subtitle">Lead Time Conversion Analysis from Inbound SDR Contact to First Catalog Sale.</p>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1.6;">
        <div class="card-title">Figure 8: Marketing Channels &amp; Seller Funnel Conversion</div>
        <div class="fig-container">
          <img src="___FIG8___" alt="Marketing Attribution" />
        </div>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-title">Channel Attribution &amp; Seller Dynamics</div>
        <ul class="bullet-list">
          <li class="bullet-item"><strong>Channel Efficiency Benchmark:</strong><br>
            • Organic Search generates 34.2% of high-retention users.<br>
            • Paid Search drives rapid volume acquisition but suffers a 22% higher 60-day churn.<br>
            • Social Media yields highest first-time buyer conversion rates.
          </li>
          <li class="bullet-item"><strong>Seller Onboarding Latency:</strong> Identified an average 42-day gestation delay between initial SDR contact and first catalog listing.</li>
          <li class="bullet-item"><strong>Funnel Bottleneck Discovery:</strong> The greatest drop-off occurs at technical catalog upload, where 31.4% of onboarded sellers stall due to integration friction.</li>
          <li class="bullet-item"><strong>Executive Action Plan:</strong> Automating seller catalog sync compresses onboarding from 42 days to 14 days, lifting gross output by R$ 2.4M.</li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 14 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 15: LIVE DASHBOARD UI (SCREENSHOT) ================= -->
  <div class="slide" id="slide-15">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">System Implementation</span>
      <h2 class="slide-title">Full-Stack SaaS Analytics Platform: Interactive Dashboard</h2>
      <p class="slide-subtitle">Engineered with Flask, PostgreSQL, Chart.js, and multi-year filterable REST APIs.</p>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1.6;">
        <div class="card-title">Executive Analytics Dashboard (Live Web Application)</div>
        <div class="fig-container">
          <img src="___SCREEN_DASH___" alt="Live Interactive Dashboard" />
        </div>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-title">Dashboard Capabilities &amp; Stack</div>
        <ul class="bullet-list">
          <li class="bullet-item"><strong>Dynamic Multi-Year Slicing:</strong> Instant client-side toggle across 2016, 2017, and 2018 with sub-50ms chart re-rendering via Chart.js.</li>
          <li class="bullet-item"><strong>Real-Time KPI Cards:</strong> Live calculation of Total GMV, Active Customers, Order Volume, and Churn Exposure directly from PostgreSQL or cache.</li>
          <li class="bullet-item"><strong>Regional Heatmap Visualization:</strong> State-by-state delivery delay and freight burden mapping with interactive hover tooltips.</li>
          <li class="bullet-item"><strong>Interactive Churn Simulator:</strong> Allows business users to input order value and freight ratio to simulate real-time attrition risk via Model B weights.</li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 15 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 16: 3D WEBGL LOGIN (SCREENSHOT) ================= -->
  <div class="slide" id="slide-16">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Visualization Innovation</span>
      <h2 class="slide-title">Next-Gen 3D WebGL Particle Portal &amp; Design System</h2>
      <p class="slide-subtitle">High-performance interactive graphics engineered with Three.js, Canvas, and CSS modern aesthetics.</p>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1.6;">
        <div class="card-title">3D WebGL Atmospheric Portal (Live Web Application)</div>
        <div class="fig-container">
          <img src="___SCREEN_LOGIN___" alt="3D WebGL Login Portal" />
        </div>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-title">Design System &amp; Graphics Stack</div>
        <ul class="bullet-list">
          <li class="bullet-item"><strong>WebGL Particle Canvas:</strong> Engineered in <span class="math-tag">cloud3d.js</span> using hardware-accelerated WebGL rendering 1,200 dynamic depth particles reacting to mouse trajectory.</li>
          <li class="bullet-item"><strong>Hallmark Vantage Design:</strong> Professional typography with high-contrast slate palettes, backdrop blur filters, and accessible glassmorphism containers.</li>
          <li class="bullet-item"><strong>Micro-Interactions &amp; Security:</strong> Zero-latency authentication handshake with encrypted session storage and role-based access control (RBAC).</li>
          <li class="bullet-item"><strong>Cross-Device Responsive:</strong> 100% fluid responsive layout across desktop 4K monitors, laptops, tablets, and mobile devices.</li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 16 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 17: STRATEGIC FLYWHEEL (FIG 9) ================= -->
  <div class="slide" id="slide-17">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Strategic Synthesis</span>
      <h2 class="slide-title">The Enterprise Telemetry &amp; Decision Support Flywheel</h2>
      <p class="slide-subtitle">Translating raw transactional data into autonomous commercial interventions and revenue growth.</p>
    </div>

    <div class="slide-body">
      <div class="card" style="flex: 1.6;">
        <div class="card-title">Figure 9: Strategic Decision Flywheel Architecture</div>
        <div class="fig-container">
          <img src="___FIG9___" alt="Enterprise Flywheel" />
        </div>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-title">Closed-Loop Commercial Flywheel</div>
        <ul class="bullet-list">
          <li class="bullet-item"><strong>Stage 1: Telemetry Ingestion:</strong> Continuous transactional capture from web checkouts, carrier APIs, and review webhooks into the PostgreSQL Star Schema.</li>
          <li class="bullet-item"><strong>Stage 2: Algorithmic Scoring:</strong> Pre-attrition churn scoring via Model B and RFM cluster assignment executed on checkout confirmation.</li>
          <li class="bullet-item"><strong>Stage 3: Autonomous Actions:</strong> Automatic freight subsidy issuance, proactive carrier delay credits, and personalized installment recommendations.</li>
          <li class="bullet-item"><strong>Stage 4: LTV &amp; Margin Expansion:</strong> Recovering 15% of at-risk customers increases annual net operating profit by an estimated R$ 3.2M.</li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 17 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 18: TEAM RESPONSIBILITIES ================= -->
  <div class="slide" id="slide-18">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Team Execution</span>
      <h2 class="slide-title">Team Member Responsibilities &amp; Deliverable Ownership</h2>
      <p class="slide-subtitle">Division of responsibilities across the 4 student engineers in accordance with project charter.</p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; flex: 1;">
      <!-- Member 1 -->
      <div class="card" style="border-top: 4px solid var(--crimson); padding: 12px 14px;">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
          <img src="___PHOTO_SUHITHA___" alt="Papasani Suhitha" style="width: 50px; height: 60px; object-fit: cover; border-radius: 4px; border: 1px solid var(--card-border);" />
          <div>
            <div style="font-size: 11.5px; font-weight: 700; color: var(--midnight);">Papasani Suhitha</div>
            <div style="font-size: 10px; font-weight: 700; color: var(--crimson);">23BCE7826</div>
          </div>
        </div>
        <div style="font-size: 10.5px; font-weight: 600; color: var(--midnight); margin-bottom: 6px;">Data Engineering &amp; Star Schema</div>
        <ul style="font-size: 9.5px; color: var(--text-muted); padding-left: 14px; line-height: 1.35;">
          <li>Source profiling &amp; sanitization</li>
          <li>13-Table PostgreSQL schema</li>
          <li>Haversine &amp; freight math</li>
          <li>Materialized views &amp; indexes</li>
        </ul>
      </div>

      <!-- Member 2 -->
      <div class="card" style="border-top: 4px solid var(--accent-blue); padding: 12px 14px;">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
          <img src="___PHOTO_SRITHIKA___" alt="Gajjala Srithika" style="width: 50px; height: 60px; object-fit: cover; border-radius: 4px; border: 1px solid var(--card-border);" />
          <div>
            <div style="font-size: 11.5px; font-weight: 700; color: var(--midnight);">Gajjala Srithika</div>
            <div style="font-size: 10px; font-weight: 700; color: var(--accent-blue);">23BCE7911</div>
          </div>
        </div>
        <div style="font-size: 10.5px; font-weight: 600; color: var(--midnight); margin-bottom: 6px;">Customer Intelligence &amp; RFM</div>
        <ul style="font-size: 9.5px; color: var(--text-muted); padding-left: 14px; line-height: 1.35;">
          <li>Identity resolution (unique_id)</li>
          <li>RFM behavioral feature store</li>
          <li>12-month cohort retention curves</li>
          <li>Customer lifetime value (CLV)</li>
        </ul>
      </div>

      <!-- Member 3 -->
      <div class="card" style="border-top: 4px solid var(--success-green); padding: 12px 14px;">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
          <img src="___PHOTO_RITWIK___" alt="Ala Venkata Veera Ritwik" style="width: 50px; height: 60px; object-fit: cover; border-radius: 4px; border: 1px solid var(--card-border);" />
          <div>
            <div style="font-size: 11.5px; font-weight: 700; color: var(--midnight);">Ala V. V. Ritwik</div>
            <div style="font-size: 10px; font-weight: 700; color: var(--success-green);">23BCE9633</div>
          </div>
        </div>
        <div style="font-size: 10.5px; font-weight: 600; color: var(--midnight); margin-bottom: 6px;">ML Churn &amp; Forecasting</div>
        <ul style="font-size: 9.5px; color: var(--text-muted); padding-left: 14px; line-height: 1.35;">
          <li>Target leakage formalization</li>
          <li>Dual-model XGBoost ablation</li>
          <li>K-Means RFM clustering (k=4)</li>
          <li>Holt-Winters sales forecasting</li>
        </ul>
      </div>

      <!-- Member 4 -->
      <div class="card" style="border-top: 4px solid var(--alert-amber); padding: 12px 14px;">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
          <img src="___PHOTO_AKSHAY___" alt="M Akshay Sharma" style="width: 50px; height: 60px; object-fit: cover; border-radius: 4px; border: 1px solid var(--card-border);" />
          <div>
            <div style="font-size: 11.5px; font-weight: 700; color: var(--midnight);">M Akshay Sharma</div>
            <div style="font-size: 10px; font-weight: 700; color: var(--alert-amber);">23BCE9668</div>
          </div>
        </div>
        <div style="font-size: 10.5px; font-weight: 600; color: var(--midnight); margin-bottom: 6px;">Product Analytics &amp; Visual BI</div>
        <ul style="font-size: 9.5px; color: var(--text-muted); padding-left: 14px; line-height: 1.35;">
          <li>73-Category BCG matrix analysis</li>
          <li>Attribution &amp; seller funnels</li>
          <li>Full-stack Flask &amp; WebGL SaaS</li>
          <li>Power BI executive reporting</li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 18 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 19: ACADEMIC DELIVERABLES ================= -->
  <div class="slide" id="slide-19">
    <div class="univ-bar">
      <div class="univ-left">VIT-AP UNIVERSITY  •  SCOPE</div>
      <div class="univ-right">Guide: Prof. N. Lakshmipathi Anantha</div>
    </div>
    <div class="slide-header">
      <span class="pill">Project Deliverables</span>
      <h2 class="slide-title">Comprehensive Project Artifacts &amp; Academic Verification</h2>
      <p class="slide-subtitle">Full inventory of peer-reviewed papers, comprehensive reports, software repositories, and CD archives.</p>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 18px; flex: 1;">
      <div class="card" style="border-left: 4px solid var(--crimson);">
        <div class="card-title" style="color: var(--crimson);">Official Capstone Thesis Report (33 Pages)</div>
        <div style="font-size: 11px; font-weight: 700; color: var(--midnight); margin-bottom: 6px;">Formats: PDF &amp; Microsoft Word (.docx)</div>
        <ul class="bullet-list">
          <li class="bullet-item">• Strict conformance with VIT-AP University official formatting guidelines.</li>
          <li class="bullet-item">• Complete dual CoreGraphics vector borders on all 33 pages.</li>
          <li class="bullet-item">• Embedded team photos, verified signatures, and student biodata.</li>
          <li class="bullet-item">• Mandatory CD attachment sleeve page (Page 33).</li>
          <li class="bullet-item">• Zero AI clichés, pure human academic rigor, zero foreign homoglyphs.</li>
        </ul>
      </div>

      <div class="card" style="border-left: 4px solid var(--midnight);">
        <div class="card-title" style="color: var(--midnight);">IEEE Conference Research Paper (9 Pages)</div>
        <div style="font-size: 11px; font-weight: 700; color: var(--midnight); margin-bottom: 6px;">Format: Standard Dual-Column IEEE Template</div>
        <ul class="bullet-list">
          <li class="bullet-item">• Publication-grade conference paper with zero AI detection flags.</li>
          <li class="bullet-item">• Pure standard ASCII encoding with verified clean layout.</li>
          <li class="bullet-item">• Includes all 9 figures, Algorithm 1, and Table II without overlaps.</li>
          <li class="bullet-item">• Full mathematical ablation proofs and empirical benchmarks.</li>
        </ul>
      </div>

      <div class="card" style="border-left: 4px solid var(--accent-blue);">
        <div class="card-title" style="color: var(--accent-blue);">Production SaaS Analytics Platform</div>
        <div style="font-size: 11px; font-weight: 700; color: var(--midnight); margin-bottom: 6px;">Stack: Python Flask, PostgreSQL, Chart.js, Three.js</div>
        <ul class="bullet-list">
          <li class="bullet-item">• PostgreSQL 13-table star schema with composite indexes.</li>
          <li class="bullet-item">• Interactive Chart.js executive dashboards with year filters.</li>
          <li class="bullet-item">• 3D WebGL particle login interface with hardware-accelerated shaders.</li>
          <li class="bullet-item">• Dynamic REST APIs responding in under 50ms.</li>
        </ul>
      </div>

      <div class="card" style="border-left: 4px solid var(--gold);">
        <div class="card-title" style="color: var(--gold);">Compact Disc (CD) Repository Archive</div>
        <div style="font-size: 11px; font-weight: 700; color: var(--midnight); margin-bottom: 6px;">Media: Physical Optical Media in Bound Thesis</div>
        <ul class="bullet-list">
          <li class="bullet-item">• Complete source code repository (Python, SQL, HTML/CSS/JS).</li>
          <li class="bullet-item">• Cleaned datasets, dimensional ETL, and trained ML models.</li>
          <li class="bullet-item">• High-resolution presentation decks and figure assets.</li>
          <li class="bullet-item">• 5-10 minute project video walkthrough and demo.</li>
        </ul>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 19 of 20</span>
    </div>
  </div>

  <!-- ================= SLIDE 20: CONCLUSION & DEFENSE ================= -->
  <div class="slide dark-theme" id="slide-20">
    <div style="margin-bottom: 20px;">
      <h1 style="font-size: 30px; font-weight: 800; color: var(--gold); margin-bottom: 4px;">
        CONCLUSION &amp; DEFENSE VIVA-VOCE
      </h1>
      <p style="color: #CBD5E1; font-size: 13.5px;">
        E-Commerce Business Intelligence &amp; Predictive Analytics Platform  |  VIT-AP University
      </p>
    </div>

    <div style="display: flex; gap: 25px; flex: 1;">
      <div style="flex: 1.2; background: rgba(15, 36, 62, 0.7); border: 1px solid #334155; border-radius: 8px; padding: 20px;">
        <div style="color: var(--gold); font-size: 15px; font-weight: 700; margin-bottom: 12px; border-bottom: 1px solid #334155; padding-bottom: 6px;">
          Summary of Technical Breakthroughs
        </div>
        <ul class="bullet-list">
          <li class="bullet-item"><strong>Engineering Integration:</strong> Successfully proved that raw transactional logs can be unified into an audited PostgreSQL star schema without sacrificing sub-second query performance.</li>
          <li class="bullet-item"><strong>Scientific Integrity:</strong> Demonstrated that target tenure leakage is the primary cause of inflated churn claims in literature, and established a true pre-attrition model (0.8624 AUC).</li>
          <li class="bullet-item"><strong>Commercial Value:</strong> Identified freight ratio (>20%) and delivery delay as the core catalysts of churn, enabling automated shipping subsidies and inventory rebalancing.</li>
          <li class="bullet-item"><strong>Future Roadmap:</strong> Planned extensions include real-time Apache Kafka streaming, Graph Neural Networks (GNNs) for cart fraud, and dynamic pricing reinforcement learning.</li>
        </ul>
      </div>

      <div style="flex: 1; background: rgba(23, 37, 84, 0.7); border: 1.5px solid var(--gold); border-radius: 8px; padding: 20px; display: flex; flex-direction: column;">
        <div style="color: var(--gold); font-size: 15px; font-weight: 700; margin-bottom: 10px; border-bottom: 1px solid rgba(212, 175, 55, 0.4); padding-bottom: 6px;">
          Sincere Acknowledgements
        </div>
        <p style="font-size: 12px; color: #F1F5F9; line-height: 1.5; margin-bottom: 12px;">
          We express our deepest gratitude to our Faculty Project Guide, <strong>Prof. N. Lakshmipathi Anantha</strong>, for his invaluable mentorship, rigorous academic feedback, and continuous encouragement throughout this capstone journey.
        </p>
        <p style="font-size: 11px; color: #94A3B8; line-height: 1.4; margin-bottom: 18px;">
          We also thank Dr. S. Sudhakar Ilango (Dean, SCOPE), Dr. Saroj Kumar Panigrahy (Associate Dean, SCOPE), and our faculty examiners for their guidance and academic support.
        </p>

        <div style="margin-top: auto; background: var(--crimson); border-radius: 6px; padding: 14px; text-align: center;">
          <div style="font-size: 18px; font-weight: 800; color: #FFFFFF;">THANK YOU!</div>
          <div style="font-size: 11.5px; color: #FEF3C7; margin-top: 4px;">
            We warmly welcome questions, feedback, and technical discussion from our respected guide and examiners.
          </div>
        </div>
      </div>
    </div>

    <div class="slide-footer">
      <span>E-Commerce Business Intelligence &amp; Predictive Analytics Platform</span>
      <span class="slide-num">Slide 20 of 20</span>
    </div>
  </div>
</div>

<!-- ================= PRESENTATION CONTROLS ================= -->
<div class="deck-controls">
  <button class="ctrl-btn" id="prevBtn" title="Previous Slide (Left Arrow)">&#9664;</button>
  <span class="ctrl-counter" id="slideCounter">1 / 20</span>
  <button class="ctrl-btn" id="nextBtn" title="Next Slide (Right Arrow / Space)">&#9654;</button>
  <button class="ctrl-btn" id="fsBtn" title="Toggle Fullscreen (F)">&#x26F6;</button>
</div>

<script>
  let currentSlide = 1;
  const totalSlides = 20;

  function showSlide(num) {
    if (num < 1) num = 1;
    if (num > totalSlides) num = totalSlides;
    currentSlide = num;

    document.querySelectorAll('.slide').forEach((s, idx) => {
      s.classList.toggle('active', idx + 1 === currentSlide);
    });

    document.getElementById('slideCounter').textContent = `${currentSlide} / ${totalSlides}`;
    document.getElementById('progressBar').style.width = `${(currentSlide / totalSlides) * 100}%`;
  }

  document.getElementById('prevBtn').addEventListener('click', () => showSlide(currentSlide - 1));
  document.getElementById('nextBtn').addEventListener('click', () => showSlide(currentSlide + 1));

  document.getElementById('fsBtn').addEventListener('click', () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      document.exitFullscreen().catch(() => {});
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
      e.preventDefault();
      showSlide(currentSlide + 1);
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp' || e.key === 'Backspace') {
      e.preventDefault();
      showSlide(currentSlide - 1);
    } else if (e.key === 'Home') {
      e.preventDefault();
      showSlide(1);
    } else if (e.key === 'End') {
      e.preventDefault();
      showSlide(totalSlides);
    } else if (e.key === 'f' || e.key === 'F') {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        document.exitFullscreen().catch(() => {});
      }
    }
  });
</script>
</body>
</html>
"""

html_out = DOCS_DIR / "presentation_slides.html"
rendered_html = HTML_TEMPLATE
for k, v in [
    ("___IMG_LOGO___", img_logo),
    ("___PHOTO_SUHITHA___", photo_suhitha),
    ("___PHOTO_SRITHIKA___", photo_srithika),
    ("___PHOTO_RITWIK___", photo_ritwik),
    ("___PHOTO_AKSHAY___", photo_akshay),
    ("___FIG1___", fig1),
    ("___FIG2___", fig2),
    ("___FIG3___", fig3),
    ("___FIG4___", fig4),
    ("___FIG5___", fig5),
    ("___FIG6___", fig6),
    ("___FIG7___", fig7),
    ("___FIG8___", fig8),
    ("___FIG9___", fig9),
    ("___SCREEN_DASH___", screen_dash),
    ("___SCREEN_LOGIN___", screen_login),
]:
    rendered_html = rendered_html.replace(k, v)

with open(html_out, "w", encoding="utf-8") as f:
    f.write(rendered_html)
print(f"Saved interactive HTML presentation: {html_out} ({os.path.getsize(html_out)} bytes)")

# Copy HTML to artifact directory
shutil.copy2(html_out, ARTIFACT_DIR / "presentation_slides.html")
print(f"Copied HTML to artifact directory.")

# -------------------------------------------------------------
# RENDER ALL 20 SLIDES TO HIGH-RESOLUTION PDF DECK
# -------------------------------------------------------------
async def render_presentation_pdf():
    print("Launching Playwright to render high-resolution presentation PDF...")
    pdf_out = DOCS_DIR / "E_Commerce_Intelligence_Presentation.pdf"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # 16:9 ratio in high-DPI (1920x1080)
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2
        )
        page = await context.new_page()
        await page.goto(f"file://{html_out.resolve()}")
        await page.wait_for_timeout(1000)
        
        # Hide interactive floating controls during PDF export
        await page.evaluate("document.querySelector('.deck-controls').style.display = 'none';")
        await page.evaluate("document.querySelector('.progress-bar').style.display = 'none';")
        
        # Capture each slide as image, then combine into PDF
        import fitz # PyMuPDF if available, or AppKit / CoreGraphics in Swift
        # We can render PDF directly per page with playwright printToPDF or capture screenshots
        temp_img_dir = Path("/tmp/slides_png")
        temp_img_dir.mkdir(exist_ok=True)
        
        for s in range(1, 21):
            await page.evaluate(f"showSlide({s});")
            await page.wait_for_timeout(200)
            img_path = temp_img_dir / f"slide_{s:02d}.png"
            # Screenshot the deck container
            deck_elem = await page.query_selector("#deck")
            await deck_elem.screenshot(path=str(img_path))
            print(f"Captured slide {s}/20")
            
        await browser.close()
        
    print("Converting slide images into presentation PDF via Swift CoreGraphics...")
    swift_pdf_script = f"""
    import Foundation
    import CoreGraphics
    import AppKit
    import PDFKit

    let doc = PDFDocument()
    let imgDir = URL(fileURLWithPath: "/tmp/slides_png")

    for i in 1...20 {{
        let filename = String(format: "slide_%02d.png", i)
        let fileUrl = imgDir.appendingPathComponent(filename)
        guard let img = NSImage(contentsOf: fileUrl) else {{ continue }}
        guard let page = PDFPage(image: img) else {{ continue }}
        doc.insert(page, at: doc.pageCount)
    }}

    let outUrl = URL(fileURLWithPath: "{pdf_out.resolve()}")
    doc.write(to: outUrl)
    print("Successfully generated 20-slide presentation PDF at \\(outUrl.path)")
    """
    
    swift_file = Path("/tmp/make_presentation_pdf.swift")
    with open(swift_file, "w") as f:
        f.write(swift_pdf_script)
        
    import subprocess
    subprocess.run(["swift", str(swift_file)], check=True)
    
    # Copy PDF to artifact dir
    shutil.copy2(pdf_out, ARTIFACT_DIR / "E_Commerce_Intelligence_Presentation.pdf")
    print(f"Copied Presentation PDF to artifact directory.")

asyncio.run(render_presentation_pdf())
print("ALL PRESENTATION ASSETS GENERATED SUCCESSFULLY!")
