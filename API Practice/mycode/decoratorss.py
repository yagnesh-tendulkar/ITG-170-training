
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(u"⏱️ [Log] Starting execution...")
        result = func(*args, **kwargs)
        print(u"✅ [Log] Execution finished.")
        return result
    return wrapper

@log_execution
def fetch_data():
    print("Fetching records from the database...")

# Calling the function automatically triggers the decorator wrapper
fetch_data()
