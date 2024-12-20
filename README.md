# Study Class Restaurant
<img src="https://github.com/user-attachments/assets/17347b6b-0354-41ff-9de1-188f2927f6d0" width="200" height="200" alt="logo_study_restaurant">


This is the backend of a restaurant system, developed to manage menu items and apply discounts. The project includes the following main classes:

- **Restaurant**: Main class representing the restaurant.
- **MenuItem**: Parent class for menu items.
  - **DrinkItem**: Child class representing drinks.
  - **DishItem**: Child class representing dishes.

## Features

- Add items to the menu.
- List menu items.
- Apply discounts to items.
- Change status from active to inactive and vice versa
- Add rating
- Calcule average rating
- List all restaurants (Class method)

## Project Structure

```plaintext
study_class_restaurant/
├── Include/
├── Lib/
├── Scripts/
├── models/
│   ├── reviews.py
│   ├── restaurant.py
│   └── menu/
│       ├── drinkItem.py
│       ├── menuItem.py
│       └── dishItem.py
├── app.py
├── pyvenv.cfg
├── .gitignore
└── README.md
```

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/Lucas-I-Marciano/study_class_restaurant.git
   ```
2. Navigate to the project directory:
   ```bash
   cd study_class_restaurant
   ```

## Contribution

Contributions are welcome! Feel free to open issues and pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
