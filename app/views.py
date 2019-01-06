#  from flask import request, jsonify
from flask_restful import Resource, reqparse
from app.models import users


class User(Resource):
    def get(self, name):
        """
        Pobiera dane usera podanego w sciezce GET
        :param name: nazwa uzytkownika
        :return: dane uzytkownika w JSON
        """
        print("Get for user: {user}".format(user=name))
        for u in users:
            if name == u["name"]:
                # return jsonify(u), 200
                return u, 200
        return "User not found", 404

    def post(self, name):
        """
        Dodaje nowego Usera podanego w sciezce URL uzupelniajac dane o age i city przekazane w JSONie POSTa
        :param name: nazwa uzytkownika
        :param age: wiek w JSON POST
        :param city: miasto w JSON POST
        :return:
        """
        if reqparse.request.is_json:
            print("New user: {user} - {json}".format(user=name, json=reqparse.request.get_json()))
        else:
            return "Only JSON data allowed", 400

        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("city")
        args = parser.parse_args()

        for u in users:
            if name == u["name"]:
                return "User already exists", 400

        u = {
            "name": name,
            "age":  args["age"],
            "city": args["city"]
        }
        users.append(u)
        return u, 201

    def put(self, name):
        """
        Aktualizacja istniejacego Usera
        :param name: nazwa uzytkownika
        :param age: wiek w JSON PUT
        :param city: miasto w JSON PUT
        :return:
        """

        if reqparse.request.is_json:
            print("Change user: {user} - {json}".format(user=name, json=reqparse.request.get_json()))
        else:
            return "Only JSON data allowed", 400

        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("city")
        args = parser.parse_args()

        for u in users:
            if name == u["name"]:
                u["age"]  = args["age"]
                u["city"] = args["city"]
                return u, 200

        u = {
            "name": name,
            "age":  args["age"],
            "city": args["city"]
        }
        users.append(u)
        return u, 201

    def delete(self, name):
        """
        Usuniecie wskazanego usera
        :param name: nazwa uzytkownika
        :return:
        """
        global users
        print("Delete for user: {user}".format(user=name))
        users = [user for user in users if user["name"] != name]
        return "{} is deleted".format(name), 200
