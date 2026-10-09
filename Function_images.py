from PIL import Image
from matplotlib import pyplot
import numpy as np


# Image Processing Functions

from PIL import Image
import random


def load_image(file_name):
    image = Image.open(file_name)

    width , height = image.size

    pixels = list(image.getdata())
    return pixels , width , height


def view_image(pixels , width , height , image_mode , color_pixel):
    new_image = Image.new(mode=image_mode ,
                          size=(width , height) ,
                          color= color_pixel)
    new_image.putdata(pixels)
    new_image.show()


def gray2binary(pixels):
    binary_pixels = []

    for p in pixels:
        if p <= 128:
            binary_pixels.append(0)

        else:
            binary_pixels.append(255)

    return binary_pixels


def rgb2gray(rgb_pixels):
    binary_pixels = []

    for p in rgb_pixels:
        avrage = round(sum(p) / 3)
        binary_pixels.append(avrage)

    return binary_pixels


def noise2image(pixel , intensity):
    binary_pixel = []

    if type(pixel[0]) == int:
        for p in pixel:
            p1 = p + random.randint(-intensity , intensity)
            binary_pixel.append(p1)

    if type(pixel[0]) == tuple:
        for p in pixel:
            p1 = p[0] + random.randint(-intensity , intensity)
            p2 = p[1] + random.randint(-intensity , intensity)
            p3 = p[2] + random.randint(-intensity , intensity)

            binary_pixel.append(  (p1 , p2 , p3)  )

    return binary_pixel



# pixels , w , h = load_image("images/rgb.png")
# binary = noise2image(pixels , 30)
# result = view_image(binary , w , h , "RGB" , (0 , 0 , 0))
# print(result)

def remove_background(pixels):
    bg_pixels = []

    for p in pixels:
        if p[0] < 230 and p[1] < 230 and p[2] < 230:
            bg_pixels.append(p)

    return bg_pixels

def average(pixels):
    length = len(pixels)
    c_r = 0
    c_g = 0
    c_b = 0

    for p in pixels:
        c_r += p[0]
        c_g += p[1]
        c_b += p[2]

    ave_r = round(c_r / length, 0)
    ave_g = round(c_g / length, 0)
    ave_b = round(c_b / length, 0)

    return ave_r , ave_g , ave_b

# def check_object_1(r , g , b):
#     result_color = None
    
#     if r < 30 and g < 30 and b < 30:
#         result_color = "Black"

#     elif b > 35 and b < 120 and g > 80 and g < 180 and r > 140:
#         result_color = "Orange"

#     elif g > 46 and g < 146 and b < 148 and r > 155:
#         result_color = "Red"

#     elif b > 25 and g > 70 and r > 45 and r < 140:
#         result_color = "Green"

#     return result_color

def check_object(r, g, b):
    if r < 95 and g < 95 and b < 95 and abs(r - g) < 25 and abs(g - b) < 25:
        return "Black"

    if r > 160 and g > 70 and g < 175 and b < 130 and (r - g) > 20:
        return "Orange"

    if r > 155 and g < 120 and b < 110 and (r - g) > 50:
        return "Red"

    if g > 80 and g > r and g > b and r < 160:
        return "Green"

    if r > 170 and g > 80 and g < 150 and b < 100:
        return "Orange"

    return None

def get_hist_data(gray_pixels):
    lst = []
    for gray in range(256):
        c = 0
        for p in gray_pixels:
            if p == gray:
                c +=1

        lst.append(c)

    return lst

def get_hist_features(gray_pixels):
    hist = get_hist_data(gray_pixels)
    total = sum(hist)
    if total == 0:
        return None

    max_hist = hist_max(hist)

    sum_number = 0

    for i in range(256):
        sum_number += i * hist[i]

    mean_gray = sum_number / total

    ratio_200 = caclc_ratio(hist, 200)
    dark_ratio = sum(hist[:80]) / total
    mid_ratio  = sum(hist[80:160]) / total
    bright_ratio = sum(hist[160:]) / total

    return {
        "max_hist": max_hist,
        "mean_gray": round(mean_gray, 1),
        "ratio_200": ratio_200,
        "dark": round(dark_ratio, 4),
        "mid": round(mid_ratio, 4),
        "bright": round(bright_ratio, 4),
        "hist": hist         
    }

def show(hist_data):
    x = np.array(range(256))
    y = np.array(hist_data)

    pyplot.bar(x , y)
    pyplot.show()

def caclc_ratio(lst , a , b = 226):
    over_a = sum(lst[a : b])
    under_a = sum(lst[:a])
    ratio = round(over_a / under_a , 5)

    return ratio

def hist_max(hist_data):
    max_bar = max(hist_data)
    gray_level = hist_data.index(max_bar)

    return gray_level



def finall_check(features, color_family, ave_r, ave_g, ave_b):
    if features is None:
        return None

    max_hist = features["max_hist"]
    mean = features["mean_gray"]
    dark = features["dark"]
    bright = features["bright"]
    ratio = features["ratio_200"]

    if color_family == "Black":
        return "بادمجان"

    if color_family == "Orange":
        if mean >= 125 and ave_b >= 70 and ave_g >= 135 and dark < 0.15 and ratio < 0.20:
            return "سیب‌زمینی"
        
        if mean >= 110 and mean <= 155 and ave_r >= 175 and ave_g <= 150 and ave_b <= 105 and (ave_r - ave_g) >= 55 and ratio < 0.12 and dark < 0.25:
            return "پیاز"
        
        if mean >= 100 and ave_g >= 120 and ave_b < 90 and ratio < 0.25 and dark < 0.30:
            return "فلفل دلمه‌ای زرد"
        
        return "هویج"

    if color_family == "Red":
        if mean > 105 or bright > 0.15 or max_hist > 100:
            return "فلفل دلمه‌ای قرمز"
        else:
            return "گوجه فرنگی"

    if color_family == "Green":
        if mean >= 105 and dark < 0.30:
            return "کدو سبز"

        if ave_g > 130 and mean > 95 and dark < 0.40:
            return "فلفل دلمه‌ای سبز"

        return "خیار"

    if color_family is None:
        if ave_r > 160 and ave_g > 130 and ave_b >= 70 and mean >= 125 and dark < 0.15:
            return "سیب‌زمینی"
        
        if ave_r >= 175 and ave_g <= 150 and ave_b <= 110 and(ave_r - ave_g) >= 55 and mean >= 110 and mean <= 160 and ratio < 0.12 and dark < 0.25:
            return "پیاز"
        
        if ave_r > 150 and ave_g > 130 and ave_b < 100 and mean > 110 and dark < 0.30:
            return "فلفل دلمه‌ای زرد"
        
        if ave_r >= 170 and ave_g <= 155 and ave_b <= 120 and (ave_r - ave_g) >= 45 and mean >= 95 and mean <= 160:
            return "هویج"

    return None