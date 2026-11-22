from fastmcp import FastMCP
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__),"expenses.db")

mcp = FastMCP("ExpenseTracker")

def init_db():
  with sqlite3.connect(DB_PATH) as c:
    c.execute("""
        CREATE TABLE IF NOT EXIST expenses(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          data TEXT NOT NULL,
          amount REAL NOT NULL,
          category TEXT NOT NULL,
          subcategory TEXT DEFAULT '',
          not TEXT DEFAULT ''
        )
    """)

init_db()

@mcp.tool
def add_expenses(data, amount, category , subcategory="",note=""):
  with sqlite3.connect(DB_PATH) as c:
    
