Transportation_expense = int(input("enter your transportation expense:"))
Accomodation_expense = int(input("enter your accomodation expense:"))
Food_expense = int(input("enter your food expense:"))

total_expense = Transportation_expense + Accomodation_expense + Food_expense

travel_expenses = {
    "Transportation Expense":Transportation_expense,
    "Accomodation Expense" : Accomodation_expense,
    "Food Expense" : Food_expense,
    "Total Expense" : total_expense
}

print(travel_expenses)