#!/usr/bin/env python3
"""
generate_brushstroke_html_and_pdf.py
Builds the 12-slide interactive HTML deck and PDF in the exact
Blue Oil Paint Brushstroke & Gold Wireframe theme from the user's reference image.
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

hero_brush_b64 = b64_img(ASSETS_DIR / "brushstroke_hero_transparent.png")
small_brush_b64 = b64_img(ASSETS_DIR / "brushstroke_small_badge.png")

fig1_b64 = b64_img(FIG_DIR / "fig1_system_architecture.png")
fig2_b64 = b64_img(FIG_DIR / "fig2_star_schema.png")
fig6_b64 = b64_img(FIG_DIR / "fig6_regional_economics.png")
fig4_b64 = b64_img(FIG_DIR / "fig4_kmeans_pca_elbow.png")
fig3_b64 = b64_img(FIG_DIR / "fig3_churn_roc_feature_importance.png")
fig5_b64 = b64_img(FIG_DIR / "fig5_revenue_forecasting.png")
fig7_b64 = b64_img(FIG_DIR / "fig7_category_bcg_matrix.png")
dash_b64 = b64_img(FIG_DIR / "screenshot_dashboard.png")
login_b64 = b64_img(FIG_DIR / "screenshot_login.png")

print("Building Brushstroke & Gold Wireframe 12-slide HTML presentation deck...")

SLIDES_HTML = """
<!-- ========================================== -->
<!-- SLIDE 1: COVER (BLUE BRUSHSTROKE & GOLD FRAME) -->
<!-- ========================================== -->
<div class="slide slide-white" id="slide-1">
  <div class="slide-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCHOOL OF COMPUTER SCIENCE AND ENGINEERING (SCOPE)</div>
    <div class="top-guide">Faculty Guide: <strong>Prof. N. Lakshmipathi Anantha</strong> | Fall 2026&ndash;27</div>
  </div>
  
  <div class="s1-brush-content">
    <div class="s1-logo-row">
      <img src="___LOGO_B64___" class="vit-logo-brush" alt="VIT-AP Logo">
      <span class="gold-wire-badge">B.TECH CAPSTONE THESIS DEFENSE</span>
    </div>
    
    <!-- Hero Oil Paint Brushstroke with Gold Wireframe Box -->
    <div class="hero-brush-container">
      <div class="gold-frame-behind"></div>
      <img src="___HERO_BRUSH_B64___" class="hero-brush-img" alt="Blue Oil Paint Brushstroke">
      <div class="hero-brush-text">
        <div class="hbt-tag">B . T E C H   C A P S T O N E   D E F E N S E</div>
        <div class="hbt-main">E-COMMERCE INTELLIGENCE</div>
        <div class="hbt-sub">&amp; PREDICTIVE ANALYTICS PLATFORM</div>
      </div>
    </div>
    
    <div class="s1-sub-line">Enterprise Kimball Data Warehouse, Geospatial Freight Telemetry, Target Leakage Ablation &amp; Production Cloud SaaS</div>
    
    <div class="guide-box-gold">
      <span class="gb-label">FACULTY PROJECT GUIDE:</span>
      <span class="gb-name">Prof. N. Lakshmipathi Anantha</span>
      <span class="gb-dept">| Assistant Professor, School of Computer Science and Engineering (SCOPE), VIT-AP University</span>
    </div>
    
    <div class="candidates-grid-brush">
      <!-- Suhitha -->
      <div class="cand-card-b">
        <div class="gold-inner-frame"></div>
        <div class="cand-num-b">#1</div>
        <img src="___PHOTO1_B64___" class="cand-photo-b" alt="Papasani Suhitha">
        <div class="cand-name-b">Papasani Suhitha</div>
        <div class="cand-reg-b">23BCE7826</div>
        <div class="cand-role-b">Data Engineering &amp; Star Schema</div>
      </div>
      
      <!-- Srithika -->
      <div class="cand-card-b">
        <div class="gold-inner-frame"></div>
        <div class="cand-num-b">#2</div>
        <img src="___PHOTO2_B64___" class="cand-photo-b" alt="Gajjala Srithika">
        <div class="cand-name-b">Gajjala Srithika</div>
        <div class="cand-reg-b">23BCE7911</div>
        <div class="cand-role-b">Customer Intelligence &amp; RFM</div>
      </div>
      
      <!-- Ritwik -->
      <div class="cand-card-b">
        <div class="gold-inner-frame"></div>
        <div class="cand-num-b">#3</div>
        <img src="___PHOTO3_B64___" class="cand-photo-b" alt="Ala Venkata Veera Ritwik">
        <div class="cand-name-b">Ala Venkata Veera Ritwik</div>
        <div class="cand-reg-b">23BCE9633</div>
        <div class="cand-role-b">ML Churn Leakage &amp; Forecasting</div>
      </div>
      
      <!-- Akshay -->
      <div class="cand-card-b">
        <div class="gold-inner-frame"></div>
        <div class="cand-num-b">#4</div>
        <img src="___PHOTO4_B64___" class="cand-photo-b" alt="M Akshay Sharma">
        <div class="cand-name-b">M Akshay Sharma</div>
        <div class="cand-reg-b">23BCE9668</div>
        <div class="cand-role-b">Product Analytics &amp; WebGL SaaS</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Good morning respected Faculty Guide Prof. N. Lakshmipathi Anantha and honorable evaluators. We are team NEXUS.AI presenting our Capstone Project: E-Commerce Business Intelligence & Predictive Analytics Platform. Our team consists of Papasani Suhitha (Data Engineering), Gajjala Srithika (Customer Intelligence), Ala Venkata Veera Ritwik (Machine Learning & Forecasting), and M Akshay Sharma (Product Analytics & WebGL Platform). Today we present an end-to-end enterprise solution addressing silent customer churn, target leakage, and geospatial logistics friction."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 2: THE SILENT CHURN DILEMMA -->
