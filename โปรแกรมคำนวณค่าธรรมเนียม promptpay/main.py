from tkinter import *
# นำเข้าโมดูล tkinter และเมธอดทั้งหมด
import threading
# นำเข้าโมดูล threading เพื่อจัดการทำงานให้ทำงานได้ลื่นไหล
import time

class MyApp():
#สร้างคลาส MyApp
    def __init__(self):
    #สร้างฟังค์ชั่น init เพื่อกำหนด แอตทริบิวต์
        self.root = Tk()
        #สร้างแอตทริบิวต์ self.root เท่ากับ Tk() คือ tkinter
        self.root.title("โปรแกรมคำนวณค่าบริการโอนเงิน Prompay")
        #แอตทริบิวต์สร้างส่วนของชื่อแสดงส่วน title UI
        self.root.geometry("300x300")
        #แอตทริบิวต์กำหนดขนาดของ UI
        self.root.configure(bg='#a1fffc')
        #แอตทริบิวต์กำหนดสีพื้นหลัง
        self.Lables(" ")
        #แอตทริบิวต์สร้าง Lable เปล่า
        self.Lables("โปรแกรมคำนวณค่าบริการโอนเงิน Prompay")
        #แอตทริบิวต์สร้าง Lable โดยมีข้อความว่า โปรแกรมคำนวณค่าบริการโอนเงิน Prompay
        self.Lables(" ")
        #แอตทริบิวต์สร้าง Lable เปล่า
        self.Lables("กรอกชื่อของคุณ")
        #แอตทริบิวต์สร้าง Lable โดยมีข้อความว่า กรอกชื่อของคุณ
        self.name = Entry(self.root, font=(15),highlightthickness=2,relief='solid',border=0,background="#fff",highlightbackground = "#5de3db",highlightcolor="#5de3db")
        #สร้างแอตทริบิวต์ self.name เพื่อเก็บค่าจาก เมธอด Entry ซึ่งเป็นเมธอด UI ในการรับข้อมูลจากแป้นพิมพ์โดยจะรับข้อมูลที่เป็น สตริง หรือชื่อของผู้ใช้
        self.name.pack()
        #แอตทริบิวต์เพื่อให้ self.name มาแสดงผลบน UI โดยใช้เมธอด pack()
        self.Lables(" ")
        #แอตทริบิวต์สร้าง Lable เปล่า
        self.Lables("กรอกจำนวนเงิน")
        #แอตทริบิวต์สร้าง Lable โดยมีข้อความว่า กรอกจำนวนเงิน
        self.number = Entry(self.root, font=(20),highlightthickness=2,relief='solid',border=0,background="#fff",highlightbackground = "#5de3db",highlightcolor="#5de3db")
        #สร้างแอตทริบิวต์ self.number เพื่อเก็บค่าจาก เมธอด Entry ซึ่งเป็นเมธอด UI ในการรับข้อมูลจากแป้นพิมพ์โดยจะรับข้อมูลที่เป็น number หรือจำนวนเงิน
        self.number.pack()
        #แอตทริบิวต์เพื่อให้ self.name มาแสดงผลบน UI โดยใช้เมธอด pack()
        self.number.insert(0, "0")
        #แอตทริบิวต์เพื่อให้ self.number มีค่าเริ่มเต้นเป็น 0
        self.Lables(" ")
        #แอตทริบิวต์สร้าง Lable เปล่า
        self.Button_Cal()
        #แอตทริบิวต์เรียกใช้เมธทอด Button_Cal()
        self.TextWarning = Label(self.root, text="", font=(30),bg='#a1fffc')
        #สร้างแอตทริบิวต์ self.TextWarning เพื่อเก็บค่าเมธทอด Label เพื่อใช้ในการแจ้งเตือนผู้ใช้งาน
        self.TextWarning.pack()
        #แอตทริบิวต์เพื่อให้ self.TextWarning มาแสดงผลบน UI โดยใช้เมธอด pack()
        threading.Thread(target=self.run).start()
        #เรียกใช้งาน class threading เมธทอด Thread() โดยจะให้ทำงานผ่าน threading โดยไปเรียกใช้ ฟังค์ชั่น run()
    def run(self):
    #สร้างฟังค์ชั่น run รับ พารามิเตอร์ self เพื่อจะใช้แอตทริบิวต์ใน class ฟังค์ชั่นนี้ใช้ในการ แสดงข้อความการทำงานของโปรแกรม
        for i in range(0,101,5):
        #สร้าง for loop โดยให้ i ไปวนใน range() ตั้งแต่ 0 - 100 โดยเพิ่มทีละ 5
            self.TimeRuns()['text'] = f'กำลังทำงาน {i}%'
            #สร้างแอตทริบิวต์ self.TimeRuns()['text'] 'text' คือค่าของพารามิเตอร์ที่อยู่ในเมธทอด Label ของ ฟังค์ชั่น TimeRuns() โดยให้มีค่าเท่ากับ f'กำลังทำงาน {i}%' 
            time.sleep(0.01)
            #จากนั้นหน่วงเวลา 0.01 ด้วย time.sleep
            if i == 100:
            #ตรวจสอบเงื่อนไข ถ้า i เท่ากับ 100 จะให้
                self.TimeRuns()['text'] = "พร้อมทำงานแล้วตอนนี้"
                #แอตทริบิวต์ self.TimeRuns()['text'] เท่ากับ "พร้อมทำงานแล้วตอนนี้"
        time.sleep(1)
        #จากนั้นหน่วงเวลา 1 ด้วย time.sleep
        self.TimeRuns()['text'] = "                                                 "
        #แอตทริบิวต์ self.TimeRuns()['text'] เท่ากับ ข้อความว่าง

    def TimeRuns(self):
    #สร้างฟังค์ชั่น TimeRuns รับ พารามิเตอร์ self เพื่อจะใช้แอตทริบิวต์ใน class ฟังค์ชั่นนี้ใช้ในการเป็นตัวต้นแบบข้อความแสดงการทำงานโปรแกรม
        self.TimeRun = Label(self.root, text="", font=(20),bg='#a1fffc')
        #สร้างแอตทริบิวต์ self.TimeRun ให้มีค่าเท่ากับ เมธทอด Label() โดยระบุพารามิเตอร์ text เท่ากับ สตริงว่าง เพราะค่อยเอาไปเพิ่มเมื่อต้องการในอนาคต
        self.TimeRun.place(x=0,y=270)
        #เรียกใช้เมธทอด place() เพื่อกำหนดตำแหน่งของข้อความ
        return self.TimeRun
        #ส่งค่า self.TimeRun คืนกลับไปให้หลังจาก call 

    def Lables(self, text,):
    #สร้างฟังก์ชั่น Lables รับพารามิเตอร์ self กับ text text ก็คือข้อความที่จะแสดง
        self.lable = Label(self.root, text=text,bg='#a1fffc')
        #สร้างแอตทริบิวต์ self.lable โดยมีค่า Label(self.root, text=text (คือพามิเตอร์ที่รับเข้ามา),bg='#a1fffc') 
        self.lable.pack()
        #เรียกใช้งานแอตทริบิวต์

    def Button_Cal(self):
    #สร้างฟังก์ชั่น Lables รับพารามิเตอร์ self เพราะจะให้ปุ่นเพื่อคำนวณผล
        self.button = Button(self.root, text="คำนวน", command=self.CheckMoney, background="#3dff54", foreground="#03400a", font=(20), width=20, activebackground="#32db46", activeforeground="#03400a",relief="groove")
        #สร้างแอตทริบิวต์สร้างปุ่มขึ้นมาแล้วปรับแต่งนิดหน่อย
        self.button.pack()
        #เรียกใช้งานปุ่มให้แสดงผล

    def CheckMoney(self):
    #สร้างฟังค์ชั่น CheckMoney(self) โดยมี self เป็นพารามิเตอร์ ฟังค์ชั่นนี้ใช้ในการตรวจสอบตัวเลขที่รับเข้ามา
        self.TextResult = None
        #สร้างแอตทริบิวต์ self.TextResult มีค่าเป็น None
        self.valueInput = self.number.get()
        #สร้างแอตทริบิวต์ self.valueInput มีค่าเป็น self.number.get() เพื่อรับค่าของแอตทริบิวต์ self.number ที่เป็นตัวเลขเข้ามาโดยใช้เมธทอด get()
        self.checkName = "0" if self.name.get() == "" else "1"
        #สร้าง Shorthandf If Else โดยถ้า self.name.get() == ค่าว่าง จะใช้ self.checkName = "0" แต่ถ้าไม่ใช่ก็ให้ self.checkName = "1"

        if self.checkName == "1":
        #ถ้า self.checkName เท่ากับ "1" จะทำการ
            self.FinallCal()
            #เรียกใช้ เมธทอต FinallCal()
        else:
        # ถ้าไม่ใช่
            self.TextWarning['text'] = "กรุณากรอกชื่อ"
            # จะให้ self.TextWarning['text'] = "กรุณากรอกชื่อ"
    def runRes(self):
    #สร้างฟังค์ชั่น runRes(self)
        for i in range(0, 101,4):
        #สร้าง for loop โดยให้ i ไปวนใน range() ตั้งแต่ 0 - 100 โดยเพิ่มทีละ 4
            time.sleep(0.01)
            #หน่วงเวลาด้วย time.sleep() ไป 0.01
            self.TextWarning['text'] = f'กำลังคำนวณ {i}%'
            #ให้ self.TextWarning['text'] มีค่าเท่ากับ f'กำลังคำนวณ {i}%'
        self.TextWarning['text'] = f'ค่าธรรมเนียมของคุณ{self.name.get()} คือ {self.fee} บาท'
        #หลังจากวนเสร็จให้ self.TextWarning['text'] มีค่าเท่ากับ f'ค่าธรรมเนียมของคุณ{self.name.get()} คือ {self.fee} บาท'
    def FinallCal(self):
    #สร้างฟังค์ชั่น FinallCal(self)
        try:
        #สร้าง try except เพื่อดัก error ที่อาจจะทำให้โปรแกรมหยุดการทำงานได้ โดย try คือให้ทำงานเงื่อนไขต่อไปนี้
            self.valueInput = int(self.valueInput)
            #สร้างแอตทริบิวต์ self.valueInput ให้มีค่าเท่ากับ self.valueInput ที่แปลงให้เป็น int แล้ว
            if self.valueInput > 0:
            #ถ้า self.valueInput มากกว่า 0 จะให้
                self.fee = 0
                #สร้างแอตทริบิวต์ self.fee เก็บค่า 0 เข้าไป
                self.fee = 0 if self.valueInput <= 5000 else 2 if self.valueInput > 5000 and self.valueInput <= 30000 else 5 if 30000 <= self.valueInput <= 100000 else 10
                #สร้าง Shorthandf If Else โดย ถ้า self.valueInput น้อยกว่าหรือเท่ากับ 5000 จะให้ self.fee = 0 แต่ถ้าหากว่า self.valueInput มากกว่า 5000 และ self.valueInput น้อยกว่าหรือเท่ากับ 30000 ถ้าเป็นจริงจะให้ self.fee = 2 แต่ถ้าหากว่า 30000 น้อยกว่าหรือเท่ากับ self.valueInput น้อยกว่าหรือเท่ากับ 100000 ถ้าจริงจะให้ self.fee = 5 แต่ถ้าไม่ใช่ทั้งหมดจะให้ self.fee = 10
                threading.Thread(target=self.runRes).start()
                #เรียกใช้งาน class threading เมธทอด Thread() โดยจะให้ทำงานผ่าน threading โดยไปเรียกใช้ ฟังค์ชั่น runRes() แล้วเริ่มด้วย start()
            else:
            #หากไม่ตรงเงื่อนไขใดๆ
                self.TextWarning['text'] = "กรุณากรอกจำนวนเงิน"
                #ให้ self.TextWarning['text'] = "กรุณากรอกจำนวนเงิน"
        except:
        #except คือหากพบข้อผิดพลาดใดๆใน try จะให้ทำงาน
            self.TextWarning['text'] = "กรุณากรอกจำนวนเงิน"
            #ให้ self.TextWarning['text'] = "กรุณากรอกจำนวนเงิน"


app = MyApp()
#สร้างตัวแปร app เก็บค่า MyApp() ซึ่งเป็น class MyApp()
app.root.mainloop()
#ทำการ while loop โปรแกรมไปเรื่อยๆจนกว่าจะบังคับปิดโปรแกรมหรือกดปุ่มปิด