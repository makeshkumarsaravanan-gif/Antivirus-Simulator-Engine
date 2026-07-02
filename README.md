# Antivirus Simulator Engine

A lightweight, behavioral Signature-Based Antivirus Simulator written in Python. This security tool demonstrates malware identification mechanisms by auditing specific application directories, analyzing digital signatures (SHA-256 cryptographic hashes), and mitigating threats via isolated file quarantine deployment.

---

## 🚀 How It Works (Core Mechanics)

The system operates based on static file analysis pipelines structured across three critical phases:

1. **Static Directory Auditing:** The engine recursively parses a targeted storage location (e.g., `./my_documents`) to extract tracking paths of all local computational payloads.
2. **Cryptographic Signature Verification:** It extracts data from every file block and computes a distinct **SHA-256 Hardware Signature Checksum**. This signature is cross-referenced with a secure global dynamic threat data definitions repository containing unique malware definitions (e.g., `Trojan.Dummy.Example`).
3. **Quarantine Containment Mitigation:** Once an anomalous, modified, or identified signature matches the database block, the analyzer flags it immediately. It cuts off local execution vulnerabilities by revoking file paths and safely shifting the payload structure into an isolated sandbox storage space (`./quarantine/`).

---

## 🛠️ File System Architecture

```text
Antivirus_Project/
├── antivirus_simulator.py  # Core Signature Engine & Scanning Mechanism
├── my_documents/           # Primary Storage Testbed Directory
│   ├── clean_file.txt      # Safe target operational data payload
│   └── empty_virus.txt     # Test virus simulation container
├── output/                 # Project documentation / Report folder
├── quarantine/             # Sandboxed threat isolation storage space
└── .gitignore              # Safeguards runtime environment parameters from deployment

⚙️ Setup & Live Execution Guide
Follow these sequential parameters inside your Linux terminal workspace to deploy and test the toolchain architecture:

1. Project Directory Assembly
Ensure your localized files and testing data models are initialized before running the simulation engine loops:

Bash
cd ~/Desktop/Antivirus_Project

# Initialize verification vectors and operational documents
mkdir -p my_documents quarantine
touch my_documents/clean_file.txt

# Generate an evaluation signature container to test the detection loop
touch my_documents/empty_virus.txt
2. Live Simulator Scanning Execution
Run the system scan using the core engine layout parameters:

Bash
python3 antivirus_simulator.py
3. Simulation Target Test Log Trace Matrix
During runtime configurations, the console output details real-time threat detection metrics as follows:

Plaintext
[+] Starting scan on folder: ./my_documents...
[*] Scanning: clean_file.txt...
[*] Scanning: empty_virus.txt...

[!!!] ALERT! Malicious file detected: empty_virus.txt
      Threat Name: Trojan.Dummy.Example
      SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
[->] Successfully moved to Quarantine: ./quarantine/empty_virus.txt

[+] Scan complete.
