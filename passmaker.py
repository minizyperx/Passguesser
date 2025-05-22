#!/usr/bin/env python3
import itertools  #for generating combinations 
import argparse   #for cli for hacker based interface
from datetime import datetime
import os #

# Fancy banner
def print_banner():
    banner = r"""
 ___             _     _   _             
|  _|_ _ _ _ ___| |___|_|_| |___ ___     
|  _| | |_'_| . | | . | | . | -_|  _|    
|_| |___|_,_|  _|_|___|_|___|___|_| v1.0 
            |_|                          
Password Wordlist Generator - by minizyperx
"""
    print(banner)

# Generate combinations
def generate_combinations(inputs):
    inputs = [item for item in inputs if item]
    combos = set()

    # Add base inputs
    for word in inputs:
        combos.add(word.lower())
        combos.add(word.capitalize())
        combos.add(word.upper())

    # Combine inputs
    for r in range(2, 4):  # 2 and 3 word combos
        for combo in itertools.permutations(inputs, r):
            joined = ''.join(combo)
            combos.add(joined)
            combos.add(joined.lower())
            combos.add(joined.upper())
            combos.add(joined.capitalize())

    # Append numbers/symbols
    extended = set()
    for word in combos:
        for suffix in ["123", "1234", "@123", "!", "@", "2024"]:
            extended.add(word + suffix)
    combos |= extended

    return sorted(combos)

# Save to .txt with unique filename
def save_to_file(words, filename):
    base, ext = os.path.splitext(filename)
    counter = 0
    final_filename = filename

    while os.path.exists(final_filename):
        counter += 1
        final_filename = f"{base}{counter}{ext}"

    with open(final_filename, 'w') as f:
        for word in words:
            f.write(word + '\n')

    print(f"[+] Saved {len(words)} passwords to '{final_filename}'")

# Main logic
def main():
    print_banner()

    parser = argparse.ArgumentParser(description="Generate password wordlists from personal info")
    parser.add_argument("--nickname", help="Nickname")
    parser.add_argument("--dob", help="Date of Birth (e.g., 23052005)")
    parser.add_argument("--birthyear", help="Birth Year")
    parser.add_argument("--age", help="Age")
    parser.add_argument("--mobile", help="Mobile Number")
    parser.add_argument("--email", help="Email ID")
    parser.add_argument("--partner", help="Partner Name")
    parser.add_argument("--parents", help="Parents' Name")
    parser.add_argument("--siblings", help="Siblings' Name")
    parser.add_argument("--school", help="School Name")
    parser.add_argument("--college", help="College Name")
    parser.add_argument("--workplace", help="Workplace")
    parser.add_argument("--department", help="Department")
    parser.add_argument("--hometown", help="Hometown")
    parser.add_argument("--currentcity", help="Current City")
    parser.add_argument("--favplace", help="Favourite Place")
    parser.add_argument("--actor", help="Favourite Actor")
    parser.add_argument("--hobbies", help="Hobbies")
    parser.add_argument("--pet", help="Pet Name")
    parser.add_argument("--vehicle", help="Vehicle Number")
    parser.add_argument("--output", help="Output filename", default="passlist.txt")

    args = parser.parse_args()

    # Gather all inputs into a list
    inputs = [
        args.nickname, args.dob, args.birthyear, args.age,
        args.mobile, args.email, args.partner, args.parents,
        args.siblings, args.school, args.college, args.workplace,
        args.department, args.hometown, args.currentcity,
        args.favplace, args.actor, args.hobbies, args.pet,
        args.vehicle
    ]

    # Generate and save passwords
    passwords = generate_combinations(inputs)
    save_to_file(passwords, args.output)

if __name__ == "__main__":
    main()

    #for all hackers
