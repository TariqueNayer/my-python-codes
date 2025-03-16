class Category:
    def __init__(self, cat):
        self.cat = cat
        self.ledger = []
        self.bal = 0.0
    def __str__(self):
        # Creating Title
        tcount = int(round((30 - len(self.cat)) / 2))
        title = self.cat
        while len(title) < 30:
            for _ in range(tcount):
                if len(title) == 30:
                    break
                title = '*' + title
            for _ in range(tcount):
                if len(title) == 30:
                    break
                title = title + '*'
        # creating items list
        ledg = self.ledger
        lst = ''
        for item in ledg:
            am = f"{item['amount']:.2f}"
            if len(item['description']) > 23:
                lcount = int(30 - len(am) - len(item['description'][:23]))
            else: lcount = int(30 - len(am) - len(item['description']))
            if len(item['description']) > 23:
                lst += item['description'][:23]
            else: lst += item['description']
            for _ in range(lcount):
                lst += ' '
            lst += am + '\n'
            total = str(self.get_balance())
        return title +'\n'+ lst + 'Total: '+ total

    def deposit(self, amount: float, descryption = ''):
        float(amount)
        self.ledger.append({'amount': amount, 'description': descryption})
        self.bal += amount

    def check_funds(self, amount: float):
        #Calculate funds
        total = float(0)
        if self.ledger:
            for i in self.ledger:
                total += i['amount']
        #Return the answer
            if total < amount:
                return False
            return True
        return False
    
    def withdraw(self, amount: float, description = ''):
        ans = self.check_funds(amount)
        if ans == True:
            
            self.ledger.append({'amount':amount*-1, 'description': description})
            self.bal -= amount
            return True
        return False
        
    
    def get_balance(self):
        return self.bal

    def transfer(self, amount: float, category):
        if self.ledger:
            bal = self.get_balance()
            if bal >= amount:
                self.withdraw(amount, f'Transfer to {category.cat}')
                category.deposit(amount,f'Transfer from {self.cat}')
                return True
            return False
        return False

def create_spend_chart(categories: list):
    spent_amounts = []
    # Get total spent in each category
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    # Calculate percentage rounded down to near 10
    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

    # Create the bar chart substrings
    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.cat, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")



if __name__ == '__main__':
    
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    print(food.get_balance())
    food.transfer(50, clothing)
    print(clothing.get_balance())
    #print(food,'\n')
    #print(clothing)
    #print(create_spend_chart([food,clothing]))