#!/usr/bin/env python3
import urllib.request
import os
import ipaddress

def main():
    # Dictionary mapping destination file paths to their raw source URLs
    urls = {
        "DoH/doh-ipv4.txt": "https://raw.githubusercontent.com/dibdot/DoH-IP-blocklists/refs/heads/master/doh-ipv4.txt",
        "DoH/doh-ipv6.txt": "https://raw.githubusercontent.com/dibdot/DoH-IP-blocklists/refs/heads/master/doh-ipv6.txt"
    }

    # Ensure the target local 'DoH' directory exists
    os.makedirs("DoH", exist_ok=True)

    for filepath, url in urls.items():
        print(f"Downloading blocklist from {url}...")
        
        # Open and read the remote text file
        req = urllib.request.urlopen(url)
        lines = req.read().decode("utf-8").splitlines()
        
        cleaned = []
        for line in lines:
            # Remove inline comments by splitting on '#' and taking the first part
            line_no_comment = line.split('#', 1)[0]
            stripped = line_no_comment.strip()
            
            # Skip empty lines
            if not stripped:
                continue
            
            try:
                # Validate that the string is a legitimate IP address
                ip = ipaddress.ip_address(stripped)
                
                # Enforce that IPv4 lists only get IPv4 addresses and IPv6 lists only get IPv6 addresses
                if "ipv4" in filepath and isinstance(ip, ipaddress.IPv4Address):
                    cleaned.append(stripped)
                elif "ipv6" in filepath and isinstance(ip, ipaddress.IPv6Address):
                    cleaned.append(stripped)
                else:
                    print(f"  -> Skipping mismatched IP type '{stripped}' for {filepath}")
                    
            except ValueError:
                # Catches syntax errors, domain names, or invalid IP structures
                print(f"  -> Skipping invalid IP format: '{stripped}'")
        
        # Write the clean, validated IP entries back out
        with open(filepath, "w") as f:
            f.write("\n".join(cleaned) + "\n")
            
        print(f"Successfully processed and saved {len(cleaned)} valid entries to {filepath}")

if __name__ == "__main__":
    main()
