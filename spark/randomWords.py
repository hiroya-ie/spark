import random
from pytrends.request import TrendReq
from bs4 import BeautifulSoup
from urllib.request import urlopen
import wikipedia
import warnings


ie_word_list=["人工知能", "WEB","スマホ","API","拡張現実", "仮想現実", "自然言語処理", "画像処理", "機械学習", 
"データベース", "GPS", "カメラ", "指紋認証", "顔認証", "サーモグラフィ", "リモート", "ロボット", "3D",
 "音声", "SNS", "メール", "自動化", "オンライン", "電子化","分析","Python","C言語","Java","JavaScript",
  "HTML","CSS","C++","Go言語","Django", "Tkinter", "Xcode", "Processing",]
  
ie_original_word=["北食","でんちう","琉大map","宜野湾農工大", "ファイヤー和田", "TODOリスト","webmail",
"教務情報",
"webclass",
"図書館",
"時間割",
"駐車場",
"中央食堂",
"アルバイト",
"副専攻",
"オンライン授業","TKG","Do link","サークル", "冷水機", "301号室","インターン","一人暮らし", "安否確認システム",
"課題", "レポート", "OS","河野先生", "相談", "学サポ", "ゲーム", "休み時間", "教科書", "トイレ", "ゴミ箱" ,"出欠", "テスト",
"単位", "モブプロ", "ペアプロ", "自販機", "自動車学校", "休憩場所", "zoom", "mattermost" ,"discord","cotediter",
"翻訳", "ニュース", "スポーツ", "ショッピング", "マッチング", "音楽", "写真", "ホテル", "ヘルスケア",]

  #'アイデンティティ管理', 'アクセス解析', 'アドイン', 'アドオン', 'アンケートシステム', '安否確認システム',
