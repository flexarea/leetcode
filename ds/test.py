from collections import deque

# [20, 21, 23, 26, 28]
# now = 40


class SessionWindow:
    def __init__(self):
        self._timestamps = deque()

    def evict_old(self, now: float, window: float):
        cutoff = now - window
        while self._timestamps and self._timestamps[0] < cutoff:
            self._timestamps.popleft()

    def add(self, timestamp: float):
        self._timestamps.append(timestamp)

    def count(self) -> int:
        return len(self._timestamps)


store = {}  # apikey -> session  object
window = 60


def Allow(api_key: str, now: float) -> bool:

    # check for new api_key
    if api_key not in store:
        store[api_key] = SessionWindow()
        return True

    # evict
    store[api_key].evict_old(now, window)

    # check rate limit
    if store[api_key].count() >= 10:
        return False

    store[api_key].add(now)
    return True


seen_request = set()
timestamps = deque()
window = 30


def is_duplicate(request_id: str, now: float) -> bool:

    # evict old entries - worst case O(n)
    while timestamps and timestamps[0][0] < (now - window):
        _, old_id = timestamps.popleft()
        seen_request.discard(old_id)

    # duplicate check O(1)
    if request_id in seen_request:
        return True

    # check if it's a new request
    seen_request.add(request_id)
    timestamps.append((now, request_id))
    return False
