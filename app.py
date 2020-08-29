import os, io, csv, string
from flask import Flask, flash, request, render_template, url_for, redirect, session, jsonify
from werkzeug.utils import secure_filename
from efficient_apriori import apriori
from flask_session.__init__ import Session
import pandas as pd
from func_timeout import func_timeout, FunctionTimedOut

import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

#Initialize the app by adding:
UPLOAD_FOLDER = 'web_ressources'
ALLOWED_EXTENSIONS = {'csv'} #'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024
app.static_folder = 'static'

def allowed_file(filename):
  return '.' in filename and \
       filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	   
def arules(data, min_support, min_confidence):
	itemsets, rules = apriori(data, min_support=min_support,  min_confidence=min_confidence)
	return [itemsets, rules]

def process(data, min_support, min_confidence):
	try:
		doitReturnValue = func_timeout(5, arules, args=(data, min_support, min_confidence))
		return doitReturnValue
	except FunctionTimedOut:

		print ( "Could not complete within 5 seconds and was terminated.\n=")
	except Exception as e:

	# Handle any exceptions that arules might raise here
		print('bad awfully')
	return None
@app.route('/handleUpload', methods=['POST'])
def handleUpload():
  if request.method == 'POST':
    # check if the post request has the file part
    if 'file' not in request.files:
      flash('No file part')
      return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename

    if file.filename == '':
      flash('No selected file')
      return redirect(request.url)
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      data = file.read()
      file.seek(0); 
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      r = pd.read_csv(StringIO(data.decode('utf8')), sep=';')
      r = r.loc[:, r.isnull().mean() < .8]
      r.dropna(axis=0, how='all', inplace=True)
      r.fillna('nan', inplace=True)
      r = list(r.itertuples(index=False, name=None))
      r = [tuple(filter(bool, tup)) for tup in r]
      itemsets, rules = process(data = r[1:], min_support=request.form['min_support'] or 0.02,  min_confidence=request.form['min_confidence'] or 0.05)
      rules = [rule for rule in rules if 'nan' not in str(rule)]
      return (jsonify(str(sorted(rules, key=lambda rule: rule.lift))))
  return redirect(url_for('fileFrontPage', #filename=filename
                  ))	  
	  
@app.route("/")
def fileFrontPage():
  return render_template('index.html')

#sess = Session()
if __name__ == '__main__':
#  app.secret_key = 'super secret key'
#  app.config['SESSION_TYPE'] = 'filesystem'
  
#  sess.init_app(app)
  app.run(host='0.0.0.0', port=8080)
