
class Config:
    SECRET_KEY='\xb3\t\x92mr\xb7\xed=lx1V\xdf@H\xa1Rp\xf5\xbb\xb3I\x98\xaa'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI ='mysql+mysqlconnector://root:123456@localhost:3306/lightblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

config={'development':DevelopmentConfig}