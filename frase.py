import random

verbs = ["voar", "dançar", "cantar", "viajar", "estudar", "dormir"]

adjectives = ["lindo", "esperto", "inteligente" , "amigo" , "amável" , "adorável"]

animals = ["gato" , "camelo" , "cachorro" , "elefante", "coelho"]

verb = random.choice(verbs)

adjective = random.choice(adjectives)

animal = random.choice(animals)

phrase = animal +" " +  adjective + " gosta de " + verb

print(phrase)