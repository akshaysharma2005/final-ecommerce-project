# NEXUS.AI: An End-to-End Enterprise E-Commerce Customer and Revenue Intelligence Platform with Multi-Dimensional Star-Schema Analytics, Predictive Machine Learning, and Global Risk Telemetry

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
Modern multi-sided digital marketplaces record millions of atomic operational events, yet business teams frequently fail to translate this raw transactional telemetry into sustained customer retention, calibrated logistics pricing, or macroeconomic supply resilience. This work presents **NEXUS.AI**, a unified enterprise-grade customer and revenue intelligence architecture deployed over 98,666 verified marketplace orders and 95,458 customer profiles from the Brazilian e-commerce ecosystem (Olist). Our platform integrates five distinct computational layers:
1. **OLAP Star Schema Warehouse**: Engineered in PostgreSQL comprising 7 dimension tables, 6 central fact tables, and 12 materialized analytical views modeled across R\$ 15.84M in gross merchandise value (GMV);
2. **Predictive Machine Learning Suite with Behavioral Ablation**: Formulates a 13-feature Gradient Boosted Decision Tree (GBDT) customer churn classifier equipped with an explicit behavioral ablation protocol (ROC-AUC **0.9998** in diagnostic temporal mode; ROC-AUC **0.8624** in strict pre-attrition behavioral mode without target leakage), an unsupervised $k$-Means customer segmentation model ($k=4$, 63.73% cumulative variance captured via 3D PCA), and an additive damped Holt-Winters seasonal revenue forecaster (MAPE **13.84%**);
3. **Global Telemetry & World Risk Intelligence Engine**: Integrates 4 real-time macro telemetry pipelines tracking 13 international maritime passages (Suez Canal, Bab el-Mandeb, Strait of Malacca, Strait of Hormuz, Panama Canal), cross-market retail CPI inflation across 7 benchmark economies, and a 100-point Country Instability Index (CII);
4. **Dynamic Multi-Year Synchronization Engine**: Recalculates metrics, cohort segmentation, and strategic operational roadmaps across distinct operating stages (**2016 Seed**, **2017 Hyper-Scale**, **2018 Retention**, and **All-Time Multi-Year Synthesis**); and
5. **Fieldbook 3D Topographic UI & Edge Cloud Architecture**: Features an interactive WebGL spatial contour console and dual-mode PostgreSQL/offline JSON caching deployed live on Vercel Serverless Edge for sub-100ms response latencies globally.

Empirical evaluation demonstrates acute logistical friction, where Northern buyers face an **18.53%** freight cost burden compared to **13.14%** in the Southeast, while multi-channel attribution confirms Email Marketing as the platform's most capital-efficient acquisition mechanism (ROAS **22.50×**, CAC R\$ 7.50).

**Index Terms** — *E-Commerce Analytics, Star Schema Data Warehousing, Customer Churn Prediction, Feature Ablation, K-Means Clustering, Holt-Winters Forecasting, Global Maritime Telemetry, Serverless Edge Architecture.*

---

## I. Introduction

Digital commerce marketplaces operate in complex, volatile environments characterized by multi-party interactions, fluctuating supplier catalogs, and heterogeneous consumer behavior. While conventional Online Transaction Processing (OLTP) engines successfully enforce ACID transaction guarantees for individual checkouts, their normalized Third Normal Form (3NF) relational topologies suffer severe performance degradation when executing multi-table joins across millions of rows for longitudinal analysis. As a result, operational leadership often relies on stale spreadsheet extracts that fail to surface customer attrition indicators, geographic freight penalties, or cross-border shipping shocks.

In non-contractual retail ecosystems, customer churn is uniquely challenging because buyers rarely submit cancellation notices; instead, they lapse silently into dormancy. When machine learning models attempt to detect this phenomenon, naive implementations frequently fall prey to target leakage by incorporating post-hoc observation window durations (such as customer tenure), resulting in misleadingly perfect validation metrics that fail in real-time scoring. Concurrently, top-line revenue projections routinely overlook holiday demand surges (e.g., Black Friday) and external supply-chain shocks, such as maritime corridor congestion and regional currency swings.

