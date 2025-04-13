def print_menu(options):
    for idx, option in enumerate(options):
        print(f"({idx + 1}) {option.capitalize()}")
    
    menu_selection = 0
    while menu_selection <= 0 or menu_selection > len(options):
        menu_selection = int(input(f"Select a menu option (1-{len(options)}): "))
    
    print("")
    return menu_selection