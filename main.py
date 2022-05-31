import csv
class Pet:
    def __init__(self):
        self.is_valid = False

    def valid_entry(self):
        while self.is_valid == False:
            fileInput = str(input("which file do you want? Please enter cats or dogs: "))
            if fileInput == "cats" or fileInput == "dogs":
                if not ".csv" in fileInput:
                    fileInput += ".csv"
                    self.is_valid = True
                    self.input_species(fileInput)
            else:
                print("Sorry, not a valid pet entry. Please enter either cats or dogs.")
        
        
    def input_species(self, fileInput):
        with open(f"data/{fileInput}") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                print(f'\t{row[0]} is a{row[1]} year old{row[2]}.')
        csv_file.close()
    


def main():
    myObj = Pet()
    print(myObj.valid_entry())

if __name__ == '__main__':
    main()