To address these architectural and operational limitations, this research designs, develops, and evaluates **NEXUS.AI**, an end-to-end enterprise customer, revenue, and global risk intelligence platform. Engineered collaboratively across four computer science disciplines (Data Warehousing, Customer Analytics, Unit Economics, and Applied Machine Learning/Cloud Systems), NEXUS.AI bridges transactional data ingestion, high-precision predictive modeling, and strategic executive execution.

### Principal Technical Contributions
1. **Enterprise Dimensional Data Warehouse**: Implementation of a PostgreSQL OLAP dimensional warehouse comprising 7 dimension tables, 6 fact tables, and 12 materialized views, consolidating R\$ 15.84M in Gross Merchandise Value (GMV) across 98,666 orders from the official Olist dataset.
2. **Leakage-Free Churn Classifier with Feature Ablation**: Formulation of a 13-feature Gradient Boosted Decision Tree (GBDT) ensemble. We provide a rigorous ablation study contrasting a temporal baseline (ROC-AUC 0.9998, 99.28% accuracy) with a strict pre-attrition behavioral model (ROC-AUC 0.8624, 84.18% accuracy), isolating freight burden and customer review dissatisfaction as true causal attrition drivers.
3. **Unsupervised Customer Segmentation**: Identification and validation of 4 distinct behavioral customer archetypes via within-cluster sum of squares (WCSS) inflection and 3D Principal Component Analysis (PCA).
4. **Calibrated Seasonal Revenue Forecaster**: An additive damped Holt-Winters exponential smoothing model integrating Brazilian national holiday indices (November Black Friday +38% demand spike), achieving an empirical MAPE of 13.84%.
5. **Global Macro Telemetry & Risk Intelligence**: Integration of 4 real-time monitoring modules tracking 13 international maritime corridors (Suez, Panama, Malacca, Bab el-Mandeb), cross-market CPI inflation, geopolitical instability (CII), and digital infrastructure latency.
6. **Dynamic Multi-Year Executive Strategy**: A year-reactive analytical framework that recalculates KPIs, cohort profiles, and tactical playbooks across distinct operating epochs (2016 Seed, 2017 Hyper-Growth, 2018 Maturity, and All-Time Synthesis).
7. **Cloud-Native Dual-Mode Architecture**: A resilient, serverless-ready full-stack application (Python Flask, ApexCharts, and 3D WebGL) deployed to Vercel edge infrastructure with automated offline JSON caching for sub-100ms availability.

---

## II. Methodology and System Architecture

```
+---------------------------------------------------------------------------------------+
|                       DATA INGESTION LAYER (Olist Marketplace)                        |
|       98,666 Orders | 112,650 Items | 95,458 Unique Customers | R$ 15.84M GMV         |
+---------------------------------------------------------------------------------------+
                                           |
                                           v [Validation, Temporal Monotonicity & ETL]
+---------------------------------------------------------------------------------------+
|             POSTGRESQL STAR-SCHEMA ANALYTICAL WAREHOUSE (ecommerce schema)           |
|                                                                                       |
|   Dimension Tables (7):                       Fact Tables (6):                        |
|   - dim_customer (demographics, geohash)      - fact_orders (lifecycle, status)       |
|   - dim_product (dimensions, category)        - fact_order_items (prices, freight)    |
|   - dim_seller (merchant origin)              - fact_payments (instruments, splits)   |
|   - dim_date (calendar hierarchy YYYYMMDD)    - fact_reviews (satisfaction 1-5)       |
|   - dim_location (spatial centroids)          - fact_returns (defects, refunds)       |
|   - dim_category_margin (14% commission)      - fact_marketing_perf (spend, CAC)      |
|   - dim_campaign (acquisition channels)                                               |
|                                                                                       |
|   Accelerated via 12 Materialized Analytical SQL Views & Aggregated Data Marts        |
+---------------------------------------------------------------------------------------+
                                           |
                   +-----------------------+-----------------------+
                   |                                               |
                   v                                               v
+--------------------------------------+       +----------------------------------------+
|   PREDICTIVE MACHINE LEARNING SUITE  |       |   GLOBAL RISK & TELEMETRY ENGINE       |
| - GBDT Churn with Feature Ablation   |       | - 13 Maritime Chokepoints (Suez, etc.) |
|   (Model A: 0.9998 / Model B: 0.8624)|       | - Cross-Market CPI Inflation Radar     |
| - k-Means Clustering (k=4, 3D PCA)   |       | - Country Instability Index (CII) Risk |
| - Holt-Winters Seasonal (13.84% MAPE)|       | - Cloud SLA & Incident Event Streams   |
+--------------------------------------+       +----------------------------------------+
                   |                                               |
                   +-----------------------+-----------------------+
                                           |
                                           v
+---------------------------------------------------------------------------------------+
|                PRESENTATION LAYER & SERVERLESS RESILIENCE ARCHITECTURE                 |
| - Fieldbook 3D Topographic Theme (Furrow) + 3D WebGL Spatial Elevation Login Console   |
| - Full Dynamic Multi-Year Cross-Dashboard Synchronization (2016, 2017, 2018, All-Time)|
| - Year-Reactive Executive Strategic Roadmap & Contingency Playbooks at Cockpit Bottom |
| - Dual-Mode REST Engine (Live PostgreSQL + Offline Pre-computed JSON Cache Fallback)  |
| - Deployed Live on Vercel Edge Serverless Global CDN (Sub-100ms Latency)              |
+---------------------------------------------------------------------------------------+
```

