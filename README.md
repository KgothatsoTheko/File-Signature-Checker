# File Signature Checker

## Description
This project contains a **Python script** that checks a file’s **signature (magic number)** to identify its real file type.  
The script performs **static analysis only** and does **not execute** any files.

It is used to demonstrate how suspicious files (including malware) can be detected even if they use fake file extensions.

---

## Script File
- `file_signature_checker.py`

---

## How It Works
1. Opens a file in binary mode
2. Reads the first 4 bytes
3. Compares them to known file signatures
4. Prints the detected file type
5. Displays a warning if the file is an executable

---

## Files Included
- `file_signature_checker.py` – Python script for checking file signatures
- `README.md` – Project documentation
- `malshare_sample.bin` – Malware sample (renamed for safety)
- `Que-es-Malware.png` – sample image

---

## Requirements
- Python 3.x
- Windows Command Prompt (or Terminal)
- Malware samples: https://github.com/mikesiko/PracticalMalwareAnalysis-Labs

---

## How to Run

1. Open Command Prompt
2. Navigate to the folder containing the script
3. Run: python file_signature_checker.py
4. Enter the file name when prompted: malware_sample.bin or Que-es-Malware.png.png
5. Results

## Safety Notes
- Files are never executed
- Malware samples are renamed to `.bin`
- Script only reads file bytes
- Static analysis only

---

## Screenshot Section

 <img width="753" height="141" alt="image" src="https://github.com/user-attachments/assets/fd2b5542-7f5d-4a56-bd93-4e5a58b0df38" />

<img width="1702" height="908" alt="image" src="https://github.com/user-attachments/assets/6102abd2-a84d-4e7e-9822-0d8b4c500f2e" />

## Conclusion
This script shows how **file signature checking** can quickly identify suspicious executable files using a simple and safe Python program.
