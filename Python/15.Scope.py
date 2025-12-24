# Interview Questions

# What is python namespace?
"""
A namespace in Python is a container (like a dictionary) that maps names (variables, functions, classes)
to objects. It ensures names are unique within their scope and prevents naming conflicts.

Types of Namespaces:
Built-in - Contains print(), len(), int(), etc. (always available)

Global - Module-level names (created when module loads)

Local - Function/method-level names (created when function called)

Enclosing - Nested functions (outer function's namespace)
"""
x = "global"  # Global namespace

def outer():
    y = "outer"  # Enclosing namespace
    
    def inner():
        z = "inner"  # Local namespace
        print(x, y, z)  # Looks: local → enclosing → global → built-in
    
    inner()

outer()
# LEGB Rule (name lookup order):
# Local → Enclosing → Global → Built-in

# What is Global and Local scope in Python?
"""Global scope = module-level variables (accessible everywhere for reading). 
Local scope = function-level variables (only accessible inside that function)."""