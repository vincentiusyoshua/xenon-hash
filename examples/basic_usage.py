from src.xenon_hash import XenonHash

def main():
    # Create hasher instance
    hasher = XenonHash(debug=True)
    
    # Basic usage
    message = "Hello, World!"
    hash_value = hasher.hash(message)
    print(f"Input: {message}")
    print(f"Hash: {hash_value}\n")
    
    # Multiple inputs
    test_inputs = [
        "The quick brown fox jumps over the lazy dog",
        "Lorem ipsum dolor sit amet",
        "1234567890",
        "Special characters: !@#$%^&*()",
    ]
    
    for input_str in test_inputs:
        hash_value = hasher.hash(input_str)
        print(f"Input: {input_str}")
        print(f"Hash: {hash_value}\n")

if __name__ == "__main__":
    main()