from pageObject.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()
    logger.info("***************** Test_001_Login *****************")

    def testHomePageTitle(self, setup):
        self.logger.info("***************** Verifying testHomePageTitle *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "nopCommerce demo store. Login":
            self.driver.get_screenshot_as_png()
            self.driver.save_screenshot("C:\\Users\\Kiran\\PycharmProjects\\HybridFramework\\Screenshot\\test_login"
                                        ".png")
            self.driver.close()
            self.logger.info("***************** Home page title TC passed *****************")
            assert True
        else:
            self.logger.error("***************** Home page title TC passed *****************")
            assert False

    def test_login(self, setup):
        self.logger.info("***************** Login TC started *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.close()

        # act_title = self.driver.title
        # time.sleep(10)
        #
        # if act_title == "Dashboard / nopCommerce administration":
        #     self.logger.info("***************** Login TC passed *****************")
        #     assert True
        # else:
        #     self.driver.save_screenshot(".\\Screenshot\\test_login.png")
        #     self.driver.close()
        #     self.logger.error("***************** Login TC failed *****************")
        #     assert False
