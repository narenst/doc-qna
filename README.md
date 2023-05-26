# Document understanding using LLMs

This project uses LLMs to understand a pdf document and answer questions about its contents.

## Setup

First install all the dependencies in `requirements.txt`

```
pip install requirements.txt
```

## Configuration

Configure your OPENAI key in your terminal environment.

```
export OPENAI_API_KEY=secret_from_open_ai
```

Tweak the prompt in `ai.py`. You can see the context document in `document.py` - this can be updated to read content from a pdf or txt file.

## Run the bot

To interact with the bot, run the main.py file

```
$ python main.py

Chat started. Type 'exit' to exit.
You: Who is curry?
Bot:  Wardell Stephen Curry II is an American professional basketball player for the Golden State Warriors of the National Basketball Association (NBA). He is widely regarded as one of the greatest basketball players of all time and the greatest shooter in NBA history.

You: How many MVPs has he won?
Bot:  Curry has won two NBA Most Valuable Player (MVP) awards.

You: How about Klay thompson?
Bot:  I don't know.

You: When did curry win his first championship?
Bot:  Curry won his first championship in 2014–15.

You: How many years before that did warriors win their previous championship?
Bot:  Curry and the Warriors won their previous championship in 1975, which was 39 years before Curry won his first championship in 2014–15.

You: How many nba records does he hold?
Bot:  Curry holds the NBA record for most three-pointers made in a regular season, with 272, and he holds the NBA record for career three-pointers, passing Ray Allen. He and teammate Klay Thompson also hold the record for combined three-pointers made in an NBA season with 484, a record they broke the following season (525) and again in the 2015–16 season (678).

You: what he is best known for?
Bot:  Curry is best known for revolutionizing the sport of basketball by inspiring teams and players to take more three-point shots, as well as for his shooting abilities, which have earned him and teammate Klay Thompson the nickname "The Splash Brothers."
```

## Changing behavior

There are a few ways to change the behavior of the bot:

- Edit the OpenAI configuration in `ai.py`
- Tweak the prompt in `ai.py`
- Change the document parsing logic in `document.py`
- To change the chat behavior update `chat.py`