from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    l_margin: float = 10
    r_margin: float = 10
    def header(self):
        self.set_y(3)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(100,100,100)
        header_right_text = f"TAX YEAR 2022-23"
        self.set_x(-(self.get_string_width(header_right_text) + 8))
        self.cell(self.get_string_width(header_right_text), 10,header_right_text, align="L", border=0, new_x="LMARGIN", new_y="NEXT")
    
    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-12)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # get page width using predefined method
        page_w = self.w
        
        # footer text
        footer_text = "generated by revbook " 
        self.set_text_color(140,140,140)
        self.cell(self.get_string_width(footer_text), 10,footer_text , align="L", border=False, new_x="RIGHT")
        
        # Printing page number:
        page_number_string = f"Page {self.page_no()}/{{nb}}"
        self.set_x(-(self.get_string_width(page_number_string) + 10))
        self.cell(self.get_string_width(page_number_string), 10,page_number_string , align="L", border=False, new_x="RIGHT")
        
        # self.cell(self)
    def left_para(self,heading_name = None, description = None,heading_font_size = 18, desc_font_size = 9, border_value = 0, head_style = "", desc_style = ''):
        # pdf.set_text_color(100,100,100)
        header_right_text = heading_name
        if header_right_text:
            self.set_font("helvetica", head_style, heading_font_size)
            self.set_x(self.l_margin)
            self.cell(self.get_string_width(header_right_text), 10,header_right_text, align="L", border=border_value, new_x="LMARGIN", new_y="NEXT")
        
        if description:
            self.set_font("helvetica", desc_style, desc_font_size)
            description_text = description
            # self.set_x(pdf.l_margin)
            self.cell((self.w//2) - ((self.l_margin*2) + self.r_margin),5,description_text, align="L", border=border_value, new_x="LMARGIN", new_y="NEXT")
    def right_para(self,heading_name = None, description = None,heading_font_size = 18, desc_font_size = 9, border_value = 0, head_style = "", desc_style = ''):
        # pdf.set_text_color(100,100,100)
        self.set_x((self.w//2)+ (self.l_margin//2))
        header_right_text = heading_name
        if header_right_text:
            self.set_font("helvetica", head_style, heading_font_size)
            rr = (self.w//2)+ (self.l_margin//2)
            self.cell(self.get_string_width(header_right_text), 10,header_right_text, align="L", border=border_value, new_x="LEFT", new_y="NEXT")
        
        if description:
            self.set_font("helvetica", desc_style, desc_font_size)
            description_text = description
            # self.set_x(pdf.l_margin)
            self.cell((self.w//2) - ((self.l_margin*2) + self.r_margin),5,description_text, align="L", border=border_value, new_x="LMARGIN", new_y="NEXT")    

pdf = PDF('L', 'mm','Letter')
# pdf.set_left_margin(10)
# pdf.set_right_margin(10)
pdf.add_page()

# must set the cursor y-position separately before the left_para method for new right para (x position is already set in the method)
pdf.set_y(10) # sets the position from TOP of the page (from the bottom of page if value is negative)

pdf.left_para("Capital gains summary", "Summary of your profit and loss from crypto disposals/sales/trades.")
pdf.left_para( description=" ", border_value=1) # for spacing below the last cell
pdf.left_para( description="..", border_value=1)
pdf.left_para( description="...", border_value=1)
pdf.left_para( description="....", border_value=1)



pdf.left_para(heading_name="Number of disposals", description="Number of taxable events during the year - this number may be higher than ", heading_font_size=12, head_style="B")
pdf.left_para( description="Summary of your profit and loss from crypto disposals/sales/trades.")

pdf.left_para(heading_name="Number of disposals", description="Number of taxable events during the year - this number may be higher than ", heading_font_size=12, head_style="B")
pdf.left_para( description="Summary of your profit and loss from crypto disposals/sales/trades.")

pdf.left_para(heading_name="Number of disposals", description="Number of taxable events during the year - this number may be higher than ", heading_font_size=12, head_style="B")
pdf.left_para( description="Summary of your profit and loss from crypto disposals/sales/trades.")


# set the cursor y-position separately before the right_para method for new right para (x position is already set in the method)
pdf.set_y(10)  # sets the position from TOP of the page (from the bottom of page if value is negative)

pdf.right_para(heading_name="Number of disposals", description="Number of taxable events during the year - this number may be higher than ", heading_font_size=12, head_style="B")
pdf.right_para( description="Summary of your profit and loss from crypto disposals/sales/trades.")

pdf.right_para( description=" ", border_value=1) # for spacing below the last cell
pdf.right_para( description="..", border_value=1)
pdf.right_para( description="...", border_value=1)
pdf.right_para( description="....", border_value=1)

pdf.output("newrev.pdf")
print("File saved")