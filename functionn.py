from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, HRFlowable)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import KeepTogether

OUTPUT = "/mnt/user-data/outputs/GATE_CS_StudyPlan_2027.pdf"

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm
)

# Colors
DARK_BLUE = colors.HexColor("#1A237E")
MED_BLUE  = colors.HexColor("#1565C0")
LIGHT_BLUE= colors.HexColor("#E3F2FD")
ORANGE    = colors.HexColor("#E65100")
LIGHT_ORG = colors.HexColor("#FFF3E0")
GREEN     = colors.HexColor("#1B5E20")
LIGHT_GRN = colors.HexColor("#E8F5E9")
RED       = colors.HexColor("#B71C1C")
LIGHT_RED = colors.HexColor("#FFEBEE")
GRAY      = colors.HexColor("#424242")
LIGHT_GRY = colors.HexColor("#F5F5F5")
WHITE     = colors.white

styles = getSampleStyleSheet()

def sty(name, **kw):
    s = styles[name].clone(name + str(id(kw)))
    for k, v in kw.items():
        setattr(s, k, v)
    return s

title_style   = sty('Title',   fontSize=22, textColor=WHITE,    alignment=TA_CENTER, spaceAfter=4)
sub_style     = sty('Normal',  fontSize=11, textColor=LIGHT_BLUE,alignment=TA_CENTER, spaceAfter=2)
h1_style      = sty('Heading1',fontSize=14, textColor=WHITE,    spaceAfter=4, spaceBefore=4)
h2_style      = sty('Heading2',fontSize=12, textColor=DARK_BLUE, spaceAfter=3, spaceBefore=6)
h3_style      = sty('Heading3',fontSize=10, textColor=ORANGE,   spaceAfter=2, spaceBefore=4, fontName='Helvetica-Bold')
body_style    = sty('Normal',  fontSize=9,  textColor=GRAY,     spaceAfter=2, leading=14)
bullet_style  = sty('Normal',  fontSize=9,  textColor=GRAY,     spaceAfter=1, leading=13, leftIndent=12)
small_style   = sty('Normal',  fontSize=8,  textColor=GRAY,     spaceAfter=1, leading=12)
center_style  = sty('Normal',  fontSize=9,  textColor=GRAY,     alignment=TA_CENTER)
bold_style    = sty('Normal',  fontSize=9,  textColor=DARK_BLUE, fontName='Helvetica-Bold', spaceAfter=2)
warn_style    = sty('Normal',  fontSize=9,  textColor=RED,      fontName='Helvetica-Bold', spaceAfter=2)

def colored_box(text, bg=DARK_BLUE, fg=WHITE, size=13, bold=True):
    font = 'Helvetica-Bold' if bold else 'Helvetica'
    s = ParagraphStyle('cb', fontSize=size, textColor=fg, alignment=TA_CENTER,
                       backColor=bg, fontName=font, spaceAfter=6, spaceBefore=6,
                       leading=size+6, borderPadding=8)
    return Paragraph(text, s)

def section_header(text, bg=MED_BLUE):
    s = ParagraphStyle('sh', fontSize=12, textColor=WHITE, alignment=TA_LEFT,
                       backColor=bg, fontName='Helvetica-Bold', spaceAfter=4,
                       spaceBefore=8, leading=18, leftIndent=8, borderPadding=6)
    return Paragraph(text, s)

def info_table(data, col_widths, header_bg=DARK_BLUE, alt_bg=LIGHT_BLUE):
    ts = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), header_bg),
        ('TEXTCOLOR',  (0,0), (-1,0), WHITE),
        ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',   (0,0), (-1,0), 9),
        ('ALIGN',      (0,0), (-1,-1), 'CENTER'),
        ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [WHITE, alt_bg]),
        ('FONTSIZE',   (0,1), (-1,-1), 8),
        ('GRID',       (0,0), (-1,-1), 0.5, colors.HexColor("#BBDEFB")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING',(0,0),(-1,-1), 5),
        ('LEFTPADDING', (0,0),(-1,-1), 6),
        ('RIGHTPADDING',(0,0),(-1,-1), 6),
    ])
    t = Table(data, colWidths=col_widths)
    t.setStyle(ts)
    return t

story = []

