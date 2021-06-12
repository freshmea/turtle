# from tkinter import *
# import os
# from tkinter.filedialog import *
#
# es = ""
#
#
# def newFile():
#     top.title("제목없음- 메모장")
#     file = None
#     ta.delete(1.0, END)
#
#
# def openFile():
#     file = askopenfilename(title="파일 선택", filetypes=(("텍스트 파일", "*.txt"), ("모든 파일", "*.*")))
#     top.title(os.path.basename(file) + " - 메모장")
#     ta.delete(1.0, END)
#     f = open(file, "r")
#     ta.insert(1.0, f.read())
#     f.close()
#
#
# def saveFile():
#     f = asksaveasfile(mode="w", defaultextension=".txt")
#     if f is None:
#         return
#     ts = str(ta.get(1.0, END))
#     f.write(ts)
#     f.close()
#
#
# def cut():
#     global es
#     es = ta.get(SEL_FIRST, SEL_LAST)
#     ta.delete(SEL_FIRST, SEL_LAST)
#
#
# def copy():
#     global es
#     es = ta.get(SEL_FIRST, SEL_LAST)
#
#
# def paste():
#     global es
#     ta.insert(INSERT, es)
#
#
# def delete():
#     ta.delete(SEL_FIRST, SEL_LAST)
#
#
# def help():
#     he = Toplevel(top)
#     he.geometry("200x200")
#     he.title("정보")
#     lb = Label(he, text="메모장 버전 1.0\n 파이썬으로 만든 메모장입니다^^")
#     lb.pack()
#
#
# top = Tk()
# top.title("메모장")
# top.geometry("400x400")
#
# ta = Text(top)
# sb = Scrollbar(ta)
# sb.config(command=ta.yview)
# top.grid_rowconfigure(0, weight=1)
# top.grid_columnconfigure(0, weight=1)
# sb.pack(side=RIGHT, fill=Y)
# ta.grid(sticky=N + E + S + W)
#
# file = None
#
# mb = Menu(top)
# fi = Menu(mb, tearoff=0)
# fi.add_command(label="새파일", command=newFile)
# fi.add_command(label="열기", command=openFile)
# fi.add_command(label="저장", command=saveFile)
# fi.add_separator()
# fi.add_command(label="종료", command=top.destroy)
# mb.add_cascade(label="파일", menu=fi)
#
# e = Menu(mb, tearoff=0)
# e.add_command(label="잘라내기", command=cut)
# e.add_command(label="복사", command=copy)
# e.add_command(label="붙이기", command=paste)
# e.add_command(label="삭제", command=delete)
# mb.add_cascade(label="편집", menu=e)
#
# h = Menu(mb, tearoff=0)
# h.add_command(label="메모장 정보", command=help)
# mb.add_cascade(label="도움말", menu=h)
#
# top.config(menu=mb)
#
# top.mainloop()

import tkinter as tk
import tkinter.filedialog as tkf
import os

def domenu():
    pass

def save():
    f = tkf.asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:
        return
    ts = str(text.get(1.0, 'end'))
    f.write(ts)
    f.close()

def openf():
    file = tkf.askopenfilename(title="파일 선택", filetypes=(("텍스트 파일", "*.txt"), ("모든 파일", "*.*")))
    root.title(os.path.basename(file) + " - 메모장")
    text.delete(1.0, 'end')
    f = open(file, "r")
    text.insert(1.0, f.read())
    f.close()


root = tk.Tk()
mb = tk.Menu(root)
fmb = tk.Menu(mb, tearoff=0)
mb.add_cascade(label='파일', menu=fmb)
fmb.add_command(label='새파일', command=domenu)
fmb.add_command(label='불러오기', command=openf)
fmb.add_command(label='저장', command=save)
fmb.add_command(label='다른이름으로 저장', command=domenu)

emb = tk.Menu(mb, tearoff=0)
mb.add_cascade(label='에디트', menu=emb)
emb.add_command(label='복사', command=domenu)
emb.add_command(label='붙여넣기', command=domenu)
emb.add_command(label='반복', command=domenu)
emb.add_command(label='되돌리기', command=domenu)

text = tk.Text(root, height=30, width=80)
text.pack()

root.config(menu=mb)
root.mainloop()
#
# from tkinter import *
#
# def domenu():
#     print("OK")
#
# root = Tk()
# menubar = Menu(root)                                # 윈도우에 메뉴바 추가
# filemenu = Menu(menubar, tearoff=0)                 # 상위 메뉴 탭 항목 추가
# menubar.add_cascade(label="File", menu=filemenu)    # 상위 메뉴 탭 설정
# filemenu.add_command(label="New", command=domenu)   # 항목 추가
# filemenu.add_command(label="Open", command=domenu)
# filemenu.add_command(label="Save", command=domenu)
# filemenu.add_command(label="Save as...", command=domenu)
# filemenu.add_separator()                            # 분리선 추가
# filemenu.add_command(label="Exit", command=root.quit)
#
# editmenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Edit", menu=editmenu)
# editmenu.add_command(label="Copy", command=domenu)
# editmenu.add_command(label="Paste", command=domenu)
# editmenu.add_separator()
# editmenu.add_command(label="Delete", command=domenu)
#
# helpmenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Help", menu=helpmenu)
# helpmenu.add_command(label="About...", command=domenu)
#
# root.config(menu=menubar)             # 생성된 객체를 위에서 생성된 메뉴바에 연결
# root.mainloop()


# import tkinter as tk
#
# root = tk.Tk()
# root.geometry("320x240")  # root 윈도우는 pack()이 필요없다.
# root.title("Frame Test")
#
# frame = tk.Frame(root, bd=5, bg='light blue', relief='groove')  # 메인프레임
# frame.pack()
#
# l_frame = tk.Frame(root, bd=40, bg='white')  # 왼쪽프레임
# l_frame.pack(side=tk.LEFT)
#
# l_frame1 = tk.Frame(l_frame, bd=40, bg='white')  # 왼쪽1프레임
# l_frame1.pack(side=tk.LEFT)
#
# l_frame2 = tk.Frame(l_frame, bd=40, bg='white')  # 왼쪽2프레임
# l_frame2.pack(side=tk.RIGHT)
#
# r_frame = tk.Frame(root)  # 오른쪽프레임
# r_frame.pack(side=tk.RIGHT)
#
# label = tk.Label(frame, text='Hello Tkinter!')  # top 쪽에 올라감
# label.pack()
#
# button1 = tk.Button(l_frame1, text='Button 1')  # 기본형
# button1.pack(padx=10, pady=10)
#
# button11 = tk.Button(l_frame1, text='Button 11')  # 기본형
# button11.pack(padx=10, pady=10)
#
# button12 = tk.Button(l_frame1, text='Button 12')  # 기본형
# button12.pack(padx=10, pady=10)
#
# button2 = tk.Button(r_frame, text='Button 2', bd=5, bg='light blue', )
# button2.pack(padx=10, pady=10)
#
# button3 = tk.Button(l_frame2, text='Button 3', bd=5, bg='light green')
# button3.pack(padx=10, pady=10)
#
# button4 = tk.Button(r_frame, text='Button 4', relief='sunken')
# button4.pack(padx=10, pady=10)
#
# root.mainloop()
