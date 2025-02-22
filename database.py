import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
token_db = os.getenv('DB_TOKEN')
class StoryDatabase:
    def __init__(self):
        self.conn = psycopg2.connect(token_db)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS stories (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                role TEXT NOT NULL,
                location TEXT NOT NULL,
                story TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def save_story(self, name, role, location, story):
        self.cursor.execute("""
            INSERT INTO stories (name, role, location, story)
            VALUES (%s, %s, %s, %s)
        """, (name, role, location, story))
        self.conn.commit()

    def get_all_stories(self):
       
        self.cursor.execute("SELECT * FROM stories")
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
