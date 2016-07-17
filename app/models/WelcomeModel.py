""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.c(query, data)

    """
    def get_friend(self, id):
        query = "SELECT * from friends where id = :id"
        data = {'id': id}
        return self.db.query_db(query, data)

    def get_friends(self):
        query = "SELECT * FROM friends ORDER BY id DESC"
        return self.db.query_db(query)

    def del_friend(self,id):
        print id
        query = "DELETE FROM friends WHERE id = :id"
        data = {'id': id}
        self.db.query_db(query,data)
        return True

    def update_friend(self,data):
        query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
        # data = {
        #     'first_name': request.args.get('first_name'),
        #     'last_name': request.args.get('last_name'),
        #     'occupation': request.args.get('occupation'),
        #     'id': id
        # }
        self.db.query_db(query,data)
        return True

    def add_new_friend(self, data):
        query = "INSERT INTO friends(first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
        
        self.db.query_db(query,data)
        return True





