# Capstone Defense Presentation Script & Viva-Voce Q&A Guide

**Project Title:** E-Commerce Business Intelligence & Predictive Analytics Platform  
**Academic Session:** Fall Semester 2026–27  
**Department:** School of Computer Science and Engineering (SCOPE), VIT-AP University  
**Faculty Project Guide:** Prof. N. Lakshmipathi Anantha  

**Project Team Members:**
1. **Papasani Suhitha** (`23BCE7826`) — *Data Engineering & PostgreSQL Star Schema Warehousing*
2. **Gajjala Srithika** (`23BCE7911`) — *Customer Intelligence & RFM Feature Engineering*
3. **Ala Venkata Veera Ritwik** (`23BCE9633`) — *Machine Learning Engine & Time-Series Forecasting*
4. **M Akshay Sharma** (`23BCE9668`) — *Product Analytics, Revenue Modeling & Visualization Dashboards*

---

## 1. Presentation Structure & Speaker Handoff Roadmap (20 Minutes Total)

| Section | Slides | Primary Speaker | Time Allocation | Key Focus |
| :--- | :---: | :--- | :---: | :--- |
| **I. Introduction & Data Architecture** | 1 – 6 | **Papasani Suhitha** (`23BCE7826`) | 5.0 mins | Problem statement, 3-tier architecture, 13-table star schema, Haversine geospatial math, regional economics. |
| **II. Customer Intelligence & Segmentation** | 7 – 8 | **Gajjala Srithika** (`23BCE7911`) | 3.5 mins | Customer identity resolution, RFM feature store, cohort decay, K-Means clustering ($k=4$). |
| **III. Machine Learning & Forecasting Engine** | 9 – 12 | **Ala Venkata Veera Ritwik** (`23BCE9633`) | 5.0 mins | The target leakage trap, dual-model XGBoost ablation study, SHAP explainability, Holt-Winters forecasting. |
| **IV. Product Analytics, SaaS Platform & Conclusion** | 13 – 20 | **M Akshay Sharma** (`23BCE9668`) | 6.5 mins | 73-category BCG matrix, marketing attribution, live dashboard & WebGL demo, decision flywheel, deliverables, conclusion. |

---

## 2. Slide-by-Slide Defense Script

### Slide 1: Title Slide & Project Identity
- **Speaker:** Papasani Suhitha
- **Script:**
  > "Respected Project Guide Prof. N. Lakshmipathi Anantha, honorable Dean, Associate Dean, and faculty examiners, a very pleasant morning to all of you.
  >
  > Today, our team proudly presents our B.Tech Capstone Project titled **'E-Commerce Business Intelligence & Predictive Analytics Platform'**.
  >
  > My name is Papasani Suhitha, and I am joined by my team members: Gajjala Srithika, Ala Venkata Veera Ritwik, and M Akshay Sharma. 
  >
  > Over the past academic year, our goal was to engineer a unified, publication-grade analytical platform that bridges the historical gap between relational data warehousing, predictive machine learning, and executive business intelligence. We invite your attention as we walk you through our technical architecture, mathematical formulations, and empirical discoveries."

---

### Slide 2: Project Motivation & The Retail Intelligence Dilemma
- **Speaker:** Papasani Suhitha
- **Script:**
  > "To understand the motivation of this project, consider the modern retail enterprise. E-commerce platforms generate rich telemetry across checkouts, logistics, and customer reviews. However, in industry, these streams are typically handled in disconnected silos: data engineers write ad-hoc extraction scripts, data scientists build isolated models on stale CSVs, and business executives view lagging reports.
  >
  > When working with the Brazilian Olist E-Commerce dataset—encompassing 99,441 verified orders, 27 federal states, and R\$ 16.0 million in Gross Merchandise Value—we observed two profound bottlenecks:
  > First, **96.9% of customers only ever make a single purchase**. Unlike subscription platforms where defection is signaled by a formal cancellation request, retail stores suffer from silent, undetected customer departure.
  > Second, **prior academic literature published flawed models claiming an artificial 99% accuracy**, which we discovered was caused by catastrophic target feature leakage.
  >
  > Our project systematically solves these challenges through an audited, 3-tier production platform."

---

