from flask import Flask
from flask_restful import Resource, Api

app= Flask(__name__)
api= Api(app)


frutas=[[{
  "genus": "Ananas",
  "name": "Abacaxi",
  "id": 1,
  "family": "Bromeliaces",
  "order": "Poales",
  "nutritions": {
      "carbohydrates": 12,
      "protein": 0,
      "fat": 0,
      "calories": 49,
      "sugar": 9.26
  }
}],
[{
  "genus": "Malpighia",
  "name": "Acerola",
  "id": 2,
  "family": "Malpighiaceae",
  "order": "Malpighiales",
  "nutritions": {
      "carbohydrates": 7.69,
      "protein": 0.4,
      "fat": 0.3,
      "calories": 32,
      "sugar": 0
  }
}],
[{
  "genus": "Prunus",
  "name": "Ameixa",
  "id": 3,
  "family": "Rosaceae",
  "order": "Rosales",
  "nutritions": {
      "carbohydrates": 11.42,
      "protein": 0.7,
      "fat": 0.30,
      "calories": 46,
      "sugar": 9.92
  }
}],
[{
  "genus": "Musa",
  "name": "Banana",
  "id": 4,
  "family": "Musaceae",
  "order": "Zingiberales",
  "nutritions": {
      "carbohydrates": 22.84,
      "protein": 1.09,
      "fat": 0.33,
      "calories": 89,
      "sugar": 12.23
  }
}],
[{
  "genus": "Anacardium",
  "name": "Caju",
  "id": 5,
  "family": "Anacardiaceae",
  "order": "Sapindales",
  "nutritions": {
      "carbohydrates": 11.41,
      "protein": 0.21,
      "fat": 0.14,
      "calories": 43,
      "sugar": 8.59
  }
}],
[{
  "genus": "Prunus",
  "name": "Damascos",
  "id": 6,
  "family": "Rosaceae",
  "order": "Rosales",
  "nutritions": {
      "carbohydrates": 11.12,
      "protein": 1.4,
      "fat": 0.39,
      "calories": 48,
      "sugar": 9.24
  }
}]
]

class Frutas(Resource):
    def get(self):
        return frutas


api.add_resource(Frutas, '/frutas')       

if __name__ == '__main__':
    app.run(debug=True)