<!-- ========================================== -->
<div class="slide slide-white" id="slide-2">
  <div class="slide-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body-b">
    <div class="header-brush-row">
      <img src="___SMALL_BRUSH_B64___" class="small-brush-icon" alt="Brush Badge">
      <div class="header-brush-text">
        <div class="tag-spaced">P R O B L E M   S T A T E M E N T</div>
        <h1 class="slide-title-b">The Silent Churn Dilemma in Non-Contractual Retail</h1>
      </div>
    </div>
    <div class="slide-sub-b">Why top-line GMV expansion conceals destructive 96.9% one-time buyer attrition</div>
    
    <div class="kpi-strip-b">
      <div class="kpi-box-b">
        <div class="gold-inner-frame"></div>
        <div class="kpi-val-b text-blue">99,441</div>
        <div class="kpi-title-b">Validated Orders</div>
        <div class="kpi-desc-b">R$ 15.8M Gross Merchandise Value</div>
      </div>
      <div class="kpi-box-b">
        <div class="gold-inner-frame"></div>
        <div class="kpi-val-b text-crimson">96.9%</div>
        <div class="kpi-title-b">Single-Purchase Rate</div>
        <div class="kpi-desc-b">Silent attrition: 97/100 never return</div>
      </div>
      <div class="kpi-box-b">
        <div class="gold-inner-frame"></div>
        <div class="kpi-val-b text-amber">20.4%</div>
        <div class="kpi-title-b">Mean Freight Ratio</div>
        <div class="kpi-desc-b">Freight Fr > 0.20 drives churn</div>
      </div>
      <div class="kpi-box-b">
        <div class="gold-inner-frame"></div>
        <div class="kpi-val-b text-green">73</div>
        <div class="kpi-title-b">Product Categories</div>
        <div class="kpi-desc-b">32,951 SKUs across 27 federal states</div>
      </div>
    </div>
    
    <div class="two-col-b">
      <div class="col-left-box-b">
        <div class="gold-inner-frame"></div>
        <h3 class="box-title-b text-crimson">THE NON-CONTRACTUAL BLINDSPOT</h3>
        <p class="para-b">In SaaS or subscription businesses, customer churn is explicit (marked by a cancellation trigger). In non-contractual e-commerce, customer departure is completely silent.</p>
        <p class="para-b">While aggregate platform GMV was growing at 14.8% annually, 96.9% of customers made only one purchase. Traditional CRMs mistook customer dormancy for retention, leading to wasted marketing spend and high CAC.</p>
        <p class="para-b">Our objective was to establish an enterprise data warehouse and deploy leak-free machine learning to diagnose and solve this silent churn.</p>
      </div>
      
      <div class="col-right-steps-b">
        <!-- Step 1 -->
        <div class="step-row-b">
          <div class="circle-badge-b">1</div>
          <div class="step-card-b">
            <div class="gold-inner-frame"></div>
            <div class="sc-title-b">Silent Non-Contractual Attrition</div>
            <div class="sc-desc-b">96.9% of customers made exactly one purchase and departed without explicit notification.</div>
          </div>
        </div>
        
        <!-- Step 2 -->
        <div class="step-row-b">
          <div class="circle-badge-b">2</div>
          <div class="step-card-b">
            <div class="gold-inner-frame"></div>
            <div class="sc-title-b">Deceptive GMV Growth Signaling</div>
            <div class="sc-desc-b">Top-line revenue expansion hid chronic customer defection, inflating acquisition costs by 3.4x.</div>
          </div>
        </div>
        
        <!-- Step 3 -->
        <div class="step-row-b">
          <div class="circle-badge-b">3</div>
          <div class="step-card-b">
            <div class="gold-inner-frame"></div>
            <div class="sc-title-b">Geospatial Logistics Friction Penalty</div>
            <div class="sc-desc-b">Freight ratio exceeding 20% of cart value triggered severe 1-star review surges.</div>
          </div>
        </div>
        
        <!-- Step 4 -->
        <div class="step-row-b">
          <div class="circle-badge-b">4</div>
          <div class="step-card-b">
            <div class="gold-inner-frame"></div>
            <div class="sc-title-b">OLTP Database Concurrency Bottlenecks</div>
            <div class="sc-desc-b">Operational databases locked under heavy aggregation and lacked longitudinal cohort storage.</div>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="In non-contractual retail, customers never inform you when they leave. Over 96.9% of our 99,441 customers made exactly one purchase. Standard dashboards celebrate top-line GMV while hiding bleeding churn. Our objective was to establish an enterprise data warehouse, uncover the math of target leakage that invalidates prior ML churn studies, and deliver an actionable decision platform."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 3: SYSTEM ARCHITECTURE -->
<!-- ========================================== -->
<div class="slide slide-white" id="slide-3">
  <div class="slide-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body-b">
    <div class="header-brush-row">
      <img src="___SMALL_BRUSH_B64___" class="small-brush-icon" alt="Brush Badge">
      <div class="header-brush-text">
        <div class="tag-spaced">S Y S T E M   A R C H I T E C T U R E</div>
        <h1 class="slide-title-b">Decoupled 3-Tier Enterprise Data &amp; Inference Architecture</h1>
      </div>
    </div>
    <div class="slide-sub-b">Unified pipeline from raw transaction ingestion to low-latency analytical serving</div>
    
    <div class="two-col-fig-b">
      <div class="col-text-box-b">
        <div class="gold-inner-frame"></div>
        <h3 class="box-title-b text-black">THE 3-TIER ARCHITECTURAL STACK</h3>
        
        <div class="tier-card-b">
          <div class="t-badge-b">Tier 1: Ingestion &amp; Data Staging</div>
          <div class="t-desc-b">9 raw CSV transactional tables validated via SHA-256 data integrity checks, UTF-8 cleansing, and Haversine geospatial calculations. Ingestion rate: <strong>28,500 rec/sec</strong>.</div>
        </div>
        
        <div class="tier-card-b">
          <div class="t-badge-b">Tier 2: Kimball Star Schema Warehouse</div>
          <div class="t-desc-b">13-table PostgreSQL dimensional database using 32-bit surrogate integer keys and indexed foreign relations. Eliminates string joins and delivers sub-120ms aggregation.</div>
        </div>
        
        <div class="tier-card-b">
          <div class="t-badge-b">Tier 3: Analytics Inference &amp; WebGL SaaS</div>
          <div class="t-desc-b">FastAPI asynchronous backend serving leak-free ML pipelines (XGBoost, K-Means, Holt-Winters). React executive cockpit with Three.js WebGL particle gateway.</div>
        </div>
        
        <div class="perf-strip-b">
          <div class="ps-title-b">PRODUCTION PERFORMANCE TELEMETRY:</div>
          <div class="ps-grid-b">
            <div><strong>28,500</strong><span>rows/sec ingestion</span></div>
            <div><strong>84ms</strong><span>p95 query latency</span></div>
            <div><strong>112ms</strong><span>p99 API response</span></div>
          </div>
        </div>
      </div>
      
      <div class="col-fig-box-b">
        <div class="gold-inner-frame"></div>
        <div class="fig-img-b">
          <img src="___FIG1_B64___" alt="Figure 1: System Architecture">
        </div>
        <div class="fig-cap-b">Figure 1: End-to-end 3-tier enterprise architecture showing data staging, star schema, and inference engines.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Figure 1 illustrates our decoupled 3-tier architecture. In Tier 1, Papasani Suhitha built an ingestion pipeline capable of processing 28,500 records per second with automated UTF-8 cleansing and Haversine distance calculations. Tier 2 is our 13-table PostgreSQL Kimball star schema. Tier 3 hosts the analytical models and FastAPI endpoints delivering p95 latencies under 84ms."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 4: 13-TABLE STAR SCHEMA -->
<!-- ========================================== -->
<div class="slide slide-white" id="slide-4">
  <div class="slide-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body-b">
    <div class="header-brush-row">
      <img src="___SMALL_BRUSH_B64___" class="small-brush-icon" alt="Brush Badge">
      <div class="header-brush-text">
        <div class="tag-spaced">D A T A   W A R E H O U S I N G</div>
        <h1 class="slide-title-b">13-Table Relational PostgreSQL Star Schema</h1>
      </div>
    </div>
    <div class="slide-sub-b">Surrogate key architecture eliminating 32-character hexadecimal string join bottlenecks</div>
    
    <div class="two-col-fig-b">
      <div class="col-text-box-b">
        <div class="gold-inner-frame"></div>
        <h3 class="box-title-b text-black">ENTERPRISE DIMENSIONAL CATALOG</h3>
        
        <div class="schema-item-b">
          <div class="si-tag-b">Grain Isolation</div>
          <div class="si-desc-b"><strong>5 Central Fact Tables:</strong> <code>fact_orders</code> (1 row/order), <code>fact_order_items</code> (line items), <code>fact_order_payments</code>, <code>fact_order_reviews</code>, and <code>fact_daily_sales</code>.</div>
        </div>
        
        <div class="schema-item-b">
          <div class="si-tag-b">Surrogate Key Optimization</div>
          <div class="si-desc-b">Replaced 32-character hex UUIDs with 32-bit <code>SERIAL INT</code> surrogate keys (<code>customer_key</code>, <code>seller_key</code>, <code>product_key</code>), reducing B-Tree index size by <strong>68.4%</strong> and accelerating JOIN queries by <strong>4.2x</strong>.</div>
        </div>
        
        <div class="schema-item-b">
          <div class="si-tag-b">Conformed Dimensions</div>
          <div class="si-desc-b"><strong>7 Conformed Dimensions:</strong> <code>dim_customers</code>, <code>dim_sellers</code>, <code>dim_products</code>, <code>dim_geography</code>, <code>dim_date</code>, <code>dim_payment_types</code>, and <code>dim_order_status</code> guarantee slice-and-dice consistency.</div>
        </div>
        
        <div class="schema-item-b">
          <div class="si-tag-b">Zero Update Anomalies</div>
          <div class="si-desc-b">Strict 3NF dimension design eliminates transitive dependencies while maintaining high-speed denormalized reporting views.</div>
        </div>
      </div>
      
      <div class="col-fig-box-b">
        <div class="gold-inner-frame"></div>
        <div class="fig-img-b">
          <img src="___FIG2_B64___" alt="Figure 2: Star Schema">
        </div>
        <div class="fig-cap-b">Figure 2: 13-table Kimball star schema highlighting fact-dimension cardinality and foreign key indexing.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Figure 2 exhibits our 13-table PostgreSQL star schema. A key technical contribution was replacing 32-character hexadecimal UUIDs with 32-bit surrogate integer keys. This simple architectural decision compressed our B-Tree index memory footprint by 68.4% and delivered a 4.2x speedup on complex multi-table joins across 99,441 transactional records."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 5: GEOSPATIAL FRICTION -->
