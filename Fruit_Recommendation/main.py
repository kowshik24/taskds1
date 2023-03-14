import openai
from flask import Flask, request, jsonify
import json
# Initialize OpenAI API key
openai.api_key = "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"


# Define the function to generate recommendations
def generate_recommendations(party, flavor, texture, price):
    allowed_fruits = ['oranges', 'apples', 'pears', 'grapes', 'watermelon', 'lemon', 'lime']
    if party == 'yes':
        allowed_fruits = list(set(allowed_fruits) & set(['apples', 'pears', 'grapes', 'watermelon']))
    if flavor == 'cider':
        allowed_fruits = list(set(allowed_fruits) & set(['apples', 'oranges', 'lemon', 'lime']))
    elif flavor == 'sweet':
        allowed_fruits = list(set(allowed_fruits) & set(['watermelon', 'oranges']))
    elif flavor == 'waterlike':
        allowed_fruits = list(set(allowed_fruits) & set(['watermelon']))
    if texture == 'smooth':
        allowed_fruits.remove('pears')
    elif texture == 'slimy':
        allowed_fruits = list(set(allowed_fruits) - set(['watermelon', 'lime', 'grapes']))
    elif texture == 'waterlike':
        allowed_fruits.remove('watermelon')
    if price < 3:
        allowed_fruits = list(set(allowed_fruits) - set(['lime', 'watermelon']))
    elif price > 4 and price < 7:
        allowed_fruits = list(set(allowed_fruits) - set(['apples', 'pears']))
    return allowed_fruits

# Define Flask app and API route

app = Flask(__name__)
@app.route('/recommend', methods=['POST'])

def get_recommendations():
    #data = request.get_json()


    # Opening JSON file
    f = open('scratch.json')
    data = json.load(f)
    party = data['party_on_weekends']
    flavor = data['preferred_flavors']
    texture = data['disliked_texture']
    price = data['price_range']
    recommendations = generate_recommendations(party, flavor, texture, price)
    return recommendations

if __name__ == '__main__':
    app.run(debug=True)