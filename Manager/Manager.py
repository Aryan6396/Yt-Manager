import json


def load_data():
    try:
        with open("vedios.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
            
def save_data(vedios):
    with open("vedios.txt",'w') as file:
        json.dump(vedios,file)

def list_vedios(vedios):
    for index,vedio in enumerate(vedios, start=1):
        print(f"{index}. {vedio['name']} - {vedio['time']}")

def add_vedio(vedios):
    name = input("Enter the name of the vedio: ")
    time = input("Enter the time of the vedio: ")
    vedios.append({"name":name,"time":time})
    save_data(vedios)
    print("Vedio added successfully")

def main():
    vedios = load_data()
    while True:
        print("\nWelcome to the vedio manager")
        print("1. List all the vedios")
        print("2. Add a new vedio")
        print("3. Update for a vedio")
        print("4. Delete a vedio")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_vedios(vedios)
                break
            case "2":
                add_vedio(vedios)
            case "3":
                update_vedio(vedios)
            case "4":
                delete_vedio(vedios)
            case "5":
                break
            case _:
                print("Invalid choice") 
        
if __name__ == "__main__":
    main()