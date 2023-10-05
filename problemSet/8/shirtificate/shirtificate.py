from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.add_page()
        self.set_title("CS50 Shirtificate")
        self.set_font("helvetica", "", 50)
        self.cell(0, 60, self.title, new_x="LMARGIN", new_y="NEXT", align="C")
        self.image("shirtificate.png", w=self.epw)
        self.print_name(name)
        self.output("shirtificate.pdf")

    def print_name(self, name):
        self.set_font("helvetica", "", 25)
        self.set_text_color(255, 255, 255)
        self.set_y(-155)
        self.cell(80)
        self.cell(30, -10, f"{name} took CS50", align="C")


name = input("Name: ")
pdf = PDF(name)
