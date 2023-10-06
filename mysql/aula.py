import mysql.connector

conexao = mysql.connector.connect(
host="localhost",
user="root",
password="jota#1970",
database="fabin_db"
)

cursor = conexao.cursor()

dsFrase = "Persista"
autorFrase = "professor"
blActive ="S"


comando = f'SELECT * FROM tabFrase'
cursor.execute(comando)

#conexao.commit() #editar

resultado = cursor.fetchall() #ler
print(resultado)

# INSERT
# comando = f'INSERT INTO tabFrase (dsFrase,autorFrase,blActive) VALUES("{dsFrase}","{autorFrase}","{blActive}")'

cursor.close()
conexao.close()

