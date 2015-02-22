# python-websockets-talk
Talk inspired and based on makaimc/python-websockets-example

## Building and running the code

### Using Fig and Docker

```sh
fig build
fig up
```
The site should be served at http://localhost:8888/

### Alternatives

```sh
sudo apt-get install redis python3 python-virtualenv
virtualenv demoenv -p python3
source demoenv/bin/activate
pip install -r requirements.txt
```
You will also need to set the database connection to localhost.

```sh
python app.py
```

The site should be served at http://localhost:8888/