# ─── COVER ───────────────────────────────────────────────────────────────────
cover_data = [[colored_box("GATE CS 2027", DARK_BLUE, WHITE, 26)],
              [colored_box("Complete Study Plan & Syllabus", MED_BLUE, WHITE, 14)],
              [Spacer(1, 0.3*cm)],
              [colored_box("July 2025 → January 2027  |  18 Months Roadmap", ORANGE, WHITE, 11)],
              [Spacer(1, 0.2*cm)],
              [colored_box("General Category  |  Target: NIT / IIT", GRAY, WHITE, 10)]]

cover_t = Table(cover_data, colWidths=[17*cm])
cover_t.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,-1), DARK_BLUE),
    ('TOPPADDING',(0,0),(-1,-1),8),
    ('BOTTOMPADDING',(0,0),(-1,-1),8),
    ('ROUNDEDCORNERS',[8]),
]))
story.append(Spacer(1, 1*cm))
story.append(cover_t)
story.append(Spacer(1, 0.6*cm))
#that is sudao code for repo
# Score targets
story.append(section_header("  Target Score vs College"))
tgt_data = [
    ["Target Score", "Expected Rank", "College"],
    ["40-48 marks", "Top 4,000-6,000", "MANIT Bhopal / Lower NITs"],
    ["48-55 marks", "Top 2,000-4,000", "NIT Surathkal / NIT Calicut"],
    ["55-62 marks", "Top 1,500-2,500", "NIT Trichy / NIT Warangal"],
    ["62-70 marks", "Top 800-1,500",   "IIT Guwahati / IIT BHU"],
    ["70-78 marks", "Top 300-700",     "IIT Roorkee / IIT Hyderabad"],
    ["78+ marks",   "Top 50-200",      "IIT Bombay / IIT Delhi"],
]
story.append(info_table(tgt_data, [5*cm, 5.5*cm, 6.5*cm]))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("Teri normal preparation mein 50 marks tak pahunch sakta hai → NIT Warangal/Trichy level realistic hai. Agar dedicated rahe → IIT Guwahati bhi possible.", body_style))
story.append(Spacer(1, 0.4*cm))

# ─── FULL SYLLABUS ────────────────────────────────────────────────────────────
story.append(section_header("  GATE CS Complete Syllabus — Subject-wise"))
story.append(Spacer(1, 0.2*cm))

