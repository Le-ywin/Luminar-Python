# class library

# pbj1 >>> []

# method 1, add book (b_name,b_author) obj1.addbook(b_name,b_author) >>> [{"name":b_name,"author":b_author}]

# method 2, remove_book, b_name

# method 3, display books


class Library:

    def __init__(self):
        
        self.books = []

    def add(self,b_name,b_author):

        self.b_name = b_name

        self.b_author = b_author

        new = {"Name":b_name,"Author":b_author}

        self.books.append(new)

    def delete(self,b_name):

        for i in self.books:

            if i["Name"] == b_name:

                self.books.remove(i)

    def display(self,b_author):

        result = [i for i in self.books if i["Author"] == b_author]

        if result:

            for i in result:

                print(i)

        else:

            print("Not found!")

light_novels = Library()

light_novels.add(b_name="The Beginning After The End",b_author="TurtleMe")

light_novels.add(b_name="Solo Leveling",b_author="Chugong")

light_novels.add(b_name="Omniscient Reader's Viewpoint",b_author="Sing Shong")

light_novels.display(b_author="TurtleMe")

light_novels.delete(b_name="Solo Leveling")

light_novels.display(b_author="Sing Shong")
