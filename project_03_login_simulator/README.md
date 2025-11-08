# Login Simulator

This Python project simulates a simple login system where the user has up to three attempts to enter the correct username and password.

---

## 🔹 How It Works

1. The program starts with `attempts = 0`.
2. It uses a `while` loop that allows the user to try logging in up to 3 times.
3. Each time, the program asks for a **username** and **password**.
4. If the input matches the correct credentials (`name == "reza"` and `password == 1234`), the program prints `"Welcome!"` and stops.
5. If the credentials are wrong, it prints `"Try again."` and increases the attempt count.
6. After 3 failed tries, the program prints `"Too many tries. Access denied."`.

---

## 🔹 Features

- Allows a maximum of 3 login attempts
- Checks username and password
- Displays clear success/failure messages

---

## 🔹 Example Output
