class Animal:
    """This class contains infoemation about some animals"""
    
    def __init__(self, genus, name, y_o_b, latin_name, extincted):
        self.genus = genus
        self.name = name
        self.year_of_birth = y_o_b
        self.latin_name = latin_name
        self.extinced = extincted
        
    def get_age(self, year):
        if year >= self.year_of_birth:
            age = (year - self.year_of_birth)
            return ("In this year the age of the animal would be "+str(age))
        else:
            return ("Provide the correct year")
        
    def get_info(self):
        vowels = ('a', 'e', 'i', 'u', 'y', 'o')
        word = list(self.genus)
        if word[0].lower() in vowels:
            return (self.name+" is an "+self.genus)
        else:
            return (self.name+" is a "+self.genus)
        
    def jux_age(self, year):
        if  year >= self.year_of_birth:
            jux = year - self.year_of_birth
            return("The difference detween the ages of these animals is "+str(jux)+" years")
        else:
            jux = self.year_of_birth - year
            return("The difference detween the ages of these animals is "+str(jux)+" years")
        
    def oldest(self, animals):
        o_animal = None
        o_age = 0
        for i in animals:
            this_age = 2024 - i.year_of_birth
            if this_age > o_age:
                o_age = this_age
                o_animal = i
        if o_animal is not None:
            return f"The oldest animal in the list is a {o_animal.genus}, {o_animal.name}, and it is {o_age} years old."
        else:
            return "You provided an empty list in your input. Please, denote the animals"