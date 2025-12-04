import requests
import csv

# Funksiya 1: API-dən postları çək və başlıqları ekrana çıxar
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    # Status kodunu çap et
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()  # JSON obyektinə çevir
        for post in posts:
            print(post['title'])  # Hər bir postun title-ini çap et
    else:
        print("Request failed!")

# Funksiya 2: API-dən postları çək və CSV faylına yaz
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()  # JSON obyektinə çevir
        # CSV üçün data strukturunu hazırla
        csv_data = []
        for post in posts:
            csv_data.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
        # CSV faylını yaz
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(csv_data)
        print("Data saved to posts.csv")
    else:
        print("Request failed!")
