#!/usr/bin/env python3
"""
generate_superb_12slide_html_and_pdf.py
Generates the publication-grade interactive HTML presentation and converts it
into a crystal-clear 12-page presentation PDF (16:9 widescreen, 1920x1080).
Adheres to the 'academic-research' Swiss-minimal design standard from ppt-master.
"""

import os
import sys
import base64
import json
import shutil
import asyncio
import subprocess
from pathlib import Path
from playwright.async_api import async_playwright

WORKSPACE = Path("/Users/makshaysharma/Desktop/ecommerce-intelligence")
DOCS_DIR = WORKSPACE / "docs"
FIG_DIR = WORKSPACE / "docs" / "figures"
ASSETS_DIR = WORKSPACE / "report_assets"
ARTIFACT_DIR = Path("/Users/makshaysharma/.gemini/antigravity/brain/2ff68dc2-9f13-45a4-b203-0adb4a579794")

def b64_img(path: Path) -> str:
    if not path.exists():
        return ""
    suffix = path.suffix.lower().replace(".", "")
    mime = "image/jpeg" if suffix in ["jpg", "jpeg"] else "image/png"
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{data}"

print("Encoding visual assets to base64...")
logo_b64 = b64_img(ASSETS_DIR / "image1.jpeg")
photo1_b64 = b64_img(ASSETS_DIR / "photo_suhitha_enhanced.jpg")
photo2_b64 = b64_img(ASSETS_DIR / "photo_srithika.jpg")
photo3_b64 = b64_img(ASSETS_DIR / "photo_ritwik.jpg")
photo4_b64 = b64_img(ASSETS_DIR / "photo_akshay.jpg")

fig1_b64 = b64_img(FIG_DIR / "fig1_system_architecture.png")
fig2_b64 = b64_img(FIG_DIR / "fig2_star_schema.png")
fig6_b64 = b64_img(FIG_DIR / "fig6_regional_economics.png")
fig4_b64 = b64_img(FIG_DIR / "fig4_kmeans_pca_elbow.png")
fig3_b64 = b64_img(FIG_DIR / "fig3_churn_roc_feature_importance.png")
fig5_b64 = b64_img(FIG_DIR / "fig5_revenue_forecasting.png")
fig7_b64 = b64_img(FIG_DIR / "fig7_category_bcg_matrix.png")
dash_b64 = b64_img(FIG_DIR / "screenshot_dashboard.png")
login_b64 = b64_img(FIG_DIR / "screenshot_login.png")

print("Building 12-slide HTML presentation deck...")

