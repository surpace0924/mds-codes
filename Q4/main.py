import random
from matplotlib import pyplot as plt

random.seed(42)

def monty_hall_problem(door_num, change_player=True):
    item_num = random.randrange(door_num)

    door_list_master = [i for i in range(door_num)]
    door_list = [i for i in range(door_num)]

    player_num = random.randrange(door_num)
    remove_num_list = [item_num, player_num]

    remove_num_list_door = []

    if change_player:
        while len(door_list) > 2:
            host_num = random.choice([i for i in door_list if i not in remove_num_list])
            remove_num_list.append(host_num)
            remove_num_list_door.append(host_num)

            door_list = [i for i in door_list_master if i not in remove_num_list_door]
        door_list.remove(player_num)
        player_num = door_list[0]

    if item_num == player_num:
        return 1
    else:
        return 0


def main():
    iter = 1000
    door_num = 100

    result_change = 0
    result_not_change = 0
    change_true = []
    change_false = []
    for num in range(1, iter+1):
        result_change += monty_hall_problem(door_num=door_num, change_player=True)
        result_not_change += monty_hall_problem(door_num=door_num, change_player=False)

        change_true.append(result_change/num)
        change_false.append(result_not_change/num)
    
    print('door num: ', door_num)
    print('iteration: ', iter)
    print('player change door: ', sum(change_true)/iter)
    print('player not change door: ', sum(change_false)/iter)

    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.plot([_num for _num in range(1, iter+1)], change_true, label="change")
    ax.plot([_num for _num in range(1, iter+1)], change_false, label="do not change")
    ax.set_xlabel('iteration')
    ax.set_ylabel('probability')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()