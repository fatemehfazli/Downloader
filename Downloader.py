# downloader
from urllib.request import urlretrieve
import os
def downloader(url):
    path = os.path.basename(url)
    urlretrieve(url, f"C:\\Users\\ASUS\Downloads\\{path}")
    return 'The content of this link is stored in the downloads disk'

url = input("Enter your url: ")
print(downloader(url))