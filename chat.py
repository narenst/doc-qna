class ChatInterface:

    messages = []
    persons = {
        "user": {
            "name": "User",
            "color": "default",
            "role": "user"
        },
        "bot": {
            "name": "Bot",
            "color": "\033[94m",
            "role": "assistant"
        },
    }

    COLORS_ENDC = '\033[0m'

    # COLORS = {
    #     OKBLUE: '\033[94m',
    #     OKCYAN: '\033[96m',
    #     OKGREEN: '\033[92m',
    #     ENDC: '\033[0m',
    # }

    def __init__(self, ai):
        self.ai = ai
        self.bootstrap_messages()

    def add_message(self, person, message):
        """
        Adds the message to the messages list.
        """
        self.messages.append({
            "role": self.persons[person]["role"],
            "message": message,
        })

    def bootstrap_messages(self):
        """
        Adds the initial messages to the messages list.
        """
        pass

    def get_response(self, message):
        """
        Sends the message to the AI system (llm) and get the response.
        """
        return self.ai.process_messages(self.messages)
    
    def print_message(self, person, message):
        """
        Prints message with appropriate color encoding
        """
        print(self.persons[person]["color"] + f"{self.persons[person]['name']}: {message}" + self.COLORS_ENDC)

    def start(self):
        """
        Runs the chat interface.
        """
        print("Chat started. Type 'exit' to exit.")
        while True:
            message = input("You: ")
            if message == "exit":
                break
            self.add_message("user", message)
            response = self.get_response(message)

            self.print_message("bot", response)
            self.add_message("bot", response)
        print("Chat ended.")

        # print("Chat log:\n" + "\n".join([f"{message['role']}: {message['message']}" for message in self.messages]))