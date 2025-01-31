def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone
    
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f"{fn.__name__}: called{run_dt}")
        
        return result

    return inner