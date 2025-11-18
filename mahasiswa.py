from database import db_conn
import datetime

class Mahasiswa : 
	def __init__(self, npm_mahasiswa, nama_mahasiswa, id_prodi, nama_prodi) :
		self.npm_mahasiswa = npm_mahasiswa
		self.nama_mahasiswa = nama_mahasiswa
		self.id_prodi = id_prodi
		self.nama_prodi = nama_prodi

	def insert_mahasiswa(self) :
		sql = f"INSERT INTO mahasiswa VALUES(%s,%s,%s)"
		data = (self.npm_mahasiswa, self.nama_mahasiswa, self.id_prodi)

		insert_result = db_conn.execute_sql(sql, data)

		if insert_result > 0 :
			return True

		return False

	def update_mahasiswa(self) :
		sql = f"UPDATE mahasiswa SET nama_mahasiswa = %s, prodi_mahasiswa = %s WHERE npm_mahasiswa IN (%s)"
		data = (self.nama_mahasiswa, self.id_prodi, self.npm_mahasiswa)

		update_result = db_conn.execute_sql(sql, data)

		if update_result > 0 :
			return True

		return False

	def delete_mahasiswa(self) :
		sql = f"DELETE mahasiswa WHERE npm_mahasiswa IN (%s)"
		data = (self.npm_mahasiswa)

		delete_result = db_conn.execute_sql(sql, data)

		if delete_result > 0 :
			return True

		return False

	def generate_npm(self) :
		year_code = datetime.now().strftime("%y")
		npm_code = year_code+self.id_prodi
		sql = f"SELECT RIGHT(mhs_npm,3) as npmbaru FROM mahasiswa WHERE mhs_npm LIKE '{npm_code}%'"
		db_data = db_conn.fetch_data(sql)
		print(db_data)
		current_npm = "001"
		if len(db_data) > 0 :
			result_num = db_data[0][0]
			current_npm = f"{result_num:03d}"

		generated_npm = npm_code + current_npm

		self.npm_mahasiswa = generated_npm

def get_all_mahasiswa() :
	sql = "SELECT npm_mahasiswa,nama_mahasiswa,prodi_mahasiswa,nama_prodi FROM mahasiswa JOIN program_studi ON program_studi.id_prodi = mahasiswa.prodi_mahasiswa"
	db_data = db_conn.fetch_data(sql)
	mahasiswa_data = []

	if len(db_data) > 0 :
		for row_data in db_data:
			mahasiswa = Mahasiswa(row_data[0],row_data[1],row_data[2],row_data[3])
			mahasiswa_data.append(mahasiswa)

	return mahasiswa_data
