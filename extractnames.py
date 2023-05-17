text = """
#2   | Sleepteiner     | 65,434
#4   | WiMpN           | 44,484
#5   | Virgo           | 40,719
#6   | EEEEEEEEEEEEEEE | 39,972
#7   | Sure            | 36,758
#8   | WubWoofWolf     | 35,774
#9   | Alduric         | 34,423
#10  | TheShadowOfDark | 33,503
#11  | SS or Quit      | 32,969
#12  | vasasu          | 31,421
#13  | Sevelik         | 31,374
#14  | WorldChallenge  | 31,050
#15  | Sayonara Sakura | 29,230
#16  | Noercy          | 28,614
#17  | Patience        | 26,700
#18  | xasuma          | 25,216
#19  | Louis Marble    | 24,823
#20  | eralfehT        | 24,475
#21  | Nitry           | 23,004
#22  | seven39         | 22,666
#23  | Hammer          | 22,615
#24  | Duskyui         | 21,691
#26  | phionebaby56    | 20,980
#27  | Marquez         | 20,759
#28  | Genki1000       | 20,515
#29  | Namazu          | 20,440
#30  | Sowisty         | 20,180
#31  | Suwako          | 20,130
#33  | ImMyyrh         | 19,699
#35  | Wilchq          | 19,206
#36  | Andrea          | 18,844
#37  | Autumn Brightness | 18,680
#38  | P e n g u       | 18,584
#39  | _starry         | 18,419
#40  | Salamat         | 18,384
#41  | Suome           | 18,198
#42  | Torveld         | 18,126
#43  | WillCookie      | 18,104
#44  | Yuzyu           | 17,634
#45  | Ringtext        | 17,624
#46  | Azukane         | 17,516
#47  | Musa            | 16,924
#48  | Koltay          | 16,761
#50  | STS2            | 16,385
#51  | wiuuuh          | 16,380
#52  | Maklovitz       | 16,340
#53  | shun2yu         | 16,262
#54  | Mithrane        | 16,256
#55  | Hranolka        | 15,967
#56  | novaaa          | 15,629
#57  | SS is hard      | 15,557
#59  | [-Griffin-]     | 15,483
#60  | Kilgar          | 15,320
#61  | aya_nico        | 15,164
#63  | Aikyuu-Chan     | 14,726
#65  | Ma Yuyu         | 14,314
#66  | Amity-Senpai    | 13,986
#67  | Piro13          | 13,725
#69  | Emilily         | 13,600
#71  | boob enjoyer    | 13,190
#72  | Dakishimeru     | 13,181
#73  | iPhong          | 13,153
#74  | Vernien         | 13,046
#75  | Tactic          | 12,929
#76  | auroraflow12    | 12,681
#77  | -Purple         | 12,675
#79  | Psychicpsycho   | 12,409
#80  | Domi            | 12,395
#81  | Lokra           | 12,135
#83  | hent2222        | 11,995
#84  | Arx Alveria     | 11,992
#85  | Swakz           | 11,737
#86  | fjw             | 11,727
#87  | amea            | 11,700
#88  | 290ms           | 11,660
#89  | MomoPrecil      | 11,571
#90  | Naren           | 11,455
#91  | LosingCrayon    | 11,416
#92  | Chaoslitz       | 11,401
#93  | Xeanex          | 11,279
#94  | FuzimiyaYuki    | 11,239
#95  | Yurukane        | 11,008
#96  | Sipsu           | 10,822
#97  | CyberSylver     | 10,793
#98  | sanghaaaa       | 10,792
#99  | MystExiStentia  | 10,693
#100 | mashihunter     | 10,671
"""

lines = text.strip().split('\n')
names = [line.split('|')[1].strip() for line in lines]
print(names)
