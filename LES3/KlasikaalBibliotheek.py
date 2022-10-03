class Bibliotheek:
    def __init__(self, max: int) -> None:
        self.max = max

    def __iter__(self):
        self.n =0
        return self
    def __next__(self):
        if self.n < self.max:
            self.n +=1
            return f"Book{self.n}"
        else:
            self.n = 0 #iterator reset'n
            raise StopIteration

if __name__ == '__main__':
    bib = Bibliotheek(max=10)
    books = iter(bib)

    for book in books:
        print(book)