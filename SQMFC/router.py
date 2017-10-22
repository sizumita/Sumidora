class MyAppRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'minewebchat':
            return 'chat'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'minewebchat':
            return 'chat'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'minewebchat' or \
           obj2._meta.app_label == 'minewebchat':
           return True

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == 'minewebchat':
            return db == 'chat'