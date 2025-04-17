# http://127.0.0.1:5000 LIEN DE LA PAGE WEB


from flask import Flask, render_template_string, request
from datetime import datetime

app = Flask(__name__)

def calculate_age(birthdate, option):
    today = datetime.today()
    birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
    delta = today - birth_date  # Différence entre aujourd'hui et la date de naissance

    if option == "months":
        months_lived = (today.year - birth_date.year) * 12 + (today.month - birth_date.month)
        return f"You have lived {months_lived} months."
    
    elif option == "days":
        return f"You have lived {delta.days} days."

    elif option == "seconds":
        return f"You have lived {delta.total_seconds():,.0f} seconds."

    elif option == "milliseconds":
        return f"You have lived {delta.total_seconds() * 1000:,.0f} milliseconds."

    else:
        return "Invalid option! Please choose 'months', 'days', 'seconds', or 'milliseconds'."

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        birthdate = request.form.get("birthdate")
        option = request.form.get("option")
        if birthdate:
            result = calculate_age(birthdate, option)
        else:
            result = "Please enter a valid birthdate."

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Age Calculator</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; background-image:url('https://applescoop.org/image/wallpapers/mac/adventure-time-finn-and-jake-tv-show-cartoon-network-top-best-free-download-wallpapers-for-macbook-pro-air-and-microsoft-windows-pcs-desktop-4k-07-12-2024-1733638078-hd-wallpaper.jpeg');background-image:cover; margin: 20px; }
            .container { max-width: 600px; margin: auto; padding: 20px; background:	#ffb3d9; border-radius: 10px;
                        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); margin-top :150px ;}
            h2 { color: #333; font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;}
            label { display: block; margin-top: 10px;  font-weight: bold;; color:white}
            input, select, button { width: 100%; padding: 8px; margin-top: 5px; border: 1px solid #ccc; border-radius: 5px; }
            button { margin-top: 15px; background-color:rgb(174, 125, 174); color: white; border: none; cursor: pointer; }
            button:hover { background-color:rgba(166, 102, 166, 0.94); }
            .result { margin-top: 20px; color:rgb(141, 121, 172); font-size: 18px; font-weight: bold; }
        </style>
    </head>
    <body>

        <div class="container">
            <h2>Age Calculator</h2>
            <form method="post">
                <label for="birthdate">Enter your birthdate:</label>
         
                <input type="date" id="birthdate" name="birthdate" required>
                
                <label for="option">Choose an option:</label>
                <select id="option" name="option">
                    <option value="months">Months</option>
                    <option value="days">Days</option>
                     <option value="seconds">Seconds</option>
                    <option value="milliseconds">Milliseconds
                </select>

                <button type="submit">Calculate</button>
            </form>

            {% if result %}
            <h3 class="result">{{ result }}</h3>
            {% endif %}
        </div>

    </body>
    </html>
    """, result=result)

if __name__ == "__main__":
    app.run(debug=True)


