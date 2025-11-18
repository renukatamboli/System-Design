import time
class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, window_size: float):
        """
        Initialize a Sliding Window rate limiter.

        :param max_requests: Maximum number of requests allowed in the window.
        :param window_size: Size of the sliding window in seconds.
        """
        self.max_requests = max_requests
        self.window_size = window_size
        self.request_timestamps = []
    
    def allow_request(self) -> bool:
        """
        Check if a request can be allowed based on the current state of the sliding window.

        :return: True if the request is allowed, False otherwise.
        """
    
        now = time.time()
        # Remove timestamps that are outside the sliding window
        self.request_timestamps = [timestamp for timestamp in self.request_timestamps if now - timestamp < self.window_size]

        if len(self.request_timestamps) < self.max_requests:
            self.request_timestamps.append(now)
            return True
        return False