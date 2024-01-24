import logging
import flet as ft
from utils import get_options, first_run

if_first_run = first_run()

options = get_options()

class MenuBar(ft.UserControl):
    def build(self):
        menubar = ft.MenuBar(
            expand=True,
            style=ft.MenuStyle(
                alignment=ft.alignment.top_left,
                # mouse_cursor={ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                #           ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
            ),
            controls=[
                ft.SubmenuButton(
                    expand=True,
                    height=30,
                    content=ft.Text("File"),
                    controls=[
                        ft.MenuItemButton(
                            height=30,
                            content=ft.Text("Save"),
                            leading=ft.Icon(ft.icons.SAVE),
                        ),
                        ft.MenuItemButton(
                            height=30,
                            content=ft.Text("Import Files"),
                            leading=ft.Icon(ft.icons.FILE_COPY),
                        ),
                        ft.SubmenuButton(
                            height=30,
                            content=ft.Text("Import and Export Folders"),
                            leading=ft.Icon(ft.icons.FOLDER),
                            controls=[
                                ft.SubmenuButton(
                                    height=30,
                                    content=ft.Text("Pause"),
                                    leading=ft.Icon(ft.icons.PAUSE),
                                    controls=[
                                        ft.MenuItemButton(
                                            height=30,
                                            content=ft.Text("Pause Import"),
                                            leading=ft.Icon(ft.icons.PAUSE),
                                        ),
                                        ft.MenuItemButton(
                                            height=30,
                                            content=ft.Text("Pause Export"),
                                            leading=ft.Icon(ft.icons.PAUSE),
                                        ),
                                    ],
                                ),
                                ft.MenuItemButton(
                                    height=30,
                                    content=ft.Text("Check import folder now"),
                                    leading=ft.Icon(ft.icons.FOLDER),
                                ),
                                ft.SubmenuButton(
                                    height=30,
                                    content=ft.Text("Run emport folders now"),
                                    leading=ft.Icon(ft.icons.FOLDER),
                                ),
                            ],
                        ),
                        #ft.Divider(),
                        ft.MenuItemButton(
                            height=30,
                            content=ft.Text("Open"),
                            leading=ft.Icon(ft.icons.FOLDER_OPEN),
                        ),
                        #ft.Divider(),
                        ft.MenuItemButton(
                            height=30,
                            content=ft.Text("Options"),
                            leading=ft.Icon(ft.icons.SETTINGS),
                        ),
                        ft.MenuItemButton(
                            height=30,
                            content=ft.Text("Shortcuts"),
                            leading=ft.Icon(ft.icons.KEYBOARD),
                        ),
                        ft.MenuItemButton(
                            height=30,
                            content=ft.Text("Minimize to system tray"),
                            leading=ft.Icon(ft.icons.ARROW_DOWNWARD),
                        ),
                        ft.MenuItemButton(
                            height=30,
                            content=ft.Text("Restart"),
                            leading=ft.Icon(ft.icons.REFRESH),
                        ),
                        ft.MenuItemButton(
                            height=30,
                            content=ft.Text("Exit Force Maintainance"),
                            leading=ft.Icon(ft.icons.CONSTRUCTION),
                        ),
                        ft.MenuItemButton(
                            height=30,
                            content=ft.Text("Quit"),
                            leading=ft.Icon(ft.icons.CLOSE),
                        )
                    ],
                ),
                ft.SubmenuButton(
                    expand=True,
                    height=30,
                    content=ft.Text("View"),
                    controls=[
                        ft.SubmenuButton(
                            height=30,
                            content=ft.Text("Zoom"),
                            leading=ft.Icon(ft.icons.LOCATION_SEARCHING),
                            controls=[
                                ft.MenuItemButton(
                                    height=30,
                                    content=ft.Text("Magnify"),
                                    leading=ft.Icon(ft.icons.ZOOM_IN),
                                    close_on_click=False,
                                    style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.PURPLE_200}),
                                ),
                                ft.MenuItemButton(
                                    height=30,
                                    content=ft.Text("Minify"),
                                    leading=ft.Icon(ft.icons.ZOOM_OUT),
                                    close_on_click=False,
                                    style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.PURPLE_200}),
                                )
                            ],
                        ),
                    ],
                ),
                ft.SubmenuButton(
                    expand=True,
                    height=30,
                    content=ft.Text("Pages"),
                ),
                ft.SubmenuButton(
                    expand=True,
                    height=30,
                    content=ft.Text("Database"),
                ),
                ft.SubmenuButton(
                    expand=True,
                    height=30,
                    content=ft.Text("Network"),
                ),
                ft.SubmenuButton(
                    expand=True,
                    height=30,
                    content=ft.Text("Services"),                   
                ),
                ft.SubmenuButton(
                    expand=True,
                    height=30,
                    content=ft.Text("Tags"),
                ),
                ft.SubmenuButton(
                    expand=True,
                    visible=False,
                    height=30,
                    content=ft.Text("Pending"),
                ),
                ft.SubmenuButton(
                    expand=True,
                    height=30,
                    content=ft.Text("Help"),
                    controls=[
                        ft.MenuItemButton(
                            height=30,
                            content=ft.Text("About"),
                            leading=ft.Icon(ft.icons.INFO),
                            )
                        ],
                    ),
            ],
        )
        return menubar
    