<!-- ========================================== -->
<div class="slide slide-white" id="slide-5">
  <div class="slide-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body-b">
    <div class="header-brush-row">
      <img src="___SMALL_BRUSH_B64___" class="small-brush-icon" alt="Brush Badge">
      <div class="header-brush-text">
        <div class="tag-spaced">L O G I S T I C S   T E L E M E T R Y</div>
        <h1 class="slide-title-b">Geospatial Economics &amp; Freight Ratio (Fr > 0.20) Friction</h1>
      </div>
    </div>
    <div class="slide-sub-b">Haversine distance telemetry proves delivery overhead dominates product satisfaction</div>
    
    <div class="two-col-fig-b">
      <div class="col-text-box-b">
        <div class="gold-inner-frame"></div>
        <h3 class="box-title-b text-black">MATHEMATICAL FORMULATION</h3>
        
        <div class="formula-box-b">
          <div class="fb-label-b">Haversine Great-Circle Distance (d):</div>
          <div class="fb-code-b">d = 2R &sdot; arcsin(&radic;(sin&sup2;(&Delta;&phi;/2) + cos &phi;&sub1; cos &phi;&sub2; sin&sup2;(&Delta;&lambda;/2)))</div>
          <div class="fb-sub-b">Where R = 6,371 km represents Earth's mean radius.</div>
        </div>
        
        <div class="formula-box-b">
          <div class="fb-label-b">Freight Ratio Burden (Fr):</div>
          <div class="fb-code-b">Fr = freight_value / (item_price + freight_value)</div>
          <div class="fb-sub-b">Measures shipping overhead relative to total cart expenditure.</div>
        </div>
        
        <div class="highlight-blue-card-b">
          <div class="hbc-title-b">THE 20% FRICTION INFLECTION POINT</div>
          <div class="hbc-desc-b">When shipping exceeds 20% of cart value (Fr > 0.20), 1-star reviews surge by <strong>78.4%</strong> independent of product quality. Carrier delivery delays past SLA (&Delta;t > 3 days) multiply churn probability by <strong>2.3x</strong>.</div>
        </div>
      </div>
      
      <div class="col-fig-box-b">
        <div class="gold-inner-frame"></div>
        <div class="fig-img-b">
          <img src="___FIG6_B64___" alt="Figure 3: Geospatial Economics">
        </div>
        <div class="fig-cap-b">Figure 3: Geospatial logistics telemetry: Haversine route density, state freight burdens, and delivery delay distributions.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="In Figure 3, we demonstrate why logistics economics directly governs e-commerce retention. By computing Haversine great-circle distances across all customer-seller pairs, we identified that freight burden Fr = freight / (price + freight) is the single greatest operational driver of dissatisfaction. When Fr exceeds 0.20, review scores collapse from 4.3 to 2.8 stars, proving customers punish sellers for shipping overhead rather than product defects."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 6: CUSTOMER INTELLIGENCE -->
<!-- ========================================== -->
<div class="slide slide-white" id="slide-6">
  <div class="slide-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body-b">
    <div class="header-brush-row">
      <img src="___SMALL_BRUSH_B64___" class="small-brush-icon" alt="Brush Badge">
      <div class="header-brush-text">
        <div class="tag-spaced">C U S T O M E R   I N T E L L I G E N C E</div>
        <h1 class="slide-title-b">Algorithmic Customer Segmentation: Log-Transformed K-Means (k=4)</h1>
      </div>
    </div>
    <div class="slide-sub-b">Unsupervised PCA decomposition isolating 4 distinct behavioral lifecycle personas</div>
    
    <div class="two-col-fig-b">
      <div class="col-text-box-b">
        <div class="gold-inner-frame"></div>
        <h3 class="box-title-b text-black">THE 4 BEHAVIORAL PERSONAS</h3>
        
        <div class="persona-row-b">
          <div class="pr-title-b text-blue">[1] Champions (12.4% pop | R$ 812.40 GMV)</div>
          <div class="pr-desc-b">High frequency, low recency (&lt;45 days), heavy credit card installments. Core profit engine. <em>Strategy: VIP exclusivity &amp; loyalty perks.</em></div>
        </div>
        
        <div class="persona-row-b">
          <div class="pr-title-b text-green">[2] Loyal High-Value (23.8% pop | R$ 348.10 GMV)</div>
          <div class="pr-desc-b">Consistent repeat buyers with high basket size and high satisfaction scores. <em>Strategy: Category cross-selling &amp; restocking reminders.</em></div>
        </div>
        
        <div class="persona-row-b">
          <div class="pr-title-b text-crimson">[3] At-Risk Defectors (28.6% pop | R$ 142.50 GMV)</div>
          <div class="pr-desc-b">High recency (&gt;180 days), declining review scores, and elevated freight ratios. <em>Strategy: Automated win-back discount vouchers.</em></div>
        </div>
        
        <div class="persona-row-b">
          <div class="pr-title-b text-amber">[4] Dormant Bargain Hunters (35.2% pop | R$ 68.20 GMV)</div>
          <div class="pr-desc-b">Single-purchase customers attracted solely by promotional markdowns via Boleto. Low margin, high churn propensity.</div>
        </div>
        
        <div class="method-box-b">
          <strong>Methodology:</strong> Standardized log-transform x&#771; = ln(x + 1) normalized heavy right-skew. WCSS elbow heuristic and Silhouette analysis (<strong>s = 0.612</strong>) confirmed mathematical optimality at k = 4.
        </div>
      </div>
      
      <div class="col-fig-box-b">
        <div class="gold-inner-frame"></div>
        <div class="fig-img-b">
          <img src="___FIG4_B64___" alt="Figure 4: K-Means & PCA">
        </div>
        <div class="fig-cap-b">Figure 4: Unsupervised clustering: (a) WCSS elbow curve confirming k=4, and (b) 2D PCA projection of the 4 behavioral customer clusters.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Figure 4 presents Gajjala Srithika's customer intelligence pipeline. Monetary value in e-commerce follows a Pareto power law. Applying standard K-Means directly fails due to extreme outliers. By applying a logarithmic transform x̃ = ln(x+1) and Z-score normalization, our WCSS elbow curve confirmed an optimal inflection at k=4 with a Silhouette score of 0.612. The 2D PCA projection reveals sharp separation between high-margin Champions and high-risk At-Risk Defectors."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 7: TARGET LEAKAGE DISCOVERY -->
