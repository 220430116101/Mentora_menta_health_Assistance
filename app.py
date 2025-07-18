from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key="AIzaSyAPQQkiQY_hsIgNSywfGILHBx6QO_eUD5Q")
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    try:
        response = model.generate_content([
            "You are a helpful and compassionate mental wellness assistant.",
            "⚠️ Only answer questions related to: mental health, stress, anxiety, motivation, or emotional support.",
            "❌ If a user asks anything unrelated, politely redirect them back to mental wellness topics.",
            "✅ Respond like a smart, friendly assistant with a warm and caring tone.",
            "✅ Use emojis where helpful (like 😊, 💡, 🧠, ❤️).",
            "📌 Strict formatting rules (MANDATORY):\n"
            "- Use bullet points that start with '•'.\n"
            "- Each bullet must be on a **new line**.\n"
            "- Leave **Half blank line** between each bullet.\n"
            "- NEVER merge bullet points in the same paragraph.\n"
            "- DO NOT start with any paragraph or summary.\n"
            "- ONLY output well-formatted bullet points.",
            """✅ Example format (copy this style):

• Try deep breathing exercises to relax your body and mind. 🧘

• Talk to a supportive friend or therapist to release feelings. ❤️

• Focus on getting quality sleep and eating healthy meals. 💤

• Take small breaks during the day to avoid burnout. 💡
            """,
            f"🧠 User's message: {user_message}"
        ])
        reply = response.text
    except Exception as e:
        reply = f"❌ Error: {str(e)}"
    return jsonify({"reply": reply})
    # return jsonify({"reply": f"Mentora: {reply}"})

if __name__ == "__main__":
    app.run(debug=True)



