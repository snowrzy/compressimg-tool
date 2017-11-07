import tkinter as tk
from PIL import Image
from tkinter import messagebox
import os


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.srcPath = tk.StringVar()
        self.distPath = tk.StringVar()
        self.pack()
        self.create_entry()
        self.create_widgets()

    def create_entry(self):

        self.srclabel = tk.Label(self, text="请输入图片所在文件夹:")
        self.srclabel.pack(side="top")

        self.srcentry = tk.Entry(self, textvariable=self.srcPath, width=50)
        self.srcentry.pack(side="top")

        self.distlabel = tk.Label(self, text="请输入压缩后图片储存位置:")
        self.distlabel.pack(side="top")

        self.distentry = tk.Entry(self, textvariable=self.distPath, width=50)
        self.distentry.pack(side="top")

    def create_widgets(self):
        self.hi_there = tk.Button(self, fg="red", bg="blue")
        self.hi_there["text"] = "点我压缩"
        self.hi_there["width"] = 10
        self.hi_there["command"] = lambda: self.compressImage(self.srcPath.get(), self.distPath.get())
        self.hi_there.pack(side="bottom")

    def say_hi(self):
        print("21312")
        print(self.srcPath.get(), self.distPath.get())

    def compressImage(self, srcPath=None, distPath=None):
        print(srcPath, distPath)
        if type(srcPath) != str:
            messagebox.showinfo('CompressTool', '路径输入有误，请重新输入')
            return
        i = 1
        for filename in os.listdir(srcPath):
            filename.endswith('.txt')
            # 如果不存在目的目录则创建一个，保持层级结构
            if not os.path.exists(distPath):
                os.makedirs(distPath)
                # 拼接完整的文件或文件夹路径
            srcFile = os.path.join(srcPath, filename)
            dstFile = os.path.join(distPath, filename)
            print("Prepare compressing: " + filename)

            # 如果是图片文件就处理
            if os.path.isfile(srcFile) and (
                            srcFile.endswith('.png') or srcFile.endswith('.jpg') or srcFile.endswith('.jpeg')):
                sImg = Image.open(srcFile)
                w, h = sImg.size
                dImg = sImg.resize((int(w / 2), int(h / 2)), Image.ANTIALIAS)  # 设置压缩尺寸和选项，注意尺寸要用括号
                sImg.save(dstFile, optimize=True, quality=70)
                print(filename + " compressed succeeded! Under the folder: " + dstFile)
            # 如果是文件夹就递归
            if os.path.isdir(srcFile):
                self.compressImage(srcFile, dstFile)
        messagebox.showinfo('CompressTool', 'Compression complete')


root = tk.Tk()
root.title("Compress Tool")
root.geometry("550x150")
app = Application(master=root)
app.mainloop()
