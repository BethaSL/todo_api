from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [
    {
        "done": true,
        "label": "Sample Todo 1"
    },
    {
        "done": true,
        "label": "Sample Todo 2"
    }
]

@app.route('/todos', methods=['GET', 'POST'])
def handdle_todos():
    request = ()

    if request == 'GET':
        json_text = jsonify(todos)
        return json_text
    else: 
        request_body = {
        "done": true,
        "label": "Sample Todo 1"
        }
        request_body = request.json
        decoded_object = json.loads(request_body)
        todos.append(decoded_object)
        print("Incoming request with the following body", request_body)
        return jsonify(todos), 200


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)