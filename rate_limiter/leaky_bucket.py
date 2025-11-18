import time
class LeakyBucket:
    def __init__(self, capacity: int, leak_rate: float):
        """
        Initialize a Leaky Bucket rate limiter.

        :param capacity: Maximum number of tokens in the bucket.
        :param leak_rate: Rate at which tokens leak from the bucket (tokens per second).
        """
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.current_tokens = capacity
        self.last_check = time.time()
    
    def allow_request(self, tokens=1) -> bool:
        """
        Check if a request can be allowed based on the current state of the bucket.

        :param tokens: Number of tokens required for the request.
        :return: True if the request is allowed, False otherwise.
        """
        now = time.time()
        elapsed = now - self.last_check
        self.last_check = now

        # Calculate how many tokens have leaked out
        leaked_tokens = elapsed * self.leak_rate
        self.current_tokens = max(0, self.current_tokens - leaked_tokens)

        if self.current_tokens + tokens <= self.capacity:
            self.current_tokens += tokens
            return True
        return False