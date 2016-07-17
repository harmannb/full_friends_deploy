"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('WelcomeModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        friends = self.models['WelcomeModel'].get_friends()
        print friends
        return self.load_view('index.html', all_friends = friends )
    def delete(self,id):
       
        return self.load_view('delete.html', friend_id=id)


    def delete_friend(self,id):
        was_deleted = self.models['WelcomeModel'].del_friend(id)
        if(was_deleted):
            return redirect('/')
        else:
            flash('Unexpected error while deleting')
            return redirect('/delete/id')
        

    def add(self):
        return self.load_view('add.html')

    def add_friend(self):
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'occupation': request.form['occupation']
        }
        friend_added = self.models['WelcomeModel'].add_new_friend(data)
        if friend_added:
            return redirect('/')
        else:
            flash('They aint yo friend')
            return redirect('/add')

    def edit(self,id):
        friends = self.models['WelcomeModel'].get_friend(id)
        return self.load_view('edit.html', friends=friends)


    def show(self, id):
        friends = self.models['WelcomeModel'].get_friend(id)
        print friends
        return self.load_view('show.html', friends = friends)

    def update(self,id):
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'occupation': request.form['occupation'],
            'id': id
        }

        updated = self.models['WelcomeModel'].update_friend(data)
        if updated:
            return redirect('/')
        else:
            flash('Unexpected error while updating')
            return redirect('/edit/id')
