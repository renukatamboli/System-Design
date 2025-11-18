import time
class TokenBucket:
    def __init__(self, rate: float, capacity: float):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_check = time.time()

    def allow_request(self, tokens=1):
        now = time.time()
        elapsed = now - self.last_check
        self.last_check = now
        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False
