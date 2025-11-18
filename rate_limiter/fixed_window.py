import time
class FixedWindow:
    def __init__(self, window_size, max_requests):
        """Initialize the fixed window rate limiter.
        
        :param window_size: Size of the fixed window in seconds.
        :param max_requests: Maximum number of requests allowed in the window.
        """
        self.window_size = window_size
        self.max_requests = max_requests
        self.data = []

    def allow_request(self):
        current_time = time.time()
        window_start = current_time - self.window_size

        # Remove data points that are outside the fixed window
        self.data = [timestamp for timestamp in self.data if timestamp >= window_start]

        if len(self.data) < self.max_requests:
            self.data.append(current_time)
            return True
        return False