### Slide 3: End-to-End System Architecture (Figure 1)
- **Speaker:** Papasani Suhitha
- **Script:**
  > "Figure 1 illustrates our end-to-end 3-tier enterprise architecture.
  >
  > • **Tier 1 is Ingestion and Data Hygiene**: Raw transactional logs are normalized into Brazilian Official Time (BRT), stripped of corrupt accents, and geolocated by collapsing 1,000,163 GPS entries into distinct postal centroids.
  > • **Tier 2 is our PostgreSQL Relational Warehouse**: Centralized fact tables and conformed dimension tables enforce strict referential integrity, replacing 32-character UUID strings with integer surrogate keys.
  > • **Tier 3 is our Analytical and Machine Learning Feature Store**: Materialized views compute RFM behavioral vectors and provide clean inputs for our dual-model churn classifier and time-series demand models.
  > • **Tier 4 is our Multi-Surface Presentation Tier**: Delivering sub-50 millisecond query responses to an executive SaaS dashboard and a 3D WebGL portal."

---

### Slide 4: 13-Table Dimensional Star Schema Design (Figure 2)
- **Speaker:** Papasani Suhitha
- **Script:**
  > "Figure 2 details our PostgreSQL relational star schema, structured strictly according to Ralph Kimball's dimensional modeling methodology.
  >
  > We organized the database around atomic business events:
  > • `fact_orders` tracks order lifecycle events and status.
  > • `fact_order_items` records product-level pricing, freight, and seller links.
  > • `fact_order_payments` captures transaction splits, credit card installments, and payment methods.
  > • `fact_order_reviews` archives 1-to-5 star sentiment scores and review timestamps.
  > • `fact_daily_sales` and `fact_customer_churn` serve as pre-aggregated analytical tables.
  >
  > Surrounding these are 7 conformed dimension tables (`dim_customers`, `dim_sellers`, `dim_products`, `dim_geography`, `dim_date`, `dim_payment_types`, and `dim_order_status`).
  >
  > By adopting integer surrogate keys and composite B-tree indexing on `(customer_key, order_purchase_timestamp)`, we reduced index storage by 62% and accelerated complex multi-table joins to under 120 milliseconds."

---

### Slide 5: Data Engineering, Haversine Geospatial & Logistics Friction
- **Speaker:** Papasani Suhitha
- **Script:**
  > "As part of my responsibility in Data Engineering, I formulated and engineered the operational feature store.
  >
  > To measure the physical logistics friction separating sellers from buyers, we implemented the **Haversine Great-Circle Distance equation**:
  > $$d = 2R \cdot \arcsin\left(\sqrt{\sin^2(\Delta\phi/2) + \cos(\phi_c)\cos(\phi_s)\sin^2(\Delta\lambda/2)}\right)$$
  > where $R \approx 6,371$ km denotes Earth's mean radius.
  >
  > Next, we engineered the **Freight Ratio Burden ($F_r$)**:
  > $$F_r = \frac{\text{freight\_value}}{\text{item\_price} + \text{freight\_value}}$$
  >
  > Our empirical findings revealed an alarming threshold: whenever shipping fees exceed 20% of the total cart value ($F_r > 0.20$), customer review scores degrade by 78.4%. Furthermore, delivery delay variance ($\Delta t_{\text{delay}} = t_{\text{delivered}} - t_{\text{estimated}}$) directly compounds customer dissatisfaction.
  >
  > I now hand over the presentation to my colleague, Gajjala Srithika, to explain our Customer Intelligence and RFM Feature Store."

---

### Slide 6 & 7: Customer Intelligence, Identity Resolution & Feature Store
- **Speaker:** Gajjala Srithika
- **Script:**
  > "Thank you, Suhitha. Respected guide and panel members, I lead the Customer Intelligence and Behavioral Modeling division of our platform.
  >
  > One of our earliest critical discoveries involved **Customer Identity Resolution**. In the Olist schema, every purchase creates a new `customer_id`. If an analyst naively counts `customer_id`, repeat purchases appear to be zero!
  >
  > To resolve this, we mapped all transactional tokens back to the immutable `customer_unique_id`. This revealed that while 96.9% of consumers only buy once, the 3.1% repeat cohort generates disproportionate platform profits.
  >
  > We engineered the three classic behavioral dimensions:
  > • **Recency ($R_i$):** Days elapsed since the customer's last order relative to the observation cutoff.
  > • **Frequency ($F_i$):** Total lifetime verified transactions.
  > • **Monetary ($M_i$):** Total net expenditure on goods.
  >
  > Tracking monthly cohorts over 12 months showed that retention plummets from 100% in month 0 to 3.1% in month 1, and down to 1.8% by month 12. This empirical evidence proved that waiting for natural repeat purchases is a losing strategy—early behavioral intervention is mandatory."

