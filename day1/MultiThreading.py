#multi threading


import threading
import requests


def fetch_data(url):
    try:
        response = requests.get(url)
        data = response.json()

        print(f"Fetched from {url}")
        print("Title:", data.get("title", "No title"))
        print("-" * 40)

    except Exception as e:
        print("Error:", e)


urls = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/todos/2",
    "https://jsonplaceholder.typicode.com/todos/3"
]

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_data, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All tasks completed")
