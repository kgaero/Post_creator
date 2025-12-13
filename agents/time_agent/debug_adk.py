import sys
import os

try:
    # Attempt to import the registry
    from google.adk.models import registry
    print("Successfully imported registry.")
    
    # Try to find a 'resolve' function or similar
    if hasattr(registry, 'resolve'):
        resolver = registry.resolve
        print("Found 'resolve' function.")
    elif hasattr(registry, 'ModelRegistry'):
        print("Found 'ModelRegistry' class.")
        # Try to instantiate or usage
        resolver = None
    else:
        print("Could not find 'resolve' or 'ModelRegistry'. Dir:", dir(registry))
        resolver = None

    # Test candidates if we have a resolver
    candidates = [
        "gemma-2-27b-it",
        "models/gemma-2-27b-it",
        "google/gemma-2-27b-it",
        "vertex_ai/gemma-2-27b-it",
        "gemini-1.5-flash" # Control
    ]

    if resolver:
        for c in candidates:
            try:
                print(f"Testing '{c}'...")
                res = resolver(c)
                print(f"  -> VALID. Type: {type(res)}")
            except Exception as e:
                print(f"  -> INVALID: {e}")
    
    # Print what models might be available if there's a list
    # Inspect registry for any lists
    for attr in dir(registry):
        if "MODEL" in attr.upper() or "REGISTRY" in attr.upper():
            val = getattr(registry, attr)
            if isinstance(val, (list, dict, set)):
                print(f"Found potential model list '{attr}': {val}")

except Exception as e:
    print(f"An error occurred: {e}")
    # Print path to help user troubleshooting
    print("Python path:", sys.path)
