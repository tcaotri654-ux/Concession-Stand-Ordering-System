# 🍿 Concession Stand Program

A Python command-line program that simulates a movie theater concession stand. Users can browse a menu, customize orders, choose sizes, remove ingredients, and order combo deals.

---

## Files

| File | Description |
|------|-------------|
| `concession_stand.py` | Main program |
| `GUIDE.md` | Full guide (English) |

---

## Requirements

- Python 3.6 or higher
- No external libraries needed

---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/your-username/concession-stand.git
cd concession-stand
```

**2. Run the program**
```bash
python concession_stand.py
```

---

## How to Order

**Step 1 — Type the food you want:**
```
enter the food you want to order (q to quit): hamburger
```

You can type a general name like `hamburger` or go straight to a specific type like `big mac`, `chili dog`, `curly`, etc.

**Step 2 — Customize your order:**

For burgers and hot dogs, the program shows ingredients and asks if you want to remove anything:
```
Ingredients for Big Mac: ['beef patty', 'special sauce', 'lettuce', 'cheese', 'pickles', 'onions', 'sesame bun']
enter ingredient to remove (or press Enter to skip):
```

**Step 3 — Choose a size:**
```
1. Small  - $0.00
2. Medium - $0.50
3. Large  - $1.00
enter size (1/2/3):
```

**Step 4 — Type `q` to finish and see your receipt.**

---

## Menu

| Item | Price |
|------|-------|
| Hot Dog | $2.50 |
| Hamburger | $3.00 |
| Fries | $1.50 |
| Soda | $1.00 |
| Popcorn | $2.00 |
| Chips | $1.25 |

### Combos (On Sale)

| Combo | Includes | Price | You Save |
|-------|----------|-------|----------|
| Burger Combo | Hamburger + Fries + Soda | $4.50 | $1.00 |
| Hot Dog Combo | Hot Dog + Fries + Soda | $3.75 | $0.75 |
| Family Combo | 2x Burger/Hotdog + 2x Fries + 2x Soda | $9.00 | $2.00 |

---

## Tax

- Fewer than 10 items → 5% tax
- 10 or more items → 10% tax

---

## Example Order

```
enter the food you want to order: big mac

Ingredients for Big Mac: ['beef patty', 'special sauce', 'lettuce', 'cheese', 'pickles', 'onions', 'sesame bun']
enter ingredient to remove (or press Enter to skip): special sauce
updated ingredients: ['beef patty', 'lettuce', 'cheese', 'pickles', 'onions', 'sesame bun']

1. Small  - $1.00
2. Medium - $1.25
3. Large  - $2.00
enter size (1/2/3): 2

Medium Big Mac Hamburger added to cart. current total: $4.25

enter the food you want to order: q

--------------------
your order summary:
--------------------
- Medium big mac hamburger
--------------------
subtotal: $4.25
tax (1 items): $0.21
total: $4.46
```