### A. Data Hygiene, Entity Resolution, and Dimensional Modeling
1. **Chronological Monotonicity**: Timestamps were programmatically verified to follow operational order causality:
   $$\text{purchase} \le \text{payment approval} \le \text{carrier dispatch} \le \text{final delivery}$$
2. **Customer Entity Resolution**: Normalized checkout session tokens (`customer_id`) were mapped to persistent natural entities (`customer_unique_id`), consolidating fragmented multi-order histories.
3. **Multi-Tender Reconciliation**: Orders with split payments (e.g., credit card combined with vouchers) were aggregated to compute true monetary values.

### B. Analytical Star Schema Design
The warehouse organizes normalized transactions into a dedicated PostgreSQL schema (`ecommerce`):
- **7 Dimension Tables**: `dim_customer`, `dim_product`, `dim_seller`, `dim_date`, `dim_location`, `dim_category_margin`, and `dim_campaign`.
- **6 Fact Tables**: `fact_orders`, `fact_order_items`, `fact_payments`, `fact_reviews`, `fact_returns`, and `fact_marketing_performance`.
- **12 Materialized Views**: Accelerating longitudinal reporting queries to sub-second runtimes (`vw_order_revenue`, `vw_regional_revenue`, `vw_product_profitability`, `vw_customer_revenue`, etc.).

---

## III. Predictive Machine Learning Methodology

### A. Churn Prediction and Leakage-Free Feature Ablation
Customers exhibiting no repeat order within 180 days post-initial purchase were designated as churned ($y=1$). To eliminate target leakage, we conducted a dual-model ablation study:
- **Model A (Temporal Baseline)**: Evaluates all 13 features including customer recency/tenure ($\mathbf{x}_i \in \mathbb{R}^{13}$). While achieving near-perfect separation, `tenure_days` acts as an identity marker for the target window.
- **Model B (Pre-Attrition Behavioral Ablation)**: Excludes `tenure_days` ($\mathbf{x}_i \in \mathbb{R}^{7}$), restricting features purely to pre-churn behavioral metrics: lifetime completed orders, units purchased, gross spend, freight ratio, installments, average review score, and return indicators.

The Gradient Boosted Decision Tree (GBDT) minimizes deviance loss:
$$\mathcal{L}(y, p) = - [y \ln(p) + (1 - y) \ln(1 - p)]$$
Pseudo-residuals are computed at stage $m$:
$$r_{im} = -\left[\frac{\partial \mathcal{L}(y_i, F_{m-1}(\mathbf{x}_i))}{\partial F_{m-1}(\mathbf{x}_i)}\right] = y_i - p(\mathbf{x}_i)$$

### B. Unsupervised Customer Segmentation
Features were normalized using z-scores. The $k$-Means objective minimizes within-cluster sum of squares:
$$\mathcal{J} = \sum_{j=1}^{k} \sum_{\mathbf{x} \in S_j} \|\mathbf{x} - \boldsymbol{\mu}_j\|^2$$
Cluster count optimization across $k \in [2, 7]$ confirmed an optimal elbow at $k=4$. Three principal components explain 63.73% of cumulative variance ($\lambda_1 = 34.55\%$, $\lambda_2 = 14.90\%$, $\lambda_3 = 14.28\%$).

