import cx_Oracle

oracle_client_initialized = False

def conectar():
    global oracle_client_initialized
    
    try:
        if not oracle_client_initialized:
            cx_Oracle.init_oracle_client(lib_dir="./instantclient_21_9")
            oracle_client_initialized = True
        
        dsn_tns = cx_Oracle.makedsn('xxx.xxx.xxx.xxx', 1521, service_name='WINT')
        connection = cx_Oracle.connect(user='xxxxx', password='xxxxx', dsn=dsn_tns)
        return connection
    except cx_Oracle.Error as error:
        print("Falha ao conectar ao banco de dados:", error)
