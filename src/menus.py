def print_menu(options):
    for idx, option in enumerate(options):
        print(f"({idx + 1}) {option.capitalize()}")
    
    menu_selection = 0
    while menu_selection <= 0 and menu_selection >= len(options):
        menu_selection = input(f"Select 1-{len(options)}:")
    
    return menu_selection