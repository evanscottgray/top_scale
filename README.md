# top scale
because you need a USB scale in your python life.

this is meant to work with MyWeigh Ultraship U2 USB scales.

#### up and running
- have python
- have pip / virtualenv
- have a ULTRASHIP U-2 scale thing (note: it must be the v2 version)

in repo directory
```
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
python scale_serve.py
```


#### GET SOME READINGS YO
```
# using your favorite http client.
# fetch the latest reading from the scale
GET /reading, Content-Type: application/json
# fetch the last 10 readings from the scale
GET /readings, Content-Type: application/json
```

#### NOTE
To send readings over serial from the scale, you have to press the send button.   
:(



