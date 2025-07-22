import argparse
from analyzer import analyze_password
from generator import generate_wordlist
from utils import save_wordlist

def main():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer + Wordlist Generator")
    parser.add_argument('--password', type=str, required=True, help='Password to analyze')
    parser.add_argument('--inputs', nargs='*', help='Personal info like name, pet, birthyear')
    parser.add_argument('--export', action='store_true', help='Export wordlist to txt')

    args = parser.parse_args()

    print("\n🔐 Analyzing Password...")
    result = analyze_password(args.password)
    print(f"Entropy: {result['entropy']} bits")
    print(f"Strength: {result['strength']}")

    if args.inputs:
        print("\n🛠 Generating custom wordlist...")
        wordlist = generate_wordlist(args.inputs)
        print(f"Generated {len(wordlist)} entries")

        if args.export:
            save_wordlist(wordlist)

if __name__ == '__main__':
    main()
