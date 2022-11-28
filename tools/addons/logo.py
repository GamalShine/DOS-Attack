"""This module provides a function that prints the logo's application."""


def show_logo() -> None:
    """Print the application logo.

    Args:
        None

    Returns:
        None
    """  
    logo = """KONTOL """

    CRED2 = "\33[91m"
    print(CRED2 + logo + CRED2)
    print("├───DOS TOOL LAYER 7")
