Wikipedia Path Finder
=====================

A Python tool that finds the shortest hyperlink path between two Wikipedia pages.
Enter a starting page and a target page, and it returns the exact sequence of links connecting them.

What It Does
------------
- Queries Wikipedia using the official public API
- Returns the shortest valid link path (not approximate, not heuristic — *always shortest*)
- Uses dual-direction BFS (bidirectional search) for significantly reduced search time
- Eliminates disambiguation pages to avoid meaningless expansions
- Deduplicates links for better performance
- Caches visited pages locally in memory during a run to avoid repeated API calls
- Validates backlink correctness (only accepts real reversals)
- Handles Wikipedia pagination (max link limits per response)

Purpose
-------
This project is centered around correctness:
It **never sacrifices the shortest path guarantee** for speed.
If the shortest path exists, this tool is designed to find it.

Tradeoff:  
It *may* take longer than a heuristic or local-graph-based model, but it returns the actual shortest path.

Example
-------
Input:
  Start page: Land
  Target page: Lando Norris

Output:
  Land → International Space Station → United Kingdom → Bristol → Lando Norris

Tech Summary
------------
✔ Official Wikipedia API  
✔ Forward BFS + Reverse BFS  
✔ Backlink validation  
✔ Avoids disambiguation traps  
✔ Link deduplication  
✔ On-the-fly caching  
✔ Guaranteed minimum path length  

Install
-------
Requires the `requests` package.

    pip install requests

Run
---

    python WikiFinder.py

File Overview
-------------
WikiFinder.py    # Core implementation
README.txt       # This documentation

Core Design Choices
-------------------
- **Bidirectional BFS** is used because BFS complexity is exponential; meeting in the middle reduces runtime massively
- **Using backlinks** helps control the search when forward exploration grows too quickly, reducing wasted expansions. 
- **Deduplication** ensures minimal duplicate state exploration
- **Excluding disambiguation pages** prevents exponential pollution of the search frontier
- **Local run-time caching** avoids repeated API fetches within the same execution

Future Improvements
-------------------
- Search time optimizations (without losing correctness)
- On-disk persistent caching (optional mode)
- Parallel request batching
- Visualization of routes using graph tools
- Public web interface / hostable version

Notes
-----
- The program prioritizes correctness over raw speed.
- It may take longer on long or rare pairings, but its output is guaranteed valid.
- Designed as a technical exploration tool, not an enterprise-grade search engine.

Author
------
Dragoș Chițulescu
