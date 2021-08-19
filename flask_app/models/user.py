from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_email( cls, data ):
        query = "INSERT INTO users (email) VALUES (%(email)s);"
        results = connectToMySQL('email_validation').query_db(query, data)
        return results

    @classmethod
    def get_emails( cls ):
        query = "SELECT * FROM users;"
        results = connectToMySQL('email_validation').query_db(query)

        emails = []
        for item in results:
            new_email = User(item)
            emails.append(new_email)
        return emails

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid