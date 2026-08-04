"""Generate three interview-prep PDFs:
   1. Python_Interview_Questions.pdf  (full syllabus, theory + answers)
   2. Python_Coding_Round.pdf         (coding problems + solutions)
   3. PostgreSQL_Interview_Questions.pdf (concepts + queries)

Run:  python3 generate_pdfs.py
"""

from fpdf import FPDF

from python_questions import PYTHON_SECTIONS
from coding_questions import CODING_QUESTIONS
from postgres_questions import POSTGRES_SECTIONS


# ---- helpers -------------------------------------------------------------

def clean(text):
    """fpdf2 core fonts are latin-1; replace common unicode punctuation."""
    replacements = {
        "’": "'", "‘": "'", "“": '"', "”": '"',
        "–": "-", "—": "-", "…": "...", "→": "->",
        "≤": "<=", "≥": ">=", " ": " ", "•": "*",
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    return text.encode("latin-1", "replace").decode("latin-1")


class InterviewPDF(FPDF):
    def __init__(self, title, subtitle):
        super().__init__(format="A4")
        self.doc_title = title
        self.doc_subtitle = subtitle
        self.set_auto_page_break(auto=True, margin=18)
        self.set_margins(18, 18, 18)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 8, clean(self.doc_title), align="R")
        self.ln(10)
        self.set_text_color(0, 0, 0)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")
        self.set_text_color(0, 0, 0)

    def cover(self, total_count):
        self.add_page()
        self.ln(60)
        self.set_font("Helvetica", "B", 26)
        self.set_text_color(20, 40, 90)
        self.multi_cell(0, 14, clean(self.doc_title), align="C")
        self.ln(6)
        self.set_font("Helvetica", "", 14)
        self.set_text_color(80, 80, 80)
        self.multi_cell(0, 9, clean(self.doc_subtitle), align="C")
        self.ln(10)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(20, 110, 60)
        self.cell(0, 9, f"{total_count} questions with answers", align="C")
        self.ln(20)
        self.set_font("Helvetica", "I", 10)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, "Interview Preparation Guide", align="C")
        self.set_text_color(0, 0, 0)

    def section_title(self, text):
        if self.get_y() > 250:
            self.add_page()
        self.ln(4)
        self.set_fill_color(20, 40, 90)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 13)
        self.multi_cell(0, 9, clean("  " + text), fill=True)
        self.set_text_color(0, 0, 0)
        self.ln(3)

    def question(self, number, q):
        # keep question + start of answer from splitting awkwardly
        if self.get_y() > 245:
            self.add_page()
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(20, 40, 90)
        self.multi_cell(0, 6, clean(f"Q{number}. {q}"))
        self.set_text_color(0, 0, 0)
        self.ln(1)

    def answer(self, a):
        self.set_font("Helvetica", "", 10.5)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 5.5, clean(a))
        self.set_text_color(0, 0, 0)
        self.ln(4)

    def code_block(self, code):
        self.set_font("Courier", "", 9)
        self.set_fill_color(244, 244, 244)
        self.set_text_color(20, 20, 20)
        for line in code.split("\n"):
            line = clean(line) if line else " "
            # crude wrap for very long code lines
            while len(line) > 90:
                self.cell(0, 5, line[:90], fill=True, new_x="LMARGIN", new_y="NEXT")
                line = "    " + line[90:]
            self.cell(0, 5, line, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(4)


# ---- builders ------------------------------------------------------------

def build_python_pdf():
    total = sum(len(qs) for _, qs in PYTHON_SECTIONS)
    pdf = InterviewPDF("Python Interview Questions",
                       "Complete Syllabus - Theory, Concepts & Internals")
    pdf.cover(total)
    n = 0
    for section, questions in PYTHON_SECTIONS:
        pdf.add_page()
        pdf.section_title(section)
        for q, a in questions:
            n += 1
            pdf.question(n, q)
            pdf.answer(a)
    pdf.output("Python_Interview_Questions.pdf")
    return total


def build_coding_pdf():
    total = len(CODING_QUESTIONS)
    pdf = InterviewPDF("Python Coding Round",
                       "Common Coding Problems with Solutions")
    pdf.cover(total)
    pdf.add_page()
    pdf.section_title("Coding Problems & Solutions")
    for i, (title, problem, solution) in enumerate(CODING_QUESTIONS, 1):
        pdf.question(i, title)
        pdf.answer(problem)
        pdf.code_block(solution)
    pdf.output("Python_Coding_Round.pdf")
    return total


def build_postgres_pdf():
    total = sum(len(qs) for _, qs in POSTGRES_SECTIONS)
    pdf = InterviewPDF("PostgreSQL Interview Questions",
                       "Concepts, Queries & Administration")
    pdf.cover(total)
    n = 0
    for section, questions in POSTGRES_SECTIONS:
        pdf.add_page()
        pdf.section_title(section)
        for q, a in questions:
            n += 1
            pdf.question(n, q)
            # SQL-looking answers go into a code block for readability
            if any(tok in a for tok in ("SELECT", "INSERT", "UPDATE", "DELETE",
                                        "CREATE", "ALTER", "WITH", "GRANT")):
                # split prose intro from SQL if present on its own lines
                pdf.code_block(a)
            else:
                pdf.answer(a)
    pdf.output("PostgreSQL_Interview_Questions.pdf")
    return total


if __name__ == "__main__":
    p = build_python_pdf()
    c = build_coding_pdf()
    pg = build_postgres_pdf()
    print(f"Python theory questions : {p}")
    print(f"Coding round questions  : {c}")
    print(f"PostgreSQL questions    : {pg}")
    print(f"TOTAL                   : {p + c + pg}")
    print("Generated:")
    print("  - Python_Interview_Questions.pdf")
    print("  - Python_Coding_Round.pdf")
    print("  - PostgreSQL_Interview_Questions.pdf")
