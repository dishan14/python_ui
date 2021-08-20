from flask import Flask
from string import Template
import pandas as pd
from script1 import A
from script2 import B
from script3 import C
from script4 import D


app = Flask(__name__)

df = pd.DataFrame({"Name": ['Anurag', 'Manjeet', 'Shubham',
                            'Saurabh', 'Ujjawal'],

                   "Address": ['Patna', 'Delhi', 'Coimbatore',
                               'Greater noida', 'Patna'],

                   "ID": [15, 20000, 20145, 20146, 20147],

                   "Sell": [140000, 300000, 600000, 200000, 600000]})

result = df.to_html()

html_temp = Template(""" 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1">
    <title>Title</title>
    <style>

body {
  font-family: Arial;
  color: white;
}
.vertical-menu {
  width: 300px;
  height: 400px;
  overflow-y: auto;
}

.vertical-menu a {
  background-color: #eee;
  color: black;
  display: block;
  padding: 12px;
  text-decoration: none;
}

.vertical-menu a:hover {
  background-color: #ccc;
}

.vertical-menu a.active {
  background-color: #04AA6D;
  color: white;
}

.split {
  height: 100%;
  width: 50%;
  position: fixed;
  z-index: 1;
  top: 0;
  overflow-x: hidden;
  padding-top: 20px;
}

.left {
  left: 0;
  background-color: #001;
}

.right {
  right: 0;
  background-color: #110;
}

.centered {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}

.centered img {
  width: 150px;
  border-radius: 50%;
}
</style>

<script>
    function autoRefresh() {
        window.location = window.location.href;
    }
    setInterval('autoRefresh()', 10000);
</script>

</head>
<body>
<div class="split left" id='one'>
  <div class="centered">
    <div > ${table_name} </div>
    <h2>Table</h2>
    <p>.......</p>
  </div>
</div>

<div class="split right">
  <div class="centered">
    <div class="vertical-menu">

      <a href="/script1" target="_blank">Script 1</a>
      <a href="/script2" target="_blank">Script 2</a>
      <a href="/script3" target="_blank">Script 3</a>
      <a href="/script4" target="_blank">Script 4</a>
      <a href="/script5" target="_blank">Script 5</a>
      <a href="#">Script 6</a>
      <a href="#">Script 7</a>
      <a href="#">Script 8</a>
      <a href="#">Script 9</a>
      <a href="#">Script 10</a>
    </div>
    <h2>List of links</h2>
    <p>......</p>
  </div>
</div>
</body>
</html>



""")


@app.route('/')
def homepage():
    return html_temp.substitute(table_name=result)

@app.route('/script1')
def script1():
    a = A().printt()
    template1 = Template("""   
    <h2>${text}</h2>   
    """)
    return template1.substitute(text=a)

@app.route('/script2')
def script2():
    a = B().printt()
    template1 = Template("""   
    <h2>${text}</h2>    
    """)
    return template1.substitute(text=a)

@app.route('/script3')
def script3():
    a = C().printt()
    template1 = Template("""   
    <h2>${text}</h2>    
    """)
    return template1.substitute(text=a)

@app.route('/script4')
def script4():
    a = D().printt()
    template1 = Template("""   
    <h2>${text}</h2>    
    """)
    return template1.substitute(text=a)




if __name__ == '__main__':
    app.run(use_reloader=True)
