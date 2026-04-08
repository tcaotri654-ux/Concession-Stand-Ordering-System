# 📋 Concession Stand — How It Works

## 1. Program Structure

The program is built around **dictionaries** and **functions**.

### Dictionaries (Data)

```
menu                  → base price of each item
menu_combos           → combo deals with items, price, and savings
fries_type            → fries types + surcharge
soda_flavor           → soda flavors + surcharge
popcorn_flavor        → popcorn flavors + surcharge
chips_flavor          → chips flavors + surcharge
burger_ingredients    → burger types + list of ingredients
hot_dog_ingredients   → hot dog types + list of ingredients

cart = []             → shopping cart (list of ordered items)
total = 0             → running total price
```

---

## 2. Functions

### `add_tax(amount)`
Calculates tax based on number of items in cart.

```python
if len(cart) >= 10:
    tax_rate = 0.10    # 10% tax for 10+ items
else:
    tax_rate = 0.05    # 5% tax for fewer than 10 items
```

Example:
- 5 items, total = $10.00 → tax = $0.50
- 12 items, total = $20.00 → tax = $2.00

---

### `size_up()`
Handles size selection for fries, soda, popcorn, chips, and hot dog.

Returns `(size_name, extra_price)`:
- Small → `("small", 0.00)`
- Medium → `("medium", 0.50)`
- Large → `("large", 1.00)`

---

### `size_hamburger()`
Handles size selection specifically for burgers.

Returns `(size_name, size_price)`:
- Small → `("small", 1.00)`
- Medium → `("medium", 1.25)`
- Large → `("large", 2.00)`

> **Note:** `size_up()` returns an *extra* charge on top of the base price. `size_hamburger()` returns the *total* size price — this is because burger sizes have higher fixed prices.

---

### `add_hamburger(choice=None)`
Handles burger ordering, ingredient removal, and size selection.

**Flow:**
```
1. If choice is None → ask user which burger type
2. Check if choice exists in burger_ingredients
   ✅ Found  → show ingredients, ask to remove one
   ❌ Not found → print error, return 0.00
3. Call size_hamburger() → get size and price
4. Build name: f"{size} {choice} hamburger"
5. Append to cart
6. Return price (menu["hamburger"] + size_cost)
```

**Why `choice=None`?**
So the function can be called two ways:
```python
add_hamburger()         # user types "hamburger" → ask which type
add_hamburger("big mac") # user types "big mac" directly → skip asking
```

---

### `add_hot_dog(choice=None)`
Same logic as `add_hamburger()` but uses `hot_dog_ingredients` and `size_up()`.

---

### `add_fries()`, `add_soda()`, `add_popcorn()`, `add_chips()`
All follow the same pattern:

```
1. Ask user which type/flavor
2. Check if it exists in the dictionary
   ✅ Found  → call size_up(), calculate price, append to cart
   ❌ Not found → print error, return 0.00
3. Price = flavor_surcharge + size_cost
4. Return price
```

Example for `add_fries()`:
```
User picks: curly fries + large
Price = fries_type["curly"] + size_cost
      = 0.50 + 1.00
      = 1.50
```

---

### `add_combos()`
Handles combo ordering.

```
1. Show available combos
2. Ask user which combo
3. Check if it exists in menu_combos
   ✅ Found  → loop through items, append each to cart
   ❌ Not found → print error, return 0.00
4. Return combo price (already discounted)
```

The combo uses a **nested dictionary**:
```python
menu_combos["burger combo"]["items"]    → ["hamburger", "fries", "soda"]
menu_combos["burger combo"]["price"]    → 4.50
menu_combos["burger combo"]["savings"]  → 1.00
```

---

## 3. Main Loop Flow

```
while True:
    user types food name
    
    → "q"                    : break out of loop
    → ""                     : ask again
    → food in menu           : add base price, call add_xxx()
    → food in burger_ingredients : add menu["hamburger"], call add_hamburger(food)
    → food in hot_dog_ingredients: add menu["hot dog"], call add_hot_dog(food)
    → food in menu_combos    : call add_combos()
    → anything else          : print error
```

**Why check `burger_ingredients` separately?**

When a user types `big mac`, it is not in `menu` — only `hamburger` is. So the program checks `burger_ingredients` next, adds the base hamburger price manually, then passes `"big mac"` straight into `add_hamburger()` to skip asking again.

---

## 4. Receipt

When the user types `q`:

```
1. Print all items in cart
2. Print subtotal
3. Calculate tax with add_tax(total)
4. Print tax amount
5. Print final total (subtotal + tax)
```

---

## 5. Full Example

```
User: big mac
→ total += menu["hamburger"]        → total = 3.00
→ add_hamburger("big mac")
   - show ingredients
   - user removes: nothing
   - user picks size: Medium ($1.25)
   - cart.append("Medium Big Mac Hamburger")
   - return 3.00 + 1.25 = 4.25
→ total += 4.25                     → total = 7.25

User: curly
→ total += menu["fries"]            → total = 8.75
→ add_fries() called with "curly"
   - user picks size: Small ($0.00)
   - cart.append("small curly fries")
   - return 0.50 + 0.00 = 0.50
→ total += 0.50                     → total = 9.25

User: q
→ cart = ["Medium Big Mac Hamburger", "small curly fries"]
→ subtotal: $9.25
→ tax (2 items): $9.25 × 0.05 = $0.46
→ total: $9.71
```
