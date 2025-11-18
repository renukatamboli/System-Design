import time
class SlidingWindowCounter:
    def __init__(self, window_size, max_requests, request_rate):
        """
        Initialize a Sliding Window Counter rate limiter.

        :param window_size: Size of the sliding window in seconds.
        :param max_requests: Maximum number of requests allowed in the window.
        :param request_rate: Rate at which requests are counted (requests per second).
        """
        self.window_size = window_size
        self.max_requests = max_requests
        self.request_rate = request_rate
        self.request_counts = []

    def allow_request(self):
        """
        Check if a request can be allowed based on the rolling window logic.

        :return: True if the request is allowed, False otherwise.
        """
        now = time.time()
        window_start = now - self.window_size
        prev_window_start = window_start - self.window_size

        # Split requests into previous and current window
        current_window_requests = [count for timestamp, count in self.request_counts if window_start <= timestamp < now]
        previous_window_requests = [count for timestamp, count in self.request_counts if prev_window_start <= timestamp < window_start]

        # Calculate overlap percentage (position in current window)
        overlap_percentage = 1 - ((now - window_start) / self.window_size)
        # Clamp to [0, 1]
        overlap_percentage = max(0, min(1, overlap_percentage))

        total_requests = sum(current_window_requests)
        total_requests += sum(previous_window_requests) * overlap_percentage

        # Round down as per example
        total_requests = int(total_requests)

        if total_requests < self.max_requests:
            self.request_counts.append((now, 1))
            return True
        return False