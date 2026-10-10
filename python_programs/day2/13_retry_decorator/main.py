import functools
from typing import Any, Callable, Tuple, Type

# a decorator function will wrap the wrapper function which contains the retry logic
# @retry(3) = retry(3)(flaky)
def retry(
    max_attempts: int,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable[[Callable[..., Any]], Callable[..., Any]]: # 1. Configures retry behavior
    """Return a decorator that retries the function up to max_attempts calls in total."""

    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")
    
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]: # 2. Receives the target function
        @functools.wraps(func)
        def wrapper(*args, **kwargs): # 3. Wraps the target function with retry logic
            attempts = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise

        return wrapper

    return decorator



def main():
    calls = {"n": 0}

    @retry(3)
    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise ConnectionError(f"attempt {calls['n']} failed")
        return "ok"

    print("result =", flaky())
    print("calls made =", calls["n"])


if __name__ == "__main__":
    main()