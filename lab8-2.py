def cal():
  r= int(tb1.get())
  circle = (3.14)*pow(r,2)
  messagebox.showinfo("พื้นที่วงกลม","ผลลัพธ์ %.2f" % circle)
  result.set(circle)
  
from tkinter import *
window = Tk()
window.geometry("800x500")
window.title("โดยวิภาดา ศรีสอาด")

result = StringVar()


lb = Label(window,text = "ยินดีต้อนรับเข้าสู่โปรแกรม python",font = ("Cooper Black",24))
lb.place(x=50, y=10)

lb1 =Label(window,text = "รับค่ารัศมี",font = ("Cooper Black",18))
lb1.place(x=50, y=80)
tb1 =Entry(window)
tb1.place(x=160, y=90 , width=200 , height=30)

lb2 =Label(window,text = "ผลลัพธ์",font = ("Cooper Black",18))
lb2.place(x=50, y=120)
tb2 =Entry(window,textvariable=result)
tb2.place(x=160, y=130,width=200 , height=30 )

btn =Button(window,text = "คำนวณ", font = ("Cooper Black",18),command =cal)
btn.place(x=370, y=100)

window.mainloop()
