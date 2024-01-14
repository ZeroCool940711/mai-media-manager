
import flet as ft

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
                            #leading=ft.Icon(ft.icons.SAVE),
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
                        ft.MenuItemButton(
                            height=30,
                            content=ft.Text("Save"),
                            #leading=ft.Icon(ft.icons.SAVE),
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
                    content=ft.Text("Tab 1 Content")
                ),
                #ft.Tab(tab_content=ft.Icon(ft.icons.ADD), visible=False),
                # ft.Tab(
                #     text="Tab 2",
                #     content=ft.Text("Tab 2 Content"),
                # ),
                # ft.Tab(
                #     text="Tab 3",
                #     content=ft.Text("Tab 3 Content"),
                # ),
                ]
        t = ft.Tabs(
            expand=1,
            selected_index=0,
            tabs=tabs,
            #height=900,
        )

        return t

class BottomBar(ft.UserControl):
    def build(self):
        search_info = ft.Text("No search", tooltip="No Search", text_align="left", expand=True)
        network_info = ft.Text("16.5 GB (1 MB/s)", tooltip="Total bandwidth used on this session, and current network speed.", text_align="right")
        status = ft.Text("idle", tooltip="Simple status of the application", text_align="right")
        current_job = ft.Text("no job", tooltip="Current job", text_align="right")

        bottombar = ft.Column(
            controls=[
                ft.Divider(height=1),
                ft.Row(
                    controls=[
                        search_info,
                        network_info,
                        status,
                        current_job,
                    ],
                ),
                ft.Divider(height=0.1, thickness=0.1),
            ],
        )
        return bottombar

class PopUp(ft.UserControl):
    def build(self):
        popup = ft.FloatingActionButton(
                    shape=ft.ContinuousRectangleBorder(),
                    
                    width=200,
                    height=30,
                    #right=20,
                    bgcolor=ft.colors.GREY_900,   
                    offset=ft.Offset(0, -1), # hardcoded offset so we can put the FloatingActionButton in the bottom right corner. This SHOULD be changed. 
                    tooltip="",
                    content=ft.Row(
                        controls=[
                            ft.Text("10 messages", expand=True, text_align="left", no_wrap=True),
                            ft.TextButton("dismiss all",
                                           style=ft.ButtonStyle(
                                               bgcolor=ft.colors.GREY_700,
                                               color=ft.colors.GREY_50,
                                               padding=5,
                                               shape=ft.ContinuousRectangleBorder(),
                                               ),
                                               expand=True,
                                            ),
                            ft.Icon(ft.icons.KEYBOARD_ARROW_UP),
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
            expand=True,
            controls=[
                MenuBar(),
                PageOfPages().build(),
                #PopUp(),
                BottomBar(),
            ],
        )
    )

    page.floating_action_button = PopUp().build()
    page.floating_action_button_location = ft.FloatingActionButtonLocation.MINI_END_FLOAT

    page.update()

if __name__ == "__main__":
    ft.app(target=main, port=8000)