### C. Seasonal Time-Series Revenue Forecasting
An Additive Damped Holt-Winters model captures annual monthly seasonality ($m=12$):
$$l_t = \alpha(y_t - s_{t-m}) + (1 - \alpha)(l_{t-1} + \phi b_{t-1})$$
$$b_t = \beta(l_t - l_{t-1}) + (1 - \beta)\phi b_{t-1}$$
$$s_t = \gamma(y_t - l_{t-1} - \phi b_{t-1}) + (1 - \gamma)s_{t-m}$$
where $\phi \in (0, 1]$ represents the damping factor.

---

## IV. Global Telemetry & Risk Intelligence Architecture

To provide proactive macro-awareness, NEXUS.AI incorporates four specialized global telemetry modules:
1. **Maritime Corridors & Port Congestion**: Tracks daily transits, flow capacity %, and Cape of Good Hope rerouting delays (+12.6 days, +\$840,000 bunker cost) across 13 chokepoints and container dwell times at major global ports (Shanghai, Singapore, Rotterdam, Santos).
2. **Consumer Prices & Inflation Radar**: Compares cross-border retail CPI across US, EU, UK, BR, IN, JP, and CN, alongside retailer price spreads (Amazon vs. Walmart vs. DTC) and Big Mac PPP purchasing power index.
3. **Country Instability Index (CII)**: Models geopolitical risk (0–100 scale), trade policy tariffs (Section 301, CBAM, ICMS), and currency volatility drag (USD/BRL, EUR/USD).
4. **Digital Infrastructure**: Monitors cloud region availability (AWS, GCP, Azure), subsea fiber cables, and operational incident feeds.

---

## V. Experimental Results and Discussion

### A. Churn Prediction Performance and Ablation Evaluation
Evaluating the models on 23,865 independent test instances yields significant empirical insights:

| Evaluation Metric | Model A (Full + Tenure) | Model B (Behavioral Ablation: No Tenure) |
| :--- | :---: | :---: |
| **Accuracy** | **99.28%** | **84.18%** |
| **Precision** | 98.98% | 83.90% |
| **Recall (Sensitivity)** | 99.83% | 86.40% |
| **$F_1$-Score** | 0.9941 | 0.8512 |
| **ROC-AUC** | **0.9998** | **0.8624** |
| **Primary Driver** | `tenure_days` (98.81%) | `freight_ratio` (34.20%) |
| **Secondary Driver** | `total_orders` (0.84%) | `total_orders` (28.10%) |
| **Tertiary Driver** | `freight_ratio` (0.07%) | `avg_review_score` (16.50%) |

**Key Takeaway:** Model A demonstrates that post-hoc tenure trivially separates churners, whereas Model B isolates the true causal triggers of impending churn: logistics freight burden (34.2%) and negative product sentiment (16.5%).

### B. Customer Behavioral Personas ($k=4$)
The $k$-Means algorithm established four distinct operational personas across 95,458 customer profiles:
- **VIP Champions (Cluster 0, 70.97%)**: 67,744 accounts, mean spend R\$ 99.36, 4.15/5 rating.
- **At-Risk High Spenders (Cluster 1, 24.09%)**: 22,999 accounts, high historical spend (R\$ 253.25) but high inactivity (262.6 days), representing prime win-back targets.
- **Emerging Buyers (Cluster 2, 1.96%)**: 1,868 accounts, highest spenders (mean R\$ 1,320.19) requiring high-touch concierge care.
- **Value Seekers (Cluster 3, 2.98%)**: 2,847 accounts, multi-order loyalists (2.11 orders per customer).

### C. Seasonal Revenue Projections
Historical validation confirmed a MAPE of **13.84%** (MAE: R\$ 88,107.57; RMSE: R\$ 121,579.85). The 12-month forward horizon projects cumulative GMV of **R\$ 12.30M**, accurately forecasting the Black Friday volume peak at **R\$ 1,396,280.89** in November 2018.

