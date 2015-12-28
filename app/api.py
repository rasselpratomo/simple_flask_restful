import json
import httplib

from app import app

from flask import Response
from flask_restful import Api, Resource, reqparse
from werkzeug.exceptions import BadRequest

api = Api(app)


class Greetings(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument(
            'message',
            type=str,
            required=True,
            help="Name cannot be blank!")
        super(Greetings, self).__init__()

    def get(self):
        result = dict()
        result['message'] = 'test message'

        return Response(
            json.dumps(result),
            status=httplib.OK,
            mimetype='application/json'
        )

    def post(self):
        try:
            args = self.reqparser.parse_args()
            result = dict()
            result['message'] = args.get('message')
        except Exception, e:
            raise BadRequest(description='Message should be filled!')

        return Response(
            json.dumps(result),
            status=httplib.OK,
            mimetype='application/json'
        )


api.add_resource(Greetings, '/')
