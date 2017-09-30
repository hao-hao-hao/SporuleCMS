from flask import Blueprint


#Create new Blueprint
admin = Blueprint("admin",__name__,template_folder="templates")

from app.modules.admin.views import user_management_view, post_management_view, navigation_management_view,category_management_view, tag_management_view
