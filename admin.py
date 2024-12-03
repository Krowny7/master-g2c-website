from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for
from models import db, User, News, Application, Event, Teacher, Ranking

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

class SecureAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin
        
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

class NewsAdmin(SecureModelView):
    column_list = ('title', 'published', 'created_at')
    column_searchable_list = ('title', 'content')
    column_filters = ('published', 'created_at')
    form_columns = ('title', 'content', 'image_path', 'published')

class ApplicationAdmin(SecureModelView):
    column_list = ('last_name', 'first_name', 'email', 'status', 'created_at')
    column_searchable_list = ('last_name', 'first_name', 'email')
    column_filters = ('status', 'created_at')
    form_columns = ('first_name', 'last_name', 'email', 'phone', 'education', 'motivation', 'cv_path', 'status')

class EventAdmin(SecureModelView):
    column_list = ('title', 'date', 'location')
    column_searchable_list = ('title', 'description')
    column_filters = ('date',)
    form_columns = ('title', 'description', 'date', 'location', 'image_path')

class TeacherAdmin(SecureModelView):
    column_list = ('last_name', 'first_name', 'title', 'email', 'order')
    column_searchable_list = ('last_name', 'first_name', 'email')
    column_filters = ('title', 'created_at')
    form_columns = ('first_name', 'last_name', 'title', 'description', 
                   'email', 'image_path', 'order')
    column_sortable_list = ('last_name', 'first_name', 'order')
    column_default_sort = 'order'

class RankingView(SecureModelView):
    column_list = ['position', 'year', 'category', 'source']
    form_columns = ['position', 'year', 'category', 'source', 'url']
    column_default_sort = ('year', True)

def init_admin(app):
    admin = Admin(app, name='Master G2C Admin', template_mode='bootstrap4', index_view=SecureAdminIndexView())
    admin.add_view(NewsAdmin(News, db.session))
    admin.add_view(ApplicationAdmin(Application, db.session))
    admin.add_view(EventAdmin(Event, db.session))
    admin.add_view(TeacherAdmin(Teacher, db.session, name='Équipe'))
    admin.add_view(RankingView(Ranking, db.session))
    return admin
