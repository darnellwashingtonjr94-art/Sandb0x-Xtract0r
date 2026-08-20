# Payloads Directory (`/payloads`)

This directory stores raw, encrypted, and test payloads utilized by the `Sandb0x-Xtract0r` engine. 

## Storage Guidelines
* **Never commit raw, unencrypted malware or active shellcode to this repository.** 
* All payloads must be encrypted using the provided `AES-256-GCM` utility script before being merged.

## Included Test Payloads
1. `calc_shellcode.enc`: A benign payload that spawns `calc.exe`. Used for verifying extraction and memory injection success.
2. `msgbox_test.enc`: Spawns a basic Windows message box to test UI interaction capabilities within the sandbox.

## Payload Generation
To encrypt a new raw payload for the extractor:
```bash
python3 ../scripts/encrypt_payload.py --in my_raw.bin --out my_encrypted.enc --key <256-bit-key>
