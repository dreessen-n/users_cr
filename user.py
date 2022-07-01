# Import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        """Model the class after user tbl in users db"""
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        """Class method to get all the users"""
        query = "SELECT * FROM users;"
        # Call connectToMySQL func with db schema
        results = connectToMySQL('users_schema').query_db(query)
        # Create empty list to append our instancse of users
        users = []
        # Iterate over db results and create instances of users with cls
        for user in results:
            users.append( cls(user) )
        return users 

    @classmethod
    def save_user(cls, data):
        """Create a classmethod to save a new user"""
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        # The data is a dict that will pass to the method from server.py
        return connectToMySQL('users_schema').query_db(query, data)