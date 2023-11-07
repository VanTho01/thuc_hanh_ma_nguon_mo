from numpy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

win = Tk()
win.title('Bộ lọc FFT ')
win.geometry('700x600')
kgt = StringVar()
Label(win, text='Nhập khoảng giá trị', font=('Times New Roman', 13), bg='yellow', fg='black', height=2, relief='solid',
      borderwidth=2, width=30).place(x=250, y=55)
Entry(win, textvariable=kgt, font=('Times New Roman', 14), bg='yellow', fg='black', relief='solid', borderwidth=2,
      width=5).place(x=555, y=55)
def ifft(b):
    t = np.arange(int(b))
    n = np.zeros(int(b), dtype=complex)
    n[40:60] = np.exp(1j * np.random.uniform(0, 2 * np.pi, (20)))
    s = np.fft.ifft(n)
    plt.plot(t, s.real, label='real')
    plt.plot(t, s.imag, '--', label='imaginary')
    plt.legend()
    plt.show()

def button2():
    t = int(kgt.get())
    ifft(t)

Label(win, text='Chọn bộ lọc', font=('Times New Roman', 13), bg='yellow', fg='black', height=2, relief='solid',
      borderwidth=2, width=10).place(x=250, y=105)
Button(win, text = 'fft', command = button2, font=('Times New Roman', 14), bg='yellow', fg='black', relief='solid', borderwidth=2,
      width=5).place(x=355, y=105)
Button(win, text = 'exit', command = exit, font=('Times New Roman', 14), bg='yellow', fg='black', relief='solid', borderwidth=2,
      width=5).place(x=455, y=105)

win.mainloop()
