from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = "C:\PBL\Craw\chromedriver.exe"
wd = webdriver.Chrome(PATH)
urls = [
    #     "https://plantix.net/vi/library/plant-diseases/100350/black-rot-of-grape/",
    #    "https://plantix.net/vi/library/plant-diseases/300050/bacterial-spot-and-speck-of-tomato/",
    #    "https://plantix.net/vi/library/plant-diseases/100321/early-blight/",
    #    "https://plantix.net/vi/library/plant-diseases/100046/tomato-late-blight/",
    #    "https://plantix.net/vi/library/plant-diseases/100257/leaf-mold-of-tomato/",
    #    "https://plantix.net/vi/library/plant-diseases/800074/angular-leaf-scorch/"
    #    "https://plantix.net/vi/library/plant-diseases/100291/gray-leaf-spot/",
    #    "https://plantix.net/vi/library/plant-diseases/200061/alfalfa-mosaic-virus/",
    #    "https://plantix.net/vi/library/plant-diseases/100102/soybean-rust/",
    #    "https://plantix.net/vi/library/plant-diseases/100006/apple-scab/",
    #    "https://plantix.net/vi/library/plant-diseases/500004/spider-mites/",
    #    "https://plantix.net/vi/library/plant-diseases/100109/target-spot-of-soybean/",
    #    "https://plantix.net/vi/library/plant-diseases/200036/tomato-yellow-leaf-curl-virus/",
       ]

for url in urls:
    wd.get(url)
    data = {
        "name": "",
        "symptom": "",
        "recommend": "",
        "reason": "",
        "prevent": "",
    }

    name = wd.find_element(By.CLASS_NAME,"disease-name")
    data["name"] = name.text

    symptoms = wd.find_elements(By.CLASS_NAME,"card.collapsible.symptoms")
    for symptom in symptoms:
        data["symptom"] += symptom.text

    recommendations = wd.find_elements(By.CLASS_NAME,"product-recommendations")
    for recommendation in recommendations:
        data["recommend"] += recommendation.text

    reasons = wd.find_elements(By.CLASS_NAME,"card.collapsible.trigger-card")
    for reason in reasons:
        data["reason"] += reason.text

    prevents = wd.find_elements(By.CLASS_NAME,"preventive-measures-list")
    for prevent in prevents:
        data["prevent"] += prevent.text

    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(data["name"])
        f.write("\n")
        f.write(data["symptom"])
        f.write("\n")
        f.write(data["recommend"])
        f.write("\n")
        f.write(data["reason"])
        f.write("\n")
        f.write(data["prevent"])
        f.write("\n ----------------------------------------- \n")

    time.sleep(5)
    