subjects = [
    {
        "name": "1. Engineering Mathematics",
        "marks": "13-15 marks",
        "color": MED_BLUE,
        "topics": [
            ("Discrete Mathematics", "Propositional & First Order Logic, Sets, Relations, Functions, Partial Orders, Lattice, Groups, Graphs — Connectivity, Matching, Coloring, Combinatorics"),
            ("Linear Algebra", "Matrices, Determinants, System of Linear Equations, Eigenvalues & Eigenvectors, LU Decomposition"),
            ("Calculus", "Limits, Continuity, Differentiability, Maxima/Minima, Mean Value Theorem, Integration, Sequences & Series"),
            ("Probability & Statistics", "Random Variables, Uniform/Normal/Exponential/Poisson Distributions, Mean, Median, Mode, Standard Deviation, Conditional Probability, Bayes Theorem"),
        ]
    },
    {
        "name": "2. Digital Logic",
        "marks": "5-7 marks",
        "color": colors.HexColor("#6A1B9A"),
        "topics": [
            ("Boolean Algebra", "Logic Gates, Minimization — K-Map, Quine-McCluskey"),
            ("Combinational Circuits", "MUX, DEMUX, Encoder, Decoder, Adders, Comparators"),
            ("Sequential Circuits", "Flip-Flops, Counters, Shift Registers, Finite State Machines"),
            ("Number Systems", "Binary, Octal, Hex, BCD, IEEE 754 Floating Point"),
        ]
    },
    {
        "name": "3. Computer Organization & Architecture",
        "marks": "7-9 marks",
        "color": colors.HexColor("#00695C"),
        "topics": [
            ("Machine Instructions", "Addressing Modes, Instruction Formats, ALU Design"),
            ("Memory Hierarchy", "Cache — Direct/Associative/Set-Associative, TLB, Virtual Memory, Paging, Segmentation"),
            ("I/O Organization", "Interrupts, DMA, I/O Interface"),
            ("Pipelining", "Hazards — Data/Control/Structural, Pipeline Performance"),
            ("CPU Design", "Hardwired vs Microprogrammed Control"),
        ]
    },
    {
        "name": "4. Programming & Data Structures",
        "marks": "10-12 marks",
        "color": RED,
        "topics": [
            ("C Programming", "Pointers, Arrays, Structures, Recursion, Parameter Passing, Scope"),
            ("Arrays & Linked Lists", "Operations, Complexity Analysis"),
            ("Stacks & Queues", "Implementation, Applications — Expression Evaluation, BFS"),
            ("Trees", "Binary Trees, BST, AVL, Red-Black, Heaps, B-Trees, Traversals"),
            ("Graphs", "BFS, DFS, Spanning Trees — Prim/Kruskal, Shortest Path — Dijkstra/Bellman-Ford"),
            ("Hashing", "Hash Functions, Collision — Chaining/Open Addressing"),
        ]
    },
    {
        "name": "5. Algorithms",
        "marks": "8-10 marks",
        "color": ORANGE,
        "topics": [
            ("Asymptotic Notation", "Big-O, Theta, Omega — Analysis of Loops & Recursion"),
            ("Searching & Sorting", "Binary Search, Quick/Merge/Heap Sort, Counting Sort"),
            ("Divide & Conquer", "Recurrence Relations — Master Theorem"),
            ("Greedy Algorithms", "Activity Selection, Fractional Knapsack, Huffman Coding"),
            ("Dynamic Programming", "0/1 Knapsack, LCS, LIS, Matrix Chain, Edit Distance, Floyd-Warshall"),
            ("Graph Algorithms", "Topological Sort, Strongly Connected Components — Kosaraju/Tarjan"),
            ("NP Completeness", "P vs NP, NP-Hard, NP-Complete problems, Reductions"),
        ]
    },
    {
        "name": "6. Theory of Computation (TOC)",
        "marks": "8-10 marks",
        "color": colors.HexColor("#1565C0"),
        "topics": [
            ("Regular Languages", "DFA, NFA, epsilon-NFA, Regex, Pumping Lemma"),
            ("Context Free Languages", "CFG, PDA, CNF, Pumping Lemma for CFL"),
            ("Turing Machines", "TM variants, Decidability, Halting Problem, Reducibility"),
            ("Computability", "Recursive & Recursively Enumerable Languages"),
        ]
    },
    {
        "name": "7. Compiler Design",
        "marks": "5-7 marks",
        "color": colors.HexColor("#4E342E"),
        "topics": [
            ("Lexical Analysis", "Tokens, Lexemes, Patterns, LEX tool"),
            ("Parsing", "Top-Down — LL(1), Bottom-Up — LR/SLR/LALR, Parse Trees, Ambiguity"),
            ("Semantic Analysis", "Attribute Grammars, Type Checking, Symbol Table"),
            ("Code Generation", "Intermediate Code — 3AC, DAG, Code Optimization — Peephole/Loop"),
        ]
    },
    {
        "name": "8. Operating Systems",
        "marks": "10-12 marks",
        "color": colors.HexColor("#0D47A1"),
        "topics": [
            ("Processes & Threads", "Process States, PCB, Context Switching, Thread Models"),
            ("CPU Scheduling", "FCFS, SJF, Priority, Round Robin, Multilevel Queue — Gantt Charts"),
            ("Synchronization", "Critical Section, Mutex, Semaphore, Monitors, Deadlock — Detection/Prevention/Avoidance — Banker's"),
            ("Memory Management", "Paging, Segmentation, Page Replacement — FIFO/LRU/Optimal, Thrashing"),
            ("File Systems", "File Allocation — Contiguous/Linked/Indexed, Directory Structure, Disk Scheduling — SSTF/SCAN/C-SCAN"),
        ]
    },
    {
        "name": "9. Databases (DBMS)",
        "marks": "8-10 marks",
        "color": GREEN,
        "topics": [
            ("ER Model", "Entities, Attributes, Relationships, Mapping to Relational Model"),
            ("Relational Model", "Keys — Primary/Foreign/Candidate, Relational Algebra, SQL"),
            ("Normalization", "1NF, 2NF, 3NF, BCNF — Functional Dependencies, Armstrong's Axioms"),
            ("Transactions", "ACID Properties, Serializability, Conflict/View Serializability"),
            ("Concurrency Control", "2PL, Timestamp-based, MVCC"),
            ("Indexing", "B-Trees, B+ Trees, Hashing — Static/Dynamic"),
        ]
    },
    {
        "name": "10. Computer Networks",
        "marks": "8-10 marks",
        "color": colors.HexColor("#880E4F"),
        "topics": [
            ("OSI & TCP/IP Model", "All 7 layers — Functions, Protocols"),
            ("Data Link Layer", "Framing, Error Detection — CRC/Parity, Flow Control — Stop-&-Wait/Go-Back-N/Selective Repeat, MAC — CSMA/CD/CA"),
            ("Network Layer", "IP Addressing, Subnetting, CIDR, Routing — RIP/OSPF/BGP, ICMP, NAT"),
            ("Transport Layer", "TCP — 3-way handshake, Flow/Congestion Control, UDP"),
            ("Application Layer", "HTTP, FTP, DNS, SMTP, DHCP"),
            ("Network Security", "Symmetric/Asymmetric Encryption, Digital Signatures, SSL/TLS"),
        ]
    },
]

