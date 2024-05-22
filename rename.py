# 各試合毎のPlayer1とPlayer2の文字列をプレイヤーの名称に置換
# 1試合1行でプレイヤーの名称がスペース区切りで記載されたplayers.txtを読み込み
# 各試合の対戦キャラと対戦プレイヤー、試合結果に反映する

from tkinter import filedialog
import datetime
import calendar

players_name_en = []
players_name_jp = []


def replace_formal(player_file, replace_info):
    players_list = []
    with open(player_file, 'r', encoding='utf-8') as player_in:
        with open(replace_info, 'r', encoding='utf-8') as info_in:
            player_lines = player_in.readlines()
            info_lines = info_in.readlines()
            for player_index in player_lines:
                player_split = player_index.split()
                for info_index in info_lines:
                    info_split = info_index.split(',')
                    player_index = player_index.replace(info_split[0], info_split[1])
                    player_index = player_index.replace('\n', '')
#                    player_index = player_index.replace(info_split[0], info_split[1])
#                    player_index = player_index.replace('\n', '')
                player_split = player_index.split()
                players_list.append([player_split[1], player_split[3]])
                if player_split[1] not in players_name_en:
                    players_name_en.append(player_split[1])
                    jp_name = player_split[1]
                    for info_index in info_lines:
                        info_split = info_index.split(',')
                        if info_split[1].replace('\n', '') == player_split[1]:
                            jp_name = info_split[0] + '(' + player_split[1] + ')'
                    players_name_jp.append(jp_name)
                if player_split[3] not in players_name_en:
                    players_name_en.append(player_split[3])
                    jp_name = player_split[3]
                    for info_index in info_lines:
                        info_split = info_index.split(',')
                        if info_split[1].replace('\n', '') == player_split[3]:
                            jp_name = info_split[0] + '(' + player_split[3] + ')'
                    players_name_jp.append(jp_name)
    return players_list, players_name_en, players_name_jp
def replace_player(input_file, output_file, player_file):
    with open(input_file, 'r', encoding='utf-8') as f_in:
        with open(player_file, 'r', encoding='utf-8') as p_in:
            with open(output_file, 'w', encoding='utf-8') as f_out:
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
    with open(input_file, 'r', encoding='utf-8') as f_in:
        with open(output_file, 'a', encoding='utf-8') as f_out:
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
            f_out.write('\n#hellishquart')

# timestampファイル名
input_file = filedialog.askopenfilename(title="タイムスタンプファイルを選択")

# 置換情報ファイル
replace_info = 'replace_info.txt'

# 置換情報ファイル
youtube_comment = 'youtube_comment.txt'

# プレイヤーテキストファイル名
player_file = filedialog.askopenfilename(title="対戦情報ファイルを選択")
filename = player_file[-21:]
year = filename[0:4]
month = filename[4:6]
day = filename[6:8]

# 出力テキストファイル名
output_file_en = 'timestamps_rename_en.txt'
output_file_jp = 'timestamps_rename_jp.txt'

# Playerを置換して新しいテキストファイルを作成
with open(player_file, 'r', encoding='utf-8') as p_in:
    line = p_in.readline()
    sprit = line.split()
    if sprit[0] == 'M01:':
        # BOT自動生成用
        [player_list, players_name_en, players_name_jp] = replace_formal(player_file, replace_info)
        with open(youtube_comment, 'r', encoding='utf-8') as yfile:
            comment = yfile.readlines()
        with open(output_file_en, 'w', encoding='utf-8') as f_out:
            title = ('[Hellish Quart PvP] ' + calendar.month_abbr[int(month)] + '-' + day + '-' + year)
            date = datetime.date(int(year), int(month), int(day))
            if date.weekday() == 5:
                f_out.write(title + ' Weekly Sparring\n\n')
                f_out.write('\n')
            else:
                f_out.write(title + ' Sparring\n')
                f_out.write('\n')
            for name in players_name_en:
                f_out.write(' - ' + name + '\n')
            f_out.write('\n')
        replace_playerlist(input_file, output_file_en, player_list)
        with open(output_file_jp, 'w', encoding='utf-8') as f_out:
            title = ('[Hellish Quart PvP] ' + year + '-' + month + '-' + day)
            date = datetime.date(int(year), int(month), int(day))
            if date.weekday() == 5:
                f_out.write(title + ' 週例オンライン対戦会\n')
                f_out.write('\n')
            else:
                f_out.write(title + ' 道場マッチ\n')
                f_out.write('\n')
            for name in players_name_jp:
                f_out.write(' - ' + name + '\n')
            f_out.write('\n')
        replace_playerlist(input_file, output_file_jp, player_list)
    else:
        # 手動生成用
        replace_player(input_file, output_file_en, player_file)