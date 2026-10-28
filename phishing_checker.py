"""
EWB Phishing URL Awareness Checker

This program checks URL text for common warning signs.
It never opens or visits a URL.
"""

import ipaddress
from urllib.parse import urlsplit


def check_url(url):
    """Return a list of warning signs found in a URL."""

    url = url.strip()

    if not url:
        raise ValueError("No URL entered. Please enter a URL.")

    try:
        parsed = urlsplit(url)
        hostname = parsed.hostname
    except ValueError:
        raise ValueError("Malformed URL. Please check the URL format.")

    if not parsed.scheme or not parsed.netloc or not hostname:
        raise ValueError(
            "Malformed URL. Include a scheme and hostname, "
            "for example https://www.example.com"
        )

    warnings = []
    hostname = hostname.lower()

    # Warning sign 1: @ symbol
    if "@" in url:
        warnings.append(
            "Contains an @ symbol; inspect carefully."
        )

    # Warning sign 2: URL longer than 100 characters
    if len(url) > 100:
        warnings.append(
            "URL is unusually long (more than 100 characters)."
        )

    # Warning sign 3: IP address used as hostname
    try:
        ipaddress.ip_address(hostname)
        warnings.append(
            "Uses an IP address instead of a familiar domain."
        )
    except ValueError:
        pass

    # Warning sign 4: Five or more hostname segments
    # IPv6 addresses are excluded from this hostname-segment check.
    if ":" not in hostname and len(hostname.split(".")) >= 5:
        warnings.append(
            "Contains many hostname segments/subdomains."
        )

    # Warning sign 5: Punycode marker
    if "xn--" in hostname:
        warnings.append(
            "Contains a punycode-style hostname."
        )

    # Warning sign 6: HTTP scheme
    if parsed.scheme.lower() == "http":
        warnings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    return warnings


def main():
    """Run the interactive URL checker."""

    print("=" * 48)
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")
    print("=" * 48)

    while True:
        url = input(
            "\nEnter a sample URL (or type q to quit): "
        ).strip()

        if url.lower() in ("q", "quit", "exit"):
            print("Thank you for using the checker.")
            break

        try:
            warnings = check_url(url)

            print("\nResult:")

            if warnings:
                for warning in warnings:
                    print(f"- {warning}")

                print(
                    f"\nREVIEW CAREFULLY: "
                    f"{len(warnings)} warning sign(s) found."
                )
            else:
                print("No warning signs found.")
                print(
                    "This does NOT guarantee that the URL is safe."
                )

        except ValueError as error:
            print(f"\nInput error: {error}")

        print(
            "\nReminder: Never enter passwords or OTPs "
            "because an unexpected link asks you to."
        )


if __name__ == "__main__":
    main()
