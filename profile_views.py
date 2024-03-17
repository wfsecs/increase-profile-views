from colorama import Fore, init
import requests
import time

init()

F_YELLOW = Fore.YELLOW
RESET = Fore.RESET


url = input('URL to visit: ')
times = int(input('How many visits? '))


def main(value):
    for x in range(value):
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})
        print(f'    ({value + 1}) ({F_YELLOW}{url[0:25]}{RESET}...) Visited URL: {r.status_code}')
        time.sleep(0.1)


main(times)