for subj in subjects:
    bg = subj["color"]
    light = colors.Color(bg.red, bg.green, bg.blue, alpha=0.08)
    story.append(KeepTogether([
        colored_box(f"{subj['name']}   |   Expected: {subj['marks']}", bg, WHITE, 11),
    ]))
    for topic, detail in subj["topics"]:
        story.append(Paragraph(f"<b>{topic}:</b> {detail}", bullet_style))
    story.append(Spacer(1, 0.3*cm))

story.append(PageBreak())

# ─── 18-MONTH PLAN ────────────────────────────────────────────────────────────
story.append(section_header("  18-Month Study Plan — July 2025 to January 2027"))
story.append(Spacer(1, 0.2*cm))

phases = [
    {
        "phase": "PHASE 1 — Foundation",
        "period": "July 2025 – September 2025 (3 Months)",
        "color": GREEN,
        "daily": "2-3 ghante daily (job ke saath)",
        "months": [
            ("July 2025", "Engineering Mathematics",
             ["Discrete Math — Logic, Sets, Relations, Graph Theory",
              "Linear Algebra — Matrices, Eigenvalues",
              "Practice: 10 PYQ per topic"]),
            ("August 2025", "Digital Logic + COA Part 1",
             ["Boolean Algebra, K-Map, Combinational Circuits",
              "Sequential Circuits, Flip-Flops, FSM",
              "Memory Hierarchy, Cache — direct/associative"]),
            ("September 2025", "COA Part 2 + C Programming",
             ["Pipelining, Virtual Memory, I/O, DMA",
              "C — Pointers, Recursion, Structures",
              "Revision: Phase 1 full + 20 PYQ mixed"]),
        ]
    },
    {
        "phase": "PHASE 2 — Core CS",
        "period": "October 2025 – December 2025 (3 Months)",
        "color": MED_BLUE,
        "daily": "3-4 ghante daily",
        "months": [
            ("October 2025", "Data Structures",
             ["Arrays, Linked Lists, Stacks, Queues",
              "Trees — BST, AVL, Heaps, B-Trees",
              "Graphs — BFS, DFS, Spanning Trees, Shortest Path",
              "Hashing — all collision techniques"]),
            ("November 2025", "Algorithms",
             ["Sorting — all O(nlogn) sorts",
              "Divide & Conquer — Master Theorem",
              "Greedy + DP — 15 standard problems",
              "NP Completeness — concept + examples"]),
            ("December 2025", "TOC",
             ["DFA, NFA, Regex, Pumping Lemma",
              "CFG, PDA, CNF",
              "Turing Machines, Decidability, Halting Problem",
              "Revision: Phase 2 + 30 PYQ"]),
        ]
    },
    {
        "phase": "PHASE 3 — Systems",
        "period": "January 2026 – March 2026 (3 Months)",
        "color": ORANGE,
        "daily": "3-4 ghante daily",
        "months": [
            ("January 2026", "Operating Systems",
             ["Process Management, Scheduling algorithms with Gantt",
              "Synchronization — Semaphore, Deadlock — Banker's",
              "Memory — Paging, Page Replacement"]),
            ("February 2026", "DBMS",
             ["ER Model, Relational Algebra, SQL queries",
              "Normalization — 1NF to BCNF with examples",
              "Transactions, Concurrency Control, Indexing"]),
            ("March 2026", "Compiler Design",
             ["Lexical Analysis, LL(1) parsing, LR parsing",
              "Attribute Grammars, Intermediate Code",
              "Revision: Phase 3 full"]),
        ]
    },
    {
        "phase": "PHASE 4 — Networks + Revision",
        "period": "April 2026 – June 2026 (3 Months)",
        "color": colors.HexColor("#6A1B9A"),
        "daily": "4-5 ghante daily",
        "months": [
            ("April 2026", "Computer Networks",
             ["OSI model — all layers in detail",
              "IP addressing, Subnetting practice — 20+ sums",
              "TCP/IP — 3-way handshake, Flow Control",
              "Routing Protocols, DNS, HTTP, Security"]),
            ("May 2026", "Full Syllabus Revision Round 1",
             ["Weak subjects — extra time",
              "Previous Year Questions — 2015 to 2022 full papers",
              "Error log maintain karo — mistakes track karo"]),
            ("June 2026", "Full Syllabus Revision Round 2",
             ["All formula sheets ready karo",
              "Topic-wise PYQ — 50+ per subject",
              "Mock test weekly — full 3hr paper"]),
        ]
    },
    {
        "phase": "PHASE 5 — Mock Test Intensive",
        "period": "July 2026 – October 2026 (4 Months)",
        "color": RED,
        "daily": "5-6 ghante daily — full mock focus",
        "months": [
            ("July 2026", "Mock Tests — Week 1-4",
             ["2 full mocks per week — GO Institute / Made Easy",
              "Each mock ke baad 2 din analysis",
              "Weak areas identify karo"]),
            ("August 2026", "Mock Tests + Weak Area Fix",
             ["3 mocks per week",
              "Specific weak topics — targeted revision",
              "Speed improvement — 3hr mein 65 questions"]),
            ("September 2026", "Intense Mock Phase",
             ["Daily 1 mock or section test",
              "Time management practice",
              "Standard deviation < 5 marks across mocks"]),
            ("October 2026", "Final Revision",
             ["All PYQs from 2010-2023 complete",
              "Formula sheet final review",
              "Exam strategy — attempt order, time per section"]),
        ]
    },
    {
        "phase": "PHASE 6 — Final Prep",
        "period": "November 2026 – January 2027 (3 Months)",
        "color": DARK_BLUE,
        "daily": "4-5 ghante — smart revision, no new topics",
        "months": [
            ("November 2026", "Light Revision",
             ["Only formula sheets + PYQ",
              "No new topics — consolidate only",
              "Sleep schedule fix karo — 7-8 hrs mandatory"]),
            ("December 2026", "Pre-Exam Prep",
             ["2 mocks per week — maintain score",
              "Admit card, center visit",
              "Confidence building"]),
            ("January 2027", "EXAM MONTH",
             ["Last week — only light revision",
              "GATE 2027 — typically 1st-2nd week of Feb",
              "Result March 2027 — NIT/IIT counseling April-May"]),
        ]
    },
]

