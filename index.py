
from flask import Flask, request, make_response
app = Flask(__name__)

koders = [
    {
        'name': 'charles'
    },
    {
        'name': 'rose'
    },
    {
        'name': 'rurick'
    }
]

@app.route('/')
def hello():
    return {
        'success': True,
        'message': 'APIv1'
    }

@app.route('/koders', methods=['GET'])
def get_all_koders():
    return {
        'koders': koders
    }

@app.route('/koders', methods=['POST'])
def create_koder():
    data = request.json
    koders.append({ 'name': data['name'] })
    return {
        'message': 'koder created',
        'koders': koders
    }

@app.route('/koders/<name>', methods=['DELETE'])
def delete_koder(name):
    # filtered_koders = list(filter(
    #     lambda koder:koder['name'] != name,
    #     koders
    # ))
    if ({ 'name': name } in koders):
        koders.remove({ 'name': name })
    else: 
        return make_response(
            {  
                'message': f'{name} not found'
            },
            404
        )
        
    return {
        'koders': koders
    }