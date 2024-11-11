from typing import Any

import time


def trying_with_intervals(timing):
    def decorator(func):
        def wraper(*args, **kwargs) -> Any:
            while True:
                res = func(*args, **kwargs)
                if res is not None:
                    break
                print("sleep", args, kwargs)
                time.sleep(timing)
            return res
        return wraper
    return decorator