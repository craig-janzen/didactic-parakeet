#!/usr/bin/env python3
"""Generate ordering-questions.json covering every grammar point in grammar-questions.js."""
import json, os

# Each entry: (lesson, grammar, prefix, [4 tokens], suffix, star_slot_1_indexed, explanation_ja, translation_en)
Q = [
    # ========== Lesson 1 ==========
    (1, "～際に", "", ["海外へ","出張する","際には","現地の"], "法律を事前に調べておくべきだ。", 3,
     "「～際に」は「～とき」の硬い表現で、改まった場面や書き言葉でよく使われる。",
     "When traveling abroad for business, you should look into local laws in advance."),
    (1, "～にあたって", "", ["新入生を","迎えるに","あたり","校長が"], "歓迎の言葉を述べた。", 3,
     "「～にあたって（にあたり）」は「～する時に」の意味で、何か重要なことを始める場面で使う。",
     "On the occasion of welcoming the new students, the principal gave a welcoming address."),
    (1, "～とたんに", "", ["ドアを","開けた","とたん","猫が"], "外に飛び出していった。", 2,
     "「～とたん（に）」は「～した直後に」の意味で、前後の出来事が同時または連続で起こることを表す。",
     "The moment I opened the door, the cat ran outside."),
    (1, "～かと思うと", "", ["娘は","学校から","帰ったかと","思うと"], "すぐ友達の家へ出かけた。", 3,
     "「～かと思うと」は「～した直後にすぐ別のことが起こる」様子を表す。意外性を伴うことが多い。",
     "No sooner had my daughter come home from school than she went to a friend's house."),
    (1, "～かのうちに", "", ["電車の","ドアが","閉まるか","閉まらないかの"], "うちに走って乗り込んだ。", 3,
     "「～か～ないかのうちに」は「～するとほぼ同時に」の意味で、二つの動作が非常に近いタイミングで起こる。",
     "The moment the train doors were about to close, I ran in and boarded."),

    # ========== Lesson 2 ==========
    (2, "～最中に", "", ["会議の","最中に","突然","携帯が"], "鳴ってしまい、恥ずかしかった。", 2,
     "「～最中に」は「まさに～している途中で」の意味で、進行中の動作を強調する。",
     "Right in the middle of the meeting, my phone suddenly rang, and it was embarrassing."),
    (2, "～うちに", "", ["雨が","降らない","うちに","洗濯物を"], "取り込んでおこう。", 3,
     "「～うちに」は「～という状態が続いている間に」の意味で、その状態が変わる前にという含みがある。",
     "Let's bring the laundry in before it starts to rain."),
    (2, "～一方だ", "", ["インターネットの","普及で","情報量は","増える"], "一方だ。", 4,
     "「～一方だ」は「ずっと～し続けている」「ますます～になる」の意味で、変化が一方向に進む様子を表す。",
     "With the spread of the internet, the amount of information just keeps increasing."),
    (2, "～ところだ", "", ["ちょうど","晩ご飯を","食べる","ところだった"], "ので、電話に出られなかった。", 3,
     "「～ところだ」は動作の段階を表し、「～する直前／最中／直後」などを意味する。",
     "I couldn't answer the phone because I was just about to eat dinner."),
    (2, "～つつある", "", ["地球の","温暖化は","急速に","進行しつつある"], "と言われている。", 4,
     "「～つつある」は「だんだん～している」の意味で、変化が継続している様子を書き言葉で表す。",
     "It is said that global warming is progressing rapidly."),
    (2, "～つつ/ながら", "", ["仕事を","続けつつ","大学院で","勉強する"], "のはとても大変だ。", 2,
     "「～つつ」は「～ながら」と同じく同時進行を表す、やや硬い表現。",
     "Continuing to work while studying in graduate school is extremely demanding."),
    (2, "～している(進行中)", "", ["今","母は","台所で","料理をしている"], "ところです。", 4,
     "「～している」は動作の進行中や状態の継続を表す基本表現。",
     "Right now my mother is in the kitchen cooking."),

    # ========== Lesson 3 ==========
    (3, "～はじめて", "", ["親に","なってから","子育ての","大変さを"], "はじめて実感した。", 4,
     "「～てはじめて」は「～した後に初めて～する」の意味で、経験を通じた気づきを表す。",
     "Only after becoming a parent did I truly realize how difficult child-rearing is."),
    (3, "～上で", "", ["契約書を","よく読んだ","上で","サインを"], "してください。", 2,
     "「～上で」は「～してから、その結果を踏まえて」の意味。順序と根拠を示す。",
     "Please sign only after carefully reading the contract."),
    (3, "～次第", "", ["先方から","連絡が","あり","次第"], "すぐに知らせます。", 4,
     "「～次第」は「～したらすぐに」の意味で、ビジネス場面でよく使われる。",
     "As soon as we hear back from the other party, I'll let you know immediately."),
    (3, "～以来", "", ["あの","事故","以来","彼は"], "二度と車に乗っていない。", 3,
     "「～以来」は「～してから（ずっと）」の意味で、ある出来事を起点とする継続を表す。",
     "Ever since that accident, he has not gotten into a car again."),
    (3, "～からでないと", "", ["登録を","済ませて","からでないと","会員サービスは"], "ご利用いただけません。", 3,
     "「～からでないと」は「～した後でなければ」の意味で、必要条件を示す。",
     "You cannot use our member services until after you have completed registration."),
    (3, "～後で", "", ["会議が","終わった","後で","資料を"], "送ってください。", 3,
     "「～後で」は「～した後に」の意味で、時間の順序を明確にする。",
     "Please send the materials after the meeting is over."),

    # ========== Lesson 4 ==========
    (4, "～をはじめ", "", ["日本は","東京を","はじめ","多くの"], "都市で人口が集中している。", 3,
     "「～をはじめ」は「～を代表として、他にも」の意味で、多くのものの中から一つを例示する。",
     "In Japan, starting with Tokyo, population is concentrated in many cities."),
    (4, "～からして", "", ["あの","店は","料理の","見た目からして"], "プロの腕前だとわかる。", 4,
     "「～からして」は「～を見ただけで」の意味で、一例からの強い推測を表す。",
     "At that restaurant, the very look of the food tells you it's prepared by professionals."),
    (4, "～にわたって", "", ["この","調査は","10年に","わたって"], "続けられてきた。", 4,
     "「～にわたって」は時間・範囲の広がりを表し、「～の全範囲で」の意味。",
     "This research has been carried out over a span of ten years."),
    (4, "～を通じて", "", ["読書を","通じて","様々な","知識を"], "得ることができる。", 2,
     "「～を通じて」は「～を手段や経路として」または「～の期間ずっと」の意味で使われる。",
     "Through reading, one can acquire various kinds of knowledge."),
    (4, "～限り", "", ["力の","限り","最後まで","諦めずに"], "戦いたい。", 2,
     "「～限り」は「～の範囲の全て」「～である間は」など範囲・期間の上限を示す。",
     "I want to fight to the very end with all my strength, without giving up."),
    (4, "～だけ", "", ["好きな","だけ","食べて","いいですよ"], "と言われた。", 2,
     "「～だけ」は「その範囲のすべて」を表し、制限なしに行ってよいことを示す。",
     "I was told, \"You can eat as much as you like.\""),

    # ========== Lesson 5 ==========
    (5, "～に限り", "", ["本日に","限り","全商品が","半額で"], "ご購入いただけます。", 2,
     "「～に限り」は「～の場合のみ特別に」の意味で、書き言葉・案内でよく使われる。",
     "For today only, all items may be purchased at half price."),
    (5, "～限りでは", "", ["私が","知っている","限りでは","彼は"], "まだ帰国していない。", 3,
     "「～限りでは」は「～の範囲で判断すると」の意味で、情報の範囲を限定する。",
     "As far as I know, he has not yet returned to his home country."),
    (5, "～に限って", "", ["急いで","いる時に","限って","電車が"], "遅れるものだ。", 3,
     "「～に限って」は「よりにもよって～の時に」の意味で、悪いタイミングが重なる様子を表す。",
     "It's precisely when you're in a hurry that the trains tend to be delayed."),

    # ========== Lesson 11 ==========
    (11, "～を問わず", "", ["このアプリは","年齢を","問わず","誰でも"], "楽しむことができる。", 3,
     "「～を問わず」は「～に関係なく」の意味で、条件や属性に左右されないことを示す。",
     "This app can be enjoyed by anyone, regardless of age."),
    (11, "～にかかわらず", "", ["天候に","かかわらず","試合は","予定通り"], "行われます。", 2,
     "「～にかかわらず」は「～に関係なく」の意味で、影響を受けないことを強調する。",
     "Regardless of the weather, the match will be held as scheduled."),
    (11, "～もかまわず", "", ["彼は","人目も","かまわず","大声で"], "泣き出した。", 3,
     "「～もかまわず」は「～を気にしないで」の意味で、普通は気を遣う場面で構わない様子を表す。",
     "He broke into loud sobs, not caring who might see him."),
    (11, "～はともかく", "", ["味は","ともかく","値段は","とても"], "手ごろだ。", 2,
     "「～はともかく」は「～は一旦置いておいて」の意味で、別の側面に焦点を当てる。",
     "Setting taste aside, the price is very reasonable."),
    (11, "～はさておき", "", ["冗談は","さておき","本題に","入りましょう"], "か。", 2,
     "「～はさておき」は「～は後回しにして」の意味で、話題を切り替える際に使う。",
     "Jokes aside, shall we get down to the main topic?"),

    # ========== Lesson 12 ==========
    (12, "～わけがない", "", ["彼が","そんな","嘘を","つくわけがない"], "。", 4,
     "「～わけがない」は「～はずがない」と似て、可能性を強く否定する表現。",
     "There's no way he would tell such a lie."),
    (12, "～どころか", "", ["宿題を","終える","どころか","まだ"], "始めてもいない。", 3,
     "「～どころか」は「～はもちろん、それ以下（以上）の事も」という強い否定・対比を表す。",
     "Far from finishing my homework, I haven't even started it."),
    (12, "～もんか", "", ["あんな","失礼な店に","二度と","行くもんか"], "。", 4,
     "「～もんか」は話し言葉で「絶対に～しない」という強い拒否を表す。",
     "There's no way I'm ever going back to that rude restaurant."),
    (12, "～というわけではない", "", ["嫌いだ","という","わけではない","が"], "あまり食べたくない。", 3,
     "「～というわけではない」は部分否定で「完全にそうとは限らない」と和らげて言う表現。",
     "It's not that I dislike it, but I don't really feel like eating it."),
    (12, "～というものではない", "", ["値段が","高ければ","いいという","ものではない"], "。", 4,
     "「～というものではない」は「必ずしも～ではない」の意味で、一般論を否定する。",
     "It's not as though something is good simply because it's expensive."),

    # ========== Lesson 13 ==========
    (13, "～とは", "", ["締め切りが","明日","だとは","全く"], "知らなかった。", 3,
     "「～とは」は驚きや意外性を表す表現で、「～なんて」と似た使い方をする。",
     "I had no idea at all that the deadline was tomorrow."),
    (13, "～といえば", "", ["京都","といえば","やはり","寺や"], "神社が有名だ。", 2,
     "「～といえば」は話題を導入し、「～について言うなら」の意味で関連情報を続ける。",
     "Speaking of Kyoto, it's of course famous for its temples and shrines."),
    (13, "～といったら", "", ["富士山の","美しさ","といったら","言葉に"], "できないほどだ。", 3,
     "「～といったら」は強い感情や驚きを伴う評価を表す。",
     "The beauty of Mt. Fuji is almost beyond words."),
    (13, "～のこととなると", "", ["普段は","冷静な","父も","野球のこととなると"], "興奮する。", 4,
     "「～のこととなると」は「～の話題になると特別な反応をする」という意味を表す。",
     "My normally calm father gets excited whenever the topic turns to baseball."),

    # ========== Lesson 14 ==========
    (14, "～にもかかわらず", "", ["雨が","降っているに","もかかわらず","試合は"], "続行された。", 3,
     "「～にもかかわらず」は「～のに」の硬い形で、逆接的な状況を強調する。",
     "Despite the fact that it was raining, the match continued."),
    (14, "～ものの", "", ["日本語を","10年勉強した","ものの","まだ"], "新聞は読みにくい。", 3,
     "「～ものの」は「～したけれど」の意味で、予想と違う結果を導く。",
     "Although I've studied Japanese for ten years, newspapers are still difficult for me."),
    (14, "～ながら", "", ["狭い","ながら","我が家は","とても"], "落ち着く。", 2,
     "逆接の「～ながら」は「～だけれども」の意味で、形容詞や名詞に接続する。",
     "Small though it may be, my home is very relaxing."),
    (14, "～つつ", "", ["体に","悪いと","知りつつ","夜食を"], "やめられない。", 3,
     "逆接の「～つつ」は「～しているのに」の意味で、書き言葉的な表現。",
     "Even though I know it's bad for me, I can't stop my late-night snacking."),
    (14, "～からといって", "", ["安い","からといって","品質が","悪い"], "とは限らない。", 2,
     "「～からといって」は「～という理由だけで（当然のように）」を否定する文脈で使う。",
     "Just because something is cheap doesn't necessarily mean its quality is poor."),

    # ========== Lesson 15 ==========
    (15, "～とすれば", "", ["今から","出発する","とすれば","何時に"], "着くだろうか。", 3,
     "「～とすれば」は「仮に～したら」と仮定を表し、推量の結論と組み合わせて使う。",
     "If we leave now, what time do you think we'll arrive?"),
    (15, "～ものなら", "", ["できる","ものなら","もう一度","学生時代に"], "戻りたい。", 2,
     "「～ものなら」は「もしも～できるなら」の意味で、実現が難しい願望を表す。",
     "If I could, I would love to return to my student days once more."),
    (15, "～ようものなら", "", ["約束を","破ろう","ものなら","二度と"], "信用されないだろう。", 3,
     "「～ようものなら」は「もし～したら大変なことになる」と悪い結果を強調する仮定表現。",
     "If you were to break the promise, you would never be trusted again."),
    (15, "～ないことには", "", ["実物を","見ない","ことには","判断"], "しようがない。", 3,
     "「～ないことには」は「～しなければ…できない」という必要条件を表す。",
     "Without actually seeing the real thing, there's no way to make a judgment."),
    (15, "～抜きにしては", "", ["彼の","協力を","抜きにしては","この"], "プロジェクトは成功しなかっただろう。", 3,
     "「～抜きにしては」は「～なしでは」の意味で、不可欠な要素を強調する。",
     "Without his cooperation, this project would not have succeeded."),
    (15, "～にせよ", "", ["どんな","理由が","あったに","せよ"], "遅刻はよくない。", 4,
     "「～にせよ」は「～であっても」の意味で、どの場合でも結論が変わらないことを示す。",
     "Whatever the reason may have been, being late is not acceptable."),
]

out = []
for i, (lesson, grammar, prefix, answer, suffix, star, explanation, translation) in enumerate(Q, 1):
    assert len(answer) == 4, f"Q{i} {grammar} has {len(answer)} tokens"
    assert 1 <= star <= 4
    out.append({
        "id": i,
        "lesson": lesson,
        "prefix": prefix,
        "suffix": suffix,
        "answer": answer,
        "star": star,
        "grammar": grammar,
        "explanation": explanation,
        "translation": translation,
    })

target = os.path.join(os.path.dirname(__file__), "ordering-questions.json")
with open(target, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(out)} questions to {target}")
by_lesson = {}
for q in out:
    by_lesson.setdefault(q["lesson"], 0)
    by_lesson[q["lesson"]] += 1
for l in sorted(by_lesson):
    print(f"  Lesson {l}: {by_lesson[l]} questions")
