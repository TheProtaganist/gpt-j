import requests
from .Gptj import generate
from .ImaginaryFriend import GPTJ_API


class Completion(GPTJ_API):

    def __init__(self, setting, user_bot_input_output_example):
        super().__init__(setting, user_bot_input_output_example)

        self.certain_slices = []
        assert isinstance(user_bot_input_output_example, dict), """Examples must be contained with a dictionary\nof key value pairs, the key being the example\nthe value being how you would like your friend to respond\nExamples... {"Hi":"How are you", "what is 2 + 2":"4"}"""
        self.sample_dialog = ""
        self.setting = str(setting) + "\n"
        self.user_bot_input_output_example = user_bot_input_output_example
        self.prompt = ""
        self.main_intention = ""
        self.result = ""
        self.user_name = ""
        self.friend_name = ""
        self.prompt_intent = ""
        self.response = ""
        self.answer = ""
        self.input_data = ""
        self.example_slices = []
        self.slices = []
        self.re_add_user = []
        self.add_new_line = ""
        self.new = ""
        self.newer = []
        self.new_list_of_edited_strings = ""
        self.newer_list = ""
        self.newest_list = ""
        self.amount_delete = 0
        self.new_prompt = ""
        self.final_answer = ""

    def completion(self, prompt, user="User", bot="Bot", max_tokens=100, temperature=1.0, top_p=0.6):
        try:
            self.user_name = str(user)
            self.friend_name = str(bot)
            self.prompt_intent = str(prompt)
            assert isinstance(user, str), "user argument must be string a value"
            assert isinstance(bot, str), "bot argument must be string a value"
            assert isinstance(max_tokens, int), "Max token most be integer value"
            assert isinstance(temperature, float), "temperature most be float value"
            assert isinstance(top_p, float), "top_p most be float value"
            if self.user_name != "" and self.friend_name != "" and self.prompt_intent != "":
                self.main_intention = str(prompt)
                self.sample_dialog = self.imaginary_friend(user, bot)
                self.input_data = f"{self.sample_dialog}\n{user}: {self.main_intention}\n{bot}: "
                self.example_slices = self.input_data.split("\nStudent: ")
                self.slices = [formatted_data for ex in zip(self.example_slices, ["\n"] * len(self.example_slices))
                               for formatted_data in ex][:-1]
                self.certain_slices = self.slices[2::2]
                self.re_add_user = [f"{user}: {i}\n\n" for i in self.certain_slices[:-1]]
                self.add_new_line = "".join(self.re_add_user)
                self.new = self.example_slices[0] + '\n' + self.add_new_line
                self.new.split("\n\n")
                self.newer = self.new.split("\n\n\n")
                self.new_list_of_edited_strings = self.newer[0]
                self.newer_list = self.new_list_of_edited_strings.split("\n\n")
                self.amount_delete = len(self.newer_list) - 1
                del self.newer_list[self.amount_delete]
                self.new_prompt = "\n\n".join(self.newer_list)
                self.response = generate(f"{self.new_prompt} {user}: {self.main_intention}",
                                         token_max_length=max_tokens,
                                         temperature=temperature,
                                         top_p=top_p)
                answer = self.response.replace(f"{bot}: ", "")
                list_of_char = answer.split(f"{user}: ", 1)
                answer2 = list_of_char[0]
                answer3 = answer2.split("\n")
                answer4 = "\n".join(answer3)
                self.final_answer = "\n".join([empty_line.rstrip() for  empty_line in answer4.splitlines() if empty_line.strip()])
                return self.final_answer
            elif self.user_name == "":
                print("Empty user name detected")
            elif self.friend_name == "":
                print("Empty bot name detected")
            else:
                print("Empty friend name detected")
            return self.result
        except requests.HTTPError:
            print("""Either the API is down or your values are too high."\nTry keeping max tokens, temperature, and top_p to a reasonable value\nAlso don't add too many examples add enough but not an huge amount""")
        return self.final_answer