import sqlite3

def get_db(t):
	conn=sqlite3.connect("person.db")
	a=conn.execute("SELECT * from status")
	db=[]
	for i in a:
		for j in i:
			db.append(str(j))
	conn.close()
	if (t=='name'):
		return db[0]
	if (t=='phone'):
		return db[1]
	if (t=='email'):
		return db[2]
	if (t=='all'):
		return db
	else:
		return db[t+2]

def change_db(pos,value):
	conn=sqlite3.connect("person.db")
	if (pos=='name'):
		conn.execute("UPDATE status set name= ?",(value,))
	elif (pos=='phone'):
		conn.execute("UPDATE status set phone= ?",(value,))
	elif (pos=='email'):
		conn.execute("UPDATE status set email= ?",(value,))
	else:
		conn.execute("UPDATE status set t"+str(pos)+"=?",(value,))
	conn.commit()
	conn.close()

def change_all_db(name,phone,email,t1,t2,t3,t4,t5,t6,t7,t8):
	if (1==1):
		conn1 = sqlite3.connect('person.db')
		conn1.execute("UPDATE status set name = ?",(name,))
		conn1.execute("UPDATE status set phone = ?",(phone,))
		conn1.execute("UPDATE status set email = ?",(email,))
		conn1.execute("UPDATE status set t1 = ?",(t1,))
		conn1.execute("UPDATE status set t2 = ?",(t2,))
		conn1.execute("UPDATE status set t3 = ?",(t3,))
		conn1.execute("UPDATE status set t4 = ?",(t4,))
		conn1.execute("UPDATE status set t5 = ?",(t5,))
		conn1.execute("UPDATE status set t6 = ?",(t6,))
		conn1.execute("UPDATE status set t7 = ?",(t7,))
		conn1.execute("UPDATE status set t8 = ?",(t8,))
		conn1.commit()
		conn1.close()
def get_status():
	conn1 = sqlite3.connect('status.db')
	cursor = conn1.execute("SELECT current from status")
	for row in cursor:
		state=int(row[0])
	conn1.close()
	return state

def change_status(no):
	conn = sqlite3.connect('status.db')
	conn.execute("UPDATE status set current = ? ",(no,))
	conn.commit()
	conn.close()
#change_db(3,'0')
print(get_db('all'))