<!-- ========================================== -->
<div class="slide slide-white" id="slide-7">
  <div class="slide-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body-b">
    <div class="header-brush-row">
      <img src="___SMALL_BRUSH_B64___" class="small-brush-icon" alt="Brush Badge">
      <div class="header-brush-text">
        <div class="tag-spaced">M A C H I N E   L E A R N I N G   P R O O F</div>
        <h1 class="slide-title-b">Target Leakage Discovery: The Deceptive 99% Accuracy Trap</h1>
      </div>
    </div>
    <div class="slide-sub-b">Mathematical proof of how post-hoc tenure features artificially inflate churn models</div>
    
    <div class="two-col-b">
      <div class="col-half-box-b">
        <div class="gold-inner-frame"></div>
        <h3 class="box-title-b text-crimson">MATHEMATICAL INFORMATION LEAKAGE PROOF</h3>
        
        <div class="proof-row-b">
          <div class="pr-num-b">1</div>
          <div><strong>Ground Truth Churn Label:</strong> y_i = 1 if (t_obs - t_last) &gt; 90 days, else y_i = 0.</div>
        </div>
        
        <div class="proof-row-b">
          <div class="pr-num-b">2</div>
          <div><strong>Standard Customer Tenure:</strong> T_tenure = t_obs - t_first (elapsed days since first purchase).</div>
        </div>
        
        <div class="proof-row-b">
          <div class="pr-num-b">3</div>
          <div><strong>Single-Purchase Collapse:</strong> For 96.9% of buyers, t_first = t_last &implies; T_tenure = t_obs - t_last.</div>
        </div>
        
        <div class="proof-row-b">
          <div class="pr-num-b">4</div>
          <div><strong>The Trivial Decision Split:</strong> y_i = 1 &iff; T_tenure &gt; 90. Tree models trivially exploit this to claim <strong>0.9998 AUC</strong>.</div>
        </div>
      </div>
      
      <div class="col-half-box-b bg-offwhite-b">
        <div class="gold-inner-frame"></div>
        <h3 class="box-title-b text-amber">PRODUCTION DEPLOYMENT CATASTROPHE</h3>
        
        <div class="cat-item-b">
          <strong>The Literature Blindspot:</strong> Numerous published academic papers claim 99% accuracy on retail churn by including <code>tenure_days</code>. They unknowingly train on the target label!
        </div>
        
        <div class="cat-item-b">
          <strong>Day-1 Production Failure:</strong> A new buyer places their first order today: <code>T_tenure = 0 &le; 90</code>. The leaked model classifies <strong>100% of newly acquired buyers as NON-CHURNERS</strong>!
        </div>
        
        <div class="cat-item-b">
          <strong>Our Pre-Attrition Remediation (X_pre):</strong> Formulated a clean behavioral feature store strictly removing post-hoc duration features.
        </div>
        
        <div class="contrib-box-b">
          <strong>Core Contribution:</strong> We establish the first empirical ablation framework that decouples post-hoc tenure leakage from real causal drivers of customer defection.
        </div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Slide 7 represents one of our most significant academic contributions, authored by Ala Venkata Veera Ritwik. Many published papers claim 99% accuracy on retail churn. We proved this is a mathematical illusion caused by target leakage. Because 96.9% of customers only buy once, customer tenure equals time since last purchase. The decision tree simply splits on tenure > 90 days. But in production, a brand new customer has tenure=0, so the model falsely predicts they will never churn! We formulated a leak-free pre-attrition feature store X_pre to solve this."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 8: DUAL-MODEL CHURN ABLATION STUDY -->
<!-- ========================================== -->
<div class="slide slide-white" id="slide-8">
  <div class="slide-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body-b">
    <div class="header-brush-row">
      <img src="___SMALL_BRUSH_B64___" class="small-brush-icon" alt="Brush Badge">
      <div class="header-brush-text">
        <div class="tag-spaced">E M P I R I C A L   B E N C H M A R K S</div>
        <h1 class="slide-title-b">Dual-Model Churn Ablation Study &amp; TreeSHAP Attribution</h1>
      </div>
    </div>
    <div class="slide-sub-b">Rigorous empirical benchmark proving real behavioral signals vs leaked baseline</div>
    
    <div class="two-col-fig-b">
      <div class="col-text-box-b">
        <div class="gold-inner-frame"></div>
        <h3 class="box-title-b text-black">EMPIRICAL ABLATION COMPARISON</h3>
        
        <table class="table-brush">
          <thead>
            <tr>
              <th>Metric</th>
              <th>Model A (Leaked)</th>
              <th>Model B (Ablated)</th>
              <th>Operational Implication</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Accuracy</strong></td>
              <td>99.28%</td>
              <td class="td-gold">84.18%</td>
              <td>Eliminates artificial overfitting</td>
            </tr>
            <tr>
              <td><strong>ROC-AUC</strong></td>
              <td>0.9998</td>
              <td class="td-gold">0.8624</td>
              <td>Production-grade ranking</td>
            </tr>
            <tr>
              <td><strong>PR-AUC</strong></td>
              <td>0.9986</td>
              <td class="td-gold">0.8519</td>
              <td>High precision under imbalance</td>
            </tr>
            <tr>
              <td><strong>Recall</strong></td>
              <td>98.92%</td>
              <td class="td-gold">85.12%</td>
              <td>Captures 85% of defecting buyers</td>
            </tr>
            <tr>
              <td><strong>Top Feature</strong></td>
              <td>tenure (98.8%)</td>
              <td class="td-gold">freight_ratio (34.2%)</td>
              <td>Actionable logistics lever</td>
            </tr>
          </tbody>
        </table>
        
        <div class="shap-box-b">
          <div class="sb-title-b">TOP TREESHAP BEHAVIORAL DRIVERS:</div>
          <div class="sb-row-b"><span class="sb-badge-b">34.20%</span><strong>Freight Ratio (Fr):</strong> Steep inflection at Fr &gt; 0.20 drives churn.</div>
          <div class="sb-row-b"><span class="sb-badge-b">16.50%</span><strong>Review Score:</strong> Low rating triggers 78.4% churn odds.</div>
          <div class="sb-row-b"><span class="sb-badge-b">14.80%</span><strong>Installments:</strong> Credit card installments create retention lock-in.</div>
          <div class="sb-row-b"><span class="sb-badge-b">12.10%</span><strong>Monetary GMV:</strong> High-ticket orders correlate with platform trust.</div>
        </div>
      </div>
      
      <div class="col-fig-box-b">
        <div class="gold-inner-frame"></div>
        <div class="fig-img-b">
          <img src="___FIG3_B64___" alt="Figure 5: Churn ROC & SHAP">
        </div>
        <div class="fig-cap-b">Figure 5: Dual-model evaluation: (a) ROC curve comparison (Model A 0.9998 vs Model B 0.8624), and (b) TreeSHAP feature importance.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Figure 5 demonstrates the empirical ablation results. Model A with leakage achieves a suspicious 0.9998 ROC-AUC driven 98.8% by tenure. Model B strictly removes tenure and achieves an honest, production-ready 0.8624 ROC-AUC and 85.12% recall. More importantly, our TreeSHAP analysis reveals that freight ratio and review sentiment are the true causal drivers of churn, giving business executives concrete operational levers to fix customer attrition."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 9: LONGITUDINAL DEMAND FORECASTING -->
