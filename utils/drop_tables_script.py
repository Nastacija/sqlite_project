sql_drop = """
DROP TABLE IF EXISTS sentences;
DROP TABLE IF EXISTS morphemes
""".strip()

with open("sqlite_drop_tables.sql", "w", encoding="UTF-8") as wh:
  wh.write(sql_drop)