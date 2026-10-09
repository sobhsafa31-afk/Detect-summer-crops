import tkinter as tk
from Function_images import *
from tkinter import messagebox

def check():
    address = addres_image_entry.get()
    try:
        p , h , w = load_image(address)
    except (OSError, ValueError):
        messagebox.showerror("خطا", "عکس یافت نشد یا قابل خواندن نیست")
        return

    pixels = remove_background(p)

    try:
        a_r , a_g , a_b = average(pixels)
    except ValueError:
        messagebox.showerror("خطا", "پیکسل قابل استفاده‌ای در تصویر پیدا نشد")
        return

    gray_pixel = rgb2gray(pixels)
    hist_data = get_hist_features(gray_pixel)

    color_family = check_object(a_r , a_g , a_b)

    final_result = finall_check(hist_data , color_family , a_r , a_g , a_b)

    messagebox.showinfo("یافته شد" , f"سیستم {final_result}را تشخیص داد")


########################################################################################
########################################################################################
    

root = tk.Tk()
root.geometry("300x200")
root.title("برنامه ی تشخیص صیفی جات")

#Frame
main_frame = tk.Frame(root , background="lightgreen")
main_frame.pack(fill="both" , expand="True")

#lables
wel_lable = tk.Label(main_frame , text="به سیستم تشخیص صیفی جات خوش آمدید")
wel_lable.grid(row=1 , column=2)

addres_image_lable = tk.Label(main_frame , text="آدرس عکس:")
addres_image_lable.grid(row=2 , column=1)

#Entry

addres_image_entry = tk.Entry(main_frame)
addres_image_entry.grid(row=2 , column=2)

#button
finish_button = tk.Button(main_frame , text="ثبت" , command=check)
finish_button.grid(row=5 , column=2)

root.mainloop()