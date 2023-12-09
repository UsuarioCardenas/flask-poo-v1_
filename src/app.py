from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOUsuario import DAOUsuario
from dao.DAOEmpleado import DAOEmpleado
 

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = DAOUsuario()
dao_empleado = DAOEmpleado()
ruta='/usuario'

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route(ruta+'/')
# @app.route('/usuario/')
def index():
    data = db.read(None)

    return render_template('usuario/index.html', data = data)

@app.route(ruta+'/add/')
def add():
    return render_template('/usuario/add.html')

@app.route(ruta+'/addusuario', methods = ['POST', 'GET'])
def addusuario():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Nuevo usuario creado")
        else:
            flash("ERROR, al crear usuario")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.route(ruta+'/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('usuario/update.html', data = data)


@app.route(ruta+'/updateusuario', methods = ['POST'])
def updateusuario():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route(ruta+'/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('usuario/delete.html', data = data)

@app.route(ruta+'/deleteusuario', methods = ['POST'])
def deleteusuario():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('Usuario eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')


#empleados
@app.route('/empleados/')
# @app.route('/usuario/')
def empleados():
    data = dao_empleado.read(None)
    return render_template('empleado/index_emp.html', data=data)


@app.route('/empleados/'+'add/')
def addempleados():
    return render_template('empleado/add_emp.html')


@app.route('/empleados'+'/addempleado', methods = ['POST', 'GET'])
def addempleado():
    if request.method == 'POST' and request.form['save']:
        if dao_empleado.insert(request.form):
            flash("Nuevo empleado agregado")
        else:
            flash("ERROR, al agregar empleado")

        return redirect(url_for('empleados'))
    else:
        return redirect(url_for('empleados'))


@app.route('/empleados'+'/update/<int:cod_emp>/')
def update2(cod_emp):
    data = dao_empleado.read(cod_emp);

    if len(data) == 0:
        return redirect(url_for('empleados'))
    else:
        session['update'] = cod_emp
        return render_template('empleado/update_emp.html', data = data)



@app.route('/empleados'+'/updateempleados', methods = ['POST'])
def updateempleado():
    if request.method == 'POST' and request.form['update']:

        if dao_empleado.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('empleados'))
    else:
        return redirect(url_for('empleados'))


@app.route('/empleados'+'/delete/<int:cod_emp>/')
def borrar(cod_emp):
    data = dao_empleado.read(cod_emp);

    if len(data) == 0:
        return redirect(url_for('empleados'))
    else:
        session['delete'] = cod_emp
        return render_template('empleado/delete_emp.html', data = data)



@app.route('/empleados'+'/deleteempleados', methods = ['POST'])
def borrarempleado():
    if request.method == 'POST' and request.form['delete']:

        if dao_empleado.delete(session['delete']):
            flash('Empleado eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('empleados'))
    else:
        return redirect(url_for('empleados'))







if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)

#empleados

