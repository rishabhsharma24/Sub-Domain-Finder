import requests
import argparse

def find_subdomains(domain, wordlist):
    """
    Find subdomains for a given domain using a wordlist.
    
    :param domain: The target domain.
    :param wordlist: The path to the wordlist file containing possible subdomains.
    :return: A list of discovered subdomains.
    """
    discovered_subdomains = []

    try:
        with open(wordlist, 'r') as file:
            subdomains = file.read().splitlines()

        print(f"Scanning subdomains for {domain}...\n")

        for subdomain in subdomains:
            full_url = f"http://{subdomain}.{domain}"
            try:
                response = requests.get(full_url, timeout=3)
                if response.status_code < 400:
                    print(f"[+] Found: {full_url}")
                    discovered_subdomains.append(full_url)
            except requests.ConnectionError:
                pass
    except FileNotFoundError:
        print("Wordlist file not found. Please provide a valid file.")
    
    return discovered_subdomains


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Finder Tool")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist file")

    args = parser.parse_args()

    domain = args.domain
    wordlist = args.wordlist

    # Start the subdomain finding process
    results = find_subdomains(domain, wordlist)

    print("\n[!] Scanning completed.")
    if results:
        print("\nDiscovered subdomains:")
        for subdomain in results:
            print(f"- {subdomain}")
    else:
        print("No subdomains found.")
