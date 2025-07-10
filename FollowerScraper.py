import os
import requests
import json
import time
import colorama
from colorama import Fore, Back, Style, init
import ctypes
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout

class UI:
    green = Fore.LIGHTGREEN_EX
    blue = Fore.LIGHTBLUE_EX
    red = Fore.RED
    reset = Fore.RESET
    white = Fore.LIGHTWHITE_EX
    cyan = Fore.LIGHTCYAN_EX

    error = f"{Fore.RED}Error{Fore.RESET} {Fore.LIGHTWHITE_EX}┣{Fore.RESET} "
    alert = f"{Fore.LIGHTRED_EX}Alert{Fore.RESET} {Fore.LIGHTWHITE_EX}┣{Fore.RESET} "
    invalid = f"{red}[Invalid]{reset}"
    valid = f"{green}[Valid]{reset}"
    success = f"{green}[Success]{reset}"
    failed = f"{red}[Failed]{reset}"

    @staticmethod
    def clear():
        if os.name == 'nt':  
            os.system('cls')
        else: 
            os.system('clear')
        
    def set_console_title(title: str):
        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW(title)
        else:
            os.system(f'echo -ne "\033]0;{title}\007"')

class FollowersScraper:
    session = requests.Session()
    header = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
    }

    def __init__(self):
        self.session.headers.update(self.header)
        self.scraped_users = []
        self.index = 0

    def scrape(self, username, cursor='-1', max_retries=3):
        url = f"https://api.x.com/1.1/followers/list.json?screen_name={username}&count=200&cursor={cursor}&skip_status=true"

        for attempt in range(max_retries):
            try:
                response = self.session.get(url, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    users = data.get("users", [])
                    self.scraped_users.extend(users)
                    self.index += 1
                    print(f"{Fore.LIGHTWHITE_EX}Scraped{UI.reset} {Fore.RED}{len(users)}{UI.reset} {UI.white}Followers from{UI.reset} {Fore.RED}{username}{UI.reset}")
                    next_cursor = data.get("next_cursor_str", '0')
                    if next_cursor and int(next_cursor) != 0:
                        return next_cursor
                    break
                else:
                    print(f"{UI.error}{UI.red}HTTP Status {response.status_code} - {username}.{UI.reset}")

            except (HTTPError, ConnectionError, Timeout, RequestException) as e:
                print(f"{UI.error}{UI.red}Request Failed - {username}: stre.{UI.reset}")
            
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
        else:
            print(f"{UI.error}{UI.red}Failed to Scrape - {username}.{UI.reset}")
        
        return None

def save_to_txt(scraped_users, filename):
    with open(f'{filename}_Followers.txt', 'w', encoding='utf-8') as f:
        for user in scraped_users:
            f.write(f"{user['screen_name']}\n")

def main():
    while True:
        username = input(f"{UI.white}Username{UI.reset} {Fore.LIGHTWHITE_EX}:{UI.reset} ").strip()
        if len(username) > 15:
            print(f"{UI.error}{UI.red}Username is too long. Maximum Length is 15 Characters.{UI.reset}")
            continue
        
        if not username:
            print(f"{UI.error}{UI.red}Username can't be Empty.{UI.reset}")
            continue
        else:
            break

    print("")
    scraper = FollowersScraper()
    cursor = '-1'
    
    while cursor:
        cursor = scraper.scrape(username, cursor)
    
    if scraper.scraped_users:
        save_to_txt(scraper.scraped_users, username)
        print(f"\n{UI.white}Scraped{UI.reset} {Fore.RED}{len(scraper.scraped_users)}{UI.reset} {UI.white}Followers and saved into {Fore.RED}{username}_Followers.txt{UI.reset}{Fore.LIGHTWHITE_EX}.{Fore.RESET}")
    else:
        print(f"\n{UI.error}{UI.red}No Followers were scraped for {username}.{UI.reset}")
    
    print(f'\n{Fore.LIGHTWHITE_EX}Press Enter to Return.{UI.reset}')
    input("")

if __name__ == "__main__":
    main()