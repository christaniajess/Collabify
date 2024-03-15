from flask import Flask, request, jsonify

app = Flask(__name__)

def get_all():
    pass


#get all projects
@app.route('/')
def get_all_projects():
    pass


#get project details from user_id
@app.route('/<user_id>')
def get_projects(user_id):
    pass


@app.route('/PostProject', methods=['POST'])
def PostProject():
    #checks if input format and data of the requests are JSON
    if request.is_json:
        try:
            project = request.get_json()
            print ('\nReceived a new project request in JSON:' , project)

        except Exception as e:
            #unexpected error
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_fileame)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify(
            {
                "code": 500,
                "message": "PostProject.py internal error: " + ex_str
            }) , 500
    
    #if it reached to this point -> this is not a JSON request 
    return jsonify(
        {
            "code": 400,
            "message": "Invalid JSON input: " + str(request.get_data())
        }) , 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)