from flask import Flask
from views import PingView, CreateUserView, GetUsersView, PostUsersView, PutUsersView, PatchUsersView, DeleteUsersView

app = Flask(__name__)

app.add_url_rule('/ping', view_func=PingView.as_view('ping'))
app.add_url_rule('/users', view_func=CreateUserView.as_view('create_user'))
app.add_url_rule('/users/get', view_func=GetUsersView.as_view('get_users'))
app.add_url_rule('/users/post', view_func=PostUsersView.as_view('post_users'))
app.add_url_rule('/users/put/<int:id>', view_func=PutUsersView.as_view('put_users'))
app.add_url_rule('/users/patch/<int:id>', view_func=PatchUsersView.as_view('patch_users'))
app.add_url_rule('/users/delete/<int:id>', view_func=DeleteUsersView.as_view('delete_users'))
