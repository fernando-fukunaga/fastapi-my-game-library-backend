class UserEntity:
    id: str
    name: str
    email: str
    username: str
    password: str

    def __init__(self, id, name, email, username, password):
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.password = password
