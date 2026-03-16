# Order Discount Processing – Python Assignment

## Project Description

This assignment demonstrates basic Python programming concepts such as:

* Conditional statements (`if / elif / else`)
* Loops (`for`, `while`)
* Lists
* Arithmetic operations
* User input handling
* Loop control (`break` and `continue`)

The program calculates discounts on orders, processes multiple orders, and demonstrates menu-driven interaction and loop control logic.

---

# Task 1 – Discount Rules

The program reads an **order amount entered by the user** and applies a discount based on predefined rules.

### Discount Structure

| Order Amount | Discount Applied |
| ------------ | ---------------- |
| ≥ 2000       | 15%              |
| 1500 – 1999  | 10%              |
| 1000 – 1499  | 7%               |
| < 1000       | No discount      |

### Example

```
Input:
Enter amount : 2500

Output:
order_amount 2125.0
```

---

# Task 2 – Process Multiple Orders

A list of order amounts is processed using a **for loop**.
The program applies the same discount rules to each order.

```
orders = [1200, 2500, 800, 1750, 3000]
```

For each order the program prints:

```
order_amount -> discount% -> final_amount
```

### Example Output

```
1200 -> 7 % -> 1116
Total revenue 1116

2500 -> 15 % -> 2125
Total revenue 3241

800 -> 0 % -> 800
Total revenue 4041
```

---

# Task 3 – User Menu (While Loop)

This task implements a **menu-driven program using a while loop**.
The program keeps running until the user chooses to quit.

### Menu Options

```
1 – Add order amount
2 – Show all orders and totals after discounts
q – Quit
```

### Features

* Uses a **while loop** to continuously display the menu
* Stores orders in a **list**
* Uses **continue** to handle invalid input
* Uses **break** to exit when the user presses `q`
* Calculates the total revenue after applying discounts to all orders

### Example Menu

```
Menu
1 - Add order amount
2 - Show all orders and totals
q - Quit
```

---

# Task 4 – Loop Control with Conditions

This task demonstrates how **break and continue** control loop execution.

The program processes daily sales data:

```
daily_sales = [200, 150, 0, 400, 50, -1, 300]
```

### Rules Applied

* If a value is **-1**, the data is considered corrupted and the loop **breaks**.
* If a value is **0**, it represents a day with no sales and the program **continues** to the next iteration.
* Positive sales values are added to the **running total**.

### Example Output

```
Running total: 200
Running total: 350
Day with no sales
Running total: 750
Running total: 800
Corrupted data
Final total: 800
```

---

# Key Concepts Demonstrated

* Python **conditional logic**
* **Loops (`for`, `while`)**
* **break and continue statements**
* **List data structure**
* **Menu-driven program design**
* Maintaining a **running total**
* Basic **error handling and input validation**

---

# Author

**Abhinav Kumar**
