#get proxies to extract news URLs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

def get_box_data(year_list, chromedriver):
    driver=webdriver.Chrome(chromedriver)
    box_office_frame=pd.DataFrame()
    for year in year_list:
        url = 'https://www.boxofficemojo.com/yearly/chart/?view2=worldwide&yr='+str(year)+'&p=.htm'
        driver.get(url)
        table=driver.find_element_by_xpath("//div[@id='main']//table[@cellpadding='5']//tbody")
        table_to_save=[]
        for i in table.find_elements_by_xpath('tr'):
            row=[]
            row.append(i.find_elements_by_xpath('td').text)
            #print(row)
            table_to_save.append(row)
        box_office_frame=pd.concat([box_office_frame,pd.DataFrame(table_to_save)], ignore_index=True)
    driver.quit()
    return box_office_frame
    
