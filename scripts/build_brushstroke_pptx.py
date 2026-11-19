#!/usr/bin/env python3
"""
build_brushstroke_pptx.py
Builds the 12-slide Microsoft PowerPoint Presentation (.pptx)
in the exact artistic aesthetic requested by the user:
- Blue oil paint brushstroke splash & gold wireframe rectangle theme
- Clean pure white background (#FFFFFF)
- Delicate gold (#C5A880) and slate wireframe geometric accents
- Section header badge with blue paint dab
- Minimalist circular process badges (1, 2, 3, 4)
- High-contrast figures, formulas, student photo cards, and full speaker notes
"""

import os
from pathlib import Path
import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

WORKSPACE = Path("/Users/makshaysharma/Desktop/ecommerce-intelligence")
DOCS_DIR = WORKSPACE / "docs"
FIG_DIR = WORKSPACE / "docs" / "figures"
ASSETS_DIR = WORKSPACE / "report_assets"
ARTIFACT_DIR = Path("/Users/makshaysharma/.gemini/antigravity/brain/2ff68dc2-9f13-45a4-b203-0adb4a579794")

# Artistic Palette (Blue Oil Paint & Gold Wireframe Theme)
WHITE = RGBColor(255, 255, 255)
OFF_WHITE = RGBColor(248, 250, 252)          # #F8FAFC
CARD_BORDER = RGBColor(226, 232, 240)        # #E2E8F0 - Clean slate border
GOLD_BORDER = RGBColor(197, 168, 128)        # #C5A880 - Delicate metallic gold frame
GOLD_ACCENT = RGBColor(212, 175, 55)         # #D4AF37 - Rich gold
TEXT_BLACK = RGBColor(15, 23, 42)            # #0F172A - Headline black
TEXT_MUTED = RGBColor(100, 116, 139)         # #64748B - Body secondary
TEXT_LIGHT = RGBColor(255, 255, 255)
ROYAL_BLUE = RGBColor(30, 58, 138)           # #1E3A8A - Deep Prussian / Navy Blue
VIBRANT_BLUE = RGBColor(37, 99, 235)         # #2563EB - Vibrant Royal Blue
LIGHT_BLUE_BG = RGBColor(239, 246, 255)      # #EFF6FF - Subtle blue tint
ACCENT_AMBER = RGBColor(217, 119, 6)         # #D97706
ACCENT_GREEN = RGBColor(16, 185, 129)        # #10B981
CRIMSON = RGBColor(185, 28, 28)              # #B91C1C

SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

HERO_BRUSH_PATH = ASSETS_DIR / "brushstroke_hero_transparent.png"
SMALL_BRUSH_PATH = ASSETS_DIR / "brushstroke_small_badge.png"


