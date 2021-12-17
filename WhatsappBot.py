from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import datetime
import keyboard

print("WhatsappBot Yükleniyor...")

for i in range(5, 0, -1):
    print("Yükleniyor... (" + str(i) + ")")
    time.sleep(0.5)

print("WhatsappBot Başarıyla Yüklendi!")
print("Kontrol Edilecek Kullanıcının İsmini Girin:")
user = input()
print("Kontrol Edilecek Kullanıcı " + user + " Olarak Ayarlandı!")
print("Tarayıcı (Microsoft Edge) Başlatılıyor...")
time.sleep(2)
services = Service(r'C:\Users\Toshiba\Desktop\msedgedriver.exe')
driver = webdriver.Edge(service=services)
driver.get("https://web.whatsapp.com")
print("Tarayıcı (Microsoft Edge) Başarıyla Başlatıldı!")
print("Kontrolü Başlatmak İçin '<' Tuşuna Basın!")
keyboard.wait("<")
print("Kontrol Başlatıldı!")

try:
    message_button = driver.find_element(By.XPATH, "//*[@id='side']/header/div[2]/div/span/div[2]/div")
    message_button.click()
    time.sleep(1.5)
    search_box = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]")
    search_box.click()
    time.sleep(0.5)
    search_box.send_keys(user)
    time.sleep(1)
    chat = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]")
    chat.click()
    time.sleep(2)
    status = driver.find_element(By.XPATH, "//*[@id='main']/header/div[2]/div[2]/span").text

    while True:
        try:
            if status == "çevrimiçi":
                date = datetime.datetime.now()
                date_format = date.strftime("%d/%m/%Y - %H:%M:%S")
                print(user + " İsimli Kullanıcı Şuan Çevrimiçi (" + date_format + ")")
                time.sleep(10)
        except:
            pass
except:
    pass
