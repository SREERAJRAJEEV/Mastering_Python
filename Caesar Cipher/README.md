# Caesar Cipher Encryption and Decryption

This Python script implements the Caesar Cipher, a simple encryption technique where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features

- **Encryption**: Encrypts a message based on a specified shift value.
- **Decryption**: Decrypts a previously encrypted message using the same shift value.
- **Alphabet Support**: Handles lowercase English alphabets (a-z) for encryption and decryption.
- **Command-Line Interface**: Provides an interactive CLI for ease of use.

## Usage

1. **Copy the code from:**
   
   ```bash
   - main.py
   - logo.py
   ```

2. **Run the Script**

   ```bash
   python main.py
   ```

3. **Follow the Prompts**

   - Choose 'encode' to encrypt a message or 'decode' to decrypt a message.
   - Enter your message and specify the shift number.

4. **Output**

   - The encrypted or decrypted message will be displayed in the console.

## Example

### Encrypting a Message

```plaintext
$ python main.py
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
3
khoor
```

### Decrypting a Message

```plaintext
$ python main.py
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
khoor
Type the shift number:
3
hello
```

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Acknowledgments

- Inspired by the Caesar Cipher encryption technique.
- Built with Python 3.
