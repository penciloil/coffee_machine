# 菜單，每種飲料包含所需原料與價格
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# 咖啡機目前擁有的資源：水、牛奶、咖啡、金錢
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# 檢查資源是否足夠製作該飲料，若不足則回傳 False 並顯示缺少的項目
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# 印出咖啡機目前的資源報告
def print_report():
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}"

# 請使用者投入硬幣，並計算投入的總金額
def process_coins():
    print("Please insert coins.")
    try:
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickles?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
    except ValueError:
        print("Sorry that's not a valid number. Please try again.")
        return process_coins()
    return total

# 咖啡機主流程：接收指令、處理訂單、檢查資源與金額、製作飲料
def coffee_maker():
    while True:
        what_they_want = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # 關機指令，結束程式
        if what_they_want == "off":
            break
        # 印出咖啡機目前的資源狀態
        elif what_they_want == "report":
            print(print_report())
        # 檢查用戶選擇的飲料是否在菜單中
        elif what_they_want in MENU:
            drink = MENU[what_they_want]
            # 若資源足夠，則進行付款流程
            if is_resource_sufficient(drink["ingredients"]):
                pay = process_coins()
                # 若付款金額足夠，則扣除資源、找零並製作飲料
                if pay >= drink["cost"]:
                    change = round(pay - drink["cost"], 2)
                    resources["money"] += drink["cost"]
                    for item, quantity in drink["ingredients"].items():
                        resources[item] -= quantity
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {what_they_want} ☕️. Enjoy!")
                # 若付款金額不足，退款並結束本次交易
                else:
                    print("Sorry that's not enough money. Money refunded.")
        # 用戶輸入的飲料不存在於菜單中
        else:
            print("We don't have that item.")

coffee_maker()
