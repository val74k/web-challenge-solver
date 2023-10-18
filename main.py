import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def search_for_flags(content):
    flag_pattern = re.compile(r'\w+\{[^\}]*\}')
    flags = flag_pattern.findall(content)
    return flags

def extract_links(url, content):
    soup = BeautifulSoup(content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    
    links = [urljoin(url, link) for link in links]
    return links

files_to_check = ['/robots.txt', '/flag.txt', '/sitemap.xml', '/admin.html']

start_url = input("Enter the website: ")

urls_to_explore = [start_url]

found_flags = []

while urls_to_explore:
    current_url = urls_to_explore.pop(0)

    if current_url.startswith('http://') or current_url.startswith('https://'):
        response = requests.get(current_url)
        if response.status_code == 200:
            page_content = response.text

            flags_on_page = search_for_flags(page_content)
            if flags_on_page:
                for flag in flags_on_page:
                    print(f"Flag found on {current_url}: {flag}")
                found_flags.extend(flags_on_page)

            links_on_page = extract_links(current_url, page_content)

            for link in links_on_page:
                if link not in urls_to_explore:
                    urls_to_explore.append(link)

            for file_to_check in files_to_check:
                if current_url.endswith('/index.html'):
                    check_url = current_url.rsplit('/index.html', 1)[0] + file_to_check
                else:
                    check_url = current_url + file_to_check

                check_response = requests.get(check_url)
                if check_response.status_code == 200:
                    print(f"File {file_to_check} detected on {check_url}:")
                    print(check_response.text)
