from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from retrying import retry

class Driver():
    def __init__(self,driver):
        self.driver = driver

    @retry(stop_max_attempt_number=3,wait_fixed=3000)
    def waitElement(self,css):
        if "=>" in css:
            by=str(css).split("=>")[0]
            loc = str(css).split("=>")[1]
            if by=="id":
                element = WebDriverWait(self.driver,2,0.5).until(EC.presence_of_element_located((By.ID,loc)))
                self.driver.execute_script("arguments[0].scrollIntoView()",element)
                return element
            elif by=="xpath":
                element = WebDriverWait(self.driver,2,0.5).until(EC.presence_of_element_located((By.XPATH,loc)))
                self.driver.execute_script("arguments[0].scrollIntoView()",element)
                return element
            elif by=="css":
                element = WebDriverWait(self.driver,2,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,loc)))
                self.driver.execute_script("arguments[0].scrollIntoView()",element)
                return element
            else:
                raise exceptions.NoSuchElementException("请检查定位方法，目前只支持id,xpath,css_selector")
        else:
            print("定位语法错误，请检查语法，示例：id=>//div[@id='kw']")

    @retry(stop_max_attempt_number=3, wait_fixed=5000)
    def getElements(self,css):
        if "=>" not in css:

            by = str(css).split("=>")[0]
            value = str(css).split("=>")[1]
            if by == "id":
                elements = self.driver.find_elements(By.ID, value)
            elif by == "name":
                elements = self.driver.find_elements(By.NAME, value)
            elif by == "class":
                elements = self.driver.find_elements(By.CLASS_NAME, value)
            elif by == "link_text":
                elements = self.driver.find_elements(By.LINK_TEXT, value)
            elif by == "xpath":
                elements = self.driver.find_elements(By.XPATH, value)
            elif by == "css":
                elements = self.driver.find_elements(By.CSS_SELECTOR, value)
            else:
                raise NameError(
                    "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
            return elements


    def openUrl(self, url):
        """
        打开url.并窗口最大化
        用法:
        driver.open("https://www.baidu.com")
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def sendKeys(self, css, text):
        """
        操作输入框.
        用法:
        driver.type("css=>#el","selenium")
        """
        el = self.waitElement(css)
        el.send_keys(text)


    def clickElement(self, css):
        """
        它可以点击任何文本/图像
        连接，复选框，单选按钮，甚至下拉框等等..
        用法:
        driver.click("css=>#el")
        """
        el = self.waitElement(css)
        el.click()
        # self.js("arguments[0].click()",el)

    def moveToElement(self, css):
        """
        鼠标移到元素（悬停）.
        用法:
        driver.move_to_element("css=>#el")
        """
        el = self.waitElement(css)
        ActionChains(self.driver).move_to_element(el).perform()


    def quit(self):
        """
        关闭使用的所有窗口.
        用法:
        driver.quit()
        """
        self.driver.quit()

    def F5(self):
        """
        刷新当前页面.
        用法:
        driver.F5()
        """
        self.driver.refresh()


    def js(self, script,element):
        """
        执行JavaScript脚本.
        用法:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script,element)
    def getAttribute(self, css, attribute):
        """
        获取元素属性的值.
        用法:
        driver.get_attribute("css=>#el","type")
        """
        el = self.waitElement(css)
        return el.get_attribute(attribute)

    def addAttribute(self,css,attribute,value):
        '''
        添加元素的属性值
        用法：
        dricer.addAttribute("css=>#test","id","exmpname")
        '''
        el=self.waitElement(css)
        self.driver.execute_script("arguments[0].%s=arguments[1]" % attribute, el, value)


    def removeAttribute(self,css,attribute):
        '''
        删除元素属性值
        用法：
        driver.removeAttribute("css=>#test","id")
        '''
        element = self.waitElement(css)
        self.driver.execute_script("arguments[0].removeAttribute(arguments[1])", element, attribute)

    def getText(self, css):
        """
        获得元素文本信息
        用法:
        driver.get_text("css=>#el")
        """
        el = self.waitElement(css)
        return el.text

    def getTitle(self):
        """
        得到窗口标题.
        用法:
        driver.get_title()
        """
        return self.driver.title