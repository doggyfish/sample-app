def greet(name, uppercase=False):
    name = name.strip() or "stranger"
    greeting = f"hello, {name}!"
    return greeting.upper() if uppercase else greeting