<!-- ========================================== -->
<div class="slide slide-white" id="slide-9">
  <div class="slide-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body-b">
    <div class="header-brush-row">
      <img src="___SMALL_BRUSH_B64___" class="small-brush-icon" alt="Brush Badge">
      <div class="header-brush-text">
        <div class="tag-spaced">P R E D I C T I V E   R E V E N U E</div>
        <h1 class="slide-title-b">Longitudinal Demand Forecasting: Multiplicative Holt-Winters</h1>
      </div>
    </div>
    <div class="slide-sub-b">Triple exponential smoothing capturing Black Friday demand surges with 8.42% MAPE</div>
    
    <div class="two-col-fig-b">
      <div class="col-text-box-b">
        <div class="gold-inner-frame"></div>
        <h3 class="box-title-b text-black">TRIPLE EXPONENTIAL SMOOTHING</h3>
        
        <div class="formula-box-b">
          <div class="fb-label-b">Level Component (&ell;_t):</div>
          <div class="fb-code-b">&ell;_t = &alpha;(y_t / s_{t-m}) + (1 - &alpha;)(&ell;_{t-1} + b_{t-1})</div>
          <div class="fb-sub-b">Tracks underlying baseline sales volume across weekly cycles.</div>
        </div>
        
        <div class="formula-box-b">
          <div class="fb-label-b">Trend Component (b_t):</div>
          <div class="fb-code-b">b_t = &beta;(&ell;_t - &ell;_{t-1}) + (1 - &beta;)b_{t-1}</div>
          <div class="fb-sub-b">Captures secular year-over-year revenue expansion.</div>
        </div>
        
        <div class="formula-box-b">
          <div class="fb-label-b">Multiplicative Seasonality (s_t):</div>
          <div class="fb-code-b">s_t = &gamma;(y_t / (&ell;_{t-1} + b_{t-1})) + (1 - &gamma;)s_{t-m}</div>
          <div class="fb-sub-b">Captures 52-week annual consumer buying spikes.</div>
        </div>
        
        <div class="highlight-blue-card-b">
          <div class="hbc-title-b">FORECASTING BENCHMARK:</div>
          <div class="hbc-desc-b">Achieved <strong>8.42% out-of-sample MAPE</strong> (vs SARIMA at 14.12%). Accurately captured the <strong>4.1x November volume explosion</strong> within 95% confidence intervals, enabling 3-month carrier pre-booking.</div>
        </div>
      </div>
      
      <div class="col-fig-box-b">
        <div class="gold-inner-frame"></div>
        <div class="fig-img-b">
          <img src="___FIG5_B64___" alt="Figure 6: Demand Forecasting">
        </div>
        <div class="fig-cap-b">Figure 6: Longitudinal sales forecasting: 90-day multiplicative Holt-Winters demand projection with 95% confidence bounds.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Figure 6 highlights our longitudinal demand forecasting module. In retail, additive models fail during holiday surges because variance scales with volume. By deploying Multiplicative Holt-Winters triple exponential smoothing with m=52 weekly seasonality, we achieved an out-of-sample MAPE of 8.42%, outperforming standard SARIMA (14.12%). Our model captured the massive 4.1x Black Friday spike within 95% confidence bands, allowing supply chain teams to pre-allocate logistics capacity."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 10: PRODUCT PORTFOLIO STRATEGY -->
<!-- ========================================== -->
<div class="slide slide-white" id="slide-10">
  <div class="slide-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body-b">
    <div class="header-brush-row">
      <img src="___SMALL_BRUSH_B64___" class="small-brush-icon" alt="Brush Badge">
      <div class="header-brush-text">
        <div class="tag-spaced">S T R A T E G I C   M E R C H A N D I S I N G</div>
        <h1 class="slide-title-b">Product Portfolio Optimization: 73-Category BCG Matrix</h1>
      </div>
    </div>
    <div class="slide-sub-b">Market growth rate vs relative market share capital allocation across 32,951 catalog SKUs</div>
    
    <div class="two-col-fig-b">
      <div class="col-text-box-b">
        <div class="gold-inner-frame"></div>
        <h3 class="box-title-b text-black">THE 4 STRATEGIC MERCHANDISING QUADRANTS</h3>
        
        <div class="quad-box-b qb-green">
          <strong>Cash Cows (38.4% GMV Share):</strong> Bed/Bath/Table, Health/Beauty. Mature cash engines funding platform growth.
        </div>
        
        <div class="quad-box-b qb-blue">
          <strong>Stars (24.1% GMV Share):</strong> Computers, Telephony. Strategic high-growth investment targets.
        </div>
        
        <div class="quad-box-b qb-amber">
          <strong>Question Marks (19.2% GMV Share):</strong> Small Appliances, Audio. Fast-growing categories requiring seller subsidies.
        </div>
        
        <div class="quad-box-b qb-red">
          <strong>Dogs (18.3% GMV Share):</strong> DVDs, Security items. Candidates for catalog pruning, vendor delisting, and markdowns.
        </div>
      </div>
      
      <div class="col-fig-box-b">
        <div class="gold-inner-frame"></div>
        <div class="fig-img-b">
          <img src="___FIG7_B64___" alt="Figure 7: BCG Matrix">
        </div>
        <div class="fig-cap-b">Figure 7: 73-category BCG Growth-Share matrix showing relative market share, annual category growth, and GMV bubble sizing.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Figure 7 illustrates M Akshay Sharma's product portfolio analytics. Analyzing 73 categories and 32,951 SKUs, we constructed the BCG Growth-Share matrix. Cash Cows such as Bed/Bath and Health/Beauty represent 38.4% of total GMV, generating the operating cash flows necessary to aggressively subsidize high-growth Stars in Computers and Electronics. Conversely, catalog pruning in the Dog quadrant frees up critical working capital."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 11: PRODUCTION SAAS PLATFORM -->
<!-- ========================================== -->
<div class="slide slide-white" id="slide-11">
  <div class="slide-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: Prof. N. Lakshmipathi Anantha | Fall 2026&ndash;27</div>
  </div>
  
  <div class="slide-body-b">
    <div class="header-brush-row">
      <img src="___SMALL_BRUSH_B64___" class="small-brush-icon" alt="Brush Badge">
      <div class="header-brush-text">
        <div class="tag-spaced">P R O D U C T I O N   S A A S</div>
        <h1 class="slide-title-b">Enterprise Production SaaS Platform &amp; Interactive 3D WebGL</h1>
      </div>
    </div>
    <div class="slide-sub-b">Live cloud deployment featuring Three.js particle portal and multi-year temporal slicing</div>
    
    <div class="dual-ss-grid-b">
      <div class="ss-box-b">
        <div class="gold-inner-frame"></div>
        <div class="ss-img-b">
          <img src="___DASH_B64___" alt="Executive Dashboard">
        </div>
        <div class="ss-cap-b">Executive Decision Cockpit: Multi-year temporal filters, real-time KPI tiles, and dynamic cohort analysis.</div>
      </div>
      
      <div class="ss-box-b">
        <div class="gold-inner-frame"></div>
        <div class="ss-img-b">
          <img src="___LOGIN_B64___" alt="3D WebGL Gateway">
        </div>
        <div class="ss-cap-b">3D WebGL Gateway: Three.js interactive particle system representing live customer network topology.</div>
      </div>
    </div>
    
    <div class="saas-features-box-b">
      <div class="gold-inner-frame"></div>
      <div class="sfb-title-b">FULL-STACK PRODUCTION CLOUD ARCHITECTURE &amp; KEY CAPABILITIES:</div>
      <div class="sfb-grid-b">
        <div><strong>FastAPI Async Microservices:</strong> RESTful backend with JWT authentication, CORS middleware, and p99 query latency under 112ms.</div>
        <div><strong>Interactive 3D Three.js Visuals:</strong> Custom WebGL shader particle canvas providing tactile feedback and dynamic network clustering.</div>
        <div><strong>Multi-Year Temporal Slicing:</strong> Real-time date slider allowing multi-year cohort comparisons across 2016, 2017, and 2018 data.</div>
        <div><strong>Automated Win-Back Triggers:</strong> Integrates XGBoost churn inference to dispatch automated retention alerts for At-Risk customers.</div>
      </div>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="Slide 11 presents our live production platform built by M Akshay Sharma. We did not stop at Jupyter notebooks; we deployed a full-stack enterprise cloud application. The frontend features a custom Three.js WebGL particle portal and an executive dashboard with multi-year temporal sliders, state-level freight heatmaps, and dynamic cohort drill-downs, backed by FastAPI delivering sub-100ms analytical queries."></div>
