import time


class RateLimiter:

    def __init__(self):
        # user_id -> {action: last_time}
        self.user_actions = {}

    def is_allowed(self, user_id: int, action: str, limit_seconds: int = 5):

        now = time.time()

        if user_id not in self.user_actions:
            self.user_actions[user_id] = {}

        last_time = self.user_actions[user_id].get(action)

        if last_time:
            if now - last_time < limit_seconds:
                return False

        self.user_actions[user_id][action] = now
        return True


rate_limiter = RateLimiter()