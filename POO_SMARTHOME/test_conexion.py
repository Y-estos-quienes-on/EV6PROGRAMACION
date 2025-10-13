import sys
sys.path.insert(0, '.')

from conn.conn_db import DBConnection

print("=" * 50)
print("PROBANDO CONEXIÓN A MYSQL")
print("=" * 50)

try:
    print("\n1. Conectando a MySQL...")
    conn = DBConnection()
    cursor = conn.__enter__()
    print("Conexión exitosa!")
    
    print("\n2. Consultando tabla Usuario...")
    cursor.execute("SELECT COUNT(*) as total FROM Usuario")
    resultado = cursor.fetchone()
    if resultado:
        print(f"Usuarios en BD: {resultado[0]}")
    
    print("\n3. Consultando tabla Dispositivo...")
    cursor.execute("SELECT COUNT(*) as total FROM Dispositivo")
    resultado = cursor.fetchone()
    if resultado:
        print(f"Dispositivos en BD: {resultado[0]}")
    
    print("\n4. Listando 3 usuarios...")
    cursor.execute("SELECT usuario, email FROM Usuario LIMIT 3")
    usuarios = cursor.fetchall()
    for user in usuarios:
        print(f"   - {user[0]}: {user[1]}")
    
    conn.__exit__(None, None, None)
    
    print("\n" + "=" * 50)
    print("TODO FUNCIONA CORRECTAMENTE")
    print("=" * 50)

except Exception as e:
    print(f"\n ERROR: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
