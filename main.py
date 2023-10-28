import requests
from bs4 import BeautifulSoup
import re

# Fungsi untuk mencari dan mencetak file dengan ekstensi tertentu dalam daftar tautan
def find_and_print_files(links, extension, file_description):
    matching_files = [link for link in links if link.endswith(extension)]
    if matching_files:
        print(f"{file_description} files:")
        for file in matching_files:
            print(file)

# URL dari website yang ingin Anda telusuri
website_url = "https://api-node-app.jobseeker.partners/"  # Ganti dengan URL yang sesuai

# Mengambil semua tautan dari halaman web
response = requests.get(website_url)
soup = BeautifulSoup(response.text, 'html.parser')
links = [link.get('href') for link in soup.find_all('a', href=True)]

# Mencari dan mencetak file .git
find_and_print_files(links, ".git", ".git")

# Mencari dan mencetak file docker-compose.yml
find_and_print_files(links, "docker-compose.yml", "docker-compose.yml")

# Mencari dan mencetak file Dockerfile
find_and_print_files(links, "Dockerfile", "Dockerfile")
