from service import app
from service.db import init_db

if __name__ == '__main__':
    init_db()
    app.run()
