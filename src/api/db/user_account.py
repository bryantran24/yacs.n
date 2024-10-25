import json
from psycopg2.extras import RealDictCursor
import asyncio

if __name__ == "__main__":
    import connection
else:
    from . import connection

class User:
    def __init__(self, db_conn, cache):
        self.db_conn = db_conn
        self.cache = cache

    def add_user(self, name, email, phone, password, major, degree, enable):
        if email is not None:
            self.db_conn.execute("""
                INSERT INTO professor (Name, Email, Phone, Password, Major,
                                    Degree, Enable)
                VALUES (%(name)s, %(email)s, %(phone)s, %(password)s,
                        %(major)s, %(degree)s, %(enable)s)
                ON CONFLICT DO NOTHING;
            """, {
                "Name": name,
                "Email": email,
                "Phone": phone,
                "Password": password,
                "Major": major,
                "Degree": degree,
                "Enable": enable,
            })
        else:
            return False, "Email cannot be None."
        
    def delete_user(self, uid):
        if email is not None:
            sql = """
                DELETE FROM 
                    professor
                WHERE
                    email = '%s'
                """
            error = self.db_conn.execute(sql, (email,), False)
