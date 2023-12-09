import pymysql

class DAOEmpleado:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="db_poo" )

    def read(self, cod_emp):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            if cod_emp == None:
                cursor.execute("SELECT * FROM empleado order by nombre asc")
            else:
                cursor.execute("SELECT * FROM empleado where cod_emp = %s order by nombre asc", (cod_emp,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO empleado(nombre,telefono,email,fecha_emp,puesto,salario) VALUES(%s, %s, %s, %s, %s, %s)", (data['nombre'],data['telefono'],data['email'],data['fecha_emp'],data['puesto'],data['salario'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, cod_emp, data):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE empleado set nombre = %s, telefono = %s, email = %s, fecha_emp=%s, puesto=%s, salario=%s where cod_emp = %s", (data['nombre'],data['telefono'],data['email'],data['fecha_emp'],data['puesto'],data['salario'],cod_emp,))
            con.commit()
            return True
        except:
            con.rollback()
            return False

        finally:
            con.close()

    def delete(self, cod_emp):
        con = DAOEmpleado.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM empleado where cod_emp = %s", (cod_emp,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
