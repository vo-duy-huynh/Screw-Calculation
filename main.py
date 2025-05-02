from datetime import timedelta
from flask import Flask, flash, render_template, request, session, redirect, url_for
import json


app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.secret_key = 'huynhprohtestkey'
app.permanent_session_lifetime = timedelta(days=1)

@app.route('/')
def index():
    return render_template('./index.html')
@app.route('/trough/tab1')
def tab1():
    # Đọc dữ liệu JSON
    with open('data02.json', 'r', encoding='utf-8') as f:
        materials = json.load(f)
    with open('hesodanbac.json', 'r', encoding='utf-8') as f:
        hesodanbacdata = json.load(f)
    return render_template('./trough/tab1.html', materials=materials, hesodanbacdata=hesodanbacdata)
@app.route('/trough/tab2', methods=['POST'])
def tab2():
    session['tytrong'] = request.form.get('tytrong1')
    session['hesovatlieu'] = request.form.get('hesovatlieu1')
    session['hesodienday'] = request.form.get('hesodienday1')
    session['kichthuocvatlieu'] = request.form.get('kichthuocvatlieu1')
    session['khanangchay'] = request.form.get('khanangchay1')
    session['mucdomaimon'] = request.form.get('mucdomaimon1')
    session['tinhchatdacbiet'] = request.form.get('tinhchatdacbiet1')
    session['loaidanbac'] = request.form.get('loaidanbac1')
    session['tenvatlieu'] = request.form.get('tenvatlieu1')
    return redirect(url_for('show_tab2'))

@app.route('/trough/tab2')
def show_tab2():
    if not session.get('tytrong'):
        flash("⚠️ Vui lòng nhập dữ liệu vật liệu trước khi tiếp tục.")
        return redirect(url_for('tab1'))
    return render_template('./trough/tab2.html', data={
        'tytrong': session.get('tytrong'),
        'hesodienday': session.get('hesodienday'),
        'tenvatlieu': session.get('tenvatlieu')
    })
@app.route('/trough/tab3', methods=['POST'])
def tab3():
    fields = [
    'nangsuatm3h', 'nangsuatft3h', 'khoiluongkgh', 'khoiluonglbsh',
    'hesovattulieu', 'gocnghieng', 'hesodienfull',
    'duongkinhcanh', 'buoccanh', 'duongkinhtruc', 'tocdo'
    ]

    for field in fields:
        value = request.form.get(field)
        if value:
            session[field] = value
    return redirect(url_for('show_tab3'))

@app.route('/trough/tab3')
def show_tab3():
    if not session.get('tytrong'):
        flash("⚠️ Vui lòng nhập dữ liệu vật liệu trước khi tiếp tục.")
        return redirect(url_for('tab1'))
    return render_template('./trough/tab3.html', data={
        'tytrong': session.get('tytrong'),
        'hesodienday': session.get('hesodienday'),
        'tenvatlieu': session.get('tenvatlieu')
    })
@app.route('/trough/tab4', methods=['POST'])
def tab4():
    fields = [
    'nangsuatm3h', 'nangsuatft3h', 'khoiluongkgh', 'khoiluonglbsh',
    'hesovattulieu', 'gocnghieng', 'hesodienfull',
    'duongkinhcanh', 'buoccanh', 'duongkinhtruc', 'tocdo'
    ]

    for field in fields:
        value = request.form.get(field)
        if value:
            session[field] = value
    return redirect(url_for('show_tab4'))

@app.route('/trough/tab4')
def show_tab4():
    if not session.get('tytrong'):
        flash("⚠️ Vui lòng nhập dữ liệu vật liệu trước khi tiếp tục.")
        return redirect(url_for('tab1'))
    return render_template('./trough/tab4.html', data={
        'tytrong': session.get('tytrong'),
        'hesodienday': session.get('hesodienday'),
        'tenvatlieu': session.get('tenvatlieu')
    })
@app.route('/trough/tab5', methods=['POST'])
def tab5():
    fields = [
    'nangsuatm3h', 'nangsuatft3h', 'khoiluongkgh', 'khoiluonglbsh',
    'hesovattulieu', 'gocnghieng', 'hesodienfull',
    'duongkinhcanh', 'buoccanh', 'duongkinhtruc', 'tocdo'
    ]

    for field in fields:
        value = request.form.get(field)
        if value:
            session[field] = value
    
    return redirect(url_for('show_tab5'))

@app.route('/trough/tab5')
def show_tab5():
    if not session.get('tytrong'):
        flash("⚠️ Vui lòng nhập dữ liệu vật liệu trước khi tiếp tục.")
        return redirect(url_for('tab1'))
    mpas = [
        {"name": "Thép cacbon", "modulus_mpa": 200, "density": 7.85},
        {"name": "Inox 304/316", "modulus_mpa": 200, "density": 7.93},
        {"name": "Gang", "modulus_mpa": 150, "density": 7.20},
        {"name": "Nhôm", "modulus_mpa": 69, "density": 2.70},
        {"name": "Đồng", "modulus_mpa": 120, "density": 8.96},
    ]
    with open('data02.json', 'r', encoding='utf-8') as f:
        materials = json.load(f)
    # cần bước cánh, đường kính cánh, đường kính trục, tên vật liệu
    return render_template('./trough/tab5.html', data={
        'duongkinhcanh': session.get('duongkinhcanh'),
        'buoccanh': session.get('buoccanh'),
        'duongkinhtruc': session.get('duongkinhtruc'),
        'tytrong': session.get('tytrong'),
        'hesodienday': session.get('hesodienday'),
        'tenvatlieu': session.get('tenvatlieu')
    }, mpas=mpas, materials=materials) 
    
 
if __name__ == '__main__':
    app.run(debug=True)
