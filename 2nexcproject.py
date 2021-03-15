canteen_menu = ["-------", "MENU:", "mince pie", "lolly cake", "cookie", "sandwich", "-------"]
my_cart = []
continue_option = ""
desired_item = ""

while continue_option != ("no"):
  for item in canteen_menu:
    print(item)
  desired_item = input("what would you like to order?: ")
  if desired_item in canteen_menu:
    my_cart.append (desired_item)
    continue_option = input("would you like to add another item? yes/ no: ")
  else:
    print("sorry, that's not on the menu")
  

print("your finished order:")
for item in my_cart:
  print(item)
