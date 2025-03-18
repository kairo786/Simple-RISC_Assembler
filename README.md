# 🛠️ SimpleRISC Assembler

A user-friendly web-based assembler for the SimpleRISC architecture. Write your assembly code and instantly convert it into machine-readable hexadecimal or binary instructions.

---

## 🚀 Features

- **Interactive Web Interface**: Easily input and assemble your assembly code directly from your browser.
- **Syntax Highlighting**: Enhanced readability and debugging with built-in syntax highlighting (powered by CodeMirror).
- **Hexadecimal \& Binary Output**: Toggle between hexadecimal and binary representations of machine code.
- **Detailed Error Reporting**: Clear, informative error messages to help debug assembly code quickly.

---

## 📂 Project Structure

```
SimpleRISC-Assembler/
├── app.py                # Flask backend server
├── assembler.py          # Core assembler logic (two-pass assembler)
├── index.html            # Frontend web interface
└── README.md             # Project documentation (this file)
```

---

## ⚙️ Technologies Used

### Backend:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/latest/)


### Frontend:

- HTML, CSS, JavaScript
- [CodeMirror](https://codemirror.net/) (Syntax highlighting)

---

## 🛠️ Installation \& Setup

Follow these steps to set up and run the project locally:

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd SimpleRISC-Assembler
```

(Replace `<your-repository-url>` with your actual repository URL.)

### Step 2: Set Up Python Environment

Create a virtual environment (recommended):

```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

Install required dependencies:

```bash
pip install flask
```


### Step 3: Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and navigate to:

```
http://localhost:5000
```

---

## 📖 Usage Instructions

1. Enter your SimpleRISC assembly code in the provided editor.
2. Select "Show Binary Output" if you prefer binary representation (optional).
3. Click the **Assemble** button.
4. View your assembled machine code displayed clearly on-screen.

---

---

## 📌 Features

- **Interactive Web Interface**: Write and assemble assembly code directly in your browser.
- **Syntax Highlighting**: Integrated CodeMirror editor for clear and readable assembly code.
- **Binary & Hexadecimal Output**: Easily toggle between binary and hexadecimal representations of machine code.
- **Robust Error Handling**: Clear, informative error messages to help debug assembly code.
- **Two-Pass Assembly Process**:
  - First pass identifies labels and addresses.
  - Second pass encodes instructions into machine-readable binary format.

---


## 💻 Supported Instructions

| Instruction Type | Mnemonics Supported                             |
|------------------|--------------------------------------------------|
| Data Movement    | `mov`, `ld`, `st`, `ncp`                         |
| Arithmetic       | `add`, `sub`, `mul`, `div`, `mod`, `cmp`         |
| Logical          | `and`, `or`, `not`                               |
| Shift Operations | `isl`, `isr`, `asr`                              |
| Branching        | Unconditional: `b`, `call`, `ret`Conditional: `.beg`, `.bgt` |

---

## 📌 Example Usage

### Assembly Code Example:
```assembly

@1. Example

mov R1, #10
mov R2, #20
add R3, R1, R2
st R3, [R0]


```

### Output:
The assembler generates machine code in both binary and hexadecimal formats displayed clearly on the web interface.

---

## ⚠️ Common Challenges & Solutions

| Challenge                 | Solution Provided                                 |
|---------------------------|---------------------------------------------------|
| Label Resolution Errors   | Two-pass assembler resolves labels accurately.    |
| Incorrect Register Usage  | Robust validation ensures registers within range (R0-R15). |
| Immediate Parsing Issues  | Supports decimal (`#10`), hexadecimal (`#0xA`), binary (`#0b1010`). |
| Branch Offset Calculation | Automatically calculates relative offsets correctly. |

---

## 📚 Future Enhancements

- Integration with a SimpleRISC simulator/emulator for direct execution of assembled programs.
- Support for multiprocessor simulations or FPGA-based hardware implementations.
---

## 🚩 Troubleshooting Common Issues

- **"Network Error" or Backend Not Running**:
    - Ensure Flask server (`app.py`) is running correctly on port `5000`.
- **Assembly Errors**:
    - Check syntax carefully. The assembler provides detailed error messages to help you pinpoint issues.

---

## 🤝 Contribution Guidelines

Contributions are welcome! Feel free to open issues or pull requests for bug fixes, improvements, or new features.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 📧 Contact \& Support

For questions or support, please open an issue in this repository or contact the maintainer directly.

Happy assembling! 🚀

---

## 📅 Last Updated

Tuesday, March 18, 2025