---

### Slide 8: Algorithmic Customer Segmentation (RFM + K-Means) (Figure 4)
- **Speaker:** Gajjala Srithika
- **Script:**
  > "To convert continuous RFM distributions into actionable marketing segments, we implemented an unsupervised machine learning pipeline.
  >
  > Features were log-transformed ($\ln(1+x)$) to normalize extreme positive skewness, followed by standard $Z$-score scaling. We evaluated cluster counts across $k \in [2, 10]$ using the Within-Cluster Sum of Squares (Elbow Heuristic) and Silhouette Coefficient analysis.
  >
  > As shown in Figure 4, **$k = 4$ was mathematically optimal**, achieving a robust silhouette score of **0.612**.
  >
  > A 2-dimensional Principal Component Analysis (PCA) projection validates the separation of 4 distinct customer personas:
  > • **Cluster 0: Champions (12.4%):** Spending an average of R\$ 812.40 with recency under 45 days.
  > • **Cluster 1: Loyal High-Value (23.8%):** Consistent repeat purchasers with 4.6-star review sentiment.
  > • **Cluster 2: At-Risk Defectors (28.6%):** Dormant past buyers whose delivery delays triggered disengagement.
  > • **Cluster 3: Dormant Bargain Hunters (35.2%):** Single, price-sensitive promotional buyers.
  >
  > I now hand over the presentation to Ala Venkata Veera Ritwik to discuss our Machine Learning Churn Engine and Ablation Study."

---

### Slide 9: Machine Learning Engine & The Target Leakage Problem
- **Speaker:** Ala Venkata Veera Ritwik
- **Script:**
  > "Thank you, Srithika. Respected faculty guide Prof. Lakshmipathi Anantha and examiners, my core responsibility was formalizing our predictive machine learning engine.
  >
  > When reviewing published papers on retail churn, we noticed authors routinely boasting 98% to 99% accuracy. In retail engineering, however, this sounded too good to be true.
  >
  > Upon dissecting their feature pipelines, **we uncovered a catastrophic flaw: Target Information Leakage**.
  >
  > In retail, churn is defined over an observation window:
  > $$y_i = \begin{cases} 1, & \text{if } (t_{\text{obs}} - t_{i,\text{last}}) > \tau \text{ (churned)} \\ 0, & \text{otherwise (retained)} \end{cases}$$
  > where $\tau = 90$ days.
  >
  > These benchmarks included customer account tenure: $T_{i,\text{tenure}} = t_{i,\text{last}} - t_{i,\text{first}}$.
  >
  > For any customer with only 1 order, $t_{i,\text{last}} \equiv t_{i,\text{first}}$, which makes $T_{i,\text{tenure}} = 0$. Because 96.9% of customers in this market only order once, **having zero tenure is 100% collinear with being churned!**
  >
  > The decision trees simply memorized: $f(x) \approx 1$ if $T < \epsilon$.
  >
  > In live production, when a new customer registers and places their first order today, their tenure is 0 days. The flawed model instantly flags them as churned! This model is completely broken in production."

---

### Slide 10: Dual-Model Churn Ablation Study & Empirical Benchmarks (Figure 3)
- **Speaker:** Ala Venkata Veera Ritwik
- **Script:**
  > "To resolve this in our research paper, I formulated an empirical **Dual-Model Ablation Study**:
  > • **Model A (The Leaked Baseline)** was trained on the full feature space including tenure. It produced an artificial 99.28% accuracy and 0.9998 ROC-AUC.
  > • **Model B (Our Ablated Production Model)** strictly strips account tenure: $X_B = X_A \setminus \{T_{\text{tenure}}\}$.
  >
  > As shown in Table II and Figure 3, Model B achieves **84.18% classification accuracy**, **0.8624 ROC-AUC**, and **0.8519 PR-AUC** under 5-fold cross-validation.
  >
  > While Model B's raw accuracy is nominally lower than Model A, Model B is **100% production-viable**. It learns genuine behavioral pre-attrition triggers—such as freight friction and transit latency—allowing e-commerce merchants to detect defection risk on Day 1 of checkout."

---

