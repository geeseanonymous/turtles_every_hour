from time import sleep
import instabot


bot = instabot.Bot()

bot.login(username="turtles_every_hour",password="Turtles_All_The_Time@102938")

path = '/home/geeseanonymous/.virtualenvs/myvirtualenv/igbot/pics'
for image in path:
    bot.upload_photo(image,caption="nice hour for turtles")
    sleep(7200)
