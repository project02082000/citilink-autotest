import datetime


class Base:
    base_url = "https://www.citilink.ru"

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        current_url = self.driver.current_url
        print(current_url)

    def screenshot(self):
        current_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'Screen' + current_date + ".png"
        self.driver.save_screenshot('.\\Screen\\' + name_screenshot)