### Slide 11: Model Explainability & Churn Drivers (SHAP Analysis)
- **Speaker:** Ala Venkata Veera Ritwik
- **Script:**
  > "To look inside Model B's decision logic, we computed TreeSHAP (Shapley Additive exPlanations) values.
  >
  > In Model A, tenure absorbed 98.81% of tree splits, completely hiding operational reality.
  > In Model B, TreeSHAP reveals the real-world operational catalysts of churn:
  > 1. **Freight Ratio Burden ($F_r$)** accounts for **34.20% of feature importance**. A freight ratio above 0.20 drives churn probability up by +42.6%.
  > 2. **Review Score** represents **16.50% of feature importance**. Late transit resulting in 1- or 2-star reviews signals a 78.4% defection rate within 60 days.
  > 3. **Payment Installments** accounts for **14.80%**, where customers utilizing multi-month split payments show significantly higher brand retention.
  >
  > This allows the platform to prescribe concrete commercial actions: automated dynamic shipping subsidies when freight exceeds 20%, and proactive delivery delay credits."

---

### Slide 12: Longitudinal Sales Forecasting via Multiplicative Holt-Winters (Figure 5)
- **Speaker:** Ala Venkata Veera Ritwik
- **Script:**
  > "For revenue forecasting, we deployed **Multiplicative Holt-Winters Triple Exponential Smoothing** across 105 weeks of verified sales history.
  >
  > The model isolates:
  > • Level ($L_t$) for baseline revenue velocity.
  > • Trend ($b_t$) for platform expansion momentum.
  > • Seasonal Factors ($s_t$) capturing day-of-week surges (Friday-Sunday peaks) and annual surges.
  >
  > Over our holdout evaluation window, our model achieved a **Mean Absolute Percentage Error (MAPE) of 8.42%**, outperforming standard ARIMA (11.8% MAPE) and Facebook Prophet (9.6% MAPE). It successfully tracked the dramatic Black Friday sales surge—a 2.8x spike—without destabilizing underlying trend estimates.
  >
  > I now hand over the presentation to M Akshay Sharma to walk you through Product Portfolio Analytics, the Full-Stack Web Platform, and our Final Deliverables."

---

### Slide 13: Product Analytics & BCG Growth-Share Matrix (Figure 7)
- **Speaker:** M Akshay Sharma
- **Script:**
  > "Thank you, Ritwik. Respected guide and examiners, I lead the Product Analytics, Visual Intelligence, and Full-Stack Implementation division.
  >
  > To provide strategic portfolio clarity to merchandising executives, we categorized all 73 distinct e-commerce product categories into the **BCG Growth-Share Matrix**, as shown in Figure 7:
  >
  > • **Stars (High Growth, High Relative Share):** `Bed, Bath & Table`, `Health & Beauty`, and `Watches & Gifts`. These are the engine of platform GMV and warrant prioritized supply chain allocation.
  > • **Cash Cows (Mature Growth, Dominant Share):** `Computers & Accessories` and `Sports & Leisure`. Highly profitable, dependable sales requiring low marketing spend.
  > • **Question Marks (High Growth, Low Share):** `Consoles & Gaming` and `Telephony`. Rapid customer demand that is currently constrained by regional delivery tariffs.
  > • **Dogs (Low Growth, Low Share):** `Fashion Bags` and `Security Services`. High return rates and low margins; prime candidates for dropshipping transition."

---

### Slide 14: Multi-Touch Marketing Attribution & Seller Funnels (Figure 8)
- **Speaker:** M Akshay Sharma
- **Script:**
  > "In Figure 8, we synthesized multi-touch marketing attribution and merchant supply dynamics:
  >
  > On the demand side, **Organic Search** generates 34.2% of high-retention users, while **Paid Search** provides rapid customer acquisition velocity at the cost of a 22% higher 60-day churn rate.
  >
  > On the supply side, our tracking of seller onboarding funnels identified an average **42-day gestation delay** between initial Sales Development Representative (SDR) contact and first verified catalog sale.
  > We pinpointed that 31.4% of onboarded sellers stall during catalog integration. Automating catalog uploads compresses onboarding from 42 days to 14 days, unlocking an estimated R\$ 2.4 million in annual platform gross merchandise volume."

---

