# file signature checker
# Script reads the first bytes of a file to identify its type

def check_signature(file_path):
    # Known file signatures
    signatures = {
        b"MZ": "Windows Executable (.exe)",
        b"%PDF": "PDF file",
        b"PK": "ZIP file",
        b"\x89PNG": "PNG image",
        b"GIF": "GIF image"
    }

    try:
        # Open file in binary mode
        file = open(file_path, "rb")
        first_bytes = file.read(4)
        file.close()

        print("File analyzed:", file_path)
        print("File signature (hex):", first_bytes.hex())

        # Check file signature
        for sig in signatures:
            if first_bytes.startswith(sig):
                print("Detected file type:", signatures[sig])

                if sig == b"MZ":
                    print("WARNING: This is an executable file and may be malicious.")

                return

        print("Unknown file type. This could be suspicious.")

    except:
        print("Error: Could not read the file.")

# Run the function
file_name = input("Enter file name or path: ")
check_signature(file_name)