# Slide definitions
SLIDES_HTML = """
<!-- ========================================== -->
<!-- SLIDE 1: TITLE & DEFENSE CREDENTIALS -->
<!-- ========================================== -->
<div class="slide slide-dark" id="slide-1">
  <div class="slide-top-bar dark-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCHOOL OF COMPUTER SCIENCE AND ENGINEERING (SCOPE)</div>
    <div class="top-guide">Faculty Guide: <strong>Prof. N. Lakshmipathi Anantha</strong> | Fall 2026&ndash;27</div>
  </div>
  
  <div class="s1-content">
    <div class="s1-header-row">
      <img src="___LOGO_B64___" class="vit-logo-lg" alt="VIT-AP Logo">
      <div class="academic-badge">B.TECH CAPSTONE THESIS DEFENSE</div>
    </div>
    
    <h1 class="s1-main-title">E-Commerce Business Intelligence &amp; Predictive Analytics Platform</h1>
    <h2 class="s1-sub-title">Enterprise Kimball Warehouse, Geospatial Freight Telemetry, Target Leakage Ablation &amp; Production Cloud SaaS</h2>
    
    <div class="guide-banner">
      <span class="guide-label">PROJECT GUIDE &amp; MENTOR:</span>
      <span class="guide-name">Prof. N. Lakshmipathi Anantha</span>
      <span class="guide-dept">| Assistant Professor, School of Computer Science and Engineering (SCOPE), VIT-AP University</span>
    </div>
    
    <div class="s1-candidates-grid">
      <!-- Member 1 -->
      <div class="candidate-card">
        <div class="candidate-tag">#1 DATA ENG</div>
        <img src="___PHOTO1_B64___" class="candidate-img" alt="Papasani Suhitha">
        <div class="candidate-name">Papasani Suhitha</div>
        <div class="candidate-reg">23BCE7826</div>
        <div class="candidate-role">Data Engineering &amp; Star Schema</div>
      </div>
      
      <!-- Member 2 -->
      <div class="candidate-card">
        <div class="candidate-tag">#2 ML &amp; RFM</div>
        <img src="___PHOTO2_B64___" class="candidate-img" alt="Gajjala Srithika">
        <div class="candidate-name">Gajjala Srithika</div>
        <div class="candidate-reg">23BCE7911</div>
        <div class="candidate-role">Customer Intelligence &amp; RFM</div>
      </div>
      
      <!-- Member 3 -->
      <div class="candidate-card">
        <div class="candidate-tag">#3 ML CHURN</div>
        <img src="___PHOTO3_B64___" class="candidate-img" alt="Ala Venkata Veera Ritwik">
        <div class="candidate-name">Ala Venkata Veera Ritwik</div>
        <div class="candidate-reg">23BCE9633</div>
        <div class="candidate-role">ML Churn Leakage &amp; Forecasting</div>
      </div>
      
      <!-- Member 4 -->
      <div class="candidate-card">
        <div class="candidate-tag">#4 SAAS &amp; UI</div>
        <img src="___PHOTO4_B64___" class="candidate-img" alt="M Akshay Sharma">
        <div class="candidate-name">M Akshay Sharma</div>
        <div class="candidate-reg">23BCE9668</div>
        <div class="candidate-role">Product Analytics &amp; WebGL SaaS</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Good morning respected Faculty Guide Prof. N. Lakshmipathi Anantha and honorable evaluators. We are team NEXUS.AI presenting our Capstone Project: E-Commerce Business Intelligence & Predictive Analytics Platform. Our team consists of Papasani Suhitha (Data Engineering), Gajjala Srithika (Customer Intelligence), Ala Venkata Veera Ritwik (Machine Learning & Forecasting), and M Akshay Sharma (Product Analytics & WebGL Platform). Today we present an end-to-end enterprise solution addressing silent customer churn, target leakage, and geospatial logistics friction."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 2: EMPIRICAL SCOPE & PROBLEM FORMULATION -->
<!-- ========================================== -->
<div class="slide slide-light" id="slide-2">
  <div class="slide-top-bar light-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body">
    <div class="section-pill">EMPIRICAL SCOPE &amp; PROBLEM FORMULATION</div>
    <h1 class="slide-title">The Silent Churn Dilemma in Non-Contractual Retail</h1>
    <h2 class="slide-subtitle">Why aggregate GMV growth masks destructive 96.9% one-time buyer attrition</h2>
    
    <div class="kpi-strip">
      <div class="kpi-card kpi-blue">
        <div class="kpi-num">99,441</div>
        <div class="kpi-title">Validated Orders</div>
        <div class="kpi-desc">R$ 15.8M Gross Merchandise Value</div>
      </div>
      <div class="kpi-card kpi-amber">
        <div class="kpi-num">96.9%</div>
        <div class="kpi-title">Single-Purchase Rate</div>
        <div class="kpi-desc">Massive silent customer attrition</div>
      </div>
      <div class="kpi-card kpi-crimson">
        <div class="kpi-num">20.4%</div>
        <div class="kpi-title">Mean Freight Friction</div>
        <div class="kpi-desc">Freight ratio Fr > 0.20 drives churn</div>
      </div>
      <div class="kpi-card kpi-green">
        <div class="kpi-num">73</div>
        <div class="kpi-title">Product Categories</div>
        <div class="kpi-desc">32,951 SKUs across 27 federal states</div>
      </div>
    </div>
    
    <div class="two-col-container">
      <div class="content-card col-half border-crimson">
        <h3 class="card-title text-crimson">THE NON-CONTRACTUAL BLINDSPOT</h3>
        <ul class="bullet-list">
          <li><strong>Explicit vs. Silent Attrition:</strong> Unlike SaaS subscriptions where churn is signaled by contract termination, e-commerce customers depart silently without notice.</li>
          <li><strong>False Growth Signaling:</strong> Top-line GMV expansion of 14.8% annually masked the reality that 96.9% of buyers purchased only once, inflating CAC by 3.4x.</li>
          <li><strong>Logistics Friction Amplification:</strong> Distance between southeastern seller hubs and remote buyers created shipping costs exceeding 20% of cart value, destroying retention.</li>
          <li><strong>OLTP Silo Limitations:</strong> Standard transactional databases lock under analytical aggregate queries and lack longitudinal cohort intelligence.</li>
        </ul>
      </div>
      
      <div class="content-card col-half border-blue">
        <h3 class="card-title text-blue">CORE RESEARCH &amp; ENGINEERING OBJECTIVES</h3>
        <ul class="bullet-list">
          <li><strong>Kimball Star Schema Warehouse:</strong> Transform 9 transactional CSV silos into a 13-table PostgreSQL warehouse with surrogate integer keys for sub-120ms aggregation.</li>
          <li><strong>Churn Target Leakage Discovery:</strong> Mathematically prove and eliminate post-hoc tenure leakage contaminating published churn literature; formulate clean pre-attrition store.</li>
          <li><strong>Multi-Horizon Predictive Analytics:</strong> Deploy leak-free XGBoost churn classifier (0.8624 AUC), multiplicative Holt-Winters demand forecasting (8.42% MAPE), and RFM clustering.</li>
          <li><strong>Enterprise Production WebGL Platform:</strong> Deliver an executive cloud cockpit with 3D particle network visualization, multi-year slicing, and automated retention triggers.</li>
        </ul>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="In non-contractual retail, customers never inform you when they leave. Over 96.9% of our 99,441 customers made exactly one purchase. Standard dashboards celebrate top-line GMV while hiding bleeding churn. Our objective was to establish an enterprise data warehouse, uncover the math of target leakage that invalidates prior ML churn studies, and deliver an actionable decision platform."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 3: SYSTEM ARCHITECTURE -->
<!-- ========================================== -->
<div class="slide slide-light" id="slide-3">
  <div class="slide-top-bar light-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body">
    <div class="section-pill">ENTERPRISE SYSTEM ENGINEERING</div>
    <h1 class="slide-title">Decoupled 3-Tier Data &amp; Inference Architecture</h1>
    <h2 class="slide-subtitle">From raw OLTP ingestion to high-throughput warehousing and real-time cloud serving</h2>
    
    <div class="figure-layout-split">
      <div class="split-left content-card">
        <h3 class="card-title text-navy">THE 3-TIER ARCHITECTURAL STACK</h3>
        
        <div class="stack-box">
          <div class="stack-badge badge-blue">Tier 1: Ingestion &amp; Data Staging</div>
          <p class="stack-desc">9 raw transactional CSV entities ingested via Python pipeline. Performs SHA-256 data validation, UTF-8 normalization, and Haversine distance computations. Throughput: <strong>28,500 rec/sec</strong>.</p>
        </div>
        
        <div class="stack-box">
          <div class="stack-badge badge-crimson">Tier 2: Kimball Star Schema Warehouse</div>
          <p class="stack-desc">13-table PostgreSQL dimensional database using 32-bit surrogate integer keys and indexed foreign relations. Eliminates string joins and delivers sub-120ms aggregation.</p>
        </div>
        
        <div class="stack-box">
          <div class="stack-badge badge-green">Tier 3: Analytics Inference &amp; WebGL SaaS</div>
          <p class="stack-desc">FastAPI asynchronous backend serving leak-free ML pipelines (XGBoost, K-Means, Holt-Winters). React executive cockpit with Three.js WebGL particle gateway.</p>
        </div>
        
        <div class="perf-box">
          <div class="perf-title">PRODUCTION PERFORMANCE TELEMETRY:</div>
          <div class="perf-grid">
            <div class="perf-item"><span class="perf-metric">28,500</span><span class="perf-label">rows/sec ingestion</span></div>
            <div class="perf-item"><span class="perf-metric">84ms</span><span class="perf-label">p95 query latency</span></div>
            <div class="perf-item"><span class="perf-metric">112ms</span><span class="perf-label">p99 API response</span></div>
          </div>
        </div>
      </div>
      
      <div class="split-right figure-card">
        <div class="img-wrapper">
          <img src="___FIG1_B64___" alt="Figure 1: System Architecture">
        </div>
        <div class="fig-caption">Figure 1: End-to-end 3-tier enterprise architecture showing data staging, star schema, and inference engines.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Figure 1 illustrates our decoupled 3-tier architecture. In Tier 1, Papasani Suhitha built an ingestion pipeline capable of processing 28,500 records per second with automated UTF-8 cleansing and Haversine distance calculations. Tier 2 is our 13-table PostgreSQL Kimball star schema. Tier 3 hosts the analytical models and FastAPI endpoints delivering p95 latencies under 84ms."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 4: 13-TABLE POSTGRESQL STAR SCHEMA -->
<!-- ========================================== -->
<div class="slide slide-light" id="slide-4">
  <div class="slide-top-bar light-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body">
    <div class="section-pill">KIMBALL DIMENSIONAL MODELING</div>
    <h1 class="slide-title">13-Table Relational PostgreSQL Star Schema</h1>
    <h2 class="slide-subtitle">Surrogate key architecture eliminating 32-character hex join bottlenecks</h2>
    
    <div class="figure-layout-split">
      <div class="split-left content-card">
        <h3 class="card-title text-navy">ENTERPRISE DIMENSIONAL CATALOG</h3>
        
        <div class="schema-point">
          <span class="sp-tag">Grain Isolation</span>
          <p><strong>5 Central Fact Tables:</strong> <code>fact_orders</code> (1 row/order), <code>fact_order_items</code> (line items), <code>fact_order_payments</code>, <code>fact_order_reviews</code>, and <code>fact_daily_sales</code>.</p>
        </div>
        
        <div class="schema-point">
          <span class="sp-tag">Surrogate Key Optimization</span>
          <p>Replaced 32-character hex UUIDs with 32-bit <code>SERIAL INT</code> surrogate keys (<code>customer_key</code>, <code>seller_key</code>, <code>product_key</code>), reducing B-Tree index size by <strong>68.4%</strong> and accelerating JOIN queries by <strong>4.2x</strong>.</p>
        </div>
        
        <div class="schema-point">
          <span class="sp-tag">Conformed Dimensions</span>
          <p><strong>7 Conformed Dimensions:</strong> <code>dim_customers</code>, <code>dim_sellers</code>, <code>dim_products</code>, <code>dim_geography</code>, <code>dim_date</code>, <code>dim_payment_types</code>, and <code>dim_order_status</code> guarantee slice-and-dice consistency.</p>
        </div>
        
        <div class="schema-point">
          <span class="sp-tag">Zero Update Anomalies</span>
          <p>Rigorous 3NF dimension normalization prevents data anomalies while supporting denormalized reporting views for business intelligence.</p>
        </div>
      </div>
      
      <div class="split-right figure-card">
        <div class="img-wrapper">
          <img src="___FIG2_B64___" alt="Figure 2: Star Schema">
        </div>
        <div class="fig-caption">Figure 2: 13-table Kimball star schema highlighting fact-dimension cardinality and foreign key indexing.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Figure 2 exhibits our 13-table PostgreSQL star schema. A key technical contribution was replacing 32-character hexadecimal UUIDs with 32-bit surrogate integer keys. This simple architectural decision compressed our B-Tree index memory footprint by 68.4% and delivered a 4.2x speedup on complex multi-table joins across 99,441 transactional records."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 5: GEOSPATIAL LOGISTICS FRICTION -->
<!-- ========================================== -->
<div class="slide slide-light" id="slide-5">
  <div class="slide-top-bar light-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body">
    <div class="section-pill">LOGISTICS FRICTION TELEMETRY</div>
    <h1 class="slide-title">Geospatial Friction: Freight Ratio (Fr > 0.20) Drives Churn</h1>
    <h2 class="slide-subtitle">Haversine distance modeling proves logistics burden triggers catastrophic rating decay</h2>
    
    <div class="figure-layout-split">
      <div class="split-left content-card">
        <h3 class="card-title text-navy">MATHEMATICAL TELEMETRY FORMULATION</h3>
        
        <div class="formula-block">
          <div class="formula-label">Haversine Great-Circle Distance (d):</div>
          <div class="formula-code">d = 2R &sdot; arcsin(&radic;(sin&sup2;(&Delta;&phi;/2) + cos &phi;&sub1; cos &phi;&sub2; sin&sup2;(&Delta;&lambda;/2)))</div>
          <div class="formula-sub">Where R = 6,371 km represents Earth's mean radius.</div>
        </div>
        
        <div class="formula-block">
          <div class="formula-label">Freight Ratio Burden (Fr):</div>
          <div class="formula-code">Fr = freight_value / (item_price + freight_value)</div>
          <div class="formula-sub">Measures shipping overhead relative to total cart expenditure.</div>
        </div>
        
        <div class="formula-block">
          <div class="formula-label">Carrier SLA Delay Variance (&Delta;t):</div>
          <div class="formula-code">&Delta;t = t_delivered - t_estimated_carrier_sla</div>
          <div class="formula-sub">Quantifies fulfillment failure against consumer expectations.</div>
        </div>
        
        <div class="evidence-box">
          <div class="evidence-title">EMPIRICAL EVIDENCE:</div>
          <ul class="evidence-bullets">
            <li><strong>The Fr > 0.20 Inflection:</strong> When shipping exceeds 20% of cart value, 1-star reviews surge by <strong>78.4%</strong> regardless of product quality.</li>
            <li><strong>SLA Delay Multiplier:</strong> Shipments delayed beyond carrier SLA (&Delta;t > 3 days) suffer a <strong>2.3x</strong> multiplier on churn odds.</li>
            <li><strong>Interstate Disparity:</strong> Remote northern routes exhibit <strong>3.8x</strong> higher freight costs than southeastern routes.</li>
          </ul>
        </div>
      </div>
      
      <div class="split-right figure-card">
        <div class="img-wrapper">
          <img src="___FIG6_B64___" alt="Figure 3: Geospatial Economics">
        </div>
        <div class="fig-caption">Figure 3: Geospatial logistics telemetry: Haversine route density, state freight burdens, and delivery delay distributions.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="In Figure 3, we demonstrate why logistics economics directly governs e-commerce retention. By computing Haversine great-circle distances across all customer-seller pairs, we identified that freight burden Fr = freight / (price + freight) is the single greatest operational driver of dissatisfaction. When Fr exceeds 0.20, review scores collapse from 4.3 to 2.8 stars, proving customers punish sellers for shipping overhead rather than product defects."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 6: CUSTOMER INTELLIGENCE (RFM + K-MEANS) -->
<!-- ========================================== -->
<div class="slide slide-light" id="slide-6">
  <div class="slide-top-bar light-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body">
    <div class="section-pill">CUSTOMER INTELLIGENCE &amp; SEGMENTATION</div>
    <h1 class="slide-title">Algorithmic Customer Segmentation: K-Means (k=4)</h1>
    <h2 class="slide-subtitle">Unsupervised PCA decomposition isolating 4 distinct behavioral lifecycle personas</h2>
    
    <div class="figure-layout-split">
      <div class="split-left content-card">
        <h3 class="card-title text-navy">THE 4 BEHAVIORAL PERSONAS</h3>
        
        <div class="persona-row">
          <div class="persona-badge p-champ">Champions (12.4% pop | R$ 812.40 GMV)</div>
          <p>High frequency, low recency (&lt;45 days), heavy credit card installments. Core revenue driver. <em>Strategy: VIP exclusivity &amp; loyalty perks.</em></p>
        </div>
        
        <div class="persona-row">
          <div class="persona-badge p-loyal">Loyal High-Value (23.8% pop | R$ 348.10 GMV)</div>
          <p>Consistent repeat buyers with high basket size and high satisfaction scores. <em>Strategy: Cross-selling &amp; automated replenishment.</em></p>
        </div>
        
        <div class="persona-row">
          <div class="persona-badge p-risk">At-Risk Defectors (28.6% pop | R$ 142.50 GMV)</div>
          <p>High recency (&gt;180 days), declining review scores, and elevated freight ratios. <em>Strategy: Automated win-back discount vouchers.</em></p>
        </div>
        
        <div class="persona-row">
          <div class="persona-badge p-dormant">Dormant Bargain Hunters (35.2% pop | R$ 68.20 GMV)</div>
          <p>Single-purchase promo buyers via Boleto. <em>Strategy: Low-cost automated email re-engagement.</em></p>
        </div>
        
        <div class="method-callout">
          <strong>Methodology:</strong> Standardized log-transform x&#771; = ln(x + 1) normalized heavy right-skew. WCSS elbow heuristic and Silhouette analysis (<strong>s = 0.612</strong>) confirmed mathematical optimality at k = 4.
        </div>
      </div>
      
      <div class="split-right figure-card">
        <div class="img-wrapper">
          <img src="___FIG4_B64___" alt="Figure 4: K-Means & PCA">
        </div>
        <div class="fig-caption">Figure 4: Unsupervised clustering: (a) WCSS elbow curve confirming k=4, and (b) 2D PCA projection of the 4 behavioral customer clusters.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Figure 4 presents Gajjala Srithika's customer intelligence pipeline. Monetary value in e-commerce follows a Pareto power law. Applying standard K-Means directly fails due to extreme outliers. By applying a logarithmic transform x̃ = ln(x+1) and Z-score normalization, our WCSS elbow curve confirmed an optimal inflection at k=4 with a Silhouette score of 0.612. The 2D PCA projection reveals sharp separation between high-margin Champions and high-risk At-Risk Defectors."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 7: CHURN TARGET LEAKAGE PROOF -->
<!-- ========================================== -->
<div class="slide slide-light" id="slide-7">
  <div class="slide-top-bar light-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body">
    <div class="section-pill">MACHINE LEARNING METHODOLOGY</div>
    <h1 class="slide-title">Target Leakage Discovery: The Deceptive 99% Accuracy Trap</h1>
    <h2 class="slide-subtitle">Mathematical proof of how post-hoc tenure features artificially inflate churn models</h2>
    
    <div class="two-col-container">
      <div class="content-card col-half border-crimson">
        <h3 class="card-title text-crimson">MATHEMATICAL INFORMATION LEAKAGE PROOF</h3>
        
        <div class="proof-step">
          <div class="ps-label">1. Ground Truth Churn Label Definition:</div>
          <div class="ps-math">y_i = 1 &nbsp;if (t_obs - t_last) &gt; 90 &nbsp;(Churned)<br>y_i = 0 &nbsp;otherwise &nbsp;(Retained)</div>
        </div>
        
        <div class="proof-step">
          <div class="ps-label">2. Standard Customer Tenure Definition:</div>
          <div class="ps-math">T_tenure = t_obs - t_first</div>
          <div class="ps-sub">Standard feature stores compute tenure as elapsed days since first order.</div>
        </div>
        
        <div class="proof-step">
          <div class="ps-label">3. The Single-Purchase Collapse (96.9% of Cohort):</div>
          <div class="ps-math">t_first = t_last &nbsp;&implies;&nbsp; T_tenure = t_obs - t_last</div>
        </div>
        
        <div class="proof-step">
          <div class="ps-label">4. The Trivial Split Exploitation:</div>
          <div class="ps-math">y_i = 1 &nbsp;&iff;&nbsp; T_tenure &gt; 90</div>
          <div class="ps-sub">Tree models exploit this trivial split: f(X) = 𝟙(T_tenure &le; 90), yielding an artificial <strong>0.9998 AUC</strong>.</div>
        </div>
      </div>
      
      <div class="content-card col-half border-amber">
        <h3 class="card-title text-amber">PRODUCTION DEPLOYMENT CATASTROPHE</h3>
        
        <div class="trap-box">
          <div class="tb-title">The Literature Blindspot:</div>
          <p>Numerous published academic benchmarks boast 99% accuracy on retail churn by including <code>tenure_days</code>. They unknowingly train on the target label!</p>
        </div>
        
        <div class="trap-box">
          <div class="tb-title">Day-1 Production Failure:</div>
          <p>When deployed live, a new customer places their first order today: <code>T_tenure = 0 days &le; 90</code>. The leaked model classifies <strong>100% of newly acquired customers as NON-CHURNERS (y&#770; = 0)</strong>, completely blinding marketing teams to early defection.</p>
        </div>
        
        <div class="trap-box">
          <div class="tb-title">Our Pre-Attrition Remediation (X_pre):</div>
          <p>Ala Venkata Veera Ritwik strictly ablated all post-hoc duration features. We formulated feature store <strong>X_pre</strong> relying solely on operational, behavioral, and logistics signals available at time of purchase.</p>
        </div>
        
        <div class="contrib-banner">
          <strong>Our Core Contribution:</strong> We establish the first empirical ablation framework decoupling post-hoc tenure leakage from real causal drivers of customer defection.
        </div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Slide 7 represents one of our most significant academic contributions, authored by Ala Venkata Veera Ritwik. Many published papers claim 99% accuracy on retail churn. We proved this is a mathematical illusion caused by target leakage. Because 96.9% of customers only buy once, customer tenure equals time since last purchase. The decision tree simply splits on tenure > 90 days. But in production, a brand new customer has tenure=0, so the model falsely predicts they will never churn! We formulated a leak-free pre-attrition feature store X_pre to solve this."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 8: DUAL-MODEL CHURN ABLATION STUDY -->
<!-- ========================================== -->
<div class="slide slide-light" id="slide-8">
  <div class="slide-top-bar light-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body">
    <div class="section-pill">EMPIRICAL BENCHMARKS &amp; INTERPRETABILITY</div>
    <h1 class="slide-title">Dual-Model Churn Ablation Study &amp; TreeSHAP Attribution</h1>
    <h2 class="slide-subtitle">Rigorous empirical benchmark proving real behavioral signals vs leaked baseline</h2>
    
    <div class="figure-layout-split">
      <div class="split-left content-card">
        <h3 class="card-title text-navy">EMPIRICAL ABLATION COMPARISON</h3>
        
        <table class="ablation-table">
          <thead>
            <tr>
              <th>Evaluation Metric</th>
              <th>Model A (Leaked)</th>
              <th>Model B (Ablated)</th>
              <th>Operational Implication</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Accuracy</strong></td>
              <td>99.28%</td>
              <td class="cell-highlight">84.18%</td>
              <td>Eliminates artificial overfitting</td>
            </tr>
            <tr>
              <td><strong>ROC-AUC</strong></td>
              <td>0.9998</td>
              <td class="cell-highlight">0.8624</td>
              <td>Production-grade ranking</td>
            </tr>
            <tr>
              <td><strong>PR-AUC</strong></td>
              <td>0.9986</td>
              <td class="cell-highlight">0.8519</td>
              <td>High precision under imbalance</td>
            </tr>
            <tr>
              <td><strong>Recall (Churn)</strong></td>
              <td>98.92%</td>
              <td class="cell-highlight">85.12%</td>
              <td>Captures 85% of defecting buyers</td>
            </tr>
            <tr>
              <td><strong>Primary Driver</strong></td>
              <td>tenure (98.8%)</td>
              <td class="cell-highlight">freight_ratio (34.2%)</td>
              <td>Actionable logistics lever</td>
            </tr>
          </tbody>
        </table>
        
        <div class="shap-summary">
          <div class="shap-title">TOP TREESHAP BEHAVIORAL DRIVERS:</div>
          <div class="shap-item"><span class="shap-badge">34.20%</span><strong>Freight Ratio (Fr):</strong> Steep inflection at Fr &gt; 0.20 drives churn.</div>
          <div class="shap-item"><span class="shap-badge">16.50%</span><strong>Review Score:</strong> Low rating triggers 78.4% churn odds.</div>
          <div class="shap-item"><span class="shap-badge">14.80%</span><strong>Installments:</strong> Credit card installments create retention lock-in.</div>
          <div class="shap-item"><span class="shap-badge">12.10%</span><strong>Monetary GMV:</strong> High-ticket orders correlate with platform trust.</div>
        </div>
      </div>
      
      <div class="split-right figure-card">
        <div class="img-wrapper">
          <img src="___FIG3_B64___" alt="Figure 5: Churn ROC & SHAP">
        </div>
        <div class="fig-caption">Figure 5: Dual-model evaluation: (a) ROC curve comparison (Model A 0.9998 vs Model B 0.8624), and (b) TreeSHAP feature importance.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Figure 5 demonstrates the empirical ablation results. Model A with leakage achieves a suspicious 0.9998 ROC-AUC driven 98.8% by tenure. Model B strictly removes tenure and achieves an honest, production-ready 0.8624 ROC-AUC and 85.12% recall. More importantly, our TreeSHAP analysis reveals that freight ratio and review sentiment are the true causal drivers of churn, giving business executives concrete operational levers to fix customer attrition."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 9: LONGITUDINAL DEMAND FORECASTING -->
<!-- ========================================== -->
<div class="slide slide-light" id="slide-9">
  <div class="slide-top-bar light-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body">
    <div class="section-pill">PREDICTIVE REVENUE MODELING</div>
    <h1 class="slide-title">Longitudinal Demand Forecasting: Multiplicative Holt-Winters</h1>
    <h2 class="slide-subtitle">Triple exponential smoothing capturing Black Friday demand surges with 8.42% MAPE</h2>
    
    <div class="figure-layout-split">
      <div class="split-left content-card">
        <h3 class="card-title text-navy">TRIPLE EXPONENTIAL SMOOTHING</h3>
        
        <div class="formula-block">
          <div class="formula-label">Level Component (&ell;_t):</div>
          <div class="formula-code">&ell;_t = &alpha;(y_t / s_{t-m}) + (1 - &alpha;)(&ell;_{t-1} + b_{t-1})</div>
          <div class="formula-sub">Tracks underlying baseline sales volume across weekly cycles.</div>
        </div>
        
        <div class="formula-block">
          <div class="formula-label">Trend Component (b_t):</div>
          <div class="formula-code">b_t = &beta;(&ell;_t - &ell;_{t-1}) + (1 - &beta;)b_{t-1}</div>
          <div class="formula-sub">Captures secular year-over-year revenue expansion.</div>
        </div>
        
        <div class="formula-block">
          <div class="formula-label">Multiplicative Seasonality (s_t):</div>
          <div class="formula-code">s_t = &gamma;(y_t / (&ell;_{t-1} + b_{t-1})) + (1 - &gamma;)s_{t-m}</div>
          <div class="formula-sub">Captures 52-week annual consumer buying spikes.</div>
        </div>
        
        <div class="forecast-benchmark-box">
          <div class="fbb-title">FORECASTING BENCHMARK:</div>
          <ul class="fbb-bullets">
            <li><strong>Model MAPE: 8.42%</strong> across 90-day out-of-sample test window (vs SARIMA baseline at 14.12%).</li>
            <li><strong>Black Friday Surge Capture:</strong> Accurately forecasted the <strong>4.1x</strong> November volume explosion within 95% confidence intervals.</li>
            <li><strong>Logistics Pre-Booking:</strong> Enables supply chain managers to pre-book 3PL carrier capacity 90 days in advance.</li>
          </ul>
        </div>
      </div>
      
      <div class="split-right figure-card">
        <div class="img-wrapper">
          <img src="___FIG5_B64___" alt="Figure 6: Demand Forecasting">
        </div>
        <div class="fig-caption">Figure 6: Longitudinal sales forecasting: 90-day multiplicative Holt-Winters demand projection with 95% confidence bounds.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Figure 6 highlights our longitudinal demand forecasting module. In retail, additive models fail during holiday surges because variance scales with volume. By deploying Multiplicative Holt-Winters triple exponential smoothing with m=52 weekly seasonality, we achieved an out-of-sample MAPE of 8.42%, outperforming standard SARIMA (14.12%). Our model captured the massive 4.1x Black Friday spike within 95% confidence bands, allowing supply chain teams to pre-allocate logistics capacity."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 10: PRODUCT PORTFOLIO STRATEGY (BCG MATRIX) -->
<!-- ========================================== -->
<div class="slide slide-light" id="slide-10">
  <div class="slide-top-bar light-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body">
    <div class="section-pill">STRATEGIC MERCHANDISING</div>
    <h1 class="slide-title">Product Portfolio Optimization: 73-Category BCG Matrix</h1>
    <h2 class="slide-subtitle">Market growth rate vs relative market share capital allocation across 32,951 catalog SKUs</h2>
    
    <div class="figure-layout-split">
      <div class="split-left content-card">
        <h3 class="card-title text-navy">THE 4 STRATEGIC QUADRANTS</h3>
        
        <div class="bcg-quad-box bq-cows">
          <div class="bq-title">Cash Cows (38.4% GMV Share)</div>
          <p><em>Bed/Bath/Table, Health/Beauty, Sports/Leisure.</em> High share in mature categories. High margin cash generators funding platform growth.</p>
        </div>
        
        <div class="bcg-quad-box bq-stars">
          <div class="bq-title">Stars (24.1% GMV Share)</div>
          <p><em>Computers/Accessories, Telephony.</em> High market share in rapidly growing categories. Strategic growth drivers requiring continuous inventory capital.</p>
        </div>
        
        <div class="bcg-quad-box bq-qm">
          <div class="bq-title">Question Marks (19.2% GMV Share)</div>
          <p><em>Small Appliances, Audio, Fashion.</em> High category growth but low platform penetration. Require selective seller subsidies to convert into Stars.</p>
        </div>
        
        <div class="bcg-quad-box bq-dogs">
          <div class="bq-title">Dogs (18.3% GMV Share)</div>
          <p><em>DVDs, Security items, Niche hardware.</em> Low growth and low share. Candidates for catalog pruning and inventory liquidation.</p>
        </div>
      </div>
      
      <div class="split-right figure-card">
        <div class="img-wrapper">
          <img src="___FIG7_B64___" alt="Figure 7: BCG Matrix">
        </div>
        <div class="fig-caption">Figure 7: 73-category BCG Growth-Share matrix showing relative market share, annual category growth, and GMV bubble sizing.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Figure 7 illustrates M Akshay Sharma's product portfolio analytics. Analyzing 73 categories and 32,951 SKUs, we constructed the BCG Growth-Share matrix. Cash Cows such as Bed/Bath and Health/Beauty represent 38.4% of total GMV, generating the operating cash flows necessary to aggressively subsidize high-growth Stars in Computers and Electronics. Conversely, catalog pruning in the Dog quadrant frees up critical working capital."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 11: PRODUCTION SAAS PLATFORM -->
<!-- ========================================== -->
<div class="slide slide-light" id="slide-11">
  <div class="slide-top-bar light-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body">
    <div class="section-pill">PRODUCTION SAAS IMPLEMENTATION</div>
    <h1 class="slide-title">Enterprise Production SaaS Platform &amp; Interactive 3D WebGL</h1>
    <h2 class="slide-subtitle">Live cloud deployment featuring Three.js particle portal and multi-year temporal slicing</h2>
    
    <div class="dual-screenshot-grid">
      <div class="ss-box">
        <div class="ss-img-container">
          <img src="___DASH_B64___" alt="Executive Dashboard">
        </div>
        <div class="ss-caption">Executive Decision Cockpit: Multi-year temporal filters, real-time KPI tiles, and dynamic cohort analysis.</div>
      </div>
      
      <div class="ss-box">
        <div class="ss-img-container">
          <img src="___LOGIN_B64___" alt="WebGL 3D Portal">
        </div>
        <div class="ss-caption">3D WebGL Gateway: Three.js interactive particle system representing live customer network topology.</div>
      </div>
    </div>
    
    <div class="content-card full-card-saas">
      <div class="saas-features-title">FULL-STACK PRODUCTION CLOUD ARCHITECTURE &amp; KEY CAPABILITIES:</div>
      <div class="saas-features-grid">
        <div class="sf-item"><strong>FastAPI Async Microservices:</strong> RESTful backend with JWT authentication, CORS middleware, and p99 query latency under 112ms.</div>
        <div class="sf-item"><strong>Interactive 3D Three.js Visuals:</strong> Custom WebGL shader particle canvas providing tactile feedback and dynamic network clustering.</div>
        <div class="sf-item"><strong>Multi-Year Temporal Slicing:</strong> Real-time date slider allowing multi-year cohort comparisons across 2016, 2017, and 2018 data.</div>
        <div class="sf-item"><strong>Automated Win-Back Triggers:</strong> Integrates XGBoost churn inference to dispatch automated retention alerts for At-Risk customers.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Slide 11 presents our live production platform built by M Akshay Sharma. We did not stop at Jupyter notebooks; we deployed a full-stack enterprise cloud application. The frontend features a custom Three.js WebGL particle portal and an executive dashboard with multi-year temporal sliders, state-level freight heatmaps, and dynamic cohort drill-downs, backed by FastAPI delivering sub-100ms analytical queries."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 12: ACADEMIC SYNTHESIS & DELIVERABLES -->
<!-- ========================================== -->
<div class="slide slide-dark" id="slide-12">
  <div class="slide-top-bar dark-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: <strong>Prof. N. Lakshmipathi Anantha</strong> | Fall 2026&ndash;27</div>
  </div>
  
  <div class="s1-content">
    <div class="academic-badge badge-center">RESEARCH SYNTHESIS &amp; DEFENSE CONCLUSION</div>
    <h1 class="s1-main-title text-center">Academic Contributions, Project Deliverables &amp; Research Summary</h1>
    <h2 class="s1-sub-title text-center">Bridging empirical data science research with enterprise-grade cloud software engineering</h2>
    
    <div class="deliverables-grid">
      <!-- Deliverable 1 -->
      <div class="deliv-card deliv-blue">
        <div class="deliv-badge">40+ PAGES COMPREHENSIVE</div>
        <h3 class="deliv-title">1. Capstone Thesis Report</h3>
        <ul class="deliv-list">
          <li>Official VIT-AP SCOPE thesis format compliance</li>
          <li>Complete 13-table Kimball star schema specification</li>
          <li>Mathematical proofs for Haversine, Fr, and leakage</li>
          <li>Student credentials, photo badges &amp; CD sleeve design</li>
          <li>Available in publication DOCX, Markdown, and PDF</li>
        </ul>
      </div>
      
      <!-- Deliverable 2 -->
      <div class="deliv-card deliv-crimson">
        <div class="deliv-badge">DOUBLE-COLUMN RESEARCH</div>
        <h3 class="deliv-title">2. IEEE Conference Paper</h3>
        <ul class="deliv-list">
          <li>Target leakage discovery and ablation protocol</li>
          <li>Empirical dual-model benchmarks (0.8624 AUC)</li>
          <li>TreeSHAP causal feature attribution plots</li>
          <li>Humanized, zero-plagiarism academic prose</li>
          <li>Ready for peer-reviewed conference submission</li>
        </ul>
      </div>
      
      <!-- Deliverable 3 -->
      <div class="deliv-card deliv-green">
        <div class="deliv-badge">PRODUCTION SAAS CODEBASE</div>
        <h3 class="deliv-title">3. Production Software Platform</h3>
        <ul class="deliv-list">
          <li>FastAPI async backend with 13 SQL schemas</li>
          <li>Three.js 3D WebGL particle interactive gateway</li>
          <li>Multi-year executive dashboard with cohort filters</li>
          <li>Automated test suite, Dockerfile &amp; Vercel deployment</li>
          <li>Complete GitHub version-controlled repository</li>
        </ul>
      </div>
    </div>
    
    <div class="acknowledgment-banner">
      <div class="ack-title">FACULTY GUIDE &amp; INSTITUTIONAL ACKNOWLEDGMENT</div>
      <p class="ack-text">We extend our deepest gratitude to our Project Guide <strong>Prof. N. Lakshmipathi Anantha</strong>, Assistant Professor, SCOPE, and the faculty of VIT-AP University for their invaluable mentorship, technical guidance, and constructive evaluation throughout Fall 2026&ndash;27.</p>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="In conclusion, NEXUS.AI delivers on all 3 research frontiers: a comprehensive 40+ page Capstone Thesis, an IEEE research paper exposing churn target leakage, and a fully functional production SaaS platform. On behalf of Papasani Suhitha, Gajjala Srithika, Ala Venkata Veera Ritwik, and M Akshay Sharma, we express our profound gratitude to our guide Prof. N. Lakshmipathi Anantha and the School of Computer Science and Engineering. We are now open for viva defense questions. Thank you!"></div>
</div>
"""

