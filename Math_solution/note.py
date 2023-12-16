import sympy as sym
from customtkinter import *
from tkinter import messagebox

class calLimit:
    def __init__(self, win):
        self.win = win
        win.configure(fg_color = '#98f5d0')
        CTkLabel(win, text = "Tính giới hạn hàm số", font = ('Times new roman', 20), fg_color = '#42dfed', text_color = 'Black', width = 174, height = 46, corner_radius=8, justify = 'center').place(x = 151, y = 2)
        win.geometry('475x336')

        CTkLabel(win, corner_radius=8, text = "Chọn Cận", font = ('Times new roman', 15), fg_color = '#C59FF5', text_color = 'Black', width = 86, height = 27).place(x = 53, y = 104)

        self.selected_option = StringVar()
        self.selected_option.set('-')
        self.options = ['-','+']
        self.option_menu = CTkOptionMenu(win, corner_radius = 6, variable = self.selected_option,  values = self.options, hover = True, button_hover_color = '#4287f5', text_color = 'black', width = 51, height = 27)
        self.option_menu.place(x = 282, y = 104)

        self.radio_var1 = StringVar()
        self.radio_var1.set('cận 1 phía')
        self.options2 = ['cận 1 phía', 'cận 2 phía']
        self.can_value = CTkOptionMenu(win, corner_radius= 6, variable = self.radio_var1,  values = self.options2, hover = True, button_hover_color = '#4287f5', text_color = 'black', width = 106, height = 27)
        self.can_value.place(x = 152, y = 104)

        self.expression_label = CTkLabel(win, corner_radius = 7, text = "Hàm f(x)", font = ('Times new roman', 15), fg_color = '#C59FF5', text_color = 'Black', width = 86, height = 27)
        self.expression_label.place(x = 53, y = 62)
        self.expression_entry = CTkEntry(win, corner_radius=6, font = ('Times new roman', 15), text_color = 'Black', width = 270, height = 28, placeholder_text= 'Example: (4*x**3)/(5*x+5*x**2)')
        self.expression_entry.place(x = 152, y = 62)

        self.output = CTkTextbox(win, corner_radius = 6, font = ('Times New Roman', 15), height = 117, width = 270)
        self.output.configure(text_color = 'black', fg_color = "white")
        self.output.place(x = 152, y = 189)

        #expression = expression_entry.get()
        self.x0 = StringVar()
        CTkLabel(win, corner_radius= 7, text = "Giá trị limit", font = ('Times new roman', 15), fg_color = '#C59FF5', text_color = 'Black', width = 86, height = 27).place(x = 53, y = 147)
        CTkEntry(win, corner_radius= 6, textvariable = self.x0, font = ('Times new roman', 15), text_color = 'Black', fg_color = 'white', width = 106, height = 27).place(x = 152, y = 147)
        #type_can = on_radio_button_select()

        self.limit_button = CTkButton(win, corner_radius = 7, text = "Kết Quả", command = self.compute_Limit, font = ('Times new roman', 15), fg_color = '#C59FF5', text_color = 'Black', width = 86, height = 53, hover = True, hover_color='#37a4de', border_color = '#37a4de', border_width = 3)
        self.limit_button.place(x = 53, y = 189)
        self.exit_button = CTkButton(win, corner_radius = 7, text = "Thoát", command = exit, font = ('Times new roman', 15), fg_color = '#C59FF5', text_color = 'Black', width = 86, height = 53, hover = True, hover_color='#37a4de', border_color = '#37a4de', border_width = 3)
        self.exit_button.place(x = 53, y = 253)
    def compute_Limit(self):
        try:
            self.output.delete("1.0", "end")
            type_can = self.radio_var1.get()
            x = sym.symbols('x')
            expression = self.expression_entry.get()
            if (str(type_can) == 'cận 1 phía'):
                integral = sym.limit(expression, x, int(self.x0.get()), str(self.selected_option.get()))
                text="Giới hạn của hàm số: " + str(integral)
                self.output.insert(INSERT, text)
            if (str(type_can) == 'cận 2 phía'):
                integral = sym.limit(expression, x, int(self.x0.get()))
                text="Giới hạn của hàm số: " + str(integral)
                self.output.insert(INSERT, text)
        except:
            messagebox.showerror('Error', 'Kiểm tra lại đầu vào!')

if __name__ == "__main__":
    win = CTk()
    app = calLimit(win)
    win.mainloop()
