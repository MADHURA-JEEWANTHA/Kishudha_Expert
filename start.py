import threading
import webbrowser
import time

from waitress import serve
from app import app

def open_browser():
    time.sleep(2)
    webbrowser.open("http://127.0.0.1:5000")

threading.Thread(target=open_browser).start()

serve(app, host="127.0.0.1", port=5000)