# Concession Stand Program

## Overview
This project is a simple concession stand ordering program written in Python. It lets a user order items such as hamburgers, hot dogs, fries, soda, popcorn, chips, and combos. The program supports:
- item selection
- size selection
- custom burger/hot dog ingredient removal
- combo orders
- tax calculation

## Files
- `concession_stand_programs.py` - main program logic
- `HUONG_DAN_CONCESSION_STAND.md` - Vietnamese guide
- `GUIDE_CONCESSION_STAND_ENGLISH.md` - English guide

## How the program works
1. The program defines dictionaries for the menu and item options.
2. It prints the menu, then enters a loop to ask the user for an order.
3. If the user enters an item in `menu`, the base price is added.
4. For items like fries, soda, popcorn, chips, and hot dog, the program asks for a type and size.
5. For burgers, the program checks `burger_ingredients` to handle specific burger names such as `big mac` or `quarter pounder with cheese`.
6. Each valid order is appended to `cart` and its price is added to `total`.
7. When the user quits, the program prints the order summary and calculates tax with `add_tax()`.

## Key functions
- `add_tax(amount)`
  - Determines tax rate: 5% for fewer than 10 items, 10% for 10 or more.

- `size_up()`
  - Shows size options for fries, soda, popcorn, chips, and hot dog.
  - Returns `(size_name, extra_price)`.

- `size_hamburger()`
  - Shows burger size options.
  - Returns `(size_name, total_size_price)`.

- `add_hamburger(choice=None)`
  - Handles burger ordering, ingredient removal, and size selection.

- `add_hot_dog(choice=None)`
  - Handles hot dog ordering, ingredient removal, and size selection.

- `add_fries()`, `add_soda()`, `add_popcorn()`, `add_chips()`
  - Handle the specific logic for each item type.

## Notes
- `menu` contains only base item names and base prices.
- `burger_ingredients` is used so the program can recognize specific burger names.
- The code can be extended to support new combos by adding them to `combos` and checking `elif food in combos:` in the ordering loop.

## Vietnamese summary
1. `menu` lưu giá cơ bản của mỗi loại.
2. `burger_ingredients` lưu các burger cụ thể và thành phần của chúng.
3. `add_hamburger()` xử lý chọn burger, loại bỏ nguyên liệu, chọn size.
4. `add_hot_dog()` xử lý chọn hot dog giống vậy.
5. Với fries/soda/popcorn/chips, hàm `size_up()` trả về giá thêm theo size.
6. Khi user nhập `big mac`, chương trình dùng `elif food in burger_ingredients` vì `big mac` không có trong `menu`.

## How to use
1. Run `python3 concession_stand_programs.py`.
2. Enter an item name from the menu or burger list.
3. Follow prompts for size and ingredient removal.
4. Enter `q` to finish and see your receipt.

## GitHub repository
I cannot directly create a GitHub repo from this environment, but you can copy this folder into a repository and publish it. The `README.md` file is ready to use as your project README.
