class ebook:
    def __init__(self, title = 'title', author = 'author', page_count = 1):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.current_page = 0
        self.is_open = False

    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False

    def next_page(self):
        if self.is_open:
            if self.current_page < self.page_count - 1:
                self.current_page += 1
            else:
                return
        else:
            print('Action cannot be performed, the book is closed, please open the book to read it.')
            return
        
    
    def previous_page(self):
        if self.current_page < self.page_count - 1:
            if self.current_page > 0:
                self.current_page -= 1
            else:
                return
        else:
            print('Action cannot be performed, the book is closed, please open the book to read it.')
            return
        
        
    def read(self):
        if self.is_open:
            return self.current_page + 1
        else:
            print('Action cannot be performed, the book is closed, please open the book to read it.')
            return 'none'
    
    def __str__(self):
        return f'Author: {self.author}, title: {self.title}, number of pages: {self.page_count}, open: {self.is_open}, current page: {self.read()}'
    
    def status(self):
        print(str(self))
    
def main():
    book1 = ebook('Annihilation', 'Jeff Vandermeer', 208)
    book1.open()
    book1.status()
    for i in range(144):
        book1.next_page()
    book1.status()
    book1.close()
    book1.next_page()
    book1.status()

if __name__ == "__main__":
    main()