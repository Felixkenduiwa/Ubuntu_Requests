# ubuntu_image_fetcher.py
"""
Ubuntu-Inspired Image Fetcher
------------------------------------
"I am because we are"

This script connects to the global community (the web),
fetches images from a provided URL, and stores them
in a shared folder for later appreciation.

Ubuntu Principles Applied:
- Community: Connects to the wider internet community
- Respect: Handles errors gracefully without crashing
- Sharing: Organizes downloaded images into a folder
- Practicality: Provides a real and reusable tool
"""

import os
import requests
from urllib.parse import urlparse
from datetime import datetime

def fetch_image():
    # Prompt user for the image URL
    url = input("Enter the image URL: ").strip()
    
    # Create directory for storing images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Fetch the image using requests
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Extract filename from the URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename present in URL, generate one
        if not filename:
            filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"

        # Define save path
        file_path = os.path.join(save_dir, filename)

        # Save image in binary mode
        with open(file_path, "wb") as file:
            file.write(response.content)

        print(f"✅ Image successfully fetched and saved as: {file_path}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL. Please include 'http://' or 'https://'.")
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Try again later.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    fetch_image()
