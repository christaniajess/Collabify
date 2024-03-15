from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+mysqlconnector://root:root@localhost:3306'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Project(db.Model):
    __tablename__ = 'Project'

    proj_id = db.Column(db.Integer(10), primary_key = True)
    user_id = db.Column(db.Integer(10))
    proj_name = db.Column(db.String)
    proj_image = db.Column(db.String)
    proj_description = db.Column(db.String)

    def __init__(self, proj_id, user_id, proj_name, proj_image, proj_description):
        self.proj_id = proj_id
        self.user_id = user_id
        self.proj_name = proj_name
        self.proj_image = proj_image
        self.proj_description = proj_description

    def json(self):
        return {
            "proj_id": self.proj_id, "user_id": self.user_id, "proj_name": self.proj_name,
            "proj_image": self.proj_image, "proj_description": self.proj_description
        }

@app.route('/PostProject')
def get_all():
    project_list = db.session.scalars(db.select(Project)).all()
    if len(project_list):
        return jsonify(
            {
                "code" : 200,
                "data":
                    {
                        "Projects": [project.json() for project in project_list]
                    }
            }
        )
    return jsonify(
        {
            "code": 404, 
            "message": "This user has not created a project before."
    ), 404


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