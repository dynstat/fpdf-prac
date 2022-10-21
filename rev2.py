from fpdf import FPDF

class PDF(FPDF):
    l_margin: float = 10
    r_margin: float = 10

    def header(self):
        self.set_y(3)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(100, 100, 100)
        header_right_text = f"TAX YEAR 2022-23"
        self.set_x(-(self.get_string_width(header_right_text) + 8))
        self.cell(self.get_string_width(header_right_text), 10,
                  header_right_text, align="L", border=0, new_x="LMARGIN", new_y="NEXT")

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-12)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # get page width using predefined method
        page_w = self.w

        # footer text
        footer_text = "generated by revbook "
        self.set_text_color(140, 140, 140)
        self.cell(self.get_string_width(footer_text), 10,
                  footer_text, align="L", border=False, new_x="RIGHT")

        # Printing page number:
        page_number_string = f"Page {self.page_no()}/{{nb}}"
        self.set_x(-(self.get_string_width(page_number_string) + 10))
        self.cell(self.get_string_width(page_number_string), 10,
                  page_number_string, align="L", border=False, new_x="RIGHT")

        # self.cell(self)
    def left_para(self, heading_name=None, description=None, value=None, heading_font_size=18, desc_font_size=9, border_value=0, head_style="", desc_style='', head_cell_height=5, desc_cell_height=5):
        # pdf.set_text_color(100,100,100)
        header_left_text = heading_name
        if value:
            self.set_font("helvetica", head_style, heading_font_size)
            self.set_x(self.l_margin)
            self.cell(self.w//2 - 30, head_cell_height, str(value),
                      align="R", border=border_value, new_x="LMARGIN")

        if header_left_text:
            self.set_font("helvetica", head_style, heading_font_size)
            self.set_x(self.l_margin)
            self.cell(self.get_string_width(header_left_text), head_cell_height, header_left_text,
                      align="L", border=border_value, new_x="LMARGIN", new_y="NEXT")

        if description:
            self.set_font("helvetica", desc_style, desc_font_size)
            description_text = description
            # self.set_x(pdf.l_margin)
            self.cell((self.w//2) - ((self.l_margin*2) + self.r_margin), desc_cell_height, description_text,
                      align="L", border=border_value, new_x="LMARGIN", new_y="NEXT")

    def right_para(self, heading_name=None, description=None, value=None, heading_font_size=18, desc_font_size=9, border_value=0, head_style="", desc_style='', head_cell_height=5, desc_cell_height=5):

        # pdf.set_text_color(100,100,100)
        self.set_x((self.w//2) + (self.l_margin//2))
        if value:
            self.set_font("helvetica", head_style, heading_font_size)
            # self.set_x(self.l_margin)
            self.cell(self.w//2 - 30, head_cell_height, str(value),
                      align="R", border=border_value, new_x="LEFT")
        header_right_text = heading_name
        if header_right_text:
            self.set_font("helvetica", head_style, heading_font_size)
            rr = (self.w//2) + (self.l_margin//2)
            self.cell(self.get_string_width(header_right_text), head_cell_height, header_right_text,
                      align="L", border=border_value, new_x="LEFT", new_y="NEXT")

        if description:
            self.set_font("helvetica", desc_style, desc_font_size)
            description_text = description
            # self.set_x(pdf.l_margin)
            self.cell((self.w//2) - ((self.l_margin*2) + self.r_margin), desc_cell_height, description_text,
                      align="L", border=border_value, new_x="LMARGIN", new_y="NEXT")