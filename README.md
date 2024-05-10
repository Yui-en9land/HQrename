## 別で公開中のHQTimestampsから生成されるタイムスタンプのプレイヤー名をリネームするソフト  
# 必要なもの
 ・rename.exe(本ソフト)  
 ・タイムスタンプファイル（HQTimestampsから生成されるファイル）  
 ・対戦結果ファイル  
   　手動作成：１P側のプレイヤー名と２P側のプレイヤー名をスペース区切りで記載(1行毎)  
   　　　　　　記載例：sato kato  
   　BOT自動生成：生成されたファイル(yyyymmddresult.txt)をそのまま使用可能  
 ・replace_info.txt(手動作成の場合は不要)  
   　BOTが自動生成したファイルはサーバー名で記載されるため日本語が含まれる人もいるため  
   　youtubeで公開する際はアルファベットで記載する必要あり  
   　このファイルにリネーム対象を設定することでリネームが可能  
   　先頭にリネーム対象、カンマを挟んで後方にリネーム後の名称を記載  
   　　記載例：さとう,sato  
# 使い方  
  　①rename.exeを実行  
  　②ファイル選択画面でタイムスタンプファイルを選択  
  　③ファイル選択画面で対戦結果ファイルを選択  
  　④リネーム結果：timestamps_rename.txtが出力される  
