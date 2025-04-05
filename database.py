import sqlite3

def create_tables(con):
    try:
        con.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            jwt_token TEXT
        )
        """)

        con.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id TEXT PRIMARY KEY,
            start_date TEXT DEFAULT (datetime('now')),
            user_id TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)
        
        con.execute("""
        CREATE TABLE IF NOT EXISTS interactions (
            id TEXT PRIMARY KEY,
            conversation_id TEXT,
            interaction_type TEXT CHECK (interaction_type IN ('request', 'response')) NOT NULL,
            topic TEXT DEFAULT 'none',
            subject TEXT DEFAULT 'none',
            FOREIGN KEY(conversation_id) REFERENCES conversations(id)
        )
        """)

        con.execute("""
        CREATE TABLE IF NOT EXISTS topics (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            feel TEXT NOT NULL CHECK (feel IN ('horrified', 'negative', 'neutral', 'positive'))
        )
        """)

        con.execute("""
        CREATE TABLE IF NOT EXISTS subject (
            id TEXT PRIMARY KEY,
            topic_id TEXT,
            name TEXT NOT NULL,
            feel TEXT NOT NULL CHECK (feel IN ('horrified', 'negative', 'neutral', 'positive')),
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        )
        """)
        con.commit()
    except:
        raise

def insert_mock_data(con):
    try:
        con.execute("""
        INSERT INTO users (id, username, password, jwt_token) VALUES
        ('6f8c1a59-6f80-4bfe-a197-d65fc44c78b4', 'alice', 'hashed_pw_1', NULL),
        ('e9476f91-6f1d-4300-9c4a-b2d6d41cf87b', 'bob', 'hashed_pw_2', 'token_abc123'),
        ('af9e4181-e3ae-4574-bdc3-d80f66f06163', 'carol', 'hashed_pw_3', 'token_xyz789')
        """)

        con.execute("""
        INSERT INTO conversations (id, user_id) VALUES
        ('56a4c7e5-28aa-4ad3-9819-6a01de45c3e1', '6f8c1a59-6f80-4bfe-a197-d65fc44c78b4'),
        ('7eacdb1a-9816-43a0-939f-56782d3b8b02', 'e9476f91-6f1d-4300-9c4a-b2d6d41cf87b')
        """)

        con.execute("""
        INSERT INTO interactions (id, conversation_id, interaction_type, topic, subject) VALUES
        ('fe4d4197-5aa1-4268-b0a3-683b2912ad2a', '56a4c7e5-28aa-4ad3-9819-6a01de45c3e1', 'request', 'technology', 'ai'),
        ('9bc4e2a5-14de-4f0d-b8c2-6a8d8d3d02f6', '56a4c7e5-28aa-4ad3-9819-6a01de45c3e1', 'response', 'technology', 'ai'),
        ('139a1176-03e4-41b8-93be-58b7c4524c57', '7eacdb1a-9816-43a0-939f-56782d3b8b02', 'request', 'philosophy', 'ethics')
        """)

        con.execute("""
        INSERT INTO topics (id, name, feel) VALUES
        ('df914f84-61c2-4715-bcd7-969bd54706f1', 'technology', 'positive'),
        ('8c04868d-bb08-4c3e-b2a9-d7e77f193d5f', 'philosophy', 'neutral'),
        ('9f881c6d-c42e-47b7-a938-75899384ff1e', 'climate change', 'negative')
        """)

        con.execute("""
        INSERT INTO subject (id, topic_id, name, feel) VALUES
        ('0875417a-caa1-4b8d-bc18-b9638b40962a', 'df914f84-61c2-4715-bcd7-969bd54706f1', 'ai', 'positive'),
        ('1239e3ae-f9a9-4a33-bf3d-bf586cf8e1c2', '8c04868d-bb08-4c3e-b2a9-d7e77f193d5f', 'ethics', 'neutral'),
        ('2e221afe-2626-4096-94eb-6c7b679b1db4', '9f881c6d-c42e-47b7-a938-75899384ff1e', 'global warming', 'negative')
        """)
        con.commit()
    except:
        raise

def test_reset_database(con, cur):
    try:
        cur.execute("""
            DELETE FROM interactions;
            DELETE FROM conversations;
            DELETE FROM subject;
            DELETE FROM topics;
            DELETE FROM users;
        """)
        con.commit()
        
        insert_mock_data(con)
    except:
        raise

def main():
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    create_tables(con)
    insert_mock_data(con)

    res = cur.execute("SELECT * FROM conversations")
    print(res.fetchall())
    res = cur.execute("SELECT * FROM subject")
    print(res.fetchall())

if __name__ == "__main__":
    main()
