# 🤖 Welcome to SimpleRisc Robot!

Hello, SimpleRisc Robot! Our world is made of 0s and 1s, and unfortunately, we cannot talk to humans—yet! 😢 But don't worry, I am here to help me! Use `unassemble.py` to understand what the binary world is saying.

---

## 🔄 Using the Disassembler (`unassemble.py`)

Have some binary code but don't know what it means? Use `unassemble.py` to convert it back into human-readable assembly!

### Usage:
```sh
python unassemble.py -f input.bin -o output.txt [-i]
```

### Options:
- `-h, --help` → Show help message.
- `-f, --file FILE` → Input file containing binary instructions.
- `-o, --output OUTPUT` → Output file to save the disassembled assembly.
- `-i, --include-binary` → Include binary instructions in the output for reference.

### 🔹 Example:
```sh
python unassemble.py -f machine_code.txt -o decoded.txt -i
```

---

## 🔍 Are You Human?
Oh... wait! You are not a robot? 🤖❌ Are you human?

Before we proceed, please verify that you're a human! 
<p align="center">
  <a href="https://www.youtube.com/watch?v=xvFZjo5PgG0" target="_blank">
  <img src="verifcation.png" alt="Human Verification" width="300px">
</p>

---

## 🛠 Using the Assembler (`assemble.py`)

Want to teach me how to think in 0s and 1s? Use `assemble.py` to convert human-readable assembly into machine code!

### Usage:
```sh
python assemble.py -f input.txt [options]
```

### Options:
- `-h, --help` → Show help message.
- `-f, --file FILE` → Assembly file to parse.
- `-t, --tokens` → Print tokenized instructions.
- `-e, --encode` → Print encoded instructions.
- `-b, --bin` → Generate binary output.
- `-hh, --hex` → Generate hex output.
- `-tb, --txtbin` → Save binary output to a text file.
- `-th, --txthex` → Save hex output to a text file.

### 🔹 Example:
```sh
python assemble.py -f program.txt -b
```
This command converts `program.txt` into binary machine code.

---

## 📂 Project Structure
```
├── README.md        # 📖 Project Documentation
├── assemble.py      # 🔄 Converts Assembly to Binary
├── unassemble.py    # 🔄 Converts Binary to Assembly
```

---

## 🌟 Features

✅ Convert Assembly to Binary  
✅ Convert Binary to Assembly  
✅ Tokenization & Instruction Encoding  
✅ Multiple Output Formats (Binary, Hex, Text)  
✅ Supports Labels & Immediate Values  

---

## 🤝 Contributing

Want to help improve SimpleRisc Robot? Here’s how:

- 🛠 Report issues and suggest improvements.
- 🔥 Submit pull requests with new features.
- 📖 Improve documentation.
- ⭐ Give this repository a star if you like it! ⭐

🚀 Let's bridge the gap between humans and machines!
