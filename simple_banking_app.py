balance = 0.0
kyc_documents = {}


def check_balance():
    print(f"Your Current Balance is \n{balance}")
    

def deposit(amount):
    
    global balance
    if amount > 0:
        balance += amount
    else:
        print("Cann't deposit negative amount.")
      

def withdrawl(amount):
    global balance
    if amount < 0:
        print("Cann't withdrawl negative or zero amount. ")
      
    elif amount > balance:
        print("Invalid !!. Insufficient Balance ")
        
    else:
       balance -= amount

def update_kyc(**docs):
    global kyc_documents
    kyc_documents.update(docs)
    
    

def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC not done yet !!!")
    else:
        print("Your KYC Documents:")
        for doc in kyc_documents:
            print(f"{doc} : {kyc_documents[doc]}")



if __name__ == "__main__": 
    
   
    print("Welcome to Tanay's Bank Application. ")
    
    while True:
        
        print("1. Check your bank balance")
        print("2. Deposit an amount")
        print("3. Withdraw an amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Quit")
       
        print("===============================") 
        choice = input("Enter your preference (1-6) : ")
        
        if choice == "1":
            check_balance()
        
        elif choice == "2":
            amt =  float(input("\nEnter amount to be deposite:"))
            deposit(amt)
            
        elif choice == "3":
            amt =  float(input("\nEnter amount to be withdrawn :"))
            withdrawl(amt)
        
        elif choice == "4":
            check_kyc()
        
        elif choice == "5":
            kyc_docs = {}   
            n_kycdoucuments = int(input("Enter number of documents you want to add : "))
            for i in range (n_kycdoucuments):
                key = input("Enter the document type : ")
                value = input("Enter the document number : ")
                kyc_docs[key] = value
                update_kyc(**kyc_docs)  
            print("Kyc successfully updated !")
                      
            
            
        elif choice == "6":
            break
        else:
            print("Invalid Choice . ")
    
    print("Thank u for choosing us .")
    print("***************************")