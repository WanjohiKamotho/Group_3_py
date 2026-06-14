# Import the base Person class from the local person module
from .person import Person


class User(Person):
    """Represents a system user, inheriting base attributes from Person."""

    # Class variable to automatically generate unique, sequential IDs
    id_counter = 1

    def __init__(self, name, username, role):
        """Initialize a new User instance."""
        # Call the parent class (Person) constructor to initialize the name
        super().__init__(name)

        # Assign a unique ID and increment the class counter for the next user
        self.id = User.id_counter
        User.id_counter += 1

        # Set user attributes (username triggers the setter validation)
        self.username = username
        self.role = role

    @property
    def username(self):
        """Getter for the username property."""
        return self._username

    @username.setter
    def username(self, value):
        """Setter for username that enforces a minimum length of 5 characters."""
        if len(value) < 5:
            raise ValueError("Username too short")

        # Store the validated value in a protected attribute
        self._username = value

    def __str__(self):
        """Return a formatted string representation of the User object."""
        return (
            f"ID: {self.id} | "
            f"{self.name} | "
            f"{self.role}"
        )