def create_deck():
    prs = pptx.Presentation()
    prs.slide_width = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT
    blank_layout = prs.slide_layouts[6]

    # -------------------------------------------------------------
    # HELPER DESIGN FUNCTIONS
    # -------------------------------------------------------------
    def set_white_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_WIDTH, SLIDE_HEIGHT)
        bg.fill.solid()
        bg.fill.fore_color.rgb = WHITE
        bg.line.fill.background()
        return bg

    def add_gold_wireframe(slide, left, top, width, height, border_color=GOLD_BORDER, border_width=1.2):
        wire = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        wire.fill.background()
        wire.line.color.rgb = border_color
        wire.line.width = Pt(border_width)
        return wire

    def add_top_bar(slide):
        tbox = slide.shapes.add_textbox(Inches(0.8), Inches(0.28), Inches(11.7), Inches(0.32))
        p = tbox.text_frame.paragraphs[0]
        r1 = p.add_run()
        r1.text = "VIT-AP UNIVERSITY  •  SCHOOL OF COMPUTER SCIENCE AND ENGINEERING (SCOPE)"
        r1.font.name = "Arial"
        r1.font.size = Pt(9.5)
        r1.font.bold = True
        r1.font.color.rgb = ROYAL_BLUE

        r2 = p.add_run()
        r2.text = "   |   Faculty Guide: Prof. N. Lakshmipathi Anantha   |   Fall 2026-27"
        r2.font.name = "Arial"
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = TEXT_MUTED

    def add_header(slide, tag_text, title, subtitle):
        add_top_bar(slide)

        # Small brushstroke dab in top left
        if SMALL_BRUSH_PATH.exists():
            slide.shapes.add_picture(str(SMALL_BRUSH_PATH), Inches(0.8), Inches(0.68), width=Inches(0.85), height=Inches(0.48))

        # Tag text next to dab (spaced uppercase)
        tag_box = slide.shapes.add_textbox(Inches(1.72), Inches(0.72), Inches(7.5), Inches(0.3))
        tp = tag_box.text_frame.paragraphs[0]
        tr = tp.add_run()
        tr.text = tag_text.upper()
        tr.font.name = "Arial"
        tr.font.size = Pt(9.5)
        tr.font.bold = True
        tr.font.color.rgb = ROYAL_BLUE

        # Slide Title & Subtitle
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.15), Inches(11.7), Inches(0.65))
        p = t_box.text_frame.paragraphs[0]
        r = p.add_run()
        r.text = title
        r.font.name = "Arial"
        r.font.size = Pt(21)
        r.font.bold = True
        r.font.color.rgb = TEXT_BLACK

        if subtitle:
            p2 = t_box.text_frame.add_paragraph()
            r2 = p2.add_run()
            r2.text = subtitle
            r2.font.name = "Arial"
            r2.font.size = Pt(11)
            r2.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, fill_color=WHITE, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = fill_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        return card

    def add_circle_badge(slide, left, top, number_str, size=Inches(0.42), fill_color=ROYAL_BLUE):
        circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, left, top, size, size)
        circle.fill.solid()
        circle.fill.fore_color.rgb = fill_color
        circle.line.fill.background()
        cp = circle.text_frame.paragraphs[0]
        cp.alignment = PP_ALIGN.CENTER
        cr = cp.add_run()
        cr.text = number_str
        cr.font.name = "Arial"
        cr.font.size = Pt(11)
        cr.font.bold = True
        cr.font.color.rgb = TEXT_LIGHT
        return circle

    def add_figure_panel(slide, fig_path, left, top, width, height, caption):
        # Card background
        card = add_card(slide, left, top, width, height, fill_color=WHITE, border_color=CARD_BORDER)
        # Gold wireframe accent offset slightly (matching the artistic theme!)
        add_gold_wireframe(slide, left + Inches(0.06), top + Inches(0.06), width - Inches(0.12), height - Inches(0.12), border_color=GOLD_BORDER, border_width=1.0)
        
        if os.path.exists(fig_path):
            pad = Inches(0.16)
            slide.shapes.add_picture(str(fig_path), left + pad, top + pad, width - (pad * 2), height - Inches(0.55))
        
        cap_box = slide.shapes.add_textbox(left + Inches(0.15), top + height - Inches(0.45), width - Inches(0.3), Inches(0.38))
        p = cap_box.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = caption
        r.font.name = "Arial"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 1: COVER WITH HERO BRUSHSTROKE & GOLD WIREFRAME (PPTWORK THEME)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_white_bg(s1)

    # University Logo top-left
    logo_path = ASSETS_DIR / "image1.jpeg"
    if logo_path.exists():
        s1.shapes.add_picture(str(logo_path), Inches(0.8), Inches(0.45), width=Inches(2.8))

    # Hero Gold Wireframe Box (matching the template cover!)
    add_gold_wireframe(s1, Inches(4.3), Inches(0.6), Inches(4.7), Inches(3.4), border_color=GOLD_BORDER, border_width=1.5)

    # Hero Blue Oil Paint Splash across center
    if HERO_BRUSH_PATH.exists():
        s1.shapes.add_picture(str(HERO_BRUSH_PATH), Inches(3.2), Inches(0.4), width=Inches(6.9), height=Inches(3.8))

    # Text inside/over hero brushstroke
    t_hero = s1.shapes.add_textbox(Inches(3.5), Inches(1.3), Inches(6.3), Inches(2.0))
    hp1 = t_hero.text_frame.paragraphs[0]
    hp1.alignment = PP_ALIGN.CENTER
    hr1 = hp1.add_run()
    hr1.text = "B . T E C H   C A P S T O N E   D E F E N S E\n"
    hr1.font.name = "Arial"
    hr1.font.size = Pt(11)
    hr1.font.bold = True
    hr1.font.color.rgb = GOLD_ACCENT

    hp2 = t_hero.text_frame.add_paragraph()
    hp2.alignment = PP_ALIGN.CENTER
    hr2 = hp2.add_run()
    hr2.text = "E-COMMERCE INTELLIGENCE"
    hr2.font.name = "Arial"
    hr2.font.size = Pt(26)
    hr2.font.bold = True
    hr2.font.color.rgb = TEXT_LIGHT

    hp3 = t_hero.text_frame.add_paragraph()
    hp3.alignment = PP_ALIGN.CENTER
    hr3 = hp3.add_run()
    hr3.text = "& PREDICTIVE ANALYTICS PLATFORM"
    hr3.font.name = "Arial"
    hr3.font.size = Pt(16)
    hr3.font.bold = True
    hr3.font.color.rgb = RGBColor(191, 219, 254)

    # Subtitle line below brushstroke
    sub_box = s1.shapes.add_textbox(Inches(1.0), Inches(4.2), Inches(11.333), Inches(0.4))
    sp = sub_box.text_frame.paragraphs[0]
    sp.alignment = PP_ALIGN.CENTER
    sr = sp.add_run()
    sr.text = "Enterprise Kimball Data Warehouse, Geospatial Freight Telemetry, Target Leakage Ablation & Production Cloud SaaS"
    sr.font.name = "Arial"
    sr.font.size = Pt(12)
    sr.font.color.rgb = TEXT_MUTED

    # Guide Card
    g_card = add_card(s1, Inches(0.8), Inches(4.7), Inches(11.733), Inches(0.55), fill_color=OFF_WHITE, border_color=CARD_BORDER)
    add_gold_wireframe(s1, Inches(0.83), Inches(4.73), Inches(11.67), Inches(0.49), border_color=GOLD_BORDER, border_width=0.8)
    gtx = s1.shapes.add_textbox(Inches(1.0), Inches(4.72), Inches(11.3), Inches(0.5))
    gp = gtx.text_frame.paragraphs[0]
    gr1 = gp.add_run()
    gr1.text = "FACULTY PROJECT GUIDE: "
    gr1.font.bold = True
    gr1.font.size = Pt(10)
    gr1.font.color.rgb = ROYAL_BLUE

    gr2 = gp.add_run()
    gr2.text = "Prof. N. Lakshmipathi Anantha"
    gr2.font.bold = True
    gr2.font.size = Pt(11)
    gr2.font.color.rgb = TEXT_BLACK

    gr3 = gp.add_run()
    gr3.text = "   |   Assistant Professor, School of Computer Science and Engineering (SCOPE), VIT-AP University   |   Fall 2026-27"
    gr3.font.size = Pt(9.5)
    gr3.font.color.rgb = TEXT_MUTED

    # 4 Candidate Cards with Gold Wireframe
    candidates = [
        {"num": "1", "name": "Papasani Suhitha", "reg": "23BCE7826", "role": "Data Engineering & Star Schema", "photo": ASSETS_DIR / "photo_suhitha_enhanced.jpg"},
        {"num": "2", "name": "Gajjala Srithika", "reg": "23BCE7911", "role": "Customer Intelligence & RFM", "photo": ASSETS_DIR / "photo_srithika.jpg"},
        {"num": "3", "name": "Ala Venkata Veera Ritwik", "reg": "23BCE9633", "role": "ML Churn Leakage & Forecasting", "photo": ASSETS_DIR / "photo_ritwik.jpg"},
        {"num": "4", "name": "M Akshay Sharma", "reg": "23BCE9668", "role": "Product Analytics & WebGL SaaS", "photo": ASSETS_DIR / "photo_akshay.jpg"},
    ]

    c_w = Inches(2.78)
    c_gap = Inches(0.2)
    c_top = Inches(5.35)
    c_h = Inches(1.85)

    for i, c in enumerate(candidates):
        c_left = Inches(0.8) + i * (c_w + c_gap)
        add_card(s1, c_left, c_top, c_w, c_h, fill_color=WHITE, border_color=CARD_BORDER)
        add_gold_wireframe(s1, c_left + Inches(0.04), c_top + Inches(0.04), c_w - Inches(0.08), c_h - Inches(0.08), border_color=GOLD_BORDER, border_width=0.8)

        # Photo
        p_path = c["photo"]
        if p_path.exists():
            im_w = Inches(0.85)
            im_h = Inches(1.1)
            im_left = c_left + Inches(0.12)
            im_top = c_top + Inches(0.35)
            s1.shapes.add_picture(str(p_path), im_left, im_top, im_w, im_h)
            add_gold_wireframe(s1, im_left, im_top, im_w, im_h, border_color=GOLD_BORDER, border_width=0.8)

        # Badge
        add_circle_badge(s1, c_left + Inches(0.12), c_top + Inches(0.08), c["num"], size=Inches(0.24))

        # Details
        tx = s1.shapes.add_textbox(c_left + Inches(1.05), c_top + Inches(0.2), c_w - Inches(1.12), Inches(1.5))
        p = tx.text_frame.paragraphs[0]
        r = p.add_run()
        r.text = c["name"]
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = TEXT_BLACK

        p2 = tx.text_frame.add_paragraph()
        r2 = p2.add_run()
        r2.text = c["reg"]
        r2.font.name = "Arial"
        r2.font.size = Pt(9)
        r2.font.bold = True
        r2.font.color.rgb = ROYAL_BLUE

        p3 = tx.text_frame.add_paragraph()
        r3 = p3.add_run()
        r3.text = c["role"]
        r3.font.name = "Arial"
        r3.font.size = Pt(8)
        r3.font.color.rgb = TEXT_MUTED

    s1.notes_slide.notes_text_frame.text = (
        "Good morning respected Faculty Guide Prof. N. Lakshmipathi Anantha and honorable evaluators. "
        "We are team NEXUS.AI, presenting our Capstone Project: 'E-Commerce Business Intelligence & Predictive Analytics Platform'. "
        "Our team consists of Papasani Suhitha (Data Engineering), Gajjala Srithika (Customer Intelligence), "
        "Ala Venkata Veera Ritwik (Machine Learning & Forecasting), and M Akshay Sharma (Product Analytics & WebGL Platform). "
        "Today we present an end-to-end enterprise solution addressing silent customer churn, target leakage, and geospatial logistics friction."
    )

    # =========================================================================
    # SLIDE 2: THE SILENT CHURN DILEMMA (CIRCULAR STEP BADGES)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_white_bg(s2)
    add_header(s2, "P R O B L E M   S T A T E M E N T", 
               "The Silent Churn Dilemma in Non-Contractual Retail", 
               "Why top-line GMV expansion conceals destructive 96.9% one-time buyer attrition")

    # 4 KPI Stat Cards across top with delicate gold wireframes
    kpis = [
        {"val": "99,441", "lbl": "Validated Orders", "sub": "R$ 15.8M Gross Merchandise Value", "color": ROYAL_BLUE},
        {"val": "96.9%", "lbl": "Single-Purchase Rate", "sub": "Silent attrition: 97/100 never return", "color": CRIMSON},
        {"val": "20.4%", "lbl": "Mean Freight Ratio", "sub": "Freight Fr > 0.20 drives churn", "color": ACCENT_AMBER},
        {"val": "73", "lbl": "Product Categories", "sub": "32,951 SKUs across 27 federal states", "color": ACCENT_GREEN},
    ]

    kw = Inches(2.78)
    kgap = Inches(0.2)
    ktop = Inches(1.85)
    kh = Inches(1.25)

    for i, kp in enumerate(kpis):
        kleft = Inches(0.8) + i * (kw + kgap)
        add_card(s2, kleft, ktop, kw, kh, fill_color=OFF_WHITE)
        add_gold_wireframe(s2, kleft + Inches(0.04), ktop + Inches(0.04), kw - Inches(0.08), kh - Inches(0.08), border_color=GOLD_BORDER, border_width=0.8)

        ktx = s2.shapes.add_textbox(kleft + Inches(0.12), ktop + Inches(0.08), kw - Inches(0.24), kh - Inches(0.16))
        p = ktx.text_frame.paragraphs[0]
        r = p.add_run()
        r.text = kp["val"]
        r.font.name = "Arial"
        r.font.size = Pt(23)
        r.font.bold = True
        r.font.color.rgb = kp["color"]

        p2 = ktx.text_frame.add_paragraph()
        r2 = p2.add_run()
        r2.text = kp["lbl"]
        r2.font.name = "Arial"
        r2.font.size = Pt(10.5)
        r2.font.bold = True
        r2.font.color.rgb = TEXT_BLACK

        p3 = ktx.text_frame.add_paragraph()
        r3 = p3.add_run()
        r3.text = kp["sub"]
        r3.font.name = "Arial"
        r3.font.size = Pt(8.5)
        r3.font.color.rgb = TEXT_MUTED

    # Left Column: Non-Contractual Blindspot summary with wireframe box
    add_card(s2, Inches(0.8), Inches(3.25), Inches(4.8), Inches(3.85), fill_color=WHITE)
    add_gold_wireframe(s2, Inches(0.85), Inches(3.3), Inches(4.7), Inches(3.75), border_color=GOLD_BORDER, border_width=1.0)
    
    tx_bl = s2.shapes.add_textbox(Inches(1.0), Inches(3.45), Inches(4.4), Inches(3.45))
    p = tx_bl.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = "THE NON-CONTRACTUAL BLINDSPOT"
    r.font.name = "Arial"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = CRIMSON

    p = tx_bl.text_frame.add_paragraph()
    p.space_before = Pt(8)
    r = p.add_run()
    r.text = (
        "In SaaS or subscription businesses, customer churn is explicit (marked by a cancellation trigger). "
        "In non-contractual e-commerce, customer departure is completely silent.\n\n"
        "While aggregate platform GMV was growing at 14.8% annually, 96.9% of customers made only one purchase. "
        "Traditional CRMs mistook customer dormancy for retention, leading to wasted marketing spend and high CAC.\n\n"
        "Our objective was to establish an enterprise data warehouse and deploy leak-free machine learning to diagnose and solve this silent churn."
    )
    r.font.size = Pt(9.5)
    r.font.color.rgb = TEXT_MUTED

    # Right Column: 4 Circular Step Badges (1, 2, 3, 4) & Callout Boxes (matching the template!)
    callouts = [
        ("1", "Silent Non-Contractual Attrition", "96.9% of customers made exactly one purchase and departed without explicit notification."),
        ("2", "Deceptive GMV Growth Signaling", "Top-line revenue expansion hid chronic customer defection, inflating acquisition costs by 3.4x."),
        ("3", "Geospatial Logistics Friction Penalty", "Freight ratio exceeding 20% of cart value triggered severe 1-star review surges."),
        ("4", "OLTP Database Concurrency Bottlenecks", "Operational databases locked under heavy aggregation and lacked longitudinal cohort storage.")
    ]

    c_top_start = Inches(3.25)
    c_step_h = Inches(0.9)
    for i, (num, h_txt, b_txt) in enumerate(callouts):
        cur_y = c_top_start + i * c_step_h
        
        # Timeline connector line
        if i < 3:
            tline = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.05), cur_y + Inches(0.4), Inches(0.03), Inches(0.55))
            tline.fill.solid()
            tline.fill.fore_color.rgb = CARD_BORDER
            tline.line.fill.background()

        # Blue circle badge
        add_circle_badge(s2, Inches(5.85), cur_y, num, size=Inches(0.42), fill_color=ROYAL_BLUE)

        # Callout card with gold wireframe
        add_card(s2, Inches(6.45), cur_y, Inches(6.08), Inches(0.82), fill_color=OFF_WHITE)
        add_gold_wireframe(s2, Inches(6.48), cur_y + Inches(0.03), Inches(6.02), Inches(0.76), border_color=GOLD_BORDER, border_width=0.8)

        ctx = s2.shapes.add_textbox(Inches(6.6), cur_y + Inches(0.08), Inches(5.8), Inches(0.68))
        cp = ctx.text_frame.paragraphs[0]
        cr = cp.add_run()
        cr.text = h_txt
        cr.font.name = "Arial"
        cr.font.size = Pt(10.5)
        cr.font.bold = True
        cr.font.color.rgb = TEXT_BLACK

        cp2 = ctx.text_frame.add_paragraph()
        cr2 = cp2.add_run()
        cr2.text = b_txt
        cr2.font.name = "Arial"
        cr2.font.size = Pt(8.5)
        cr2.font.color.rgb = TEXT_MUTED

    s2.notes_slide.notes_text_frame.text = (
        "In non-contractual retail, customers never inform you when they leave. Over 96.9% of our 99,441 customers made exactly one purchase. "
        "Standard dashboards celebrate top-line GMV while hiding bleeding churn. Our objective was to establish an enterprise data warehouse, "
        "uncover the math of target leakage that invalidates prior ML churn studies, and deliver an actionable decision platform."
    )

    # =========================================================================
    # SLIDE 3: SYSTEM ARCHITECTURE
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_white_bg(s3)
    add_header(s3, "S Y S T E M   A R C H I T E C T U R E", 
               "Decoupled 3-Tier Enterprise Data & Inference Architecture", 
               "Unified pipeline from raw transaction ingestion to low-latency analytical serving")

    col_w = Inches(5.1)
    col_h = Inches(5.5)

    add_card(s3, Inches(0.8), Inches(1.7), col_w, col_h, fill_color=WHITE)
    add_gold_wireframe(s3, Inches(0.85), Inches(1.75), col_w - Inches(0.1), col_h - Inches(0.1), border_color=GOLD_BORDER, border_width=1.0)
    
    tx_arch = s3.shapes.add_textbox(Inches(1.0), Inches(1.9), col_w - Inches(0.4), col_h - Inches(0.4))
    p = tx_arch.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = "THE 3-TIER ARCHITECTURAL STACK"
    r.font.name = "Arial"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = TEXT_BLACK

    tiers = [
        ("Tier 1: Ingestion & Data Staging", 
         "9 raw CSV transactional tables validated via SHA-256 data integrity checks, UTF-8 cleansing, and Haversine geospatial calculations. Ingestion rate: 28,500 rec/sec."),
        ("Tier 2: Kimball Star Schema Warehouse", 
         "13-table PostgreSQL dimensional database using 32-bit surrogate integer keys and indexed foreign relations. Eliminates string joins and delivers sub-120ms aggregation."),
        ("Tier 3: Analytics Inference & WebGL SaaS", 
         "FastAPI asynchronous backend serving leak-free ML pipelines (XGBoost, K-Means, Holt-Winters). React executive cockpit with Three.js WebGL particle gateway.")
    ]

    for t_name, t_desc in tiers:
        p = tx_arch.text_frame.add_paragraph()
        p.space_before = Pt(8)
        r1 = p.add_run()
        r1.text = t_name + "\n"
        r1.font.bold = True
        r1.font.size = Pt(10)
        r1.font.color.rgb = ROYAL_BLUE
        r2 = p.add_run()
        r2.text = t_desc
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = TEXT_MUTED

    p = tx_arch.text_frame.add_paragraph()
    p.space_before = Pt(12)
    r = p.add_run()
    r.text = "PRODUCTION PERFORMANCE TELEMETRY:\n"
    r.font.bold = True
    r.font.size = Pt(9.5)
    r.font.color.rgb = GOLD_ACCENT
    r = p.add_run()
    r.text = "• Ingestion Throughput: 28,500 rows/sec\n• Analytical Query Latency: 84ms p95\n• End-to-End API Response: 112ms p99"
    r.font.size = Pt(8.5)
    r.font.color.rgb = TEXT_BLACK

    # Right Column: Figure 1
    fig1_path = FIG_DIR / "fig1_system_architecture.png"
    add_figure_panel(s3, fig1_path, Inches(6.1), Inches(1.7), Inches(6.433), col_h, 
                     "Figure 1: End-to-end 3-tier enterprise architecture showing data staging, star schema, and inference engines.")

    s3.notes_slide.notes_text_frame.text = (
        "Figure 1 illustrates our decoupled 3-tier architecture. In Tier 1, Papasani Suhitha built an ingestion pipeline capable of processing "
        "28,500 records per second with automated UTF-8 cleansing and Haversine distance calculations. Tier 2 is our 13-table PostgreSQL "
        "Kimball star schema. Tier 3 hosts the analytical models and FastAPI endpoints delivering p95 latencies under 84ms."
    )

    # =========================================================================
    # SLIDE 4: 13-TABLE STAR SCHEMA
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_white_bg(s4)
    add_header(s4, "D A T A   W A R E H O U S I N G", 
               "13-Table Relational PostgreSQL Star Schema", 
               "Surrogate key architecture eliminating 32-character hexadecimal string join bottlenecks")

    add_card(s4, Inches(0.8), Inches(1.7), Inches(5.1), col_h, fill_color=WHITE)
    add_gold_wireframe(s4, Inches(0.85), Inches(1.75), Inches(5.0), col_h - Inches(0.1), border_color=GOLD_BORDER, border_width=1.0)
    
    tx_star = s4.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(4.7), col_h - Inches(0.4))
    p = tx_star.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = "ENTERPRISE DIMENSIONAL CATALOG"
    r.font.name = "Arial"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = TEXT_BLACK

    star_points = [
        ("Grain Isolation & Fact Centrality: ", 
         "5 central fact tables isolate business events at varying granularities: fact_orders (1 row/order), fact_order_items (line items), fact_order_payments, fact_order_reviews, and fact_daily_sales."),
        ("Surrogate Integer Keys: ", 
         "Replaced 32-character hex UUID strings with 32-bit SERIAL INT surrogate keys (customer_key, seller_key, product_key), reducing B-Tree index size by 68.4% and accelerating JOIN queries by 4.2x."),
        ("Conformed Dimensions: ", 
         "7 conformed dimensions (dim_customers, dim_sellers, dim_products, dim_geography, dim_date, dim_payment_types, dim_order_status) ensure cross-functional slice-and-dice consistency."),
        ("Zero Update Anomalies: ", 
         "Strict 3NF dimension design eliminates transitive dependencies while maintaining high-speed denormalized reporting views.")
    ]

    for sp_title, sp_desc in star_points:
        p = tx_star.text_frame.add_paragraph()
        p.space_before = Pt(8)
        r1 = p.add_run()
        r1.text = sp_title
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = ROYAL_BLUE
        r2 = p.add_run()
        r2.text = sp_desc
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = TEXT_MUTED

    fig2_path = FIG_DIR / "fig2_star_schema.png"
    add_figure_panel(s4, fig2_path, Inches(6.1), Inches(1.7), Inches(6.433), col_h, 
                     "Figure 2: 13-table Kimball star schema highlighting fact-dimension cardinality and foreign key indexing.")

    s4.notes_slide.notes_text_frame.text = (
        "Figure 2 exhibits our 13-table PostgreSQL star schema. A key technical contribution was replacing 32-character hexadecimal UUIDs "
        "with 32-bit surrogate integer keys. This simple architectural decision compressed our B-Tree index memory footprint by 68.4% "
        "and delivered a 4.2x speedup on complex multi-table joins across 99,441 transactional records."
    )

    # =========================================================================
    # SLIDE 5: GEOSPATIAL LOGISTICS FRICTION
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_white_bg(s5)
    add_header(s5, "L O G I S T I C S   T E L E M E T R Y", 
               "Geospatial Economics & Freight Ratio (Fr > 0.20) Friction", 
               "Haversine distance telemetry proves delivery overhead dominates product satisfaction")

    add_card(s5, Inches(0.8), Inches(1.7), Inches(5.1), col_h, fill_color=WHITE)
    add_gold_wireframe(s5, Inches(0.85), Inches(1.75), Inches(5.0), col_h - Inches(0.1), border_color=GOLD_BORDER, border_width=1.0)
    
    tx_geo = s5.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(4.7), col_h - Inches(0.4))
    p = tx_geo.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = "MATHEMATICAL FORMULATION"
    r.font.name = "Arial"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = TEXT_BLACK

    geo_formulas = [
        ("Haversine Great-Circle Distance (d):", 
         "d = 2R · arcsin(√(sin²(Δφ/2) + cos φ₁ cos φ₂ sin²(Δλ/2)))\nWhere R = 6,371 km represents Earth's mean radius."),
        ("Freight Ratio Burden (Fr):", 
         "Fr = freight_value / (item_price + freight_value)\nMeasures shipping overhead relative to total cart expenditure.")
    ]

    for gf_title, gf_eq in geo_formulas:
        p = tx_geo.text_frame.add_paragraph()
        p.space_before = Pt(6)
        r1 = p.add_run()
        r1.text = gf_title + "\n"
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = ROYAL_BLUE
        r2 = p.add_run()
        r2.text = gf_eq
        r2.font.name = "Courier New"
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = TEXT_BLACK

    # Solid Royal Blue Highlight Card with Gold Border
    add_card(s5, Inches(1.0), Inches(3.95), Inches(4.7), Inches(1.4), fill_color=ROYAL_BLUE, border_color=None)
    add_gold_wireframe(s5, Inches(1.04), Inches(3.99), Inches(4.62), Inches(1.32), border_color=GOLD_ACCENT, border_width=1.0)
    
    htx = s5.shapes.add_textbox(Inches(1.15), Inches(4.02), Inches(4.4), Inches(1.25))
    hp = htx.text_frame.paragraphs[0]
    hr1 = hp.add_run()
    hr1.text = "THE 20% FRICTION INFLECTION POINT\n"
    hr1.font.bold = True
    hr1.font.size = Pt(10.5)
    hr1.font.color.rgb = GOLD_ACCENT

    hr2 = hp.add_run()
    hr2.text = (
        "When shipping exceeds 20% of cart value (Fr > 0.20), 1-star reviews surge by 78.4% independent of product quality. "
        "Carrier delivery delays past SLA (Δt > 3 days) multiply churn probability by 2.3x."
    )
    hr2.font.size = Pt(8.5)
    hr2.font.color.rgb = TEXT_LIGHT

    fig6_path = FIG_DIR / "fig6_regional_economics.png"
    add_figure_panel(s5, fig6_path, Inches(6.1), Inches(1.7), Inches(6.433), col_h, 
                     "Figure 3: Geospatial logistics telemetry: Haversine route density, state freight burdens, and delivery delay distributions.")

    s5.notes_slide.notes_text_frame.text = (
        "In Figure 3, we demonstrate why logistics economics directly governs e-commerce retention. By computing Haversine great-circle "
        "distances across all customer-seller pairs, we identified that freight burden Fr = freight / (price + freight) is the single greatest "
        "operational driver of dissatisfaction. When Fr exceeds 0.20, review scores collapse from 4.3 to 2.8 stars, proving customers "
        "punish sellers for shipping overhead rather than product defects."
    )

    # =========================================================================
    # SLIDE 6: CUSTOMER INTELLIGENCE (RFM + K-MEANS)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_white_bg(s6)
    add_header(s6, "C U S T O M E R   I N T E L L I G E N C E", 
               "Algorithmic Customer Segmentation: Log-Transformed K-Means (k=4)", 
               "Unsupervised PCA decomposition isolating 4 distinct behavioral lifecycle personas")

    add_card(s6, Inches(0.8), Inches(1.7), Inches(5.1), col_h, fill_color=WHITE)
    add_gold_wireframe(s6, Inches(0.85), Inches(1.75), Inches(5.0), col_h - Inches(0.1), border_color=GOLD_BORDER, border_width=1.0)
    
    tx_rfm = s6.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(4.7), col_h - Inches(0.4))
    p = tx_rfm.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = "THE 4 BEHAVIORAL PERSONAS"
    r.font.name = "Arial"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = TEXT_BLACK

    personas = [
        ("1", "Champions (12.4% pop | R$ 812.40 GMV):", 
         "High frequency, low recency (<45 days), heavy credit card installments. Core profit engine. Strategy: VIP exclusivity & loyalty perks."),
        ("2", "Loyal High-Value (23.8% pop | R$ 348.10 GMV):", 
         "Consistent repeat buyers with high basket size and high satisfaction scores. Strategy: Category cross-selling & restocking reminders."),
        ("3", "At-Risk Defectors (28.6% pop | R$ 142.50 GMV):", 
         "High recency (>180 days), declining review scores, and elevated freight ratios. Prime targets for automated win-back discount vouchers."),
        ("4", "Dormant Bargain Hunters (35.2% pop | R$ 68.20 GMV):", 
         "Single-purchase customers attracted solely by promotional markdowns via Boleto. Low margin, high churn propensity.")
    ]

    for num, pr_title, pr_desc in personas:
        p = tx_rfm.text_frame.add_paragraph()
        p.space_before = Pt(6)
        r1 = p.add_run()
        r1.text = f"[{num}] " + pr_title + "\n"
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = ROYAL_BLUE
        r2 = p.add_run()
        r2.text = pr_desc
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = TEXT_MUTED

    p = tx_rfm.text_frame.add_paragraph()
    p.space_before = Pt(8)
    r = p.add_run()
    r.text = "CLUSTERING METHODOLOGY:\n"
    r.font.bold = True
    r.font.size = Pt(9.5)
    r.font.color.rgb = GOLD_ACCENT
    r = p.add_run()
    r.text = "Log-transform x̃ = ln(x + 1) normalized heavy right-skew. Elbow heuristic and Silhouette analysis (s = 0.612) confirmed mathematical optimality at k = 4."
    r.font.size = Pt(8.5)
    r.font.color.rgb = TEXT_BLACK

    fig4_path = FIG_DIR / "fig4_kmeans_pca_elbow.png"
    add_figure_panel(s6, fig4_path, Inches(6.1), Inches(1.7), Inches(6.433), col_h, 
                     "Figure 4: Unsupervised clustering: (a) WCSS elbow curve confirming k=4, and (b) 2D PCA projection of the 4 behavioral customer clusters.")

    s6.notes_slide.notes_text_frame.text = (
        "Figure 4 presents Gajjala Srithika's customer intelligence pipeline. Monetary value in e-commerce follows a Pareto power law. "
        "Applying standard K-Means directly fails due to extreme outliers. By applying a logarithmic transform x̃ = ln(x+1) and Z-score "
        "normalization, our WCSS elbow curve confirmed an optimal inflection at k=4 with a Silhouette score of 0.612. The 2D PCA projection "
        "reveals sharp separation between high-margin Champions and high-risk At-Risk Defectors."
    )

    # =========================================================================
    # SLIDE 7: TARGET LEAKAGE DISCOVERY
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_white_bg(s7)
    add_header(s7, "M A C H I N E   L E A R N I N G   P R O O F", 
               "Target Leakage Discovery: The Deceptive 99% Accuracy Trap", 
               "Mathematical proof of how post-hoc tenure features artificially inflate churn models")

    pan_w = Inches(5.75)
    pan_h = Inches(5.5)

    add_card(s7, Inches(0.8), Inches(1.7), pan_w, pan_h, fill_color=WHITE)
    add_gold_wireframe(s7, Inches(0.85), Inches(1.75), pan_w - Inches(0.1), pan_h - Inches(0.1), border_color=GOLD_BORDER, border_width=1.0)
    
    tx_lp = s7.shapes.add_textbox(Inches(1.0), Inches(1.9), pan_w - Inches(0.4), pan_h - Inches(0.4))
    p = tx_lp.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = "THE MATHEMATICAL INFORMATION LEAKAGE PROOF"
    r.font.name = "Arial"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = CRIMSON

    proof_steps = [
        ("Step 1: Ground Truth Label Definition", 
         "Churn label y_i is defined over observation cutoff t_obs and inactivity window Δt_churn = 90 days:\n  y_i = 1  if (t_obs - t_last) > 90  (Churned)\n  y_i = 0  otherwise (Retained)"),
        ("Step 2: Customer Tenure Definition", 
         "Standard e-commerce feature stores compute customer tenure T_tenure as elapsed days since first purchase:\n  T_tenure = t_obs - t_first"),
        ("Step 3: The Single-Purchase Collapse (96.9% of Data)", 
         "For 96.9% of customers in non-contractual retail, t_first = t_last. Consequently:\n  T_tenure = t_obs - t_last"),
        ("Step 4: The Trivial Decision Boundary", 
         "Substituting into the churn definition yields strict equivalence:\n  y_i = 1  ⟺  T_tenure > 90\nTree models exploit this trivial split: f(X) = 𝟙(T_tenure ≤ 90), yielding an artificial 0.9998 AUC.")
    ]

    for p_title, p_desc in proof_steps:
        p = tx_lp.text_frame.add_paragraph()
        p.space_before = Pt(6)
        r1 = p.add_run()
        r1.text = p_title + "\n"
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = ROYAL_BLUE
        r2 = p.add_run()
        r2.text = p_desc
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = TEXT_BLACK

    add_card(s7, Inches(6.75), Inches(1.7), pan_w, pan_h, fill_color=OFF_WHITE)
    add_gold_wireframe(s7, Inches(6.8), Inches(1.75), pan_w - Inches(0.1), pan_h - Inches(0.1), border_color=GOLD_BORDER, border_width=1.0)
    
    tx_cf = s7.shapes.add_textbox(Inches(6.95), Inches(1.9), pan_w - Inches(0.4), pan_h - Inches(0.4))
    p = tx_cf.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = "PRODUCTION DEPLOYMENT CATASTROPHE"
    r.font.name = "Arial"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = ACCENT_AMBER

    catastrophe_points = [
        ("The Literature Blindspot: ", 
         "Numerous published academic benchmarks boast 99% accuracy on retail churn by including tenure_days. They unknowingly train on the target label!"),
        ("Day-1 Production Failure: ", 
         "When deployed live, a new customer places their first order today: T_tenure = 0 days ≤ 90. The leaked model classifies 100% of newly acquired customers as NON-CHURNERS (ŷ = 0), completely blinding marketing teams to early defection."),
        ("Our Remediation (Pre-Attrition Feature Store X_pre): ", 
         "Ala Venkata Veera Ritwik strictly ablated all post-hoc duration features. We formulated feature store X_pre relying solely on operational, behavioral, and logistics signals available at time of purchase.")
    ]

    for c_title, c_desc in catastrophe_points:
        p = tx_cf.text_frame.add_paragraph()
        p.space_before = Pt(8)
        r1 = p.add_run()
        r1.text = c_title
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = TEXT_BLACK
        r2 = p.add_run()
        r2.text = c_desc
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = TEXT_MUTED

    p = tx_cf.text_frame.add_paragraph()
    p.space_before = Pt(12)
    r = p.add_run()
    r.text = "OUR CORE RESEARCH CONTRIBUTION:\n"
    r.font.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = ROYAL_BLUE
    r = p.add_run()
    r.text = "We establish the first empirical ablation framework that decouples post-hoc tenure leakage from real causal drivers of customer defection."
    r.font.size = Pt(9)
    r.font.color.rgb = TEXT_BLACK

    s7.notes_slide.notes_text_frame.text = (
        "Slide 7 represents one of our most significant academic contributions, authored by Ala Venkata Veera Ritwik. "
        "Many published papers claim 99% accuracy on retail churn. We proved this is a mathematical illusion caused by target leakage. "
        "Because 96.9% of customers only buy once, customer tenure equals time since last purchase. The decision tree simply splits on "
        "tenure > 90 days. But in production, a brand new customer has tenure=0, so the model falsely predicts they will never churn! "
        "We formulated a leak-free pre-attrition feature store X_pre to solve this."
    )

    # =========================================================================
    # SLIDE 8: DUAL-MODEL CHURN ABLATION STUDY
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_white_bg(s8)
    add_header(s8, "E M P I R I C A L   B E N C H M A R K S", 
               "Dual-Model Churn Ablation Study & TreeSHAP Attribution", 
               "Rigorous empirical benchmark proving real behavioral signals vs leaked baseline")

    add_card(s8, Inches(0.8), Inches(1.7), Inches(5.1), col_h, fill_color=WHITE)
    add_gold_wireframe(s8, Inches(0.85), Inches(1.75), Inches(5.0), col_h - Inches(0.1), border_color=GOLD_BORDER, border_width=1.0)
    
    tx_abl = s8.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(4.7), col_h - Inches(0.4))
    p = tx_abl.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = "EMPIRICAL ABLATION COMPARISON"
    r.font.name = "Arial"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = TEXT_BLACK

    p = tx_abl.text_frame.add_paragraph()
    p.space_before = Pt(6)
    r = p.add_run()
    r.text = (
        "Metric          Model A (Leaked)  Model B (Ablated)\n"
        "───────────────────────────────────────────────────\n"
        "Accuracy        99.28%            84.18%  (Realistic)\n"
        "ROC-AUC         0.9998            0.8624  (Production)\n"
        "PR-AUC          0.9986            0.8519  (Imbalanced)\n"
        "Recall (Churn)  98.92%            85.12%  (Win-Back)\n"
        "Brier Score     0.0071            0.1142  (Calibrated)\n"
        "Top Feature     tenure (98.8%)    freight_ratio (34.2%)\n"
        "───────────────────────────────────────────────────\n"
    )
    r.font.name = "Courier New"
    r.font.size = Pt(8.5)
    r.font.color.rgb = TEXT_BLACK

    p = tx_abl.text_frame.add_paragraph()
    p.space_before = Pt(6)
    r = p.add_run()
    r.text = "TOP TREESHAP BEHAVIORAL DRIVERS:\n"
    r.font.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = ROYAL_BLUE
    r = p.add_run()
    r.text = (
        "1. Freight Ratio (34.20%): Steep non-linear inflection at Fr > 0.20.\n"
        "2. Review Score (16.50%): 1-star ratings trigger 78.4% churn odds.\n"
        "3. Payment Installments (14.80%): Multi-installment credit builds lock-in.\n"
        "4. Monetary Total (12.10%): High GMV customers exhibit brand loyalty."
    )
    r.font.size = Pt(8.5)
    r.font.color.rgb = TEXT_BLACK

    fig3_path = FIG_DIR / "fig3_churn_roc_feature_importance.png"
    add_figure_panel(s8, fig3_path, Inches(6.1), Inches(1.7), Inches(6.433), col_h, 
                     "Figure 5: Dual-model evaluation: (a) ROC curve comparison (Model A 0.9998 vs Model B 0.8624), and (b) TreeSHAP feature importance.")

    s8.notes_slide.notes_text_frame.text = (
        "Figure 5 demonstrates the empirical ablation results. Model A with leakage achieves a suspicious 0.9998 ROC-AUC driven 98.8% by tenure. "
        "Model B strictly removes tenure and achieves an honest, production-ready 0.8624 ROC-AUC and 85.12% recall. "
        "More importantly, our TreeSHAP analysis reveals that freight ratio and review sentiment are the true causal drivers of churn, "
        "giving business executives concrete operational levers to fix customer attrition."
    )

    # =========================================================================
    # SLIDE 9: LONGITUDINAL DEMAND FORECASTING
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_white_bg(s9)
    add_header(s9, "P R E D I C T I V E   R E V E N U E", 
               "Longitudinal Demand Forecasting: Multiplicative Holt-Winters", 
               "Triple exponential smoothing capturing Black Friday demand surges with 8.42% MAPE")

    add_card(s9, Inches(0.8), Inches(1.7), Inches(5.1), col_h, fill_color=WHITE)
    add_gold_wireframe(s9, Inches(0.85), Inches(1.75), Inches(5.0), col_h - Inches(0.1), border_color=GOLD_BORDER, border_width=1.0)
    
    tx_hw = s9.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(4.7), col_h - Inches(0.4))
    p = tx_hw.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = "TRIPLE EXPONENTIAL SMOOTHING"
    r.font.name = "Arial"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = TEXT_BLACK

    hw_formulas = [
        ("Level Component (ℓ_t):", 
         "ℓ_t = α(y_t / s_{t-m}) + (1 - α)(ℓ_{t-1} + b_{t-1})\nTracks underlying baseline sales volume across weekly cycles."),
        ("Trend Component (b_t):", 
         "b_t = β(ℓ_t - ℓ_{t-1}) + (1 - β)b_{t-1}\nCaptures secular year-over-year revenue expansion."),
        ("Multiplicative Seasonality (s_t):", 
         "s_t = γ(y_t / (ℓ_{t-1} + b_{t-1})) + (1 - γ)s_{t-m}\nCaptures 52-week annual consumer buying spikes.")
    ]

    for hf_title, hf_eq in hw_formulas:
        p = tx_hw.text_frame.add_paragraph()
        p.space_before = Pt(6)
        r1 = p.add_run()
        r1.text = hf_title + "\n"
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = ROYAL_BLUE
        r2 = p.add_run()
        r2.text = hf_eq
        r2.font.name = "Courier New"
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = TEXT_BLACK

    p = tx_hw.text_frame.add_paragraph()
    p.space_before = Pt(8)
    r = p.add_run()
    r.text = "FORECASTING PERFORMANCE BENCHMARK:\n"
    r.font.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = GOLD_ACCENT
    r = p.add_run()
    r.text = (
        "• Out-of-Sample Horizon: 90-day test window\n"
        "• Model MAPE: 8.42% (Multiplicative Holt-Winters) vs 14.12% (SARIMA baseline)\n"
        "• Extreme Event Capture: Accurately forecasted the 4.1x November volume explosion within 95% confidence bounds.\n"
        "• Logistics Pre-Booking: Enables supply chain managers to pre-book 3PL carrier capacity 90 days in advance."
    )
    r.font.size = Pt(8.5)
    r.font.color.rgb = TEXT_BLACK

    fig5_path = FIG_DIR / "fig5_revenue_forecasting.png"
    add_figure_panel(s9, fig5_path, Inches(6.1), Inches(1.7), Inches(6.433), col_h, 
                     "Figure 6: Longitudinal sales forecasting: 90-day multiplicative Holt-Winters demand projection with 95% confidence bounds.")

    s9.notes_slide.notes_text_frame.text = (
        "Figure 6 highlights our longitudinal demand forecasting module. In retail, additive models fail during holiday surges because variance "
        "scales with volume. By deploying Multiplicative Holt-Winters triple exponential smoothing with m=52 weekly seasonality, "
        "we achieved an out-of-sample MAPE of 8.42%, outperforming standard SARIMA (14.12%). Our model captured the massive 4.1x "
        "Black Friday spike within 95% confidence bands, allowing supply chain teams to pre-allocate logistics capacity."
    )

    # =========================================================================
    # SLIDE 10: PRODUCT PORTFOLIO STRATEGY (BCG MATRIX)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_white_bg(s10)
    add_header(s10, "S T R A T E G I C   M E R C H A N D I S I N G", 
               "Product Portfolio Optimization: 73-Category BCG Matrix", 
               "Market growth rate vs relative market share capital allocation across 32,951 catalog SKUs")

    add_card(s10, Inches(0.8), Inches(1.7), Inches(5.1), col_h, fill_color=WHITE)
    add_gold_wireframe(s10, Inches(0.85), Inches(1.75), Inches(5.0), col_h - Inches(0.1), border_color=GOLD_BORDER, border_width=1.0)
    
    tx_bcg = s10.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(4.7), col_h - Inches(0.4))
    p = tx_bcg.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = "THE 4 STRATEGIC MERCHANDISING QUADRANTS"
    r.font.name = "Arial"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = TEXT_BLACK

    bcg_quads = [
        ("Cash Cows (38.4% GMV Share):", 
         "Bed/Bath/Table, Health/Beauty, Sports/Leisure. High relative market share in mature, low-growth categories. Primary engine of liquidity. Strategy: Harvest cash flow to subsidize growth."),
        ("Stars (24.1% GMV Share):", 
         "Computers/Accessories, Telephony. High market share in rapidly expanding categories. Strategic growth drivers. Strategy: Aggressive reinvestment in inventory and seller acquisition."),
        ("Question Marks (19.2% GMV Share):", 
         "Small Appliances, Audio, Fashion. High category growth but low platform share. Strategy: Selective seller subsidies or platform consolidation to convert into Stars."),
        ("Dogs (18.3% GMV Share):", 
         "DVDs, Security items, Niche hardware. Low growth and low market share. Strategy: Catalog pruning, vendor delisting, and markdowns to free up warehouse working capital.")
    ]

    for bq_title, bq_desc in bcg_quads:
        p = tx_bcg.text_frame.add_paragraph()
        p.space_before = Pt(6)
        r1 = p.add_run()
        r1.text = bq_title + "\n"
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = ROYAL_BLUE
        r2 = p.add_run()
        r2.text = bq_desc
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = TEXT_MUTED

    fig7_path = FIG_DIR / "fig7_category_bcg_matrix.png"
    add_figure_panel(s10, fig7_path, Inches(6.1), Inches(1.7), Inches(6.433), col_h, 
                     "Figure 7: 73-category BCG Growth-Share matrix showing relative market share, annual category growth, and GMV bubble sizing.")

    s10.notes_slide.notes_text_frame.text = (
        "Figure 7 illustrates M Akshay Sharma's product portfolio analytics. Analyzing 73 categories and 32,951 SKUs, we constructed the BCG "
        "Growth-Share matrix. Cash Cows such as Bed/Bath and Health/Beauty represent 38.4% of total GMV, generating the operating cash flows "
        "necessary to aggressively subsidize high-growth Stars in Computers and Electronics. Conversely, catalog pruning in the Dog quadrant "
        "frees up critical working capital."
    )

    # =========================================================================
    # SLIDE 11: PRODUCTION SAAS PLATFORM
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_white_bg(s11)
    add_header(s11, "P R O D U C T I O N   S A A S", 
               "Enterprise Production SaaS Platform & Interactive 3D WebGL", 
               "Live cloud deployment featuring Three.js particle portal and multi-year temporal slicing")

    dash_path = FIG_DIR / "screenshot_dashboard.png"
    add_figure_panel(s11, dash_path, Inches(0.8), Inches(1.7), Inches(6.0), Inches(3.6), 
                     "Executive Decision Cockpit: Multi-year temporal filters, real-time KPI tiles, and dynamic cohort analysis.")

    login_path = FIG_DIR / "screenshot_login.png"
    add_figure_panel(s11, login_path, Inches(7.0), Inches(1.7), Inches(5.533), Inches(3.6), 
                     "3D WebGL Gateway: Three.js interactive particle system representing live customer network topology.")

    # Bottom 4 Horizontal Capability Cards with Gold Wireframe
    add_card(s11, Inches(0.8), Inches(5.45), Inches(11.733), Inches(1.65), fill_color=OFF_WHITE)
    add_gold_wireframe(s11, Inches(0.85), Inches(5.5), Inches(11.633), Inches(1.55), border_color=GOLD_BORDER, border_width=1.0)
    
    tx_saas = s11.shapes.add_textbox(Inches(1.0), Inches(5.55), Inches(11.3), Inches(1.45))
    p = tx_saas.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = "FULL-STACK PRODUCTION CLOUD ARCHITECTURE & KEY CAPABILITIES:"
    r.font.name = "Arial"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = TEXT_BLACK

    saas_feats = [
        ("FastAPI Async Microservices: ", "RESTful backend with JWT authentication, CORS middleware, and p99 query latency under 112ms."),
        ("Interactive 3D Three.js Visuals: ", "WebGL shader particle engine providing tactile visual feedback and dynamic network clustering."),
        ("Multi-Year Temporal Slicing: ", "Custom date-range slider enabling multi-year cohort comparisons across 2016, 2017, and 2018."),
        ("Automated Win-Back Triggers: ", "Integrates XGBoost churn inference to dispatch automated retention alerts for At-Risk customers.")
    ]

    for sf_title, sf_desc in saas_feats:
        p = tx_saas.text_frame.add_paragraph()
        r1 = p.add_run()
        r1.text = "• " + sf_title
        r1.font.bold = True
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = ROYAL_BLUE
        r2 = p.add_run()
        r2.text = sf_desc
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = TEXT_MUTED

    s11.notes_slide.notes_text_frame.text = (
        "Slide 11 presents our live production platform built by M Akshay Sharma. We did not stop at Jupyter notebooks; we deployed "
        "a full-stack enterprise cloud application. The frontend features a custom Three.js WebGL particle portal and an executive "
        "dashboard with multi-year temporal sliders, state-level freight heatmaps, and dynamic cohort drill-downs, backed by FastAPI "
        "delivering sub-100ms analytical queries."
    )

    # =========================================================================
    # SLIDE 12: ACADEMIC SYNTHESIS & DELIVERABLES (CLOSING HERO BRUSHSTROKE)
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_white_bg(s12)
    add_top_bar(s12)

    # Decorative brushstroke in bottom right
    if HERO_BRUSH_PATH.exists():
        s12.shapes.add_picture(str(HERO_BRUSH_PATH), Inches(8.5), Inches(3.8), width=Inches(4.6), height=Inches(2.8))

    # Header Box
    t_box12 = s12.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.7), Inches(0.85))
    p = t_box12.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = "R E S E A R C H   S Y N T H E S I S   &   D E F E N S E   C O N C L U S I O N\n"
    r.font.name = "Arial"
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = ROYAL_BLUE

    r2 = p.add_run()
    r2.text = "Academic Contributions, Deliverables & Defense Conclusion"
    r2.font.name = "Arial"
    r2.font.size = Pt(21)
    r2.font.bold = True
    r2.font.color.rgb = TEXT_BLACK

    p2 = t_box12.text_frame.add_paragraph()
    r3 = p2.add_run()
    r3.text = "Bridging empirical data science research with enterprise-grade cloud software engineering"
    r3.font.name = "Arial"
    r3.font.size = Pt(11)
    r3.font.color.rgb = TEXT_MUTED

    # 3 Deliverable Cards with Gold Wireframes
    deliv_w = Inches(3.7)
    deliv_gap = Inches(0.31)
    deliv_top = Inches(1.7)
    deliv_h = Inches(4.1)

    deliverables = [
        {"title": "1. Capstone Thesis Report", 
         "badge": "40+ PAGES COMPREHENSIVE",
         "items": [
             "Official VIT-AP SCOPE thesis format compliance",
             "Complete 13-table Kimball star schema specification",
             "Mathematical proofs for Haversine, Fr, and leakage",
             "Student credentials, photo badges & CD sleeve design",
             "Available in publication DOCX, Markdown, and PDF"
         ]},
        {"title": "2. IEEE Conference Paper", 
         "badge": "DOUBLE-COLUMN RESEARCH",
         "items": [
             "Target leakage discovery and ablation protocol",
             "Empirical dual-model benchmarks (0.8624 AUC)",
             "TreeSHAP causal feature attribution plots",
             "Humanized, zero-plagiarism academic prose",
             "Ready for peer-reviewed conference submission"
         ]},
        {"title": "3. Production Software Platform", 
         "badge": "PRODUCTION SAAS CODEBASE",
         "items": [
             "FastAPI async backend with 13 SQL schemas",
             "Three.js 3D WebGL particle interactive gateway",
             "Multi-year executive dashboard with cohort filters",
             "Automated test suite, Dockerfile & Vercel deployment",
             "Complete GitHub version-controlled repository"
         ]},
    ]

    for i, d in enumerate(deliverables):
        d_left = Inches(0.8) + i * (deliv_w + deliv_gap)
        add_card(s12, d_left, deliv_top, deliv_w, deliv_h, fill_color=OFF_WHITE)
        add_gold_wireframe(s12, d_left + Inches(0.04), deliv_top + Inches(0.04), deliv_w - Inches(0.08), deliv_h - Inches(0.08), border_color=GOLD_BORDER, border_width=1.0)

        # Header Box
        tx_dh = s12.shapes.add_textbox(d_left + Inches(0.15), deliv_top + Inches(0.12), deliv_w - Inches(0.3), Inches(0.75))
        p = tx_dh.text_frame.paragraphs[0]
        r = p.add_run()
        r.text = d["badge"] + "\n"
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = ROYAL_BLUE

        r2 = p.add_run()
        r2.text = d["title"]
        r2.font.name = "Arial"
        r2.font.size = Pt(12)
        r2.font.bold = True
        r2.font.color.rgb = TEXT_BLACK

        # Item Bullets
        tx_db = s12.shapes.add_textbox(d_left + Inches(0.15), deliv_top + Inches(0.85), deliv_w - Inches(0.3), deliv_h - Inches(0.95))
        for item in d["items"]:
            p = tx_db.text_frame.add_paragraph()
            p.space_before = Pt(8)
            r1 = p.add_run()
            r1.text = "✓ "
            r1.font.bold = True
            r1.font.size = Pt(9.5)
            r1.font.color.rgb = ROYAL_BLUE
            r2 = p.add_run()
            r2.text = item
            r2.font.name = "Arial"
            r2.font.size = Pt(8.5)
            r2.font.color.rgb = TEXT_MUTED

    # Bottom Mentor Acknowledgment Banner
    ack_card = add_card(s12, Inches(0.8), Inches(6.0), Inches(11.733), Inches(1.1), fill_color=WHITE, border_color=CARD_BORDER)
    add_gold_wireframe(s12, Inches(0.85), Inches(6.05), Inches(11.633), Inches(1.0), border_color=GOLD_BORDER, border_width=1.2)
    
    tx_ack = s12.shapes.add_textbox(Inches(1.0), Inches(6.12), Inches(11.3), Inches(0.9))
    p = tx_ack.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = "FACULTY GUIDE & INSTITUTIONAL ACKNOWLEDGMENT\n"
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = GOLD_ACCENT

    r2 = p.add_run()
    r2.text = "We extend our deepest gratitude to our Project Guide Prof. N. Lakshmipathi Anantha, Assistant Professor, SCOPE, "
    r2.font.name = "Arial"
    r2.font.size = Pt(9.5)
    r2.font.bold = True
    r2.font.color.rgb = TEXT_BLACK

    r3 = p.add_run()
    r3.text = "and the faculty of VIT-AP University for their invaluable mentorship, technical guidance, and constructive evaluation throughout Fall 2026–27."
    r3.font.name = "Arial"
    r3.font.size = Pt(9.5)
    r3.font.color.rgb = TEXT_MUTED

    s12.notes_slide.notes_text_frame.text = (
        "In conclusion, NEXUS.AI delivers on all 3 research frontiers: a comprehensive 40+ page Capstone Thesis, an IEEE research paper "
        "exposing churn target leakage, and a fully functional production SaaS platform. On behalf of Papasani Suhitha, Gajjala Srithika, "
        "Ala Venkata Veera Ritwik, and M Akshay Sharma, we express our profound gratitude to our guide Prof. N. Lakshmipathi Anantha "
        "and the School of Computer Science and Engineering. We are now open for viva defense questions. Thank you!"
    )

    # -------------------------------------------------------------
    # SAVE PPTX
    # -------------------------------------------------------------
    out_pptx = DOCS_DIR / "E_Commerce_Intelligence_Presentation.pptx"
    prs.save(str(out_pptx))
    print(f"Successfully generated Artistic Blue Brushstroke PPTX at: {out_pptx}")
    
    # Copy to Artifact directory
    artifact_pptx = ARTIFACT_DIR / "E_Commerce_Intelligence_Presentation.pptx"
    prs.save(str(artifact_pptx))
    print(f"Copied to artifact directory at: {artifact_pptx}")

if __name__ == "__main__":
    create_deck()