class PageOfPages(ft.UserControl):
    def build(self):
        tabs = [
                ft.Tab(
                    text="All",
                    content=ft.Row(
                        expand=1,
                        controls=[
                            SearchPanel(expand=4),
                            ft.VerticalDivider(width=0.1),
                            ft.Container(
                                expand=15,
                                content=ft.Text("Results", expand=True),
                                )
                        ]
                    ),
                ),
                #ft.Tab(tab_content=ft.Icon(ft.icons.ADD), visible=False),
                ]
        t = ft.Tabs(
            expand=8,
            selected_index=0,
            tabs=tabs,
        )

        return t

class SearchPanel(ft.UserControl):
    """This is the left search panel."""
    def build(self):
        search = ft.SearchBar(
            view_shape=ft.ContinuousRectangleBorder(),
            expand=8,
        )

        file_sort = ft.Row(
                    spacing=10,
                    controls=[
                        ft.ElevatedButton(
                            content=ft.Text(
                                "sort by tags: series-creator-title-volume-chapter-page",
                                 no_wrap=True,
                                 text_align="center",
                                 max_lines=1,
                                 color=ft.colors.WHITE,
                                 ),
                            expand=4,
                            style=ft.ButtonStyle(
                                shape=ft.ContinuousRectangleBorder(),
                                elevation=5,
                                padding=5,
                                
                            ),
                        ),
                        ft.ElevatedButton(
                            content=ft.Text(
                                "display tags",
                                 no_wrap=True,
                                 text_align="center",
                                 max_lines=1,
                                 color=ft.colors.WHITE,
                                 ),
                            expand=2,
                            style=ft.ButtonStyle(
                                shape=ft.ContinuousRectangleBorder(),
                                elevation=5,
                                padding=5,                                
                            ),
                        ),
                        ft.ElevatedButton(
                            content=ft.Text(
                                "a-z",
                                 no_wrap=True,
                                 text_align="center",
                                 max_lines=1,
                                 color=ft.colors.WHITE,
                                 ),
                            expand=1,
                            style=ft.ButtonStyle(
                                shape=ft.ContinuousRectangleBorder(),
                                elevation=5,
                                padding=5,
                                
                            ),                            
                        ),
                        ft.ElevatedButton(
                            content=ft.Text(
                                "tags",
                                 no_wrap=True,
                                 text_align="center",
                                 max_lines=1,
                                 color=ft.colors.WHITE,
                                 ),
                            expand=1,
                            style=ft.ButtonStyle(
                                shape=ft.ContinuousRectangleBorder(),
                                elevation=5,
                                padding=5,
                                
                            ),                            
                        ),
                    ],
                    expand=1,
                )
        
        file_collection = ft.Row(
                    spacing=10,
                    controls=[
                        ft.ElevatedButton(
                            content=ft.Text(
                                "no collections",
                                 no_wrap=True,
                                 text_align="center",
                                 max_lines=1,
                                 color=ft.colors.WHITE,
                                 ),
                            expand=3,
                            style=ft.ButtonStyle(
                                shape=ft.ContinuousRectangleBorder(),
                                elevation=5,
                                padding=5,
                                
                            ),
                        ),
                        ft.ElevatedButton(
                            content=ft.Text(
                                "collected unmatched",
                                 no_wrap=True,
                                 text_align="center",
                                 max_lines=1,
                                 color=ft.colors.WHITE,
                                 ),
                            expand=2,
                            style=ft.ButtonStyle(
                                shape=ft.ContinuousRectangleBorder(),
                                elevation=5,
                                padding=5,                                
                            ),
                        ),
                        ft.ElevatedButton(
                            content=ft.Text(
                                "tags",
                                 no_wrap=True,
                                 text_align="center",
                                 max_lines=1,
                                 color=ft.colors.WHITE,
                                 ),
                            expand=1,
                            style=ft.ButtonStyle(
                                shape=ft.ContinuousRectangleBorder(),
                                elevation=5,
                                padding=5,  
                            ),                            
                        ),
                    ],
                    expand=1,
                )
    

        search_panel = ft.Container(
            margin=0,
            padding=0,
            content=ft.Column(
                spacing=0,
                tight=True,
                run_spacing=0,
                controls=[
                    file_sort,
                    file_collection,
                    ft.Row(
                        wrap=True,
                        expand=2,
                        controls=[
                            ft.Divider(height=1),
                            ft.Text(
                                "search",
                                no_wrap=True,
                                text_align="center",
                                max_lines=1,
                                color=ft.colors.WHITE,
                                width=350,
                            ),
                            ft.Divider(height=0.1),
                    ],
                    ),
                    ft.Column(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.top_left,
                                #height=300,
                                width=400,
                                padding=5,
                                bgcolor=ft.colors.GREY_900,
                                content=
                                ft.Text(
                                    "system:inbox (3,223,005)",
                                    no_wrap=True,
                                    text_align="left",
                                    max_lines=1,
                                    color=ft.colors.WHITE,
                                    width=350,
                                    expand=True,
                                ),
                                expand=1,
                            ),
                        ],
                        expand=5,
                    ),
                    ft.Row(
                        controls=[
                        search,
                        ft.IconButton(
                            expand=1,
                            icon=ft.icons.EVENT_NOTE_OUTLINED,
                            style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(),
                                    elevation=5,
                                    padding=1,
                                    bgcolor=ft.colors.GREY_800,
                                    ),
                            ),
                        ft.IconButton(
                            expand=1,
                            icon=ft.icons.STAR,
                            style=ft.ButtonStyle(
                                    shape=ft.ContinuousRectangleBorder(),
                                    elevation=5,
                                    padding=1,
                                    bgcolor=ft.colors.GREY_800,
                                    ),
                            ),
                        ],
                        expand=1,
                    ),
                    ft.Column(
                        expand=8,
                        alignment=ft.alignment.top_center,
                        controls=[
                            ft.Divider(height=0.1),
                            ft.Text(
                                "selection tags",
                                no_wrap=True,
                                text_align="center",
                                max_lines=1,
                                color=ft.colors.WHITE,
                                width=350,
                            ),
                            ft.Divider(height=0.1),
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        alignment=ft.alignment.top_left,
                                        #height=300,
                                        width=400,
                                        padding=0,
                                        border_radius=5,
                                        bgcolor=ft.colors.GREY_900,
                                        content=
                                        ft.Text(
                                            "1",
                                            no_wrap=True,
                                            text_align="left",
                                            max_lines=1,
                                            color=ft.colors.WHITE,
                                            width=350,
                                            expand=True,
                                        ),
                                        expand=1,
                                    ),
                                ],
                                expand=5,
                            ),
                        ],
                    ),
                    ft.Divider(height=0.1),
                    ft.Container(
                            alignment=ft.alignment.center,
                            padding=1,
                            bgcolor=ft.colors.GREY_900,
                            content=
                            ft.Image(
                                src="assets/image_viewer_background.png",
                                expand=1,
                                fit=ft.ImageFit.FILL,
                            ),
                            expand=9,
                        ),
                ],
            ),
                        )
        
        return search_panel

