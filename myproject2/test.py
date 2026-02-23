def show(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
    
show(name="Alice", age=30, city="New York")