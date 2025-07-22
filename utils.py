import os

def save_wordlist(wordlist, filename="wordlists/custom_wordlist.txt"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(word + '\n')
    print(f"[+] Wordlist saved to {filename}")
