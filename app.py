import re

SENSITIVE_KEYWORDS = [
    "password",
    "secret",
    "api_key",
    "token",
    "private_key"
]

def scan_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()

        print("\nScanning file for sensitive data...\n")

        found = False

        for keyword in SENSITIVE_KEYWORDS:
            if re.search(keyword, content, re.IGNORECASE):
                print(f"⚠ Found sensitive keyword: {keyword}")
                found = True

        if not found:
            print("✅ No sensitive data found.")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    file_path = input("Enter file path to scan: ")
    scan_file(file_path)
