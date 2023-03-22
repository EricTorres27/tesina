class Baseconfig():
    SECRET_KEY= "key"
    DEBUG= True
    TESTING= True

class ProductionConfig(Baseconfig):
    DEBUG= False
    TESTING= False
    
class DevelopmentConfig(Baseconfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/aplicacion_tesina'
    SQLALCHEMY_TRACK_MODIFICATIONS = False