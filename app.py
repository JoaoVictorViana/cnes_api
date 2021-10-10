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

@app.route("/<tipo>/<uf>/<ano>/<mes>")
def hello_world(tipo: str, uf: str, ano: int, mes: int):
    data_dict = []
    df = download(tipo, uf, ano, mes)

    for row in range(len(df)):
        row_dict = dict()
        
        for col_index in range(len(df.columns)):
            row_dict[df.columns[col_index]] = df.iloc[row,col_index]
        
        data_dict.append(row_dict)

    response = app.response_class(
        response=json.dumps(data_dict, cls=NpEncoder),
        status=200,
        mimetype='application/json'
    )

    return response


