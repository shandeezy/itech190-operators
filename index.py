def main():
    balance = 800
    paycheck = 2000

    print(f"balance plus paycheck equals:{balance + paycheck}") #2800
    print(f"balance minus paycheck equals:{balance - paycheck}") #1200
    print(f"balance multipy paycheck equals:{balance * paycheck}") #1600000
    print(f"balance integer divison paycheck equals:{balance // paycheck}") #0
    print(f"balance modulo divison paycheck equals:{balance % paycheck}") #800
    print(f"balance divison paycheck equals:{balance / paycheck}") #0.4
    print()
    print(f"balance greater than paycheck equals:{balance > paycheck}") #false
    print(f"balance less than paycheck equals:{balance < paycheck}") #true
    print(f"balance is equal to paycheck:{balance < paycheck}") #true
    print(f"balance greater than or equal to paycheck:{balance <= paycheck}") #false
    print(f"balance less than or equal to paycheck:{balance <= paycheck}") #true
    print(f"balance is not equal to paycheck:{balance != paycheck}") #true
    print()
    balance += paycheck
    print(f"balance plus paycheck equals:{balance}") #2800
    balance -= paycheck
    print(f"balance minus paycheck equals:{balance}") #800
    balance *= paycheck
    print(f"balance multipy paycheck equals:{balance}") #1600000
    balance /= paycheck
    print(f"balance divide paycheck equals:{balance}") #0.4
    balance //= paycheck
    print(f"balance integer paycheck equals:{balance}") #0
    balance %= paycheck
    print(f"balance modulo divide paycheck equals:{balance}") #800
    


if __name__ == "__main__":
    main()



















