from flask import Flask, jsonify, request, render_template
import psycopg2
import psycopg2.extras

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/employees')
def employees():
    try:
        connection = connect_db()
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute('SELECT * FROM employee')
            records = cur.fetchall()
            employees_list = [{'id': record['id'], 'name': record['name'], 'salary': record['salary'], 'dept_id': record['dept_id']} for record in records]
        return render_template('employees.html', employees=employees_list)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if connection is not None:
            connection.close()

def connect_db():
    return psycopg2.connect(user = "postgres", password = "1234", host = "localhost", port = 5432, database = "app")

@app.route('/create_employee', methods=['POST'])
def create_employee():
    data = request.get_json()
    employee_id = data['id']
    name = data['name']
    salary = data['salary']
    dept_id = data['dept_id']
    try:
        connection = connect_db()
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            create_script = '''CREATE TABLE IF NOT EXISTS employee(
                                    id      int PRIMARY KEY,
                                    name    varchar(40) NOT NULL,
                                    salary  int,
                                    dept_id varchar(30))'''
            cur.execute(create_script)

            insert_script = '''INSERT INTO employee(id, name, salary, dept_id) 
                            VALUES (%s, %s, %s, %s)
                            ON CONFLICT (id) DO NOTHING'''
            cur.execute(insert_script, (employee_id, name, salary, dept_id))
            cur.execute('SELECT * FROM employee')
            record = cur.fetchall()
            print(record)
            connection.commit()
        return jsonify({'message': 'Employee create succesfully'}), 201

    except Exception as e:
        return jsonify({'error':str(e)}), 500

    finally:
        if connection is not None:
            connection.close()

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = '80')