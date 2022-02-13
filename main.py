from flask import Flask, request

app = Flask(__name__)


@app.route('/emails/create/')
def email_create():
    name = request.args['name']
    phone = request.args['phone']

    import sqlite3
    db = sqlite3.connect('example.sqlite')
    cur = db.cursor()
    sql = f'''
        INSERT INTO emails (name, phone)
        VALUES ('{name}', '{phone}');
        '''
    cur.execute(sql)
    db.commit()
    db.close()
    return 'ok'


@app.route('/emails/read/')
def read_emails():
    id_ = request.args.get('id')
    import sqlite3
    db = sqlite3.connect('example.sqlite')
    cur = db.cursor()
    if id_:
        sql = f'''SELECT * FROM emails WHERE id={id_};'''
    else:
        sql = f'''SELECT * FROM emails;'''
    cur.execute(sql)
    results = cur.fetchall()
    db.close()
    return str(results)


@app.route('/emails/update/')
def email_update():
    id_ = request.args['id']
    name = request.args['name']

    import sqlite3
    db = sqlite3.connect('example.sqlite')
    cur = db.cursor()
    sql = f'''
            UPDATE emails
            SET name='{name}'
            WHERE id={id_};
            '''
    cur.execute(sql)
    db.commit()
    db.close()
    return 'ok'


@app.route('/emails/delete/')
def email_delete():
    import sqlite3
    db = sqlite3.connect('example.sqlite')
    cur = db.cursor()
    sql = f'''DELETE FROM emails WHERE id={5};'''
    cur.execute(sql)
    db.commit()
    results = cur.fetchall()
    db.close()
    return 'ok'




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)