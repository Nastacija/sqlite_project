sql_query = """
CREATE TABLE sentences (
 sentence TEXT NOT NULL
);

CREATE TABLE morphemes (
 word TEXT NOT NULL,
 morphemes TEXT NOT NULL
);
""".strip()

with open("sqlite_create_tables.sql", "w", encoding="UTF-8") as wh:
  wh.write(sql_query)