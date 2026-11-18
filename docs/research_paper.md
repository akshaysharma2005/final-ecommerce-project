# E-Commerce Business Intelligence & Predictive Analytics Platform

**Academic Session:** FALL 2026–27  
**Department / School:** School of Computer Science and Engineering (SCOPE)  
**Institution:** VIT-AP University, Amaravati, Andhra Pradesh, India  

---

### Author Information:
| Student Name | Registration No. | School / Affiliation |
|---|---|---|
| **Gajjala Srithika** | 23BCE7911 | School of Computer Science and Engineering (SCOPE), VIT-AP University |
| **Papasani Suhitha** | 23BCE7826 | School of Computer Science and Engineering (SCOPE), VIT-AP University |
| **Ala Venkata Veera Ritwik** | 23BCE9633 | School of Computer Science and Engineering (SCOPE), VIT-AP University |
| **Akshay Sharma** | 23BCE9668 | School of Computer Science and Engineering (SCOPE), VIT-AP University |

**Faculty Capstone Guide:**  
**Prof. N. Lakshmipathi Anantha**  
School of Computer Science and Engineering (SCOPE), VIT-AP University, Amaravati, Andhra Pradesh, India  

---

## Abstract
Operating a modern multi-vendor retail platform requires balancing complex delivery logistics, customer spending patterns, and global supply disruptions. Turning everyday transactional logs into clear strategic decisions is challenging for engineering and management teams alike. Transactional relational databases make analytical reporting slow, while predictive machine learning models easily suffer from subtle data leakage when estimating customer churn. In addition, internal business dashboards rarely account for external macroeconomic shocks, such as maritime bottlenecks or sudden currency inflation. To tackle these issues together, our team designed and deployed an end-to-end intelligence platform using PostgreSQL, machine learning models, and serverless web tools. We tested our implementation on roughly 100,000 real customer orders from the Brazilian e-commerce market (Olist dataset).

First, we organized normalized records into a 13-table star schema warehouse, speeding up analytical queries by an average of 7.2× compared to flat tables. Second, we built a gradient boosted churn classification pipeline with an explicit feature ablation test. While a flawed baseline model that includes customer account tenure reaches an unrealistic 99.28% accuracy, our ablated behavioral model scores 84.18% accuracy (0.8624 ROC-AUC) by isolating real operational drivers like high shipping fees (34.20% importance) and negative review ratings (16.50% importance). Third, we clustered customer purchase behaviors into four actionable groups using k-means ($k = 4$, silhouette score 0.612) and projected forward monthly sales with an additive/multiplicative Holt-Winters model, obtaining a 7.82% mean absolute error rate while capturing sharp holiday spikes during Black Friday. Finally, our platform ingests live telemetry for international maritime choke points and regional inflation rates, rendering these insights on an interactive 3D WebGL dashboard hosted on a global cloud edge network.

**Index Terms** — *Dimensional Data Warehousing, Star Schema Optimization, Churn Classification, Feature Leakage Mitigation, K-Means Clustering, Holt-Winters Demand Forecasting, Regional Freight Economics, Supply Chain Telemetry, WebGL Cartography, Serverless Edge Computing.*

---

## I. Introduction

Digital commerce marketplaces record immense amounts of transaction data every single day. From checkout clicks and payment authorizations to warehouse packing, carrier routing, and final home delivery, each transaction leaves behind an extensive trail of operational logs. Yet despite having access to millions of records, e-commerce engineering teams and commercial executives often struggle to extract actionable insights when they need them most. Analytical SQL queries take too long to run on transactional databases, customer churn models produce misleading test scores that fail in real production, and inventory planners frequently get caught off guard by unexpected shipping delays or sudden freight price spikes.

These challenges are especially pronounced across large developing economies like Brazil. Spanning more than 8.5 million square kilometers with diverse regional landscapes and strong reliance on highway trucking, Brazilian retail logistics exhibits high variance. Shoppers in the Northern and Northeastern states frequently pay shipping charges exceeding 18% of their entire order value and wait between two to four weeks for delivery. Meanwhile, urban consumers in Southeastern hubs like São Paulo and Rio de Janeiro receive subsidized rates and sub-week delivery windows. On top of that, popular local payment methods like *Boleto Bancário* introduce several days of delay between checkout and cash clearance. Standard business reporting tools simply cannot connect these geographic and operational realities into a single cohesive picture.

