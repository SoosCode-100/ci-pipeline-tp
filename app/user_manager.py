class UserManager:
    def __init__(self):
        self.users = []
    def add_user(self, username):
        if not username:
            raise ValueError("Le nom d'utilisateur est obligatoire")
        if username in self.users:
            raise ValueError("Utilisateur déjà existant")
        self.users.append(username)
    def remove_user(self, username):
        if username not in self.users:
            raise ValueError("Utiilisateur untrouvable")
        self.users.remove(username)
    def count_users(self):
        return len(self.users)
    def count_total_users(users):
        temp= 0
        return len(users)
# This is a rudimentary test to see if my yml file has worked 
