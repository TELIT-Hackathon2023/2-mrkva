from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = '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'

# Replace 'your-custom-model-name' with the identifier of your custom model
custom_model_name = 'DanielChat'

@app.route('/chat', methods=['POST'])
def chat_with_custom_gpt():
    data = request.json
    user_input = data.get('message', '')

    try:
        # Send the user input to your custom chat model
        response = openai.ChatCompletion.create(
            model=custom_model_name,
            messages=[{"role": "user", "content": user_input}]
        )
        # Extract the response text
        gpt_response = response['choices'][0]['message']['content']
    except Exception as e:
        gpt_response = f"An error occurred: {str(e)}"

    return jsonify({"response": gpt_response})

if __name__ == '__main__':
    app.run(debug=True)