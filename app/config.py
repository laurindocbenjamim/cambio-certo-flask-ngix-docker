from app.dependencies import os


#
class Config:
    """ """
    SECRET_KEY='&g!8a@B)=zmWUbZ%VpxFsG6Rn_GAMFNd'
    APP_PORT=5000
    UPLOAD_FOLDER = 'app/static/uploads'
    FILES_FOLDER = 'app/static/files'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3', 'mp4', 'webm', 'mkv', 'avi'}
    _DATABASE_URI = "sqlite:///dataframe.db"

    @property
    def DATABASE_URI(self): return self._DATABASE_URI

#
class TestConfig(Config):
    """ """
    _DEBUG=True
    APP_PORT=5001    
    _JDBC=None

    def __init__(self,JDBC='sqlite'):
        self._JDBC = JDBC

        self.load_database()

    @property
    def JDBC(self): return self._JDBC

    @property
    def PORT(self): return self.APP_PORT

    @property
    def DEBUG(self): return self._DEBUG

    


    def load_database(self):
        if self._JDBC !='sqlite':
            self._DATABASE_URI=''


class ProductionConfig(Config):
    DEBUG=False
    DATABASE_URI = "sqlite:///dataframe.db"
    JDBC=None

    def __init__(self,JDBC='sqlite'):
        self.JDBC = JDBC

    @property
    def JDBC(self): return self.JDBC

    @property
    def DATABASE_URI(self): return self.DATABASE_URI