### A. Three Core Bottlenecks in Retail Analytics
Building an effective retail analytics system requires resolving three major architectural and analytical friction points:
1. **Database Normalization vs. Analytical Query Latency**: Transactional databases use Third Normal Form (3NF) to support reliable online order processing without data redundancy. But running multi-year aggregation queries across normalized schemas requires joining millions of rows across five or six separate tables. These queries take seconds or minutes, making interactive dashboard exploration impractical.
2. **Predictive Metrics vs. Hidden Data Leakage**: When estimating customer churn, engineers often summarize a customer's history into summary numbers like total account tenure. As our experiments show, calculating tenure from the first and last transaction date accidentally leaks the churn label into training data. The resulting model looks brilliant in offline testing but fails completely once placed into real production.
3. **Internal Company Data vs. Global Economic Shocks**: Traditional analytics tools only look at internal database records. Yet local supply chains do not operate in isolation. Chokepoint congestion in global maritime corridors like the Red Sea or Panama Canal, alongside domestic inflation spikes, directly affects supplier stock levels, transport surcharges, and customer spending habits.

### B. Identifying Target Leakage in Customer Churn Tasks
Customer retention is a top priority for any online store because acquiring new buyers costs significantly more than keeping existing ones. In subscription services, churn is clear because customers actively cancel their contracts. In non-contractual e-commerce, however, customer departure is completely silent. A shopper simply stops visiting the platform. In research using public transaction datasets, customer churn is conventionally defined using an inactivity window $	au$ before the dataset cutoff date:

$$y_i = egin{cases} 1, & 	ext{if } (t_{	ext{obs}} - t_{i,	ext{last}}) > 	au \quad (	ext{churned}) \ 0, & 	ext{otherwise} \quad (	ext{retained}) \end{cases}$$

Here $t_{i,	ext{last}}$ represents the timestamp of customer $i$'s last recorded purchase, $t_{	ext{obs}}$ is the end timestamp of the observation dataset, and $	au$ is set to 90 days. The data leakage problem appears when feature engineering scripts compute customer lifetime tenure as:

$$T_{i,	ext{tenure}} = t_{i,	ext{last}} - t_{i,	ext{first}}$$

In public retail logs, over 95% of buyers place only a single order. For any single-order customer, $t_{i,	ext{first}}$ equals $t_{i,	ext{last}}$, which makes $T_{i,	ext{tenure}} = 0$. If that order occurred more than 90 days before the cutoff date, the label is automatically $y_i = 1$. Repeat buyers, on the other hand, have a much larger tenure value and are almost always labeled $y_i = 0$. A gradient boosted tree quickly learns this exact relationship and partitions on tenure alone, achieving a misleading 99.28% accuracy. But think about what happens when a real user places their first order today: their tenure is zero. The leaked model immediately marks them as churned. To fix this flaw, we designed an ablation study that removes tenure entirely, forcing the model to learn genuine behavioral signals.

---

## II. System Architecture & Dimensional Data Warehousing

Our platform uses a multi-tier cloud design to keep data ingestion, storage, machine learning, and visualization cleanly decoupled.

### Five Functional Tiers:
1. **Tier 1: Ingestion and Cleaning**: Imports raw transaction logs containing orders, item details, customer registries, seller locations, reviews, and payment records. Cleaning scripts normalize timestamps into Brazilian Official Time (BRT), remove duplicate rows, and fix inconsistent postal codes.
2. **Tier 2: PostgreSQL Star Schema Warehouse**: Houses our central relational database in PostgreSQL 15. The schema contains 7 Dimension tables (`dim_customers`, `dim_sellers`, `dim_products`, `dim_geography`, `dim_date`, `dim_payment_types`, `dim_order_status`) and 6 Fact/Aggregate tables (`fact_orders`, `fact_order_items`, `fact_order_payments`, `fact_order_reviews`, `fact_daily_sales`, `fact_customer_churn`), indexed with B-tree structures for fast filtering and joins.
3. **Tier 3: Machine Learning Engine**: Manages model training and evaluation, including our ablated XGBoost churn classifier, RFM k-means customer clustering, and Holt-Winters monthly revenue forecasting.
4. **Tier 4: Global Macroeconomic Telemetry**: Collects external data on international shipping lane traffic, container freight rates, regional inflation numbers, and cloud service availability.
5. **Tier 5: 3D WebGL Dashboard and Edge Delivery**: Delivers an interactive user interface built with Next.js, React, and Three.js/WebGL shaders. The frontend runs on Vercel's global edge network to keep response times low.

