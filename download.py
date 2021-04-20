from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import sys
import os


#taking user input
def download_images(download):
   
    site = 'https://www.google.com/search?tbm=isch&q='+ download


    #providing driver path
    driver = webdriver.Firefox(executable_path = 'C:\Drivers\geckodriver.exe')

    #passing site url
    driver.get(site)


    i = 0

    while i<1:  
        #for scrolling page
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        
        try:
            #for clicking show more results button
            driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
        except Exception as e:
            pass
        i+=1

    #parsing
    soup = BeautifulSoup(driver.page_source, 'html.parser')


    #closing web browser
    driver.close()


    #scraping image urls with the help of image tag and class used for images
    img_tags = soup.find_all("img", class_="rg_i")


    count = 1
    for i in img_tags:
        #print(i['src'])
        try:
            #passing image urls one by one and downloading
            urllib.request.urlretrieve(i['src'], download + str(count) + ".jpg")
            count+=1
            if count == 11:
                break
            print("Number of images downloaded = "+str(count),end='\r')
        except Exception as e:
            pass


download = ['dog', 'cat']

for i in download:
    download_images(i)
