from ui.create_user_view import CreateUserView
from services.budget_service import budget_service
class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_create_user_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None


    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root, budget_service, handle_create_user = self._handle_create_user
        )

        self._current_view.pack()
    
    def _handle_create_user(self, username, password):
        print(f"Creating user: {username} with password: {password}")