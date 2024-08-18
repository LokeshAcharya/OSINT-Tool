import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr
import tweepy
from bs4 import BeautifulSoup

# ANSI escape sequences for colored text
Bl = '\033[30m'
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'

# Twitter API credentials (replace with your own)
TWITTER_API_KEY = 'your_api_key'
TWITTER_API_SECRET = 'your_api_secret'
TWITTER_ACCESS_TOKEN = 'your_access_token'
TWITTER_ACCESS_SECRET = 'your_access_secret'

# Initialize Tweepy
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
)
twitter_api = tweepy.API(auth)

def print_banner():
    banner = f"""{Re}
       __       ______     ______   __     __  __     ______     __   __     ______     ______    
      /\ \     /\  ___\   /\__  _\ /\ \   /\_\_\_\   /\  ___\   /\ "-.\ \   /\  ___\   /\  == \   
     _\_\ \    \ \___  \  \/_/\ \/ \ \ \  \/_/\_\/_  \ \  __\   \ \ \-.  \  \ \  __\   \ \  __<   
    /\_____\    \/\_____\    \ \_\  \ \_\   /\_\/\_\  \ \_____\  \ \_\\"\_\  \ \_____\  \ \_\ \_\ 
    \/_____/     \/_____/     \/_/   \/_/   \/_/\/_/   \/_____/   \/_/ \/_/   \/_____/   \/_/ /_/                                                                                            
    """
    print(banner)

def is_option(func):
    def wrapper(*args, **kwargs):
        print_banner()
        func(*args, **kwargs)
    return wrapper

