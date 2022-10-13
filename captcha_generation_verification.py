from email.mime import image
from tkinter import Image
from captcha.image import ImageCaptcha
import random
import time

def generate_captcha():
    captcha_text = ""
    captcha_len = random.randint(3,7)
    for i in range(1,captcha_len):
        captcha_text = captcha_text+chr(random.randint(97,122))
    image = ImageCaptcha()
    image.write(captcha_text, "image.png")
    
    user_entered_captcha = str(input("Enter the captcha from the image : "))
    if user_entered_captcha == captcha_text:
        print("Captcha Correct!")
    else:
        print("Captcha Incorrect! Correct captcha is "+captcha_text)

while True:
    generate_captcha()
    time.sleep(20)
