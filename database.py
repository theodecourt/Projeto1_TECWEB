import sqlite3
from dataclasses import dataclass


class Database:
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(str(self.db) + '.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,
                                            title TEXT,
                                            content TEXT NOT NULL);""")
        
    def add(self, note):
        self.conn = sqlite3.connect(str(self.db) + '.db')
        self.cur = self.conn.cursor()
        self.cur.execute("INSERT INTO note (title, content) VALUES (?, ?);", (note.title, note.content))   
        self.conn.commit()   

    def get_all(self):
        notas = []
        self.conn = sqlite3.connect(str(self.db) + '.db')
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT id, title, content FROM note")
        for linha in self.cur:
            nota = Note(id=linha[0], title=linha[1], content=linha[2])
            notas.append(nota)
        self.conn.commit() 
        return(notas)
    
    def update(self, entry):
        self.conn = sqlite3.connect(str(self.db) + '.db')
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE note SET title = '' WHERE id = entry")
        self.conn.commit()   

    def delete(self, note_id):
        self.conn = sqlite3.connect(str(self.db) + '.db')
        self.cur = self.conn.cursor()
        self.cur.execute("DELETE FROM note WHERE id = ?", (note_id,))
        self.conn.commit()

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''