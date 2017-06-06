from app import db
from app.decorators import links
from flask import abort
from app.forms import Super_Form
from app.helpers import Helper

class Navigation(db.Model):
    _tablename_="navigation"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable = False)
    link= db.Column(db.String(255))
    parent_id = db.Column(db.Integer)
  #properties below are only for displaying the information, they are not stored in database
    parent_name = ""
    all_children=[]
    children = []
      


    #add itself to the database
    def add_itself(self):
        if self.parent_id == self.id:
            self.parent_id=-1
        navigation_item = Navigation(name=self.name,link=self.link,parent_id=self.parent_id)
        db.session.add(navigation_item)
        db.session.commit()

    #delete itself and all child elements from database
    def delete_itself(self):
        if not Helper.is_None(self):
            children = self.get_children()
            if children is not None:
                for child in children:
                    child.delete_itself()
            db.session.delete(self)
            db.session.commit()

    #get its children navigation items
    def get_children(self):
        return (o for o in Navigation.get_all_items() if o.parent_id == self.id)

    #get the name of parent navigation item
    def get_parent_name(self):
        if self.parent_id !=-1:
            self.parent_name = Navigation.get_item_by_id(self.parent_id).name
            return self.parent_name
        return None
        
    def get_higher_level_navigations(self):
        all_items = Navigation.get_all_items()
        except_items = self.get_all_children()
        except_items.append(self)
        higher_level_items = [o for o in all_items if o not in except_items]
        default_item =  [(-1,"Top Menu")]
        return Super_Form.get_chocies_data(higher_level_items,default_item)

    #needs to rewrite
    def get_all_children(self):
        self.children = self.get_children()
        self.all_children=[]
        print (self.name)
        for child in self.children:
            if not Helper.is_None(child):
                self.all_children.append(child)
                self.all_children.extend(child.get_all_children())
        return self.all_children

    @staticmethod
    def get_item_by_id(id):
        if id != -1:
            item  = Navigation.query.get(id)
            if not Helper.is_None(item):
                if not item.is_top_nav() and item.parent_id != item.id:
                    item.get_parent_name()
                return item
            else:
                return None
        return None

    @staticmethod
    def get_all_items():
        items = Navigation.query.all()
        for item in items:
            if not item.is_top_nav():
                item.get_parent_name()
        return items

    def is_top_nav(self):
        return self.parent_id ==-1

    @staticmethod
    def genenrate_navigation_list(items):
        navigations = []
        parent_ids = [o.parent_id for o in items if not o.is_top_nav()]
        for id in parent_ids:
            parent_item = [o for o in items if o.id == id][0]
            parent_item_index = items.index(parent_item)
            items[parent_item_index].children=[];
            items[parent_item_index].children.extend(o for o in items if o.parent_id == id)
        for item in items:
            if item.is_top_nav():
                navigations.append(item)
        return navigations

'''archived functions


    def change_parent(self,parent_id):
        self.parent_id=parent_id
        db.session.commit()
'''