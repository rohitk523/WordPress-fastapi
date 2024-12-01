import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import json

# Load environment variables
load_dotenv()

# Get credentials from .env file
WP_URL = os.getenv('WP_URL')
WP_USER = os.getenv('WP_USER')
WP_PASSWORD = os.getenv('WP_PASSWORD')

def check_wordpress_access():
    # 1. Basic site accessibility check
    try:
        response = requests.get(WP_URL)
        print(f"Site Status: {response.status_code}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)[:100]}")
        return

    # 2. Check WordPress.com REST API
    try:
        # WordPress.com specific API endpoint
        api_url = "https://public-api.wordpress.com/wp/v2/sites/praiseandworshipdotcom.wordpress.com/posts"
        response = requests.get(api_url)
        if response.status_code == 200:
            posts = response.json()
            print(f"Public Posts found: {len(posts)}")
            for post in posts[:3]:
                print(f"Post title: {post.get('title', {}).get('rendered', 'No title')}")
        else:
            print(f"Public API Status: {response.status_code}")
        
    except Exception as e:
        print(f"API Error: {str(e)[:100]}")

    # 3. Try authenticated access
    try:
        auth_url = "https://public-api.wordpress.com/rest/v1.1/sites/praiseandworshipdotcom.wordpress.com/posts"
        headers = {
            'Authorization': f'Bearer {WP_PASSWORD}'
        }
        
        response = requests.get(auth_url)
        if response.status_code == 200:
            data = response.json()
            print(f"Total Posts: {data.get('found', 0)}")
        else:
            print(f"Auth Status: {response.status_code}")
            
    except Exception as e:
        print(f"Auth Error: {str(e)[:100]}")

if __name__ == "__main__":
    # Verify environment variables are loaded
    if not all([WP_URL, WP_USER, WP_PASSWORD]):
        print("Error: Missing environment variables. Check your .env file.")
        exit(1)
        
    print("WordPress.com Site Check")
    print("-" * 20)
    check_wordpress_access()