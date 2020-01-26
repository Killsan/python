from tkinter import *

def agree():
	for i in chk_buttons:
		i.set(True)

root = Tk()

chkb_v1 = IntVar()
chkb_v2 = IntVar()
chkb_v3 = IntVar()
chkb_v4 = IntVar()
chkb_v5 = IntVar()
chkb_v6 = IntVar()

chkb_spec_v = IntVar()

chkb1 = Checkbutton(root, text='Agree', variable=chkb_v1).pack()
chkb2 = Checkbutton(root, text='Agree', variable=chkb_v2).pack()
chkb3 = Checkbutton(root, text='Agree', variable=chkb_v3).pack()
chkb4 = Checkbutton(root, text='Agree', variable=chkb_v4).pack()
chkb5 = Checkbutton(root, text='Agree', variable=chkb_v5).pack()
chkb6 = Checkbutton(root, text='Agree', variable=chkb_v6).pack()

chkb_spec = Checkbutton(root, text='Agree with all', variable=chkb_spec_v, command=agree).pack()

chk_buttons = [chkb_v1, chkb_v2, chkb_v3, chkb_v4, chkb_v5, chkb_v6]

root.mainloop()