import requests

def cek_git_directory(url):
    # Tambahkan '/' ke URL jika tidak ada
    if not url.endswith('/'):
        url += '/'

    # Gabungkan URL dengan .git
    git_url = url + 'Dockerfile'

    # Kirim permintaan HTTP GET ke URL .git
    response = requests.get(git_url)

    # Periksa status respons untuk menentukan apakah .git ada
    if response.status_code == 200:
        print(f"File Docker ditemukan di {url}")
    else:
        print(f"File Docker tidak ditemukan di {url}")

if __name__ == "__main__":
    website_url = input("Masukkan URL website: ")
    cek_git_directory(website_url)