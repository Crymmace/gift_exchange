import os
from fpdf import FPDF

giver = []
receiver = []


class GiftInfo:
    def __init__(self, fname, lname, color, size, snack, chocolate, drink,
                 allergies, hobby, show, movie, game, store, animal):
        self.fname = fname
        self.lname = lname
        self.color = color
        self.size = size
        self.snack = snack
        self.chocolate = chocolate
        self.drink = drink
        self.allergies = allergies
        self.hobby = hobby
        self.show = show
        self.movie = movie
        self.game = game
        self.store = store
        self.animal = animal

    def create_text(self):
        text = f"""
        Name: {self.fname} {self.lname}
        Favorite Color: {self.color}
        Size: {self.size}
        Favorite Snack: {self.snack}
        Chocolate: {self.chocolate}
        Favorite Drink: {self.drink}
        Allergies: {self.allergies}
        Favorite Hobby: {self.hobby}
        Favorite Show: {self.show}
        Favorite Movie: {self.movie}
        Favorite Game: {self.game}
        Favorite Store: {self.store}
        Favorite Animal: {self.animal}
        """
        return text

    def create_name_file(self):
        with open(f"participants.txt", "a") as file:
            file.write(self.fname + " " + self.lname + "\n")
            file.close()

    def create_text_file(self, text):
        with open(f"{self.fname}_{self.lname}.txt", "w") as file:
            file.write(text)
            file.close()

    def create_pdf_file(self):
        pdf = FPDF()
        # Add a page
        pdf.add_page()
        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size=15)
        # open the text file in read mode
        f = open(f"{self.fname}_{self.lname}.txt", "r")
        # insert the texts in pdf
        for x in f:
            pdf.cell(50, 5, txt=x, ln=1, align='L')
            # save the pdf with name .pdf
        pdf.output(f"{self.fname}_{self.lname}.pdf")
        os.remove(f"{self.fname}_{self.lname}.txt")


def get_info():

    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    color = input("What is your favorite color? ")
    size = input("What size are you? S, M, L, XL, etc... ")
    snack = input("What is your favorite snack? ")
    chocolate = input("Do you like chocolate? ")
    drink = input("What is your favorite drink? ")
    allergies = input("Any allergies? ")
    hobby = input("What is your favorite hobby? ")
    show = input("What is your favorite show? ")
    movie = input("What is your favorite movie? ")
    game = input("What is your favorite game? ")
    store = input("What is your favorite store? ")
    animal = input("What is your favorite animal? ")

    info = GiftInfo(fname, lname, color, size, snack, chocolate, drink,
                    allergies, hobby, show, movie, game, store, animal)
    return info


gt = get_info()
print(gt.create_text())
gt.create_text_file(gt.create_text())
gt.create_pdf_file()
gt.create_name_file()

