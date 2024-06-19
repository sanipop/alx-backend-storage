# Redis Basic - ALX Backend Storage

This project focuses on basic operations using Redis, a powerful in-memory data structure store. By completing this project, you'll gain hands-on experience in using Redis as a simple cache and performing various Redis operations using Python.

## Curriculum Overview

- **Specialization**: Back-end
- **Topic**: Redis
- **Project Duration**: June 19, 2024, 6:00 AM to June 20, 2024, 6:00 AM
- **Checker Release**: June 19, 2024, 12:00 PM
- **Auto Review**: At the deadline

## Learning Objectives

- Perform basic operations with Redis.
- Use Redis as a simple caching mechanism.

## Requirements

- **OS**: Ubuntu 18.04 LTS
- **Python**: Python 3.7
- **Code Style**: PEP 8 (pycodestyle version 2.5)
- **Documentation**: Modules, classes, functions, and methods must have comprehensive docstrings.
- **Type Annotations**: All functions and coroutines must include type annotations.

## Setup Instructions

### Install Redis on Ubuntu 18.04

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

### Start Redis Server

To start Redis when using a container:

```bash
$ service redis-server start
```

## Tasks

### 0. Writing Strings to Redis

Create a `Cache` class:
- In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` and flush the instance using `flushdb`.
- Implement a `store` method that generates a random key, stores the input data in Redis using this key, and returns the key. Type-annotate the method to handle data types: `str`, `bytes`, `int`, and `float`.

**Example:**

```python
#!/usr/bin/env python3
import redis
import uuid

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
```

### 1. Reading from Redis and Recovering Original Type

Implement:
- A `get` method that retrieves data and optionally converts it using a provided callable.
- `get_str` and `get_int` methods that utilize `get` with appropriate conversion functions.

**Example:**

```python
#!/usr/bin/env python3

class Cache:
    # previous code

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        return self.get(key, int)
```

### 2. Incrementing Values

Implement a `count_calls` decorator to count how many times methods of the `Cache` class are called. Use `functools.wraps` to maintain function metadata.

**Example:**

```python
#!/usr/bin/env python3
from functools import wraps

def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    # previous code

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
```

### 3. Storing Lists

Implement a `call_history` decorator to store input and output history of a function.

**Example:**

```python
#!/usr/bin/env python3

def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper

class Cache:
    # previous code

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
```

### 4. Retrieving Lists

Implement a `replay` function to display the call history of a particular function.

**Example:**

```python
#!/usr/bin/env python3

def replay(method: Callable):
    self = method.__self__
    inputs = self._redis.lrange(f"{method.__qualname__}:inputs", 0, -1)
    outputs = self._redis.lrange(f"{method.__qualname__}:outputs", 0, -1)
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input, output in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input.decode('utf-8')}) -> {output.decode('utf-8')}")

class Cache:
    # previous code
```

## Repository Structure

- **GitHub Repository**: `alx-backend-storage`
- **Directory**: `0x02-redis_basic`
- **Primary File**: `exercise.py`

## Resources

- [Redis Crash Course Tutorial](https://example.com)
- [Redis Commands](https://example.com)
- [Redis Python Client](https://example.com)
- [How to Use Redis With Python](https://example.com)

## Author

- **ALX, 2024**

All rights reserved.
