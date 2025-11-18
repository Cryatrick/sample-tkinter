from database import db_conn

class Session :
	user_id = ""
	user_name = ""


	def login_user(self, user_id, user_password) :
		sql = f"SELECT usr_id, usr_name FROM user WHERE usr_username = '{user_id}' AND usr_password = '{user_password}'"

		db_data = db_conn.fetch_data(sql)
		print(db_data)

		if len(db_data) > 0 :
			self.user_id = db_data[0][0]
			self.user_name = db_data[0][1]
			return True
		else :
			return False

	def logout(self) :
		self.user_id = ""
		self.user_name = ""