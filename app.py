from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'Data analyst',
  'location': 'Bengaluru,India',
  'salary': 'Rs.100,000',
}, {
  'id': 2,
  'title': 'Data scientist',
  'location': 'Delhi,India',
  'salary': 'Rs.150,000',
}, {
  'id': 3,
  'title': 'Front-end Engineer',
  'location': 'Remote',
  'salary': 'Rs.200,000',
}, {
  'id': 3,
  'title': 'Back-end Engineer',
  'location': 'San Francisco,USA',
  'salary': '$200,000',
}]


@app.route('/')
def helloworld():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


app.run(host='0.0.0.0', debug='True')
