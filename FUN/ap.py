from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

dics = {
    "task",  "wirte Hello World program" ,"summary", "write the code using python"
    "task", "task2", "summary", "write the task 2"
    "task", "task3" ,"summary", "write the task 3"
}

task_post_agrg =reqparse.RequestParser()
task_post_agrg.add_argument("task", help='task is required',type=str, required=True)
task_post_agrg.add_argument("summary", type=str,  help='summary is required', required=True)

class Vilist(Resource):
    def get(self):
        return dics


class VISUAL(Resource):
    def get(self, Visual_id):
        return dics[Visual_id]
    
    def post(self, Visual_id ):
        args = task_post_args.parse_args()
        if Visual_id is dics:
            abort(409, "Task ID already taken")
        dics[Visual_id] = {"task": args["task"], "summary": args['summary']}
        return dics[Visual_id] 

api.add_resource(VISUAL, '/Visual/<int:visual_id>')

if __name__ == "__main__":
    app.run(debug=True)
