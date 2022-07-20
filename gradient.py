print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<style>")
print("hr{margin-top:0; margin-bottom:0} ")
print("</style>")
print("</head>")

print("<body>")

def print_range():
    for x in range(0, 256):
        print(f'<hr style = "color:rgb({x},{255-x},{255-x})">')
print_range()

print("</body>")

print("</html>")