</div>

<!-- ========================================== -->
<!-- SLIDE 12: ACADEMIC SYNTHESIS & DELIVERABLES -->
<!-- ========================================== -->
<div class="slide slide-white" id="slide-12">
  <div class="slide-top-bar">
    <div class="top-uni">VIT-AP UNIVERSITY &bull; SCOPE</div>
    <div class="top-guide">Faculty Guide: <strong>Prof. N. Lakshmipathi Anantha</strong> | Fall 2026&ndash;27</div>
  </div>
  
  <img src="___HERO_BRUSH_B64___" class="bottom-right-brush" alt="Decorative Brush">
  
  <div class="slide-body-b">
    <div class="header-brush-row">
      <img src="___SMALL_BRUSH_B64___" class="small-brush-icon" alt="Brush Badge">
      <div class="header-brush-text">
        <div class="tag-spaced">R E S E A R C H   S Y N T H E S I S</div>
        <h1 class="slide-title-b">Academic Contributions, Deliverables &amp; Defense Conclusion</h1>
      </div>
    </div>
    <div class="slide-sub-b">Bridging empirical data science research with enterprise-grade cloud software engineering</div>
    
    <div class="deliv-grid-b">
      <!-- Deliverable 1 -->
      <div class="deliv-card-b">
        <div class="gold-inner-frame"></div>
        <div class="dc-badge-b">40+ PAGES COMPREHENSIVE</div>
        <h3 class="dc-title-b">1. Capstone Thesis Report</h3>
        <ul class="dc-list-b">
          <li>Official VIT-AP SCOPE thesis format compliance</li>
          <li>Complete 13-table Kimball star schema specification</li>
          <li>Mathematical proofs for Haversine, Fr, and leakage</li>
          <li>Student credentials, photo badges &amp; CD sleeve design</li>
          <li>Available in publication DOCX, Markdown, and PDF</li>
        </ul>
      </div>
      
      <!-- Deliverable 2 -->
      <div class="deliv-card-b">
        <div class="gold-inner-frame"></div>
        <div class="dc-badge-b">DOUBLE-COLUMN RESEARCH</div>
        <h3 class="dc-title-b">2. IEEE Conference Paper</h3>
        <ul class="dc-list-b">
          <li>Target leakage discovery and ablation protocol</li>
          <li>Empirical dual-model benchmarks (0.8624 AUC)</li>
          <li>TreeSHAP causal feature attribution plots</li>
          <li>Humanized, zero-plagiarism academic prose</li>
          <li>Ready for peer-reviewed conference submission</li>
        </ul>
      </div>
      
      <!-- Deliverable 3 -->
      <div class="deliv-card-b">
        <div class="gold-inner-frame"></div>
        <div class="dc-badge-b">PRODUCTION SAAS CODEBASE</div>
        <h3 class="dc-title-b">3. Production Software Platform</h3>
        <ul class="dc-list-b">
          <li>FastAPI async backend with 13 SQL schemas</li>
          <li>Three.js 3D WebGL particle interactive gateway</li>
          <li>Multi-year executive dashboard with cohort filters</li>
          <li>Automated test suite, Dockerfile &amp; Vercel deployment</li>
          <li>Complete GitHub version-controlled repository</li>
        </ul>
      </div>
    </div>
    
    <div class="ack-card-b">
      <div class="gold-inner-frame"></div>
      <div class="ac-title-b">FACULTY GUIDE &amp; INSTITUTIONAL ACKNOWLEDGMENT</div>
      <p class="ac-text-b">We extend our deepest gratitude to our Project Guide <strong>Prof. N. Lakshmipathi Anantha</strong>, Assistant Professor, SCOPE, and the faculty of VIT-AP University for their invaluable mentorship, technical guidance, and constructive evaluation throughout Fall 2026&ndash;27.</p>
    </div>
  </div>
  
  <div class="speaker-note-content" data-notes="In conclusion, NEXUS.AI delivers on all 3 research frontiers: a comprehensive 40+ page Capstone Thesis, an IEEE research paper exposing churn target leakage, and a fully functional production SaaS platform. On behalf of Papasani Suhitha, Gajjala Srithika, Ala Venkata Veera Ritwik, and M Akshay Sharma, we express our profound gratitude to our guide Prof. N. Lakshmipathi Anantha and the School of Computer Science and Engineering. We are now open for viva defense questions. Thank you!"></div>
</div>
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>E-Commerce Business Intelligence Platform - Brushstroke & Gold Theme</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background-color: #0c121e;
  color: #0f172a;
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
  background-color: #ffffff;
}

.slide.active {
  display: flex;
}

.slide-white {
  background-color: #ffffff;
  color: #0f172a;
  position: relative;
}

/* Top bar */
.slide-top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 48px;
  font-size: 13px;
  font-weight: 600;
  height: 38px;
  border-bottom: 1px solid #f1f5f9;
  background-color: #ffffff;
  z-index: 10;
}
.slide-top-bar .top-uni {
  color: #1e3a8a;
  font-weight: 700;
  letter-spacing: 0.5px;
}
.slide-top-bar .top-guide {
  color: #64748b;
  font-weight: 500;
}

/* Gold wireframe decorative overlay */
.gold-inner-frame {
  position: absolute;
  top: 4px;
  left: 4px;
  right: 4px;
  bottom: 4px;
  border: 1px solid #c5a880;
  pointer-events: none;
  opacity: 0.85;
  border-radius: 4px;
}

/* Slide 1 Brush Content */
.s1-brush-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px 48px 24px 48px;
  position: relative;
  z-index: 10;
}
.s1-logo-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin-bottom: 10px;
}
.vit-logo-brush {
  height: 42px;
  object-fit: contain;
}
.gold-wire-badge {
  border: 1px solid #c5a880;
  color: #1e3a8a;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1px;
  padding: 4px 12px;
  background: #ffffff;
}

/* Hero Brushstroke with Gold Wireframe Box */
.hero-brush-container {
  position: relative;
  width: 680px;
  height: 240px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 8px;
}
.gold-frame-behind {
  position: absolute;
  width: 440px;
  height: 220px;
  border: 1.5px solid #c5a880;
  top: 10px;
  left: 120px;
  z-index: 1;
}
.hero-brush-img {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: contain;
  z-index: 2;
}
.hero-brush-text {
  position: relative;
  z-index: 3;
  text-align: center;
}
.hbt-tag {
  font-size: 11px;
  font-weight: 800;
  color: #d4af37;
  letter-spacing: 1.5px;
  margin-bottom: 4px;
}
.hbt-main {
  font-size: 26px;
  font-weight: 900;
  color: #ffffff;
  letter-spacing: 1px;
  line-height: 1.15;
  text-shadow: 0 2px 8px rgba(0,0,0,0.4);
}
.hbt-sub {
  font-size: 16px;
  font-weight: 700;
  color: #bfdbfe;
  letter-spacing: 0.8px;
  margin-top: 2px;
  text-shadow: 0 2px 6px rgba(0,0,0,0.3);
}

.s1-sub-line {
  font-size: 13.5px;
  font-weight: 500;
  color: #64748b;
  text-align: center;
  margin-bottom: 12px;
}

