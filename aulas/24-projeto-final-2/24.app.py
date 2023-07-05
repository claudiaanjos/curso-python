import psycopg2
from flask import Flask, request


app = Flask(__name__)


@app.route('/consulta', methods=['GET'])
def cotacaocompleta():
  argumentos = request.args
  origem = argumentos.get('origem')
  hora = str(argumentos.get('hora'))
  ret = []
  con = psycopg2.connect(host='database-1.cuf8rlopzxtf.us-east-1.rds.amazonaws.com', database='Rotas',
                       user='postgres', password='12345678')
  con.autocommit = True
  cur = con.cursor()
  cur.execute("select * from horarios where origem = '" + origem  + "' and hora='" + hora + "'" )
  recset = cur.fetchall()
  for rec in recset:
    #print(rec)
    ret.append(str(rec))
  con.close()

  return ret


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5005)
	