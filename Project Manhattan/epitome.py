from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/1')

def tell_bad_jokes():
 bad_jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the claustrophobic astronaut? He just needed a little space.",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Parallel lines have so much in common. It's a shame they'll never meet.",
        "How do you organize a space party? You 'planet'!",
        "What do you call fake spaghetti? An 'impasta'!",
        "What's orange and sounds like a parrot? A carrot!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "I used to play piano by ear, but now I use my hands."
    ]
 jokes = random.choice(bad_jokes)
 return render_template('stale_jokes.html',jokes=jokes)

@app.route('/2')

def scientific_facts():
 science_facts = [
    "The double helix structure of DNA was first described by James Watson and Francis Crick in 1953.",
    "Albert Einstein's theory of relativity, including the famous equation E=mc², revolutionized our understanding of space, time, and energy-matter equivalence.",
    "The prevailing cosmological model suggests that the universe originated from a singularity in an event known as the Big Bang, around 13.8 billion years ago.",
    "The theory of plate tectonics explains the movement of Earth's lithospheric plates, leading to phenomena like earthquakes, volcanic activity, and the shaping of continents.",
    "Charles Darwin's theory of evolution by natural selection proposes that species gradually change over time through the inheritance of beneficial traits, driving biodiversity.",
    "Quantum physics is a branch of science that deals with the behavior of particles at the smallest scales, often exhibiting strange phenomena like superposition and entanglement.",
    "Humans have landed on the Moon (Apollo 11, 1969) and sent numerous spacecraft to explore other planets, moons, and even asteroids in our solar system.",
    "Completed in 2003, the Human Genome Project identified and mapped all the genes in human DNA, providing insights into our genetic makeup and potential health conditions.",
    "The scientific consensus supports the understanding that human activities, particularly the emission of greenhouse gases, are contributing to global climate change and rising temperatures.",
    "Science has led to remarkable medical breakthroughs, including the discovery of antibiotics, vaccines, and advanced imaging technologies, greatly improving human health and longevity."
  ]
 facts = random.choice(science_facts)
 return facts

@app.route('/3')

def widgets():
  return render_template('widget.html')
app.run(debug=True)
