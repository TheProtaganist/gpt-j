import json
from .Text2TextGen import GPTJ


class GPTJ_API(GPTJ):

    def __init__(self, context, user_bot_input_output_example):
        super().__init__(user_bot_input_output_example)
        self.conversation_dictionary = {}
        self.setting = str(context)
        self.dialog = ""
        self.user_bot_input_output_example = user_bot_input_output_example
        self.Person_speaking = [str(key) for key in user_bot_input_output_example]
        self.Bot_responding = [str(value) for value in user_bot_input_output_example.values()]
        self.ID = ""
        self.your_friend = ""
        self.json_conversation = {}
        self.intentions = ""
        self.responses = ""
        self.final_intention = []
        self.final_responses = []
        self.all_conversation = []
        self.user_aspect = []
        self.bot_aspect = []
        self.length = 0
        self.formatted_convo = []
        self.model_input = []

    def imaginary_friend(self, user_id, friend):
        self.ID = str(user_id) + ": "
        self.your_friend = str(friend) + ": "
        self.dialog = self.gptj_examples(self.Person_speaking, self.Bot_responding)
        self.json_conversation = json.loads(self.dialog)
        self.intentions = self.json_conversation["intentions"]
        self.responses = self.json_conversation["responses"]
        self.final_intention = [self.ID + i for i in self.intentions]
        self.final_responses = [self.your_friend + r for r in self.responses]
        self.all_conversation = [self.final_intention, self.final_responses]
        self.user_aspect = ["".join(i) for i in self.all_conversation[0]]
        self.bot_aspect = ["".join(r) for r in self.all_conversation[1]]
        self.length = len(self.user_aspect) * 2
        self.formatted_convo = [i for e in zip(self.user_aspect, [r for r in self.bot_aspect] * len(self.user_aspect))
                                for i in e][:self.length]
        self.model_input = '\n'.join(map(str, self.formatted_convo))
        self.setting += "\n" + self.model_input
        return self.setting
