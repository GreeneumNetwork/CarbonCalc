import requests
print("Please answer the following questions to help us learn more about your company")
company_name = input("Enter the company name: ")
country = input("Enter the two-letter country code: ")
currency = input("Enter the three-letter currency code: ")
date = input("Enter the date of estimation: ")
category = input("Enter the name of the supplier's industry: ")

url_overall = "https://api.ditchcarbon.com/v1.0/supplier?name=" + company_name + "&currency=" + currency + "&country=" + \
    country + "&date="+date + "&category=" + category

headers = {
    "accept": "application/json",
    "authorization": "Bearer 06ac9efc749cb32c48b636e5f33ac42f"
}

response = requests.get(url_overall, headers=headers)

print(response.text)

num_expenses = int(input("We can also calculate the carbon emmissions of expenses. How many expenses would you like to list? "))
count = 1
for e in range(num_expenses):
    print("EXPENSE #", count)
    supplier = input("Enter the name of the supplier: ")
    description = input("Give a description of the expense: ")
    amount = input("Enter the value of the expense: ")
    date2 = input("Enter the date of the expense: ")
    currency2 = input("Enter the three-letter currency code: ")
    region = input("Enter the two-digit code of the country where the expense occurred: ")

    url_expenses = "https://api.ditchcarbon.com/v1.0/calculate?supplier=" + supplier + "&description=" + description + "&amount=" \
    + amount + "&amount_currency=" + currency2 + "&date=" + date2 + "&region=US"

    headers = {
    "accept": "application/json",
    "authorization": "Bearer 06ac9efc749cb32c48b636e5f33ac42f"
    }

    response_expenses = requests.get(url_expenses, headers=headers)

    print(response_expenses.text)
    count+=1


