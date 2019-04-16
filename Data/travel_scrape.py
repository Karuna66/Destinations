import pandas as pd
from splinter import Browser
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import pymongo


def scrape():

    #Dictionary to store all output
    travel_dict = {}

    un_url = requests.get("https://www.un.org/en/member-states/index.html")
    un_soup = bs(un_url.text, 'lxml')

    ids = un_soup.find_all(class_="member-state col-md-12")
    mem_states = un_soup.find_all(class_="member-state-name")
    nat_holidays = un_soup.find_all(class_="national-holiday")

    country_id = [id_['id'] for id_ in ids]
    un_members= [mem_state.get_text(strip=True) for mem_state in mem_states]
    holidays = [holiday.get_text(strip=True) for holiday in nat_holidays]
    
    un_df = pd.DataFrame({
        "country_id": country_id,
        "country": un_members,
        "nat_holidays": holidays})
        
    un_df = un_df.to_html(index=True)
    un_df = un_df.replace('\n', '')

    travel_dict['un_df'] = un_df

    return travel_dict

if __name__ == "__main__":
    data = scrape()
    print(data)