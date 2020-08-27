from flask import Flask, render_template,request,redirect
from flask_mysqldb import MySQL
app=Flask(__name__)
 
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "spor_salonu"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# Mysql Kullanıcı Ekleme
@app.route('/kullaniciekle')
def kullaniciekle():
   return render_template("kayit.html")

# Mysql Kullanıcı Ekleme
@app.route('/kullanicieklesonuc', methods=['POST'])
def kullanicieklesonuc():
   if request.method == 'POST':
      ad = request.form.get('ad')
      soyad = request.form.get('soyad')
      yas = int(request.form.get('yas'))
      cinsiyet = request.form.get('cinsiyet')
      sure = request.form.get('sure')
      fiyat = int(request.form.get('fiyat'))
      kayit_tarihi = request.form.get('kayit_tarihi')
      boy = float(request.form.get('boy'))
      kilo = float(request.form.get('kilo'))

      cursor = mysql.connection.cursor()

      sorgu = "INSERT INTO musteriler VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

      cursor.execute(sorgu,(None,ad,soyad,yas,cinsiyet,sure,fiyat,kayit_tarihi,boy,kilo))
      mysql.connection.commit()
      cursor.close()


      return render_template("kullanicieklesonuc.html",ad=ad,soyad=soyad,yas=yas,cinsiyet=cinsiyet,sure=sure,fiyat=fiyat,kayit_tarihi=kayit_tarihi,boy=boy,kilo=kilo,page_title="Kayıt Ekle")

   else:
      return render_template("kullanicieklesonuc.html",hata="Formdan veri gelmedi!")


@app.route('/')
def home_page()->'html':
    return render_template('homepage.html',page_title='Spor Salonu Yönetimi Yazılımı')

@app.route('/kayit')
def kayit()->'html':
    return render_template('kayit.html',page_title='Yeni Sporcu Kaydı')

@app.route('/hesap')
def entry_page()->'html':
    return render_template('hesap.html',page_title='Vücut Kitle İndeksi Hesaplama')
 
@app.route('/account')
def account_a()->'html':
    return render_template('account.html')
 
@app.route('/kitleindeksi',methods=['POST'])
def vkihesap()->'html':
    x=int(request.form['firstValue'])
    y=int(request.form['secondValue'])
    return render_template('result.html',page_title='Hesaplama Sonucu',sum_result=(((x*x)*y)/100000),first_value=x,second_value=y,)


@app.route('/kalorihesap',methods=['POST'])
def kalorihesap()->'html':
    b=int(request.form['boyValue'])
    c=int(request.form['kiloValue'])
    d=int(request.form['yasValue'])
    a=request.form['cinsiyet']
    return render_template('result2.html',page_title='Kalori İhtiyacı Hesaplama',result=(2.4*(65.5+(9.6*c))+(1.8*b)-(4.7*d)),value1=a,value2=b,value3=c,cinsiyet=d,)



app.run(debug=True)