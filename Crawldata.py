import requests
from bs4 import BeautifulSoup
import csv

# URL halaman indeks Detik
url = "https://news.detik.com/indeks"

# Mengirim permintaan GET ke halaman
response = requests.get(url)
response.raise_for_status()  # memastikan permintaan berhasil

# Parsing konten halaman dengan BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Mencari elemen-elemen yang berisi data yang diinginkan
articles = soup.find_all("article")

# Menyimpan data yang diambil
data = []

for article in articles:
    try:
        # Inisialisasi variabel dengan nilai default
        title, link, img_url, date = None, None, None, None

        title_tag = article.find("h3", class_="title")
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag.find("a")["href"]

        img_tag = article.find("img")
        img_url = img_tag["src"] if img_tag else None

        date_tag = article.find("time")
        date = date_tag.get_text(strip=True) if date_tag else None

        data.append([link, title, img_url, date])
    except Exception as e:
        print(f"Error processing article: {e}")

# Menyimpan data ke file CSV
csv_file = "detik_news.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["URL", "Judul", "Gambar", "Tanggal"])
    writer.writerows(data)

print(f"Data berhasil disimpan ke {csv_file}")
