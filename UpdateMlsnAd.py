from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#Load configuration
MLSNLogin = "<login>"
MLSNPass  = "<pass>"

def process_ad_page(pageUrl):
    #Переходим на страницу "Мои объекты"
    driver.get(pageUrl)
    sleep(1)
    #Перейти к активным объявлениям
    driver.find_element_by_xpath("//a[contains(text(),'Активные')]").click()
    sleep(1)
    #Нажать "Обновить всё"
    driver.find_element_by_id("update-button-all-bottom").click()
    sleep(1)

#Actions
#Запускаем браузер
driver = webdriver.Chrome()
driver.implicitly_wait(10)

#Авторизация (ввод логина/пароля)
print("Авторизация на сайте MLSN, как "+MLSNLogin)
driver.get("https://omsk.mlsn.ru/user/default/login/")
driver.find_element_by_id("LoginForm_username").send_keys(MLSNLogin)
driver.find_element_by_id("LoginForm_password").send_keys(MLSNPass)
sleep(0.5)
driver.find_element_by_id("LoginForm_password").send_keys(Keys.RETURN)

#Заходим на все страницы "Мои объекты"
print("Обрабатываем: Аренда жилья")
process_ad_page("https://omsk.mlsn.ru/office/rent/admin/?SearchRent%5Bplatform%5D=2&SearchRent%5Bregion_fias%5D=55&userId=361940&filialId=&agencyId=")

print("Обрабатываем: Аренда коммерческой")
process_ad_page("https://omsk.mlsn.ru/office/rentBusiness/admin/")

print("Обрабатываем: Продажа коммерческой")
process_ad_page("https://omsk.mlsn.ru/office/saleBusiness/admin/")

print("Обрабатываем: Продажа жилья")
process_ad_page("https://omsk.mlsn.ru/office/sale/admin/")

print("Обрабатываем: Дома, дачи и участки")
process_ad_page("https://omsk.mlsn.ru/office/land/admin/")

print("Обрабатываем: Продажа гаражей")
process_ad_page("https://omsk.mlsn.ru/office/garage/admin/")

driver.close()