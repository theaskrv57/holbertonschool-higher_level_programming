import sqlite3
import os

def create_database():
    # Əgər fayl artıq varsa, silirik
    if os.path.exists('products.db'):
        os.remove('products.db')

    # Yeni SQLite bazasını yaradıb əlaqə qururuq
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Cədvəl yaradılır
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Məlumatlar əlavə olunur
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    # Dəyişiklikləri yadda saxlayırıq və bağlantını bağlayırıq
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    print("Database created successfully!")
