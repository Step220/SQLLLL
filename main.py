import sqlite3
class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
class SimpleORM:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    def create_table(self, table_name, **columns):
        columns_with_type = ', '.join([f'{col} {dtype}' for col, dtype in columns.items()])
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} '
                            f'(id INTEGER PRIMARY KEY, {columns_with_type})')
        self.conn.commit()
    def insert(self, table_name, **data):
        columns = ', '.join(data.keys())
        placeholder = ', '.join(['?'] * len(data))
        self.cursor.execute(f'INSERT INTO {table_name} ({columns}) '
                            f' VALUES({placeholder})', tuple(data.values()))
        self.conn.commit()
    def update_quantity(self, table_name, target_name, new_quantity):
        self.cursor.execute(f'UPDATE {table_name} SET Quantity = ? WHERE Name = ?',
                            (new_quantity, target_name))
        self.conn.commit()
    def delete_by_quantity(self, table_name, target_quantity):
        self.cursor.execute(f'DELETE FROM {table_name} WHERE Quantity = ?',
                            (target_quantity,))
        self.conn.commit()
        self.conn.close()
    def get_raw_data(self, table_name):
         self.cursor.execute(f'SELECT * FROM {table_name}')
         return self.cursor.fetchall()
test = SimpleORM(":memory:")
test.create_table('Products', name="TEXT", text="REAL", Quantity="INTEGER")
test.insert('Products', Name="Laptop", Price=1200.50, Quantity=5)
test.insert('Products', Name="Phone", Price=800.00, Quantity=10)
test.insert('Products', Name="Tablet", Price=300.00, Quantity=0)
test.insert('Products', Name="Laptop", Price=1200.50, Quantity=5)
test.insert('Products', Name="Phone", Price=800.00, Quantity=10)
test.update_quantity('Products', "Laptop", 10)
test.delete_by_quantity('Products', 0)
result = test.get_raw_data('Products')
print( )