import requests

def check_robots_txt(url):
    robots_url = url + "/robots.txt"
    response = requests.get(robots_url)
    if response.status_code == 200:
        print(f"robots.txt for {url}:\n{response.text}")
        return response.text
    else:
        print(f"No robots.txt found for {url}")
        return None

def analyze_robots_txt(robots_txt, user_agent="*"):
    disallowed_paths = []
    lines = robots_txt.split("\n")
    user_agent_found = False
    
    for line in lines:
        line = line.strip()
        if line.startswith("User-agent"):
            user_agent_found = (user_agent in line or "*" in line)
        if user_agent_found and line.startswith("Disallow"):
            path = line.split(":")[1].strip()
            disallowed_paths.append(path)
        if line == "":
            user_agent_found = False
    
    return disallowed_paths

# URLs of the websites
urls = ["https://www.99acres.com", "https://www.magicbricks.com", "https://www.nobroker.in"]

for url in urls:
    robots_txt = check_robots_txt(url)
    if robots_txt:
        disallowed_paths = analyze_robots_txt(robots_txt)
        print(f"Disallowed paths for {url}: {disallowed_paths}")
