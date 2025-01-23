from flask import Flask, render_template, request, jsonify
from insert_funcs import insert_sents, insert_word
import sqlite3 as sl

app = Flask(__name__)

@app.route("/")
def fnc():
    return render_template('sqlite.html')

@app.route('/insert_sent', methods=['GET', 'POST'])
def sent():
    to_insert = []
    data = request.get_json()
    splt_data = data['sentence'].split('\n')
    for snt in splt_data:
        snt = (snt, )
        to_insert.append(snt)
    insert_sents(to_insert)
    return data

@app.route('/get_morph', methods=['GET', 'POST'])
def get_morph():
    data = request.get_json()
    wrd = data['word']
    result = {'answer': '\nВ словаре нет этого слова! Вы можете добавить его через форму ниже.'}
    con = sl.connect('sqlite_python.db')
    mrph = ''
    with con:
        info = con.execute("SELECT * FROM morphemes")
        for row in info:
         if row[0] == wrd:
             mrph = row[1]
             break
    if mrph != '':
        sent_list = []
        with con:
            info = con.execute("SELECT * FROM sentences")
            for row in info:
                if f'{wrd}' in row[0].lower():
                    sent_list.append(row[0])
        if sent_list == []:
            result['answer'] = '\n' + mrph + '\n\n' + 'В базе нет предложений, содержащих это слово!'
        else:
            result['answer'] = '\n' + mrph + '\n\n' + '\n'.join(sent_list)
    print(result)
    return jsonify(result)

@app.route('/insert_word', methods=['GET', 'POST'])
def word():
    data = request.get_json()
    wrd, mrph = data['word'].split('/')
    check = 0
    con = sl.connect('sqlite_python.db')
    with con:
        info = con.execute("SELECT * FROM morphemes")
        for row in info:
            if wrd == row[0]:
                check = 1
    if check == 0:
        insert_word((wrd, mrph))
        answ = {'reaction': '\nСлово успешно добавлено!'}
    if check == 1:
        answ = {'reaction': '\nСлово уже есть в базе!'}
    return jsonify(answ)

if __name__ == "__main__":
    app.run(debug=True)