@is_option
def track_ip():
    try:
        ip = input(f"{Wh}\n Enter IP target: {Gr}")
        if not ip:
            print(f"{Re}Invalid IP address. Please enter a valid IP address.{Wh}")
            return
        print(f'\n {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
        req_api = requests.get(f"http://ipwho.is/{ip}")
        if req_api.status_code != 200:
            print(f"{Re}Failed to retrieve information. Please check the IP address and try again.{Wh}")
            return
        ip_data = json.loads(req_api.text)
        time.sleep(2)
        print(f"{Wh}\n IP target       :{Gr}", ip)
        print(f"{Wh} Type IP         :{Gr}", ip_data["type"])
        print(f"{Wh} Country         :{Gr}", ip_data["country"])
        print(f"{Wh} Country Code    :{Gr}", ip_data["country_code"])
        print(f"{Wh} City            :{Gr}", ip_data["city"])
        print(f"{Wh} Continent       :{Gr}", ip_data["continent"])
        print(f"{Wh} Continent Code  :{Gr}", ip_data["continent_code"])
        print(f"{Wh} Region          :{Gr}", ip_data["region"])
        print(f"{Wh} Region Code     :{Gr}", ip_data["region_code"])
        print(f"{Wh} Latitude        :{Gr}", ip_data["latitude"])
        print(f"{Wh} Longitude       :{Gr}", ip_data["longitude"])
        lat = int(ip_data['latitude'])
        lon = int(ip_data['longitude'])
        print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
        print(f"{Wh} EU              :{Gr}", ip_data["is_eu"])
        print(f"{Wh} Postal          :{Gr}", ip_data["postal"])
        print(f"{Wh} Calling Code    :{Gr}", ip_data["calling_code"])
        print(f"{Wh} Capital         :{Gr}", ip_data["capital"])
        print(f"{Wh} Borders         :{Gr}", ip_data["borders"])
        print(f"{Wh} Country Flag    :{Gr}", ip_data["flag"]["emoji"])
        print(f"{Wh} ASN             :{Gr}", ip_data["connection"]["asn"])
        print(f"{Wh} ORG             :{Gr}", ip_data["connection"]["org"])
        print(f"{Wh} ISP             :{Gr}", ip_data["connection"]["isp"])
        print(f"{Wh} Domain          :{Gr}", ip_data["connection"]["domain"])
        print(f"{Wh} ID              :{Gr}", ip_data["timezone"]["id"])
        print(f"{Wh} ABBR            :{Gr}", ip_data["timezone"]["abbr"])
        print(f"{Wh} DST             :{Gr}", ip_data["timezone"]["is_dst"])
        print(f"{Wh} Offset          :{Gr}", ip_data["timezone"]["offset"])
        print(f"{Wh} UTC             :{Gr}", ip_data["timezone"]["utc"])
        print(f"{Wh} Current Time    :{Gr}", ip_data["timezone"]["current_time"])
    except Exception as e:
        print(f"{Re}Error: {e}{Wh}")

@is_option
def track_phone():
    try:
        user_phone = input(f"\n {Wh}Enter phone number target {Gr}Ex [+977xxxxxxxxx] {Wh}: {Gr}")
        default_region = "NP"  # DEFAULT REGION FOR NEPAL

        parsed_number = phonenumbers.parse(user_phone, default_region)
        region_code = phonenumbers.region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "en")  # "en" for English language
        is_valid_number = phonenumbers.is_valid_number(parsed_number)
        is_possible_number = phonenumbers.is_possible_number(parsed_number)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
        number_type = phonenumbers.number_type(parsed_number)
        timezone1 = timezone.time_zones_for_number(parsed_number)
        timezoneF = ', '.join(timezone1)

        print(f"\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
        print(f"\n {Wh}Location             :{Gr} {location}")
        print(f" {Wh}Region Code          :{Gr} {region_code}")
        print(f" {Wh}Timezone             :{Gr} {timezoneF}")
        print(f" {Wh}Operator             :{Gr} {jenis_provider}")
        print(f" {Wh}Valid number         :{Gr} {is_valid_number}")
        print(f" {Wh}Possible number      :{Gr} {is_possible_number}")
        print(f" {Wh}International format :{Gr} {formatted_number}")
        print(f" {Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
        print(f" {Wh}Original number      :{Gr} {parsed_number.national_number}")
        print(f" {Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
        print(f" {Wh}Country code         :{Gr} {parsed_number.country_code}")
        print(f" {Wh}Local number         :{Gr} {parsed_number.national_number}")
        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            print(f" {Wh}Type                 :{Gr} This is a mobile number")
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(f" {Wh}Type                 :{Gr} This is a fixed-line number")
        else:
            print(f" {Wh}Type                 :{Gr} This is another type of number")
    except Exception as e:
        print(f"{Re}Error: {e}{Wh}")

def fetch_twitter_data():
    try:
        username = input(f"{Wh}\n Enter Twitter username: {Gr}")
        user = twitter_api.get_user(screen_name=username)
        print(f"\n{Wh}========== {Gr}TWITTER PROFILE {Wh}==========")
        print(f"{Wh}Name             :{Gr} {user.name}")
        print(f"{Wh}Username         :{Gr} {user.screen_name}")
        print(f"{Wh}Description      :{Gr} {user.description}")
        print(f"{Wh}Followers Count  :{Gr} {user.followers_count}")
        print(f"{Wh}Following Count  :{Gr} {user.friends_count}")
        print(f"{Wh}Tweets Count     :{Gr} {user.statuses_count}")
        print(f"{Wh}Location         :{Gr} {user.location}")
        print(f"{Wh}URL              :{Gr} {user.url}")
        print(f"{Wh}Profile Image    :{Gr} {user.profile_image_url_https}")
    except tweepy.TweepError as e:
        print(f"{Re}Error fetching Twitter data: {e}{Wh}")

def web_scraper(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract and print some basic information
            title = soup.title.string if soup.title else 'No title found'
            print(f"\n{Wh}========== {Gr}WEB SCRAPER RESULTS {Wh}==========")
            print(f"{Wh}Title            :{Gr} {title}")
            
            # Add more scraping logic as needed
            # Example: print all the <h1> tags on the page
            h1_tags = soup.find_all('h1')
            if h1_tags:
                print(f"{Wh}H1 Tags:")
                for tag in h1_tags:
                    print(f"{Gr}  - {tag.text.strip()}")
            else:
                print(f"{Wh}No H1 tags found.")
        else:
            print(f"{Re}Failed to retrieve the webpage. Status code: {response.status_code}{Wh}")
    except Exception as e:
        print(f"{Re}Error: {e}{Wh}")

def main():
    while True:
        print(f"{Wh}\nChoose an option:")
        print(f"{Gr}1.{Wh} Track IP")
        print(f"{Gr}2.{Wh} Track Phone")
        print(f"{Gr}3.{Wh} Fetch Twitter Data")
        print(f"{Gr}4.{Wh} Exit")
        option = input(f"\n{Wh}Enter your choice: {Gr}")
        
        if option == '1':
            track_ip()
        elif option == '2':
            track_phone()
        elif option == '3':
            fetch_twitter_data()
        elif option == '4':
            print(f"{Gr}Exiting...{Wh}")
            break
        else:
            print(f"{Re}Invalid option. Please try again.{Wh}")

if __name__ == "__main__":
    main()
