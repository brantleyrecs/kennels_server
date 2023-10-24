class Customer():
    """customer class"""

    def __init__(self, id, full_name, address, email = "", password = ""):
        self.id = id
        self.name = full_name
        self.adress = address
        self.email = email
        self.password = password

        # extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
