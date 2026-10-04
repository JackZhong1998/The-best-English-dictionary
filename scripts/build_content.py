"""Turn the hand-authored compact entries below into the public JSON schema.

This is an editorial source file, not a model API client. Edit entries here, run
python3 scripts/build_content.py, then regenerate audio for changed examples.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEAD = {
    'break': ('/breɪk/', ['break'], ['打破', '中断', '休息'], '从“分开”延伸到状态或过程的中断。'),
    'call': ('/kɔːl/', ['call'], ['呼叫', '称作', '电话'], ''),
    'case': ('/keɪs/', ['case'], ['情况', '案件', '盒子'], ''),
    'change': ('/tʃeɪndʒ/', ['change'], ['改变', '更换', '零钱'], ''),
    'charge': ('/tʃɑːrdʒ/', ['charge'], ['收费', '充电', '负责', '指控'], ''),
    'come': ('/kʌm/', ['come'], ['来', '到达', '发生'], ''),
    'cut': ('/kʌt/', ['cut'], ['切', '减少', '中断'], ''),
    'draw': ('/drɔː/', ['draw'], ['画', '拉', '吸引', '平局'], ''),
    'drive': ('/draɪv/', ['drive'], ['驾驶', '驱动', '动力'], ''),
    'fall': ('/fɔːl/', ['fall'], ['落下', '下降', '秋天'], ''),
    'get': ('/ɡet/', ['get'], ['得到', '到达', '变得', '理解'], ''),
    'go': ('/ɡoʊ/', ['go'], ['去', '运行', '变得'], ''),
    'hold': ('/hoʊld/', ['hold'], ['拿住', '容纳', '举办', '保持'], ''),
    'keep': ('/kiːp/', ['keep'], ['保留', '保持', '继续'], ''),
    'leave': ('/liːv/', ['leave'], ['离开', '留下', '假期'], ''),
    'light': ('/laɪt/', ['light'], ['光', '灯', '轻的', '点燃'], ''),
    'line': ('/laɪn/', ['line'], ['线', '队伍', '台词', '线路'], ''),
    'make': ('/meɪk/', ['make'], ['制作', '使得', '赚钱', '赶上'], ''),
    'matter': ('/ˈmætər/', ['mat', 'ter'], ['重要', '事情', '物质'], ''),
    'move': ('/muːv/', ['move'], ['移动', '搬家', '感动', '行动'], ''),
    'order': ('/ˈɔːrdər/', ['or', 'der'], ['顺序', '命令', '点餐', '订单'], ''),
    'pass': ('/pæs/', ['pass'], ['经过', '通过', '传递', '消逝'], ''),
    'play': ('/pleɪ/', ['play'], ['玩', '比赛', '演奏', '扮演'], ''),
    'point': ('/pɔɪnt/', ['point'], ['点', '要点', '指向', '得分'], ''),
    'put': ('/pʊt/', ['put'], ['放', '表达', '推迟', '穿上'], ''),
    'right': ('/raɪt/', ['right'], ['正确', '右边', '权利', '立刻'], ''),
    'run': ('/rʌn/', ['run'], ['跑', '运行', '经营', '流动'], '从快速移动延伸到机器运转、液体流动和事务运行。'),
    'set': ('/set/', ['set'], ['放置', '设定', '一套', '凝固'], ''),
    'take': ('/teɪk/', ['take'], ['拿', '乘坐', '花费', '接受'], ''),
    'turn': ('/tɜːrn/', ['turn'], ['转动', '转向', '轮次', '变成'], ''),
}

# word|part of speech|English definition|Chinese definition|usage label|
# collocation~translation;...|example~translation;...
ROWS = """
break|v.|to separate into pieces|使某物分成碎片|打破或弄坏物品|break a cup~打碎杯子;break a window~打破窗户|I broke a glass.~我打碎了一个玻璃杯。;The toy broke yesterday.~玩具昨天坏了。
break|v.|to stop for a short time|短时间停止|中断活动或规则|break a rule~违反规则;break the silence~打破沉默|Please do not break the rules.~请不要违反规则。;A loud sound broke the silence.~一声巨响打破了寂静。
break|v.|to stop working properly|停止正常工作|机器或身体部位坏掉|break down~出故障;break a leg~摔断腿|Our car broke down.~我们的车坏了。;He broke his arm.~他摔断了胳膊。
break|n.|a short rest from work or study|工作或学习之间的短暂休息|休息一会儿|take a break~休息一下;coffee break~喝咖啡的休息时间|Let's take a break.~我们休息一下吧。;I need a short break.~我需要短暂休息。
call|v.|to speak loudly to someone|大声呼唤某人|喊叫或呼唤|call my name~喊我的名字;call for help~呼救|She called my name.~她喊了我的名字。;He called for help.~他大声呼救。
call|v.|to contact someone by phone|通过电话联系某人|打电话|call a friend~给朋友打电话;call back~回电话|I called my mother.~我给妈妈打了电话。;Please call me back.~请给我回电话。
call|v.|to give someone or something a name|给人或物起称呼|称作|call him Tom~叫他汤姆;call it a mistake~称之为错误|They call him Jack.~他们叫他杰克。;I call this a success.~我认为这算成功。
call|n.|a phone conversation|一次电话交谈|一通电话|make a call~打电话;miss a call~错过来电|I got a call from Dad.~我接到了爸爸的电话。;She missed my call.~她没接到我的电话。
case|n.|a particular situation|一种特定情况|情况或事例|in this case~在这种情况下;in many cases~在很多情况下|This is a special case.~这是一个特殊情况。;In this case, wait here.~在这种情况下，请在这里等。
case|n.|a matter investigated by police or a court|警方或法院调查的事情|案件|a murder case~谋杀案;solve a case~破案|The police solved the case.~警方破了这个案子。;This case is still open.~这个案子仍在调查中。
case|n.|a container for carrying or protecting things|装载或保护物品的容器|盒子或保护套|phone case~手机壳;glasses case~眼镜盒|My phone case is blue.~我的手机壳是蓝色的。;Put your glasses in the case.~把眼镜放进盒子里。
case|n.|a set of facts supporting a view|支持某种观点的一组事实|论据或理由|make a case~提出理由;a strong case~有力的理由|She made a strong case.~她提出了有力的理由。;His case sounds reasonable.~他的理由听起来合理。
change|v.|to become different|变得不同|发生变化|change quickly~迅速变化;change over time~随时间变化|The weather changed fast.~天气变得很快。;People change over time.~人会随着时间改变。
change|v.|to replace one thing with another|用另一物替换|更换|change clothes~换衣服;change a plan~改变计划|I changed my shirt.~我换了衬衫。;We changed our plan.~我们改了计划。
change|n.|a difference from what was before|与以前相比的差异|变化|a big change~巨大的变化;make a change~作出改变|This is a big change.~这是一个很大的变化。;We need a change.~我们需要改变。
change|n.|coins or money returned after payment|硬币或付款后找回的钱|零钱或找零|small change~零钱;keep the change~不用找零|Do you have any change?~你有零钱吗？;You can keep the change.~不用找零了。
charge|v.|to ask for money for a service or product|为商品或服务索要费用|收费|charge a fee~收取费用;charge ten dollars~收十美元|They charge ten dollars.~他们收费十美元。;This bank charges a fee.~这家银行收手续费。
charge|v.|to put electricity into a battery|把电能存入电池|给设备充电|charge a phone~给手机充电;charge a battery~给电池充电|I need to charge my phone.~我需要给手机充电。;The battery charges slowly.~电池充电很慢。
charge|v.|to accuse someone officially of a crime|正式指控某人犯罪|指控|charge someone with theft~指控某人盗窃;charge someone with a crime~指控某人犯罪|Police charged him with theft.~警方指控他盗窃。;She faced a serious charge.~她面临严重指控。
charge|n.|responsibility for someone or something|对人或事的责任|负责|in charge of~负责;take charge~接管|She is in charge of the shop.~她负责这家店。;Tom took charge today.~汤姆今天接手负责。
charge|n.|an amount of money that must be paid|必须支付的一笔钱|费用|service charge~服务费;extra charge~额外费用|There is no extra charge.~没有额外费用。;The service charge is small.~服务费很少。
come|v.|to move toward the speaker or a place|朝说话人或某地移动|来或到来|come here~到这里来;come home~回家|Please come here.~请到这里来。;She came home late.~她回家晚了。
come|v.|to reach a place or point|到达某处或某阶段|到达|come first~获得第一;come to an end~结束|Our team came first.~我们队得了第一。;The show came to an end.~演出结束了。
come|v.|to happen or become available|发生或出现|到来或出现|come soon~很快到来;come up~出现|Winter comes soon.~冬天快到了。;A new problem came up.~出现了一个新问题。
come|v.|to go with someone|与某人一起去|跟着来|come along~一起来;come with me~跟我来|Come along with us.~跟我们一起来吧。;Can you come with me?~你能跟我一起来吗？
cut|v.|to divide something with a sharp tool|用锋利工具切开某物|切或剪|cut bread~切面包;cut hair~剪头发|She cut the bread.~她切了面包。;I cut my hair yesterday.~我昨天剪了头发。
cut|v.|to make something shorter or smaller|使某物变短或变少|削减|cut costs~降低成本;cut the price~降价|We need to cut costs.~我们需要降低成本。;The shop cut the price.~商店降了价。
cut|v.|to interrupt or remove part of something|中断或删去一部分|切断或删去|cut off power~切断电源;cut a scene~删掉一个场景|They cut off the power.~他们切断了电源。;The editor cut the scene.~编辑删掉了那个场景。
cut|n.|a wound made by something sharp|尖锐物体造成的伤口|伤口|a small cut~小伤口;get a cut~划伤|I have a cut on my hand.~我手上有一道伤口。;The cut is not deep.~伤口不深。
draw|v.|to make a picture with a pen or pencil|用笔画图|画画|draw a picture~画一幅画;draw a map~画地图|She drew a cat.~她画了一只猫。;Please draw a line.~请画一条线。
draw|v.|to pull something toward you or in a direction|将某物拉向自己或某方向|拉或拖|draw the curtains~拉窗帘;draw a chair closer~把椅子拉近|He drew the curtains.~他拉上了窗帘。;She drew her chair closer.~她把椅子拉近了。
draw|v.|to attract people or attention|吸引人或注意力|吸引|draw a crowd~吸引人群;draw attention~引起注意|The music drew a crowd.~音乐吸引了一群人。;The sign drew my attention.~标志引起了我的注意。
draw|v.|to take money from an account|从账户取出钱|提取|draw money~取钱;draw cash~提取现金|I drew cash at the bank.~我在银行取了现金。;She drew some money today.~她今天取了一些钱。
draw|n.|a game with no winner|没有赢家的比赛|平局|end in a draw~以平局结束;a one-one draw~一比一平|The game ended in a draw.~比赛以平局结束。;It was a draw again.~又是一场平局。
drive|v.|to control a car or other vehicle|操控汽车或其他车辆|驾驶|drive a car~开车;drive to school~开车去学校|My dad drives a bus.~我爸爸开公交车。;I drive to work.~我开车上班。
drive|v.|to make someone or something move|促使人或物移动|驱赶或推动|drive cattle~赶牛;drive animals home~把动物赶回家|The farmer drove the cows home.~农夫把牛赶回家。;The wind drove the boat forward.~风推动小船前进。
drive|n.|a trip in a car|乘车出行的一段路|驾车行程|go for a drive~开车兜风;a long drive~长途驾驶|We went for a drive.~我们开车出去兜风。;It is a long drive.~开车要走很长一段路。
drive|n.|strong energy or determination|强烈的精力或决心|干劲或动力|strong drive~强烈动力;drive to win~获胜的决心|She has a strong drive to win.~她有强烈的获胜决心。;His drive helped the team.~他的干劲帮助了团队。
fall|v.|to move down to the ground|向下落到地面|掉落或摔倒|fall down~摔倒;fall off a bike~从自行车上摔下|The cup fell off the table.~杯子从桌上掉了下来。;He fell on the ice.~他在冰上摔倒了。
fall|v.|to become lower in amount or level|数量或水平降低|下降|prices fall~价格下降;fall sharply~急剧下降|The price fell today.~价格今天下降了。;Her voice fell to a whisper.~她的声音低成了耳语。
fall|v.|to enter a state or condition|进入某种状态|进入某种状态|fall asleep~睡着;fall ill~生病|The baby fell asleep.~宝宝睡着了。;He fell ill last week.~他上周生病了。
fall|n.|the season after summer|夏季之后的季节|秋天|in the fall~在秋天;last fall~去年秋天|School starts in the fall.~学校秋天开学。;Last fall was warm.~去年秋天很暖和。
get|v.|to receive or obtain something|收到或得到某物|得到|get a gift~收到礼物;get a job~找到工作|I got a letter today.~我今天收到一封信。;She got a new job.~她找到了一份新工作。
get|v.|to reach a place|到达某地|到达|get home~到家;get to school~到学校|We got home at six.~我们六点到家。;How did you get here?~你怎么到这里的？
get|v.|to become a particular way|变成某种状态|变得|get tired~累了;get cold~变冷|I get tired after work.~我下班后会累。;It gets cold at night.~晚上会变冷。
get|v.|to understand something|理解某事|明白|get the joke~听懂笑话;get the idea~明白意思|I don't get the joke.~我没听懂这个笑话。;Now I get it.~现在我明白了。
get|v.|to bring or buy something for someone|为某人拿来或购买某物|拿来或买来|get some water~拿些水;get a ticket~买票|Can you get me some water?~你能给我拿些水吗？;I got two tickets.~我买了两张票。
get|v.|to leave a place or vehicle|离开某地或交通工具|离开或下车|get out~出去;get off the bus~下公交车|We got off the bus.~我们下了公交车。;Please get out now.~请现在出去。
go|v.|to move or travel to another place|移动或前往另一个地方|去|go home~回家;go to school~去学校|I go to school by bus.~我坐公交车上学。;Let's go home.~我们回家吧。
go|v.|to leave a place|离开某地|走或离开|go now~现在走;go away~离开|I must go now.~我现在必须走了。;The bird went away.~鸟离开了。
go|v.|to happen in a particular way|以某种方式进行|进展|go well~进展顺利;go badly~进展不顺|The meeting went well.~会议进行得很顺利。;How did the exam go?~考试进行得怎么样？
go|v.|to become or turn into a state|进入某种状态|变得|go bad~变质;go quiet~安静下来|The milk went bad.~牛奶变质了。;The room went quiet.~房间安静下来了。
go|v.|to be suitable or match|适合或相配|搭配|go with~与……相配;go together~搭配得好|This shirt goes with your jeans.~这件衬衫和你的牛仔裤很搭。;Red and white go together.~红色和白色很搭。
hold|v.|to keep something in your hand|用手拿住某物|握住或拿着|hold a cup~拿着杯子;hold hands~牵手|Hold my hand.~牵着我的手。;She held a small box.~她拿着一个小盒子。
hold|v.|to contain a number of people or things|容纳一定数量的人或物|容纳|hold ten people~容纳十人;hold water~盛水|This room holds ten people.~这个房间容纳十人。;The bottle holds one liter.~这个瓶子装一升。
hold|v.|to organize an event|组织或举行活动|举办|hold a meeting~开会;hold a party~举办聚会|We held a meeting today.~我们今天开了会。;They held a party last night.~他们昨晚举办了聚会。
hold|v.|to keep something in a state or position|使某物维持状态或位置|保持|hold still~保持不动;hold the door open~扶住门让其开着|Please hold still.~请别动。;He held the door open.~他扶着门让它开着。
hold|v.|to wait for a short time|短暂等待|稍等|hold on~稍等;hold the line~别挂电话|Hold on a minute.~稍等一分钟。;Please hold the line.~请不要挂电话。
keep|v.|to have and not give away|保有而不交出|保留|keep a book~留着一本书;keep the change~不用找零|You can keep this book.~这本书你可以留着。;Please keep the change.~请不用找零。
keep|v.|to remain in a state|维持某种状态|保持|keep calm~保持冷静;keep warm~保暖|Keep calm, please.~请保持冷静。;This coat keeps me warm.~这件外套让我暖和。
keep|v.|to continue doing something|继续做某事|继续|keep going~继续前进;keep trying~继续尝试|Keep going!~继续加油！;She kept trying.~她一直在尝试。
keep|v.|to store something for later use|保存某物以备以后使用|存放或保存|keep food fresh~保持食物新鲜;keep a record~保存记录|I keep milk in the fridge.~我把牛奶放在冰箱里。;We keep a record of sales.~我们保存销售记录。
leave|v.|to go away from a place|从某地离开|离开|leave home~离家;leave early~早走|She left home at eight.~她八点离开家。;The train leaves soon.~火车快开了。
leave|v.|to put something somewhere and go away|把某物放在某处后离开|留下或遗忘|leave a bag~留下包;leave keys at home~把钥匙落在家里|I left my bag on the bus.~我把包落在公交车上了。;Please leave the book here.~请把书留在这里。
leave|v.|to allow something to stay as it is|让某物保持原样|留着不动|leave it alone~别碰它;leave the door open~让门开着|Leave the door open.~让门开着。;Please leave me alone.~请让我一个人待着。
leave|n.|time away from work with permission|经允许离开工作的时间|休假|take leave~请假;on leave~在休假|She is on leave this week.~她这周在休假。;He took leave for two days.~他请了两天假。
light|n.|brightness that lets you see|使人能看见的亮光|光线|bright light~强光;natural light~自然光|The light is too bright.~光太亮了。;Plants need light.~植物需要光。
light|n.|a lamp or another source of light|灯或其他发光物|灯|turn on the light~开灯;street light~路灯|Turn on the light, please.~请开灯。;The street lights are on.~路灯亮着。
light|adj.|not heavy|重量不大|轻的|a light bag~轻的包;light weight~轻重量|This bag is light.~这个包很轻。;The box feels light.~这个盒子拿起来很轻。
light|adj.|not strong or great in amount|强度或数量不大|轻微的或少量的|light rain~小雨;light meal~清淡的一餐|We had light rain today.~今天下了小雨。;I ate a light lunch.~我午饭吃得很清淡。
light|v.|to make something start burning|使某物开始燃烧|点燃|light a candle~点蜡烛;light a fire~生火|She lit a candle.~她点燃了一支蜡烛。;He lit the fire.~他生了火。
line|n.|a long narrow mark|细长的痕迹|线条|draw a line~画线;a straight line~直线|Draw a line here.~在这里画一条线。;The line is straight.~这条线是直的。
line|n.|a row of people waiting|排队等候的一排人|队伍|wait in line~排队;stand in line~站成一队|We waited in line.~我们排队等候。;The line is long today.~今天队伍很长。
line|n.|a sentence in a play or film|戏剧或电影中的一句话|台词|learn your lines~背台词;forget a line~忘记一句台词|She forgot her line.~她忘了台词。;He learned his lines.~他背会了台词。
line|n.|a route or connection for travel or communication|交通或通信的线路|线路|train line~铁路线;phone line~电话线|This train line is new.~这条铁路线是新的。;The phone line is busy.~电话占线。
make|v.|to create or produce something|制作或生产某物|制作|make a cake~做蛋糕;make a plan~制定计划|She made a cake.~她做了一个蛋糕。;We made a plan.~我们制订了计划。
make|v.|to cause someone or something to be a certain way|使人或物变成某种状态|使得|make me happy~使我开心;make it easy~使它简单|Your smile makes me happy.~你的笑容让我开心。;This map makes the trip easy.~这张地图让旅程变得简单。
make|v.|to earn money|赚取钱财|赚得|make money~赚钱;make a living~谋生|He makes money from music.~他靠音乐赚钱。;She makes a living by teaching.~她靠教书谋生。
make|v.|to reach something in time|及时赶上某事|赶上|make the train~赶上火车;make it on time~及时赶到|We made the train.~我们赶上了火车。;I made it on time.~我及时赶到了。
make|v.|to decide or choose something|作出决定或选择|作出|make a choice~作出选择;make a decision~作出决定|I made my choice.~我作出了选择。;She made a quick decision.~她很快作出了决定。
matter|v.|to be important|具有重要性|重要或有关系|matter a lot~很重要;does it matter~这重要吗|Your words matter.~你的话很重要。;It does not matter now.~现在这不重要。
matter|n.|a subject or situation|需要谈论或处理的事情|事情或问题|a serious matter~严重的事情;discuss the matter~讨论此事|This is a serious matter.~这是一件严重的事情。;We discussed the matter.~我们讨论了这件事。
matter|n.|physical material|有形的物质|物质|living matter~有生命的物质;solid matter~固体物质|Air is matter.~空气是物质。;Water is matter too.~水也是物质。
matter|n.|a problem or difficulty|出了问题的状况|麻烦或问题|what's the matter~怎么了;the matter with~……的问题|What's the matter?~怎么了？;What's the matter with your phone?~你的手机怎么了？
move|v.|to change position or place|改变位置或地点|移动|move a chair~移动椅子;move slowly~慢慢移动|Please move the chair.~请挪一下椅子。;The car moved slowly.~车缓慢地移动。
move|v.|to change your home|更换住处|搬家|move house~搬家;move to Beijing~搬到北京|We moved last year.~我们去年搬家了。;She moved to Beijing.~她搬到了北京。
move|v.|to make someone feel a strong emotion|使某人产生强烈感情|感动|move someone deeply~深深打动某人;be moved by~被……感动|The story moved me.~这个故事打动了我。;Her song moved us.~她的歌感动了我们。
move|n.|an action or a change of position|一次动作或位置改变|动作或行动|make a move~采取行动;next move~下一步行动|It's your move now.~现在轮到你走棋了。;We need to make a move.~我们需要采取行动。
order|n.|the arrangement of things in a sequence|事物排列的先后方式|顺序|in order~按顺序;word order~语序|Put the numbers in order.~把数字按顺序排好。;The words are in the wrong order.~这些词的顺序错了。
order|v.|to ask for food or goods|要求提供食物或商品|点餐或订购|order lunch~点午餐;order online~网上订购|I ordered a sandwich.~我点了一个三明治。;She ordered a book online.~她在网上订了一本书。
order|n.|a request for food or goods|购买食物或商品的请求|订单|place an order~下订单;check an order~核对订单|I placed an order yesterday.~我昨天下了订单。;Your order is ready.~你的订单准备好了。
order|v.|to tell someone to do something with authority|以权威口吻要求某人做事|命令|order someone to leave~命令某人离开;order a stop~下令停止|The teacher ordered us to stop.~老师命令我们停下。;The officer ordered him to leave.~那名官员命令他离开。
order|n.|a state in which things are organized and controlled|事物井然有序的状态|秩序|keep order~维持秩序;in good order~井然有序|The room is in good order.~房间井然有序。;The teacher kept order in class.~老师维持了课堂秩序。
pass|v.|to move past someone or something|从某人或某物旁边经过|经过|pass a house~经过一栋房子;pass by~经过|We passed the school.~我们经过了学校。;A bus passed by.~一辆公交车驶过。
pass|v.|to succeed in a test|通过考试或测验|通过考试|pass a test~通过考试;pass an exam~考试及格|She passed the test.~她通过了测验。;I passed my driving exam.~我通过了驾照考试。
pass|v.|to give something to another person|把某物交给别人|传递|pass the salt~递盐;pass a note~传纸条|Please pass the salt.~请把盐递给我。;He passed me the ball.~他把球传给了我。
pass|v.|to come to an end or go by|结束或流逝|过去|time passes~时间流逝;the day passes~一天过去|Time passes quickly.~时间过得很快。;The pain passed soon.~疼痛很快就过去了。
pass|n.|a ticket or document giving permission|允许通行的票证|通行证或票卡|bus pass~公交乘车卡;visitor pass~访客通行证|I bought a bus pass.~我买了一张公交乘车卡。;Show your visitor pass.~请出示访客通行证。
play|v.|to do something for fun|为了乐趣做某事|玩耍|play outside~在外面玩;play with toys~玩玩具|The children play outside.~孩子们在外面玩。;She plays with her dog.~她和狗玩。
play|v.|to take part in a game or sport|参加游戏或运动|比赛|play soccer~踢足球;play a game~玩游戏|We play soccer after school.~我们放学后踢足球。;They played a game together.~他们一起玩了一个游戏。
play|v.|to perform music on an instrument|用乐器演奏音乐|演奏|play the piano~弹钢琴;play a song~演奏一首歌|He plays the piano.~他弹钢琴。;She played a short song.~她演奏了一首短曲。
play|v.|to act as a character|扮演一个角色|扮演|play a doctor~扮演医生;play the main role~出演主角|She plays a doctor in the film.~她在电影里扮演医生。;He played the main role.~他出演了主角。
play|n.|a story performed on a stage|在舞台上演出的故事|戏剧|watch a play~看戏;a school play~学校话剧|We watched a play last night.~我们昨晚看了一出戏。;The school play was funny.~学校话剧很有趣。
point|n.|an exact place or position|一个确切的位置|点或位置|a point on a map~地图上的一点;starting point~起点|Mark the point on the map.~在地图上标出那个点。;This is our starting point.~这是我们的起点。
point|n.|an important idea or detail|重要的想法或细节|要点|main point~主要观点;get the point~明白要点|I understand your point.~我明白你的观点。;The main point is clear.~主要意思很清楚。
point|v.|to show a direction with a finger or object|用手指或物体示意方向|指向|point at~指着;point to~指向|She pointed at the door.~她指着门。;The arrow points left.~箭头指向左边。
point|n.|a unit of a score|分数的一个单位|得分|score a point~得一分;five points~五分|Our team scored a point.~我们队得了一分。;She has five points.~她得了五分。
point|n.|a particular moment or stage|某个特定时刻或阶段|时候或阶段|at this point~此时;the halfway point~中途的位置|At this point, we stopped.~这时我们停了下来。;We are at the halfway point.~我们走到一半了。
put|v.|to place something somewhere|把某物放在某处|放置|put a book on the table~把书放在桌上;put away~收起来|Put the cup here.~把杯子放在这里。;She put away her toys.~她收起了玩具。
put|v.|to express something in words|用语言表达某事|表达|put it simply~简单地说;put into words~用语言表达|Let me put it simply.~让我简单地说。;I can't put it into words.~我无法用语言表达。
put|v.|to move an event to a later time|把活动移到较晚时间|推迟|put off a meeting~推迟会议;put off work~推迟工作|We put off the meeting.~我们推迟了会议。;She put off her trip.~她推迟了旅行。
put|v.|to place clothing on your body|把衣物穿到身上|穿上|put on a coat~穿上外套;put on shoes~穿鞋|Put on your coat.~穿上你的外套。;He put on his shoes.~他穿上了鞋。
put|v.|to connect someone to another person by phone|通过电话把某人与另一个人接通|电话转接|put someone through~给某人转接;put me through~给我转接|Please put me through to Amy.~请帮我转接给艾米。;The operator put us through.~接线员帮我们接通了电话。
right|adj.|correct or true|正确或符合事实|正确的|right answer~正确答案;get it right~答对|Your answer is right.~你的答案是对的。;I got it right.~我答对了。
right|adj.|on the side opposite the left|在左侧相反的一边|右边的|right hand~右手;right side~右侧|Raise your right hand.~举起你的右手。;The shop is on the right side.~商店在右边。
right|n.|something you are allowed to do or have|被允许做或拥有的事|权利|have the right~有权利;human rights~人权|You have the right to ask.~你有权提问。;Everyone has basic rights.~每个人都有基本权利。
right|adv.|immediately or exactly|立刻或恰好|立刻或正好|right now~现在立刻;right here~就在这里|Come here right now.~现在立刻过来。;The key is right here.~钥匙就在这里。
right|n.|the direction opposite left|与左相反的方向|右方|turn right~向右转;on the right~在右边|Turn right at the corner.~在路口右转。;The bank is on the right.~银行在右边。
run|v.|to move quickly on foot|用双脚快速移动|奔跑|run fast~跑得快;run to school~跑去学校|I run every morning.~我每天早上跑步。;The dog ran across the yard.~狗跑过院子。
run|v.|to work or function|机器或程序正常运转|运行|run smoothly~运行顺畅;run on batteries~靠电池运行|The clock runs on batteries.~这个钟靠电池运行。;The program runs well.~这个程序运行良好。
run|v.|to manage an activity or business|管理活动或企业|经营或管理|run a shop~经营商店;run a class~开办课程|They run a small shop.~他们经营一家小店。;She runs an English class.~她开办一门英语课。
run|v.|to flow in a direction|液体朝某个方向流动|流动|water runs~水流动;run down~向下流|Water ran down the wall.~水沿着墙流下来。;Her tears ran down her face.~眼泪顺着她的脸流下来。
run|v.|to become used up|某物逐渐用完|用尽|run out of milk~牛奶用完;run out of time~时间不够|We ran out of milk.~我们的牛奶用完了。;I ran out of time.~我的时间用完了。
run|n.|a period of running for exercise|一段跑步锻炼|跑步|go for a run~去跑步;morning run~晨跑|I went for a run.~我去跑步了。;Our morning run was short.~我们的晨跑很短。
set|v.|to put something in a particular place|把某物放在特定位置|放置|set the table~摆餐具;set a cup down~放下杯子|She set the cup on the table.~她把杯子放在桌上。;Please set the table.~请摆好餐具。
set|v.|to decide or fix a value, time, or rule|确定数值、时间或规则|设定|set a time~定时间;set a goal~定目标|We set a time for the meeting.~我们定了开会时间。;He set a new goal.~他定了一个新目标。
set|v.|to adjust a device to a value|把设备调到某个数值|调节|set an alarm~设闹钟;set the temperature~设定温度|I set my alarm for seven.~我把闹钟设在七点。;Set the oven to 180 degrees.~把烤箱调到 180 度。
set|n.|a group of things used together|一起使用的一组东西|一套|a set of keys~一串钥匙;a tea set~一套茶具|I lost my set of keys.~我丢了一串钥匙。;This tea set is old.~这套茶具很旧。
set|v.|to become firm or solid|变得坚硬或凝固|凝固|the paint sets~油漆干固;the jelly sets~果冻凝固|The paint sets in an hour.~油漆一小时后干固。;The jelly has set.~果冻已经凝固了。
take|v.|to pick up and carry something|拿起并带走某物|拿或带走|take a bag~拿一个包;take it home~把它带回家|Take your bag with you.~带上你的包。;She took the book home.~她把书带回家了。
take|v.|to travel by a form of transport|乘坐某种交通工具|乘坐|take a bus~坐公交车;take a train~坐火车|I take the bus to school.~我坐公交车上学。;We took a train yesterday.~我们昨天坐了火车。
take|v.|to need a period of time|需要一段时间|花费时间|take an hour~花一小时;take time~花时间|The trip takes an hour.~这段旅程要花一小时。;This work takes time.~这项工作需要时间。
take|v.|to accept or receive something|接受或收到某物|接受|take a gift~接受礼物;take advice~听取建议|She took the gift.~她收下了礼物。;I took his advice.~我听取了他的建议。
take|v.|to remove clothing from the body|从身上脱下衣物|脱下|take off a coat~脱下外套;take off shoes~脱鞋|Please take off your coat.~请脱下外套。;He took off his shoes.~他脱下了鞋。
take|v.|to leave the ground and begin to fly|离开地面开始飞行|起飞|a plane takes off~飞机起飞;take off on time~准时起飞|The plane took off at noon.~飞机中午起飞了。;Our flight took off late.~我们的航班起飞晚了。
turn|v.|to move around a central point|围绕中心旋转|转动|turn a key~转钥匙;turn a wheel~转车轮|Turn the key slowly.~慢慢转动钥匙。;The wheel turns fast.~轮子转得很快。
turn|v.|to change direction|改变前进方向|转向|turn left~向左转;turn around~转身|Turn left at the bank.~在银行那里左转。;She turned around quickly.~她迅速转过身。
turn|v.|to become a new color or state|变成新的颜色或状态|变成|turn red~变红;turn cold~变冷|The leaves turn red in fall.~树叶在秋天变红。;The water turned cold.~水变凉了。
turn|n.|a chance to do something in a sequence|轮到做某事的机会|轮次|your turn~轮到你;take turns~轮流|It's your turn now.~现在轮到你了。;We take turns at the game.~我们轮流玩这个游戏。
turn|n.|a change in direction|方向的一次改变|转弯|take a turn~转弯;a sharp turn~急转弯|Take the next turn.~在下一个路口转弯。;The road has a sharp turn.~这条路有个急转弯。
break|v.|to end a relationship|结束一段关系|分手|break up~分手;break up with someone~和某人分手|They broke up last month.~他们上个月分手了。;She broke up with Tom.~她和汤姆分手了。
break|v.|to enter a place by force|强行进入某处|闯入|break into a house~闯入房屋;break in~强行进入|Someone broke into our house.~有人闯进了我们家。;A thief broke in last night.~昨晚有小偷闯入。
call|v.|to cancel a planned event|取消计划好的活动|取消|call off a game~取消比赛;call off a meeting~取消会议|They called off the game.~他们取消了比赛。;We called off the meeting.~我们取消了会议。
call|v.|to need or demand something|需要某物|需要|call for help~需要帮助;call for action~要求行动|This job calls for patience.~这份工作需要耐心。;The problem calls for action.~这个问题需要采取行动。
case|n.|a possible event or situation|可能发生的情况|以防某种情况|in case of rain~如果下雨;just in case~以防万一|Take an umbrella just in case.~带把伞以防万一。;In case of rain, stay inside.~如果下雨，就待在室内。
change|v.|to start believing or deciding something different|改变原先的想法或决定|改变主意|change your mind~改变主意;change a decision~改变决定|I changed my mind.~我改变了主意。;She changed her decision.~她改变了决定。
come|v.|to return to a place|回到某地|回来|come back soon~快点回来;come back home~回家来|Please come back soon.~请快点回来。;He came back at night.~他晚上回来了。
come|v.|to have a particular origin|来自某个地方|来自|come from China~来自中国;come from a farm~来自农场|She comes from Shanghai.~她来自上海。;This milk comes from a farm.~这牛奶来自一家农场。
cut|v.|to stop eating or using something|停止食用或使用某物|戒掉或减少|cut out sugar~不吃糖;cut out snacks~不吃零食|I cut out sugar last month.~我上个月戒了糖。;She cut out late snacks.~她不再吃夜宵了。
draw|v.|to reach an idea after thinking|思考后得出想法|得出结论|draw a conclusion~得出结论;draw a lesson~吸取教训|We drew a simple conclusion.~我们得出了一个简单的结论。;She drew a lesson from it.~她从中吸取了教训。
drive|v.|to make a machine or process work|为机器或过程提供动力|驱动|drive a machine~驱动机器;drive growth~推动增长|Electricity drives this machine.~电力驱动这台机器。;New ideas drive change.~新想法推动改变。
fall|v.|to fail to keep pace|跟不上进度|落后|fall behind~落后;fall behind in class~在课堂上落后|He fell behind in class.~他在课堂上落后了。;Our team fell behind early.~我们队早早落后了。
fall|v.|to begin to love someone|开始爱上某人|爱上|fall in love~恋爱;fall in love with~爱上|They fell in love.~他们相爱了。;She fell in love with him.~她爱上了他。
get|v.|to enter a vehicle|进入交通工具|上车|get on the bus~上公交车;get in a car~上汽车|Get on the bus now.~现在上公交车。;She got in the car.~她上了车。
get|v.|to return to a place|回到某地|回来|get back home~回到家;get back soon~快点回来|I got back late.~我回来晚了。;When did you get back?~你什么时候回来的？
get|v.|to recover from illness or trouble|从疾病或困难中恢复|克服或恢复|get over a cold~感冒痊愈;get over a loss~从失落中走出来|She got over her cold.~她的感冒好了。;He got over the loss.~他从失落中走了出来。
get|v.|to have a friendly relationship|与人友好相处|相处融洽|get along well~相处得好;get along with~与……相处|They get along well.~他们相处得很好。;I get along with my sister.~我和姐姐相处得很好。
go|v.|to continue or happen|继续或进行|继续|go on~继续;go on with work~继续工作|The show went on.~演出继续了。;Please go on with your work.~请继续你的工作。
go|v.|to stop shining or working|灯光或电源停止工作|熄灭|the lights go out~灯灭;power goes out~停电|The lights went out.~灯灭了。;The power went out last night.~昨晚停电了。
hold|v.|to keep someone or something from moving forward|阻止人或物前进|阻挡|hold back tears~忍住眼泪;hold back a crowd~拦住人群|She held back her tears.~她忍住了眼泪。;The fence held back the crowd.~栅栏挡住了人群。
keep|v.|to continue at the same level or speed|保持同样的水平或速度|跟上|keep up~跟上;keep up with~跟上……|Keep up with the class.~跟上全班进度。;I can't keep up.~我跟不上。
leave|v.|to not include someone or something|没有把人或物算进去|遗漏|leave out a word~漏掉一个词;leave someone out~不让某人参与|You left out one word.~你漏掉了一个词。;They left me out.~他们没有让我参加。
light|adj.|pale in color|颜色较浅|浅色的|light blue~浅蓝色;light green~浅绿色|The wall is light blue.~墙是浅蓝色的。;I like light green.~我喜欢浅绿色。
line|v.|to form a row|排成一行|排队|line up~排队;line up outside~在外面排队|Please line up here.~请在这里排队。;The children lined up outside.~孩子们在外面排队。
make|v.|to invent a story or excuse|编造故事或借口|编造|make up a story~编造故事;make up an excuse~编借口|He made up a story.~他编了一个故事。;She made up an excuse.~她编了一个借口。
make|v.|to do something good to balance a bad thing|用好事弥补坏事|弥补|make up for a mistake~弥补错误;make up for lost time~补回失去的时间|I made up for my mistake.~我弥补了自己的错误。;We made up for lost time.~我们补回了耽误的时间。
move|v.|to stop thinking about the past and continue|不再停留于过去而继续前进|继续前进|move on~向前看;move on from~走出……|It's time to move on.~该向前看了。;She moved on after the loss.~失去之后她继续向前。
pass|v.|to die|去世|去世|pass away~去世;pass away peacefully~安详离世|His grandfather passed away.~他的祖父去世了。;She passed away peacefully.~她安详地离世了。
play|v.|to make recorded sound or video start|让录制的声音或视频开始播放|播放|play music~播放音乐;play a video~播放视频|Please play the song.~请播放这首歌。;The video played twice.~这个视频播放了两次。
point|v.|to tell someone about a fact or problem|让某人注意到事实或问题|指出|point out a mistake~指出错误;point out a fact~指出事实|She pointed out my mistake.~她指出了我的错误。;He pointed out the sign.~他指了指那个标志。
put|v.|to accept an unpleasant thing|忍受不愉快的事|忍受|put up with noise~忍受噪音;put up with pain~忍受疼痛|I can't put up with this noise.~我受不了这噪音。;She put up with the pain.~她忍受了疼痛。
right|adj.|suitable for a purpose or person|适合某用途或某人的|合适的|right size~合适的尺码;right time~合适的时间|This is the right size.~这是合适的尺码。;Now is the right time.~现在是合适的时间。
run|v.|to meet someone by chance|偶然遇见某人|偶遇|run into a friend~偶遇朋友;run into someone~碰见某人|I ran into an old friend.~我偶遇了一位老朋友。;She ran into her teacher.~她碰见了老师。
run|v.|to leave quickly to escape|快速离开以逃脱|逃跑|run away~逃跑;run away from danger~逃离危险|The dog ran away.~那只狗跑走了。;They ran away from danger.~他们逃离了危险。
set|v.|to start or arrange something|建立或安排某事|建立|set up a club~成立俱乐部;set up a meeting~安排会议|We set up a new club.~我们成立了一个新俱乐部。;She set up a meeting.~她安排了一次会议。
take|v.|to remove something from a place|把某物从某处移走|拿走|take away a plate~拿走盘子;take away rubbish~带走垃圾|Please take away the plates.~请把盘子拿走。;He took the rubbish away.~他把垃圾带走了。
take|v.|to gain control of something|取得某物的控制权|接管|take over a business~接管企业;take over a job~接手工作|She took over the shop.~她接管了商店。;I took over his job.~我接手了他的工作。
take|v.|to happen|发生|发生|take place today~今天发生;take place here~在这里举行|The meeting takes place today.~会议今天举行。;The event took place here.~活动在这里举行。
take|v.|to look after someone or something|照顾某人或某物|照顾|take care of a child~照顾孩子;take care of a pet~照顾宠物|She takes care of her son.~她照顾儿子。;I take care of the cat.~我照顾这只猫。
turn|v.|to start a device or light|启动设备或灯|打开|turn on a light~开灯;turn on a TV~打开电视|Turn on the light.~把灯打开。;He turned on the TV.~他打开了电视。
turn|v.|to stop a device or light|停止设备或灯|关掉|turn off a light~关灯;turn off a phone~关手机|Please turn off the light.~请把灯关掉。;She turned off her phone.~她关掉了手机。
turn|v.|to refuse an offer or request|拒绝提议或请求|拒绝|turn down an offer~拒绝提议;turn down a request~拒绝请求|He turned down the offer.~他拒绝了那份提议。;She turned down my request.~她拒绝了我的请求。
"""


def parse_rows():
    by_word = {word: [] for word in HEAD}
    for line in ROWS.strip().splitlines():
        word, pos, en_def, zh_def, label, collocs, examples = line.split('|')
        usage = {
            'usage_label': label,
            'collocations': [dict(zip(('phrase', 'translation'), item.split('~'))) for item in collocs.split(';')],
            'examples': [dict(zip(('en', 'zh'), item.split('~'))) for item in examples.split(';')],
        }
        by_word[word].append({
            'id': len(by_word[word]) + 1,
            'part_of_speech': pos,
            'en_definition': en_def,
            'zh_definition': zh_def,
            'usages': [usage],
            'synonyms': [],
            'antonyms': [],
            'confusables': [],
        })
    for word, senses in by_word.items():
        if not senses:
            raise ValueError(f'No senses for {word}')
        phonetic, syllables, core, shift = HEAD[word]
        entry = {
            'word': word,
            'phonetic': phonetic,
            'syllables': syllables,
            'pos': list(dict.fromkeys(sense['part_of_speech'] for sense in senses)),
            'core_meanings': core,
            'etymology': '',
            'semantic_shift': shift,
            'senses': senses,
        }
        target = ROOT / 'content' / 'words' / f'{word}.json'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(entry, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    parse_rows()
