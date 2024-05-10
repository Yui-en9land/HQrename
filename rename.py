# 各試合毎のPlayer1とPlayer2の文字列をプレイヤーの名称に置換
# 1試合1行でプレイヤーの名称がスペース区切りで記載されたplayers.txtを読み込み
# 各試合の対戦キャラと対戦プレイヤー、試合結果に反映する

from tkinter import filedialog


def replace_formal(player_file, replace_info):
    players_list = []
    with open(player_file, 'r') as player_in:
        with open(replace_info, 'r') as info_in:
            player_lines = player_in.readlines()
            info_lines = info_in.readlines()
            for player_index in player_lines:
                player_split = player_index.split()
                for info_index in info_lines:
                    info_split = info_index.split(',')
                    player_index = player_index.replace(info_split[0], info_split[1])
                    player_index = player_index.replace('\n', '')
                    player_index = player_index.replace(info_split[0], info_split[1])
                    player_index = player_index.replace('\n', '')
                player_split = player_index.split()
                players_list.append([player_split[1], player_split[3]])
    return players_list
def replace_player(input_file, output_file, player_file):
    with open(input_file, 'r') as f_in:
        with open(player_file, 'r') as p_in:
            with open(output_file, 'w') as f_out:
                lines = f_in.readlines()
                for i in range(0, len(lines), 2):
                    player_line = p_in.readline()
                    players = player_line.split()
                    # 1行目と2行目の両方にPlayerが含まれている場合に置換
                    if 'Player1' in lines[i] or 'Player1' in lines[i+1]:
                        lines[i] = lines[i].replace('Player1', players[0])
                        lines[i+1] = lines[i+1].replace('Player1', players[0])
                    if 'Player2' in lines[i] or 'Player2' in lines[i+1]:
                        lines[i] = lines[i].replace('Player2', players[1])
                        lines[i+1] = lines[i+1].replace('Player2', players[1])
                    f_out.write(lines[i])
                    f_out.write(lines[i+1])

def replace_playerlist(input_file, output_file, players_list):
    player_index = 0
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            lines = f_in.readlines()
            for i in range(0, len(lines), 2):
                # 1行目と2行目の両方にPlayerが含まれている場合に置換
                if 'Player1' in lines[i] or 'Player1' in lines[i+1]:
                    lines[i] = lines[i].replace('Player1', players_list[player_index][0])
                    lines[i+1] = lines[i+1].replace('Player1', players_list[player_index][0])
                if 'Player2' in lines[i] or 'Player2' in lines[i+1]:
                    lines[i] = lines[i].replace('Player2', players_list[player_index][1])
                    lines[i+1] = lines[i+1].replace('Player2', players_list[player_index][1])
                    player_index += 1
                f_out.write(lines[i])
                f_out.write(lines[i+1])

# timestampファイル名
input_file = filedialog.askopenfilename(title="タイムスタンプファイルを選択")

# 置換情報ファイル
replace_info = 'replace_info.txt'

# プレイヤーテキストファイル名
player_file = filedialog.askopenfilename(title="対戦情報ファイルを選択")

# 出力テキストファイル名
output_file = 'timestamps_rename.txt'

# Playerを置換して新しいテキストファイルを作成
with open(player_file, 'r') as p_in:
    line = p_in.readline()
    sprit = line.split()
    if sprit[0] == 'M01:':
        player_list = replace_formal(player_file, replace_info)
        replace_playerlist(input_file, output_file, player_list)
    else:
        replace_formal(player_file, replace_info)
        replace_player(input_file, output_file, player_file)