#!/usr/bin/env python

"""M03_ListFuncAndClass.py a small python app that accepts user input and demonstrates classes and inheritance"""

__author__ = "Sammy Rigdon IV"
__version__ = "1.0.0"
__email__ = "srigdon5@ivytech.edu"


# Vehicle class
class Vehicle():
    def __init__(self) -> None:
        self.vehicle_type = ""


# Automobile class <- Vehicle
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof) -> None:
        super().__init__()
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        
        
    # Class function to display info
    def display_car(self):
        print(f"Vehicle Type: {self.vehicle_type}\n"
              f"Year: {self.year}\n"
              f"Make: {self.make}\n"
              f"Model: {self.model}\n"
              f"Number of doors: {self.doors}\n"
              f"Type of roof: {self.roof}\n")
        

# Accept user input
def main():
    while True:
        # Welcome user
        input('\nHello and Welcome to the car registry! You can exit at any time by typing "exit." Please press enter to continue!\n')
        
        # dict to store car info
        car_dict = {'Year': "",
                    'Make': "",
                    'Model': "",
                    'Doors': "",
                    'Roof': ""}
        
        # inform user of of requirements
        print('You will now be asked to input data for your car. Please enter info correctly, year must be a valid year as a 4 digit number, doors must be either 2 or 4'
              ', and roof must be either "solid" or "sun roof"')
        
        # iterate over dict checking for exit
        for key in car_dict.keys():
            user_input = input(f'{key}? ')
            
            # check exit code
            if user_input.lower() == 'exit':
                print('Now Exiting')
                exit()
            
            # value specific checks
            # Year
            if key == 'Year':
                if len(user_input) > 4 or len(user_input) < 4:
                    print('Year must be entered as a 4 digit number')
                    break
                
                try:
                    user_input = int(user_input)
                except ValueError:
                    print('Year must be entered as a 4 digit number')
                    break
            # Doors
            elif key == 'Doors':
                if len(user_input) > 1:
                    print("Doors must be either 2 or 4(too long)")
                    break

                try:
                    if int(user_input) != 2 and int(user_input) != 4:
                        print("Doors must be either 2 or 4(not a number)")
                        break
                    else:
                        user_input = int(user_input)
                except ValueError:
                    print("Doors must be either 2 or 4(value error)")
                    break
            # Roof
            elif key == 'Roof':
                if user_input.lower() != 'solid' and user_input.lower() != 'sun roof':
                    print('Roof must be either "solid" or "sun roof"')
                    break
            
            # Update dict
            car_dict[key] = user_input
            
        # Create car after exiting loop    
        new_car =Automobile(car_dict['Year'], car_dict['Make'], car_dict['Model'], car_dict['Doors'], car_dict['Roof'])
        new_car.vehicle_type = 'car'
        
        # display car info
        print('\nYou have successfully registered the following car:')
        new_car.display_car()
            
    

# main loop
if __name__ == "__main__":
    main()
