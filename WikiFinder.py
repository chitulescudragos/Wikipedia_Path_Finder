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
    queue_s = deque([start])
    queue_t = deque([target])
    visited_s = {start: None}
    visited_t = {target: None}
    while queue_t and queue_s:
        current = queue_s.popleft()
        try:
            for nbh in get_links(current):
                if nbh not in visited_s:
                    visited_s[nbh] = current
                    queue_s.append(nbh)
                    if nbh in visited_s:
                        return intersection(nbh, visited_s, visited_t)

        except TypeError:
            pass

        current = queue_t.popleft()
        try:
            for nbh in get_links(current):
                if nbh not in visited_t:
                    visited_t[nbh] = current
                    queue_t.append(nbh)
                    if nbh in visited_s:
                        return intersection(nbh, visited_s, visited_t)

        except TypeError:
            pass
    return None


def intersection(meet_point, visited_s, visited_t):
    path_s = []
    node = meet_point
    while node is not None:
        path_s.append(node)
        node = visited_s[node]
    path_s.reverse()
    path_t = []
    node = visited_t[meet_point]
    while node is not None:
        path_t.append(node)
        node = visited_t[node]

    return path_s + path_t



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
