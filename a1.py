import time
from PIL import Image
from selenium import webdriver
import pytesseract


zh = '1602423102'
mm = '199712'
dri = webdriver.Chrome()
dri.maximize_window()
dri.get('http://wxkq.niit.edu.cn')
time.sleep(3)



dri.get_screenshot_as_file('a.png')

if dri.find_element_by_id('verify_img'):
    location = dri.find_element_by_id('verify_img').location
    print('找到验证码')

size = dri.find_element_by_id('verify_img').size

left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']
a = Image.open("a.png")
im = a.crop((left, top, right, bottom))
im.save('a.png')
time.sleep(1)
#打开保存的验证码图片
image = Image.open("a.png")
image2 = Image.open("test.png")
#图片转换成字符
code1 = pytesseract.image_to_string(image)

print(code1)

dri.find_element_by_id('username').send_keys(zh)
dri.find_element_by_id('password').send_keys(mm)
dri.find_element_by_id('verify').send_keys(code1)

