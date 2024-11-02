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
                INSERT INTO public.user (Name, Email, Phone, Password, Major,
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

        if uid is None:
            return (False, "uid cant be none")

        sql = """
            DELETE FROM public.user_account WHERE user_id='%s'
            DELETE FROM student_course_selection WHERE user_id='%s'
            """
        error = self.db_conn.execute(sql, (uid,), False)

        return (True, None)
    

    def get_user(self, uid='%', name='%', email='%', phone='%', password='%', major='%', degree='%', enable=True):
        sql = """
            SELECT user_id, name, email, phone, password, major, degree, enable, admin, super_admin
            FROM public.user_account
            WHERE user_id::text LIKE %s
            AND name LIKE %s
            AND email LIKE %s
            AND phone LIKE %s
            AND password LIKE %s
            AND major LIKE %s
            AND degree LIKE %s
            AND enable = %s
        """
        args = (str(uid), name, email, phone, password, major, degree, enable)
        result = self.db_conn.execute(sql, args, fetch=True)

        if not result:
            return False, "No users found matching the criteria."

        return True, result[0]
    
    def update_user(self, args):
        sql = """   UPDATE
                        public.user_account
                    SET
                        name        = %(Name)s,
                        email       = %(Email)s,
                        phone       = %(Phone)s,
                        password    = %(Password)s,
                        major       = %(Major)s,
                        degree      = %(Degree)s
                    WHERE
                        user_id = %(UID)s;
                    """
        return self.db.execute(sql, args, False)[0]




