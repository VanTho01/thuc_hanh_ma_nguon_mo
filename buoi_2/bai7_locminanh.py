import cv2
from tkinter import filedialog
from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage
import numpy as np

win = Tk()
win.title('Lam min anh')
win.geometry('800x800')

def Destroy():
    file_path = 'edit_image.jpg'
    img = Image.open(file_path)
    img = PhotoImage(img)
    image = Label(win, image = img, 
               borderwidth=1)
    image.place(x = 300, y = 210)

def open_file():
    file_path = filedialog.askopenfilename()
    input.delete("1.0", "end")
    input.insert(INSERT, file_path)
    image = cv2.imread(file_path)
    cv2.imwrite('edit_image.jpg', image)
def anh_goc():
    file_path = input.get("1.0", "end").strip()
    img = Image.open(file_path)
    img = PhotoImage(img)
    image = Label(win, image = img, 
               borderwidth=1, 
               relief = 'solid')
    image.place(x = 300, y = 210)
    image.image = img
def anh_chinh_sua():
    file_path = 'edit_image.jpg'
    img = Image.open(file_path)
    img = PhotoImage(img)
    image = Label(win, image = img, 
               borderwidth=1, 
               relief = 'solid')
    image.place(x = 300, y = 210)
    image.image = img

def mainFunction():
    file_path = 'edit_image.jpg'
    image = cv2.imread(file_path)
    image = cv2.resize(image,(0, 0), fx = 1, fy = 1)

    #image = cv2.bilateralFilter(image, 15, 90, 90)
    # Áp dụng nâng cao chất lượng ảnh
    # Khử nhiễu ảnh
    image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 6, 20)
    # Thực hiện kéo giãn tương phản
    image = cv2.normalize(image, None, 255, 0, cv2.NORM_MINMAX, cv2.CV_8UC1)
    # Điều chỉnh độ sáng
    image = cv2.convertScaleAbs(image, alpha=1, beta=5)
    # Hiệu chỉnh gamma
    gamma = 1
    lookup_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    image = cv2.LUT(image, lookup_table)
    # Làm sắc nét ảnh
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    image = cv2.filter2D(image, -1, kernel=kernel)

    cv2.imwrite('edit_image.jpg', image)
    img = Image.open('edit_image.jpg')
    img = PhotoImage(img)
    image1 = Label(win, image = img, 
               borderwidth=1, 
               relief = 'solid')
    image1.place(x = 300, y = 210)
    image1.image = img
Label(win, text = 'Lọc mịn ảnh',
           width = 20, 
           borderwidth=1, 
           relief = 'solid',
           font = ('Times new roman', 14), 
           fg = 'black',
           bg = 'white').place(x = 300, y = 2)

Button(win, text = 'Nhập file ảnh',
           width = 20,
           borderwidth = 1,
           bg = 'yellow',
           fg = 'black',
           relief='ridge',
           command = open_file,
           font = ('Times new roman', 13)).place(x = 2, y = 50)
input = Text(win, font = ('Times new roman', 13),
                  relief='solid',
                  width = 60,
                  height= 1)
input.place(x = 200, y = 50)
Button(win, text = 'Làm mịn ảnh',
           width = 20,
           borderwidth = 1,
           bg = 'yellow',
           fg = 'black',
           command = mainFunction,
           relief='ridge',
           font = ('Times new roman', 13)).place(x = 2, y = 90)
Button(win, text = 'Hiển thị ảnh gốc',
           width = 20,
           borderwidth = 1,
           bg = 'yellow',
           fg = 'black',
           command = anh_goc,
           relief='ridge',
           font = ('Times new roman', 13)).place(x = 2, y = 130)
Button(win, text = 'Hiển thị ảnh chỉnh sửa',
           width = 20,
           borderwidth = 1,
           bg = 'yellow',
           fg = 'black',
           command = anh_chinh_sua,
           relief='ridge',
           font = ('Times new roman', 13)).place(x = 200, y = 130)
Button(win, text = 'Exit',
           width = 20,
           borderwidth = 1,
           bg = 'yellow',
           fg = 'black',
           command = exit,
           relief='ridge',
           font = ('Times new roman', 13)).place(x = 2, y = 170)
Button(win, text = 'Xóa ảnh',
           width = 20,
           borderwidth = 1,
           bg = 'yellow',
           fg = 'black',
           command = Destroy,
           relief='ridge',
           font = ('Times new roman', 13)).place(x = 200, y = 90)

win.mainloop()



