import os
from shutil import copyfile
from PyPDF2 import PdfWriter, PdfReader
from PyPDF2.generic import AnnotationBuilder
from fpdf import FPDF
import re
import time
import random
random.seed(time.time)


givers = []
receivers = []


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


def get_info():

    while True:
        while True:
            fname = input("Enter your first name: ")
            if not re.match("^[A-Za-zŽžÀ-Ÿà-ÿ0-9Œœ: '-]*$", fname):
                print("Please make sure your entry is valid.")
            else:
                break
        while True:
            lname = input("Enter your last name: ")
            if not re.match("^[A-Za-zŽžÀ-Ÿà-ÿ0-9Œœ: '-]*$", lname):
                print("Please make sure your entry is valid.")
            else:
                break
        while True:
            color = input("What is your favorite color? ")
            if not re.match("^[A-Za-zŽžÀ-Ÿà-ÿ0-9Œœ: '-]*$", color):
                print("Please make sure your entry is valid.")
            else:
                break
        while True:
            size = input("What size are you? S, M, L, XL, etc... ")
            if not re.match("^[A-Za-zŽžÀ-Ÿà-ÿ0-9Œœ: '-]*$", size):
                print("Please make sure your entry is valid.")
            else:
                break
        while True:
            snack = input("What is your favorite snack? ")
            if not re.match("^[A-Za-zŽžÀ-Ÿà-ÿ0-9Œœ: '-]*$", snack):
                print("Please make sure your entry is valid.")
            else:
                break
        while True:
            chocolate = input("Do you like chocolate? ")
            if not re.match("^[A-Za-zŽžÀ-Ÿà-ÿ0-9Œœ: '-]*$", chocolate):
                print("Please make sure your entry is valid.")
            else:
                break
        while True:
            drink = input("What is your favorite drink? ")
            if not re.match("^[A-Za-zŽžÀ-Ÿà-ÿ0-9Œœ: '-]*$", drink):
                print("Please make sure your entry is valid.")
            else:
                break
        while True:
            allergies = input("Any allergies? ")
            if not re.match("^[A-Za-zŽžÀ-Ÿà-ÿ0-9Œœ: '-]*$", allergies):
                print("Please make sure your entry is valid.")
            else:
                break
        while True:
            hobby = input("What is your favorite hobby? ")
            if not re.match("^[A-Za-zŽžÀ-Ÿà-ÿ0-9Œœ: '-]*$", hobby):
                print("Please make sure your entry is valid.")
            else:
                break
        while True:
            show = input("What is your favorite show? ")
            if not re.match("^[A-Za-zŽžÀ-Ÿà-ÿ0-9Œœ: '-]*$", show):
                print("Please make sure your entry is valid.")
            else:
                break
        while True:
            movie = input("What is your favorite movie? ")
            if not re.match("^[A-Za-zŽžÀ-Ÿà-ÿ0-9Œœ: '-]*$", movie):
                print("Please make sure your entry is valid.")
            else:
                break
        while True:
            game = input("What is your favorite game? ")
            if not re.match("^[A-Za-zŽžÀ-Ÿà-ÿ0-9Œœ: '-]*$", game):
                print("Please make sure your entry is valid.")
            else:
                break
        while True:
            store = input("What is your favorite store? ")
            if not re.match("^[A-Za-zŽžÀ-Ÿà-ÿ0-9Œœ: '-]*$", store):
                print("Please make sure your entry is valid.")
            else:
                break
        while True:
            animal = input("What is your favorite animal? ")
            if not re.match("^[A-Za-zŽžÀ-Ÿà-ÿ0-9Œœ: '-]*$", animal):
                print("Please make sure your entry is valid.")
            else:
                break
        break

    info = GiftInfo(fname, lname, color, size, snack, chocolate, drink,
                    allergies, hobby, show, movie, game, store, animal)
    return info


def populate_lists():
    with open("participants.txt", "r") as file:
        f = file.readlines()
        for item in f:
            givers.append(item)
            receivers.append(item)


def assign_gifter(gifters):
    gifter_choice = random.randint(0, len(gifters) - 1)
    gifter = gifters[gifter_choice]

    return gifter


def assign_giftee(giftees):
    receiver_choice = random.randint(0, len(giftees) - 1)
    giftee = giftees[receiver_choice]

    return giftee


def create_intro_text(gifter, giftee):
    text = f"""
    Hello {gifter}!
    
    This year, you are the secret santa to {giftee}!
    You can find their information below!
    """

    return text


def extract_text():
    reader = PdfReader("sasha_kelly.pdf")
    page = reader.pages[0]
    return page.extract_text()


def create_assignment_text(text1, text2):
    with open("assignment.txt", "w") as file:
        file.write(f"{text1} \n")
        file.write(f"{text2}")


def create_assignment_pdf(file):
    pdf = FPDF()
    # Add a page
    pdf.add_page()
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)
    f = open(f"{file}", "r")
    # insert the texts in pdf
    for x in f:
        pdf.cell(50, 5, txt=x, ln=1, align='L')
    # save the pdf with name .pdf
    pdf.output(f"test.pdf")


while True:
    choice = input("What would you like to do? ").lower()
    match choice:
        case "add":
            gt = get_info()
            gt.create_text_file(gt.create_text())
            gt.create_pdf_file()
            gt.create_name_file()

        case "match":
            populate_lists()
            print(givers, receivers)
            giver = assign_gifter(givers)
            receiver = assign_giftee(receivers)
            intro = create_intro_text(giver, receiver)
            print(intro)
            print(f"{5 * 5}!")
            information = extract_text()
            create_assignment_text(intro, information)

            create_assignment_pdf("assignment.txt")

        case "exit":
            break

        case _:
            print("Please select a valid option")

