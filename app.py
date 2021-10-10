from cnes import download
from flask import Flask, json
import numpy as np

app = Flask(__name__)

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

@app.route("/<tipo>/<uf>/<ano>/<mes>/<page>/<per_page>")
def hello_world(tipo: str, uf: str, ano: int, mes: int, page: int, per_page: int):
    per_page = int(per_page)
    page = int(page)
    data_dict = dict()

    df = download(tipo, uf, ano, mes)

    index_start = ((page - 1) * per_page)
    index_final = index_start + per_page

    data_dict['quantidade'] = len(df)
    data_dict['paginas'] = len(df) // per_page
    data_dict['resultados'] = []

    df = df.iloc[index_start:index_final,:]

    for row in range(per_page):
        row_dict = dict()
        
        for col_index in range(len(df.columns)):
            row_dict[df.columns[col_index]] = df.iloc[row,col_index]
        
        data_dict['resultados'].append(row_dict)

    response = app.response_class(
        response=json.dumps(data_dict, cls=NpEncoder, indent=4),
        status=200,
        mimetype='application/json'
    )

    return response


