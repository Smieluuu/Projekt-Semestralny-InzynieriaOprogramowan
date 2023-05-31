from flask import Flask
from views import PingView, CreateUserView, GetUsersView, PostUsersView, PutUsersView, PatchUsersView, DeleteUsersView
from controllers import AddUserController, GetUserController, PostUserController, PutUserController, PatchUserController, DeleteUserController
from repositories import UserRepository

app = Flask(__name__)


# add controller to app routes here (app.add_url_rule)
app.add_url_rule('/ping', view_func=PingView.as_view('ping'))
app.add_url_rule('/users', view_func=CreateUserView.as_view('create_user'), controller=AddUserController(UserRepository()))
app.add_url_rule('/users/get', view_func=GetUsersView.as_view('get_users'), controller=GetUserController(UserRepository()))
app.add_url_rule('/users/post', view_func=PostUsersView.as_view('post_users'), controller=PostUserController(UserRepository()))
app.add_url_rule('/users/put/<int:id>', view_func=PutUsersView.as_view('put_users'), controller=PutUserController(UserRepository()))
app.add_url_rule('/users/patch/<int:id>', view_func=PatchUsersView.as_view('patch_users'), controller=PatchUserController(UserRepository()))
app.add_url_rule('/users/delete/<int:id>', view_func=DeleteUsersView.as_view('delete_users', controller=DeleteUserController(UserRepository())))
