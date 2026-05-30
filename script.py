import requests

def fetch_and_search_users():
    # 1. Define the API URL
    url = "https://jsonplaceholder.typicode.com/users"
    
    print("Fetching data from API...")
    
    try:
        # 2. Fetch the data using the requests module
        response = requests.get(url)
        
        # Check if the request was successful (Status Code 200 means OK)
        response.raise_for_status() 
        
        # 3. Parse the JSON response into a Python list
        users = response.json()
        
        # 4. Add a search filter
        # We ask the user what name they want to look for
        search_query = input("\nEnter a name or keyword to search for: ").strip().lower()
        
        print(f"\n--- Search Results for '{search_query}' ---")
        
        found_any = False
        
        # 5. Loop through the data and display results properly
        for user in users:
            name = user.get("name", "")
            username = user.get("username", "")
            email = user.get("email", "")
            company = user.get("company", {}).get("name", "")
            
            # Check if the search query is inside the name or email
            if search_query in name.lower() or search_query in email.lower():
                found_any = True
                # Displaying the results in a clean format
                print(f"Name:     {name}")
                print(f"Username: {username}")
                print(f"Email:    {email}")
                print(f"Company:  {company}")
                print("-" * 30) # Visual separator
                
        if not found_any:
            print("No users found matching that search term.")
            
    except requests.exceptions.RequestException as e:
        # If the internet is down or the URL is wrong, this handles the error safely
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    fetch_and_search_users()