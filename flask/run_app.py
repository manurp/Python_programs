import os

# from library.simple import app
# from library.html import app
# from library.template_str_inside import app
# from library.template_outside import app
# from library.basic_routing import app
# from library.raising_custom_errors import app
# from library.request_info import app
# from library.redirects import app
from library.simple_database_app import app

if __name__ == "__main__":
    app.debug = True
    # host = os.environ.get('IP', '0.0.0.0')
    # port = int(os.environ.get('PORT', 8080))
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
    # app.run()
