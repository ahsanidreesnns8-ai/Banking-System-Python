# Banking-System-Python
This is Console Based Bankinf System Project with techniques,logics and security.
# Banking System Simulation 🏦

An Object-Oriented Python application that simulates the core functionalities of a banking system, including deposits, withdrawals, and account statement generation. This project highlights the use of **Classes and Objects** to manage secure user data and financial records.

## 🚀 Overview

Developed as a **1st Semester project**, this system focuses on secure data handling and logic-driven transactions. It includes features like PIN-limited attempts to simulate real-world ATM security.

## ✨ Features

- **Object-Oriented Design:** Uses a `Bank` class to encapsulate account details such as holder name, PIN, issuance/expiry dates, and balance.
- **Secure Transactions:**
  - **PIN Verification:** Required for every transaction.
  - **Security Lockout:** Implements a 3-attempt limit for PIN entry; after three failures, the account access is denied to simulate a security block.
- **Deposit Module:** Allows users to add funds to their account with real-time balance updates and timestamps.
- **Withdrawal Module:** - Includes a **funds-check** to prevent withdrawing more than the available balance.
  - Updates the account state immediately upon successful verification.
- **Account Statement (Bill):** Generates a professional, formatted receipt displaying the account holder's information, transaction summary, and the current balance.
- **Visual UX:** Features terminal loading animations (0-100%) to provide feedback during "database" searches.

## 🛠️ Technical Implementation

- **Class Structure:** Manages state through `self` attributes, ensuring each `Account` object maintains its own independent data.
- **Input Validation:** Uses loops and conditional logic to verify PINs and withdrawal amounts.
- **Standard Libraries:** - `time`: Used for UI loading effects.
  - `datetime`: Used for precise logging of transactions.

## 🚀 How to Run

1. **Prerequisites:** Ensure you have Python 3.x installed.
2. **Setup:** Download `Banking System(1st Semester) Project.py`.
3. **Execution:**
   ```bash
   python "Banking System(1st Semester) Project.py"

## Author
M. Ahsan Idrees
