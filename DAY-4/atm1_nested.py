def process_atm_transaction():
    print("--- ATM System Initializing ---")
    
    try:
        # PRIMARY TRY: Attempt to connect to the main database
        print("Status: Connecting to Main Server...")
        # Simulating a failure (e.g., server timeout)
        raise ConnectionError("Main Server is not responding.")

    except ConnectionError as e:
        print(f"Warning: {e}")
        
        # NESTED TRY: This is our 'Plan B'
        try:
            print("Status: Attempting to connect to Backup Server...")
            # Let's say the backup server is also down
            raise ConnectionError("Backup Server is also offline.")
        
        except ConnectionError as e2:
            # Handling the failure of Plan B
            print(f"Critical Error: {e2}")
            print("Result: Transaction Cancelled. Please try again later.")
            
        else:
            print("Result: Connected to Backup Server. Processing...")

    else:
        # Runs only if the PRIMARY TRY succeeded
        print("Result: Connected to Main Server. Processing...")

    finally:
        # Always runs to ensure the user's session is safe
        print("Status: Ejecting Card. Session Closed.")
        print("--- Thank you for visiting ---")

# Execute the function
process_atm_transaction()