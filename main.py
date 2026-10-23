from flask import Flask, render_template_string
import config
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ hotel }} - Book Room</title>
<style>
body{font-family:sans-serif;margin:0;background:#f2f2f2}
.header{background:{{ color }};color:white;padding:25px;text-align:center}
.container{max-width:600px;margin:15px auto;padding:10px}
.card{background:white;border-radius:14px;padding:15px;margin-bottom:15px;box-shadow:0 2px 10px rgba(0,0,0,.08)}
input,select,button{width:100%;padding:13px;margin:7px 0;border-radius:10px;border:1px solid #ccc;font-size:15px;box-sizing:border-box}
button{background:{{ color }};color:white;border:none;font-weight:bold;cursor:pointer}
.room-price{font-weight:bold;color:{{ color }};font-size:18px}
</style>
</head>
<body>
<div class="header"><h2>{{ hotel }}</h2><small>{{ address }}</small></div>
<div class="container">
  <div class="card">
    <h3>Check Availability</h3>
    <label>Check-In</label><input type="date" id="checkin">
    <label>Check-Out</label><input type="date" id="checkout">
    <label>Guests</label><select id="guests"><option>1 Guest</option><option>2 Guests</option><option>3 Guests</option></select>
  </div>
  {% for name, room in rooms.items() %}
  <div class="card">
    <h3>{{ name }}</h3>
    <p>{{ room.desc }}</p>
    <p class="room-price">₦{{ "{:,}".format(room.price) }} / night</p>
    <input id="name-{{ loop.index }}" placeholder="Your Full Name">
    <button onclick="book('{{ name }}', {{ room.price }}, {{ loop.index }})">Reserve {{ name }}</button>
  </div>
  {% endfor %}
</div>
<script>
function book(roomName, price, idx){
  let checkin = document.getElementById('checkin').value;
  let checkout = document.getElementById('checkout').value;
  let guests = document.getElementById('guests').value;
  let name = document.getElementById('name-'+idx).value;
  if(!checkin || !checkout || !name){alert("Fill Check-in, Check-out and Name"); return;}
  let msg = `Hello {{ hotel }}!%0AI want to reserve:%0AName: ${name}%0ARoom: ${roomName}%0ACheck-in: ${checkin}%0ACheck-out: ${checkout}%0AGuests: ${guests}%0APrice: ₦${price}/night%0A%0APlease confirm availability.`;
  window.open(`https://wa.me/{{ phone }}?text=${msg}`, '_blank');
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, hotel=config.HOTEL_NAME, address=config.HOTEL_ADDRESS, color=config.COLOR, phone=config.PHONE, rooms=config.ROOMS)

if __name__ == "__main__":
    app.run()