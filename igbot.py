from time import sleep
import instabot
from selenium import webdriver
from PIL import Image
import requests
import io
import os


path = 'C:/Users/tzeka/PycharmProjects/chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)

query = 'baby turtle'
max_images = 100
driver.get('https://google.com')
seach_box = driver.find_element_by_css_selector('input.gLFyf')
seach_box.send_keys(query)

urls = set()
search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img".format(q=query)
driver.get(search_url)

while len(urls) < max_images:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(1)

    results = driver.find_elements_by_css_selector("img.Q4LuWd")
    result_number = len(results)

    for img in results:
        img.click()
        sleep(1)
        actual_images = driver.find_elements_by_css_selector("img.n3VNCb")
        for actual_image in actual_images:
            src = actual_image.get_attribute("src")
            if src and "http" in src:
                urls.add(src)

        if len(urls) >= max_images:
            print('yay')
            break
        else:
            print('getting more images')
            load_more = driver.find_element_by_css_selector(".mye4qd")
            if load_more:
                driver.execute_script("document.querySelector('.mye4qd').click();")

driver.close()

dummy = 0
file_names = set()
for url in urls:
    content = requests.get(url).content
    file = io.BytesIO(content)
    image = Image.open(file).convert("RGB")
    save_path = "C:/Users/tzeka/PycharmProjects/turtle" + str(dummy) + ".jpg"
    file_names.add("turtle" + str(dummy) + ".jpg")
    image.save(open(save_path, 'wb'), 'jpeg')
    dummy += 1


bot = instabot.Bot()

bot.login(username="turtles_every_hour",password="Turtles_All_The_Time@102938")
#
# for image in file_names:
#     bot.upload_photo(image,caption="nice hour for turtles")
#     sleep(3600)