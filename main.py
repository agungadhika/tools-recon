import requests

def check_file_existence(url, filename):
    if not url.endswith('/'):
        url += '/'
    file_url = url + filename
    response = requests.head(file_url)
    if response.status_code == 200:
        print(f"File {filename} ditemukan di {url}")
    else:
        print(f"File {filename} tidak ditemukan di {url}")

if __name__ == "__main__":
    website_url = input("Masukkan URL website: ")
    check_file_existence(website_url, 'Dockerfile')
    check_file_existence(website_url, 'docker-compose.yml')
    check_file_existence(website_url, 'nginx.conf')


# Buatkan untuk nginx.conf, default.conf, .git, docker-compose.yml
#.gitkeep
#.git-rewrite
#.gitreview
#.git/HEAD
#.git/config
#.git/index
#.git/logs
#.svnignore
#.gitattributes
#.gitmodules
#.svn/entries