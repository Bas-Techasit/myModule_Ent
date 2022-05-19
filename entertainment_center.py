import media
import fresh_tomatoes

ice_age = media.Movie("Ice Age",
                      "Twenty-thousand years ago, Earth is a wondrous, prehistoric world filled with great danger, not the least of which is the beginning of the Ice Age. To avoid a really bad frostbite, the planet's majestic creatures - and a few small, slothful ones - begin migrating south . The story revolves around sub-zero heroes: a woolly mammoth, a saber-toothed tiger, a sloth and a prehistoric combination of a squirrel and rat that is known as Scrat.",
                      "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSxVyagwfFHe3FrWofpHfuP0-gK8QIOqYs3V6jOR_phNprVoeZb",
                      "https://www.youtube.com/watch?v=Ohq6NmKMja8")


harry_potter = media.Movie("harry potter and sorcerer's stone",
                             "Based on the first of J.K. Rowling's popular children's novels about Harry Potter, the live-action family adventure film Harry Potter and the Sorcerer's Stone tells the story of a boy who learns on his 11th birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own. Invited to attend Hogwarts School of Witchcraft and Wizardry, Harry embarks on the adventure of a lifetime. At Hogwarts, he finds the home and the family he has never had.",
                             "https://images.moviesanywhere.com/143cdb987186a1c8f94d4f18de211216/fdea56fa-2703-47c1-8da8-70fc5382e1ea.jpg",
                             "https://www.youtube.com/watch?v=VyHV0BRtdxo")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=NgsQ8mVkN8w")


movies = [ice_age, ratatouille, harry_potter]
fresh_tomatoes.open_movies_page(movies)
