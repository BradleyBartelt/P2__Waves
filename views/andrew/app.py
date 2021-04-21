from flask import render_template, request
from views.andrew import andrew_bp
from views.andrew.algo.minilab import Pi
from views.andrew.algo.bubble import BubbleSort



@andrew_bp.route('/',methods = ["GET","POST"])
def index():
    return render_template("landing.html")

@andrew_bp.route('/dataset',methods = ["GET","POST"])
def dataSet():
    if request.form:
        return render_template("mini_lab.html", pi=Pi(int(request.form.get("number"))))
    return render_template("mini_lab.html", pi=Pi(2))

@andrew_bp.route('/bubbleSort',methods = ["GET","POST"])
def bubbleSort():
    arr = []
    isString = False
    if request.form:
        string = request.form.get("string")
        arr = string.split()
        original = string.split()
        if(request.form["select"] == "integer"):
            try:
                for j in range (0,len(arr)):
                    arr[j] = int(arr[j])
                for j in range (0,len(original)):
                    original[j] = int(original[j])
                return render_template("Buuble_sort.html",output_list = BubbleSort(arr,isString).OuputList,original_list = original)
            except ValueError:
                return render_template("Buuble_sort.html",output_list = "Can Only Contain String or Integer",original_list = "Error")
        else:
            try:
                isString = True
                return render_template("Buuble_sort.html",output_list = BubbleSort(arr,isString).OuputList,original_list = original)
            except ValueError:
                return render_template("Buuble_sort.html",output_list = "Can Only Contain String or Integer",original_list = "Error")
    return render_template("Buuble_sort.html",output_list = BubbleSort(arr,isString).OuputList,original_list = arr)