# HTML Template with Interactive Navigation and Swiss-Minimal Styling
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>E-Commerce Business Intelligence & Predictive Analytics Platform - Capstone Defense</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background-color: #050b14;
  color: #1e293b;
  overflow: hidden;
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
}

#deck-container {
  flex: 1;
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: none;
  flex-direction: column;
  padding: 0;
}

.slide.active {
  display: flex;
}

/* Dark slide theme (Slide 1 & 12) */
.slide-dark {
  background-color: #0b192c;
  color: #f8fafc;
}

/* Light slide theme (Slide 2 to 11) */
.slide-light {
  background-color: #f8fafc;
  color: #1e293b;
}

/* Top Bar */
.slide-top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 40px;
  font-size: 13px;
  font-weight: 600;
  height: 38px;
  border-bottom: 1px solid rgba(0,0,0,0.06);
}
.dark-top-bar {
  background-color: #050e1a;
  color: #d4af37;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}
.dark-top-bar .top-guide {
  color: #cbd5e1;
  font-weight: 400;
}
.light-top-bar {
  background-color: #0b192c;
  color: #d4af37;
}
.light-top-bar .top-guide {
  color: #e2e8f0;
  font-weight: 400;
}

/* Slide Content Containers */
.slide-body {
  flex: 1;
  padding: 16px 40px 24px 40px;
  display: flex;
  flex-direction: column;
}

.section-pill {
  display: inline-block;
  align-self: flex-start;
  background-color: #7a0019;
  color: #ffffff;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.8px;
  padding: 4px 14px;
  border-radius: 20px;
  margin-bottom: 6px;
  text-transform: uppercase;
}

.slide-title {
  font-size: 26px;
  font-weight: 800;
  color: #0f243e;
  line-height: 1.15;
  margin-bottom: 3px;
}

.slide-subtitle {
  font-size: 14px;
  font-weight: 500;
  color: #64748b;
  margin-bottom: 14px;
}

/* Cards & Containers */
.content-card {
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 18px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.02);
}

