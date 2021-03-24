print('遊戲解說:本遊戲分飽足感、含水量及快樂指數，遊戲的起始直接為3，遊戲總共分10局，一局代表1年，當快樂指數低於0時，貓咪會離家出走，當含水量跟飽足感低於0時，貓咪會得腎臟疾病及飢餓，這會影響快樂指數，同時當飽足感或含水量高於7時會得心血管疾病或水中毒，這也會影響快樂指數。當飲食指數低於-4或高於11時會直接導致死亡。')
print('本次遊戲遊玩時每局會分配4個遊戲資源，而每個資源都能造成1.5倍的各項能力成長')
print('最後預祝遊戲體驗愉快')
import sys
import random
original_water=3
original_food=3
original_mood=3

class food_and_water_and_mood():    
       
    def __init__(self,water,food,mood):
        self.water=water
        self.food=food
        self.mood=mood
        
    def toPrint(self,water,food,mood):
        self.water+= water
        self.food += food
        self.mood+=mood
        
        print('第',i+1,'年')


        a=0
        
        random_situation=random.randint(1,50)
        if random_situation==1 or random_situation==2 or random_situation==3 or random_situation==4 or random_situation==5 or random_situation==6 or random_situation==7 or random_situation==8 or random_situation==9 or random_situation==10 or random_situation==11or random_situation==12 or random_situation==13 or random_situation==14 or random_situation==15 or random_situation==16 or random_situation==17or random_situation==18 or random_situation==19 or random_situation==20:
            print('今年是平靜的一年，沒有特別的是發生。')
        elif random_situation==21 or random_situation==22 or random_situation==23 or random_situation==24 or random_situation==25:
            print('你的貓咪今天在路上抓到一隻老鼠，飽餐了一頓，又享受狩獵的快感。(飽足感+1，快樂指數+1)')
            self.food+=1
            self.mood+=1
        elif random_situation==26 or random_situation==27 or random_situation==28 or random_situation==29 or random_situation==30:
            print('你的貓咪在路上看到一另隻異性的貓咪，從其 中眼神你看得出溢滿的愛慕之情。')
            a=input()
            keep_other_cat=str(input('請問你同意收養此貓嗎?:'))
            if keep_other_cat=='yes' or keep_other_cat=='同意' or keep_other_cat=='是的' or keep_other_cat=='是的，我同意' :
                print('你的貓心情很好，快樂指數+1')
                self.mood+=2
            elif keep_other_cat=='no' or keep_other_cat=='不同意' or keep_other_cat=='否' or keep_other_cat=='不，我不同意':
                print('你的貓跟另一隻野種私奔了!!!')
                a=input()
                print('遊戲結束，你失敗了')
                sys.exit(0)
            else:
                print('貓咪是一種非常有智慧的生物，想當然爾牠聽得懂人話')
                a=input()
                print('雖然你今天沒有答應貓貓可以帶牠的愛慕者回家')
                a=input()
                print('但牠當你太笨，聽不懂高貴的語言，心生憐憫，決定放你一馬')
                a=input()
                print('因此甚麼事都沒發生')
        elif random_situation==31 or random_situation==32 or random_situation==33 or random_situation==34 or random_situation==35:
            print('貓貓今日被卡在樹上下不來')
            a=input()
            print('雖然經奴才護駕之後已安全落地，但感覺顏面無光，因此心情低落(快樂指數-2.5)')
            a=input()
            self.mood-=2.5
        elif random_situation==36 or random_situation==37 or random_situation==38 or random_situation==39 or random_situation==40:
            print('貓貓今日被狗追')
            a=input()
            print('後來發現狗只是想跟牠玩，但貓貓被整隻吞到狗的嘴巴裡再吐出來，全身都是口水')
            a=input()
            print('雖然沒有受傷，但汙辱性極強，而且被追得很累，因此心情低落+口乾+巴肚夭(快樂指數-3.5，含水度-2，飽足感-2)')
            self.mood-=3.5
            self.food-=2
            self.water-=2
        elif random_situation==41 :
            print('你家的貓貓品格高尚，被綠燈戒指選中，成為了保護地球的綠燈俠(綠燈戰警)，並加入了正義聯盟')
            a=input()
            print('遊戲過關(解鎖 綠燈俠)')
            sys.exit(0)
        elif random_situation==42:
            print('芮•天行者發現你的貓貓原力蟲的數量超高，決定收他為絕地學徒')
            a=input()
            print('最後你的貓貓憑藉著萬年難得一件的天賦成為了一代絕地宗師')
            a=input()
            print('遊戲過關(解鎖 STAR WARS)')
            sys.exit(0)
        elif random_situation==43 :
            print('你家隔壁一個名為"豆豆"的小孩打開一個封印妖怪的罐子，因此你家的貓貓被要怪附身')
            a=input()
            print('最後貓貓把你賣掉了')
            a=input()
            print('遊戲結束，你被賣掉了(解鎖 魔法阿嬤)')
            sys.exit(0)
        elif random_situation==44:
            print('你發現你家貓貓最近不太對勁')
            a=input()
            print('經過你最近的跟蹤後，你發現家裡有一間你之前從未發現的密室')
            a=input()
            print('同時你發現一些人類的殘骸')
            a=input()
            print('震驚之餘，你沒有發現牠已經繞到你的後方')
            a=input()
            print('你:##@%##%//@，R~R~R~~~!!!')
            a=input()
            print('你被乙醚迷昏了')
            a=input()
            print('醒來之後你發現被綁在椅子上')
            a=input()
            print('接著牠切開你的腦袋，並掀開你的頭蓋骨')
            a=input()
            print('牠拿出一支湯匙')
            a=input()
            print('一口')
            a=input()
            print('接著一口')
            a=input()
            print('你被迫吃下自己的腦袋')
            a=input()
            print('最後，在迷茫之際，你迎向了死亡')
            a=input()
            print('遊戲結束，你吃掉了自己的腦袋(解鎖 人魔)')
            sys.exit(0)
        elif random_situation==45:
            print('台灣為了與聖雅利安國建交，決定批准在你家旁邊蓋化工廠')
            a=input()
            print('為了保護貓皇優良的居住環境，你當選立委決心與政府對抗到底')
            a=input()
            print('不料立法院中有立委得到了聖亞利安國的特殊狂犬病病毒，轉生成了殭屍')
            a=input()
            print('1. 指甲剪  2.鐵鎚  3.國產T91')
            a=input()
            zombie_wapon_chose=int(input('請選擇武器(請輸入代號):'))
            
            if zombie_wapon_chose==1: 
                print('憑藉著你平常幫喵皇剪貓指甲的功夫，你精準的剪爆殭屍的頸動脈')
                a=input()
                print('最後你帶著你的貓貓一起從秘密出口逃出立法院(經過一番逃跑，貓貓的含水度-2、飽足感-2)')
                a=input()
                print('解鎖 逃出立法院')                   
                self.food-=2
                self.water-=2
            elif zombie_wapon_chose==2:
                print('你槌子沒揮好，踉蹌了一步，摔倒在地')
                a=input()
                print('此時貓貓護主心切，與殭屍群展開了對決')
                a=input()
                print('奈何殭屍群數量太多，你們一起被撕成碎肉塊了')
                a=input()
                print('遊戲結束，你跟貓貓都被撕碎了(解鎖 逃出立法院)')
                sys.exit(0)
            else:
             print('你隨手抄起一把農兵部隊的國產T91')
             a=input()
             print('國產T91:噠噠噠~')
             a=input()
             print('國產T91:噠噠噠~')
             a=input()
             print('國產T91:噠噠噠~喀')
             a=input()
             print('你:欸~~')
             a=input()
             print('國產T91:喀~喀喀喀')
             a=input()
             print('國產T91處理殭屍群的效率極高，奈何子彈總有打光的一天')
             a=input()
             print('遊戲結束，你跟貓貓都被撕碎了(解鎖 逃出立法院)')
             sys.exit(0)
        elif random_situation==46:
            print('魯霸•海格在一個風雨交加的夜晚破門而入闖入你的家')
            a=input()
            print('魯霸•海格:Yoy are a wizard,kitty.')
            a=input()
            print('你的貓貓成為了史上第一個就讀霍格華茲魔法與巫術學院的貓咪')
            a=input()
            print('1. 純黑色貓，狡猾  2.銀灰色貓，聰明  3.橘色虎斑貓，勇敢  4.大花貓，天真富好奇心')
            a=input()
            harry_chose=int(input('請選擇你貓咪的個性與特性(請輸入代號):'))
            if harry_chose==1: 
                print('你的貓貓進入史萊哲林學院，最後成為一代黑巫師，殘暴程度更勝當年的佛地魔，在英國掀起一陣腥風血雨')
                a=input()
                print('最後，你死在你的貓貓施展的索命咒底下')
                a=input()
                print('遊戲結束 (解鎖 哈利波特)')                   
                sys.exit(0)
            elif harry_chose==2:
                print('你的貓貓進入雷文克勞學院，成為英國魔法部史上第一個貓咪職員')
                a=input()
                print('最後還當上英國魔法部部長')
                a=input()
                print('遊戲結束 (解鎖 哈利波特)')
                sys.exit(0)
            elif harry_chose==3:
                print('你的貓貓進入葛來分多學院，成為古靈閣雇用的第一個貓咪解咒師')
                a=input()
                print('遊戲結束 (解鎖 哈利波特)')
                sys.exit(0)
            else:
                print('你的貓貓進入赫夫帕夫學院，最後成為英國魔法部史上第一個貓咪職員，但在處理一次業務的過程中被會咬人的茶壺活活咬死')
                a=input()
                print('遊戲結束 (解鎖 哈利波特)')
                sys.exit(0)
        elif random_situation==47:
            print('你的貓咪習得中國古拳法')
            a=input()
            print('最終在比賽時用無敵風火輪打敗斷水流大師兄(心情+2)')
            self.mood+=2
            
        elif random_situation==48:
            print('壽司店推出明子內有"鮭魚免費招待壽司特別企劃"')
            a=input()
            print('你在店門前跟店員盧了半個鐘頭堅持自己的貓也叫"鮭魚"，期望能蹭到免費的一頓飯')
            random_fish=random.randint(1,3)
            if random_fish==1: 
                print('你蹭到免錢的飯，貓貓也飽餐了一頓(飽足感+3)')
                a=input()
                print('解鎖 鮭魚之亂')
                self.food+=3
            else:
                print('你沒能蹭到免錢的飯，貓貓覺得這個厚顏無恥的主人感到羞恥(快樂指數-5)')
                a=input()
                print('解鎖 鮭魚之亂')
                self.mood-=5
        elif random_situation==49:
            print('你將貓貓放進了一個有毒氣開關的封閉盒子內')
            random_physic=random.randint(1,2)
            if random_physic==1: 
                print('你打開盒子，貓貓還活著')
                a=input()
                print('解鎖 薛丁格的貓')
            else:
                print('你打開盒子，你家貓貓死透了')
                a=input()
                print('解鎖 薛丁格的貓')
                sys.exit(0)
        else:
            print('你的貓貓坐在你開的跑車上出去兜風，在加油站加油時三個混混跟你買車不成殺到你家搶走你的車、殺了你的貓')
            a=input()
            print('你敲碎你家地下室的地板，拿出大量的槍械跟殺手金幣')
            a=input()
            print('最後你幹掉了大半個俄羅斯黑幫')
            a=input()
            print('遊戲結束 解鎖 捍衛任務')
            sys.exit(0)
             
             
         
                



        
        if self.water<=0 and self.water>-4:
            print('你的貓咪得到腎臟疾病')
            self.mood-=3.5
        if self.water>=7:
            print('你的貓咪水中毒')
            self.mood-=3.5
        if self.water<=-4:
            print('你的貓咪被你活活渴死了')
            sys.exit(0)
        if self.water>=11:
            print('你的貓咪水量攝取過多，在貓生的最後階段飽受生體放電異常而死')
            sys.exit(0)
        if self.food<=0:
            print('你的貓咪在哭夭，心情金賣')
            self.mood-=3.5
        if self.food>=7:
            print('你的貓咪罹患心血管相關疾病，現在很痛苦，心情金賣')
            self.mood-=3.5
        if self.food<=-4:
            print('你的貓咪被你活活餓死了')
            sys.exit(0)
        if self.food>=11:
            print('你的貓咪罹患的心血管疾病已經病入膏肓，屍體被發現暴斃在餵食器皿前方')
            sys.exit(0)
        if self.mood<=0:
            print('你的貓咪討厭你這個奴僕，所以牠離家出走了')
                  
            sys.exit(0)
        
        if i==9:
            print('你的貓過完快了的一生，最後陽壽已盡，安祥的離開貓世')
        print('現在的含水度:',self.water,'    ','現在的飽足感:',self.food,' ','現在的快樂指數:',self.mood)

        print('================================================') 
        

        

