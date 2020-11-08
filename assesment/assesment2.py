#define the gang function
def gang():
    print("Loading gang...")
    #initialise a new list called friends and populate with values
    friends = ["Scooby Doo", "Shaggy Rogers", "Fred Jones", "Daphne Blake", "Velma Dinkley"]
    #display friends list
    print(friends)
    print("...Done!")
    #return the list
    return friends

#function call for testing purposes
#gang()

#define the phrases function
def phrases(friends):
    #initialise a new dictionary called quotes
    quotes = {}
    #loop to ask user to input a quote for each friend and update the quotes dictionary
    for friend in friends:
        print(f"What does {friend} say?")
        quote = input()
        quotes[friend] = quote
    #test run to check that the dictionary is updating as expected    
    #print(quotes)
    
    #return the quotes dictionary
    return quotes

#function call for testing purposes
friends = gang()
quotes = phrases(friends)
print(f"\nPhrases: {quotes}\n") 

#define the save function
def save(quotes):
 with open ("quotes.txt", "w") as file:
    #loop to save out dictionary items to txt file with a new line for each   
    for item in quotes:
        file.write(f"{quotes}\n")
       
#function calls for testing purposes        
save(quotes)
print("The file contains...")
file = open("Quotes.txt")
print(file.read())
file.close()
    