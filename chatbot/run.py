# -*- coding: utf-8 -*-
# run.py



from app import app

#@app.route('/success/<name>')
#def success(name):
#   return 'welcome %s' % nam


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