original_food_and_water_and_mood=food_and_water_and_mood(original_water,original_food,original_mood)

for i in range(10):
    
    Water=int(input("請決定要給予你的寵物幾份水(資源有限，請謹慎決定): "))  
    Food=int(input("請決定要給予你的寵物幾份食物(資源有限，請謹慎決定): "))
    Mood=int(input("請決定要給予你的寵物多少資源來陪牠玩(資源有限，請謹慎決定): "))
    
        
   
    while Water+Food+Mood>4:
        print('基礎資源只有四份，請做有效分配')
        Water= int(input("請決定要給予你的寵物幾份水(資源有限，請謹慎決定): "))
        Food=int(input("請決定要給予你的寵物幾份食物(資源有限，請謹慎決定): "))
        Mood=int(input("請決定要給予你的寵物多少資源來陪牠玩(資源有限，請謹慎決定): "))
    Water=Water*1.5
    Food=Food*1.5
    Mood=Mood*1.5
    if Mood==1.5:
        Food-=1
        Water-=1
    elif Mood==3:
        Food-=2
        Water-=2
    elif Mood==4.5:
        Food-=3
        Water-=3
    elif Mood==6:
        Food-=4
        Water-=4
    if Water==0 and Food==0 and Mood==0:
        Water-=0.5
        Food-=0.5
        Mood-=1.5
    if Mood==0:
        Mood-=2.5

        
    original_food_and_water_and_mood.toPrint(Water,Food,Mood)


