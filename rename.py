# 各試合毎のPlayer1とPlayer2の文字列をプレイヤーの名称に置換
# 1試合1行でプレイヤーの名称がスペース区切りで記載されたplayers.txtを読み込み
# 各試合の対戦キャラと対戦プレイヤー、試合結果に反映する
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

# timestampファイル名
input_file = 'timestamps.txt'

# プレイヤーテキストファイル名
player_file = 'players.txt'

# 出力テキストファイル名
output_file = 'timestamps_rename.txt'

# Playerをsatoに置換して新しいテキストファイルを作成
replace_player(input_file, output_file, player_file)