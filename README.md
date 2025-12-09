Wikipedia Path Finder
=====================

Finds the shortest hyperlink path between two Wikipedia articles using Python and breadth-first search (BFS).
You give it a starting page and a destination page, and it figures out the shortest chain of links that connects them.

What it can do
--------------
- Gets internal Wikipedia links via the public API
- Handles pagination (pages with many links)
- Uses BFS to guarantee the shortest path
- Works across most Wikipedia pages
- Designed to be improved and optimized

How it works (short version)
----------------------------
1. Start from a given page.
2. Get every link found on that page.
3. Explore linked pages level-by-level.
4. Stop once the target page is found.
5. Rebuild and print the full path.

Example
-------
From:
Cristian Cherchez
To:
Dâmbovița County

Possible output:
Cristian Cherchez → AFC Chindia Târgoviște → Dâmbovița County

Installing
----------
You only need the 'requests' package:

pip install requests

Files
-----
WikiFinder.py | main code logic
README.txt    | this file

Future improvements
-------------------
- Caching responses to reduce API calls
- Bidirectional BFS (much faster)
- Graph visualization
- Multiple shortest route options
- Web interface

Notes
-----
This is a prototype intended for learning, experimenting, and exploring Wikipedia's link structure.

Author
------
Chiţulescu Dragoș-Mihai

Feel free to fork, test, and improve.
