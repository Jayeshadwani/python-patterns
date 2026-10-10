import functools
import time
from typing import Any, Callable



# timer func will be a decorator function, that acts as a wrapper 
# and logs the time before and after running the inner function 
# with last_elapsed attribute
def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Wrap func so the duration of its last call is stored in wrapper.last_elapsed."""
    @functools.wraps(func) # Preserve the original function's metadata (name, docstring, etc.)
    def wrapper(*args, **kwargs): 
        start = time.perf_counter() 
        try:
            result = func(*args, **kwargs)
        finally:
            wrapper.last_elapsed = time.perf_counter() - start

        return result 

    wrapper.last_elapsed = 0.0 
    return wrapper
    


@timer
def slow_add(a, b=0):
    """Add two numbers slowly."""
    time.sleep(0.05)
    return a + b


def main():
    print("slow_add(1, b=2) =", slow_add(1, b=2))
    print("last_elapsed =", round(slow_add.last_elapsed, 2))
    print("name =", slow_add.__name__)


if __name__ == "__main__":
    main()