
def dummy_churn_model(purchase_history, account_age):
    if account_age < 6 and len(purchase_history) < 3:
        return 0.8  
    elif len(purchase_history) > 5:
        return 0.1  
    else:
        return 0.4  


class Customer:
    def __init__(self, name, purchase_history, account_age):
        self.name = name
        self.purchase_history = purchase_history
        self.account_age = account_age

    def predict_churn(self):
        probability = dummy_churn_model(self.purchase_history, self.account_age)
        print(f"{self.name}'s churn probability: {probability * 100:.1f}%")
        return probability

customer1 = Customer("Alice", ["item1", "item2"], 4)
customer2 = Customer("Bob", ["item1","item2","item3","item4","item5","item6"], 12)

customer1.predict_churn()
customer2.predict_churn()
