def log(message, error=False):
    prefix = "[ERROR]" if error else "[INFO]"
    print(f"{prefix} {message}")