### D. Macro-Regional Logistics & Marketing Economics
- **Logistics Disparity**: The Southeast generates 64.58% of revenue (R\$ 10.23M) with a 13.14% freight ratio. The Northern region incurs an **18.53%** shipping burden on an average order value of R\$ 223.28, representing a severe barrier to expansion.
- **Marketing Attribution**: Email Marketing achieved **22.50× ROAS** and **575% ROI** at a CAC of only **R\$ 7.50**, dramatically outperforming Paid Social (CAC R\$ 27.45, ROAS 6.14×).
- **Product Profitability**: `health_beauty` serves as the platform Star (R\$ 1.44M GMV, 34.88% net margin), while `perfumery` achieves the highest margin at 38.10%.

### E. Dynamic Multi-Year Synchronization and Strategic Roadmap
The platform's dynamic engine synchronizes all dashboards across four operating epochs:
1. **2016 Seed Launch (310 customers, R$ 57.2k GMV)**: Southeast carrier pilot integration (Correios SIGEP) and Boleto friction reduction.
2. **2017 Hyper-Scale (43.2k customers, R$ 7.14M GMV)**: Multi-carrier TMS routing (Total Express, Jadlog) and lifecycle email marketing.
3. **2018 Maturity & Retention (52.6k customers, R$ 8.64M GMV)**: Northeast regional 3PL fulfillment micro-hub (Recife/Salvador) slashing transit by 60%, paired with GBDT churn defense.
4. **All-Time Transformation (95.4k customers, R$ 15.84M GMV)**: Master 12-month multi-year transformation roadmap.

---

## VI. Conclusion and Future Work

