def print_tea_ids(tea_ids):
    print("لیست ایدی‌های تی")
    for tea_id in tea_ids:
        print(tea_id)

def print_class_times(class_times):
    print("لیست زمان‌های کلاس")
    for class_time in class_times:
        print(class_time)
print(("اوتریچ"),("لاجستیک"),("اپریشن"))
def main():
    operation = input("لطفا عملیات مورد نظر را انتخاب کنید (1=اپریشن/2=لاجستیک/3=اوتریچ): ")

    if operation == "اپریشن":
        options = ["ایدی تی‌ها", "زمان کلاس‌ها", "کلاس زبان"]
        print("گزینه‌های موجود:")
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        choice = int(input("لطفا یکی از گزینه‌ها را انتخاب کنید: "))
        if choice == 1:
            tea_ids = ["@mehrsa_alikhani", "@Hannaneh08", "@helma_ram"]  # لیست ایدی‌های تی
            print_tea_ids(tea_ids)
        elif choice == 2:
            class_times = ["ديتا ساينس :دوشنبه=8.30تا10وپنجشنبه=8تا9.30", "گرافيک:فلان روز=.....وفلان روز=......و ", "رباتيک:فلان روز =.....وفلان روز=......و"]  # لیست زمان‌های کلاس
            print_class_times(class_times)
        elif choice == 3:
            class_en = ["کلاس بارن:روز شنبه=4تا5.30ودوشنبه=6.30تا8","کلاس اتش:فلان روز=......و فلان روز=......و","کلاس زمين:فلان روز=......وفلان روز=......و"]
            pass
        else:
            print("گزینه نامعتبر!")
#----------------------------------------------------------------------------------------------------------------------------------------------------
    elif operation == "لاجستیک":
          options =["ايدي تي اي ها","اشکالات لپتاپ","حجم وي پي ان"]
          print("گزينه هاي موجود:")
          for index, option in enumerate(options, start=1):
              print(f"{index}. {option}")
              
          choice = int(input("لطفا یکی از گزینه‌ها را انتخاب کنید: "))
          if choice == 1:
            tea_ids = ["@Basira_Banifatemeh", "@mr_fekri86", "@Amirhosseinsediqii"]  # لیست ایدی‌های تی
            print_tea_ids(tea_ids)
          elif choice == 2:
            class_times = ["مشکلات ویندوز   که وارد این سایت شویدhttps://soft98.ir/os/12921-%D8%AF%D8%A7%D9%86%D9%84%D9%80%D9%88%D8%AF%E2%80%8C-%D9%81%D8%B9%D9%80%D8%A7%D9%84-%D8%B3%D8%A7%D8%B2-%D9%88%DB%8C%D9%86%D8%AF%D9%88%D8%B2.html و برنامه  را نصب کنید و  برنامه رو ران کنید  و اگر مشکلی داشتید در گروه بپرسید","براي حل مشکل دوربين لپ تاپ به اين سايت مراجعه کنيد https://www.technolife.ir/blog/%D8%AD%D9%84-%D9%85%D8%B4%DA%A9%D9%84-%D9%87%D9%86%DA%AF-%DA%A9%D8%B1%D8%AF%D9%86-%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE/", " براي مشکل زوم اول مجوز هاي برنامه را چک کنيد و سپس اگر مشکل اينترنت داريد  بسته ي جديدي بخريد و يا به جايي برويد .که سيگنال دهي قوي باشد","اگر زوم بروز رساني بخواهد اول ديسک حافظه ي خود رو کم کنيد سپس به دانلود کردن شروع کنيد توجه داشته باشيد که در حالدانلود از برنامه خارج يا انرا کوچک نکنيد","اگر در بازکردن وي پي ان مشکل داريد و ارور ميدهد انرا پاک کرده و دوباره دانلود کنيد  سپس از روبيکمپ لينک سرور ها را بگيريد و کپي کنيد سپس در داخل برنامه گزينه ي پيست فور کيبرد را بزنيد."]  # لیست زمان‌های کلاس  
            print_class_times(class_times)
          elif choice == 3:
            class_en = ["  پيام بديداگر حجم ويپي ان تمام شد سريعا به'@Basira_Banifatemeh'"]
            pass
          else:
            print("گزینه نامعتبر!")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    elif operation == "اوتريچ":
        options = ["ايدي تي اي ها","تايم روبيگپ ها ","فيدبک"]
        print("گزينه هاي موجود:")
        for index, option in enumerate(options, start=1):
              print(f"{index}. {option}")
              
        choice = int(input("لطفا یکی از گزینه‌ها را انتخاب کنید: "))
        if choice == 1:
            tea_ids = ["@erfan_art7", "@Talaafsa", "https://t.me/BaharRazavii"]  # لیست ایدی‌های تی
            print_tea_ids(tea_ids)
        elif choice == 2:
            class_times = ["هر هفته اعلام ميشه که روبيگپ داريم يا نه و لينکش توي گروه پين شده و روز شنبه ساعت 9 تا 10.30 هست"]  # لیست زمان‌های کلاس  
            print_class_times(class_times)
        elif choice == 3:
            class_en = ["@Talaafsa اگر فيدبکي داريد که ميتونه بهمون کمک کنه به ايدي زير پيام بديد"]
            pass
        else:
            print("گزینه نامعتبر!")
    else:
        print("عملیات نامعتبر!")

if __name__ == "__main__":
    main()