.guide-box-gold {
  position: relative;
  background-color: #f8fafc;
  border: 1px solid #c5a880;
  padding: 8px 16px;
  font-size: 12.5px;
  width: 100%;
  max-width: 1100px;
  margin-bottom: 14px;
  text-align: center;
}
.gb-label { color: #1e3a8a; font-weight: 700; margin-right: 6px; }
.gb-name { color: #0f172a; font-weight: 700; margin-right: 6px; }
.gb-dept { color: #64748b; }

.candidates-grid-brush {
  display: flex;
  gap: 14px;
  width: 100%;
  max-width: 1100px;
}
.cand-card-b {
  flex: 1;
  position: relative;
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  padding: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}
.cand-num-b {
  position: absolute;
  top: 8px;
  left: 8px;
  font-size: 10px;
  font-weight: 800;
  color: #1e3a8a;
  border: 1px solid #c5a880;
  padding: 1px 5px;
  background: #ffffff;
}
.cand-photo-b {
  width: 72px;
  height: 92px;
  object-fit: cover;
  border: 1px solid #c5a880;
  margin: 6px 0 6px 0;
}
.cand-name-b { font-size: 12px; font-weight: 700; color: #0f172a; margin-bottom: 2px; }
.cand-reg-b { font-size: 11px; font-weight: 700; color: #1e3a8a; margin-bottom: 2px; }
.cand-role-b { font-size: 9.5px; color: #64748b; line-height: 1.25; }

/* Slide Body for Content */
.slide-body-b {
  flex: 1;
  padding: 14px 48px 24px 48px;
  display: flex;
  flex-direction: column;
  z-index: 10;
}
.header-brush-row {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 2px;
}
.small-brush-icon {
  width: 48px;
  height: 28px;
  object-fit: contain;
}
.tag-spaced {
  font-size: 10px;
  font-weight: 800;
  color: #1e3a8a;
  letter-spacing: 1.2px;
}
.slide-title-b {
  font-size: 24px;
  font-weight: 800;
  color: #0f172a;
  letter-spacing: -0.3px;
  line-height: 1.15;
}
.slide-sub-b {
  font-size: 13px;
  font-weight: 500;
  color: #64748b;
  margin-bottom: 12px;
  padding-left: 60px;
}

/* KPI Strip */
.kpi-strip-b {
  display: flex;
  gap: 14px;
  margin-bottom: 12px;
}
.kpi-box-b {
  flex: 1;
  position: relative;
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 10px 14px;
}
.kpi-val-b { font-size: 22px; font-weight: 900; line-height: 1.1; }
.kpi-title-b { font-size: 11.5px; font-weight: 700; color: #0f172a; margin-top: 2px; }
.kpi-desc-b { font-size: 10px; color: #64748b; margin-top: 2px; }

.text-blue { color: #1e3a8a; }
.text-crimson { color: #b91c1c; }
.text-amber { color: #d97706; }
.text-green { color: #059669; }
.text-black { color: #0f172a; }

/* 2-Column Split */
.two-col-b {
  display: flex;
  gap: 18px;
  flex: 1;
}
.col-left-box-b {
  flex: 4.8;
  position: relative;
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  padding: 16px;
}
.col-half-box-b {
  flex: 1;
  position: relative;
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  padding: 16px;
}
.bg-offwhite-b { background-color: #f8fafc; }

.box-title-b {
  font-size: 13.5px;
  font-weight: 800;
  letter-spacing: 0.5px;
  margin-bottom: 10px;
}
.para-b {
  font-size: 12px;
  color: #475569;
  line-height: 1.45;
  margin-bottom: 8px;
}

.col-right-steps-b {
  flex: 5.2;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.step-row-b {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}
.circle-badge-b {
  background-color: #1e3a8a;
  color: #ffffff;
  font-size: 12px;
  font-weight: 800;
  min-width: 26px;
  height: 26px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 4px;
}
.step-card-b {
  flex: 1;
  position: relative;
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 8px 12px;
}
.sc-title-b { font-size: 12.5px; font-weight: 700; color: #0f172a; margin-bottom: 2px; }
.sc-desc-b { font-size: 11px; color: #64748b; line-height: 1.35; }

/* 2-Column Figure Layout */
.two-col-fig-b {
  display: flex;
  gap: 18px;
  flex: 1;
  min-height: 0;
}
.col-text-box-b {
  flex: 4.8;
  position: relative;
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  padding: 14px;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}
.col-fig-box-b {
  flex: 5.2;
  position: relative;
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  padding: 10px;
  display: flex;
  flex-direction: column;
}
.fig-img-b {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.fig-img-b img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}
.fig-cap-b {
  font-size: 10.5px;
  font-weight: 600;
  color: #64748b;
  text-align: center;
  padding-top: 6px;
  border-top: 1px solid #f1f5f9;
}

/* Tier cards */
.tier-card-b { margin-bottom: 8px; }
.t-badge-b {
  display: inline-block;
  background-color: #f8fafc;
  border: 1px solid #c5a880;
  color: #1e3a8a;
  font-size: 11px;
  font-weight: 700;
  padding: 2px 6px;
  margin-bottom: 2px;
}
.t-desc-b { font-size: 11.5px; color: #475569; line-height: 1.35; }

.perf-strip-b {
  background-color: #f8fafc;
  border: 1px solid #c5a880;
  padding: 8px 10px;
  margin-top: 6px;
}
.ps-title-b { font-size: 10px; font-weight: 800; color: #1e3a8a; margin-bottom: 4px; }
.ps-grid-b { display: flex; justify-content: space-between; text-align: center; }
.ps-grid-b strong { display: block; font-size: 15px; color: #0f172a; }
.ps-grid-b span { font-size: 9.5px; color: #64748b; }

/* Schema rows */
.schema-item-b { margin-bottom: 8px; }
.si-tag-b {
  display: inline-block;
  border: 1px solid #c5a880;
  color: #1e3a8a;
  font-size: 10.5px;
  font-weight: 700;
  padding: 1px 6px;
  margin-bottom: 2px;
}
.si-desc-b { font-size: 11.5px; color: #475569; line-height: 1.35; }

/* Formulas */
.formula-box-b {
  background-color: #f8fafc;
  border-left: 3px solid #1e3a8a;
  padding: 6px 10px;
  margin-bottom: 8px;
}
.fb-label-b { font-size: 11px; font-weight: 700; color: #0f172a; margin-bottom: 2px; }
.fb-code-b { font-family: 'JetBrains Mono', monospace; font-size: 10.5px; color: #1e3a8a; font-weight: 600; margin-bottom: 2px; }
.fb-sub-b { font-size: 9.5px; color: #64748b; }

.highlight-blue-card-b {
  position: relative;
  background-color: #1e3a8a;
  color: #ffffff;
  padding: 10px 14px;
  margin-top: 6px;
  border: 1px solid #c5a880;
}
.hbc-title-b { font-size: 11px; font-weight: 800; color: #d4af37; margin-bottom: 3px; letter-spacing: 0.5px; }
.hbc-desc-b { font-size: 10.5px; color: #eff6ff; line-height: 1.35; }

/* Personas */
.persona-row-b { margin-bottom: 6px; }
.pr-title-b { font-size: 11px; font-weight: 700; margin-bottom: 2px; }
.pr-desc-b { font-size: 11px; color: #475569; line-height: 1.35; }
.method-box-b {
  font-size: 10.5px;
  background-color: #f8fafc;
  border: 1px solid #c5a880;
  padding: 6px 8px;
  color: #334155;
  margin-top: 4px;
}

/* Proof */
.proof-row-b {
  display: flex;
  gap: 10px;
  margin-bottom: 8px;
  font-size: 11px;
  color: #334155;
}
.pr-num-b {
  border: 1px solid #c5a880;
  color: #1e3a8a;
  font-weight: 800;
  min-width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10.5px;
}
.cat-item-b {
  font-size: 11px;
  color: #475569;
  line-height: 1.35;
  margin-bottom: 8px;
}
.contrib-box-b {
  border: 1px solid #c5a880;
  background-color: #ffffff;
  padding: 8px 10px;
  font-size: 11px;
  color: #1e3a8a;
  margin-top: 6px;
}

/* Table */
.table-brush {
  width: 100%;
  border-collapse: collapse;
  font-size: 10.5px;
  margin-bottom: 8px;
}
.table-brush th {
  background-color: #f8fafc;
  color: #0f172a;
  padding: 5px 8px;
  text-align: left;
  font-weight: 700;
  border-bottom: 2px solid #c5a880;
}
.table-brush td {
  padding: 4px 8px;
  border-bottom: 1px solid #e2e8f0;
  color: #334155;
}
.td-gold { font-weight: 700; color: #1e3a8a; }

.shap-box-b {
  background-color: #f8fafc;
  border: 1px solid #c5a880;
  padding: 6px 8px;
}
.sb-title-b { font-size: 10px; font-weight: 800; color: #1e3a8a; margin-bottom: 3px; }
.sb-row-b { font-size: 10px; color: #334155; margin-bottom: 2px; }
.sb-badge-b {
  display: inline-block;
  border: 1px solid #c5a880;
  color: #1e3a8a;
  font-weight: 700;
  font-size: 9.5px;
  padding: 1px 4px;
  margin-right: 4px;
}

/* Quadrants */
.quad-box-b {
  padding: 6px 10px;
  margin-bottom: 6px;
  font-size: 11px;
  line-height: 1.35;
  border-left: 3px solid #1e3a8a;
}
.qb-green { background-color: #f0fdf4; border-color: #16a34a; }
.qb-blue { background-color: #eff6ff; border-color: #1e3a8a; }
.qb-amber { background-color: #fffbeb; border-color: #d97706; }
.qb-red { background-color: #fef2f2; border-color: #dc2626; }

/* Dual Screenshot */
.dual-ss-grid-b {
  display: flex;
  gap: 14px;
  flex: 1;
  min-height: 0;
  margin-bottom: 8px;
}
.ss-box-b {
  flex: 1;
  position: relative;
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  padding: 8px;
  display: flex;
  flex-direction: column;
}
.ss-img-b {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.ss-img-b img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}
.ss-cap-b {
  font-size: 10px;
  font-weight: 600;
  color: #64748b;
  text-align: center;
  padding-top: 4px;
  border-top: 1px solid #f1f5f9;
}

.saas-features-box-b {
  position: relative;
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 8px 14px;
}
.sfb-title-b { font-size: 10.5px; font-weight: 800; color: #0f172a; margin-bottom: 4px; }
.sfb-grid-b { display: grid; grid-template-columns: 1fr 1fr; gap: 4px 14px; font-size: 10px; color: #475569; }

/* Slide 12 Deliverables */
.deliv-grid-b {
  display: flex;
  gap: 14px;
  flex: 1;
  margin-bottom: 10px;
}
.deliv-card-b {
  flex: 1;
  position: relative;
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 12px;
  display: flex;
  flex-direction: column;
}
.dc-badge-b { font-size: 9px; font-weight: 800; color: #1e3a8a; margin-bottom: 4px; }
.dc-title-b { font-size: 14px; font-weight: 800; color: #0f172a; margin-bottom: 6px; }
.dc-list-b { list-style: none; font-size: 11px; color: #475569; line-height: 1.45; }
.dc-list-b li { margin-bottom: 4px; position: relative; padding-left: 14px; }
.dc-list-b li::before {
  content: "✓";
  position: absolute;
  left: 0;
  color: #1e3a8a;
  font-weight: bold;
}

.bottom-right-brush {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 480px;
  height: 280px;
  object-fit: contain;
  pointer-events: none;
  opacity: 0.9;
  z-index: 5;
}

.ack-card-b {
  position: relative;
  background-color: #ffffff;
  border: 1.5px solid #c5a880;
  padding: 10px 18px;
  text-align: center;
  z-index: 10;
}
.ac-title-b { font-size: 10.5px; font-weight: 800; color: #1e3a8a; margin-bottom: 2px; }
.ac-text-b { font-size: 11px; color: #334155; }

/* Bottom Control Deck */
#controls-bar {
  height: 44px;
  background-color: #ffffff;
  border-top: 1px solid #e2e8f0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 24px;
  z-index: 1000;
}
.ctrl-group { display: flex; align-items: center; gap: 10px; }
.btn-ctrl {
  background-color: #f8fafc;
  color: #0f172a;
  border: 1px solid #c5a880;
  padding: 5px 12px;
  border-radius: 4px;
  font-size: 11.5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}
.btn-ctrl:hover { background-color: #1e3a8a; color: #ffffff; }
.slide-indicator { color: #64748b; font-size: 12.5px; font-weight: 700; min-width: 80px; text-align: center; }

/* Speaker Notes Drawer */
#notes-drawer {
  position: fixed;
  bottom: 44px;
  left: 0;
  width: 100%;
  background: rgba(15, 23, 42, 0.96);
  backdrop-filter: blur(8px);
  border-top: 2px solid #c5a880;
  color: #f8fafc;
  padding: 14px 40px;
  font-size: 13.5px;
  line-height: 1.5;
  max-height: 170px;
  overflow-y: auto;
  display: none;
  z-index: 999;
}
.notes-header {
  font-size: 11.5px;
  font-weight: 700;
  color: #d4af37;
  margin-bottom: 3px;
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

showSlide(1);
</script>
</body>
</html>
"""

# Replace placeholders safely
slides_processed = SLIDES_HTML
slides_processed = slides_processed.replace('___LOGO_B64___', logo_b64)
slides_processed = slides_processed.replace('___PHOTO1_B64___', photo1_b64)
slides_processed = slides_processed.replace('___PHOTO2_B64___', photo2_b64)
slides_processed = slides_processed.replace('___PHOTO3_B64___', photo3_b64)
slides_processed = slides_processed.replace('___PHOTO4_B64___', photo4_b64)
slides_processed = slides_processed.replace('___HERO_BRUSH_B64___', hero_brush_b64)
slides_processed = slides_processed.replace('___SMALL_BRUSH_B64___', small_brush_b64)
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
print(f"Successfully generated Brushstroke HTML deck at: {html_out}")

# Copy HTML to artifact directory
shutil.copy2(html_out, ARTIFACT_DIR / "presentation_slides.html")
print(f"Copied HTML deck to artifact directory.")

# =========================================================================
# PDF RENDERING VIA PLAYWRIGHT SCREENSHOTS + SWIFT PDFKIT
# =========================================================================
async def render_presentation_pdf():
    print("Launching Playwright to capture pixel-perfect 1920x1080 slide images...")
    tmp_img_dir = Path("/tmp/brushstroke_slides_png")
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
    print("Successfully generated 12-page Brushstroke presentation PDF at \\(outUrl.path)")
    """
    
    swift_file = Path("/tmp/make_brushstroke_pdf.swift")
    with open(swift_file, "w") as f:
        f.write(swift_script)
        
    subprocess.run(["swift", str(swift_file)], check=True)
    
    # Copy PDF to artifact dir
    shutil.copy2(pdf_out, ARTIFACT_DIR / "E_Commerce_Intelligence_Presentation.pdf")
    print(f"Copied Presentation PDF to artifact directory: {ARTIFACT_DIR / 'E_Commerce_Intelligence_Presentation.pdf'}")

asyncio.run(render_presentation_pdf())
print("ALL BRUSHSTROKE & GOLD PRESENTATION ASSETS GENERATED SUCCESSFULLY!")
