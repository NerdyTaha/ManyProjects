# Code to implement a mini version of flask 

class MiniFlask:
    # This will have a constructor, for any instance being made, a decorator, a run function
    def __init__(self):
        self.routes = {}  #Create an empty dictionary to store which function to call when a path is being accessed (Handler mapping)

    # Decorator function: this would register a certain path to a certain function
    # So that the programmer can use decorator above any function and that path gets registered in the dictionary 
    def route(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator
    # The purpose of this decorator is to register (using a dictionary) a path with the function on top of which this decorator is there

    def run(self, path):
        if path in self.routes:
            return self.routes[path]() # call the function that is registerd function for that path
        else:
            return "404 not found"

app = MiniFlask()

@app.route("/")
def index():
    return "Hello world"

@app.route("/about")
def about():
    return "About page"


print(app.run("/"))
print(app.run("/about"))
print(app.run("/randomStuff"))