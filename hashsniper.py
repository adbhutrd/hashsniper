#!/usr/bin/env python3
"""HashSniper — Password hash cracking orchestration tool"""
import hashlib, argparse, json, sys
from typing import List

class HashSniper:
    def __init__(self):
        self.cracked = {}
    
    def identify_hash(self, hash_str: str) -> str:
        lengths = {32: "MD5", 40: "SHA1", 56: "SHA224", 64: "SHA256", 96: "SHA384", 128: "SHA512"}
        return lengths.get(len(hash_str), "Unknown")
    
    def crack(self, hash_str: str, wordlist: List[str]) -> str:
        hash_type = self.identify_hash(hash_str)
        print(f"[HashSniper] Identified: {hash_type}")
        print(f"Testing {len(wordlist)} passwords...")
        
        for password in wordlist:
            test_hash = hashlib.sha256(password.encode()).hexdigest()
            if test_hash == hash_str:
                print(f"[CRACKED] Password found: {password}")
                return password
        return None

def main():
    parser = argparse.ArgumentParser(description="HashSniper - Hash Cracking Tool")
    parser.add_argument("hash", help="Hash to crack")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file")
    args = parser.parse_args()
    
    with open(args.wordlist) as f:
        words = [line.strip() for line in f if line.strip()]
    
    sniper = HashSniper()
    result = sniper.crack(args.hash, words)
    
    if result:
        print(f"Successfully cracked: {result}")
    else:
        print("Hash not found in wordlist")

if __name__ == "__main__":
    main()
