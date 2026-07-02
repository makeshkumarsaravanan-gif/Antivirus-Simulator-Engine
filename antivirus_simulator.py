import os
import hashlib
import shutil

# 1. DATABASE OF KNOWN MALWARE SIGNATURES (SHA-256 Hashes)
# In reality, this would be a massive database. We are using sample hashes here.
MALWARE_DATABASE = {
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855": "Trojan.Dummy.Example",
    "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824": "Ransomware.Test.Mock"
}

# 2. FUNCTION TO CALCULATE SHA-256 HASH OF A FILE
def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Read the file in small chunks to handle large files efficiently
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"[-] Could not read file {file_path}: {e}")
        return None

# 3. SCANNER ENGINE
def scan_directory(target_folder, quarantine_folder):
    print(f"\n[+] Starting scan on folder: {target_folder}...")
    
    # Create quarantine folder if it doesn't exist
    if not os.path.exists(quarantine_folder):
        os.makedirs(quarantine_folder)
        print(f"[+] Created quarantine directory at: {quarantine_folder}")

    # Loop through all files in the directory
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip checking files that are already inside the quarantine folder
            if quarantine_folder in file_path:
                continue

            print(f"[*] Scanning: {file}...")
            file_hash = calculate_sha256(file_path)

            if file_hash:
                # 4. LOGIC TO COMPARE AND QUARANTINE
                if file_hash in MALWARE_DATABASE:
                    malware_name = MALWARE_DATABASE[file_hash]
                    print(f"\n[!!!] ALERT! Malicious file detected: {file}")
                    print(f"      Threat Name: {malware_name}")
                    print(f"      SHA-256: {file_hash}")
                    
                    # Move to quarantine
                    try:
                        dest_path = os.path.join(quarantine_folder, file)
                        shutil.move(file_path, dest_path)
                        print(f"[->] Successfully moved to Quarantine: {dest_path}\n")
                    except Exception as e:
                        print(f"[-] Failed to quarantine file: {e}\n")
                else:
                    # File is clean
                    pass

    print("[+] Scan complete.")

# 5. EXECUTION BLOCK
if __name__ == "__main__":
    # Define your local folders for testing
    # You can change these paths as needed
    TARGET_DIR = "./my_documents"
    QUARANTINE_DIR = "./quarantine"

    # Just creating a target folder automatically for your testing convenience
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        print(f"[!] Created a dummy target folder '{TARGET_DIR}'. Put your test files inside it.")

    scan_directory(TARGET_DIR, QUARANTINE_DIR)
