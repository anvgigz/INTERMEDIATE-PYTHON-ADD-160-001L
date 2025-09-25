import os
from FileLoad_DataProcessing_Error import FileLoadError, DataProcessingError

# === Step 1: Define the file path ===
filename = "user_data.csv"
attempted_path = os.path.abspath(filename)

# === Step 2: Outer try block to catch DataProcessingError ===
try:
    # === Step 3: First level try block to catch FileLoadError ===
    try:
        print(f"Trying to open file at: {attempted_path}")
        
        # === Step 4: Try to open the file ===
        try:
            with open(attempted_path, 'r') as f:
                data = f.read()
                
                # === Step 5: Check if file is empty or unreadable ===
                if not data.strip():
                    raise DataProcessingError(
                        "File is empty or unreadable",
                        step="file loading"
                    )
        
        except FileNotFoundError as e:
            # Raise custom FileLoadError with cause
            raise FileLoadError(
                "File not found",
                filepath=attempted_path,
                original_exception=e
            ) from e

    # === Step 6: Catch FileLoadError and raise DataProcessingError ===
    except FileLoadError as e:
        raise DataProcessingError(
            "Failed to process user data",
            step="file loading",
            original_exception=e
        ) from e

# === Step 7: Final error handling ===
except DataProcessingError as e:
    e.log()

print("Program continues to run after handling exceptions.")
