import requests
from threading import Thread
from task_02_logic import app
import time

def run_server():
    app.run(port=5000, debug=False, use_reloader=False)

def test_items_page():
    # Serveri ayrı bir thread-də işə salırıq
    server_thread = Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    time.sleep(1)  # Serverin işə düşməsi üçün gözləyirik

    try:
        response = requests.get("http://127.0.0.1:5000/items")
        assert response.status_code == 200, "Failed: Items page did not return status code 200"
        print("Passed: Items page returned status code 200")
        assert "Python Book" in response.text, "Failed: 'Python Book' not found in page"
        print("Passed: Item 'Python Book' found in page")
    finally:
        # Serveri dayandırmaq üçün thread-i bitiririk
        server_thread.join(0)

if __name__ == "__main__":
    test_items_page()
