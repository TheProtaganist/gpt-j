import json

convo = {}


class GPTJ:

    def __init__(self, user_bot_input_output_example):
        assert isinstance(user_bot_input_output_example, dict), "User bot examples must be a dictionary"
        self.user_input_example = [key for key in user_bot_input_output_example]
        self.bot_output_example = [value for value in user_bot_input_output_example.values()]
        self.user_inputs = []
        self.bot_inputs = []
        self.conversation_json = {}

    def gptj_examples(self, uu, bb):

        full_conversation = [[], []]

        def username(user_response=uu):
            Examples1 = [str(example) for example in user_response]
            return Examples1

        def imaginary_character(bot_response=bb):
            Examples2 = [str(example2) for example2 in bot_response]
            return Examples2

        self.user_inputs = username(self.user_input_example)
        self.bot_inputs = imaginary_character(self.bot_output_example)

        length_of_user_inputs = len(self.user_inputs)
        length_of_bot_outputs = len(self.bot_inputs)
        if length_of_user_inputs == length_of_bot_outputs:
            full_conversation[0].append(self.user_inputs)
            full_conversation[1].append(self.bot_inputs)
            for element in full_conversation:
                for intention in full_conversation[0]:
                    convo['intentions'] = intention
                for response in full_conversation[1]:
                    convo['responses'] = response
            self.conversation_json = json.dumps(convo, indent=4)
            return self.conversation_json
        else:
            if length_of_user_inputs > length_of_bot_outputs:
                print([self.user_inputs[length_of_bot_outputs]])
                del self.user_inputs[length_of_bot_outputs:]
                full_conversation[0].append(self.user_inputs)
                full_conversation[1].append(self.bot_inputs)
                for element in full_conversation:
                    for intention in full_conversation[0]:
                        convo['intentions'] = intention
                    for response in full_conversation[1]:
                        convo['responses'] = response
                self.conversation_json = json.dumps(convo, indent=2)
                return self.conversation_json
            elif length_of_bot_outputs > length_of_user_inputs:
                print([self.bot_inputs[length_of_user_inputs]])
                del self.bot_inputs[length_of_user_inputs:]
                full_conversation[0].append(self.user_inputs)
                full_conversation[1].append(self.bot_inputs)
                for element in full_conversation:
                    for intention in full_conversation[0]:
                        convo['intentions'] = intention
                    for response in full_conversation[1]:
                        convo['responses'] = response
                self.conversation_json = json.dumps(convo, indent=2)
                return self.conversation_json
            return self.conversation_json