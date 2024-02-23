import requests

def scrape_local_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("Failed to fetch HTML. Status code:", response.status_code)
            return None
    except requests.RequestException as e:
        print("Error fetching HTML:", e)
        return None

if __name__ == "__main__":
    url = "http://connect.com"  # Replace with the URL of your local server
    html_content = scrape_local_html(url)
    if html_content:
        print(html_content)  # Print or process the HTML content as needed

