from sympy import *
from tkinter import *
from tkinter import messagebox

init_printing(use_unicode=True)

win = Tk()
win.title("Giải hệ ptr n ptr n ẩn")
win.geometry('900x900')
win.configure(bg = '#E3F7F2')

Label(win, text = 'Giải hệ phương trình n ẩn', font = ('Times New Roman', 13), bg = 'yellow', fg = 'black', height=2, relief='solid', borderwidth = 2, width = 40).place(x = 250, y = 0)

Label(win, text = ' Kết quả ', font = ('Times New Roman', 13), bg = 'yellow', fg = 'black', height=2, relief='solid', borderwidth = 2, width = 10).place(x = 160, y = 645)
Label(win, text = '', font = ('Times New Roman', 13), bg = 'white', fg = 'black', height=2, relief='solid', borderwidth = 2, width = 70).place(x = 250, y = 645)


sopt = StringVar()
Label(win, text = 'Nhập số phương trình', font = ('Times New Roman', 13), bg = 'yellow', fg = 'black', height=2, relief='solid', borderwidth = 2, width = 30).place(x = 250, y = 55)
Entry(win, textvariable = sopt, font = ('Times New Roman', 14), bg = 'yellow', fg = 'black', relief='solid', borderwidth = 2, width = 5).place(x = 555, y = 55)

a = 'abcdefghijklmnopqrstuvwxyz'
a1 = list(a)
A = []
entries_A = []
B = []
entries_B = []
class Cal:
    def __init__(self, A, entries_A, B, entries_B):
        self.A = A
        self.entries_A = entries_A
        self.B = B
        self.entries_B = entries_B
    def create(self):
        try:
            if (int(sopt.get()) <= 0):
                messagebox.showwarning("CHu y","So phuong trinh phai >0")
            for i in range(int(sopt.get())):
                self.A.append([])
                self.entries_A.append([])
                self.B.append([])
                self.entries_B.append([])
                for j in range(int(sopt.get())):
                    self.A[i].append(StringVar())
                    if (i != 0):
                        Label(win,background = '#E3F7F2', font = ('Times New Roman', 12), text = ' + '+f'x{i} ', width = 3).place(x = 250 + 80*i, y = 110 + 30*j)#grid(row = i, column = j+2)
                    else:
                        Label(win,background = '#E3F7F2', font = ('Times New Roman', 12), text = f'x{i} ', width = 3).place(x = 250 + 80*i, y = 110 + 30*j)#grid(row = i, column = j+2)
                    self.entries_A[i].append(Entry(win, textvariable = self.A[i][j], width=3))
                    self.entries_A[i][j].place(x =280 + 83*j, y = 110 + 30*i)#grid(row=i, column=j+4)
                self.B[i].append(StringVar())
                Label(win,background = '#E3F7F2', font = ('Times New Roman', 12), text = f' = ', width = 3).place( x = 310 + 83*(int(sopt.get())-1), y = 110 + 30*i)#grid(row = i, column = 4)
                self.entries_B[i].append(Entry(win, textvariable = self.B[i][0], width=3))
                self.entries_B[i][0].place(x=200 + 83 * (int(sopt.get())+1), y=110 + 30 * i)
        except:
            messagebox.showwarning("CHu y","Kieu du lieu khong dung!")

    def get_mat_A(self):
        matrix_A = []
        for i3 in range(int(sopt.get())):
            matrix_A.append([])
            for j3 in range(int(sopt.get())):
                if (self.A[i3][j3].get() != ''):
                    matrix_A[i3].append(float(self.A[i3][j3].get()))
                else: 
                    messagebox.showwarning("Thieu du lieu", f'Nhap thieu he so cua {a1[j3]}{i3}')

        return Matrix(matrix_A)

    def get_mat_B(self):
        matrix_B = []
        for i3 in range(int(sopt.get())):
            matrix_B.append([])
            for j3 in range(1):
                if (self.B[i3][j3].get() != ''):
                    matrix_B[i3].append(float(self.B[i3][j3].get()))
                else:
                    messagebox.showwarning("Thieu du lieu", f'Nhap thieu he so cua phuong trinh thu {i3+1}')
        return Matrix(matrix_B)

    def calculate(self):
            try:
                A = Cal.get_mat_A(self)
                B = Cal.get_mat_B(self)
                A_ = A.col_insert(int(sopt.get())-1, B)
                if (A.det() != 0):
                    if (A.rank() != A_.rank()):
                        messagebox.showinfo("Notification", "He phuong trinh vo nghiem")
                    if (A.rank() == A_.rank() and A.rank() == int(sopt.get())):
                        messagebox.showinfo("Notification", "He phuong trinh co nghiem duy nhat")
                        x = A.inv()*B
                        X = x.evalf()
                        print(X)
                        for i in range(int(sopt.get())):
                            Label(win,background = 'white', font = ('Times New Roman', 12), fg = 'black', text = f'x{i} = ', width = 4).place( x = 280 + 83*i, y = 650)#grid(row = i, column = 4)
                            Label(win,background = 'white', font = ('Times New Roman', 12), fg = 'black', text = f'{round(float(X[i]), 1)}' + ', ', width = 4).place( x = 320 + 83*i, y = 650)#grid(row = i, column = 4)
                    if (A.rank() == A_.rank() and A.rank() < int(sopt.get())):
                        messagebox.showinfo("Notification", "He phuong trinh co vo so nghiem")
                else:
                    messagebox.showwarning("Error!", "Ma tran khong kha nghich")
            except:
                messagebox.showwarning("Error!", "Nhap sai!")
def clear():
    Label(win,background = '#E3F7F2', width = 180*int(sopt.get()), height = 20).place( x = 240, y = 100)
    Label(win,background = 'white', width = 70).place( x = 280, y = 650)
    A = []
    entries_A = []
    B = []
    entries_B = []
    cal = Cal(A, entries_A, B, entries_B)

    Button(win, text = 'Create', command = cal.create, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 280, y = 710)
    Button(win, text = 'Exit', command = exit, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 380, y = 710)
    Button(win, text = 'Clear', command = clear, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 480, y = 710)
    Button(win, text = 'Calculate', command = cal.calculate, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 8, height = 2, relief='solid', borderwidth = 2).place(x = 580, y = 710)
    
cal = Cal(A, entries_A, B, entries_B)
Button(win, text = 'Create', command = cal.create, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 280, y = 710)
Button(win, text = 'Exit', command = exit, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 380, y = 710)
Button(win, text = 'Clear', command = clear, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 6, height = 2, relief='solid', borderwidth = 2).place(x = 480, y = 710)
Button(win, text = 'Calculate', command = cal.calculate, font = ('Times new roman', 15), fg = 'black', bg = 'brown', width = 8, height = 2, relief='solid', borderwidth = 2).place(x = 580, y = 710)

win.mainloop()

