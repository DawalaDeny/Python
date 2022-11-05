class Piraat:
    def __init__(self, naam: str, quote: str = "Ahoy!"):
        self.naam = naam
        self.quote = quote
    def get_naam(self):
        return self.naam
    def get_quote(self):
        return self.quote
    def __str__(self):
        return f"Pirate {self.naam} says {self.quote}"
