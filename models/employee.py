class Employee():
    """employee class"""

    def __init__(self, id, full_name, address, location_id):
        self.id = id
        self.name = full_name
        self.address = address
        self.location_id = location_id

        #extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
