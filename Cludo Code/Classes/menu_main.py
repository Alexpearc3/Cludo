from menu_run import Menu_Run

mr = Menu_Run()

while mr.running:
    mr.curr_menu.display_menu()
    mr.menu_loop()