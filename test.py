# test.py
"""
Docstring
"""

import secrets

def main():
    for _ in range(10):
        print(secrets.randbelow(1_000_000))
        
if __name__ == "__main__":
    main()
