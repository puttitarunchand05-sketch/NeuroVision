import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 widescreen slides
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Palette
    BG_DARK = RGBColor(15, 23, 42)        # Deep navy/slate (#0F172A)
    CARD_BG = RGBColor(30, 41, 59)        # Slate 800 (#1E293B)
    CARD_BORDER = RGBColor(51, 65, 85)    # Slate 700 (#334155)
    ACCENT_CYAN = RGBColor(6, 182, 212)   # Cyan 500 (#06B6D4)
    ACCENT_BLUE = RGBColor(59, 130, 246)  # Blue 500 (#3B82F6)
    ACCENT_PURPLE = RGBColor(168, 85, 247)# Purple 500 (#A855F7)
    TEXT_WHITE = RGBColor(248, 250, 252)  # Slate 50 (#F8FAFC)
    TEXT_MUTED = RGBColor(148, 163, 184)  # Slate 400 (#94A3B8)
    TEXT_BODY = RGBColor(226, 232, 240)   # Slate 200 (#E2E8F0)

    blank_layout = prs.slide_layouts[6]

    def set_slide_background(slide):
        bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = BG_DARK
        bg_shape.line.fill.background()
        return bg_shape

    def add_header(slide, title_text, category_text="NEUROVISION • SYNOPSIS PRESENTATION"):
        # Category / breadcrumb tag
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_CYAN
        
        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(26)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE

        # Divider line
        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.65), Inches(11.7), Inches(0.02))
        div.fill.solid()
        div.fill.fore_color.rgb = CARD_BORDER
        div.line.fill.background()

    def add_card(slide, left, top, width, height, title=None, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        
        content_top = top + Inches(0.15)
        content_height = height - Inches(0.3)
        if title:
            tb_title = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), width - Inches(0.5), Inches(0.5))
            p = tb_title.text_frame.paragraphs[0]
            p.text = title
            p.font.size = Pt(16)
            p.font.bold = True
            p.font.color.rgb = ACCENT_CYAN
            content_top = top + Inches(0.7)
            content_height = height - Inches(0.85)
            
        tb = slide.shapes.add_textbox(left + Inches(0.25), content_top, width - Inches(0.5), content_height)
        tf = tb.text_frame
        tf.word_wrap = True
        return tf

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Banner accent glow
    glow = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.0), Inches(11.733), Inches(0.06))
    glow.fill.solid()
    glow.fill.fore_color.rgb = ACCENT_CYAN
    glow.line.fill.background()

    # Sub-header
    tb_sub = s1.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.733), Inches(0.5))
    p = tb_sub.text_frame.paragraphs[0]
    p.text = "SYNOPSIS PRESENTATION • MASTER OF COMPUTER APPLICATIONS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    # Main Project Title
    tb_main = s1.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.8))
    tf_main = tb_main.text_frame
    tf_main.word_wrap = True
    p1 = tf_main.paragraphs[0]
    p1.text = "NeuroVision"
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p2 = tf_main.add_paragraph()
    p2.text = "Intelligent Multimodal Pattern Analysis Using Deep Learning"
    p2.font.size = Pt(24)
    p2.font.bold = False
    p2.font.color.rgb = ACCENT_BLUE

    # Info card Left: Student
    c_stud = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.2), Inches(5.6), Inches(2.2))
    c_stud.fill.solid()
    c_stud.fill.fore_color.rgb = CARD_BG
    c_stud.line.color.rgb = CARD_BORDER
    tf_s = c_stud.text_frame
    tf_s.word_wrap = True
    p = tf_s.paragraphs[0]
    p.text = "PRESENTED BY:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p_name = tf_s.add_paragraph()
    p_name.text = "Candidate Name: [Candidate Name]"
    p_name.font.size = Pt(15)
    p_name.font.color.rgb = TEXT_WHITE
    p_usn = tf_s.add_paragraph()
    p_usn.text = "USN / Roll No: [USN / Roll No]"
    p_usn.font.size = Pt(14)
    p_usn.font.color.rgb = TEXT_MUTED
    p_dept = tf_s.add_paragraph()
    p_dept.text = "Dept of Master of Computer Applications (MCA)"
    p_dept.font.size = Pt(13)
    p_dept.font.color.rgb = TEXT_MUTED

    # Info card Right: Guide & College
    c_guide = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(4.2), Inches(5.6), Inches(2.2))
    c_guide.fill.solid()
    c_guide.fill.fore_color.rgb = CARD_BG
    c_guide.line.color.rgb = CARD_BORDER
    tf_g = c_guide.text_frame
    tf_g.word_wrap = True
    p = tf_g.paragraphs[0]
    p.text = "PROJECT GUIDANCE & INSTITUTION:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p_gname = tf_g.add_paragraph()
    p_gname.text = "Guide: [Guide Name]"
    p_gname.font.size = Pt(15)
    p_gname.font.color.rgb = TEXT_WHITE
    p_gdes = tf_g.add_paragraph()
    p_gdes.text = "Assistant Professor / Faculty Guide"
    p_gdes.font.size = Pt(13)
    p_gdes.font.color.rgb = TEXT_MUTED
    p_inst = tf_g.add_paragraph()
    p_inst.text = "[Institution / College Name]"
    p_inst.font.size = Pt(14)
    p_inst.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 2: ABSTRACT
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Abstract")

    tf2_l = add_card(s2, Inches(0.8), Inches(1.9), Inches(7.5), Inches(5.0), title="Executive Summary")
    p = tf2_l.paragraphs[0]
    p.text = "Rapid expansion of multi-source digital media generates immense volumes of images, videos, and audio streams. Analyzing these modalities manually is computationally prohibitive and prone to inconsistency."
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_BODY
    
    p2 = tf2_l.add_paragraph()
    p2.text = "NeuroVision delivers an end-to-end intelligent multimodal framework integrating Deep Learning, Computer Vision, Audio Signal Processing, and Explainable AI (XAI) within a unified web environment."
    p2.font.size = Pt(14)
    p2.font.color.rgb = TEXT_BODY

    p3 = tf2_l.add_paragraph()
    p3.text = "The platform delivers automated image classification, object localization, frame-level video analysis, and spectrogram-based audio recognition, coupled with visual heatmaps to illuminate decision boundaries."
    p3.font.size = Pt(14)
    p3.font.color.rgb = TEXT_BODY

    tf2_r = add_card(s2, Inches(8.6), Inches(1.9), Inches(3.9), Inches(5.0), title="Key Innovations", border_color=ACCENT_CYAN)
    points = [
        ("Unified Multimodal Platform", "Combines Image, Video, and Audio analysis under one umbrella."),
        ("Explainable AI (XAI)", "Grad-CAM saliency heatmaps verify model trustworthiness."),
        ("Real-Time Visualization", "Bounding boxes, spectrograms, and interactive dashboards."),
        ("Modular Architecture", "Flexible backends ready for transformer & edge scaling.")
    ]
    for idx, (head, desc) in enumerate(points):
        p_h = tf2_r.paragraphs[0] if idx == 0 else tf2_r.add_paragraph()
        p_h.text = f"✔ {head}"
        p_h.font.size = Pt(14)
        p_h.font.bold = True
        p_h.font.color.rgb = ACCENT_CYAN
        p_d = tf2_r.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 3: INTRODUCTION
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Introduction & Motivation")

    cards_s3 = [
        ("The AI Revolution", "AI and Deep Learning have revolutionized pattern recognition, enabling machines to perceive complex digital signals with near-human accuracy across various industry domains.", ACCENT_CYAN),
        ("Siloed Modality Bottleneck", "Most conventional systems specialize exclusively in a single data type (only image or only audio), failing to capture the rich, multimodal nature of real-world events.", ACCENT_BLUE),
        ("The 'Black Box' Problem", "Deep neural networks generate high-confidence predictions without transparent justification, limiting clinical, legal, and enterprise adoption.", ACCENT_PURPLE),
        ("The NeuroVision Solution", "Unifies Computer Vision, Acoustic feature models, and Grad-CAM interpretability into a cohesive, interactive web dashboard.", ACCENT_CYAN)
    ]
    for i, (title, desc, col) in enumerate(cards_s3):
        col_idx = i % 2
        row_idx = i // 2
        x = Inches(0.8 + col_idx * 5.95)
        y = Inches(1.9 + row_idx * 2.55)
        tf = add_card(s3, x, y, Inches(5.65), Inches(2.3), title=title, border_color=col)
        p = tf.paragraphs[0]
        p.text = desc
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_BODY

    # ==========================================
    # SLIDE 4: PROBLEM STATEMENT
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Problem Statement")

    tf4_l = add_card(s4, Inches(0.8), Inches(1.9), Inches(5.7), Inches(5.0), title="Current Industry Challenges", border_color=RGBColor(239, 68, 68))
    challenges = [
        "Fragmented Tools: Image classifiers, video analyzers, and audio processors operate in isolated environments.",
        "Opaque Decisions: Standard neural architectures lack interpretability, hiding reasons behind classifications.",
        "High Operational Overhead: Manual inspection across multiple media formats is labor-intensive and error-prone.",
        "Lack of Confidence Grounding: End users often receive bare labels without probabilistic confidence margins."
    ]
    for idx, c in enumerate(challenges):
        p = tf4_l.paragraphs[0] if idx == 0 else tf4_l.add_paragraph()
        p.text = f"✖ {c}"
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_BODY
        p.space_after = Pt(12)

    tf4_r = add_card(s4, Inches(6.8), Inches(1.9), Inches(5.7), Inches(5.0), title="NeuroVision Response", border_color=RGBColor(34, 197, 94))
    solutions = [
        "Unified Multi-Sensory Pipeline: Supports images, temporal video frames, and audio waveforms in a single web hub.",
        "Transparent Explainable AI: Integrated Grad-CAM generates heatmaps showing exactly which pixel regions triggered the decision.",
        "Automated Feature Extraction: Deep transfer-learning models automate feature mining in real/near-real-time.",
        "Quantified Decision Metrics: Delivers confidence scores, class rankings, and localized bounding coordinates."
    ]
    for idx, s in enumerate(solutions):
        p = tf4_r.paragraphs[0] if idx == 0 else tf4_r.add_paragraph()
        p.text = f"✔ {s}"
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_BODY
        p.space_after = Pt(12)

    # ==========================================
    # SLIDE 5: OBJECTIVES
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Project Objectives")

    objs = [
        ("Multimodal Ingestion", "Process and parse heterogeneous image, video, and audio datasets with robust validation."),
        ("Image Intelligence", "Implement MobileNetV2 / EfficientNet for classification and SSD / YOLO for object detection."),
        ("Video Sequence Analysis", "Deconstruct video streams into keyframes via OpenCV for frame-by-frame entity tracking."),
        ("Audio Pattern Recognition", "Extract Mel-spectrograms using Librosa and apply 2D-CNNs for acoustic signal analysis."),
        ("Explainable AI (XAI)", "Implement Grad-CAM to highlight significant activation regions and explain predictions."),
        ("Interactive Dashboard", "Build an intuitive frontend with bounding boxes, spectrograms, and confidence metrics.")
    ]

    for idx, (otitle, odesc) in enumerate(objs):
        col_idx = idx % 3
        row_idx = idx // 3
        x = Inches(0.8 + col_idx * 3.95)
        y = Inches(1.9 + row_idx * 2.55)
        tf = add_card(s5, x, y, Inches(3.75), Inches(2.35), title=f"0{idx+1}. {otitle}", border_color=ACCENT_CYAN)
        p = tf.paragraphs[0]
        p.text = odesc
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_BODY

    # ==========================================
    # SLIDE 6: LITERATURE SURVEY
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Literature Survey")

    surveys = [
        ("CNNs & Transfer Learning (MobileNet / EfficientNet)", "Howard et al. / Tan & Le", "Demonstrated that depthwise separable convolutions and compound scaling achieve high classification accuracy while significantly reducing computational overhead and memory footprint."),
        ("Real-Time Object Detection (YOLO / SSD)", "Redmon et al. / Liu et al.", "Unified bounding box regression and class probability estimation into single-stage architectures, enabling real-time object detection across video frames."),
        ("Explainable AI & Grad-CAM", "Selvaraju et al. (2017)", "Introduced Gradient-weighted Class Activation Mapping (Grad-CAM), using gradients entering final convolutional layers to generate transparent visual saliency heatmaps."),
        ("Multimodal Deep Learning", "Ngiam et al. / Baltrušaitis et al.", "Established that fusing visual and acoustic representations extracts complementary features, overcoming limitations inherent in unimodal recognition models.")
    ]

    for idx, (title, author, finding) in enumerate(surveys):
        col_idx = idx % 2
        row_idx = idx // 2
        x = Inches(0.8 + col_idx * 5.95)
        y = Inches(1.9 + row_idx * 2.55)
        tf = add_card(s6, x, y, Inches(5.65), Inches(2.35), title=title, border_color=ACCENT_BLUE)
        p = tf.paragraphs[0]
        p.text = f"Key Researchers: {author}"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN
        p2 = tf.add_paragraph()
        p2.text = finding
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_BODY

    # ==========================================
    # SLIDE 7: SYSTEM ARCHITECTURE & 6 PHASES
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Proposed Methodology & Architecture")

    phases = [
        ("Phase 1", "Data Acquisition", "Upload & validate image, video, and audio files."),
        ("Phase 2", "Preprocessing", "Resize, normalize & generate Mel-spectrograms."),
        ("Phase 3", "Model Pipeline", "CNN, YOLO/SSD, Librosa audio feature extraction."),
        ("Phase 4", "Multimodal & XAI", "Fusion layer & Grad-CAM visual heatmaps."),
        ("Phase 5", "Web Dashboard", "Interactive UI, charts, bounding boxes & logs."),
        ("Phase 6", "Testing & Eval", "Evaluate Accuracy, F1-Score, FPS & latency.")
    ]

    for i, (p_num, p_title, p_desc) in enumerate(phases):
        x = Inches(0.8 + i * 1.98)
        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.1), Inches(1.82), Inches(4.7))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = ACCENT_CYAN if i % 2 == 0 else ACCENT_PURPLE
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        p0 = tf.paragraphs[0]
        p0.text = p_num
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = ACCENT_CYAN if i % 2 == 0 else ACCENT_PURPLE
        
        p1 = tf.add_paragraph()
        p1.text = p_title
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_WHITE
        p1.space_after = Pt(14)

        p2 = tf.add_paragraph()
        p2.text = p_desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 8: MODALITY DEEP DIVE
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "Modality-Specific Processing Pipelines")

    modalities = [
        ("1. Image Intelligence", ACCENT_CYAN, [
            "Classification: MobileNetV2 / EfficientNet extracts global semantic visual features.",
            "Object Detection: YOLO / SSD identifies, localizes, and labels multiple instances.",
            "Output: Class probabilities, bounding box coordinates, and detection labels."
        ]),
        ("2. Video Temporal Stream", ACCENT_BLUE, [
            "Frame Ingestion: OpenCV performs dynamic keyframe sampling & temporal segmentation.",
            "Tracking: Inter-frame object persistence and motion trend identification.",
            "Output: Temporal incident timeline, cumulative entity counts, and frame logs."
        ]),
        ("3. Audio & Acoustic Stream", ACCENT_PURPLE, [
            "Acoustic Preprocessing: Librosa transforms raw audio waves into Mel-Spectrograms.",
            "Pattern Analysis: 2D Convolutional layers classify audio acoustic fingerprints.",
            "Output: Sound event classification, acoustic spectrum plots, confidence rates."
        ])
    ]

    for idx, (m_title, col, items) in enumerate(modalities):
        x = Inches(0.8 + idx * 3.95)
        tf = add_card(s8, x, Inches(1.9), Inches(3.75), Inches(5.0), title=m_title, border_color=col)
        for item_idx, itm in enumerate(items):
            p = tf.paragraphs[0] if item_idx == 0 else tf.add_paragraph()
            p.text = f"• {itm}"
            p.font.size = Pt(13)
            p.font.color.rgb = TEXT_BODY
            p.space_after = Pt(12)

    # ==========================================
    # SLIDE 9: EXPLAINABLE AI (GRAD-CAM)
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "Explainable AI (XAI) & Grad-CAM Workflow")

    tf9_l = add_card(s9, Inches(0.8), Inches(1.9), Inches(6.0), Inches(5.0), title="Why Explainability Matters", border_color=ACCENT_CYAN)
    why_xai = [
        "Unmasking the Black Box: Standard neural nets output predictions without justification; XAI makes the internal reasoning visible.",
        "Grad-CAM Mechanics: Computes gradients of the target class score with respect to feature maps of the final convolutional layer.",
        "Class-Discriminative Saliency: Produces a coarse 2D heatmap highlighting regions positively correlating with the model's decision.",
        "Error Analysis & Bias Detection: Empowers developers to detect whether the network learned genuine features or spurious background artifacts."
    ]
    for idx, text in enumerate(why_xai):
        p = tf9_l.paragraphs[0] if idx == 0 else tf9_l.add_paragraph()
        p.text = f"✔ {text}"
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_BODY
        p.space_after = Pt(10)

    tf9_r = add_card(s9, Inches(7.1), Inches(1.9), Inches(5.4), Inches(5.0), title="Visual Pipeline Flow", border_color=ACCENT_PURPLE)
    steps_xai = [
        "Step 1: Input Image / Video Frame uploaded",
        "Step 2: Deep Convolutional forward pass",
        "Step 3: Target Class Logit identified",
        "Step 4: Backpropagation to Final Conv Layer",
        "Step 5: Guided Weight Averaging & ReLU filtering",
        "Step 6: Color Heatmap Superimposed on Input"
    ]
    for idx, step in enumerate(steps_xai):
        p = tf9_r.paragraphs[0] if idx == 0 else tf9_r.add_paragraph()
        p.text = step
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(14)

    # ==========================================
    # SLIDE 10: WEB DASHBOARD & USER INTERFACE
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, "Interactive Web Dashboard Features")

    dash_features = [
        ("Multimodal Upload Hub", "Unified drag-and-drop workspace supporting PNG, JPG, MP4, AVI, WAV, and MP3 files with instant client-side validation."),
        ("Real-Time Visual Canvas", "Renders detected objects bounded by dynamic bounding boxes, accompanied by class tags and confidence scores."),
        ("Interactive XAI Viewer", "Side-by-side or overlay slider view allowing users to toggle Grad-CAM attention heatmaps over original visual media."),
        ("Acoustic Spectrogram Viewer", "Visualizes frequency and amplitude distribution over time with interactive audio player synchronicity."),
        ("Telemetry & Performance Metrics", "Displays inference latency (ms), device hardware utilization (CPU/GPU), and confidence percentile breakdown."),
        ("Historical Analytics Log", "Stores past inference queries, facilitating longitudinal pattern comparison and report export.")
    ]

    for idx, (ftitle, fdesc) in enumerate(dash_features):
        col_idx = idx % 2
        row_idx = idx // 2
        x = Inches(0.8 + col_idx * 5.95)
        y = Inches(1.9 + row_idx * 1.65)
        tf = add_card(s10, x, y, Inches(5.65), Inches(1.5), title=ftitle, border_color=CARD_BORDER)
        p = tf.paragraphs[0]
        p.text = fdesc
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_BODY

    # ==========================================
    # SLIDE 11: HARDWARE & SOFTWARE REQUIREMENTS
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, "Technical System Requirements")

    tf11_l = add_card(s11, Inches(0.8), Inches(1.9), Inches(5.7), Inches(5.0), title="Software Specifications", border_color=ACCENT_CYAN)
    sw_reqs = [
        ("Operating System", "Windows 10/11 or Ubuntu Linux"),
        ("Core Language", "Python 3.9+ / Modern JavaScript (ES6+)"),
        ("Deep Learning Framework", "PyTorch / TensorFlow 2.x"),
        ("Computer Vision & Media", "OpenCV, Pillow"),
        ("Audio Signal Processing", "Librosa, SciPy, SoundFile"),
        ("Explainable AI", "Grad-CAM / PyTorch-Grad-CAM"),
        ("Backend Web Framework", "Flask / FastAPI"),
        ("Frontend Technologies", "React.js, HTML5, CSS3, Tailwind CSS")
    ]
    for idx, (label, val) in enumerate(sw_reqs):
        p = tf11_l.paragraphs[0] if idx == 0 else tf11_l.add_paragraph()
        p.text = f"• {label}: {val}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_BODY
        p.space_after = Pt(6)

    tf11_r = add_card(s11, Inches(6.8), Inches(1.9), Inches(5.7), Inches(5.0), title="Hardware Specifications", border_color=ACCENT_BLUE)
    hw_reqs = [
        ("Processor (CPU)", "Intel Core i5 / AMD Ryzen 5 or higher"),
        ("System Memory (RAM)", "8 GB minimum (16 GB recommended)"),
        ("Graphics (GPU)", "NVIDIA GeForce GTX/RTX (CUDA support) recommended for fast inference"),
        ("Storage Drive", "256 GB SSD or higher for model weights & media cache"),
        ("Audio Hardware", "Standard Sound Card / Speakers / Microphone for audio verification"),
        ("Network Connectivity", "Broadband internet connection for pretrained weight downloads")
    ]
    for idx, (label, val) in enumerate(hw_reqs):
        p = tf11_r.paragraphs[0] if idx == 0 else tf11_r.add_paragraph()
        p.text = f"• {label}: {val}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_BODY
        p.space_after = Pt(6)

    # ==========================================
    # SLIDE 12: EXPECTED OUTCOMES & CONCLUSION
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)
    add_header(s12, "Expected Outcomes & Conclusion")

    tf12_l = add_card(s12, Inches(0.8), Inches(1.9), Inches(5.7), Inches(5.0), title="Expected Outcomes", border_color=ACCENT_CYAN)
    outcomes = [
        "A fully functional web-based multimodal deep learning analysis suite.",
        "Accurate classification and multi-object detection across images and videos.",
        "Robust acoustic pattern recognition using transformed Mel-spectrograms.",
        "Transparent prediction rationale enabled through Grad-CAM visual heatmaps.",
        "Low-latency response times with real-time inference feedback."
    ]
    for idx, out in enumerate(outcomes):
        p = tf12_l.paragraphs[0] if idx == 0 else tf12_l.add_paragraph()
        p.text = f"★ {out}"
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_BODY
        p.space_after = Pt(10)

    tf12_r = add_card(s12, Inches(6.8), Inches(1.9), Inches(5.7), Inches(5.0), title="Conclusion & Future Scope", border_color=ACCENT_PURPLE)
    p_con = tf12_r.paragraphs[0]
    p_con.text = "Conclusion:"
    p_con.font.size = Pt(14)
    p_con.font.bold = True
    p_con.font.color.rgb = ACCENT_PURPLE
    p_cbody = tf12_r.add_paragraph()
    p_cbody.text = "NeuroVision bridges the gap between unimodal perception and interpretable AI. By harmonizing computer vision, acoustic feature mining, and Explainable AI within an interactive dashboard, it provides a transparent and versatile platform for multimodal intelligence."
    p_cbody.font.size = Pt(12)
    p_cbody.font.color.rgb = TEXT_BODY
    p_cbody.space_after = Pt(14)

    p_fut = tf12_r.add_paragraph()
    p_fut.text = "Future Scope:"
    p_fut.font.size = Pt(14)
    p_fut.font.bold = True
    p_fut.font.color.rgb = ACCENT_CYAN
    p_fbody = tf12_r.add_paragraph()
    p_fbody.text = "Integration of Vision-Language Transformers (CLIP/LLaVA), real-time edge deployment with TensorRT, cross-modal video-audio anomaly detection, and domain customization for healthcare and surveillance."
    p_fbody.font.size = Pt(12)
    p_fbody.font.color.rgb = TEXT_BODY

    # ==========================================
    # SLIDE 13: THANK YOU SLIDE
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13)

    tb_ty = s13.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(11.733), Inches(2.0))
    p_ty = tb_ty.text_frame.paragraphs[0]
    p_ty.text = "THANK YOU"
    p_ty.alignment = PP_ALIGN.CENTER
    p_ty.font.size = Pt(56)
    p_ty.font.bold = True
    p_ty.font.color.rgb = ACCENT_CYAN

    tb_q = s13.shapes.add_textbox(Inches(0.8), Inches(3.6), Inches(11.733), Inches(1.0))
    p_q = tb_q.text_frame.paragraphs[0]
    p_q.text = "Questions & Answers"
    p_q.alignment = PP_ALIGN.CENTER
    p_q.font.size = Pt(24)
    p_q.font.color.rgb = TEXT_WHITE

    tb_foot = s13.shapes.add_textbox(Inches(0.8), Inches(4.6), Inches(11.733), Inches(1.0))
    p_f = tb_foot.text_frame.paragraphs[0]
    p_f.text = "NeuroVision: Intelligent Multimodal Pattern Analysis Using Deep Learning"
    p_f.alignment = PP_ALIGN.CENTER
    p_f.font.size = Pt(14)
    p_f.font.color.rgb = TEXT_MUTED

    output_path = r"d:\MY PROJECT\neurovision\NeuroVision_Synopsis_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully at: {output_path}")

if __name__ == "__main__":
    create_deck()
