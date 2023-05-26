from chat import ChatInterface
from ai import AI
from document import Documents

def main():
    documents = Documents()
    ai = AI(context=documents.get_contents())
    chat = ChatInterface(ai)
    chat.start()

if __name__ == "__main__":
    main()