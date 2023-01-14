import tui

menu_option = tui.main_menu()

if menu_option == 1:
    tui.progress("Data Processing", 0)
    sub_menu_option = tui.sub_menu(1)
    if sub_menu_option == 1:
        tui.progress("review retrieval process.py", 0)



