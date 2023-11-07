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

def fft(a):
    t = np.arange(a)
    f = np.sin(t)*np.cos(t)
    sp = np.fft.fft(f)
    freq = np.fft.fftfreq(t.shape[-1])

    plt.figure(figsize = (12, 6))
    plt.subplot(121)

    plt.stem(freq, np.abs(sp), 'b', markerfmt=" ", basefmt="-b")
    plt.xlabel('Freq (Hz)')
    plt.ylabel('FFT Amplitude |X(freq)|')
    plt.xlim(0, 0.5)

    plt.subplot(122)
    plt.plot(t, ifft(sp), 'r')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()

def button1():
    n = int(kgt.get())
    fft(n)


Label(win, text='Chọn bộ lọc', font=('Times New Roman', 13), bg='yellow', fg='black', height=2, relief='solid',
      borderwidth=2, width=10).place(x=250, y=105)
Button(win, text = 'fft', command = button1, font=('Times New Roman', 14), bg='yellow', fg='black', relief='solid', borderwidth=2,
      width=5).place(x=355, y=105)
Button(win, text = 'exit', command = exit, font=('Times New Roman', 14), bg='yellow', fg='black', relief='solid', borderwidth=2,
      width=5).place(x=455, y=105)

win.mainloop()