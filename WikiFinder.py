import requests
import time
from collections import deque
blacklist = (
    "Category:",
    "File:",
    "Image:",
    "Help:",
    "Special:",
    "Template:",
    "Portal:",
    "Wikipedia:"
)


cache = {}

def get_links(page):
    if page in cache:
        return cache[page]
    cache[page] = valid_links(page)
    return cache[page]

def valid_links(page_title):
    URL = "https://en.wikipedia.org/w/api.php"
    header = {
        "User-Agent": "WikiFinderBot/0.1 (EDU project; student; chitulescudragos@gmail.com)"
    }

    links = []
    param = {
        "action": "query",
        "titles": page_title,
        "prop": "links",
        "plnamespace": 0,
        "pllimit": "max",
        "format": "json",
    }

    while True:
        try:
            response = requests.get(URL, params=param, headers=header, timeout=5)
        except Exception as e:
            print("Request failed:", e)
            break
        #time.sleep(0.1)
        if response.status_code != 200:
            print("Bad status:", response.status_code)
            break

        try:
            data = response.json()
        except Exception as e:
            print("JSON error:", e)
            print(response.text[:200])
            break

        query = data.get("query")
        if not query:
            # print(data)
            break

        pages = query.get("pages", {})

        for page in pages.values():
            if "links" in page:
                for link in page["links"]:
                    title = link["title"]
                    title = title.split("#")[0]

                    if title.startswith(blacklist):
                        #time.sleep(0.2)
                        continue
                    if title.startswith("."):
                        #time.sleep(0.2)
                        continue


                    links.append(title)

        cont = data.get("continue")
        if not cont:
            break
        param.update(cont)

    return links


def find_path(start, target):
    queue = deque([start])
    visited = {start: None}
    while queue:
        current = queue.popleft()
        #print(current, "\n")

        if current == target:
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1]
        try:
            for nbh in get_links(current):
                if nbh not in visited:
                    visited[nbh] = current
                    queue.append(nbh)
        except TypeError:
            pass
    return None

while True:
    start = input("Start page (!please input the exact title!): ")
    target = input("Target page (!please input the exact title!): ")
    try:
        print(find_path(start, target))
        break
    except Exception as e:
        print(e)
        print("Invalid, try again.")
    break


