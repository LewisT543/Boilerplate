
import sqlite3

# Basic CRUD+ database class:

class SQLiteDatabase:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.c = self.connection.cursor()

    def create_table(self, name):
        #TEMPLATE, MUST REPLACE VALUES
        create_str = '''CREATE TABLE IF NOT EXISTS <name> (
                     <id> INTEGER PRIMARY KEY,
                     <first_col> TEXT NOT NULL,
                     <second_col> INTEGER NOT NULL
                     );'''

    def add_item(self, item_dict):
        # SQL Injection vulnerable, but flexible for personal use.
        # qms = '(?,' + '?,' * (len(dict_keys) - 2) + '?)'
        # query_string = 'INSERT INTO ' + str(table) + ' VALUES ' + str(qms)

        # Use this instead: where table=<db_table_name> and the number of ?'s corresponds with the number of values being passed 
        query = 'INSERT INTO <table> VALUES <(?,?,...,?)>'
        self.c.execute(query, (item_dict.values(),))
        self.connection.commit()
    
    def update_item_by_x(self, item_id, new_val):
        query = 'UPDATE <table> SET <column_name> = ? WHERE <id> = ?'
        self.c.execute(query, (new_val, item_id))
        self.connection.commit()
    
    def delete_item(self, item_id):
        query = 'DELETE FROM <table> WHERE <id> = ?'
        self.c.execute(query, (item_id,))
        self.connection.commit()
    
    def print_rows(self):
        for row in self.c.execute('SELECT * FROM <table>'):
            print(row)

    def name_search(self, name):
        for row in self.c.execute('SELECT * FROM <table>'):
            if name in row:
                return row
        return None
    
    def id_search(self, id):
        for row in self.c.execute('SELECT * FROM <table> WHERE id = ?', (id, )):
            return row
        return None