import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

@run_once
def intialize_db_pool()
	connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="db_pool",
																  pool_size=10,
																  pool_reset_session=True,
																  host='localhost',
																  database='casaone_primary',
																  user='dbadmin',
																  password='dbadmin@123')
																  
	backup_connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="db_pool",
																  pool_size=5,
																  pool_reset_session=True,
																  host='localhost',
																  database='casaone_backup'
																  user='dbadmin',
																  password='dbadmin@123')
																  
def get_primary_con_obj():
	return db_connection_obj = mysql.connector.connect(host='localhost',user='scott', database='casaone_primary',password='dbadmin@123')
					 
def get_backup_con_obj():
	return db_connection_obj = mysql.connector.connect(host='localhost',user='scott', database='casaone_backup',password='dbadmin@123')
				
																  
																  
def get_top_products_rating():
	try:
		intialize_db_pool()
		try:
			db_connection_obj = connection_pool.get_connection() #get a connection from primary batabase pool
		except errors.PoolError as e:
			print (e)
			print("Using adding connection on primary database")
			db_connection_obj = get_primary_con_obj() #use new connection
			
		has_connection = True
		if not db_connection_obj.is_connected():
			db_connection_obj.close()
			has_connection = False
			try:
				db_connection_obj = backup_connection_pool.get_connection() #get a connection from backup batabase pool
			except errors.PoolError as e:
				print (e)
				print("Using adding connection on backup database")
				db_connection_obj = get_backup_con_obj() #use new connection
			if db_connection_obj.is_connected():
				has_connection = True
			
		if has_connection:
			cursor = connection_object.cursor()
			#get top ten products and its rating
			cursor.execute("SELECT A.AVERAGE_PRODUCT_RATING AS AVERAGE_PRODUCT_RATING,B.PRODUCT_NAME AS PRODUCT_NAME,B.PRODUCT_INFO AS"
				"PRODUCT_INFO FROM PRODUCT_AGGREGATE A,PRODUCT_DETAILS B WHERE A.PRODUCT_ID=B.PRODUCT_ID AND ROWNUM <= 10  ORDER BY "
				"A.AVERAGE_PRODUCT_RATING DESC;")
			results = cursor.fetchall()
			return results
		else:
			print("Both Primary and backup dbs are down")
			return []
		
		#return the connection to pool
		db_connection_obj.close()
	except errors.Error as e:
		print (e)
		return []