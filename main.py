from functions import plaintext_formatter, whois_lookup, iptables_generator, json_formatter

import argparse

if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-f", "--format",
                           default="iptables",
                           const="iptables",
                           nargs="?",
                           type=str,
                           choices=("iptables", "plain", "jsonl"),
                           help="Output format of IP address list (default: %(default)s)")

    args = argParser.parse_args()

    addresses: list[dict] = []

    # Get IP Addresses To Ban
    for address in whois_lookup.get_ips():
        addresses.append(address)

    # Generate IP Table Rules
    if args.format == "iptables":
        # IP Tables Commands
        for rule in iptables_generator.generate_iptable_rules(addresses=addresses):
            print(rule)
    elif args.format == "plain":
        # Just Plain Addresses
        for address in plaintext_formatter.format_addresses(addresses=addresses):
            print(address)
    elif args.format == "jsonl":
        # JSON Formatted Addresses
        for address in json_formatter.format_addresses(addresses=addresses):
            print(address)
    else:
        print(f"Unknown format: `{args.format}`")