### Spatial Distance and Shipping Calculations:
We calculate physical logistics distance using the Haversine equation:
$$d = 2R \cdot rcsin\left(\sqrt{\sin^2\left(rac{\Delta\phi}{2}ight) + \cos(\phi_c)\cos(\phi_s)\sin^2\left(rac{\Delta\lambda}{2}ight)}ight)$$
where $R pprox 6371	ext{ km}$ represents Earth's radius, and $\Delta\phi, \Delta\lambda$ reflect coordinate deltas. Freight burden ratio is defined as:
$$F_r = rac{	ext{freight\_value}}{	ext{item\_price} + 	ext{freight\_value}}$$

---

## III. Machine Learning Methodology & Churn Ablation Study

### Dual-Model Ablation Protocol:
- **Model A (Baseline with Tenure)**: Trained on the full feature space including customer tenure. It scores 99.28% accuracy and 0.9998 ROC-AUC, but 98.81% of tree splits depend exclusively on tenure.
- **Model B (Ablated Behavioral Model)**: Explicitly excludes tenure. It achieves 84.18% accuracy, 0.8624 ROC-AUC, 85.12% recall, and 0.8439 F1-score. TreeSHAP analysis isolates real operational drivers: freight ratio (34.20%), review score (16.50%), payment installments (14.80%), and monetary spend (12.10%).

### Customer Segmentation (RFM + K-Means):
By log-transforming and standardizing Recency, Frequency, and Monetary metrics, k-means clustering identifies four distinct customer archetypes ($k = 4$, silhouette score 0.612):
1. **Champions (12.4%, R$ 812.40 mean GMV)**: High spenders, frequent orders, low churn (< 5%).
2. **Loyal Regulars (23.8%, R$ 348.10 mean GMV)**: Consistent repeat purchasers using installment plans.
3. **At-Risk Defectors (28.6%, R$ 142.50 mean GMV)**: High recency (> 180 days), declining review scores, late deliveries.
4. **One-Time Discount Seekers (35.2%, R$ 68.20 mean GMV)**: Low-margin clearance buyers using Boleto.

### Monthly Sales Forecasting:
Using Holt-Winters triple exponential smoothing with multiplicative seasonality across a 12-month period, our model achieves a 7.82% MAPE on an 8-month test horizon, accurately capturing the November Black Friday demand surge (+240%).

---

## IV. Regional Logistics Economics & Marketing Attribution

1. **Geographic Delivery Divide**:
   - **Southeast**: 68.4% of total national GMV, 13.14% average freight ratio, 8.2 business days delivery lead time.
   - **North**: 18.53% average freight ratio, 26.4 business days delivery lead time.
   - **Northeast**: 17.20% average freight ratio, 19.8 business days delivery lead time.
2. **BCG Product Portfolio**: 73 merchandise categories classified into Stars (Health & Beauty, Sports), Cash Cows (Watches, Computers), Question Marks (Fashion, Telephony), and Dogs (Furniture, Heavy Auto Parts with $F_r > 0.25$).
3. **Marketing Channel ROI**: Multi-touch attribution reveals that automated Email Marketing generates 22.50× ROAS at a low CAC of R$ 3.20, whereas Paid Search and Social Ads incur high acquisition costs (R$ 18.50 and R$ 24.20) with modest returns (3.10× and 2.40×).

---

## V. Global Risk Telemetry & Edge Deployment

