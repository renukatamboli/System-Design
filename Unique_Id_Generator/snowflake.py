import time


class Snowflake:
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.sequence = 0
        self.last_timestamp = -1
        self.epoch = 1609459200000  # Custom epoch (January 1, 2021)

    def _current_timestamp(self):
        return int(time.time() * 1000)
    
    def generate_id(self):
        timestamp = self._current_timestamp()

        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & 0xFFF  # 12 bits for sequence

            if self.sequence == 0:
                while timestamp <= self.last_timestamp:
                    timestamp = self._current_timestamp()
        else:
            self.sequence = 0

        self.last_timestamp = timestamp
        id = ((timestamp - self.epoch) << 22) | (self.machine_id << 12) | self.sequence
        return id

if __name__ == "__main__":
    snowflake = Snowflake(machine_id=1)
    for _ in range(10):
        print(snowflake.generate_id())        
