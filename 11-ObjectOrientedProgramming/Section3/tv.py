class tv:
    def __init__(self, set = []):
        self.is_on = False
        self.channel = 0
        self.set = set

    def toggle_on(self):
        self.is_on = not self.is_on
        
    def switch(self, channel):
        if set.find(channel != -1):
            self.channel = channel
        else:
            print("channel not available")
        
    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel}")
        else:
            print("TV is off")
    