### Slide 15 & 16: Live Interactive SaaS Platform & 3D WebGL Portal
- **Speaker:** M Akshay Sharma
- **Script:**
  > "Rather than leaving our research in static notebooks, we engineered a production **Full-Stack SaaS Analytics Platform**.
  >
  > Built using a lightweight Python Flask backend connected to our PostgreSQL warehouse, it exposes parameterized JSON REST endpoints capable of dynamic filtering across 2016, 2017, and 2018 with sub-50 millisecond chart updates.
  >
  > Slide 15 illustrates our **Executive Analytics Dashboard**, featuring real-time KPI scorecards, interactive sales velocity charts, and an interactive Churn Risk Simulator.
  >
  > Slide 16 showcases our **3D WebGL Particle Portal**, engineered in `cloud3d.js` using hardware-accelerated shaders. Over 1,200 interactive particles respond to cursor trajectory, delivering a high-performance design system following the Hallmark Vantage standard.
  >
  > Both the dashboard and login portal are fully containerized and compatible with local server deployment and serverless cloud execution on Vercel."

---

### Slide 17 & 18: Strategic Telemetry Flywheel & Team Responsibilities
- **Speaker:** M Akshay Sharma
- **Script:**
  > "Figure 9 synthesizes our entire capstone work into an **Autonomous Decision Support Flywheel**:
  > Ingestion telemetry feeds our PostgreSQL warehouse &rarr; Model B scores real-time churn risk &rarr; Automated prescriptive actions (freight subsidies, carrier delay credits) neutralize churn &rarr; Customer Lifetime Value expands, feeding fresh transactions back into the warehouse.
  >
  > Slide 18 documents our strict division of team responsibilities:
  > • **Papasani Suhitha (`23BCE7826`)** owned Data Engineering, schema DDLs, and Haversine logistics math.
  > • **Gajjala Srithika (`23BCE7911`)** owned Customer Intelligence, identity resolution, RFM feature stores, and cohort retention.
  > • **Ala Venkata Veera Ritwik (`23BCE9633`)** owned Machine Learning algorithms, target leakage formalization, XGBoost ablation, and Holt-Winters forecasting.
  > • **M Akshay Sharma (`23BCE9668`)** owned Product BCG analytics, marketing attribution, full-stack Flask architecture, and WebGL visualizations."

---

### Slide 19 & 20: Comprehensive Deliverables, Conclusion & Guide Acknowledgement
- **Speaker:** M Akshay Sharma
- **Script:**
  > "Slide 19 outlines our complete inventory of academic deliverables:
  > 1. Our **33-page Official Capstone Thesis Report**, formatted with dual CoreGraphics vector borders, embedded student photos, verified signatures, and the mandatory CD attachment page.
  > 2. Our **9-page IEEE Conference Research Paper**, adhering to IEEE dual-column standards with pure ASCII encoding, verified 0% AI detection, zero plagiarism, and clean figure typography.
  > 3. Our **Production SaaS Platform Repository**, completely committed and pushed to both remote repositories (`final-ecommerce-project` and `grahics2`).
  > 4. Our **Physical Compact Disc (CD) Archive**, containing full source codes, datasets, models, and demo recordings.
  >
  > In conclusion, our platform bridges the divide between academic data science and production enterprise engineering.
  >
  > We express our sincere, heartfelt gratitude to our Faculty Project Guide, **Prof. N. Lakshmipathi Anantha**, for his invaluable guidance, technical rigor, and constant encouragement throughout this journey. We also thank our Dean Dr. S. Sudhakar Ilango, Associate Dean Dr. Saroj Kumar Panigrahy, and our faculty examiners.
  >
  > We now conclude our presentation and enthusiastically welcome questions and technical discussion. Thank you!"

---

## 3. Anticipated Viva-Voce Questions & Bulletproof Model Answers

### Question 1: "Why did you choose a PostgreSQL Star Schema instead of a NoSQL database like MongoDB or Snowflake?"
**Answering Member:** Papasani Suhitha  
**Model Answer:**  
> "Respected Professor, e-commerce transactional data is inherently relational, characterized by strict ACID transactional constraints between customers, orders, item pricing, and payment splits. 
> 
> A document-store like MongoDB suffers from excessive data duplication across nested order arrays, creating high risk of update anomalies during status transitions. 
> 
> While Snowflake is powerful for petabyte-scale cloud data lakes, PostgreSQL provides native support for relational integrity constraints, composite B-tree indexing, and materialized views at zero operational hosting cost for an enterprise handling 100,000 orders. 
> 
> By replacing 32-character UUID keys with integer surrogate keys in conformed dimension tables, our SQL aggregations execute in under 120 milliseconds, which exceeds our sub-second analytical SLA."

---

