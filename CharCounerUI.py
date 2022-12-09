from tkinter import *
from tkinter import font


class Main(Frame):
    """Main window"""

    def __init__(self, parent):

        self.parent = parent
        self.parent.title("Hello there")
        self.parent.configure(bg="#353535")
        self.font = font.Font(family='Helvetica', size=10, weight='bold')
        self.font_button = font.Font(family='Helvetica', size=12, weight='bold')
        self.result = False
        self.dict = {}
        self.text = ''

        self.initUI()

    def initUI(self):
        """Labels"""
        self.label_input = Label(text='Place your text:', bg="#353535", fg='#999999', font=self.font)
        self.label_input.grid(row=1, column=0, sticky=W, rowspan=1, columnspan=1)
        self.label_result = Label(text='Char  Used   %', bg="#353535", fg='#999999', font=self.font)
        self.label_result.grid(row=1, column=3, sticky=W, rowspan=1, columnspan=1)

        """Windows and buttons"""
        self.input_data = Text(self.parent, width=35, fg='#999999', bg="#212121", font=self.font)
        self.input_data.grid(row=2, column=0)

        self.listbox_data = Listbox(self.parent, height=23, width=35, fg='#999999', bg="#212121", font=self.font,
                                    selectmode=SINGLE)
        self.listbox_data.grid(row=2, column=3)

        self.btn_result = Button(self.parent, text='Result', font=self.font_button, fg='#999999', bg="#212121",
                                 activeforeground='#999999', activebackground='#353535', height=3, width=5,
                                 command=self.button_result)
        self.btn_result.grid(row=2, column=2)

        self.btn_clear = Button(self.parent, text='Clear', font=self.font_button, fg='#999999', bg="#212121",
                                activeforeground='#999999', activebackground='#353535', command=self.button_clear)
        self.btn_clear.grid(row=1, column=3)

    def letters(self):
        for char in self.text:
            if char.isalpha():
                char = char.upper()
                if char not in self.dict.keys():
                    self.dict[char] = [0]
                self.dict[char][0] += 1
        self.dict = sorted(self.dict.items(), key=lambda value: value[1], reverse=True)

        self.dict = (dict(self.dict))
        return self.dict

    def percentage_of_usage(self):
        number_of_used_chars = 0
        for value in self.dict.values():
            number_of_used_chars += value[0]
        for key, value in self.dict.items():
            percentage = value[0] / number_of_used_chars * 100
            self.dict[key].append(percentage)
        return self.dict

    def button_result(self):
        if not self.result:
            self.text = self.input_data.get("1.0", END)
            self.letters()
            self.percentage_of_usage()

            for key in self.dict.keys():
                line = f' {key}      {self.dict[key][0]}       {self.dict[key][1]:.2f}%'
                self.listbox_data.insert(END, line)
        if len(self.dict) == 0:
            self.result = False
        else:
            self.result = True

    def button_clear(self):
        self.result = False
        self.text = ''
        self.dict.clear()
        self.input_data.delete("1.0", END)
        self.listbox_data.delete(0, END)


def main():
    root = Tk()
    ex = Main(root)
    root.mainloop()


if __name__ == '__main__':
    main()