for phase in phases:
    story.append(colored_box(f"{phase['phase']}  |  {phase['period']}", phase["color"], WHITE, 11))
    story.append(Paragraph(f"Daily target: {phase['daily']}", bold_style))
    for month, topic, points in phase["months"]:
        story.append(Paragraph(f"<b>{month} — {topic}</b>", h3_style))
        for p in points:
            story.append(Paragraph(f"• {p}", bullet_style))
    story.append(Spacer(1, 0.3*cm))

story.append(PageBreak())

# ─── RESOURCES ────────────────────────────────────────────────────────────────
story.append(section_header("  Best Free Resources — Subject-wise"))
story.append(Spacer(1, 0.2*cm))

res_data = [
    ["Subject", "Best Resource", "Where"],
    ["Eng. Mathematics", "NPTEL Discrete Math + Calculus", "nptel.ac.in (Free)"],
    ["Digital Logic", "Neso Academy YouTube", "YouTube (Free)"],
    ["COA", "Hamacher Book + GO Classes", "Pdf + YouTube"],
    ["DSA + Algorithms", "Striver A2Z Sheet + Abdul Bari", "takeuforward.org + YouTube"],
    ["TOC", "Dexter Kozen Book + Neso", "Pdf + YouTube"],
    ["Compiler Design", "Aho Ullman (Dragon Book) + GO", "Pdf + YouTube"],
    ["OS", "Galvin Book + Gate Smashers", "Pdf + YouTube"],
    ["DBMS", "Korth Book + Knowledge Gate", "Pdf + YouTube"],
    ["Networks", "Forouzan Book + Gate Smashers", "Pdf + YouTube"],
    ["PYQ Practice", "GO Institute — gatecse.in", "gatecse.in (Free)"],
    ["Mock Tests", "Made Easy / GO Rank Predictor", "Online"],
    ["Notes", "Handwritten Notes — Zeal Institute", "Telegram / YouTube"],
]
story.append(info_table(res_data, [4.5*cm, 6*cm, 6.5*cm]))
story.append(Spacer(1, 0.4*cm))

