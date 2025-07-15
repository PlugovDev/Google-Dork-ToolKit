import requests
from bs4 import BeautifulSoup
import time

def banner():
    print(r"""
     `-'       `--' hjm
         _nnnn_
        dGGGGMMb     ,""""""""""""""
       @p~qp~~qMb    | @k0depp tool! |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' hjm
""")

def bing_search(query):
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/91.0.4472.124 Safari/537.36"),
        "Accept-Language": "en-US,en;q=0.9"
    }
    url = f"https://www.bing.com/search?q={query}&count=20"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        for item in soup.select('li.b_algo h2 a'):
            link = item.get('href')
            if link:
                results.append(link)
        return results
    except Exception as e:
        print(f"Error during request: {e}")
        return []

if __name__ == "__main__":
    banner()
    queries = [
        "intitle:index.of password",
        "inurl:admin login",
        "filetype:env",
        "inurl:wp-login.php",
        "intitle:login",
        "inurl:php?id=",
        "filetype:sql",
        "filetype:bak",
        "inurl:/admin/",
        "inurl:login.php",
        "intitle:\"Dashboard\"",
        "inurl:signup",
        "filetype:log",
        "intitle:\"Index of\"",
        "inurl:.git",
        "filetype:xls inurl:\"email\"",
        "intitle:\"Google Drive\"",
        "inurl:robots.txt",
        "inurl:\"wp-content\"",
        "ext:env",
        "ext:ini",
        "ext:log",
        "ext:bak",
        "ext:old",
        "ext:txt password",
        "intitle:\"Apache2 Debian Default Page\"",
        "intitle:\"Welcome to nginx\"",
        "intitle:\"phpMyAdmin\"",
        "inurl:\"phpmyadmin\"",
        "intitle:\"Error\"",
        "inurl:login",
        "inurl:register",
        "filetype:pdf confidential",
        "filetype:xls confidential",
        "filetype:doc confidential",
        "filetype:ppt confidential",
        "intitle:\"test page\"",
        "inurl:\"config.php\"",
        "inurl:\"setup.php\"",
        "intitle:\"index of /backup\"",
        "intitle:\"index of /db\"",
        "intitle:\"index of /admin\"",
        "inurl:forgot_password",
        "inurl:reset_password",
        "inurl:change_password"
    ]
    for q in queries:
        print(f"\nSearching for: {q}")
        links = bing_search(q)
        if links:
            for link in links:
                print(link)
        else:
            print("No results found or error occurred.")
        time.sleep(10)  # пауза, чтобы не забанили

    input("\nSearches complete. Press Enter to exit...")