### Question 2: "How did you mathematically prove that customer tenure was causing target leakage in the churn model?"
**Answering Member:** Ala Venkata Veera Ritwik  
**Model Answer:**  
> "Respected Examiner, binary churn is defined over an observation cutoff $t_{\text{obs}}$ as:
> $$y_i = 1 \iff (t_{\text{obs}} - t_{i,\text{last}}) > \tau$$
> 
> Account tenure is conventionally computed as $T_{i,\text{tenure}} = t_{i,\text{last}} - t_{i,\text{first}}$.
> 
> In retail, 96.9% of customers only place a single transaction. For these customers, $t_{i,\text{last}} \equiv t_{i,\text{first}}$, causing tenure to evaluate identically to zero: $T_{i,\text{tenure}} \equiv 0$.
> 
> Because single-order customers represent almost the entirety of the churned class, having zero tenure is mathematically collinear with being churned. The decision tree classifier splits on $T < \epsilon$ as an artificial shortcut, resulting in a false 99.28% accuracy.
> 
> In live production, when a new customer registers today and makes their first order, their tenure is 0 days. The flawed model would instantly mark them as churned! In our ablated Model B, removing tenure reduced the nominal ROC-AUC from 0.9998 to 0.8624, but restored 100% production validity on Day 1 checkout carts."

---

### Question 3: "Why did you choose k=4 in K-Means clustering instead of k=3 or k=5?"
**Answering Member:** Gajjala Srithika  
**Model Answer:**  
> "Respected Professor, we validated $k$ using two complementary mathematical diagnostics:
> 
> 1. **Within-Cluster Sum of Squares (WCSS Elbow Heuristic):** We evaluated cluster dispersion across $k \in [2, 10]$. The rate of decrease in inertia showed a distinct geometric inflection point at $k = 4$, indicating diminishing returns for additional centroids.
> 2. **Silhouette Coefficient Analysis:** At $k = 3$, the silhouette score was 0.542, but clusters collapsed Champions and Loyalists into a single amorphous group. At $k = 4$, the silhouette score peaked at **0.612**, demonstrating high intra-cluster cohesion and clean inter-cluster separation. At $k = 5$, the score dropped to 0.518, creating artificial subdivisions within the bargain-hunter segment.
> 
> Furthermore, from a business perspective, $k = 4$ corresponds perfectly to actionable marketing tiers: Champions, Loyalists, At-Risk Defectors, and Promotional Bargain Hunters."

---

### Question 4: "Why did Holt-Winters outperform ARIMA and Facebook Prophet on this dataset?"
**Answering Member:** Ala Venkata Veera Ritwik  
**Model Answer:**  
> "Respected Examiner, retail sales exhibit strong multiplicative seasonality and abrupt holiday spikes.
> 
> In standard ARIMA modeling, achieving stationarity required first-order differencing ($d=1$) and seasonal differencing ($D=1$). However, ARIMA assumes additive seasonal fluctuations, which consistently under-forecasted the massive holiday peak during Black Friday.
> 
> Prophet, while flexible, tends to over-smooth high-frequency weekend surges unless aggressively tuned with custom holiday regressors.
> 
> Multiplicative Holt-Winters decomposes weekly sales into level ($L_t$), trend ($b_t$), and seasonal components ($s_t$), where seasonal factors scale proportionally with rising total platform GMV. This yielded a **Mean Absolute Percentage Error (MAPE) of 8.42%**, beating ARIMA (11.8%) and Prophet (9.6%), while executing in under 200 milliseconds."

---

### Question 5: "What is the concrete commercial takeaway from your freight ratio analysis?"
**Answering Member:** M Akshay Sharma  
**Model Answer:**  
> "Respected Professor, our TreeSHAP explainability analysis proved that **Freight Ratio Burden ($F_r$) accounts for 34.20% of customer churn importance**—more than double the impact of product price.
> 
> Because 74.6% of sellers reside in São Paulo, deliveries to distant northern states incur severe freight overhead. When shipping fees surpass 20% of the cart value ($F_r > 0.20$), customer satisfaction collapses and 1-star reviews surge by 78.4%.
> 
> Rather than offering blanket price discounts, our platform prescribes **dynamic freight subsidies**: injecting a targeted R\$ 5 to R\$ 10 shipping discount on carts where $F_r > 0.20$. This directly neutralizes the single largest catalyst of customer defection at a fraction of the cost of broad promotions."
