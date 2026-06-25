import threading
import time
import webview
import os

from waitress import serve
from app import app

def run_server():
    serve(app, host="127.0.0.1", port=5000)

def start():
    server = threading.Thread(target=run_server)
    server.daemon = True
    server.start()

    time.sleep(2)

    webview.create_window(
        "KISHUDHA STOCK SYSTEM",
        "http://127.0.0.1:5000",
        width=1400,
        height=900
    )

    webview.start()

    os._exit(0)

if __name__ == "__main__":
    start()
