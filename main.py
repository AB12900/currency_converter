import requests # Imports requests library to make HTTP request

def get_exchange_rate(base_currency, target_currency):
    try:
        #construct an API url and make a GET request
        api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an HTTPError for any bad responses
        data = response.json() # parse the response as JASON
        exchange_rate = data["rates"].get(target_currency) #extract exchange rate
        #check if exchange rate is available
        if exchange_rate:
            return exchange_rate
        else:
            # this tells the user that the exchange is not available
            print(f"Rate not found for {target_currency}. Please check the currency code.")
            return None
        #this prints error message if there is a problem with request
    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None

def convert_currency(amount, exchange_rate):
    return round(amount * exchange_rate, 2)  # Round to two decimal places for better readability

def main():
    # Ask user for base currency, target currency and the amount needed to convert.
    base_currency = input("Enter the base currency: ").upper()
    target_currency = input("Enter the target currency: ").upper()
    try:
        #convert amount from string to float
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate:
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}")
# check if script isbeing run directly
if __name__ == "__main__":
    main() # execute the main function
