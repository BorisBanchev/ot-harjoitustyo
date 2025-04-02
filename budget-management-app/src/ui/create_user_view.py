from tkinter import ttk, StringVar, constants
from services.user_service import user_service, UsernameExistsError, PasswordsNotMatchingError, InvalidPasswordOrUsernameError, EmptyUsernameOrPasswordError


class CreateUserView:
    def __init__(self, root, user_service, handle_create_user):
        self._root = root
        self._handle_create_user = handle_create_user
        self._user_service = user_service
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._confirm_password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        self._hide_error()
        username = self._username_entry.get()
        password = self._password_entry.get()
        confirm_password = self._confirm_password_entry.get()

        try:
            user_service.create_user(username, password, confirm_password)
            self._handle_create_user()

        except EmptyUsernameOrPasswordError:
            self._show_error("Username and password must not be empty values")
        except UsernameExistsError:
            self._show_error(f"Username {username} already exists")
        except PasswordsNotMatchingError:
            self._show_error("Passwords do not match")
        except InvalidPasswordOrUsernameError:
            self._show_error(
                "Password and username must have a length of at least 4")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_fields(self):
        # password label and entry
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame, show="*")
        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)
        # confirm_password label and entry
        confirm_password_label = ttk.Label(
            master=self._frame, text="Confirm Password")
        self._confirm_password_entry = ttk.Entry(master=self._frame, show="*")
        confirm_password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._confirm_password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_fields()

        create_user_button = ttk.Button(
            master=self._frame,
            text="Create User",
            command=self._create_user_handler
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()
