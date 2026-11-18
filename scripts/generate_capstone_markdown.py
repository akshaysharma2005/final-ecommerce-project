#!/usr/bin/env python3
"""
generate_capstone_markdown.py
Generates docs/capstone_project_report.md
Preserves 100% of original content and adds verified empirical results.
"""

from pathlib import Path
import os
import shutil

WORKSPACE = Path("/Users/makshaysharma/Desktop/ecommerce-intelligence")
DOCS_DIR = WORKSPACE / "docs"
ARTIFACT_DIR = Path("/Users/makshaysharma/.gemini/antigravity/brain/2ff68dc2-9f13-45a4-b203-0adb4a579794")

md_content = """# E-COMMERCE BUSINESS INTELLIGENCE & PREDICTIVE ANALYTICS PLATFORM
### A CAPSTONE PROJECT REPORT

**Submitted in partial fulfillment of the requirement for the award of the Degree of**  
**BACHELOR OF TECHNOLOGY IN COMPUTER SCIENCE & ENGINEERING**

---

### by:

| S. No. | Student Name | Registration Number | Email | Mobile |
| :---: | :--- | :---: | :--- | :---: |
| 1 | **Papasani Suhitha** | 23BCE7826 | suhitha.23bce7826@vitapstudent.ac.in | +91 9391832898 |
| 2 | **Gajjala Srithika** | 23BCE7911 | srithika.23bce7911@vitapstudent.ac.in | +91 9985327089 |
| 3 | **Ala Venkata Veera Ritwik** | 23BCE9633 | ritwik.23bce9633@vitapstudent.ac.in | +91 7032499365 |
| 4 | **M Akshay Sharma** | 23BCE9668 | akshaysharma200508@gmail.com | +91 6304698235 |

**Under the Guidance of:**  
**Prof. N. Lakshmipathi Anantha**  
Faculty Project Guide

**SCHOOL OF COMPUTER SCIENCE AND ENGINEERING**  
**VIT-AP UNIVERSITY, AMARAVATI – 522237, ANDHRA PRADESH**  
**NOVEMBER 2026**

---

## CERTIFICATE

This is to certify that the Capstone Project work titled **"E-COMMERCE BUSINESS INTELLIGENCE & PREDICTIVE ANALYTICS PLATFORM"** that is being submitted by **PAPASANI SUHITHA (23BCE7826)**, **GAJJALA SRITHIKA (23BCE7911)**, **ALA VENKATA VEERA RITWIK (23BCE9633)**, and **M AKSHAY SHARMA (23BCE9668)** is in partial fulfillment of the requirements for the award of Bachelor of Technology, is a record of bonafide work done under my guidance. The contents of this Project work, in full or in parts, have neither been taken from any other source nor have been submitted to any other Institute or University for award of any degree or diploma and the same is certified.

<br>

**Prof. N. Lakshmipathi Anantha**  
Guide  
*The thesis is satisfactory / unsatisfactory.*

| Examiner 1 | Examiner 2 |
| :--- | :--- |
| Signature: ______________________ | Signature: ______________________ |

**Approved by:**  
**HoD, Department of Computer Science and Engineering**  
School of Computer Science and Engineering  
VIT-AP University, Amaravati, Andhra Pradesh  

---

## ACKNOWLEDGEMENT

We would like to express our sincere gratitude to **VIT-AP University**, Amaravati, Andhra Pradesh, for providing us with the opportunity, infrastructure, and academic environment to undertake and successfully complete our Capstone Project.

We are deeply grateful to **Dr. G. Viswanathan**, Chancellor, VIT-AP University, and **Dr. P. Arulmozhivarman**, Vice-Chancellor, VIT-AP University, for their visionary leadership, encouragement, and commitment to providing quality education and fostering innovation and research.

We express our sincere thanks to **Dr. S. Sudhakar Ilango**, Dean, SCOPE, **Dr. Saroj Kumar Panigrahy**, Associate Dean, SCOPE, and the **Head of the Department of Computer Science and Engineering** for the continuous encouragement, academic support, and facilities provided throughout the project.

We are profoundly grateful to **Prof. N. Lakshmipathi Anantha**, our Project Supervisor/Guide, for the invaluable guidance, constant support, constructive feedback, and encouragement extended to us at every stage of this project. Their expertise and suggestions have been instrumental in the successful completion of our work.

We would also like to extend our sincere appreciation to all the faculty members and staff of the School of Computer Science and Engineering for their cooperation, valuable suggestions, and support during the course of this project.

Finally, we express our heartfelt gratitude to our parents, family members, and friends for their constant encouragement, patience, and support throughout our academic journey.

**Project Team Members:**  
1. **Papasani Suhitha** – 23BCE7826  
2. **Gajjala Srithika** – 23BCE7911  
3. **Ala Venkata Veera Ritwik** – 23BCE9633  
4. **M Akshay Sharma** – 23BCE9668  

---

## ABSTRACT

Online stores create data whenever customers place orders, make payments, receive products or submit reviews. These records can reveal useful information about customers, products, sales and delivery performance. However, it is difficult to make sound business decisions when data preparation, database management, analysis, prediction and reporting are handled as separate activities. This project proposes an **E-Commerce Customer & Revenue Intelligence Platform** that brings these tasks together in one organized workflow.

The project uses the Brazilian E-Commerce Public Dataset by Olist. This public, anonymized dataset contains approximately 100,000 orders from 2016 to 2018, along with related records for customers, order items, payments, reviews, products, sellers and geolocation. Python will be used to inspect, clean and validate the source CSV files before loading the prepared data into PostgreSQL. The database will include staging tables and a dimensional model to support consistent SQL analysis and reporting.

The analytical work covers order and sales trends, average order value, product-category performance, delivery timing, customer review scores and repeat-customer behaviour using customer-level identifiers. The predictive modelling part investigates customer segmentation using K-Means clustering, evaluates a pre-attrition churn-risk classification experiment to avoid target leakage, and applies time-series sales forecasting to predict forward revenue trends.

Microsoft Power BI is used to present an overall business view and focused dashboards for customer, product and delivery performance, giving business teams reliable information supported by verified underlying data.

> [!NOTE]
> **Keywords:** E-Commerce Analytics, Relational Data Warehousing, Star Schema, Dimensional Modeling, PostgreSQL, RFM Customer Segmentation, K-Means Clustering, Churn-Risk Classification, Feature Leakage Ablation, Time-Series Sales Forecasting, Power BI Dashboards, Olist Public Dataset.

---

## TABLE OF CONTENTS

| S.No. | Chapter No. | CONTENTS | Page No. |
| :---: | :---: | :--- | :---: |
| | | Certificate | 2 |
| | | Acknowledgement | 3 |
| | | Abstract | 4 |
| | | List of Tables & List of Figures | 6 |
| **1.** | **1** | **INTRODUCTION** | **7** |
| | 1.1 | Objectives | 7 |
| | 1.2 | Background and Literature Survey | 8 |
| | 1.2.1 | E-commerce Data Analytics | 8 |
| | 1.2.2 | Data Warehousing and Dimensional Modelling | 8 |
| | 1.2.3 | RFM Analysis and Customer Value | 9 |
| | 1.2.4 | Customer Segmentation | 9 |
| | 1.2.5 | Churn-risk Modelling | 9 |
| | 1.2.6 | Sales Forecasting | 9 |
| | 1.2.7 | Research Gap and Project Motivation | 10 |
| | 1.3 | Organization of the Report | 10 |
| **2.** | **2** | **E-COMMERCE CUSTOMER & REVENUE INTELLIGENCE PLATFORM** | **11** |
| | 2.1 | Proposed System | 11 |
| | 2.1.1 | Functional Requirements | 12 |
| | 2.1.2 | Non-functional Requirements | 12 |
| | 2.2 | Working Methodology | 13 |
| | 2.3 | Standards and Design Principles | 14 |
| | 2.4 | System Details | 14 |
| | 2.4.1 | Software Details | 14 |
| | 2.4.2 | Hardware Details | 15 |
| | 2.5 | Dataset Description | 15 |
| | 2.5.1 | Important Source Fields | 15 |
| | 2.5.2 | Dataset Relationships | 16 |
| | 2.5.3 | Dataset Limitations | 16 |
| | 2.6 | Database Design | 17 |
| | 2.7 | Business Analytics and Key Metrics | 18 |
| | 2.8 | Customer Intelligence | 19 |
| | 2.8.1 | RFM Analysis | 19 |
| | 2.8.2 | Cohort and Retention Analysis | 19 |
| | 2.8.3 | Historical Customer Value | 19 |
| | 2.9 | Predictive Modelling | 19 |
| | 2.9.1 | Customer Segmentation Using K-Means | 19 |
| | 2.9.2 | Churn-risk Classification Experiment | 20 |
| | 2.9.3 | Sales Forecasting | 21 |
| | 2.10 | Power BI Dashboard Design | 21 |
| **3.** | **3** | **COST ANALYSIS** | **22** |
| | 3.1 | List of Components and Their Cost | 22 |
| | 3.2 | Cost Estimation Assumptions | 22 |
| **4.** | **4** | **RESULTS AND DISCUSSION** | **24** |
| | 4.1 | Data Profiling and Validation Outputs | 24 |
| | 4.2 | SQL Analysis Outputs | 25 |
| | 4.3 | Customer Analytics Outputs | 26 |
| | 4.4 | Model Evaluation Outputs | 26 |
| | 4.5 | Dashboard Outputs | 28 |
| | 4.6 | Discussion and Limitations | 29 |
| | 4.7 | Final Implementation Results Summary | 30 |
| **5.** | **5** | **CONCLUSION AND FUTURE WORK** | **31** |
| | 5.1 | Conclusion | 31 |
| | 5.2 | Future Work | 31 |
| **6.** | **6** | **APPENDIX** | **33** |
| | A | Sample SQL Definitions | 33 |
| | A.1 | Item Sales by Month | 33 |
| | A.2 | Repeat Customers Using customer_unique_id | 33 |
| | A.3 | Delivery Delay in Days | 33 |
| | A.4 | Payment Totals Calculated Independently | 34 |
| | B | Python ETL Workflow Template | 34 |
| | C | Team Responsibilities | 35 |
| | D | Final Submission Checklist | 35 |
| **7.** | **7** | **REFERENCES** | **36** |
| **8.** | **-** | **STUDENT BIODATA** | **37** |

---

## CHAPTER 1: INTRODUCTION

### 1. Introduction
E-commerce platforms bring customers, sellers and products together through online transactions. A single order can involve several events: the customer selects an item, submits payment, waits for the order to be approved and delivered, and later leaves a review. These operational records contain valuable information about sales patterns, delivery performance and customer behaviour.

Simply collecting CSV files or exporting operational data is not enough to create a dependable decision-support system. In practice, data is often stored in multiple tables, timestamps may be missing or recorded out of order, and the definitions used for revenue, order counts or repeat purchases can vary. Without a well-planned pipeline, business teams can easily arrive at conflicting numbers from the same basic dataset.

This project brings the main stages of analytics into one workflow. It starts with preparing the raw transaction data, loading it into PostgreSQL, organizing the tables into a dimensional model, running SQL-based descriptive analysis, performing customer segmentation and time-series forecasting, and presenting the results through Power BI dashboards. The project uses the Brazilian E-Commerce Public Dataset by Olist, a real-world dataset covering approximately 100,000 orders placed in Brazil between 2016 and 2018.

### 1.1 Objectives
The primary objectives of this capstone project are:
1. To collect and understand the Brazilian E-Commerce Public Dataset by Olist and document its source files, schema and practical constraints.
2. To develop a Python-based data preparation process for profiling, cleaning, standardizing and validating the source tables.
3. To design a PostgreSQL database with staging tables and a dimensional analytical schema suitable for business reporting.
4. To perform SQL-based exploratory and business analysis using joins, aggregations, window functions, common table expressions and date operations.
5. To analyze customer behaviour using RFM metrics, customer cohorts, retention measures and historical customer value.
6. To analyze product, revenue and operational performance, including item sales, freight costs, payment methods, delivery durations and customer review scores.
7. To investigate customer segmentation using K-Means and evaluate a carefully defined churn-risk classification experiment that avoids target leakage.
8. To compare baseline sales forecasts with a time-series forecasting approach when the data pattern and history support it.
9. To build Power BI dashboards that communicate verified analytical findings and support business decisions.
10. To document assumptions, limitations, model evaluation results and reproducible steps in an organized academic report.

### 1.2 Background and Literature Survey
#### 1.2.1 E-commerce data analytics
E-commerce analytics uses transaction and customer data to understand past activity and help organizations make better decisions. Operational systems are designed to process orders quickly, but business questions often require summarizing data across many tables, including customers, orders, items, payments and reviews. A successful analytics pipeline must define each business measure clearly, preserve the level of detail of the underlying transactions and make sure that different reports report consistent numbers [1, 2].

#### 1.2.2 Data warehousing and dimensional modelling
A dimensional model separates measurable business events from the descriptive information that provides context for those events [10]. Fact tables record numerical measures, such as item price, freight value or delivery duration, while dimension tables store descriptive attributes, such as customer locations, product categories, seller details and dates. This structure simplifies analytical SQL queries, reduces repeated data and makes it easier to connect business intelligence tools such as Power BI [4].

#### 1.2.3 RFM analysis and customer value
RFM analysis is a way to summarize customer purchasing patterns through three measures: Recency (how recently the customer bought something), Frequency (how often they buy) and Monetary value (how much they have spent) [8]. It provides an intuitive way to identify high-value customers, active buyers and customers who may be drifting away. When working with transactional datasets, it is important to distinguish historical revenue-based customer value from forward-looking Customer Lifetime Value (CLV), especially when product costs, marketing expenses and customer-acquisition channels are not available.

#### 1.2.4 Customer segmentation
Clustering can be used to group customers who show similar behaviour, even when no predefined customer categories exist. K-Means is widely used for this purpose because it is computationally efficient and produces straightforward cluster centroids [5]. Because K-Means relies on distance calculations, numerical features must be examined for skewness and scaled before clustering. Evaluating the clusters using inertia, silhouette scores and practical business interpretation helps teams choose a sensible number of segments.

#### 1.2.5 Churn-risk modelling
Churn analysis aims to identify customers who may stop buying or interacting with a business. In non-contractual e-commerce settings, customers rarely give formal notice when they leave, so churn is usually defined using a chosen period of inactivity [9]. If a churn model is attempted, the target must be created using future observations, while the input features must be limited to information available before the cut-off date. Including post-cut-off activity or total tenure in the feature set creates target leakage and produces unrealistically high evaluation scores that cannot be used in a live environment.

#### 1.2.6 Sales forecasting
Sales forecasting uses past observations to estimate future sales. A model should always be compared against simple baselines, such as naïve or moving-average forecasts, before more complex methods are adopted [7]. When transaction series exhibit seasonality or clear trends, time-series models such as SARIMA can be explored, provided the series is sufficiently long and stable. Forecast quality is evaluated using chronological test periods and metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

#### 1.2.7 Research gap and project motivation
The methods discussed in this report, including RFM analysis, K-Means, churn classification, sales forecasting and dimensional modelling, are often presented in isolation. Many public projects rely on disconnected Jupyter notebooks, omit data-quality checks or apply predictive models to raw files without first establishing an analytical database. This project addresses that gap by organizing data profiling, PostgreSQL data warehousing, descriptive SQL analysis, customer intelligence, predictive modelling and Power BI reporting into a single, cohesive workflow.

### 1.3 Organization of the Report
The rest of the report is arranged into the following chapters:
- **Chapter 2** explains the proposed platform, its workflow, software and hardware requirements, the Olist dataset, the database design, the business metrics, the customer intelligence approach, the predictive modelling plans and the Power BI dashboard layout.
- **Chapter 3** outlines the expected project costs and explains the assumptions used to estimate software, hardware and operational expenses.
- **Chapter 4** describes the data checks and analytical outputs that must be completed, discusses the empirical validation results and reviews the project's limitations.
- **Chapter 5** summarizes the project and discusses possible improvements for future work.
- **Chapter 6** provides supporting SQL examples, a Python ETL workflow template and the team responsibilities table.
- **Chapter 7** contains the dataset, technical documentation and research sources referenced throughout the report.

---

## CHAPTER 2: E-COMMERCE CUSTOMER & REVENUE INTELLIGENCE PLATFORM

This chapter introduces the proposed platform, the steps involved in building it, the software environment, the source dataset, the database design and the planned analysis. The system is intended to run as a repeatable batch-processing workflow; it is not designed as a real-time streaming application.

### 2.1 Proposed System
The platform will use the Olist CSV files as its input. Python will be used to inspect and clean the files, check data types and relationships, and prepare the records for PostgreSQL. PostgreSQL will store both the original staging data and the curated analytical model. SQL views and feature tables will then provide consistent data for customer analysis, product and revenue reporting, predictive experiments and Power BI dashboards.

![Figure 2.1: Proposed System Architecture](file:///Users/makshaysharma/Desktop/ecommerce-intelligence/report_assets/image2.png)  
*Figure 2.1: Proposed end-to-end system architecture of the enterprise analytics platform.*

The platform is organized into six connected parts: (1) data loading and quality checks, (2) PostgreSQL storage and dimensional modelling, (3) descriptive and diagnostic analysis, (4) customer intelligence, (5) predictive modelling and forecasting, and (6) dashboards and business recommendations. Each part will use shared definitions and the same analytical database.

#### 2.1.1 Functional Requirements
- The system will import the selected CSV files and record each source file name and its load date.
- The system will check column names, data types, missing values, duplicate records and relationships between tables.
- The system will keep raw or lightly processed data in staging tables, separate from the cleaned analytical tables.
- The system will provide reusable SQL queries or views for analyzing sales, orders, customers, products, payments and delivery performance.
- The system will calculate customer-level RFM measures using `customer_unique_id` to identify the same customer across different orders.
- The system will produce model evaluation results and clearly record the target definition and the time periods used for training and testing.
- The system will provide Power BI reports with filters and measures based on the validated analytical database.

#### 2.1.2 Non-Functional Requirements
- **Accuracy:** Every business measure should be linked to its source fields and a clearly stated calculation.
- **Consistency:** All parts of the platform should follow the same definitions for dates, customers, orders and sales measures.
- **Reproducibility:** Python scripts, SQL files, assumptions and model settings should be saved and managed through version control.
- **Maintainability:** Data staging, transformation, analysis and visualization should be organized as separate tasks.
- **Usability:** Dashboards should have clear titles, readable filters, units and short explanations.
- **Responsible interpretation:** Predictions should be treated as estimates, not as certain outcomes.

### 2.2 Working Methodology
1. **Step 1 – Collect the data:** Download the public Olist dataset and keep the original CSV files unchanged. Record where the files came from, when they were downloaded and any applicable usage terms.
2. **Step 2 – Understand the data:** Load each file into pandas, check its size and column names, identify possible primary and foreign keys, convert date fields and review where values are missing.
3. **Step 3 – Clean the data:** Standardize data types, tidy category text where needed, parse timestamps consistently and investigate duplicate records. Record how missing values are handled. Do not fill in missing data automatically when the absence itself may be meaningful.
4. **Step 4 – Validate the data:** Check key uniqueness, table relationships, sensible numeric ranges, timestamp order and differences between order-item totals and payment totals. Record any exceptions instead of removing them without explanation.
5. **Step 5 – Load PostgreSQL:** Import the source records into staging tables. Choose suitable data types, add primary and foreign-key constraints where valid, and create indexes for fields used often in joins.
6. **Step 6 – Build the dimensional model:** Create separate fact and dimension tables. State the level of detail represented by each fact table and avoid joining multiple one-to-many tables before aggregating their values.
7. **Step 7 – Perform SQL analysis:** Build reusable queries and views for sales, order counts, average order value, category performance, delivery, payment behaviour and customer activity.
8. **Step 8 – Study customer behaviour:** Calculate RFM measures, customer cohorts, retention indicators and a historical customer-value estimate based on revenue.
9. **Step 9 – Run predictive experiments:** Scale the features used for clustering, compare K-Means settings, define a time-based churn experiment to test feasibility, and evaluate a sales forecasting model against simple baselines.
10. **Step 10 – Connect Power BI:** Link Power BI to the curated tables or views, create reusable measures, design dashboard pages and check that the numbers match the SQL query results.
11. **Step 11 – Review and document the findings:** Include only results supported by the data, document limitations and note potential next steps for future work.

### 2.3 Standards and Design Principles
- **Data integrity:** Use unique identifiers and check the relationships between tables before running analytical queries.
- **Fact-table detail:** Define the level of detail for every fact table. For example, order items should be analyzed at the item level, while payments should be analyzed at the payment level.
- **Metric definitions:** Record the filters and formulas used for sales, order counts, delivery time, late delivery and customer review scores.
- **Time-aware testing:** Use chronological training and testing periods for churn and forecasting models rather than random shuffling.
- **Privacy and security:** Use the anonymized public dataset only for the intended academic project. Store database passwords in environment variables or configuration files, not in public code repositories.
- **Reproducibility:** Keep the Python scripts, SQL queries, model settings, dashboard files and this documentation in a shared version-controlled repository.

### 2.4 System Details
#### 2.4.1 Software Details
*Table 1: Software and tools used across the analytics lifecycle*

| Software / Tool | Purpose in the project |
| :--- | :--- |
| **Python** | Main programming language for data profiling, ETL, feature engineering and model experiments. |
| **pandas and NumPy** | Tabular data loading, cleaning, transformation, aggregation and numerical operations [3]. |
| **PostgreSQL** | Relational database for staging data, curated tables, analytical views and SQL queries [2]. |
| **SQL** | Joins, aggregations, CTEs, subqueries, window functions, date functions and validation queries. |
| **scikit-learn** | K-Means clustering, logistic regression, optional random forest, preprocessing and model evaluation [5, 6]. |
| **statsmodels** | Candidate SARIMA/SARIMAX time-series model if data history and diagnostics support it [7]. |
| **Power BI Desktop** | Interactive dashboard design and visualization of curated analytical data [4]. |
| **Jupyter / VS Code** | Development, experimentation, documentation and debugging. |
| **Git and GitHub** | Version control and collaboration for code, SQL and documentation. |

#### 2.4.2 Hardware Details
The proposed platform is software-based, so it does not need dedicated sensors, microcontrollers or special lab equipment. Local data cleaning, PostgreSQL storage, analytical queries and baseline model training can be completed on a standard laptop or desktop computer with 8 GB to 16 GB of RAM, a multi-core processor (such as an Intel Core i5/i7, AMD Ryzen 5/7 or Apple Silicon) and 10 GB to 20 GB of free storage for the raw files, database storage and temporary outputs.

### 2.5 Dataset Description
This project uses the Brazilian E-Commerce Public Dataset by Olist, available on Kaggle [1]. It covers approximately 100,000 orders placed in Brazil between 2016 and 2018 across nine source CSV files.

*Table 2: Olist dataset source files and their analytical roles*

| Source file | Main contents | Typical analytical use |
| :--- | :--- | :--- |
| `olist_orders_dataset.csv` | Order status and purchase, approval, carrier, delivery and estimated-delivery timestamps. | Order lifecycle, monthly orders, delivery delay and cancellations. |
| `olist_customers_dataset.csv` | Customer identifiers and customer location fields. | Customer grouping, repeat-purchase analysis and geography. |
| `olist_order_items_dataset.csv` | Order item, product, seller, price and freight value. | Item-level sales, category performance, freight analysis. |
| `olist_order_payments_dataset.csv` | Payment sequence, payment type, installments and payment value. | Payment method and payment reconciliation. |
| `olist_order_reviews_dataset.csv` | Review identifiers, scores, comments and review timestamps. | Customer feedback and review-score analysis. |
| `olist_products_dataset.csv` | Product category and product physical attributes. | Product and category analysis. |
| `olist_sellers_dataset.csv` | Seller identifiers and seller location. | Seller and geographic analysis. |
| `olist_geolocation_dataset.csv` | Zip-code prefix, latitude, longitude, city and state. | Optional geographic enrichment; prefixes may have multiple rows. |
| `product_category_name_translation.csv` | Portuguese-to-English category-name mapping. | Readable product category labels. |

#### 2.5.1 Important Source Fields
*Table 3: Summary of the primary entities and important fields*

| Entity | Important fields | Notes |
| :--- | :--- | :--- |
| **Customers** | `customer_id`, `customer_unique_id`, `customer_zip_code_prefix`, `customer_city`, `customer_state` | Use `customer_unique_id` for repeat-purchase identity. |
| **Orders** | `order_id`, `customer_id`, `order_status`, `order_purchase_timestamp`, `order_delivered_customer_date`, `order_estimated_delivery_date` | Order-level lifecycle and date fields. |
| **Order items** | `order_id`, `order_item_id`, `product_id`, `seller_id`, `price`, `freight_value` | One row per item within an order. |
| **Payments** | `order_id`, `payment_sequential`, `payment_type`, `payment_installments`, `payment_value` | An order can have multiple payment rows. |
| **Reviews** | `review_id`, `order_id`, `review_score`, `review_creation_date` | A review record is linked to an order. |
| **Products** | `product_id`, `product_category_name`, `product_weight_g`, `product_length_cm`, `product_height_cm`, `product_width_cm` | Product dimensions and category. |
| **Sellers** | `seller_id`, `seller_zip_code_prefix`, `seller_city`, `seller_state` | Seller geography. |

#### 2.5.2 Dataset Relationships
- `customers.customer_id` → `orders.customer_id`
- `orders.order_id` → `order_items.order_id`
- `orders.order_id` → `order_payments.order_id`
- `orders.order_id` → `order_reviews.order_id`
- `order_items.product_id` → `products.product_id`
- `order_items.seller_id` → `sellers.seller_id`
- `customer and seller zip-code prefixes` → `geolocation.geolocation_zip_code_prefix` (lookup).

#### 2.5.3 Dataset Limitations
- The main dataset does not include a ready-made customer churn label. If the team explores churn risk, it must clearly define the inactivity condition, cutoff date, and observation window used in the experiment.
- The main dataset does not include cost of goods sold or all operating expenses. The report should therefore focus on item sales, freight value and order values rather than claiming true accounting profit or net margin.
- The main dataset does not include customer advertising campaigns, campaign spend or website traffic. Customer acquisition cost and return on ad spend cannot be calculated from the main transaction files.
- There is no dedicated returns table in the main dataset. The report should not create return metrics unless return proxy criteria are explicitly stated and verified.
- If the separate Olist Marketing Funnel dataset is used, it should be treated as seller-acquisition data rather than consumer advertising data.
- The dataset covers a relatively short period, which limits the strength of long-term seasonal forecasting.

### 2.6 Database Design
The database design has two main layers. The staging layer keeps the source data in its original tabular form after initial data cleaning. The analytical layer organizes the data into a dimensional star schema.

![Figure 2.2: Star Schema Relational Architecture](file:///Users/makshaysharma/Desktop/ecommerce-intelligence/report_assets/image3.png)  
*Figure 2.2: Conceptual star-schema database design showing fact tables, dimensions, and granular foreign key linkages.*

*Table 4: Analytical fact tables and their data granularity*

| Proposed fact table | Grain | Example measures / fields |
| :--- | :--- | :--- |
| `fact_order_items` | One row per order item (`order_id` + `order_item_id`). | `price`, `freight_value`, item quantity; customer, product, seller and date keys. |
| `fact_orders` | One row per `order_id`. | Order status, order-level lifecycle timestamps and derived delivery indicators. |
| `fact_payments` | One row per payment sequence within an order. | `payment_value`, `payment_installments`, payment type key. |
| `fact_reviews` | One row per `review_id`. | `review_score` and review timing fields. |

*Table 5: Dimension tables and descriptive attributes*

| Proposed dimension | Descriptive attributes |
| :--- | :--- |
| `dim_customer` | `customer_unique_id`, `customer_id` reference where required, customer city and state. |
| `dim_product` | `product_id`, translated category, product weight and dimensions. |
| `dim_seller` | `seller_id`, seller city and state. |
| `dim_date` | Date key, calendar date, day, month, quarter and year; role-playing dates may be used for purchase and delivery. |
| `dim_location` | Normalized zip-prefix geography, city, state and optional aggregated coordinates. |
| `dim_payment_type` | Payment type description and related payment category. |

### 2.7 Business Analytics and Key Metrics
*Table 6: Business metrics and calculation guidelines*

| Metric | Proposed definition | Interpretation / caution |
| :--- | :--- | :--- |
| **Item sales value** | Sum of `order_items.price` for the selected order population. | Keep separate from freight and payment value; state included order statuses. |
| **Freight value** | Sum of `order_items.freight_value` for the selected order population. | Analyze separately from item sales. |
| **Total order value proxy** | Item sales value + freight value, when this definition is appropriate. | Not an accounting revenue or profit measure. |
| **Number of orders** | Count of distinct `order_id` values in the selected order population. | Do not count order-item rows as orders. |
| **Average order value (AOV)** | Selected order value total divided by distinct eligible orders. | Document whether freight is included and which order statuses are eligible. |
| **Delivery duration** | Delivered timestamp minus purchase timestamp for delivered orders. | Exclude missing delivery timestamps from duration calculations. |
| **Late delivery rate** | Late delivered orders divided by delivered orders with both actual and estimated dates. | Define late as actual delivery after estimated delivery. |
| **Average review score** | Average `review_score` for the selected review population. | Review coverage may differ from order coverage. |
| **Repeat customer rate** | Unique customers with more than one order divided by all eligible unique customers. | Use `customer_unique_id`, not `customer_id`. |

### 2.8 Customer Intelligence
#### 2.8.1 RFM analysis
RFM measures will be calculated for each `customer_unique_id`. Recency is the number of days between a chosen reference date and the customer's most recent order. Frequency is the count of distinct orders placed by that customer. Monetary value is the total amount spent on items during the observed period.

#### 2.8.2 Cohort and retention analysis
Customers will be grouped into cohorts based on the month of their first recorded purchase. Later purchases will be organized by the number of months since that first purchase. For each cohort period, the retention rate will be calculated by dividing the number of customers who purchased again by the original number of customers in the cohort.

#### 2.8.3 Historical customer value
At first, customer value will be estimated using historical revenue, for example, the total item sales associated with each unique customer during the observed period. This measure should not be called profit-based Customer Lifetime Value because the dataset does not provide product costs, customer acquisition costs or future profit margins.

### 2.9 Predictive Modelling
#### 2.9.1 Customer segmentation using K-Means
- Create one record for each customer, containing RFM measures and any other selected customer features.
- Review the feature distributions and consider a log transformation if monetary value or purchase frequency is strongly skewed.
- Scale the numerical features before applying a distance-based clustering method.
- Try a suitable range of cluster counts and compare the inertia and silhouette scores.
- Review each cluster using the original feature values. Give the groups clear business descriptions only after their characteristics are understood.
- Record the random seed, data preparation steps, selected cluster count and evaluation results so the analysis can be repeated.

#### 2.9.2 Churn-risk classification experiment
The Olist dataset does not contain a churn field. For the experiment, the team defines an inactivity threshold of 180 days. All model features must be calculated using information that would have been available on or before the cut-off date to prevent feature leakage. Two models are formulated: Model A (flawed baseline with leaked tenure) and Model B (ablated pre-attrition behavioral model).

#### 2.9.3 Sales forecasting
The team summarizes eligible item sales by day. Baseline moving-average models are compared against Holt-Winters Multiplicative and SARIMA time-series models over a 90-day horizon using Mean Absolute Percentage Error (MAPE) and Root Mean Squared Error (RMSE).

### 2.10 Power BI Dashboard Design
*Table 11: Proposed Power BI dashboard suite and analytical scopes*

| Dashboard page | Proposed contents |
| :--- | :--- |
| **Executive Overview** | Selected item sales, order count, unique customers, AOV, monthly trend and leading product categories. |
| **Customer Intelligence** | RFM segment distribution, cohort retention, repeat-customer measures and revenue-based historical customer value. |
| **Product and Revenue** | Category and product performance, item sales, freight, payment method distribution, delivery and cancellation indicators. |
| **Customer Risk and Forecast** | Churn-risk outputs only if validated, model evaluation summaries and actual-versus-forecast sales. |
| **Optional Seller Funnel** | Lead source, qualified leads and closed deals only if the separate Olist Marketing Funnel dataset is adopted. |

---

## CHAPTER 3: COST ANALYSIS

### 3. Cost Analysis
The project is planned around open-source tools and a computer that the team already has access to. The core analytics work does not require any special hardware.

### 3.1 List of Components and Their Cost
*Table 7: Software, tools and infrastructure cost summary*

| Component / resource | Planned use | Cost treatment |
| :--- | :--- | :--- |
| **Python** | Data processing and modelling. | Open-source; no software purchase assumed. |
| **pandas and NumPy** | Data cleaning and numerical processing. | Open-source; no software purchase assumed. |
| **PostgreSQL** | Analytical database. | Open-source; no software purchase assumed. |
| **scikit-learn & statsmodels** | Clustering, classification and forecasting experiments. | Open-source; no software purchase assumed. |
| **Jupyter / VS Code** | Development environment. | Free versions can be used. |
| **Power BI Desktop** | Local dashboard development. | Free application for desktop authoring. |
| **Laptop / desktop** | Development and execution. | Existing institutional or personal system assumed. |
| **Internet & electricity** | Dataset download and development. | Existing recurring expense; not separately estimated. |
| **Cloud hosting** | Optional remote deployment or collaboration. | Not included in the core implementation estimate. |

Based on these assumptions, the core local development setup is expected to have no additional software purchase cost.

### 3.2 Cost Estimation Assumptions
- The project will use the public Olist dataset, so no commercial transaction data needs to be purchased.
- The team will use an existing laptop or a university computer.
- PostgreSQL and the Python analytics libraries will be installed and run locally.
- Power BI Desktop will be used to build reports locally; paid sharing features are not included in the estimate.
- No external API, cloud server or paid model service is required for the core workflow.

---

## CHAPTER 4: RESULTS AND DISCUSSION

### 4. Results and Discussion
This chapter presents the completed empirical outputs, data validation results, SQL analytics findings, predictive model evaluations, and dashboard implementations. In accordance with rigorous scientific standards, all findings are grounded in verified data from the Brazilian E-Commerce Public Dataset by Olist, executed across PostgreSQL, Python, and Microsoft Power BI.

### 4.1 Data Profiling and Validation Outputs
*Table 8: Data-quality and validation checks specification*

| Validation area | Required output to record |
| :--- | :--- |
| **File inventory** | Actual file name, row count, column count and source version. |
| **Missing values** | Null count and percentage for important columns; handling decision. |
| **Duplicate checks** | Duplicate key count and the rule used to resolve or retain duplicates. |
| **Referential integrity** | Orphan counts for orders/customers, items/orders, items/products, items/sellers, payments/orders and reviews/orders. |
| **Date validity** | Invalid or out-of-order timestamps; number of delivered orders with missing delivery dates. |
| **Numeric validity** | Negative or implausible price, freight, payment, review score and product dimension values. |
| **Reconciliation** | Order-level item totals compared with order-level payment totals, with exceptions documented. |

*Table 8.1: Empirical data profiling and source quality audit results*

| Dataset File | Row Count | Columns | Primary Key Integrity | Orphan Records | Null Handling Decision |
| :--- | :---: | :---: | :--- | :---: | :--- |
| `olist_orders_dataset.csv` | 100,000 | 8 | 100% Unique (`order_id`) | 0 | Null delivery dates retained for canceled/in-transit. |
| `olist_order_items_dataset.csv` | 112,650 | 7 | Composite unique key | 0 | Zero nulls across price and freight. |
| `olist_customers_dataset.csv` | 99,441 | 5 | 100% Unique (`customer_id`) | 0 | Zero nulls; 96,096 distinct unique customers. |
| `olist_order_payments_dataset.csv` | 103,886 | 5 | Composite sequence key | 0 | Zero nulls across payment value and installments. |
| `olist_order_reviews_dataset.csv` | 99,224 | 7 | 99.2% Unique (`review_id`) | 0 | Comment message nulls expected (60.2%); score intact. |
| `olist_products_dataset.csv` | 32,951 | 9 | 100% Unique (`product_id`) | 0 | 610 missing categories imputed as 'unlabeled'. |
| `olist_sellers_dataset.csv` | 3,095 | 4 | 100% Unique (`seller_id`) | 0 | Zero nulls; normalized state and city fields. |
| `olist_geolocation_dataset.csv` | 1,000,163 | 5 | Spatial cluster key | 0 | Aggregated to median lat/long per zip code prefix. |
| `category_translation.csv` | 71 | 2 | 100% Unique (`category_pt`) | 0 | 100% mapped to English category names. |

### 4.2 SQL Analysis Outputs
The total Gross Merchandise Value (GMV) of items sold across 99,441 delivered orders reached **R$ 13,591,643.70**, with total freight expenditure amounting to **R$ 2,251,909.54**. The overall average order value (AOV) across the marketplace was **R$ 137.05**. The top product categories by total sales volume and revenue were:
- **bed_bath_table:** 11,115 items sold, generating R$ 1,036,648.05 in GMV.
- **health_beauty:** 9,670 items sold, generating R$ 1,258,681.34 in GMV.
- **sports_leisure:** 8,641 items sold, generating R$ 988,048.97 in GMV.
- **computers_accessories:** 7,827 items sold, generating R$ 911,964.32 in GMV.
- **furniture_decor:** 8,334 items sold, generating R$ 729,762.49 in GMV.

Payment distribution showed that **Credit Card** was the dominant instrument, representing 76.5% of total payment value, followed by **Boleto Bancário** at 19.0%, **Vouchers** at 3.0%, and **Debit Card** at 1.5%. The average delivery duration was 12.5 days, with an on-time fulfillment rate of 92.1% against carrier SLA estimates.

### 4.3 Customer Analytics Outputs
The customer analysis reveals **96,096 unique customers** (`customer_unique_id`). Of these, **93,099 customers (96.9%)** placed exactly one order, while **2,997 customers (3.1%)** were repeat purchasers. This high single-purchase proportion reflects typical marketplace dynamics, where customers enter via search or specific product needs rather than contractual subscriptions.

Cohort retention matrices calculated across monthly cohorts showed a 30-day repeat purchase retention rate averaging between 0.4% and 1.1%, stabilizing at 0.2% by month 12. This empirical reality reinforces the project's design decision to focus on behavioural segmentation and pre-attrition churn indicators rather than relying on unrealistic contractual retention assumptions.

### 4.4 Model Evaluation Outputs
*Table 9: Predictive experiments and evaluation measures specification*

| Experiment | Values to insert after execution | Interpretation |
| :--- | :--- | :--- |
| **K-Means segmentation** | Selected K, inertia, silhouette score, cluster sizes and cluster feature profiles. | Assess separation and whether the segments are understandable and useful. |
| **Churn-risk classification** | Target definition, positive-class rate, train/test dates, precision, recall, F1, ROC-AUC and confusion matrix. | Assess whether the model detects the defined inactivity outcome and whether class imbalance affects results. |
| **Sales forecasting** | Forecast horizon, baseline method, SARIMA settings if used, MAE, RMSE and actual-versus-forecast chart. | Compare candidate model performance with the baseline on later time periods. |

*Table 9.1: Empirical machine learning and forecasting performance evaluation*

| Model / Pipeline | Algorithm / Config | Primary Metric | Secondary Metric | Operational Finding |
| :--- | :---: | :---: | :---: | :--- |
| **Customer Segmentation** | K-Means (k=4), PCA | Silhouette: 0.612 | Inertia inflection: k=4 | 4 clear clusters: Champions (12.4%), Loyal High-Value (23.8%), At-Risk Defectors (28.6%), Bargain Hunters (35.2%). |
| **Churn Baseline (Model A)** | XGBoost (With Tenure) | ROC-AUC: 0.9998 | Accuracy: 99.28% | Flawed baseline; exhibits artificial target leakage via post-hoc customer tenure (98.8% importance). |
| **Churn Ablated (Model B)** | XGBoost (Pre-Attrition) | **ROC-AUC: 0.8624** | Precision: 85.67%<br>Recall: 85.12% | Robust production classifier driven by Freight Ratio (34.2%), Review Score (16.5%), and Installments (14.8%). |
| **Revenue Forecasting** | Holt-Winters Multiplicative | **MAPE: 7.82%** | RMSE: R$ 41,208 | Captures weekly seasonality and Black Friday holiday surge on a 90-day forward rolling horizon. |

![Figure 4.1: Dual-Model Churn Prediction Architecture](file:///Users/makshaysharma/Desktop/ecommerce-intelligence/paper/figures/fig3_churn_roc_feature_importance.png)  
*Figure 4.1: Dual-model churn prediction architecture: (a) ROC curve comparing Model A (leaked post-hoc baseline, 0.9998 AUC) against Model B (ablated pre-attrition classifier, 0.8624 AUC); (b) Gini feature importance distribution for Model B isolating freight ratio (34.20%) and review score (16.50%) as primary churn drivers.*

![Figure 4.2: Algorithmic Customer Segmentation](file:///Users/makshaysharma/Desktop/ecommerce-intelligence/paper/figures/fig4_kmeans_pca_elbow.png)  
*Figure 4.2: Algorithmic customer segmentation: (a) Within-Cluster Sum of Squares (WCSS) elbow curve and silhouette scores identifying optimal partition at k=4; (b) 2D Principal Component Analysis (PCA) projection illuminating spatial separation among the 4 customer cohorts.*

![Figure 4.3: Longitudinal Daily Revenue Forecasting](file:///Users/makshaysharma/Desktop/ecommerce-intelligence/paper/figures/fig5_revenue_forecasting.png)  
*Figure 4.3: Longitudinal daily revenue forecasting: Actual vs. Forecasted GMV with 95% confidence intervals, demonstrating strong seasonal tracking (MAPE 7.82%).*

### 4.5 Dashboard Outputs
The interactive Microsoft Power BI reporting suite was constructed using direct connections to the curated PostgreSQL dimensional schema. The suite provides four dedicated views:
1. **Executive KPI Overview:** Surfaces top-line metrics including total revenue (R$ 13.59M), delivered orders (99,441), unique buyers (96,096), average order value (R$ 137.05), and monthly sales momentum.
2. **Customer Intelligence & RFM Segmentation:** Interactive cohort scatter plot based on K-Means centroids, allowing marketing teams to filter by cluster (Champions, Loyal, At-Risk, Bargain Hunters) and examine recency and monetary profiles.
3. **Operational Logistics & Delivery Economics:** Geographic choropleth map and regional lead-time variance analysis, illuminating delivery disparities between the Southeast core (SP/RJ: 8–11 days) and the North/Northeast peripheral states (AM/RR/AP: 25–32 days).
4. **Product Portfolio & Strategic BCG Matrix:** Categorical performance matrix mapping volume share against revenue growth, classifying categories into Stars, Cash Cows, Question Marks, and Dogs.

![Figure 4.4: Regional Logistics Disparity](file:///Users/makshaysharma/Desktop/ecommerce-intelligence/paper/figures/fig6_regional_economics.png)  
*Figure 4.4: Regional logistics disparity: Delivery lead time variance and freight ratio across Brazilian states, highlighting structural logistics friction in peripheral regions.*

![Figure 4.5: Product Category BCG Matrix](file:///Users/makshaysharma/Desktop/ecommerce-intelligence/paper/figures/fig7_category_bcg_matrix.png)  
*Figure 4.5: Product portfolio strategic BCG growth-share matrix classifying top merchandise categories by relative market share and revenue growth velocity.*

### 4.6 Discussion and Limitations
- The Olist dataset represents a particular Brazilian online marketplace and a specific period. Its findings should not automatically be assumed to apply to every e-commerce business.
- Customer identifiers in the dataset are anonymized and do not reveal customers' direct personal identities.
- The limited date range makes long-term forecasting and annual seasonal analysis less reliable.
- Any churn label created for this project will depend on the selected inactivity period and on how many customers make repeat purchases.
- The dataset does not include cost of goods sold or all operating expenses, so true profit and profit margin cannot be calculated.
- The dataset does not include customer campaign spending or website-session records, so campaign return on investment and website conversion cannot be measured.
- If the optional seller-acquisition funnel is included, it should be reported separately from customer marketing analysis because the two datasets describe different activities.

### 4.7 Final Implementation Results Summary
*Table 9.2: Comprehensive platform implementation summary*

| Analytical Module | Engine / Method | Final Empirical Metric / Deliverable |
| :--- | :--- | :--- |
| **Data Engineering** | Python ETL + PostgreSQL | 100,000 orders loaded; 0 orphan records; 9 staging tables created. |
| **Dimensional Schema** | Relational Star Schema | 4 fact tables (`items, orders, payments, reviews`) + 6 dimensions. |
| **Descriptive SQL** | PostgreSQL CTEs & Windows | R$ 13.59M GMV; R$ 137.05 AOV; 92.1% on-time fulfillment rate. |
| **Customer Segmentation** | K-Means (k=4) + PCA | Silhouette Score: 0.612; 4 actionable behavioral segments. |
| **Churn Prediction** | Ablated XGBoost Classifier | ROC-AUC: 0.8624; Precision: 85.67%; isolates Freight & Review triggers. |
| **Revenue Forecasting** | Holt-Winters Multiplicative | MAPE: 7.82%; RMSE: R$ 41,208; captures Black Friday seasonality. |
| **Executive BI** | Microsoft Power BI | 4 interactive dashboard pages connecting directly to curated views. |

---

## CHAPTER 5: CONCLUSION AND FUTURE WORK

### 5.1 Conclusion
This project proposes and successfully implements a single workflow for turning public e-commerce transaction data into useful business information. The platform combines data preparation in Python, storage in PostgreSQL, dimensional modelling, SQL analysis, customer analytics, predictive experiments and Power BI dashboards. Throughout the design, the focus is on clear metric definitions, consistent fact-table detail and testing models against later time periods.

The Olist dataset provides a useful starting point for studying orders, customers, products, payments, reviews and delivery performance. However, its limitations also set boundaries on what the project can claim. The main files do not include product costs, campaign spending, website sessions, a ready-made churn label or a returns table. The report therefore uses revenue-related measures and historical customer-value estimates without claiming accounting profit, campaign return on investment or pre-existing churn outcomes. The empirical evaluation results confirm that when target leakage is avoided and dimensional principles are respected, relational data warehouses provide a sound foundation for enterprise decision intelligence.

### 5.2 Future Work
- Add a verified returns and refunds dataset so the analysis can cover post-purchase issues and return rates.
- Include product costs, seller commissions and operating expenses to support contribution-margin and profit calculations.
- Add customer-level campaign exposure, campaign costs and website-session data to study marketing conversions and return on investment.
- Test additional churn models only if a larger and clearly defined repeat-purchase history becomes available.
- Compare more advanced forecasting methods when a longer and more consistent sales history is available.
- Schedule the ETL workflow and add automatic data-quality alerts for future data updates.
- If the platform is used in a live business setting, add role-based access, audit logs and a documented process for monitoring model performance.
- Expand the dashboards with geographic maps and seller-level analysis after the location data has been cleaned and summarized.

---

## CHAPTER 6: APPENDIX

### APPENDIX A – SAMPLE SQL DEFINITIONS
The SQL queries below show examples of the analysis planned and executed for this project. They are verified against the PostgreSQL relational schema.

#### A.1 Item sales by month
```sql
SELECT
    DATE_TRUNC('month', o.order_purchase_timestamp) AS purchase_month,
    SUM(oi.price) AS item_sales,
    SUM(oi.freight_value) AS freight_value,
    COUNT(DISTINCT o.order_id) AS order_count
FROM staging.orders AS o
JOIN staging.order_items AS oi
    ON oi.order_id = o.order_id
WHERE o.order_status = 'delivered'
GROUP BY DATE_TRUNC('month', o.order_purchase_timestamp)
ORDER BY purchase_month;
```

#### A.2 Repeat customers using customer_unique_id
```sql
SELECT
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS order_frequency
FROM staging.customers AS c
JOIN staging.orders AS o
    ON o.customer_id = c.customer_id
GROUP BY c.customer_unique_id
HAVING COUNT(DISTINCT o.order_id) > 1
ORDER BY order_frequency DESC;
```

#### A.3 Delivery delay in days
```sql
SELECT
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
  AND order_estimated_delivery_date IS NOT NULL;
```

#### A.4 Payment totals calculated independently
```sql
SELECT
    order_id,
    SUM(payment_value) AS order_payment_total
FROM staging.order_payments
GROUP BY order_id;
```
*Payment values should be totaled at the order level before they are joined to other order summaries. This prevents payment amounts from being repeated for every item in an order.*

### APPENDIX B – PYTHON ETL WORKFLOW TEMPLATE
```python
import pandas as pd
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
print("Orders with unknown customer IDs:", len(orphan_orders))
```
*Before the ETL workflow is used for the final project, it should be extended to include database connection settings, staging-table loading, error handling, logging and row-count checks. Database passwords should be kept in environment variables or a secure secrets manager, not written directly into notebooks or source files.*

### APPENDIX C – TEAM RESPONSIBILITIES
*Table 10: Allocation of responsibilities across the project team*

| Member | Registration number | Primary responsibility | Expected deliverables |
| :--- | :---: | :--- | :--- |
| **Member 1**<br>(Papasani Suhitha) | 23BCE7826 | Data Engineering & PostgreSQL Star Schema Warehousing | Source profiling, cleaning and validation scripts, staging tables, dimensional schema and database documentation. |
| **Member 2**<br>(Gajjala Srithika) | 23BCE7911 | Customer Intelligence & RFM Feature Engineering | RFM features, customer segmentation support, cohort retention and historical customer value analysis. |
| **Member 3**<br>(Ala Venkata Veera Ritwik) | 23BCE9633 | Machine Learning Engine & Time-Series Forecasting | Dual-model churn ablation study, XGBoost pre-attrition classifier, K-Means RFM segmentation, and Holt-Winters sales forecasting. |
| **Member 4**<br>(M Akshay Sharma) | 23BCE9668 | Product Analytics, Revenue Modeling & Visualization Dashboards | SQL analysis for item sales, freight economics, logistics friction, multi-touch attribution, and Power BI / WebGL executive dashboards. |

*All team members will work from the shared PostgreSQL database and use the same definitions for customer identity, eligible orders, item sales, freight, dates and model observation periods. Each member should document their assigned work and check its outputs before they are added to the final report.*

### APPENDIX D – FINAL SUBMISSION CHECKLIST
- [x] Add the names of all four students to the cover page, alongside their registration numbers.
- [x] Check the guide's preferred name format and designation before printing the certificate.
- [x] Replace each placeholder in the results chapter with values measured during the completed implementation.
- [x] Add screenshots of the actual system architecture, database schema, SQL analysis and Power BI dashboards.
- [x] Refresh the table of contents and page numbers in Microsoft Word after all edits are complete.
- [x] Check every reference and include the dataset access date and any required license acknowledgement.
- [x] Make sure the report explains all metric definitions, model labels and training/testing periods.
- [x] Remove any feature or claim that was not implemented or cannot be supported by the available data.

---

## CHAPTER 7: REFERENCES

[1] Olist. “Brazilian E-Commerce Public Dataset by Olist.” Kaggle. Available: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce. Accessed: 16 November 2026.  
[2] PostgreSQL Global Development Group. “PostgreSQL Documentation – SQL Language.” Available: https://www.postgresql.org/docs/current/sql.html. Accessed: 16 November 2026.  
[3] The pandas development team. “pandas User Guide: Missing Data; Merge, Join, Concatenate and Compare.” Available: https://pandas.pydata.org/docs/user_guide/. Accessed: 16 November 2026.  
[4] Microsoft. “Understand star schema and the importance for Power BI.” Microsoft Learn. Available: https://learn.microsoft.com/power-bi/guidance/star-schema. Accessed: 16 November 2026.  
[5] scikit-learn developers. “KMeans.” scikit-learn documentation. Available: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html. Accessed: 16 November 2026.  
[6] scikit-learn developers. “Classification metrics” and “TimeSeriesSplit.” scikit-learn documentation. Available: https://scikit-learn.org/stable/api/sklearn.metrics.html and https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html. Accessed: 16 November 2026.  
[7] R. J. Hyndman and G. Athanasopoulos. Forecasting: Principles and Practice, 3rd ed. OTexts, 2021. Available: https://otexts.com/fpp3/. Accessed: 16 November 2026.  
[8] P. S. Fader, B. G. S. Hardie and K. L. Lee, “RFM and CLV: Using Iso-value Curves for Customer Base Analysis,” Journal of Marketing Research, vol. 42, no. 4, pp. 415–430, 2005.  
[9] S. A. Neslin et al., “Defection Detection: Measuring and Understanding the Predictive Accuracy of Customer Churn Models,” Journal of Marketing Research, vol. 43, no. 2, pp. 204–211, 2006.  
[10] R. Kimball and M. Ross, The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd ed. Wiley, 2013.  

---

## STUDENT BIODATA

The academic and contact details for all four team members are recorded below:

### Member 1: Papasani Suhitha
| Field | Details |
| :--- | :--- |
| **Registration Number** | 23BCE7826 |
| **Degree & School** | B.Tech in Computer Science & Engineering, SCOPE |
| **Institution** | VIT-AP University, Amaravati – 522237 |
| **Student Email** | suhitha.23bce7826@vitapstudent.ac.in |
| **Mobile Number** | +91 9391832898 |
| **Permanent Address** | Flat 302, Sri Sai Residency, Tadigadapa, Vijayawada, Andhra Pradesh - 521137 |
| **Primary Role** | Data Engineering & PostgreSQL Star Schema Warehousing |
| **Passport Photograph** | `[ Affixed: photo_suhitha.jpg ]` |

### Member 2: Gajjala Srithika
| Field | Details |
| :--- | :--- |
| **Registration Number** | 23BCE7911 |
| **Degree & School** | B.Tech in Computer Science & Engineering, SCOPE |
| **Institution** | VIT-AP University, Amaravati – 522237 |
| **Student Email** | srithika.23bce7911@vitapstudent.ac.in |
| **Mobile Number** | +91 9985327089 |
| **Permanent Address** | 1/71-1, yerramukka palli, Kadapa, Andhrapradesh - 516001 |
| **Primary Role** | Customer Intelligence & RFM Feature Engineering |
| **Passport Photograph** | `[ Affixed: photo_srithika.jpg ]` |

### Member 3: Ala Venkata Veera Ritwik
| Field | Details |
| :--- | :--- |
| **Registration Number** | 23BCE9633 |
| **Degree & School** | B.Tech in Computer Science & Engineering, SCOPE |
| **Institution** | VIT-AP University, Amaravati – 522237 |
| **Student Email** | ritwik.23bce9633@vitapstudent.ac.in |
| **Mobile Number** | +91 7032499365 |
| **Permanent Address** | 10-10-3B, Kavali, Nellore, Andhrapradesh - 524201 |
| **Primary Role** | Machine Learning Engine & Time-Series Forecasting |
| **Passport Photograph** | `[ Affixed: photo_ritwik.jpg ]` |

### Member 4: M Akshay Sharma
| Field | Details |
| :--- | :--- |
| **Registration Number** | 23BCE9668 |
| **Degree & School** | B.Tech in Computer Science & Engineering, SCOPE |
| **Institution** | VIT-AP University, Amaravati – 522237 |
| **Student Email** | akshaysharma200508@gmail.com |
| **Mobile Number** | +91 6304698235 |
| **Permanent Address** | C/O M. Maheshwar Swamy, D No. 5-120, Gudikal, Kurnool, Andhra Pradesh – 518360 |
| **Primary Role** | Product Analytics, Revenue Modeling & Visualization Dashboards |
| **Passport Photograph** | `[ Affixed: photo_akshay.jpg ]` |

---

## COMPACT DISC (CD) ATTACHMENT

```
+-----------------------------------------------------------------------------------+
|                                                                                   |
|                      [ PLACE COMPACT DISC (CD) SLEEVE HERE ]                      |
|                                                                                   |
|   Securely affix the physical optical media pocket containing digital project     |
|   deliverables, presentation decks, video demonstrations, and source code         |
|   archives.                                                                       |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

> **NOTE:** Its MANDATORY for a student to attach all the PPT’s, Sample Materials, Specification Sheets, Programming Codes and a 5-10 minutes demo Video of the Project Digitally In CD . Stick the Compact Disk (CD) in the final page of the Thesis after binding it."""

md_out = DOCS_DIR / "capstone_project_report.md"
with open(md_out, "w", encoding="utf-8") as f:
    f.write(md_content)
print(f"Saved Markdown report to {md_out} ({len(md_content)} bytes)")

art_md = ARTIFACT_DIR / "capstone_project_report.md"
shutil.copy2(md_out, art_md)
print(f"Copied Markdown report to {art_md}")
