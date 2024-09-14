
global_var = "I am a global variable"

def example_function():
    
    local_var = "I am a local variable"
    
    print(local_var)  
    print(global_var)  

def modify_global_var():
    global global_var  
    global_var = "I have been modified globally"

def main():
    print("Before modifying global variable:")
    example_function()
    
    modify_global_var()
    
    print("\nAfter modifying global variable:")
    example_function()

if __name__ == "__main__":
    main()