# '暗号化', 'インシデント', 'インジェクション攻撃', 'インフラ', 'インベントリ', 'イーサネット', 'ウィルス対策',
# 'ウォームスタンバイ', '受付システム', 'エクサバイト', 'エンタープライズサーチ', 'オブジェクト指向', 'オンデマンド',
# 'オンラインストレージ', 'オープンシステム', 'オープンソース', 'カスタマー・リレーションシップ・マネジメント', 
# 'カラーバーコード', '会計ソフト', '可用性', '開発ツール', 'キッティング', 'ギガバイト', '勤怠管理システム', 
# '給与システム', 'クエリ', 'クライアント仮想化', 'グループウェア', '原価管理', '形態素解析', '検疫ネットワーク', 
# 'コロケーション', 'コンテンツマネジメントシステム', 'コンフィグレーション', 'コールセンター', 'サプライチェーンマネジメント',
# 'サーバ', 'サービスデスク', 'シングルサインオン', '人事システム', '人事給与システム', '冗長性', '情報共有', '指紋認証', 
# '社内SNS', '資産管理', 'スイッチ', 'スケールアップ', 'ストレージ', 'ストレージ仮想化', 'スパイウェア', 'スパム',
# 'スマートデバイス', 'スループット', 'セキュリティホール', 'セキュリティ診断サービス', 'セッション', 
# 'セールスフォースオートメーション', 'ゼロデイ攻撃', '生体認証', 'タレントマネジメント', '帯域制御', '帯域監視',
# 'チャット', 'チャットボット', 'テキストマイニング', 'テラバイト', 'テレビ会議', 'ディザスタリカバリ',
# 'デジタルサイネージ', 'デスクトップ仮想化', 'デバッガ', 'データウェアハウス', 'データセンター', 'データベース', 
# 'データマイニング', '電子メール', '電子認証', 'ドキュメント管理', '特権ID管理', '統合運用管理', 'ナレッジマネジメント', 
# '入退室管理', 'ネットワーク仮想化', 'ハイアベイラビリティ', 'ハイパーバイザ', 'ハウジング', 'バイト', 'バックアップ',
# 'パケット', 'ビジネスインテリジェンス', '標的型攻撃', 'ファイアウォール', 'ファイル管理', 'フィッシング', 
# 'フェイルオーバー', 'フレームワーク', 'ブログ', 'プロジェクトマネジメント', 'プロジェクト管理', '不正アクセス', 
# '分散処理', '文書管理', '物流管理', '複合機', 'ヘルプデスク', 'ペタバイト', 'ペーパーレス会議', 'ホットスタンバイ',
# 'ボット', 'ミドルウェア', '無線LAN', 'メインフレーム', 'メールアーカイブ', 'メールセキュリティ', 'メール配信',
# 'モバイルコンピュータ', 'リカバリ', 'リストア', 'リッチクライアント', 'リモートアクセス', 'ルータ',
# 'レガシーシステム', 'ログ', 'ロードバランサ', 'ワンタイムパスワード', 'ワークフロー', 'ABI', 'ACL', 'Ajax',
# 'android', 'Apache', 'ASP', 'AV', 'BC', 'BPM', 'BREW', 'BYOD', 'CAD', 'CAE', 'CAM', 'CMS', 'DaaS',
# 'DDoS攻撃', 'DHCP', 'DLP', 'DMI', 'DMP', 'DMZ', 'DNS（DigitalNervousSystem）', 
# 'DNS（DomainNameSystem）', 'DoS攻撃', 'Dropbox', 'DWH', 'EAI', 'ECP', 'EDA', 'EDI', 'EIP',
# 'EOS', 'ESB', 'ETL', 'eラーニング', 'FAQシステム', 'Flash', 'FTP', 'GUI', 'HaaS', 'HTML', 'HTTPS', 
# 'IaaS', 'ICタグ', 'iOS', 'iPhone', 'IPP', 'IPコミュニケーション', 'IP電話', 'ITIL', 'IT資産管理', 
# 'Java', 'JSP', 'KVMスイッチ', 'L2スイッチ', 'LAN', 'Linux', 'MDM', 'MySQL', 'NAS', 'NGN', 'OCR',
# 'OpenFlow', 'PaaS', 'PBX', 'PDA', 'PDM', 'PKI', 'POSシステム', 'RDB', 'RFID', 'root権限', 'SaaS',
# 'SBC', 'SDN', 'SFA', 'SMS', 'SNS', 'SOA', 'SSD', 'SSL', 'SSO', 'TCO', 'タブレット', 'UNIX',
# 'UTM（統合脅威管理）', 'VoIP', 'VPN', 'VPS', 'WAF', 'WAN', 'WebRTC', 'Webメール', 'Web会議', 'WordPress']


#pytrendからリスト作成
pytrend = TrendReq(hl='ja-jp',tz=540)
trend_wl = pytrend.trending_searches(pn='japan')[0].to_list()

# 言語を日本語に設定
wikipedia.set_lang("jp")

def randomA():
    result = []
    result.extend(trend_wl)
    ie_list=random.sample(ie_word_list, 9)
    result.extend(ie_original_word)
    return ie_list, random.sample(result, 9)


#wikiあり
def randomB():
    result = []
    result.extend(trend_wl)
    ie_list=random.sample(ie_word_list, 9)
    result.extend(ie_original_word)

    word=ie_list[0]
    wiki= wikip(word=word)

    return ie_list, random.sample(result, 9), wiki




#連想語サイトからスクレイピングしてリスト作成
#def rensou():
wlist=[]
#for i in range(5):
html = urlopen("https://renso-ruigo.com")
data = html.read()
html = data.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all("a")
rensou_words_list=[a.text for a in links]
del rensou_words_list[:4]
del rensou_words_list[-55:]
wlist.extend(rensou_words_list)

    #return wlist

    
def wikip(word):
  warnings.catch_warnings()
  warnings.simplefilter("ignore")
  try:
    line=wikipedia.summary(word)
  except wikipedia.exceptions.DisambiguationError as e:
    line= "自分で調べてください"
  return line