# Importing necessary in built function
import datetime

# function to get current hours
def get_current_hour():
    now=datetime.datetime.now()
    return now.hour


# Function to determine part of the day.
def get_part_of_day():
    hour=get_current_hour()
    if hour <12:
        return 'morning'
    elif hour <18:
        return 'afternoon'
    else:
        return 'evening'

# Function to suggest outfit based on weather and occasion
def suggest_outfit(weather,occasion):
    #Nested if-else statements for detailed outfit suggestion.
    if weather=='sunny':
        if occasion=='casual':

            outfit='t-shirt and shorts'
            return outfit
        elif occasion=='formal':
            outfit='light suit'
            return outfit
        else:
            outfit='comfortable casual wear'
            return outfit
    elif weather =='rainy':
        if occasion=='casual':
            outfit='raincout and waterproof shoes'
            return outfit
        elif occasion=='formal':
            outfit='formal wear with an umbrella'
            return outfit
        else:
            outfit='rain-resistant casual wear'
            return outfit

    elif weather=='cold':
        if occasion=='casual':
            outfit='sweater and jeans'
            return outfit
        elif occasion==" formal":
            outfit='warm suit with an overcoat'
            return outfit
        else:
            outfit='warm casual wear'
            return outfit
    
    else:
        outfit='appropriate clothing based on personal choice'
        return outfit
    

# Main function to run the programe
def main():
    print("Welcome to the Outfit Suggester! ")
    
    # Get the part of  the day.
    part_of_day=get_part_of_day()
    print(f"Good {part_of_day} !")
    

    #Get user input for weather and occasion
    weather=input("Please enter the weather (sunny,rainy,cold) : ").strip().lower()
    occasion=input("Please enter the occasion (casual, formal,other) : ").strip().lower()

    # Check for valid input
    valid_weather=['sunny','formal','cold']
    valid_occasion=['casual','formal','other']
    
    if weather not in valid_weather or occasion not in valid_occasion :
        print("Invalid input. Please try again")
        return
    
    #Suggested outfit based on weather and occasion
    outfit=suggest_outfit(weather,occasion)
    print(f'Suggested outfit for a {occasion} occasion on a {weather} day : {outfit}')


# Run the main function
if __name__=='__main__':
    main()