from flask import Flask
import random

facts_list = ["Większość osób cierpiących na uzależnienie technologiczne doświadcza silnego stresu, gdy znajdują się poza zasięgiem sieci lub nie mogą korzystać ze swoich urządzeń.",
              "Według badania przeprowadzonego w 2018 roku ponad 50% osób w wieku od 18 do 34 lat uważa się za zależne od swoich smartfonów.",
              "Badanie zależności technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych.",
              "Według badania z 2019 r. ponad 60% osób odpowiada na wiadomości służbowe na swoich smartfonach w ciągu 15 minut po wyjściu z pracy.",
              "Jednym ze sposobów walki z uzależnieniem od technologii jest poszukiwanie zajęć, które sprawiają przyjemność i poprawiają nastrój.",
              "Elon Musk twierdzi, że sieci społecznościowe są zaprojektowane tak, aby trzymać nas na platformie, abyśmy spędzali jak najwięcej czasu na przeglądaniu treści.",
              "Elon Musk opowiada się także za regulacją sieci społecznościowych i ochroną danych osobowych użytkowników. Twierdzi, że sieci społecznościowe gromadzą o nas ogromną ilość informacji, które następnie można wykorzystać do manipulowania naszymi myślami i zachowaniami.",
              "Sieci społecznościowe mają swoje zalety i wady, a korzystając z tych platform, powinniśmy być ich świadomi."
            ]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Cześć! Na tej stronie możesz dowiedzieć się kilku ciekawostek na temat zależności technologicznych!</h1> <a href="/random_fact">Zobacz losowy fakt!</a> <br> <a href="/password_generator">Wygeneruj hasło o długości 10 znaków!</a> <br> <a href="/coinflip">Rzuć monetą!</a>'
@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'
@app.route("/password_generator")
def gen_pass():
    elements = """1234567890-=qwertyuiop[]asdfghjkl;'\`zxcvbnm,./§£!@#$%^&*()_+QWERTYUIOP}{ASDFGHJKL:"|~ZXCVBNM<>?"""
    password = ""

    for i in range(10):
        password += random.choice(elements)

    return f"<p>{password}</p>"
@app.route("/coinflip")
def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
app.run(debug=True)
