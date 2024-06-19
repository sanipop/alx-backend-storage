#!/usr/bin/env python3
import requests
import redis
from functools import wraps
from typing import Callable

# Connect to Redis server
r = redis.Redis()

def cache_page(expiration: int = 10):
    """
    Decorator to cache the page and track URL access count.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            # Track the number of accesses to the URL
            count_key = f"count:{url}"
            r.incr(count_key)

            # Check if the page is already cached
            cached_page = r.get(url)
            if cached_page:
                return cached_page.decode('utf-8')

            # Fetch the page content
            page_content = func(url)

            # Cache the page content with an expiration time
            r.setex(url, expiration, page_content)

            return page_content
        return wrapper
    return decorator

@cache_page(expiration=10)
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a given URL and returns it as a string.
    """
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"
    print(get_page(url))
    # To test the caching and counting, you can run get_page multiple times
    # and observe the behavior.
    print(f"Access count for {url}: {r.get(f'count:{url}').decode('utf-8')}")
    
