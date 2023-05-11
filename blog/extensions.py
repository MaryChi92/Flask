from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_pydantic_spec import FlaskPydanticSpec
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from blog.admin.views import CustomAdminIndexView

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
admin = Admin(
    index_view=CustomAdminIndexView(),
    name='Blog Admin Panel',
    template_mode='bootstrap4'
)

api = FlaskPydanticSpec('flask', version='1.0')
