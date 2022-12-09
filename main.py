from flask import Flask, render_template

app=Flask(__name__)

JOBS= [
  {
    'id': 1,
    'title': 'Data Analyst',
    'Location': 'Delhi, India',
    'Salary': 'Rs. 150,000'
  },
  
  {
    'id': 2,
    'title': 'Backend Engineer',
    'Location': 'Delhi, India',
    'Salary': 'Rs. 180,000'
  }
  
]
@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs=JOBS)

if __name__=='__main__':
  app.run(host='0.0.0.0' , debug=True)
