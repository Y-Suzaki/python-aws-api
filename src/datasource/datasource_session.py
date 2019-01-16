from sqlalchemy.orm import sessionmaker
import datasource_settings


class SessionContext:
    def __init__(self):
        print('init')
        session_maker = sessionmaker(bind=datasource_settings.ENGINE, expire_on_commit=False)
        self.session = session_maker()

    def __enter__(self):
        print('enter')
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        self.session.flush()
        self.session.commit()
        self.session.close()

