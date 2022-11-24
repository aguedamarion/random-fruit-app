# author: @noahgift
# modifications: @aguedamarion

from flask import Flask
from flask import render_template
from random import choices

app = Flask(__name__)


def random_fruit():
    """Returns random fruit"""

    fruits = ["Abiu", "Açaí", "Acerola"", ""Akebi", "Ackee", "African Cherry Orange", "American Mayapple", "Apple", "Apricot", "Araza",
              "Avocado", "Banana", "Bilberry", "Blackberry", "Blackcurrant", "Black sapote", "Blueberry", "Boysenberry", "Breadfruit", 
              "Buddha's hand", "Cactus pear", "Canistel", "Cashew", "Cempedak", "Cherimoya", "Cherry", 
              "Chico fruit", "Cloudberry", "Coco De Mer", "Coconut", "Crab apple", "Cranberry", "Currant", "Damson", "Date", "Dragonfruit",
              "Durian", "Egg Fruit", "Lulo", "Lychee", "Magellan Barberry", "Mamey Apple", "Mamey Sapote", "Mango", "Mangosteen", "Marionberry",
              "Melon", "Cantaloupe", "Galia melon", "Honeydew", "Mouse melon", "Musk melon", "Watermelon", "Miracle fruit", "Momordica fruit",
              "Monstera deliciosa", "Mulberry", "Nance", "Nectarine", "Orange", "Blood orange", "Clementine", "Mandarine", "Tangerine", "Papaya",
              "Passionfruit", "Pawpaw", "Peach", "Pear", "Persimmon", "Plantain", "Plum", "Prune", "Pineapple", "Pineberry", "Plumcot",
              "Pomegranate", "Pomelo", "Purple mangosteen", "Quince", "Raspberry", "Salmonberry", "Rambutan", "Redcurrant",
              "Rose apple", "Salal berry", "Salak", "Sapodilla", "Sapote", "Satsuma", "Shine Muscat or Vitis Vinifera", "Sloe or Hawthorn Berry",
              "Soursop", "Star apple", "Star fruit", "Strawberry", "Surinam cherry", "Tamarillo", "Tamarind", "Tangelo", "Tayberry", "Ugli fruit",
              "White currant", "White sapote", "Ximenia", "Yuzu" ]
    return choices(fruits)


@app.route("/")
def fruit():
    """Return random fruit"""

    my_fruit = random_fruit()
    return render_template("index.html", title="Random Fruit", fruit=my_fruit)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
