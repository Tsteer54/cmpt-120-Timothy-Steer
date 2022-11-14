from ast import Continue
from genericpath import exists
from re import X


class EmailStore:

    def __init__(self):
        '''
        Constructor method.
        '''
        self.emails = []

    def exists(self, email):
        '''
        Method that checks if an email exists in store.
        '''
        return email in self.emails

    def add(self, first_name, last_name):
        '''
        Method that adds a new email to the store.
        The email address is of the format {first_name}.{last_name}{count}@marist.edu

        @return the email that was added.
        '''
    
        
        # TODO if either first_name or last_name is None raise an exception
        if first_name == None or last_name == None:
            raise Exception("'first_name' and/or")
        email = None
        count = 1
        
        
        # TODO use a while loop to construct email from first_name and last_name and check if it exists.
        
        while True:
            email = f"{first_name.lower()}.{last_name.lower()}{count}@marist.edu"
        
        # TODO if generated email exists, increment count.
        
            if self.exists(email):
                count += 1
                continue
         
        
        # TODO if generated email doesn't exist, add it to the collection of emails (self.emails).
        
            else:
                self.emails.append(email)
                break
        return email
        

    def remove(self, email):
        '''
        Method that removes an email from the store.
        '''
        # TODO if email doesn't exist, raise an exception.
        
        if not self.exists(email):
            raise Exception(f"The email '{email}' does not exist.")
        else: 
            self.emails.remove(email)
        