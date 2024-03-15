from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+mysqlconnector://root:root@localhost:3306/Project'
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

#get all project that's available in the database
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
    ), 404;


#get project details from user_id
#@app.route('/<user_id>')
#def get_projects(user_id):
    #pass


@app.route("/PostProject/<string:proj_name>", methods=['POST'])
def PostProject(proj_name):
    if(db.session.scalars(
        db.select(Project).filter_by(proj_name = proj_name).
        limit(1)
    ).first()
    ):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "proj_name": proj_name
                },
                "message": "Project already exists."
            }
        ),400
        data = request.get_json()
        project= (proj_name, **data)

        try:
            db.session.add(project)
            db.session.commit()
        except:
            return jsonify(
                {
                    "code":500,
                    "data": {
                        "proj_name":proj_name
                    }
                     "message": "An error has occured when trying to create the new project."
                }
            ), 500

            return jsonify(
                {
                    "code": 201,
                    "data": project.json()
                }
            ),201
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)