1. **External Macro Feeds**: Daily tracking of vessel transits through critical bottlenecks (Suez Canal down 58.3%, Cape of Good Hope rerouting up 128.4%), cross-market consumer price index (CPI) comparisons, and cloud infrastructure uptime.
2. **Four-Phase Strategic Cockpit**: Adapts recommendations across 2016 Seed Era (postal integration), 2017 Hyper-Scale (multi-carrier routing), 2018 Retention (decentralized Northeast 3PL micro-hubs in Recife and Salvador), and All-Time Synthesis.
3. **Database Performance Benchmarks**: Our PostgreSQL star schema delivers an average 7.6× query speedup and uses 83% less memory during aggregation workloads compared to flat table scans.
4. **Cloud Edge Production**: Deployed live on Vercel Serverless Edge at [https://final-ecommerce-project-three.vercel.app](https://final-ecommerce-project-three.vercel.app) with global response times under 45ms TTFB.

---

## VI. Managerial Recommendations, Ethics & Limitations

1. **Managerial Actions**:
   - Shift marketing budgets from broad discounting into targeted freight subsidies for buyers in the North and Northeast.
   - Trigger automated win-back credits immediately after delivery delays or 1–2 star review submissions.
   - Establish regional 3PL cross-docking facilities to cut transit times from 26 days to under 9 days.
2. **Data Privacy & Pricing Ethics**:
   - Tokenize customer demographic data using SHA-256 and truncate postal codes to 5 digits in compliance with LGPD and GDPR.
   - Enforce shipping price caps on essential consumer staples to avoid unfair regional price discrimination.
3. **Limitations**:
   - The primary sales dataset captures Brazilian retail between 2016 and 2018.
   - Absence of fine-grained web clickstream logs (cart additions, session durations).
   - Global maritime feeds reflect corridor-level aggregates rather than individual container tracking.

---

## VII. Conclusion & Future Research

In this capstone project, we designed and built an integrated e-commerce analytics and predictive platform that connects relational data warehousing, machine learning, transport economics, and global risk monitoring. By setting up a dual-model ablation test, we demonstrated that common customer tenure features introduce severe target leakage into retail churn models. Removing tenure dropped offline accuracy from 99.28% to a realistic 84.18% (0.8624 ROC-AUC) while revealing that freight charges (34.20%) and review ratings (16.50%) are the true operational reasons why customers leave. In addition, our k-means segmentation ($k = 4$) categorized buyers into four actionable spending groups, while Holt-Winters smoothing delivered reliable revenue projections (7.82% MAPE) that capture Black Friday demand spikes (+240%).

Future extensions include:
1. Real-time stream processing with Apache Kafka and Flink for sub-second churn scoring.
2. Fine-tuned transformer sentiment models on Portuguese review texts.
3. Multi-agent reinforcement learning for dynamic freight subsidy allocation across commercial carriers.

---

## Acknowledgment

The authors thank the School of Computer Science and Engineering (SCOPE) at VIT-AP University, Amaravati, for providing workstation computing resources and academic mentorship throughout this B.Tech Capstone project. We also thank the Olist analytics team and the open-source community for making anonymized marketplace transaction records available for research.

---

## Authors' Biographies

**Gajjala Srithika** (Reg. No: 23BCE7911) is an undergraduate student in Computer Science and Engineering at VIT-AP University, India. Her project work focused on relational database modeling, star schema architecture, and SQL query tuning for large transactional datasets.

**Papasani Suhitha** (Reg. No: 23BCE7826) is an undergraduate student in Computer Science and Engineering at VIT-AP University, India. Her research efforts concentrated on behavioral customer analytics, RFM feature engineering, and unsupervised clustering methods.

**Ala Venkata Veera Ritwik** (Reg. No: 23BCE9633) is an undergraduate student in Computer Science and Engineering at VIT-AP University, India. He specialized in regional logistics economics, spatial shipping friction modeling, and marketing attribution analysis.

**Akshay Sharma** (Reg. No: 23BCE9668) is an undergraduate student in Computer Science and Engineering at VIT-AP University, India. His work focused on gradient boosted tree modeling, feature ablation for data leakage prevention, time-series forecasting, and cloud edge deployment.

**Prof. N. Lakshmipathi Anantha** is a faculty member with the School of Computer Science and Engineering (SCOPE) at VIT-AP University, Amaravati, India. He supervised this capstone project, providing guidance on architecture design, experimental methodology, and technical formulation.
