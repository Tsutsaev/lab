from flask import Flask,render_template,request

app=Flask(__name__)

    
@app.route('/')
def hello():
    user_data = {
    "name": "Ишхоев Ахмед Сайд-Мустапаевич",
    "link": "https://www.youtube.com/",
    "description": "Lorem <em>ipsum</em> dolor sit amet consectetur <strong>adipisicing </strong>  elit. Debitis mollitia deleniti, cupiditate corporis ab obcaecati sit distinctio ratione, consequatur quo illum sunt quia voluptates neque numquam incidunt repudiandae. Possimus, expedita?",
    "telegram": "ivan_dev",
}
    return render_template('hello.html', user=user_data)


app.run(debug=True)