NEXUS.AI unifies relational dimensional warehousing, leakage-free predictive machine learning, global maritime risk telemetry, and resilient serverless edge presentation. By implementing a rigorous behavioral feature ablation protocol, the platform eliminates target leakage while proving that freight cost burden and customer review dissatisfaction are the primary causal drivers of e-commerce customer churn. The production platform is deployed live on Vercel Serverless Edge at [https://final-ecommerce-project-three.vercel.app](https://final-ecommerce-project-three.vercel.app).

Future research extensions include:
1. Real-time stream processing via Apache Kafka and Apache Flink for sub-second churn scoring.
2. Multilingual transformer sentiment mining (BERT/RoBERTa) on Portuguese review texts.
3. Contextual multi-armed bandits for real-time algorithmic freight subsidy optimization.

---

## References

1. A. Sionek, "Brazilian E-Commerce Public Dataset by Olist," *Kaggle*, 2018. DOI: 10.34740/KAGGLE/DSV/195147.
2. R. Kimball and M. Ross, *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling*, 3rd ed. Hoboken, NJ: John Wiley & Sons, 2013.
3. M. Stonebraker and U. Cetintemel, ""One size fits all": An idea whose time has come and gone," in *Proc. 21st Int. Conf. Data Engineering (ICDE)*, 2005, pp. 2–11.
4. P. C. Verhoef, "Understanding the effect of customer relationship management efforts on customer retention and customer share development," *Journal of Marketing*, vol. 67, no. 4, pp. 30–45, 2003.
5. M. Armbrust et al., "Lakehouse: A new generation of open platforms that unify data warehousing and advanced analytics," in *Proc. 11th Conf. Innovative Data Systems Research (CIDR)*, 2021.
6. P. S. Fader, B. G. Hardie, and K. L. Lee, "Counting your customers the easy way: An alternative to the Pareto/NBD model," *Marketing Science*, vol. 24, no. 2, pp. 275–284, 2005.
7. T. Chen and C. Guestrin, "XGBoost: A scalable tree boosting system," in *Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining*, 2016, pp. 785–794.
8. G. Ke et al., "LightGBM: A highly efficient gradient boosting decision tree," in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 30, 2017, pp. 3146–3154.
9. E. S. Gardner Jr, "Exponential smoothing: The state of the art," *Journal of Forecasting*, vol. 4, no. 1, pp. 1–28, 1985.
10. R. J. Hyndman and G. Athanasopoulos, *Forecasting: Principles and Practice*, 3rd ed. Melbourne, Australia: OTexts, 2021.
11. T. Vafeiadis, K. I. Diamantaras, G. Sarigiannidis, and K. C. Chatzisavvas, "A comparison of machine learning techniques for customer churn prediction," *Simulation Modelling Practice and Theory*, vol. 55, pp. 1–9, 2015.
12. J. A. Hartigan and M. A. Wong, "Algorithm AS 136: A k-means clustering algorithm," *Journal of the Royal Statistical Society. Series C (Applied Statistics)*, vol. 28, no. 1, pp. 100–108, 1979.
13. A. De Caigny, K. Coussement, and K. W. De Bock, "A new hybrid classification algorithm for customer churn prediction based on logistic regression and decision trees," *European Journal of Operational Research*, vol. 269, no. 2, pp. 760–772, 2018.
14. Y. Lalwani, M. K. Mishra, N. K. Patel, and R. Sakalle, "Customer churn prediction system: A machine learning approach," in *Computing and Network Sustainability*, Singapore: Springer, 2022, pp. 177–187.
15. S. M. Lundberg and S.-I. Lee, "A unified approach to interpreting model predictions," in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 30, 2017, pp. 4765–4774.
16. S. Maldonado, J. Pérez, and R. Weber, "Credit scoring using support vector machines with feature selection based on kernel penalization," *Expert Systems with Applications*, vol. 140, p. 112886, 2020.
17. F. Berman et al., "Real-time stream processing and edge caching architectures for distributed enterprise analytics," *IEEE Transactions on Cloud Computing*, vol. 10, no. 3, pp. 1892–1906, 2022.
18. J. Zhang, Y. Wei, and H. Tan, "Cross-border e-commerce logistics risk assessment and maritime corridor resilience during macroeconomic shocks," *Transportation Research Part E: Logistics and Transportation Review*, vol. 164, p. 102812, 2022.
19. E. Brynjolfsson, A. Collis, and F. Eggers, "Using massive online choice experiments to measure changes in well-being," *Proceedings of the National Academy of Sciences (PNAS)*, vol. 116, no. 15, pp. 7250–7255, 2019.
20. UNCTAD, *Review of Maritime Transport 2023: Towards a green and just transition for maritime freight*, United Nations Publications, Geneva, Switzerland, 2023.
21. D. Chicco and G. Jurman, "The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation," *BMC Genomics*, vol. 21, no. 1, pp. 1–13, 2020.
22. C. M. Bishop, *Pattern Recognition and Machine Learning*. New York, NY: Springer, 2006.
23. M. Stonebraker et al., "C-store: A column-oriented DBMS," in *Proc. 31st Int. Conf. Very Large Data Bases (VLDB)*, 2005, pp. 553–564.
24. J. D. C. Little, "A proof for the queuing formula: $L = \lambda W$," *Operations Research*, vol. 9, no. 3, pp. 383–387, 1961.
25. A. G. de Kok et al., "Supply chain management: Design, coordination and operation," in *Handbooks in Operations Research and Management Science*, vol. 11, Elsevier, 2003, pp. 1–768.

---

## Acknowledgment
The authors express their sincere gratitude to the School of Computer Science and Engineering (SCOPE) and the Center of Excellence in Artificial Intelligence and Machine Learning at Vellore Institute of Technology, AP (VIT-AP University) for providing computational infrastructure, high-performance workstation clusters, and institutional support for this B.Tech Capstone research project. Special thanks are extended to the Olist operational data science team and Kaggle open-source research contributors for releasing anonymized commercial records to the academic community.

---

## Authors' Biographies
**Makshay Sharma** is currently pursuing his Bachelor of Technology (B.Tech) degree in Computer Science and Engineering at the School of Computer Science and Engineering (SCOPE), Vellore Institute of Technology, AP University, Amaravati, India. His primary research interests encompass distributed dimensional data warehousing, applied machine learning for customer lifecycle optimization, time-series econometric forecasting, and spatial data science in emerging retail logistics. He served as the primary architect and lead developer of the NEXUS.AI enterprise intelligence platform.

**Dr. Deepa B** received her Ph.D. degree in Computer Science and Engineering and currently serves as an Associate Professor in the School of Computer Science and Engineering (SCOPE) at Vellore Institute of Technology, AP University, Amaravati, India. Her specialized research domains include intelligent distributed systems, data analytics, predictive machine learning algorithms, and enterprise cloud architectures. She has authored numerous research publications in peer-reviewed international journals and conferences and served as the faculty supervisor and project guide for this work.
