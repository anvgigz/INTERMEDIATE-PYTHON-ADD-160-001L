try:
    number = int("Not a number")
except ValueError as e:
    print(f"Error: {e}")
    # Accessing additional information
    print(f"Encoding: {e.encoding if hasattr(e, 'encoding') else 'N/A'}")
    print(f"Reason: {e.reason if hasattr(e, 'reason') else 'N/A'}")
    
    
#      Why "Encoding" and "Reason" Are "N/A"
# - The ValueError raised by int() does not have encoding or reason attributes.
# - Those attributes are found in other exceptions like UnicodeDecodeError.
# - So hasattr(e, 'encoding') and hasattr(e, 'reason') both return False, and you get "N/A" for each.
