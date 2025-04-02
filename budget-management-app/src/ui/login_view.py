from tkinter import ttk, constants, StringVar


class LoginView:
    def __init__(self, root, handle_login, handle_show_create_user):
        self._root = root
        self._handle_login = handle_login
        self._handle_show_create_user = handle_show_create_user
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame, show="*")
        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _handle_login_click(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if not username or not password:
            self._show_error("Username and password are required!")
            return

        try:
            self._handle_login(username, password)
        except Exception as e:
            self._show_error(str(e))

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._handle_login_click
        )
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        create_user_button = ttk.Button(
            master=self._frame,
            text="Create User",
            command=self._handle_show_create_user
        )
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )
        self._error_label.grid(padx=5, pady=5)
        self._hide_error()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
