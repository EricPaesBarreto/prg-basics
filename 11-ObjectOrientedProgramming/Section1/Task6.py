class phone:
    def __init__(self,name,ram,storage,processor,brand,price):
        self.name = name
        self.ram = ram
        self.storage = storage
        self.processor = processor
        self.brand = brand
        self.price = price
        self.installed_apps = []
        self.memory = []

    def install_app(self,name):
        if len(self.installed_apps) >= self.storage: 
            print('Not enough storage, uninstall an app.')
            return
        if self.app_installed(name) == -1:
            self.installed_apps.append([name, 0])
        else:
            print('App already exists on phone')

    def app_installed(self,name):
        for index in range(len(self.installed_apps)):
            if self.installed_apps[index][0] == name:
                return index
        return -1
    
    def fav_app(self):
        most_opened = 0
        for app in self.installed_apps:
            if app[1] > most_opened:
                most_opened = app[1]
        
        fav_apps = []
        for app in self.installed_apps:
            if app[1] == most_opened:
                fav_apps.append(app[0])
        
        return fav_apps

    def open_app(self,name):
        if len(self.memory) >= self.ram:
            print('Not enough memory, close an app')
            return
        
        position = self.app_installed(name)
        if position != -1:
            self.installed_apps[position][1] += 1
            self.memory.append(name)
        else:
            print('The specified app is not installed')

    def close_app(self,name):
        if self.memory.index(name) != -1:
            self.memory.remove(name)
        else:
            print('App already exists on phone')

    def print_info(self):
        print("Specifications:")
        print(f'name: {self.name}')
        print(f'memory: {self.ram}GB')
        print(f'storage: {self.storage}GB')
        print(f'processor: {self.processor}')
        print(f'brand: {self.brand}')
        print(f'price: {self.price}$')
        print("------------------------")
        print("Installed apps: ")
        for app in self.installed_apps:
            print("Name:",app[0],"Times opened:", app[1])
        print("------------------------")
        print("Currently open apps: ")
        for app in self.memory:
            print(app)
        print("------------------------")
        print("Favourite app(s): ")
        for f_app in self.fav_app():
            print(f_app)

def main():
    phone1 = phone(
        "Nokia 3310",
        4,
        3,
        "Snapdragon 5xs",
        "Nokia",
        899.99
    )

    phone1.install_app("Chrome")
    phone1.install_app("Flappy bird")
    phone1.install_app("Flappy bird") # app already exists
    phone1.install_app("Sleepy bird")
    phone1.install_app("chatGPT") # not enough storage

    phone1.open_app("Chrome")
    for i in range(5):
        phone1.open_app("Flappy bird")
        phone1.close_app("Flappy bird")
    
    phone1.open_app("Sleepy bird")

    phone1.print_info()

if __name__ == "__main__":
    main()