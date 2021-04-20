from fpdf import FPDF

pdf_w = 210
pdf_h = 297


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.__lineStart = 0
        self.__prev_lines = 0

    def color_background(self):
        self.set_fill_color(32, 32, 32)
        self.rect(0, 0, pdf_w, pdf_h, 'DF')

    def new_page(self):
        self.add_page()
        self.color_background()

    def headings(self, title, heading_num):
        self.set_xy(30, self.__lineStart)
        title.replace('\n', '')

        fontsize = 0
        color = [255, 255, 255]
        if heading_num == 1:
            fontsize = 28
            if self.__lineStart + 10 < pdf_h - 30:
                self.__lineStart += 10
            else:
                self.new_page()
                self.__lineStart = 0
        elif heading_num == 2:
            fontsize = 24
            if self.__lineStart + 10 < pdf_h - 30:
                self.__lineStart += 10
            else:
                self.new_page()
                self.__lineStart = 0
        elif heading_num == 3:
            fontsize = 18
            if self.__lineStart + 10 < pdf_h - 30:
                self.__lineStart += 10
            else:
                self.new_page()
                self.__lineStart = 0
        elif heading_num == 4:
            fontsize = 15
            if self.__lineStart + 10 < pdf_h - 30:
                self.__lineStart += 10
            else:
                self.new_page()
                self.__lineStart = 0
        elif heading_num == 5 or heading_num == 6:
            fontsize = 13
            color = [170, 170, 170]
            if self.__lineStart + 10 < pdf_h - 30:
                self.__lineStart += 10
            else:
                self.new_page()
                self.__lineStart = 0

        self.set_text_color(color[0], color[1], color[2])
        self.set_font('Arial', 'B', fontsize)
        self.cell(w=pdf_w-60, h=40, align='L', txt=title)

    def normal_text(self, text):
        text.replace('\n', '')
        fontsize = 11
        lines = (len(text) / 90) - 2   # Larger blocks need more spacing, this is the number of lines the last block overran by

        if self.__lineStart + 15 < pdf_h - 30 and self.__prev_lines <= 0:
            self.__lineStart += 15
        elif self.__lineStart + (15 + (self.__prev_lines*5)) < pdf_h - 30:
            self.__lineStart += (15 + (self.__prev_lines*5))
        else:
            self.new_page()
            self.__lineStart = 0

        self.set_xy(30, self.__lineStart)
        self.set_text_color(255, 255, 255)
        self.set_font('Arial', '', fontsize)
        self.multi_cell(w=pdf_w-60, h=5, align='L', txt=text)
        self.__prev_lines = lines

    def snippet(self, text):
        fontsize = 11
        lines = text.count('\n')

        if self.__lineStart + (15 + (self.__prev_lines*5)) < pdf_h - 30:
            self.__lineStart += (15 + (self.__prev_lines * 5))
        else:
            self.new_page()
            self.__lineStart = 0

        self.set_xy(30, self.__lineStart)
        self.set_fill_color(26, 26, 26)
        self.set_text_color(199, 37, 78)
        self.set_font('Arial', '', fontsize)
        self.multi_cell(w=pdf_w - 60, h=5, align='L', txt=text, fill=True)
        self.__prev_lines = lines - 3

