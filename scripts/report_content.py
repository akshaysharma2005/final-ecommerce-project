# -*- coding: utf-8 -*-
"""
report_content.py
Structured content and metadata for VIT-AP University Capstone Project Report.
Project: E-Commerce Business Intelligence & Predictive Analytics Platform
Session: FALL 2026-27
"""

STUDENTS = [
    {
        "sno": "1",
        "name": "Gajjala Srithika",
        "reg": "23BCE7911",
        "degree": "B.Tech in Computer Science and Engineering",
        "school": "School of Computer Science and Engineering (SCOPE)",
        "email": "Srithika.23bce7911@vitapstudent.ac.in",
        "mobile": "+91 9985327089",
        "address": "Plot 42, H.No. 4-12/1, Revenue Colony, Vijayawada, Andhra Pradesh - 520008",
        "role": "Customer Intelligence & RFM Feature Engineering",
        "deliverables": "RFM metric calculation, customer lifetime value analysis, cohort retention tables, and customer feature store design."
    },
    {
        "sno": "2",
        "name": "Papasani Suhitha",
        "reg": "23BCE7826",
        "degree": "B.Tech in Computer Science and Engineering",
        "school": "School of Computer Science and Engineering (SCOPE)",
        "email": "Suhitha.23bce7826@vitapstudent.ac.in",
        "mobile": "+91 9391832898",
        "address": "Flat 302, Sri Sai Residency, Tadigadapa, Vijayawada, Andhra Pradesh - 521137",
        "role": "Data Engineering & PostgreSQL Star Schema Warehousing",
        "deliverables": "Source profiling, validation scripts, staging tables, 13-table dimensional star schema, index optimization, and materialized views."
    },
    {
        "sno": "3",
        "name": "Ala Venkata Veera Ritwik",
        "reg": "23BCE9633",
        "degree": "B.Tech in Computer Science and Engineering",
        "school": "School of Computer Science and Engineering (SCOPE)",
        "email": "ritwik.23bce9633@vitapstudent.ac.in",
        "mobile": "+91 7032499365",
        "address": "D.No. 7-19, Main Road, Kankipadu, Krishna District, Andhra Pradesh - 521151",
        "role": "Machine Learning Engine & Time-Series Forecasting",
        "deliverables": "Dual-model churn ablation study, XGBoost pre-attrition classifier, K-Means RFM segmentation, and Holt-Winters sales forecasting."
    },
    {
        "sno": "4",
        "name": "Akshay Sharma",
        "reg": "23BCE9668",
        "degree": "B.Tech in Computer Science and Engineering",
        "school": "School of Computer Science and Engineering (SCOPE)",
        "email": "akshaysharma200508@gmail.com",
        "mobile": "+91 6304698235",
        "address": "Flat 504, Fortune Heights, Tadepalli, Guntur District, Andhra Pradesh - 522501",
        "role": "Product Analytics, Revenue Modeling & Visualization Dashboards",
        "deliverables": "SQL analysis for item sales, freight economics, logistics friction, multi-touch attribution, and Power BI / WebGL executive dashboards."
    }
]

GUIDE_NAME = "Prof. N. Lakshmipathi Anantha"
GUIDE_DESIGNATION = "Faculty Project Guide"
HOD_DESIGNATION = "HoD, Department of Computer Science and Engineering"
DEAN_NAME = "Dr. S. Sudhakar Ilango"
DEAN_DESIGNATION = "Dean, School of Computer Science and Engineering"
ASSOC_DEAN_NAME = "Dr. Saroj Kumar Panigrahy"
ASSOC_DEAN_DESIGNATION = "Associate Dean, School of Computer Science and Engineering"
CHANCELLOR_NAME = "Dr. G. Viswanathan"
CHANCELLOR_DESIGNATION = "Chancellor, VIT-AP University"
VICE_CHANCELLOR_NAME = "Dr. P. Arulmozhivarman"
VICE_CHANCELLOR_DESIGNATION = "Vice-Chancellor, VIT-AP University"

INSTITUTION_NAME = "VIT-AP UNIVERSITY"
SCHOOL_NAME = "SCHOOL OF COMPUTER SCIENCE AND ENGINEERING"
LOCATION = "AMARAVATI - 522237, ANDHRA PRADESH"
SUBMISSION_DATE = "NOVEMBER 2026"

PROJECT_TITLE = "E-COMMERCE BUSINESS INTELLIGENCE & PREDICTIVE ANALYTICS PLATFORM"
PROJECT_DEGREE = "BACHELOR OF TECHNOLOGY IN COMPUTER SCIENCE & ENGINEERING"

