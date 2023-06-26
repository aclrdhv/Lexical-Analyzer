# Lexical Analyzer and Parser
Lexical Analyzer adalah sebuah fungsi untuk menganalisis grammar dalam pemrosesan bahasa. Fungsi ini membaca input teks dan memisah teks menjadi token.
Parser mengambil serangkaian token yang dihasilkan oleh Lexical Analyzer dan memeriksa apakah susunan token tersebut sesuai dengan aturan grammar yang ditentukan oleh struktur bahasa yang digunakan.
## Installation
**Requirements**
  * Python 3.0+
  * Windows, Linux, and macOS

Clone Repository
```bash
git clone https://github.com/aclrdhv/Lexical-Analyzer.git
```
Change Directory
```bash
cd Lexical-Analyzer
```

## Usage
**Run Program**

Linux / macOS
```bash
python3 main.py
```
Windows
```bash
py main.py
```
**Output Program**
```sh
aclrdhv@kali:~/Lexical-Analyzer$ python3 main.py
--------------------------------------------------Case Valid 1--------------------------------------------
hasil split: ['if', 'x', '==', 'z', ':', 'z', '=', 'y', '-', 'x', 'else', ':', 'z', '=', 'y', '*', 'x']
tokens: ['1', '5', '15', '5', '17', '5', '14', '5', '11', '5', '2', '17', '5', '14', '5', '12', '5', '#']

Hasil Parser
Inputan VALID karena sesuai dengan grammar
```
