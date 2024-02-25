# def greet_user(names):
    # for name in names:
        # print("Hello " + name + ", have a nice day!")
# greet_user(['james', 'kite', 'rom'])




# Modifying a list in a function :

    # Example 1 :
        # def complete_models(unprinted_models, completed_models):
            # while unprinted_models:
                # current_model = unprinted_models.pop()
                # print('Currently ' + current_model + ' is getting printed')
                # completed_models.append(current_model)
        # def print_models(completed_models):
            # print("The completed models are:")
            # for i in completed_models:
                # print(i)
        # completed_models = []
        # complete_models(['audi', 'bmw', 'hyundai'], completed_models)
        # print_models(completed_models)

    # Example 2 : List of orders getting printed
        # def order_status(incomplete_orders, completed_orders):
            # while incomplete_orders:
                # currrent_order = incomplete_orders.pop()
                # print(currrent_order + " is getting packed")
                # completed_orders.append(currrent_order)
        # def print_completed_orders(complete_order):
            # print()
            # print("The completed orders are :")
            # for i in complete_order:
                # print(i)
        # incomplete_orders = ['soap', 'brush', 'pens', 'monkey cap']
        # completed_order = []
        # order_status(incomplete_orders, completed_order)
        # print_completed_orders(completed_order)
        # print()

        


# Stopping function from modifying original list :

    # def complete_models(unprinted_models, completed_models):
        # while unprinted_models:
            # current_model = unprinted_models.pop()
            # print('Currently ' + current_model + ' is getting printed')
            # completed_models.append(current_model)
    # def print_models(completed_models):
        # print("\nThe completed models are:")
        # for i in completed_models:
            # print(i)
    # completed_models = []
    # unprinted_models = ['audi', 'bmw', 'hyundai']
    # complete_models(unprinted_models[:], completed_models) # The slice notation sends a copy of the unprinted_models list to the function instead of the original list
    # print_models(completed_models)
    # if unprinted_models:
        # print()
        # print(unprinted_models)
    # else:
        # print()
        # print("the list is empty")
    # print()