from cnes import download
from flask import Flask, make_response
import numpy as np

app = Flask(__name__)

@app.route("/download/<tipo>/<uf>/<ano>/<mes>")
def cnes_download(tipo: str, uf: str, ano: int, mes: int):
    df = download(tipo, uf, ano, mes)
    response = make_response(df.to_csv())
    response.headers["Content-Disposition"] = "attachment; filename={}{}{}{}.csv".format(tipo, uf, ano, mes)
    response.headers["Content-type"] = "text/csv"

    return response


