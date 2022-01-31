from flask_frozen import Freezer
import time

from main import app

freezer = Freezer(app)

if __name__ == '__main__':
    print('Freezing app...')
    start = time.time()
    freezer.freeze()
    end = time.time()
    print('Time: {} seconds'.format(end - start))
