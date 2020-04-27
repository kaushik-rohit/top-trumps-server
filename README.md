# Advanced Software Engineering Project

## Top Trumps: Movie, a React based game
Our project idea is to build a react based web version of a popular cards game. The rules of the game are listed below:

- There are two players. For our basic version of the game, we will have one user player and other computer player.
- There can be multiple round to the game. We decide to keep the round limited to 10.
- In every round, both player gets assigned a card randomly from the deck.
- Deck is just a random sample of cards generated from our Movies dataset. For every game, we will sample 52 (or X) cards from the dataset for a given year.
- Every card includes the movie poster, a small description of movie and some feature of the movie like revenue, budget, year of release, number of languages, ratings
- Each user alternatively takes turn and select one feature to compete on.
- If the feature selected by user has a better value than his/her opponent, the user wins the round and gains point.
- The player with highest point at the end of 10 rounds wins the game.

### Docker
The application makes use of docker containers. Follow the steps below to run it in docker

1) To build the docker image run ``sudo docker build -t image_name:latest .``
2) To run the docker image, use ``sudo docker run -d -p 5001:5001 image_name``

### Accessibility
Access the server at http://0.0.0.0:5001/. This address & port are valid for both local execution as well as running docker images (as long as step 2) in the above section is applied).
