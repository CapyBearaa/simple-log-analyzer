def analyze_logs(file_path):
    suspicious_keywords = ["ERROR", "FAILED", "WARNING"]

    with open(file_path, "r") as file:
        for line in file:
            for keyword in suspicious_keywords:
                if keyword in line:
                    print(f"[!] Suspicious activity found: {line.strip()}")

if __name__ == "__main__":
    analyze_logs("logs.txt")