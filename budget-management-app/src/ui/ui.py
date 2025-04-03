from ui.create_user_view import CreateUserView
from services.user_service import user_service
from ui.add_expense_view import AddExpenseView
from ui.login_view import LoginView
from services.expense_service import expense_service
from ui.show_expenses_view import ShowExpensesView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            handle_login=self._handle_login,
            handle_show_create_user=self._show_create_user_view
        )

        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root, user_service, handle_create_user=self._handle_create_user
        )

        self._current_view.pack()

    def _show_add_expense_view(self):
        self._hide_current_view()

        self._current_view = AddExpenseView(
            self._root,
            handle_expense_adding=self._handle_add_expense,
            handle_show_expenses=self._show_expenses_view
        )
        self._current_view.pack()

    def _show_expenses_view(self):
        self._hide_current_view()

        self._current_view = ShowExpensesView(
            self._root,
            handle_add_expense=self._show_add_expense_view
        )
        self._current_view.pack()

    def _handle_login(self, username, password):
        try:
            user_service.login(username, password)
            self._show_add_expense_view()
        except Exception as e:
            if self._current_view and isinstance(self._current_view, LoginView):
                self._current_view._show_error(str(e))

    def _handle_create_user(self):
        self._show_add_expense_view()

    def _handle_add_expense(self, description, amount, date):
        try:
            expense_service.add_expense(
                description, amount, date, user_service._user.username)
        except Exception as e:
            if self._current_view and isinstance(self._current_view, AddExpenseView):
                self._current_view._show_error(str(e))