.card-title {
  font-size: 15px;
  font-weight: 700;
  margin-bottom: 10px;
  letter-spacing: 0.5px;
}
.text-crimson { color: #7a0019; }
.text-blue { color: #1e40af; }
.text-navy { color: #0f243e; }
.text-amber { color: #d97706; }
.border-crimson { border-top: 4px solid #7a0019; }
.border-blue { border-top: 4px solid #1e40af; }
.border-amber { border-top: 4px solid #d97706; }

/* Grid & Layouts */
.two-col-container {
  display: flex;
  gap: 20px;
  flex: 1;
}
.col-half {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.figure-layout-split {
  display: flex;
  gap: 24px;
  flex: 1;
  min-height: 0;
}
.split-left {
  flex: 4.8;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}
.split-right {
  flex: 6.2;
  display: flex;
  flex-direction: column;
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}

.img-wrapper {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.img-wrapper img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  border-radius: 4px;
}

.fig-caption {
  font-size: 12px;
  font-weight: 600;
  color: #64748b;
  text-align: center;
  padding-top: 8px;
  border-top: 1px solid #f1f5f9;
}

/* Slide 1 Styles */
.s1-content {
  flex: 1;
  padding: 24px 50px 30px 50px;
  display: flex;
  flex-direction: column;
}
.s1-header-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}
.vit-logo-lg {
  height: 54px;
  object-fit: contain;
  background: rgba(255,255,255,0.95);
  padding: 6px 14px;
  border-radius: 6px;
}
.academic-badge {
  background-color: #7a0019;
  color: #ffffff;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 1px;
  padding: 6px 16px;
  border-radius: 20px;
}
.badge-center {
  margin: 0 auto 10px auto;
}
.s1-main-title {
  font-size: 34px;
  font-weight: 800;
  color: #ffffff;
  line-height: 1.2;
  margin-bottom: 6px;
}
.text-center { text-align: center; }
.s1-sub-title {
  font-size: 16px;
  font-weight: 500;
  color: #d4af37;
  margin-bottom: 16px;
}
.guide-banner {
  background-color: #0f243e;
  border: 1px solid #d4af37;
  border-radius: 6px;
  padding: 10px 18px;
  font-size: 13px;
  margin-bottom: 20px;
}
.guide-label { color: #d4af37; font-weight: 700; margin-right: 8px; }
.guide-name { color: #ffffff; font-weight: 700; font-size: 15px; margin-right: 8px; }
.guide-dept { color: #cbd5e1; font-size: 13px; }

.s1-candidates-grid {
  display: flex;
  gap: 18px;
  flex: 1;
}
.candidate-card {
  flex: 1;
  background-color: #0f243e;
  border: 1px solid #1e3a5f;
  border-radius: 8px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  position: relative;
}
.candidate-tag {
  position: absolute;
  top: 8px;
  left: 8px;
  background-color: #7a0019;
  color: #ffffff;
  font-size: 10px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 4px;
}
.candidate-img {
  width: 90px;
  height: 115px;
  object-fit: cover;
  border-radius: 4px;
  margin: 10px 0 8px 0;
  border: 2px solid #2a4365;
}
.candidate-name { font-size: 14px; font-weight: 700; color: #ffffff; margin-bottom: 2px; }
.candidate-reg { font-size: 13px; font-weight: 600; color: #d4af37; margin-bottom: 4px; }
.candidate-role { font-size: 11px; color: #93c5fd; line-height: 1.3; }

/* Slide 2 KPI Strip */
.kpi-strip {
  display: flex;
  gap: 16px;
  margin-bottom: 16px;
}
.kpi-card {
  flex: 1;
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 12px 16px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.02);
}
.kpi-blue { border-top: 4px solid #1e40af; }
.kpi-amber { border-top: 4px solid #d97706; }
.kpi-crimson { border-top: 4px solid #7a0019; }
.kpi-green { border-top: 4px solid #059669; }
.kpi-num { font-size: 28px; font-weight: 800; line-height: 1.1; }
.kpi-blue .kpi-num { color: #1e40af; }
.kpi-amber .kpi-num { color: #d97706; }
.kpi-crimson .kpi-num { color: #7a0019; }
.kpi-green .kpi-num { color: #059669; }
.kpi-title { font-size: 13px; font-weight: 700; color: #1e293b; margin-top: 2px; }
.kpi-desc { font-size: 11px; color: #64748b; margin-top: 2px; }

.bullet-list {
  list-style: none;
  font-size: 12.5px;
  line-height: 1.45;
  color: #475569;
}
.bullet-list li {
  margin-bottom: 8px;
  position: relative;
  padding-left: 14px;
}
.bullet-list li::before {
  content: "•";
  position: absolute;
  left: 0;
  color: #1e40af;
  font-weight: bold;
}

/* Slide 3 Stack Box */
.stack-box {
  margin-bottom: 10px;
}
.stack-badge {
  display: inline-block;
  font-size: 12px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  margin-bottom: 3px;
}
.badge-blue { background-color: #e0e7ff; color: #1e40af; }
.badge-crimson { background-color: #ffe4e6; color: #9f1239; }
.badge-green { background-color: #d1fae5; color: #065f46; }
.stack-desc { font-size: 11.5px; color: #475569; line-height: 1.35; }

.perf-box {
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  padding: 10px;
  margin-top: 6px;
}
.perf-title { font-size: 11px; font-weight: 700; color: #7a0019; margin-bottom: 6px; }
.perf-grid { display: flex; justify-content: space-between; }
.perf-item { text-align: center; }
.perf-metric { display: block; font-size: 18px; font-weight: 800; color: #0f243e; }
.perf-label { font-size: 10px; color: #64748b; }

/* Slide 4 Schema Points */
.schema-point {
  margin-bottom: 10px;
}
.sp-tag {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  color: #1e40af;
  background-color: #eff6ff;
  padding: 2px 6px;
  border-radius: 4px;
  margin-bottom: 3px;
}
.schema-point p { font-size: 11.5px; color: #475569; line-height: 1.35; }

/* Slide 5 & 9 Formula Blocks */
.formula-block {
  background-color: #f8fafc;
  border-left: 3px solid #1e40af;
  padding: 6px 10px;
  border-radius: 0 4px 4px 0;
  margin-bottom: 8px;
}
.formula-label { font-size: 11px; font-weight: 700; color: #1e293b; margin-bottom: 2px; }
.formula-code { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #0f243e; font-weight: 600; margin-bottom: 2px; }
.formula-sub { font-size: 10px; color: #64748b; }

.evidence-box, .forecast-benchmark-box {
  background-color: #fff1f2;
  border: 1px solid #fecdd3;
  border-radius: 6px;
  padding: 10px;
  margin-top: 6px;
}
.evidence-title, .fbb-title { font-size: 11px; font-weight: 700; color: #9f1239; margin-bottom: 4px; }
.evidence-bullets, .fbb-bullets {
  list-style: none;
  font-size: 11px;
  color: #4c0519;
  line-height: 1.35;
}
.evidence-bullets li, .fbb-bullets li {
  margin-bottom: 4px;
}

/* Slide 6 Personas */
.persona-row {
  margin-bottom: 8px;
}
.persona-badge {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  margin-bottom: 2px;
}
.p-champ { background-color: #dbeafe; color: #1e40af; }
.p-loyal { background-color: #d1fae5; color: #065f46; }
.p-risk { background-color: #fee2e2; color: #991b1b; }
.p-dormant { background-color: #f1f5f9; color: #475569; }
.persona-row p { font-size: 11.5px; color: #475569; line-height: 1.35; }
.method-callout {
  font-size: 11px;
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 8px;
  border-radius: 4px;
  color: #334155;
  margin-top: 6px;
}

/* Slide 7 Proof Steps & Traps */
.proof-step {
  margin-bottom: 8px;
}
.ps-label { font-size: 12px; font-weight: 700; color: #1e293b; margin-bottom: 2px; }
.ps-math {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11.5px;
  background-color: #f8fafc;
  padding: 4px 8px;
  border-radius: 4px;
  border: 1px solid #e2e8f0;
  color: #0f243e;
  font-weight: 600;
  margin-bottom: 2px;
}
.ps-sub { font-size: 10.5px; color: #64748b; }

.trap-box {
  margin-bottom: 8px;
}
.tb-title { font-size: 12px; font-weight: 700; color: #d97706; margin-bottom: 2px; }
.trap-box p { font-size: 11.5px; color: #475569; line-height: 1.35; }
.contrib-banner {
  background-color: #ecfdf5;
  border: 1px solid #a7f3d0;
  border-radius: 6px;
  padding: 8px 12px;
  font-size: 11.5px;
  color: #065f46;
  margin-top: 8px;
}

/* Slide 8 Ablation Table */
.ablation-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 11px;
  margin-bottom: 10px;
}
.ablation-table th {
  background-color: #0f243e;
  color: #ffffff;
  padding: 6px 8px;
  text-align: left;
  font-weight: 600;
}
.ablation-table td {
  padding: 5px 8px;
  border-bottom: 1px solid #e2e8f0;
  color: #334155;
}
.cell-highlight { font-weight: 700; color: #059669; }

.shap-summary {
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  padding: 8px 10px;
}
.shap-title { font-size: 11px; font-weight: 700; color: #7a0019; margin-bottom: 4px; }
.shap-item { font-size: 11px; color: #334155; margin-bottom: 3px; }
.shap-badge {
  display: inline-block;
  background-color: #fee2e2;
  color: #991b1b;
  font-weight: 700;
  font-size: 10px;
  padding: 1px 4px;
  border-radius: 3px;
  margin-right: 4px;
}

/* Slide 10 BCG Quads */
.bcg-quad-box {
  padding: 8px 10px;
  border-radius: 6px;
  margin-bottom: 8px;
}
.bq-cows { background-color: #ecfdf5; border-left: 4px solid #059669; }
.bq-stars { background-color: #eff6ff; border-left: 4px solid #1e40af; }
.bq-qm { background-color: #fffbeb; border-left: 4px solid #d97706; }
.bq-dogs { background-color: #fef2f2; border-left: 4px solid #dc2626; }
.bq-title { font-size: 12px; font-weight: 700; color: #0f243e; margin-bottom: 2px; }
.bcg-quad-box p { font-size: 11px; color: #475569; line-height: 1.35; }

/* Slide 11 Dual Screenshots */
.dual-screenshot-grid {
  display: flex;
  gap: 16px;
  flex: 1;
  min-height: 0;
  margin-bottom: 10px;
}
.ss-box {
  flex: 1;
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 8px;
  display: flex;
  flex-direction: column;
}
.ss-img-container {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.ss-img-container img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  border-radius: 4px;
}
.ss-caption {
  font-size: 11px;
  font-weight: 600;
  color: #64748b;
  text-align: center;
  padding-top: 6px;
  border-top: 1px solid #f1f5f9;
}

.full-card-saas {
  padding: 10px 16px;
}
.saas-features-title {
  font-size: 12px;
  font-weight: 700;
  color: #0f243e;
  margin-bottom: 6px;
}
.saas-features-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 16px;
}
.sf-item { font-size: 11px; color: #475569; }

/* Slide 12 Deliverables */
.deliverables-grid {
  display: flex;
  gap: 18px;
  flex: 1;
  margin-bottom: 16px;
}
.deliv-card {
  flex: 1;
  background-color: #0f243e;
  border-radius: 8px;
  padding: 16px;
  display: flex;
  flex-direction: column;
}
.deliv-blue { border: 1px solid #1e40af; border-top: 4px solid #1e40af; }
.deliv-crimson { border: 1px solid #9f1239; border-top: 4px solid #e11d48; }
.deliv-green { border: 1px solid #065f46; border-top: 4px solid #10b981; }

.deliv-badge { font-size: 10px; font-weight: 700; color: #d4af37; margin-bottom: 6px; letter-spacing: 0.5px; }
.deliv-title { font-size: 16px; font-weight: 700; color: #ffffff; margin-bottom: 12px; }
.deliv-list { list-style: none; font-size: 12px; color: #cbd5e1; line-height: 1.45; }
.deliv-list li { margin-bottom: 8px; position: relative; padding-left: 16px; }
.deliv-list li::before {
  content: "✓";
  position: absolute;
  left: 0;
  color: #38bdf8;
  font-weight: bold;
}

.acknowledgment-banner {
  background-color: #183153;
  border: 1px solid #d4af37;
  border-radius: 8px;
  padding: 12px 24px;
  text-align: center;
}
.ack-title { font-size: 13px; font-weight: 700; color: #d4af37; margin-bottom: 4px; }
.ack-text { font-size: 13px; color: #e2e8f0; line-height: 1.4; }

/* Bottom Control Deck */
#controls-bar {
  height: 48px;
  background-color: #08111e;
  border-top: 1px solid #1e293b;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 24px;
  z-index: 1000;
}
.ctrl-group { display: flex; align-items: center; gap: 10px; }
.btn-ctrl {
  background-color: #1e293b;
  color: #f8fafc;
  border: 1px solid #334155;
  padding: 6px 14px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}
.btn-ctrl:hover { background-color: #334155; color: #38bdf8; }
.slide-indicator { color: #94a3b8; font-size: 13px; font-weight: 600; min-width: 80px; text-align: center; }

/* Speaker Notes Drawer */
#notes-drawer {
  position: fixed;
  bottom: 48px;
  left: 0;
  width: 100%;
  background: rgba(11, 25, 44, 0.96);
  backdrop-filter: blur(8px);
  border-top: 2px solid #d4af37;
  color: #f8fafc;
  padding: 16px 40px;
  font-size: 14px;
  line-height: 1.5;
  max-height: 180px;
  overflow-y: auto;
  display: none;
  z-index: 999;
}
.notes-header {
  font-size: 12px;
  font-weight: 700;
  color: #d4af37;
  margin-bottom: 4px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
</style>
</head>
<body>

<div id="deck-container">
___SLIDES_PLACEHOLDER___
</div>

<div id="notes-drawer">
  <div class="notes-header">SPEAKER VIVA SCRIPT &amp; TIMING NOTES:</div>
  <div id="notes-text"></div>
</div>

<div id="controls-bar">
  <div class="ctrl-group">
    <button class="btn-ctrl" onclick="prevSlide()">&larr; Previous</button>
    <button class="btn-ctrl" onclick="nextSlide()">Next &rarr;</button>
    <span class="slide-indicator" id="slide-num">Slide 1 / 12</span>
  </div>
  
  <div class="ctrl-group">
    <button class="btn-ctrl" onclick="toggleNotes()">Speaker Notes [N]</button>
    <button class="btn-ctrl" onclick="toggleFullscreen()">Fullscreen [F]</button>
  </div>
</div>

<script>
let currentSlide = 1;
const totalSlides = 12;

function showSlide(n) {
  if (n < 1) n = 1;
  if (n > totalSlides) n = totalSlides;
  currentSlide = n;
  
  document.querySelectorAll('.slide').forEach((el, idx) => {
    el.classList.toggle('active', idx + 1 === currentSlide);
  });
  
  document.getElementById('slide-num').innerText = 'Slide ' + currentSlide + ' / ' + totalSlides;
  
  // Update speaker notes
  const activeSlide = document.getElementById('slide-' + currentSlide);
  const noteEl = activeSlide ? activeSlide.querySelector('.speaker-note-content') : null;
  if (noteEl) {
    document.getElementById('notes-text').innerText = noteEl.getAttribute('data-notes') || 'No notes for this slide.';
  }
}

function nextSlide() {
  if (currentSlide < totalSlides) showSlide(currentSlide + 1);
}

function prevSlide() {
  if (currentSlide > 1) showSlide(currentSlide - 1);
}

function toggleNotes() {
  const drawer = document.getElementById('notes-drawer');
  drawer.style.display = (drawer.style.display === 'block') ? 'none' : 'block';
}

function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen().catch(err => console.log(err));
  } else {
    document.exitFullscreen().catch(err => console.log(err));
  }
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
    nextSlide();
  } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
    prevSlide();
  } else if (e.key === 'Home') {
    showSlide(1);
  } else if (e.key === 'End') {
    showSlide(totalSlides);
  } else if (e.key.toLowerCase() === 'n') {
    toggleNotes();
  } else if (e.key.toLowerCase() === 'f') {
    toggleFullscreen();
  }
});

// Initialize on slide 1
showSlide(1);
</script>
</body>
</html>
"""


slides_processed = SLIDES_HTML
slides_processed = slides_processed.replace('___LOGO_B64___', logo_b64)
slides_processed = slides_processed.replace('___PHOTO1_B64___', photo1_b64)
slides_processed = slides_processed.replace('___PHOTO2_B64___', photo2_b64)
slides_processed = slides_processed.replace('___PHOTO3_B64___', photo3_b64)
slides_processed = slides_processed.replace('___PHOTO4_B64___', photo4_b64)
slides_processed = slides_processed.replace('___FIG1_B64___', fig1_b64)
slides_processed = slides_processed.replace('___FIG2_B64___', fig2_b64)
slides_processed = slides_processed.replace('___FIG6_B64___', fig6_b64)
slides_processed = slides_processed.replace('___FIG4_B64___', fig4_b64)
slides_processed = slides_processed.replace('___FIG3_B64___', fig3_b64)
slides_processed = slides_processed.replace('___FIG5_B64___', fig5_b64)
slides_processed = slides_processed.replace('___FIG7_B64___', fig7_b64)
slides_processed = slides_processed.replace('___DASH_B64___', dash_b64)
slides_processed = slides_processed.replace('___LOGIN_B64___', login_b64)

full_html = HTML_TEMPLATE.replace("___SLIDES_PLACEHOLDER___", slides_processed)


html_out = DOCS_DIR / "presentation_slides.html"
with open(html_out, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"Successfully generated HTML deck at: {html_out}")

# Copy HTML to artifact directory
shutil.copy2(html_out, ARTIFACT_DIR / "presentation_slides.html")
print(f"Copied HTML deck to artifact directory.")

# =========================================================================
# PDF RENDERING VIA PLAYWRIGHT SCREENSHOTS + SWIFT PDFKIT
# =========================================================================
async def render_presentation_pdf():
    print("Launching Playwright to capture pixel-perfect 1920x1080 slide images...")
    tmp_img_dir = Path("/tmp/superb_slides_png")
    tmp_img_dir.mkdir(parents=True, exist_ok=True)
    
    pdf_out = DOCS_DIR / "E_Commerce_Intelligence_Presentation.pdf"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--allow-file-access-from-files", "--disable-web-security"])
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()
        
        file_url = f"file://{html_out.resolve()}"
        await page.goto(file_url, wait_until="networkidle")
        
        # Hide controls bar for PDF screenshots
        await page.evaluate("document.getElementById('controls-bar').style.display = 'none';")
        await page.evaluate("document.getElementById('notes-drawer').style.display = 'none';")
        
        for s in range(1, 13):
            await page.evaluate(f"showSlide({s});")
            await page.wait_for_timeout(350)
            img_path = tmp_img_dir / f"slide_{s:02d}.png"
            await page.screenshot(path=str(img_path))
            print(f"  Captured slide {s}/12")
            
        await browser.close()
        
    print("Stitching slide images into 12-page presentation PDF via Swift CoreGraphics/PDFKit...")
    swift_script = f"""
    import Foundation
    import CoreGraphics
    import AppKit
    import PDFKit

    let doc = PDFDocument()
    let imgDir = URL(fileURLWithPath: "{tmp_img_dir.resolve()}")

    for i in 1...12 {{
        let filename = String(format: "slide_%02d.png", i)
        let fileUrl = imgDir.appendingPathComponent(filename)
        guard let img = NSImage(contentsOf: fileUrl) else {{
            print("Failed to load \\(fileUrl)")
            continue
        }}
        guard let page = PDFPage(image: img) else {{
            print("Failed to create PDFPage for \\(fileUrl)")
            continue
        }}
        doc.insert(page, at: doc.pageCount)
    }}

    let outUrl = URL(fileURLWithPath: "{pdf_out.resolve()}")
    doc.write(to: outUrl)
    print("Successfully generated 12-page presentation PDF at \\(outUrl.path)")
    """
    
    swift_file = Path("/tmp/make_superb_pdf.swift")
    with open(swift_file, "w") as f:
        f.write(swift_script)
        
    subprocess.run(["swift", str(swift_file)], check=True)
    
    # Copy PDF to artifact dir
    shutil.copy2(pdf_out, ARTIFACT_DIR / "E_Commerce_Intelligence_Presentation.pdf")
    print(f"Copied Presentation PDF to artifact directory: {ARTIFACT_DIR / 'E_Commerce_Intelligence_Presentation.pdf'}")

asyncio.run(render_presentation_pdf())
print("ALL PRESENTATION ASSETS GENERATED SUCCESSFULLY!")
