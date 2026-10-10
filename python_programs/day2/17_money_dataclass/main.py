from dataclasses import dataclass

# order=True makes the dataclass comparable using the comparison operators (<, <=, >, >=) based on the order of the fields defined in the class. 
# frozen=True makes the dataclass immutable, so you cannot change the attributes after creation.
@dataclass(order=True, frozen=True)
class Money:
    """Money as an integer number of cents in a currency. Fill in the fields and options."""
    currency: str
    amount_cents: int

    def __post_init__(self) -> None:
        if not isinstance(self.amount_cents, int) or isinstance(self.amount_cents, bool):
            raise TypeError("Amount_cents must be an integer")
        if not self.currency:
            raise ValueError("Currency cannot be empty")
        if self.amount_cents < 0:
            raise ValueError("Amount_cents cannot be negative")

    def __add__(self, other) -> "Money":
        if not isinstance(other, Money):
            raise TypeError("Can only add Money to Money")
        if self.currency != other.currency:
            raise ValueError("Cannot add Money with different currencies")
        return Money(self.currency, self.amount_cents + other.amount_cents)
    
    def __str__(self):
        return f"{self.amount_cents / 100:.2f} {self.currency}"


def main():
    a, b = Money("USD", 1050), Money("USD", 250)
    print(a, "+", b, "=", a + b)
    print(sorted([Money("USD", 300), Money("EUR", 900), Money("USD", 100)]))
    print({Money("USD", 1): "one cent"})


if __name__ == "__main__":
    main()