# ─── DAILY SCHEDULE ────────────────────────────────────────────────────────────
story.append(section_header("  Daily Schedule Template (Job ke saath)"))
story.append(Spacer(1, 0.2*cm))

sched_data = [
    ["Time", "Activity"],
    ["6:00 AM – 8:00 AM", "GATE Study — Theory / New Topic"],
    ["8:00 AM – 9:00 AM", "Getting ready + commute"],
    ["9:00 AM – 6:00 PM", "Job / Work"],
    ["6:00 PM – 7:00 PM", "Rest / Dinner"],
    ["7:00 PM – 9:00 PM", "GATE Study — Practice Problems / PYQ"],
    ["9:00 PM – 10:00 PM", "Revision of today's topic"],
    ["10:00 PM – 6:00 AM", "Sleep (8 hours — mandatory)"],
]
story.append(info_table(sched_data, [7*cm, 10*cm], header_bg=GREEN))
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph("Weekend: 6-8 ghante study — backlog clear karo + mock tests", bold_style))
story.append(Spacer(1, 0.4*cm))

# ─── 2027 vs 2028 ────────────────────────────────────────────────────────────
story.append(section_header("  Tera Plan — 2027 attempt, 2028 backup"))
story.append(Spacer(1, 0.2*cm))

plan_data = [
    ["", "GATE 2027 (1st attempt)", "GATE 2028 (2nd attempt — backup)"],
    ["Prep time", "18 months (July 25 – Jan 27)", "Additional 12 months"],
    ["Expected score", "48-60 marks", "60-75 marks"],
    ["Expected rank", "Top 2000-4000", "Top 500-1500"],
    ["Expected college", "NIT Trichy/Warangal/Surathkal", "IIT Guwahati/Roorkee/BHU"],
    ["Strategy", "Foundation strong karo", "Weak areas fix + mock intensive"],
    ["Advantage", "Early entry — 1 year less gap", "Better college — higher package"],
]
story.append(info_table(plan_data, [3.5*cm, 6.5*cm, 7*cm], header_bg=DARK_BLUE))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("Important: 2027 mein agar NIT mil raha ho — JOIN KARO. 2028 ke liye mat ruko sirf IIT ke liye, unless rank bahut kareeb ho.", warn_style))
story.append(Spacer(1, 0.4*cm))

# ─── TIPS ────────────────────────────────────────────────────────────────────
story.append(section_header("  Golden Rules — GATE Crack Karne Ke Liye"))
story.append(Spacer(1, 0.2*cm))

tips = [
    ("Consistency > Intensity", "Daily 2-3 ghante > weekend 10 ghante. Roz padhna zaroori hai."),
    ("PYQ is King", "2010-2023 ke saare previous year questions solve karo — GATE ke 40% questions similar pattern ke hote hain."),
    ("Error Log Banao", "Har galat question ek notebook mein likho. Exam se pehle sirf wahi dekho."),
    ("Formula Sheet", "Har subject ki ek A4 formula sheet banao. Revision mein time bachega."),
    ("Mock Tests Mandatory", "Phase 5 se weekly 2-3 full mocks dena start karo. Score track karo."),
    ("DSA + Algo = 20-22 marks", "Yahi sabse zyada weightage wala section hai. Isme strong hona mandatory hai."),
    ("Sleep & Health", "8 ghante neend mandatory. Tired brain padh nahi sakta — quality > quantity."),
    ("Community", "Telegram groups join karo — GATE CS 2027, GO Institute Discord. Doubts clear hote hain."),
]

for title_t, desc in tips:
    story.append(Paragraph(f"<b>{title_t}:</b> {desc}", bullet_style))

story.append(Spacer(1, 0.4*cm))

# Footer motivational box
story.append(colored_box(
    "Gyan Ganga → NIT/IIT MTech — Yeh possible hai. Sirf consistent reh.",
    DARK_BLUE, WHITE, 12
))
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph("Plan banaya hai — ab execute karna tera kaam hai. All the best!", center_style))

doc.build(story)
print("PDF created successfully!")
