class RoyalBluff:

    def __init__(self, path: str, max_err_num: int):
        self.path = path
        self.max_err_num = max_err_num
        self.err_counter = 0

        with open(path) as f:
            self.ques_lst = [i for i in f]

        self.cur_ques = -1

    def get_next_question(self):
        self.cur_ques += 1
        return False if len(self.ques_lst) == self.cur_ques else self.ques_lst[self.cur_ques]

    def is_end_game(self, add_err):
        self.err_counter += add_err
        #print(f'{self.err_counter} {self.max_err_num}')
        if self.max_err_num == self.err_counter:
            return True
        return False

    def player_response(self, question: str):
        return input(f'Response the next question (Y or N): {question} ')


r = RoyalBluff("C:\\Users\\vitalii.mocanu\\PycharmProjects\\MyGames\\data\\Questions.csv", 2)

while True:

    q_r_list = r.get_next_question()
    if q_r_list == False:
        print('Game over! You won.')
        break

    x = (q_r_list.split(';')[0])
    y = (q_r_list.split(';')[1])
    z = (q_r_list.split(';')[2])
    # print(f'x {x} y {y} z {z}')

    if r.is_end_game(0):
        print('Game over! You lose.')
        break

    resp = r.player_response(x).lower()

    if resp == 'y':
        if y == "Yes":
            print('Well done! Right answer is {z}')
        else:
            print(f'Wrong! Right answer is {z}')
            r.is_end_game(1)
    elif resp == 'n':
        if y == "No":
            print('Well done! Right answer is {z}')
        else:
            print(f'Wrong! Right answer is {z}')
            r.is_end_game(1)
    else:
        print('You can answer only Y or N.')
        r.cur_ques -= 1

# print(r.get_next_question())
