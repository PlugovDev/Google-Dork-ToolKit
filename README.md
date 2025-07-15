# Google Dork Toolkit

Simple tool for performing automated Google Dork (and Bing) searches for OSINT and penetration testing.

## Features

- Runs multiple popular Google Dork queries automatically  
- Fetches search result links using Bing search (to avoid Google CAPTCHA)  
- Displays results in the console  
- Easy to extend with your own dork queries  

## Requirements

- Python 3.x  
- `requests` library  
- `beautifulsoup4` library  

## Installation

1. Clone this repo or download the script.  
2. Install dependencies:  
   ```bash
   pip install requests beautifulsoup4

USAGE
Run the script in your terminal or command prompt:

python GoogleDorkByPlugov.py

The script will automatically perform all predefined Google Dork queries via Bing, printing found URLs to the console.
When the search completes, press Enter to exit the program.


Disclaimer!!
This tool is intended solely for educational purposes and legal penetration testing only.
Do not use this software to perform unauthorized or illegal activities.
The author is not responsible for any misuse or damages caused by this tool.

Author
Created by @PlugovDev and @k0depp in tiktok

Feel free to open issues or contribute!
