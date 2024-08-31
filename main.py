def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type} : ")
    return user_input

first_noun = get_input("noun")
first_verb = get_input("verb")
second_noun = get_input("noun")
second_verb = get_input("verb")
my_adjective = get_input("adjective")


our_tale = f"""

Today, I went to the zoo and saw a(n) {my_adjective} {first_noun}.
It was amazing to watch it {first_verb} around its enclosure. 
Nearby, a {second_noun} was trying to {second_verb}. 
I had never seen anything like it before!

"""

print(our_tale)



