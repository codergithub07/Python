# Importing all functions (may/may not use all) from the module & always using module name before function name separated by a dot :
    
    # import make_pizza # This imports all the functions from the make_pizza file
        # make_pizza.pizza('12', 'papperoni')
        # make_pizza.pizza('16', 'paneer', 'onion', 'olives')
        
# Note :- The file to be imported, must be in same directory




# Importing a specific function from module :

    # from make_pizza import pizza # This imports the function named, pizza from make_pizza file/module
        # pizza('12', 'green paper')
        # pizza('16', 'paneer', 'onion')




# Calling imported function by given alias (nickname) :

    # from make_pizza import pizza as p
    # p('12', 'red paper')
    # p('16', 'paneer', 'olives')




# Calling an imported module by given alias :

    # import make_pizza as mp
    # mp.pizza('12', 'papperoni')
    # mp.pizza('16', 'paneer', 'bell paper', 'olives')




# Copyig all functions from a module to this original program file :

    # from make_pizza import *
    # pizza('12', 'capsicum')
    # pizza('16', 'paneer', 'tomato', 'mashroom')