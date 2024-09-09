import os
import hashlib
import json
import requests
from urllib.parse import urljoin
import sys
from collections import OrderedDict

class AutoUpdater:
    # ... (保持原有的 AutoUpdater 类代码不变) ...

def update_files(local_directory, remote_base_url):
    updater = AutoUpdater(local_directory, remote_base_url)
    return updater.update_files()

def initialize_directory(local_directory, remote_base_url):
    try:
        print(f"Initializing directory: {local_directory}")
        print(f"Remote base URL: {remote_base_url}")
        updater = AutoUpdater(local_directory, remote_base_url)
        result = updater.initialize_local_directory()
        print(f"Initialization result: {result}")
        return result
    except Exception as e:
        print(f"Exception during initialization: {str(e)}")
        return json.dumps({
            "status": "error",
            "message": str(e)
        }, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python autoupdater.py initialize_directory <local_directory> <remote_base_url>")
        sys.exit(1)
    
    command = sys.argv[1]
    if command == "initialize_directory":
        result = initialize_directory(sys.argv[2], sys.argv[3])
        print(result)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)