class BottomBar(ft.UserControl):
    def build(self):
        search_info = ft.Text(
            "no search",
            tooltip="No Search",
            text_align="left",
            size=13,
            expand=7,
            no_wrap=True,
            )
        network_info = ft.Text(
            "16.5 GB (1 MB/s)",
            tooltip="Total bandwidth used on this session, and current network speed.", 
            text_align="left",
            size=13,
            no_wrap=True,
            expand=1,
            )
        status = ft.Text(
            "idle", 
            tooltip="Simple status of the application", 
            text_align="left",
            size=13,
            no_wrap=True,
            expand=1,
            )
        current_job = ft.Text(
            "no job", 
            tooltip="Current job", 
            text_align="left",
            size=13,
            no_wrap=True,
            expand=3,
            )

        bottombar = ft.Column(
            expand=1,
            controls=[
                ft.Divider(height=0.01),
                ft.Row(
                    tight=True,
                    controls=[
                        search_info,
                        network_info,
                        status,
                        current_job,
                    ],
                ),
                ft.Divider(height=0.01),
            ],
        )
        return bottombar

class PopUp(ft.UserControl):
    def build(self):

        popup = ft.FloatingActionButton(
                    shape=ft.ContinuousRectangleBorder(),
                    width=250,
                    height=30,
                    bgcolor=ft.colors.GREY_900, 
                    tooltip="",
                    content=ft.Row(
                        expand=1,
                        controls=[
                            ft.Text(
                                "10 messages",
                                expand=3, 
                                text_align="center", 
                                no_wrap=True
                                ),
                            ft.TextButton("dismiss all",
                                           style=ft.ButtonStyle(
                                               bgcolor=ft.colors.GREY_700,
                                               color=ft.colors.GREY_50,
                                               padding=5,
                                               shape=ft.ContinuousRectangleBorder(),
                                               ),
                                               expand=2,
                                               tooltip="Dismiss all empty popup messages.",
                                            ),
                            ft.Icon(
                                ft.icons.KEYBOARD_ARROW_UP,
                                expand=1,
                                tooltip="Expand to show all the popup messages.",
                                ),
                            ],
                    ),
                )
        
        return popup

def main(page: ft.Page):
    """This is the main function of the frontend. It is called when the frontend is started."""
    
    # Most of these hardcoded options bellow will later go into the Options menu, to a db or config file and loaded from there.

    # Set the page title and theme mode.
    page.title = "Mai Media Manager"
    page.theme_mode = 'dark'
    
    # set padding to 0 to remove the default padding or the menu bar and bottom bar will look out of place.
    page.padding = 0
    
    # set to auto to enable scrollbars so we can see if anything have been pushed off the screen
    #page.scroll = "AUTO" 
    
    page.window_maximized = True

    # Create our page content.
    page.add(
        ft.Column(
            expand=1,
            controls=[
                MenuBar(),
                #ft.Divider(height=0.1), # This adds a divider between the menu bar and the tabs which makes it look better but uses a bit more space.
                PageOfPages().build(), # This is a workaround to get the page to show up. 
                #PopUp(),
                BottomBar(),
            ],
        )
    )

    # Create our popup manager.
    page.floating_action_button = PopUp().build()
    page.floating_action_button_location = (260, 80)

    page.update()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    ft.app(target=main, port=8000)