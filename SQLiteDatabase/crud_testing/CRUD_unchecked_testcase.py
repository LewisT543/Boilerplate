
import sqlite3

# Basic CRUD+ database class:

class SQLiteDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('test_db.db')
        self.c = self.connection.cursor()
        self.create_table()

    def create_table(self):
        #TEMPLATE, MUST REPLACE VALUES
        self.c.execute('''CREATE TABLE IF NOT EXISTS test_table (
                     id INTEGER PRIMARY KEY,
                     number INTEGER NOT NULL,
                     astring VARCHAR(40) NOT NULL
                     );''')

    def add_item(self, item_dict):
        # SQL Injection vulnerable, but flexible for personal use.
        # qms = '(?,' + '?,' * (len(dict_keys) - 2) + '?)'
        # query_string = 'INSERT INTO ' + str(table) + ' VALUES ' + str(qms)

        # Use this instead: where table=<db_table_name> and the number of ?'s corresponds with the number of values being passed 
        query = 'INSERT INTO test_table (number, astring) VALUES (?,?)'
        
        num = item_dict['number']
        string = item_dict['astring']
        
        self.c.execute('INSERT INTO test_table (number, astring) VALUES (?,?)', (num, string))
        self.connection.commit()
    
    def update_item_by_x(self, item_id, new_val):
        query = 'UPDATE test_table SET number = ? WHERE id = ?'
        self.c.execute(query, (new_val, item_id))
        self.connection.commit()
    
    def delete_item(self, item_id):
        query = 'DELETE FROM test_table WHERE id = ?'
        self.c.execute(query, (item_id,))
        self.connection.commit()
    
    def print_rows(self):
        for row in self.c.execute('SELECT * FROM test_table'):
            print(row)

    def name_search(self, name):
        for row in self.c.execute('SELECT * FROM test_table'):
            if name in row:
                return row
        return None
    
    def id_search(self, id):
        for row in self.c.execute('SELECT * FROM test_table WHERE id = ?', (id, )):
            return row
        return None

new_db = SQLiteDatabase()
data = {"number": 10, "astring": 'dog'}
new_db.add_item(data)
new_db.print_rows()
new_db.update_item_by_x(1, 25)
new_db.print_rows()
new_db.delete_item(1)
new_db.print_rows()
new_db.delete_item(2)
new_db.delete_item(3)