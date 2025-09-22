from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv


# Estableciendo pagina de inicio
driver1 = webdriver.Chrome()
driver1.get('https://books.toscrape.com/catalogue/page-47.html')

# Scraping de las ultimas 4 paginas
with open("libros.csv", "w", newline="\n", encoding="utf-8") as f:
    writer = csv.writer(f)
    # n = int(driver1.find_element(By.XPATH, "//li[@class='current']").text.split()[-1])
    driver2 = webdriver.Chrome()
    for i in range(4):
        elements = driver1.find_elements(By.XPATH, "//h3/a")
        for element in elements:
            driver2.get(element.get_attribute("href"))
            titulo = driver2.find_element(By.XPATH, "//h1").text
            precio = driver2.find_element(By.XPATH, "//div[contains(@class, 'product_main')]/p[@class='price_color']").text
            print(titulo, precio)
            writer.writerow([titulo, precio])
        try:
            next = driver1.find_element(By.XPATH, "//li[@class='next']/a")
            next.click()
        except:
            print("No se encontro botón next")

# driver3 = webdriver.Chrome()
# driver3.get("https://www.mercadolibre.com.ec/")
# driver3.find_element(By.XPATH, "//input[@id='cb1-edit']").send_keys('juguetes')
# driver3.find_element(By.XPATH, "//input[@id='cb1-edit']").send_keys(Keys.RETURN)