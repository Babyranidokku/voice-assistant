def safe_eval(text):
    try:
        text = text.replace("plus","+").replace("minus","-").replace("multiply","*").replace("divide","/")
        result = eval(text)
        return f"Result: {result}"
    except: return "Cannot calculate."