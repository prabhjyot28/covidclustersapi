from flask import Flask, request
from flask_cors import CORS
from Cluster import Cluster
from Hexagon import Hexagon


clusters = {}

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello world"


@app.route('/query', methods=['GET', 'POST'])
def Query():
    if 'name' not in request.form:
        return 'Enter valid hexagon name'

    if 'cluster' not in request.form:
        return 'Enter valid cluster name'

    name = request.form['name']
    cluster = request.form['cluster']
    if not name:
        return 'Enter valid hexagon name'
    if not cluster:
        return 'Enter valid cluster name'

    return clusters[cluster].queryNeighbours(name)

@app.route('/addcluster', methods=['GET', 'POST'])
def AddCluster():
    if 'cluster' not in request.form:
        return 'Enter valid cluster name'

    if 'name' not in request.form:
        return 'Enter valid hexagon name'

    cluster = request.form['cluster']
    name = request.form['name']
    if cluster in clusters:
        return 'Cluster '+cluster+' already exists'

    h = Hexagon(name)
    c = Cluster(cluster, h)
    clusters[cluster] = c
    return 'Cluster '+cluster+' successfully added'

@app.route('/removecluster', methods=['GET', 'POST'])
def RemoveCluster():
    if 'cluster' not in request.form:
        return 'Enter valid cluster name'

    cluster = request.form['cluster']
    if cluster not in clusters:
        return 'Cluster '+cluster+' does not exists'

    c = clusters[cluster]
    del clusters[cluster]
    del c
    return 'cluster '+cluster+' successfully removed'



@app.route('/addhexagon', methods=['GET', 'POST'])
def AddHexagon():
    if 'name' not in request.form:
        return 'Enter valid name'
    if 'cluster' not in request.form:
        return "Enter calid cluster name"
    if 'neighbour' not in request.form:
        return 'Enter valid neighbour'
    if 'index' not in request.form:
        return 'Enter valid index'

    name = request.form['name']
    cluster = request.form['cluster']
    neighbour = request.form['neighbour']
    index = request.form['index']

    if (not name) or type(name)!=str:
        return 'Enter valid hexagon ame'

    if (not cluster) or type(cluster)!=str:
        return "Enter valid cluster name"

    if (not neighbour) or type(neighbour)!=str:
        return 'Enter valid neighbour'

    if (not index.isdigit()) or int(index)>5 or int(index)<0:
        return 'Enter valid index'

    if cluster not in clusters:
        return 'Cluster '+cluster+' does not exists'

    return clusters[cluster].addHexagon(name, neighbour, int(index))



@app.route('/removehexagon', methods=['GET', 'POST'])
def RemoveHexagon():
    if 'name' not in request.form:
        return 'Enter valid hexagon name'
    if 'cluster' not in request.form:
        return 'Enter valid cluster name'

    name = request.form['name']
    cluster = request.form['cluster']
    if not name:
        return 'Enter valid hexagon name'

    if not cluster:
        return 'Enter valid cluster name'

    if cluster not in clusters:
        return 'Cluster '+cluster+' does not exists'

    response = clusters[cluster].removeHexagon(name)
    if 'successfully removed' in response:
        if len(clusters[cluster].hexagons)==0:
            c = clusters[cluster]
            del clusters[cluster]
            del c
            return 'Hexagon '+name+' and Cluster '+cluster+' successfully removed'
        else:
            return response
    else:
        return response




if __name__=='__main__':
    app.run()
