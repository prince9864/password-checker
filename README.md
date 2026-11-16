# 🔐 Password Strength Checker

A simple, beginner-friendly Python program that checks whether a password is **WEAK**, **MEDIUM** or **STRONG**, and tells you how to improve it.

> ⚠️ **Learning project.** Don't type your real passwords into any tool you don't fully trust. For real password storage, use a trusted password manager such as Bitwarden, 1Password or KeePass.

---

## ✨ Features

- Scores a password out of 100
- Checks **length**, **character variety** and **common patterns**
- Explains *why* a password is weak and how to improve it
- Checks against a list of very common passwords
- Keeps asking for passwords until you type `quit`
- Uses only Python's built-in library, so there is nothing to install

---

## 🚀 How to Run

### Requirements
- Python 3 (check with `python --version`)

### Steps

1. Download or clone this repository:
   ```bash
   git clone https://github.com/prince9864/password-checker.git
   cd password-checker
   ```
2. Run the program:
   ```bash
   python password_checker.py
   ```
   On Mac or Linux, use `python3 password_checker.py`.
3. Type a password and press Enter.
4. Type `quit` to exit.

### Running in VS Code
1. Open the project folder with **File → Open Folder**.
2. Open `password_checker.py`.
3. Click the **▶ Run** button at the top right.
4. Click inside the terminal at the bottom and type a password.

---

## 🖥️ Example Output

```
=== Password Strength Checker ===
Type 'quit' to exit.

Enter a password to check: password

Score  : 5 / 100
Result : WEAK
How to improve:
  - Make it 12 or more characters long.
  - Add uppercase letters (A-Z).
  - Add numbers (0-9).
  - Add symbols like ! @ # $ %.
  - This is a very common password. Hackers try it first!

Enter a password to check: g7$Lm!qP9z#Xw2

Score  : 100 / 100
Result : STRONG
Great password! No problems found.
```

---

## 🧠 How the Score Works

| Check | Points |
|-------|--------|
| Length of 12 or more characters | 40 (8–11 characters gives 25, shorter gives 10) |
| Lowercase letters | +10 |
| Uppercase letters | +10 |
| Numbers | +10 |
| Symbols (`! @ # $` etc.) | +10 |
| No bad patterns | +20 bonus |
| Easy pattern such as `123`, `abc`, `qwe` | −15 |
| Same character 3 times in a row (`aaa`) | −10 |
| Found in the common password list | Score drops to 5 |

**Result:**

| Score | Result |
|-------|--------|
| Below 40 | WEAK |
| 40 to 69 | MEDIUM |
| 70 and above | STRONG |

---

## ⚠️ Limitations

- The common password list is small. Real lists have millions of entries.
- The scoring is simple. For example, `Sunny2024` scores STRONG even though it is a predictable style of password.
- The password is visible on screen while you type.
- The tool checks patterns only. It cannot tell whether a password has appeared in a data breach.

---

## 🔮 Ideas for Improvement

- [ ] Suggest a strong random password when the result is WEAK
- [ ] Store credentials behind a master password
- [ ] Flag reused passwords
- [ ] Load a bigger common password list from a file
- [ ] Add a simple GUI with Tkinter

---

## 📄 License

For educational use. Add a license of your choice (for example, MIT) before publishing.

## 👤 Author

**Rajkumar Shah**
GitHub: [@prince9864](https://github.com/prince9864)