CERTIFICATE_TEXT = (
    'This is to certify that the Capstone Project work titled "E-COMMERCE BUSINESS INTELLIGENCE & '
    'PREDICTIVE ANALYTICS PLATFORM" that is being submitted by GAJJALA SRITHIKA (23BCE7911), '
    'PAPASANI SUHITHA (23BCE7826), ALA VENKATA VEERA RITWIK (23BCE9633), and AKSHAY SHARMA (23BCE9668) '
    'is in partial fulfillment of the requirements for the award of Bachelor of Technology, is a record '
    'of bonafide work done under my guidance. The contents of this Project work, in full or in parts, '
    'have neither been taken from any other source nor have been submitted to any other Institute or '
    'University for award of any degree or diploma and the same is certified.'
)

ACKNOWLEDGEMENT_PARAS = [
    "We would like to express our sincere gratitude to VIT-AP University, Amaravati, Andhra Pradesh, for providing us with the opportunity, infrastructure, and academic environment to undertake and successfully complete our Capstone Project.",
    "We are deeply grateful to Dr. G. Viswanathan, Chancellor, VIT-AP University, and Dr. P. Arulmozhivarman, Vice-Chancellor, VIT-AP University, for their visionary leadership, encouragement, and commitment to providing quality education and fostering innovation and research.",
    "We express our sincere thanks to Dr. S. Sudhakar Ilango, Dean, SCOPE, Dr. Saroj Kumar Panigrahy, Associate Dean, SCOPE, and the Head of the Department of Computer Science and Engineering for the continuous encouragement, academic support, and facilities provided throughout the project.",
    "We are profoundly grateful to Prof. N. Lakshmipathi Anantha, our Project Supervisor/Guide, for the invaluable guidance, constant support, constructive feedback, and encouragement extended to us at every stage of this project. Their expertise and suggestions have been instrumental in the successful completion of our work.",
    "We would also like to extend our sincere appreciation to all the faculty members and staff of the School of Computer Science and Engineering for their cooperation, valuable suggestions, and support during the course of this project.",
    "Finally, we express our heartfelt gratitude to our parents, family members, and friends for their constant encouragement, patience, and support throughout our academic journey."
]

ABSTRACT_TEXT = (
    "Modern multi-vendor e-commerce retail networks operate over distributed relational transactional systems "
    "that capture millions of discrete events including cart additions, payments, carrier logistics, and customer evaluations. "
    "However, operating analytical intelligence and predictive workflows on transactional 3NF databases introduces severe "
    "operational friction: analytical joins degrade transactional throughput, customer churn models frequently suffer from "
    "subtle temporal target leakage, and static reporting fails to account for logistics bottlenecks and macroeconomic fluctuations. "
    "To address these challenges, this capstone project presents an end-to-end E-Commerce Business Intelligence & Predictive "
    "Analytics Platform evaluated on approximately 100,000 real-world customer orders from the Brazilian e-commerce market (Olist dataset).\n\n"
    "We engineered a 13-table star schema relational data warehouse in PostgreSQL 15, introducing surrogate integer keys and "
    "targeted B-tree indices that accelerated multidimensional analytical reporting queries by 4.3x to 9.2x compared to normalized "
    "transactional joins. In the predictive modeling layer, we conducted an empirical ablation study demonstrating that naive churn "
    "models achieve a deceptive 99.28% accuracy through target leakage--where post-observation customer tenure trivially reveals "
    "single-purchase status. By ablating leaked tenure, our production-grade pre-attrition XGBoost classifier achieved an honest "
    "84.18% accuracy (0.8624 ROC-AUC), identifying freight ratio (24.2% importance) and review sentiment (16.5% importance) as "
    "primary churn drivers. Furthermore, we implemented unsupervised RFM customer segmentation via K-Means (k=4, silhouette score "
    "0.612) and longitudinal revenue forecasting via Holt-Winters multiplicative seasonal smoothing (MAPE of 4.21%). Finally, the "
    "platform integrates logistics geospatial friction analysis using Haversine distance, multi-touch marketing attribution, and "
    "interactive business intelligence dashboards in Power BI and WebGL. This report documents the system architecture, mathematical "
    "formulations, engineering decisions, and empirical results."
)

CD_NOTE_TEXT = (
    "NOTE: Its MANDATORY for a student to attach all the PPT's, Sample Materials, Specification Sheets, "
    "Programming Codes and a 5-10 minutes demo Video of the Project Digitally In CD . Stick the Compact Disk (CD) "
    "in the final page of the Thesis after binding it."
)
