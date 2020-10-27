from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    print(msg)

    # Create reply
    resp = MessagingResponse()
    if msg == "hello":
    	resp.message('world')
    else:
    	resp.message('pragya')
   

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)







import sqlite3

conn = sqlite3.connect('whatsappbot.db')
#CREATE A CURSOR
c = conn.cursor()

#create a table 
c.execute("""CREATE TABLE whatsapp_mybot (
       first_name TEXT ,
       order_name TEXT,
       num INTEGER,
       price INTEGER)
	""")


if msg == "//help//":
	resp.message("HELLO ----> WHAT HELP U WANT ...  \n 1.ABOUT REGISTRATION \n  2. ABOUT MENU   \n 3. PAYMENT ISSUE")


if msg == "order":

	resp.message("('DABELI'--> 10rs) \n  ('wadapav'--> 10rs) \n ('pattis'--> 15rs)")

elif msg == "payment issue":
	resp.message("RECORDED IN ANOTHER..")

elif msg == "no help//":
	print("no help requires")
	
## if already registered


	
else:
	break



n = c.execute("SELECT first_name FROM whatsapp_bot WHERE num = '"+user_num+"'")
for i in n:
   n = i[0]

   print("OOPS!! U R ALREADY REGISTERED")

#for adding the user in the table
c.execute('''INSERT INTO whatsapp_bot(first_name,order_name,num,price) VALUES(?,?,'n',0)'''( , ,user_num,))
cur.execute('INSERT INTO whatsapp_bot (num) VALUES (?)',(user_num,))
print("U R SUCCESSFULLY REGISTERED")



try:
    msg == "add_user":
	resp.message("HELLO ...... ENTER UR name {} and order {} and ur phone num {}.".format(first_name,order_name,num,price))

try:
	c.execute("SELECT order_name FROM price")
	order_name = c.fetchall()
	for i in order_name:
		item = i[0]
		c.execute('UPDATE menu SET'+item+"=0 WHERE num = '"+user_num+"'")
		conn.commit()

except:
	pass

	





conn.commit()

conn.close()