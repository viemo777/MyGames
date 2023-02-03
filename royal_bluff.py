from game_status import GameStatus


class RoyalBluff:

    def __init__(self, path: str, max_err_num: int):

        if max_err_num > 5 or max_err_num <1:
            raise ValueError('Allowed mistakes should be between 1 and 5')

        self.path = path
        self.max_err_num = max_err_num
        self.err_counter = 0

        with open(path) as f:
            self.ques_lst = [i for i in f]

        self.cur_ques = -1
        self.__game_status = GameStatus.IN_PROGRESS

    def get_next_question(self):
        self.cur_ques += 1
        return False if len(self.ques_lst) == self.cur_ques else self.ques_lst[self.cur_ques]

    def is_end_game(self, add_err):
        self.err_counter += add_err
        #print(f'{self.err_counter} {self.max_err_num}')
        if self.max_err_num == self.err_counter:
            self.__game_status = GameStatus.GAME_IS_OVER
            print('Game over! You lost.')


    def player_response(self, question: str):
        return input(f'Response the next question (Y or N): {question} ')

    @property
    def game_status(self):
        return self.__game_status

r = RoyalBluff("C:\\Users\\vitalii.mocanu\\PycharmProjects\\MyGames\\data\\Questions.csv", 4)

while r.game_status == GameStatus.IN_PROGRESS:

    q_r_list = r.get_next_question()
    if q_r_list == False:
        print('Game over! You won.')
        break

    x = (q_r_list.split(';')[0])
    y = (q_r_list.split(';')[1])
    z = (q_r_list.split(';')[2])
    # print(f'x {x} y {y} z {z}')

    # if r.is_end_game(0):
    #     print('Game over! You lost.')
    #     break

    resp = r.player_response(x).lower()

    if resp == 'y':
        if y == "Yes":
            print(f'Well done! Right answer is {z}')
        else:
            print(f'Wrong! Right answer is {z}')
            r.is_end_game(1)
    elif resp == 'n':
        if y == "No":
            print(f'Well done! Right answer is {z}')
        else:
            print(f'Wrong! Right answer is {z}')
            r.is_end_game(1)
    else:
        print('You can answer only Y or N.')
        r.cur_ques -= 1

# print(r.get_next_question())
