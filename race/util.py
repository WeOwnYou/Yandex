import pygame
B_CONTINUE = 'CONTINUEBUTTONCHECKCODE'
B_EXIT = 'EXITBUTTONCHECKCODE'
B_EXIT_MENU = "EXITTOMENUCHECKCODE"
B_START = "STARTCHECKCODE"
B_START_GAME = "STARTGAMECHECKCODE"
B_NEXT_MAP = "NEXTMAPCHECKCODE"
action_list = {B_CONTINUE:"""
game_GUI.get_GUIElement_by_name('menu_overlay').visible = not game_GUI.get_GUIElement_by_name('menu_overlay').visible
game_GUI.get_GUIElement_by_name('continue').visible = not game_GUI.get_GUIElement_by_name('continue').visible
game_GUI.get_GUIElement_by_name('exit_game').visible = not game_GUI.get_GUIElement_by_name('exit_game').visible
paused = not paused 
""",
               B_EXIT:"""major_gamecycle = False
gamecycle = False
game = False
""",
               B_EXIT_MENU:"""
gamecycle = True
game = False
""",
               B_START: """
menu_GUI.get_GUIElement_by_name('Start').visible = not menu_GUI.get_GUIElement_by_name('Start').visible
menu_GUI.get_GUIElement_by_name('End').visible = not menu_GUI.get_GUIElement_by_name('End').visible
menu_GUI.get_GUIElement_by_name('Map').visible = not menu_GUI.get_GUIElement_by_name('Map').visible
menu_GUI.get_GUIElement_by_name('BackMenuMap').visible = not menu_GUI.get_GUIElement_by_name('BackMenuMap').visible
menu_GUI.get_GUIElement_by_name('NextMap').visible = not menu_GUI.get_GUIElement_by_name('NextMap').visible
""",
               B_START_GAME: """
gamecycle = False
map_name = util.MAP_LIST[map_index]
game = True
""",
               B_NEXT_MAP: """
map_index += 1
map_index %= len(util.MAP_LIST)
menu_GUI.get_GUIElement_by_name('Map').add_text(util.MAP_LIST[map_index])
""",
               }
MAP_LIST = ['MAP1', 'MAP2', 'map3']


