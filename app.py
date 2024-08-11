from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    input1 = request.form.get("input1", "")
    input2 = request.form.get("input2", "")
    gate = request.form.get("gate", "AND")
    
    result = None

    if input1 in ["0", "1"] and input2 in ["0", "1"]:
        input1 = int(input1)
        input2 = int(input2)
        
        if gate == "AND":
            result = input1 & input2
        elif gate == "OR":
            result = input1 | input2
        elif gate == "NAND":
            result = not (input1 & input2)
        elif gate == "NOR":
            result = not (input1 | input2)
        elif gate == "XOR":
            result = input1 ^ input2
        elif gate == "XNOR":
            result = not (input1 ^ input2)
        result = int(result)
    else:
        result = "Invalid input"

    return render_template("index.html", result=result, input1=input1, input2=input2, gate=gate)

if __name__ == "__main__":
    app.run(debug=True)