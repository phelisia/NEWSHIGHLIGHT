from app import create_app
from flask_script import Manager,Server

app =create_app('development')
manager = Manager(app)

manager.add_command('server',Server)
manager.add_command('server',Server)
# @manager.add_command
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tets)
if __name__ == '__main__':
    app.run()