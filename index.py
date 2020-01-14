from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        sleep(3)
        bot.get('https://twitter.com/i/optout')
        sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=spxr')
        sleep(3)
        for _ in range(2):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(3)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]

        for link in links:
            bot.get('https://twitter.com' + link)
            sleep(1.5)
            try:
                """bot.find_element_by_class_name('HeartAnimation').click()"""
                hearts = bot.find_elements_by_class_name('HeartAnimation')
                for index, heart in enumerate(hearts):
                    sleep(1)
                    if index % 2 == 0:
                        heart.click()
                        sleep(2)
                sleep(10)
            except Exception:
                sleep(10)

        bot.quit()


def account(username, password, hashtag):
    bot = TwitterBot(username, password)
    bot.login()
    bot.like_tweet(hashtag)


account('email@domain.com', 'password', 'hashtag')
