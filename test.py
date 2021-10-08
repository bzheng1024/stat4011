import requests
from bs4 import BeautifulSoup
import time
import csv
import re


soup = BeautifulSoup(
    '''		<div class="GameItemList">
					<div class="GameItemWrap">
	<div class="GameItem Lose  "
	     data-summoner-id="135515503"
	     data-game-time="1633650361"
	     data-game-id="5496136563"
	     data-game-result="lose"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633650361' data-type='' data-interval='60'>2021-10-08 08:46:01</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											失败									</div>
									<div class="GameLength">22分 54秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/lucian/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Lucian.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="圣枪游侠"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerExhaust.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;虚弱&lt;/b&gt;&lt;br&gt;&lt;span&gt;虚弱目标敌方英雄，降低其30%的移动速度，并使其造成的伤害减少40%，持续3秒。&lt;/span&gt;" alt="虚弱">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8005.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;强攻&lt;/b&gt;&lt;br&gt;&lt;span&gt;用3次连续的普攻命中一名敌方英雄时，将造成40 - 180的额外&lt;lol-uikit-tooltipped-keyword key=&#039;LinkTooltip_Description_AdaptiveDmg&#039;&gt;&lt;font color=&#039;#48C4B7&#039;&gt;自适应伤害&lt;/font&gt;&lt;/lol-uikit-tooltipped-keyword&gt;（基于等级）并使其进入易损状态，让其所受的来自任意来源的伤害提升8 - 12%，持续6秒。&lt;/span&gt;" alt="强攻">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/lucian/statistics" target="_blank">圣枪游侠</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">2</span> /
					<span class="Death">5</span> /
					<span class="Assist">3</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">1.00:1</span> KDA				</div>
																								</div>
			<div class="Stats">
				<div class="Level">
					等级12
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 173  + 野怪 4&lt;br&gt;每分钟CS7.7个">177 (7.7)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  42%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Grandmaster</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/6672.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;海妖杀手&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;65&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;25%&lt;/attention&gt;攻击速度&lt;br&gt;&lt;attention&gt;20%&lt;/attention&gt;暴击几率&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;放倒它：&lt;/passive&gt; 每第三次攻击造成额外的&lt;trueDamage&gt;(60+45%额外攻击力)真实伤害&lt;/trueDamage&gt;。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;10%&lt;/attention&gt;攻击速度。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;3400 (625)&lt;/span&gt;" alt="海妖杀手">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3508.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;夺萃之镰&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;45&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;20%&lt;/attention&gt;暴击几率&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;咒刃：&lt;/passive&gt;施放技能后，你的下一次普通攻击会因强化而附带额外的&lt;physicalDamage&gt;100%基础攻击力 + 40%额外攻击力的物理伤害&lt;/physicalDamage&gt;&lt;OnHit&gt;攻击特效&lt;/OnHit&gt;并回复相当于40%该伤害值的法力值(1.5秒冷却时间)。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2800 (400)&lt;/span&gt;" alt="夺萃之镰">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3006.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;狂战士胫甲&lt;/b&gt;&lt;br&gt;&lt;span&gt;增强移动速度和攻击速度&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;35%&lt;/attention&gt;攻击速度&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (500)&lt;/span&gt;" alt="狂战士胫甲">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3363.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;远见改造&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升施放距离并揭示目标区域&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;显形4000码内的一个区域并放置一个可见且脆弱的守卫。友军无法将这个守卫作为召唤师技能或技能的目标&lt;scaleLevel&gt;(198 - 99秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="远见改造">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/1018.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;灵巧披风&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升暴击几率&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;15%&lt;/attention&gt;暴击几率&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;600 (600)&lt;/span&gt;" alt="灵巧披风">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/1055.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;多兰之刃&lt;/b&gt;&lt;br&gt;&lt;span&gt;普攻型英雄的优秀起始装备&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;8&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;80&lt;/attention&gt;生命值&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;好战者：&lt;/passive&gt;获得&lt;lifeSteal&gt;2.5%全能吸血&lt;/lifeSteal&gt;。&lt;br&gt;&lt;br&gt;&lt;rules&gt;在造成群体伤害或通过宠物造成伤害时，全能吸血只有33%效能。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;450 (450)&lt;/span&gt;" alt="多兰之刃">
													</div>
																							<div class="Item">
															<div class="Image NoItem"></div>
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-red.png">
												Control Ward <span class='wards vision'>1</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-100 tip" title="放逐之刃">放逐之刃</div>
								<div class="Image20 __sprite __spc20 __spc20-100 tip" title="放逐之刃">放逐之刃</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=distant+star" class="Link" target='_blank'>distant star</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-60 tip" title="永猎双子">永猎双子</div>
								<div class="Image20 __sprite __spc20 __spc20-60 tip" title="永猎双子">永猎双子</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=2021Worlds" class="Link" target='_blank'>2021Worlds</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-6 tip" title="冰晶凤凰">冰晶凤凰</div>
								<div class="Image20 __sprite __spc20 __spc20-6 tip" title="冰晶凤凰">冰晶凤凰</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=nakreB+v2" class="Link" target='_blank'>nakreB v2</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-106 tip" title="星籁歌姬">星籁歌姬</div>
								<div class="Image20 __sprite __spc20 __spc20-106 tip" title="星籁歌姬">星籁歌姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Veignorennn" class="Link" target='_blank'>Veignorennn</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-94 tip" title="幻翎">幻翎</div>
								<div class="Image20 __sprite __spc20 __spc20-94 tip" title="幻翎">幻翎</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=xCharm" class="Link" target='_blank'>xCharm</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-0 tip" title="暗裔剑魔">暗裔剑魔</div>
								<div class="Image20 __sprite __spc20 __spc20-0 tip" title="暗裔剑魔">暗裔剑魔</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Venour" class="Link" target='_blank'>Venour</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-95 tip" title="披甲龙龟">披甲龙龟</div>
								<div class="Image20 __sprite __spc20 __spc20-95 tip" title="披甲龙龟">披甲龙龟</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=BR+Lord+Semi" class="Link" target='_blank'>BR Lord Semi</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-102 tip" title="符文法师">符文法师</div>
								<div class="Image20 __sprite __spc20 __spc20-102 tip" title="符文法师">符文法师</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=deepbIackdemon" class="Link" target='_blank'>deepbIackdemon</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-68 tip" title="圣枪游侠">圣枪游侠</div>
								<div class="Image20 __sprite __spc20 __spc20-68 tip" title="圣枪游侠">圣枪游侠</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
								<div class="Image20 __sprite __spc20 __spc20-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Efias" class="Link" target='_blank'>Efias</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
															<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-198 Off"></span>
								<span class="__spSite __spSite-197 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Lose  "
	     data-summoner-id="135515503"
	     data-game-time="1633648592"
	     data-game-id="5496153164"
	     data-game-result="lose"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633648592' data-type='' data-interval='60'>2021-10-08 08:16:32</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											失败									</div>
									<div class="GameLength">30分 28秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/kaisa/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Kaisa.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="虚空之女"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerExhaust.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;虚弱&lt;/b&gt;&lt;br&gt;&lt;span&gt;虚弱目标敌方英雄，降低其30%的移动速度，并使其造成的伤害减少40%，持续3秒。&lt;/span&gt;" alt="虚弱">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/9923.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;丛刃&lt;/b&gt;&lt;br&gt;&lt;span&gt;在攻击敌方英雄时，提供110%攻击速度给最先的3次攻击。&lt;br&gt;&lt;br&gt;每次攻击的间隔不能超过3秒，否则这个效果就会结束。&lt;br&gt;&lt;br&gt;冷却时间：12秒。&lt;br&gt;&lt;br&gt;&lt;rules&gt;被重置的攻击会使攻击次数上限提升1。&lt;br&gt;&lt;br&gt;允许你暂时溢出你的攻击速度上限。&lt;/rules&gt;&lt;/span&gt;" alt="丛刃">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/kaisa/statistics" target="_blank">虚空之女</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">4</span> /
					<span class="Death">7</span> /
					<span class="Assist">6</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">1.43:1</span> KDA				</div>
																								</div>
			<div class="Stats">
				<div class="Level">
					等级14
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 204  + 野怪 8&lt;br&gt;每分钟CS7个">212 (7)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  34%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Master</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3085.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;卢安娜的飓风&lt;/b&gt;&lt;br&gt;&lt;span&gt;远程攻击会对目标身边的2个敌人发射弩箭&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;45%&lt;/attention&gt;攻击速度&lt;br&gt;&lt;attention&gt;20%&lt;/attention&gt;暴击几率&lt;br&gt;&lt;attention&gt;7%&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;风怒：&lt;/passive&gt;你的普通攻击会朝目标附近的至多2个敌人发射弩箭，每支弩箭造成&lt;physicalDamage&gt;(40%攻击力)物理伤害&lt;/physicalDamage&gt;。这些弩箭能够附带攻击特效并且可以暴击。&lt;br&gt;&lt;br&gt;&lt;rules&gt;这件装备仅远程英雄可用。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2600 (950)&lt;/span&gt;" alt="卢安娜的飓风">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/1018.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;灵巧披风&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升暴击几率&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;15%&lt;/attention&gt;暴击几率&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;600 (600)&lt;/span&gt;" alt="灵巧披风">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/6676.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;收集者&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;55&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;20%&lt;/attention&gt;暴击几率&lt;br&gt;&lt;attention&gt;12&lt;/attention&gt;穿甲&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;死与税：&lt;/passive&gt;如果你造成的伤害将使一名敌方英雄的生命值跌到5%以下，那么会直接将其处决。击杀英雄时会为你提供额外的25金币。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;3000 (425)&lt;/span&gt;" alt="收集者">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3363.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;远见改造&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升施放距离并揭示目标区域&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;显形4000码内的一个区域并放置一个可见且脆弱的守卫。友军无法将这个守卫作为召唤师技能或技能的目标&lt;scaleLevel&gt;(198 - 99秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="远见改造">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/6672.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;海妖杀手&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;65&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;25%&lt;/attention&gt;攻击速度&lt;br&gt;&lt;attention&gt;20%&lt;/attention&gt;暴击几率&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;放倒它：&lt;/passive&gt; 每第三次攻击造成额外的&lt;trueDamage&gt;(60+45%额外攻击力)真实伤害&lt;/trueDamage&gt;。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;10%&lt;/attention&gt;攻击速度。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;3400 (625)&lt;/span&gt;" alt="海妖杀手">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3006.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;狂战士胫甲&lt;/b&gt;&lt;br&gt;&lt;span&gt;增强移动速度和攻击速度&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;35%&lt;/attention&gt;攻击速度&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (500)&lt;/span&gt;" alt="狂战士胫甲">
													</div>
																							<div class="Item">
															<div class="Image NoItem"></div>
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-red.png">
												Control Ward <span class='wards vision'>3</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-76 tip" title="齐天大圣">齐天大圣</div>
								<div class="Image20 __sprite __spc20 __spc20-76 tip" title="齐天大圣">齐天大圣</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Goldguns88" class="Link" target='_blank'>Goldguns88</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-92 tip" title="元素女皇">元素女皇</div>
								<div class="Image20 __sprite __spc20 __spc20-92 tip" title="元素女皇">元素女皇</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=JUNGKING1" class="Link" target='_blank'>JUNGKING1</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-118 tip" title="解脱者">解脱者</div>
								<div class="Image20 __sprite __spc20 __spc20-118 tip" title="解脱者">解脱者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Viikingr" class="Link" target='_blank'>Viikingr</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-68 tip" title="圣枪游侠">圣枪游侠</div>
								<div class="Image20 __sprite __spc20 __spc20-68 tip" title="圣枪游侠">圣枪游侠</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=pewpawpewpew" class="Link" target='_blank'>pewpawpewpew</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
								<div class="Image20 __sprite __spc20 __spc20-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=mad+on+pixels" class="Link" target='_blank'>mad on pixels</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-47 tip" title="未来守护者">未来守护者</div>
								<div class="Image20 __sprite __spc20 __spc20-47 tip" title="未来守护者">未来守护者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=David+Nalbandian" class="Link" target='_blank'>David Nalbandian</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-39 tip" title="战争之影">战争之影</div>
								<div class="Image20 __sprite __spc20 __spc20-39 tip" title="战争之影">战争之影</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Win+or+Valhalla" class="Link" target='_blank'>Win or Valhalla</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-63 tip" title="诡术妖姬">诡术妖姬</div>
								<div class="Image20 __sprite __spc20 __spc20-63 tip" title="诡术妖姬">诡术妖姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=GS+Bolulu" class="Link" target='_blank'>GS Bolulu</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-50 tip" title="虚空之女">虚空之女</div>
								<div class="Image20 __sprite __spc20 __spc20-50 tip" title="虚空之女">虚空之女</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-4 tip" title="牛头酋长">牛头酋长</div>
								<div class="Image20 __sprite __spc20 __spc20-4 tip" title="牛头酋长">牛头酋长</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Reu" class="Link" target='_blank'>Reu</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																										<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-198 Off"></span>
								<span class="__spSite __spSite-197 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Win  "
	     data-summoner-id="135515503"
	     data-game-time="1633646133"
	     data-game-id="5496060609"
	     data-game-result="win"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633646133' data-type='' data-interval='60'>2021-10-08 07:35:33</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											胜利									</div>
									<div class="GameLength">25分 17秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/rell/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Rell.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="镕铁少女"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;引燃&lt;/b&gt;&lt;br&gt;&lt;span&gt;引燃是对单体敌方目标施放的持续性伤害技能，在5秒的持续时间里造成70-410（取决于英雄等级）真实伤害，获得目标的视野，并减少目标所受的治疗和回复效果。&lt;/span&gt;" alt="引燃">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8439.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;余震&lt;/b&gt;&lt;br&gt;&lt;span&gt;在定身住一名敌方英雄后，使你的护甲和魔法抗性提升35+你80%的额外双抗，持续2.5秒。随后会爆炸，对附近的敌人造成魔法伤害。&lt;br&gt;&lt;br&gt;伤害值：25 - 120 (+你8%的额外生命值)&lt;br&gt;冷却时间：20秒&lt;br&gt;&lt;br&gt;来自余震的双抗加成封顶值：80-150(基于等级)&lt;br&gt;&lt;/span&gt;" alt="余震">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/rell/statistics" target="_blank">镕铁少女</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">1</span> /
					<span class="Death">5</span> /
					<span class="Assist">10</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">2.20:1</span> KDA				</div>
																								</div>
			<div class="Stats">
				<div class="Level">
					等级12
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 36  + 野怪 0&lt;br&gt;每分钟CS1.4个">36 (1.4)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  44%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Master</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3860.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;山脉壁垒&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;20&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;250&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础生命回复&lt;br&gt;&lt;attention&gt;3&lt;/attention&gt;金币/10秒&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存0个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt; &lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存4个侦察守卫，并在访问商店时补满。 &lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="山脉壁垒">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3190.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;钢铁烈阳之匣&lt;/b&gt;&lt;br&gt;&lt;span&gt;主动施放来为附近友军提供吸收伤害的护盾&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;护甲&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;魔法抗性&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;虔诚：&lt;/active&gt;为附近友军提供&lt;shield&gt;230 - 385(基于友军等级)护盾&lt;/shield&gt;，在2.5秒里持续衰减(90秒冷却时间)。&lt;br&gt;&lt;li&gt;&lt;passive&gt;奉献：&lt;/passive&gt;为附近友方英雄提供&lt;scaleArmor&gt;5护甲&lt;/scaleArmor&gt;和&lt;scaleMR&gt;魔法抗性&lt;/scaleMR&gt;。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;2&lt;/attention&gt;护甲/魔法抗性加成至&lt;passive&gt;奉献&lt;/passive&gt;。&lt;br&gt;&lt;br&gt;&lt;rules&gt;加成效果的强度是基于该友方英雄的等级。&lt;br&gt;20秒内的后续&lt;active&gt;奉献&lt;/active&gt;的护盾仅有25%效果。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2500 (200)&lt;/span&gt;" alt="钢铁烈阳之匣">
													</div>
																							<div class="Item">
															<div class="Image NoItem"></div>
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3364.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;神谕透镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;持续期间可瘫痪附近隐形的守卫和陷阱&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;扫描你的周围，预警隐藏的敌方单位，并使隐形的陷阱显形，并使附近的敌方侦察守卫显形(并暂时失效)10秒&lt;scaleLevel&gt;(90 - 60秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="神谕透镜">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3067.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;燃烧宝石&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升生命值和冷却缩减&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;10&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;800 (400)&lt;/span&gt;" alt="燃烧宝石">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3111.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;水银之靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升移动速度并降低限制效果的时长&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;25&lt;/attention&gt;魔法抗性&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;br&gt;&lt;attention&gt;30%&lt;/attention&gt;韧性&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;rules&gt;韧性会减少&lt;status&gt;晕眩&lt;/status&gt;、&lt;status&gt;减速&lt;/status&gt;、&lt;status&gt;嘲讽&lt;/status&gt;、&lt;status&gt;恐惧&lt;/status&gt;、&lt;status&gt;沉默&lt;/status&gt;、&lt;status&gt;致盲&lt;/status&gt;、&lt;status&gt;变形&lt;/status&gt;和&lt;status&gt;定身&lt;/status&gt;效果的持续时间。它对&lt;status&gt;浮空&lt;/status&gt;或&lt;status&gt;压制&lt;/status&gt;效果无效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (350)&lt;/span&gt;" alt="水银之靴">
													</div>
																							<div class="Item">
															<div class="Image NoItem"></div>
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildblue-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildblue-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-blue.png">
												Control Ward <span class='wards vision'>10</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-37 tip" title="法外狂徒">法外狂徒</div>
								<div class="Image20 __sprite __spc20 __spc20-37 tip" title="法外狂徒">法外狂徒</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Nice+Guy+Ben" class="Link" target='_blank'>Nice Guy Ben</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-90 tip" title="圣锤之毅">圣锤之毅</div>
								<div class="Image20 __sprite __spc20 __spc20-90 tip" title="圣锤之毅">圣锤之毅</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Expecto+Patrounm" class="Link" target='_blank'>Expecto Patrounm</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-121 tip" title="岩雀">岩雀</div>
								<div class="Image20 __sprite __spc20 __spc20-121 tip" title="岩雀">岩雀</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Ryuin" class="Link" target='_blank'>Ryuin</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-50 tip" title="虚空之女">虚空之女</div>
								<div class="Image20 __sprite __spc20 __spc20-50 tip" title="虚空之女">虚空之女</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=devil+in+details" class="Link" target='_blank'>devil in details</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-94 tip" title="幻翎">幻翎</div>
								<div class="Image20 __sprite __spc20 __spc20-94 tip" title="幻翎">幻翎</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=W0jti" class="Link" target='_blank'>W0jti</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-101 tip" title="机械公敌">机械公敌</div>
								<div class="Image20 __sprite __spc20 __spc20-101 tip" title="机械公敌">机械公敌</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=masked+gamer+XD" class="Link" target='_blank'>masked gamer XD</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-92 tip" title="元素女皇">元素女皇</div>
								<div class="Image20 __sprite __spc20 __spc20-92 tip" title="元素女皇">元素女皇</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=JUNGKING1" class="Link" target='_blank'>JUNGKING1</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-3 tip" title="影哨">影哨</div>
								<div class="Image20 __sprite __spc20 __spc20-3 tip" title="影哨">影哨</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=SL0WDEATH" class="Link" target='_blank'>SL0WDEATH</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-140 tip" title="机械先驱">机械先驱</div>
								<div class="Image20 __sprite __spc20 __spc20-140 tip" title="机械先驱">机械先驱</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=ManoloGap+ad+acc" class="Link" target='_blank'>ManoloGap ad acc</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-97 tip" title="镕铁少女">镕铁少女</div>
								<div class="Image20 __sprite __spc20 __spc20-97 tip" title="镕铁少女">镕铁少女</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																										<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-194 Off"></span>
								<span class="__spSite __spSite-193 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Lose  "
	     data-summoner-id="135515503"
	     data-game-time="1633643514"
	     data-game-id="5495965130"
	     data-game-result="lose"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633643514' data-type='' data-interval='60'>2021-10-08 06:51:54</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											失败									</div>
									<div class="GameLength">24分 9秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/leona/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Leona.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="曙光女神"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;引燃&lt;/b&gt;&lt;br&gt;&lt;span&gt;引燃是对单体敌方目标施放的持续性伤害技能，在5秒的持续时间里造成70-410（取决于英雄等级）真实伤害，获得目标的视野，并减少目标所受的治疗和回复效果。&lt;/span&gt;" alt="引燃">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8439.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;余震&lt;/b&gt;&lt;br&gt;&lt;span&gt;在定身住一名敌方英雄后，使你的护甲和魔法抗性提升35+你80%的额外双抗，持续2.5秒。随后会爆炸，对附近的敌人造成魔法伤害。&lt;br&gt;&lt;br&gt;伤害值：25 - 120 (+你8%的额外生命值)&lt;br&gt;冷却时间：20秒&lt;br&gt;&lt;br&gt;来自余震的双抗加成封顶值：80-150(基于等级)&lt;br&gt;&lt;/span&gt;" alt="余震">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/leona/statistics" target="_blank">曙光女神</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">2</span> /
					<span class="Death">8</span> /
					<span class="Assist">10</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">1.50:1</span> KDA				</div>
																								</div>
			<div class="Stats">
				<div class="Level">
					等级11
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 26  + 野怪 0&lt;br&gt;每分钟CS1.1个">26 (1.1)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  50%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Master</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3857.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;白岩肩铠&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;15&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;250&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础生命回复&lt;br&gt;&lt;attention&gt;3&lt;/attention&gt;金币/10秒&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存0个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt; &lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存4个侦察守卫，并在访问商店时补满。 &lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="白岩肩铠">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3190.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;钢铁烈阳之匣&lt;/b&gt;&lt;br&gt;&lt;span&gt;主动施放来为附近友军提供吸收伤害的护盾&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;护甲&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;魔法抗性&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;虔诚：&lt;/active&gt;为附近友军提供&lt;shield&gt;230 - 385(基于友军等级)护盾&lt;/shield&gt;，在2.5秒里持续衰减(90秒冷却时间)。&lt;br&gt;&lt;li&gt;&lt;passive&gt;奉献：&lt;/passive&gt;为附近友方英雄提供&lt;scaleArmor&gt;5护甲&lt;/scaleArmor&gt;和&lt;scaleMR&gt;魔法抗性&lt;/scaleMR&gt;。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;2&lt;/attention&gt;护甲/魔法抗性加成至&lt;passive&gt;奉献&lt;/passive&gt;。&lt;br&gt;&lt;br&gt;&lt;rules&gt;加成效果的强度是基于该友方英雄的等级。&lt;br&gt;20秒内的后续&lt;active&gt;奉献&lt;/active&gt;的护盾仅有25%效果。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2500 (200)&lt;/span&gt;" alt="钢铁烈阳之匣">
													</div>
																							<div class="Item">
															<div class="Image NoItem"></div>
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3364.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;神谕透镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;持续期间可瘫痪附近隐形的守卫和陷阱&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;扫描你的周围，预警隐藏的敌方单位，并使隐形的陷阱显形，并使附近的敌方侦察守卫显形(并暂时失效)10秒&lt;scaleLevel&gt;(90 - 60秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="神谕透镜">
															</div>
																							<div class="Item">
															<div class="Image NoItem"></div>
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3047.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;铁板靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;增强移动速度并减少即将到来的普攻伤害&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;20&lt;/attention&gt;护甲&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;br&gt;&lt;li&gt;使即将到来的攻击伤害降低12%。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (500)&lt;/span&gt;" alt="铁板靴">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3067.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;燃烧宝石&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升生命值和冷却缩减&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;10&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;800 (400)&lt;/span&gt;" alt="燃烧宝石">
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-red.png">
												Control Ward <span class='wards vision'>13</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-107 tip" title="腕豪">腕豪</div>
								<div class="Image20 __sprite __spc20 __spc20-107 tip" title="腕豪">腕豪</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=HUNGRY+IRL+" class="Link" target='_blank'>HUNGRY IRL </a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-27 tip" title="痛苦之拥">痛苦之拥</div>
								<div class="Image20 __sprite __spc20 __spc20-27 tip" title="痛苦之拥">痛苦之拥</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Lotus+%CE%94+%CE%A8" class="Link" target='_blank'>Lotus Δ Ψ</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-128 tip" title="蛮族之王">蛮族之王</div>
								<div class="Image20 __sprite __spc20 __spc20-128 tip" title="蛮族之王">蛮族之王</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=MuteAllToChalle" class="Link" target='_blank'>MuteAllToChalle</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-8 tip" title="残月之肃">残月之肃</div>
								<div class="Image20 __sprite __spc20 __spc20-8 tip" title="残月之肃">残月之肃</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Ukranian" class="Link" target='_blank'>Ukranian</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-5 tip" title="殇之木乃伊">殇之木乃伊</div>
								<div class="Image20 __sprite __spc20 __spc20-5 tip" title="殇之木乃伊">殇之木乃伊</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=xCharm" class="Link" target='_blank'>xCharm</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-38 tip" title="灵罗娃娃">灵罗娃娃</div>
								<div class="Image20 __sprite __spc20 __spc20-38 tip" title="灵罗娃娃">灵罗娃娃</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=23iko" class="Link" target='_blank'>23iko</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-66 tip" title="含羞蓓蕾">含羞蓓蕾</div>
								<div class="Image20 __sprite __spc20 __spc20-66 tip" title="含羞蓓蕾">含羞蓓蕾</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=FB+Rames" class="Link" target='_blank'>FB Rames</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-148 tip" title="封魔剑魂">封魔剑魂</div>
								<div class="Image20 __sprite __spc20 __spc20-148 tip" title="封魔剑魂">封魔剑魂</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=BabaGandalf" class="Link" target='_blank'>BabaGandalf</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-23 tip" title="荣耀行刑官">荣耀行刑官</div>
								<div class="Image20 __sprite __spc20 __spc20-23 tip" title="荣耀行刑官">荣耀行刑官</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=666+reverse+999" class="Link" target='_blank'>666 reverse 999</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-65 tip" title="曙光女神">曙光女神</div>
								<div class="Image20 __sprite __spc20 __spc20-65 tip" title="曙光女神">曙光女神</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
															<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-198 Off"></span>
								<span class="__spSite __spSite-197 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Lose  "
	     data-summoner-id="135515503"
	     data-game-time="1633641379"
	     data-game-id="5495959210"
	     data-game-result="lose"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633641379' data-type='' data-interval='60'>2021-10-08 06:16:19</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											失败									</div>
									<div class="GameLength">20分 51秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/sett/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Sett.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="腕豪"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;引燃&lt;/b&gt;&lt;br&gt;&lt;span&gt;引燃是对单体敌方目标施放的持续性伤害技能，在5秒的持续时间里造成70-410（取决于英雄等级）真实伤害，获得目标的视野，并减少目标所受的治疗和回复效果。&lt;/span&gt;" alt="引燃">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8439.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;余震&lt;/b&gt;&lt;br&gt;&lt;span&gt;在定身住一名敌方英雄后，使你的护甲和魔法抗性提升35+你80%的额外双抗，持续2.5秒。随后会爆炸，对附近的敌人造成魔法伤害。&lt;br&gt;&lt;br&gt;伤害值：25 - 120 (+你8%的额外生命值)&lt;br&gt;冷却时间：20秒&lt;br&gt;&lt;br&gt;来自余震的双抗加成封顶值：80-150(基于等级)&lt;br&gt;&lt;/span&gt;" alt="余震">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/sett/statistics" target="_blank">腕豪</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">4</span> /
					<span class="Death">3</span> /
					<span class="Assist">5</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">3.00:1</span> KDA				</div>
																							<div class="Badge"><span class="Text ACE">ACE</span></div>
												</div>
			<div class="Stats">
				<div class="Level">
					等级11
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 41  + 野怪 0&lt;br&gt;每分钟CS2个">41 (2)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  69%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Grandmaster</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3857.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;白岩肩铠&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;15&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;250&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础生命回复&lt;br&gt;&lt;attention&gt;3&lt;/attention&gt;金币/10秒&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存0个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt; &lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存4个侦察守卫，并在访问商店时补满。 &lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="白岩肩铠">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/6664.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;涡轮炼金罐&lt;/b&gt;&lt;br&gt;&lt;span&gt;定身敌人以获得一层护盾。激活以更快跑向敌人。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;350&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;25&lt;/attention&gt;护甲&lt;br&gt;&lt;attention&gt;25&lt;/attention&gt;魔法抗性&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;极限超载：&lt;/active&gt;在朝着敌方英雄或敌方防御塔移动时会提供&lt;speed&gt;40%移动速度&lt;/speed&gt;，持续4秒。一旦贴近一名敌方英雄(或在4秒后)，你就会放出一道冲击波，使附近敌方英雄&lt;status&gt;减速&lt;/status&gt;50%，持续1.5秒(90秒冷却时间)。&lt;br&gt;&lt;li&gt;&lt;passive&gt;献祭：&lt;/passive&gt;承受或造成伤害时会使你开始每秒对附近敌人造成&lt;magicDamage&gt;(12~30 (基于等级) + 1%额外生命值)魔法伤害&lt;/magicDamage&gt;(对小兵提升25%，对野怪提升150%)，持续3秒。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得 &lt;attention&gt;5&lt;/attention&gt;技能急速&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2800 (950)&lt;/span&gt;" alt="涡轮炼金罐">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2055.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;控制守卫&lt;/b&gt;&lt;br&gt;&lt;span&gt;用来使范围内的守卫和隐形陷阱失效。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 消耗：&lt;/active&gt;放置一个强大的控制守卫来提供附近区域的视野。这个设备还会使&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;的陷阱显形，使&lt;keywordStealth&gt;伪装&lt;/keywordStealth&gt;的敌人们显形，并使敌方守卫显形和失效。 &lt;br&gt;&lt;br&gt;&lt;rules&gt;你至多可以携带2个控制守卫。控制守卫不会使其它控制守卫失效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;75 (75)&lt;/span&gt;" alt="控制守卫">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3364.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;神谕透镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;持续期间可瘫痪附近隐形的守卫和陷阱&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;扫描你的周围，预警隐藏的敌方单位，并使隐形的陷阱显形，并使附近的敌方侦察守卫显形(并暂时失效)10秒&lt;scaleLevel&gt;(90 - 60秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="神谕透镜">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2420.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;秒表&lt;/b&gt;&lt;br&gt;&lt;span&gt;主动施放来变得无敌但无法行动&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - &lt;/active&gt; &lt;active&gt;凝滞：&lt;/active&gt;一次性使用，在2.5秒里&lt;status&gt;免疫伤害&lt;/status&gt;且&lt;status&gt;不可被选取&lt;/status&gt;，但在此期间里无法采取任何其它行动(转变为一个&lt;rarityGeneric&gt;破损的秒表&lt;/rarityGeneric&gt;)。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;650 (650)&lt;/span&gt;" alt="秒表">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3111.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;水银之靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升移动速度并降低限制效果的时长&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;25&lt;/attention&gt;魔法抗性&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;br&gt;&lt;attention&gt;30%&lt;/attention&gt;韧性&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;rules&gt;韧性会减少&lt;status&gt;晕眩&lt;/status&gt;、&lt;status&gt;减速&lt;/status&gt;、&lt;status&gt;嘲讽&lt;/status&gt;、&lt;status&gt;恐惧&lt;/status&gt;、&lt;status&gt;沉默&lt;/status&gt;、&lt;status&gt;致盲&lt;/status&gt;、&lt;status&gt;变形&lt;/status&gt;和&lt;status&gt;定身&lt;/status&gt;效果的持续时间。它对&lt;status&gt;浮空&lt;/status&gt;或&lt;status&gt;压制&lt;/status&gt;效果无效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (350)&lt;/span&gt;" alt="水银之靴">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/1028.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;红水晶&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升生命值&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;150&lt;/attention&gt;生命值&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="红水晶">
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-red.png">
												Control Ward <span class='wards vision'>12</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-42 tip" title="刀锋舞者">刀锋舞者</div>
								<div class="Image20 __sprite __spc20 __spc20-42 tip" title="刀锋舞者">刀锋舞者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=IAimToMisbehave" class="Link" target='_blank'>IAimToMisbehave</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-83 tip" title="狂野女猎手">狂野女猎手</div>
								<div class="Image20 __sprite __spc20 __spc20-83 tip" title="狂野女猎手">狂野女猎手</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=jiangyouping7" class="Link" target='_blank'>jiangyouping7</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-153 tip" title="爆破鬼才">爆破鬼才</div>
								<div class="Image20 __sprite __spc20 __spc20-153 tip" title="爆破鬼才">爆破鬼才</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Smooth+Guy" class="Link" target='_blank'>Smooth Guy</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-23 tip" title="荣耀行刑官">荣耀行刑官</div>
								<div class="Image20 __sprite __spc20 __spc20-23 tip" title="荣耀行刑官">荣耀行刑官</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Abner" class="Link" target='_blank'>Abner</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-107 tip" title="腕豪">腕豪</div>
								<div class="Image20 __sprite __spc20 __spc20-107 tip" title="腕豪">腕豪</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-37 tip" title="法外狂徒">法外狂徒</div>
								<div class="Image20 __sprite __spc20 __spc20-37 tip" title="法外狂徒">法外狂徒</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=SMB+NuQ" class="Link" target='_blank'>SMB NuQ</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-66 tip" title="含羞蓓蕾">含羞蓓蕾</div>
								<div class="Image20 __sprite __spc20 __spc20-66 tip" title="含羞蓓蕾">含羞蓓蕾</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Gilius1" class="Link" target='_blank'>Gilius1</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-2 tip" title="离群之刺">离群之刺</div>
								<div class="Image20 __sprite __spc20 __spc20-2 tip" title="离群之刺">离群之刺</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=TwTv+PROJECT+BZ" class="Link" target='_blank'>TwTv PROJECT BZ</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-126 tip" title="麦林炮手">麦林炮手</div>
								<div class="Image20 __sprite __spc20 __spc20-126 tip" title="麦林炮手">麦林炮手</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Seelame" class="Link" target='_blank'>Seelame</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-65 tip" title="曙光女神">曙光女神</div>
								<div class="Image20 __sprite __spc20 __spc20-65 tip" title="曙光女神">曙光女神</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=USE+Dreamer+Ace" class="Link" target='_blank'>USE Dreamer Ace</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
															<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-198 Off"></span>
								<span class="__spSite __spSite-197 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Lose  "
	     data-summoner-id="135515503"
	     data-game-time="1633639585"
	     data-game-id="5495933240"
	     data-game-result="lose"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633639585' data-type='' data-interval='60'>2021-10-08 05:46:25</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											失败									</div>
									<div class="GameLength">30分 30秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/nautilus/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Nautilus.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="深海泰坦"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;引燃&lt;/b&gt;&lt;br&gt;&lt;span&gt;引燃是对单体敌方目标施放的持续性伤害技能，在5秒的持续时间里造成70-410（取决于英雄等级）真实伤害，获得目标的视野，并减少目标所受的治疗和回复效果。&lt;/span&gt;" alt="引燃">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8439.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;余震&lt;/b&gt;&lt;br&gt;&lt;span&gt;在定身住一名敌方英雄后，使你的护甲和魔法抗性提升35+你80%的额外双抗，持续2.5秒。随后会爆炸，对附近的敌人造成魔法伤害。&lt;br&gt;&lt;br&gt;伤害值：25 - 120 (+你8%的额外生命值)&lt;br&gt;冷却时间：20秒&lt;br&gt;&lt;br&gt;来自余震的双抗加成封顶值：80-150(基于等级)&lt;br&gt;&lt;/span&gt;" alt="余震">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/nautilus/statistics" target="_blank">深海泰坦</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">5</span> /
					<span class="Death">5</span> /
					<span class="Assist">21</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">5.20:1</span> KDA				</div>
																							<div class="Badge"><span class="Text ACE">ACE</span></div>
												</div>
			<div class="Stats">
				<div class="Level">
					等级13
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 36  + 野怪 0&lt;br&gt;每分钟CS1.2个">36 (1.2)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  60%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Grandmaster</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3857.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;白岩肩铠&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;15&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;250&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础生命回复&lt;br&gt;&lt;attention&gt;3&lt;/attention&gt;金币/10秒&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存0个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt; &lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存4个侦察守卫，并在访问商店时补满。 &lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="白岩肩铠">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3190.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;钢铁烈阳之匣&lt;/b&gt;&lt;br&gt;&lt;span&gt;主动施放来为附近友军提供吸收伤害的护盾&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;护甲&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;魔法抗性&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;虔诚：&lt;/active&gt;为附近友军提供&lt;shield&gt;230 - 385(基于友军等级)护盾&lt;/shield&gt;，在2.5秒里持续衰减(90秒冷却时间)。&lt;br&gt;&lt;li&gt;&lt;passive&gt;奉献：&lt;/passive&gt;为附近友方英雄提供&lt;scaleArmor&gt;5护甲&lt;/scaleArmor&gt;和&lt;scaleMR&gt;魔法抗性&lt;/scaleMR&gt;。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;2&lt;/attention&gt;护甲/魔法抗性加成至&lt;passive&gt;奉献&lt;/passive&gt;。&lt;br&gt;&lt;br&gt;&lt;rules&gt;加成效果的强度是基于该友方英雄的等级。&lt;br&gt;20秒内的后续&lt;active&gt;奉献&lt;/active&gt;的护盾仅有25%效果。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2500 (200)&lt;/span&gt;" alt="钢铁烈阳之匣">
													</div>
																							<div class="Item">
															<div class="Image NoItem"></div>
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3364.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;神谕透镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;持续期间可瘫痪附近隐形的守卫和陷阱&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;扫描你的周围，预警隐藏的敌方单位，并使隐形的陷阱显形，并使附近的敌方侦察守卫显形(并暂时失效)10秒&lt;scaleLevel&gt;(90 - 60秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="神谕透镜">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/8001.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;厌恨锁链&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;650&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt; &lt;active&gt;起誓：&lt;/active&gt;选择一名【仇敌】以开始积攒一个【复仇令】(90秒)。&lt;br&gt;&lt;li&gt;&lt;passive&gt;复仇令：&lt;/passive&gt;从你的【仇敌】处所受的伤害至多减免30%，每层【复仇令】提供1%伤害减免。你会持续获得层数，并在60秒后达到最大层数。&lt;li&gt;&lt;passive&gt;报复：&lt;/passive&gt;在满层时，你的【仇敌】在你附近时会降低20%韧性。&lt;br&gt;&lt;br&gt;&lt;rules&gt;主动效果可以在阵亡时施放，并且施放距离无限。层数会在选到一个新目标时重置。需要脱离与英雄的战斗状态长达15秒后才能施放。&lt;/rules&gt;&lt;br&gt;&lt;br&gt;&lt;flavorText&gt;&quot;她曾发誓要用她的一生来毁灭他。那双挑战护手听到了。&quot;&lt;/flavorText&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2500 (800)&lt;/span&gt;" alt="厌恨锁链">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/1057.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;负极斗篷&lt;/b&gt;&lt;br&gt;&lt;span&gt;适度提升魔法抗性&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;50&lt;/attention&gt;魔法抗性&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;900 (450)&lt;/span&gt;" alt="负极斗篷">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3111.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;水银之靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升移动速度并降低限制效果的时长&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;25&lt;/attention&gt;魔法抗性&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;br&gt;&lt;attention&gt;30%&lt;/attention&gt;韧性&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;rules&gt;韧性会减少&lt;status&gt;晕眩&lt;/status&gt;、&lt;status&gt;减速&lt;/status&gt;、&lt;status&gt;嘲讽&lt;/status&gt;、&lt;status&gt;恐惧&lt;/status&gt;、&lt;status&gt;沉默&lt;/status&gt;、&lt;status&gt;致盲&lt;/status&gt;、&lt;status&gt;变形&lt;/status&gt;和&lt;status&gt;定身&lt;/status&gt;效果的持续时间。它对&lt;status&gt;浮空&lt;/status&gt;或&lt;status&gt;压制&lt;/status&gt;效果无效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (350)&lt;/span&gt;" alt="水银之靴">
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-red.png">
												Control Ward <span class='wards vision'>14</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-17 tip" title="青钢影">青钢影</div>
								<div class="Image20 __sprite __spc20 __spc20-17 tip" title="青钢影">青钢影</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=tryharder123" class="Link" target='_blank'>tryharder123</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-64 tip" title="盲僧">盲僧</div>
								<div class="Image20 __sprite __spc20 __spc20-64 tip" title="盲僧">盲僧</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Gilius1" class="Link" target='_blank'>Gilius1</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-118 tip" title="解脱者">解脱者</div>
								<div class="Image20 __sprite __spc20 __spc20-118 tip" title="解脱者">解脱者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Blodreinaaaaa" class="Link" target='_blank'>Blodreinaaaaa</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-75 tip" title="赏金猎人">赏金猎人</div>
								<div class="Image20 __sprite __spc20 __spc20-75 tip" title="赏金猎人">赏金猎人</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=SAUCE+WALKA" class="Link" target='_blank'>SAUCE WALKA</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-81 tip" title="深海泰坦">深海泰坦</div>
								<div class="Image20 __sprite __spc20 __spc20-81 tip" title="深海泰坦">深海泰坦</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-134 tip" title="暗夜猎手">暗夜猎手</div>
								<div class="Image20 __sprite __spc20 __spc20-134 tip" title="暗夜猎手">暗夜猎手</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=7+7+7+7" class="Link" target='_blank'>7 7 7 7</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-146 tip" title="德邦总管">德邦总管</div>
								<div class="Image20 __sprite __spc20 __spc20-146 tip" title="德邦总管">德邦总管</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=UOL+Cryptodir" class="Link" target='_blank'>UOL Cryptodir</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-54 tip" title="虚空行者">虚空行者</div>
								<div class="Image20 __sprite __spc20 __spc20-54 tip" title="虚空行者">虚空行者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Rank1+Macro" class="Link" target='_blank'>Rank1 Macro</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-153 tip" title="爆破鬼才">爆破鬼才</div>
								<div class="Image20 __sprite __spc20 __spc20-153 tip" title="爆破鬼才">爆破鬼才</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=PQPAANLS" class="Link" target='_blank'>PQPAANLS</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-12 tip" title="星界游神">星界游神</div>
								<div class="Image20 __sprite __spc20 __spc20-12 tip" title="星界游神">星界游神</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=EL+BARDOOOO" class="Link" target='_blank'>EL BARDOOOO</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
															<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-198 Off"></span>
								<span class="__spSite __spSite-197 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Win  "
	     data-summoner-id="135515503"
	     data-game-time="1633607823"
	     data-game-id="5495178746"
	     data-game-result="win"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="小海牛">
					小海牛
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633607823' data-type='' data-interval='60'>2021-10-07 20:57:03</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											胜利									</div>
									<div class="GameLength">10分 37秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/sylas/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Sylas.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="解脱者"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;引燃&lt;/b&gt;&lt;br&gt;&lt;span&gt;引燃是对单体敌方目标施放的持续性伤害技能，在5秒的持续时间里造成70-410（取决于英雄等级）真实伤害，获得目标的视野，并减少目标所受的治疗和回复效果。&lt;/span&gt;" alt="引燃">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8010.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;征服者&lt;/b&gt;&lt;br&gt;&lt;span&gt;普通攻击或伤害型技能在命中一名敌方英雄时会提供2层【征服者】效果，持续6秒，每层效果提供2-5&lt;lol-uikit-tooltipped-keyword key=&#039;LinkTooltip_Description_Adaptive&#039;&gt;&lt;font color=&#039;#48C4B7&#039;&gt;适应之力&lt;/font&gt;&lt;/lol-uikit-tooltipped-keyword&gt;。至多可叠加12次。远程英雄的每次普攻只会提供1层效果。&lt;br&gt;&lt;br&gt;在叠满层数后，你对英雄造成的9%伤害会转化为对自身的治疗效果(远程英雄的转化率为6%)。&lt;/span&gt;" alt="征服者">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8100.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;主宰&lt;/b&gt;&lt;br&gt;&lt;span&gt;爆发伤害并前往目标&lt;/span&gt;" alt="主宰">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/sylas/statistics" target="_blank">解脱者</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">10</span> /
					<span class="Death">5</span> /
					<span class="Assist">11</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">4.20:1</span> KDA				</div>
									<div class="MultiKill">
						<span class="Kill">三杀</span>
					</div>
															</div>
			<div class="Stats">
				<div class="Level">
					等级13
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 37  + 野怪 8&lt;br&gt;每分钟CS4.2个">45 (4.2)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  41%
					</div>
											</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3152.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;海克斯科技火箭腰带&lt;/b&gt;&lt;br&gt;&lt;span&gt;主动施放来向前冲刺并释放一阵炫目的轰炸&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;90&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;6&lt;/attention&gt;法术穿透&lt;br&gt;&lt;attention&gt;250&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;15&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;海克斯魔弹：&lt;/active&gt;朝着目标方向冲刺，释放一道魔法弹圆弧，造成&lt;magicDamage&gt;(125+15%法术强度)魔法伤害&lt;/magicDamage&gt;。随后，在朝着敌方英雄移动时提供&lt;speed&gt;30%移动速度&lt;/speed&gt;，持续1.5秒(40秒冷却时间)。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得 &lt;attention&gt;5&lt;/attention&gt;法术穿透。&lt;br&gt;&lt;br&gt;&lt;rules&gt;超音速的冲刺无法穿过地形。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;3200 (900)&lt;/span&gt;" alt="海克斯科技火箭腰带">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2421.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;破损的秒表&lt;/b&gt;&lt;br&gt;&lt;span&gt;升级为秒表&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;支离破碎的时间：&lt;/passive&gt;【秒表】目前是破损状态，但仍然可以用于升级。&lt;br&gt;&lt;br&gt;&lt;rules&gt;在打破一个【秒表】后，商店主人就只会卖给你&lt;rarityGeneric&gt;破损的秒表&lt;/rarityGeneric&gt;了。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;650 (650)&lt;/span&gt;" alt="破损的秒表">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/1028.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;红水晶&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升生命值&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;150&lt;/attention&gt;生命值&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="红水晶">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3340.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;侦查守卫&lt;/b&gt;&lt;br&gt;&lt;span&gt;周期性地放置一个侦查守卫&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;在地上放置一个可持续&lt;scaleLevel&gt;90 - 120&lt;/scaleLevel&gt;秒的侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存2个侦察守卫，每&lt;scaleLevel&gt;240 - 120&lt;/scaleLevel&gt;秒生成1个新的守卫。 &lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="侦查守卫">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3191.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;探索者的护臂&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升护甲和法术强度&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;20&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;15&lt;/attention&gt;护甲&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;女巫之道：&lt;/passive&gt;击杀一个单位提供&lt;scaleArmor&gt;0.5护甲&lt;/scaleArmor&gt;(最多提供&lt;scaleArmor&gt;15护甲&lt;/scaleArmor&gt;)。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1000 (265)&lt;/span&gt;" alt="探索者的护臂">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3089.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;灭世者的死亡之帽&lt;/b&gt;&lt;br&gt;&lt;span&gt;巨幅提升法术强度&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;120&lt;/attention&gt;法术强度&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;魔法乐章：&lt;/passive&gt;使你的总&lt;scaleAP&gt;法术强度提升35%&lt;/scaleAP&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;3600 (1100)&lt;/span&gt;" alt="灭世者的死亡之帽">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3020.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;法师之靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;增强移动速度和魔法伤害&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;18&lt;/attention&gt;法术穿透&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (800)&lt;/span&gt;" alt="法师之靴">
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildblue-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildblue-p.png">
																	</button>
																						</div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-118 tip" title="解脱者">解脱者</div>
								<div class="Image20 __sprite __spc20 __spc20-118 tip" title="解脱者">解脱者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-30 tip" title="无双剑姬">无双剑姬</div>
								<div class="Image20 __sprite __spc20 __spc20-30 tip" title="无双剑姬">无双剑姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=lucky+iceland+" class="Link" target='_blank'>lucky iceland </a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-8 tip" title="残月之肃">残月之肃</div>
								<div class="Image20 __sprite __spc20 __spc20-8 tip" title="残月之肃">残月之肃</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=2021Worlds" class="Link" target='_blank'>2021Worlds</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-134 tip" title="暗夜猎手">暗夜猎手</div>
								<div class="Image20 __sprite __spc20 __spc20-134 tip" title="暗夜猎手">暗夜猎手</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Smurfin030" class="Link" target='_blank'>Smurfin030</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-36 tip" title="酒桶">酒桶</div>
								<div class="Image20 __sprite __spc20 __spc20-36 tip" title="酒桶">酒桶</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=kijke+je+tankk" class="Link" target='_blank'>kijke je tankk</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-144 tip" title="逆羽">逆羽</div>
								<div class="Image20 __sprite __spc20 __spc20-144 tip" title="逆羽">逆羽</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Gidoeoabo" class="Link" target='_blank'>Gidoeoabo</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-39 tip" title="战争之影">战争之影</div>
								<div class="Image20 __sprite __spc20 __spc20-39 tip" title="战争之影">战争之影</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=SmiteBoi" class="Link" target='_blank'>SmiteBoi</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-131 tip" title="兽灵行者">兽灵行者</div>
								<div class="Image20 __sprite __spc20 __spc20-131 tip" title="兽灵行者">兽灵行者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=D+G0D" class="Link" target='_blank'>D G0D</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-25 tip" title="时间刺客">时间刺客</div>
								<div class="Image20 __sprite __spc20 __spc20-25 tip" title="时间刺客">时间刺客</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Azayaa" class="Link" target='_blank'>Azayaa</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-50 tip" title="虚空之女">虚空之女</div>
								<div class="Image20 __sprite __spc20 __spc20-50 tip" title="虚空之女">虚空之女</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Any%CE%B1" class="Link" target='_blank'>Anyα</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																							<div class="Item">
								<a id="right_match_replay" href="#" class="Button Replay OpenSpectateButton">
									<span class="__spSite __spSite-159"></span></a>
							</div>
																<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-194 Off"></span>
								<span class="__spSite __spSite-193 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Win  "
	     data-summoner-id="135515503"
	     data-game-time="1633606972"
	     data-game-id="5495186176"
	     data-game-result="win"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633606972' data-type='' data-interval='60'>2021-10-07 20:42:52</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											胜利									</div>
									<div class="GameLength">29分 6秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/rakan/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Rakan.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="幻翎"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;引燃&lt;/b&gt;&lt;br&gt;&lt;span&gt;引燃是对单体敌方目标施放的持续性伤害技能，在5秒的持续时间里造成70-410（取决于英雄等级）真实伤害，获得目标的视野，并减少目标所受的治疗和回复效果。&lt;/span&gt;" alt="引燃">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8465.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;守护者&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;i&gt;守护&lt;/i&gt;距离你350码内的友军，以及被你选为技能目标的友军2.5秒。当&lt;i&gt;守护&lt;/i&gt;持续时，如果你或该友军在&lt;i&gt;守护&lt;/i&gt;持续期间承受的伤害超过一定数额，那么你们两个都会获得一层持续1.5秒的护盾。&lt;br&gt;&lt;br&gt;冷却时间：&lt;scaleLevel&gt;70 ~40&lt;/scaleLevel&gt;秒&lt;br&gt;护盾值：&lt;scaleLevel&gt;70~150&lt;/scaleLevel&gt;+你&lt;scaleAP&gt;15%&lt;/scaleAP&gt;法术强度+你&lt;scalehealth&gt;9%&lt;/scalehealth&gt;额外生命值。&lt;br&gt;触发阈值：&lt;scaleLevel&gt;90~250&lt;/scaleLevel&gt;折后伤害。&lt;/span&gt;" alt="守护者">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/rakan/statistics" target="_blank">幻翎</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">4</span> /
					<span class="Death">11</span> /
					<span class="Assist">24</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">2.55:1</span> KDA				</div>
																								</div>
			<div class="Stats">
				<div class="Level">
					等级14
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 15  + 野怪 0&lt;br&gt;每分钟CS0.5个">15 (0.5)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  76%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Grandmaster</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3853.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;极冰碎片&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;40&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;75&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础法力回复&lt;br&gt;&lt;attention&gt;3&lt;/attention&gt;金币/10秒&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存0个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存4个侦察守卫，并在访问商店时补满。 &lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="极冰碎片">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2065.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;舒瑞娅的战歌&lt;/b&gt;&lt;br&gt;&lt;span&gt;激活以加速附近的友军&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;40&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础法力回复&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;鼓舞：&lt;/active&gt;为你和附近的友方英雄提供&lt;speed&gt;30%移动速度&lt;/speed&gt;，持续4秒。(75秒冷却时间)。&lt;br&gt;&lt;li&gt;&lt;passive&gt;激发：&lt;/passive&gt;强化或保护另一名己方英雄时，会为你和目标都提供&lt;speed&gt;25%移动速度&lt;/speed&gt;，持续1.5秒。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得 &lt;attention&gt;5&lt;/attention&gt;技能急速。&lt;br&gt;&lt;br&gt;&lt;rules&gt;一名友军在每4秒内仅可被&lt;keywordMajor&gt;激发&lt;/keywordMajor&gt;效果影响1次。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2500 (750)&lt;/span&gt;" alt="舒瑞娅的战歌">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/4643.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;警觉眼石&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;150&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;15&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;奥术窖藏：&lt;/passive&gt;这件装备至多可储存3个已购买的控制守卫。&lt;li&gt;&lt;passive&gt;注视：&lt;/passive&gt;使你的侦察守卫和控制守卫的放置上限提升1。&lt;li&gt;&lt;passive&gt;以绪塔尔的祝福：&lt;/passive&gt;提供12%提升至额外生命值、额外攻击力、技能急速和法术强度。&lt;br&gt;&lt;br&gt;&lt;rules&gt;由&lt;rarityLegendary&gt;戒备眼石&lt;/rarityLegendary&gt;升级而成。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (0)&lt;/span&gt;" alt="警觉眼石">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3364.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;神谕透镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;持续期间可瘫痪附近隐形的守卫和陷阱&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;扫描你的周围，预警隐藏的敌方单位，并使隐形的陷阱显形，并使附近的敌方侦察守卫显形(并暂时失效)10秒&lt;scaleLevel&gt;(90 - 60秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="神谕透镜">
															</div>
																							<div class="Item">
															<div class="Image NoItem"></div>
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3158.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;明朗之靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升移动速度和冷却缩减&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;br&gt;&lt;li&gt;提供12召唤师技能急速。&lt;br&gt;&lt;br&gt;&lt;flavorText&gt;“这个物品是为了庆祝在2010年12月10日艾欧尼亚和诺克萨斯的重赛中，艾欧尼亚取得胜利。”&lt;/flavorText&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;950 (650)&lt;/span&gt;" alt="明朗之靴">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3050.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;基克的聚合&lt;/b&gt;&lt;br&gt;&lt;span&gt;在你施放终极技能时，为你和你的队友提供加成。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;250&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;25&lt;/attention&gt;护甲&lt;br&gt;&lt;attention&gt;250&lt;/attention&gt;法力&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;导管：&lt;/active&gt;指定一名&lt;attention&gt;帮手&lt;/attention&gt;(60秒冷却时间)。&lt;br&gt;&lt;li&gt;&lt;passive&gt;聚合：&lt;/passive&gt;在你&lt;status&gt;定身&lt;/status&gt;一名敌人后的8秒里，你的&lt;attention&gt;帮手&lt;/attention&gt;的技能和攻击对这个敌人附带额外的&lt;magicDamage&gt;(30 - 70(基于等级) + 1.5%生命值 + 7.5%法术强度)魔法伤害&lt;/magicDamage&gt;。&lt;br&gt;&lt;br&gt;&lt;rules&gt;同一个英雄同一时间只能被一个【基克的聚合】所连接。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2400 (700)&lt;/span&gt;" alt="基克的聚合">
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildblue-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildblue-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-blue.png">
												Control Ward <span class='wards vision'>19</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-46 tip" title="武器大师">武器大师</div>
								<div class="Image20 __sprite __spc20 __spc20-46 tip" title="武器大师">武器大师</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=FFDP" class="Link" target='_blank'>FFDP</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-83 tip" title="狂野女猎手">狂野女猎手</div>
								<div class="Image20 __sprite __spc20 __spc20-83 tip" title="狂野女猎手">狂野女猎手</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Boukada" class="Link" target='_blank'>Boukada</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-148 tip" title="封魔剑魂">封魔剑魂</div>
								<div class="Image20 __sprite __spc20 __spc20-148 tip" title="封魔剑魂">封魔剑魂</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=MakoxenormusKEK" class="Link" target='_blank'>MakoxenormusKEK</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-62 tip" title="深渊巨口">深渊巨口</div>
								<div class="Image20 __sprite __spc20 __spc20-62 tip" title="深渊巨口">深渊巨口</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Fish+Feces" class="Link" target='_blank'>Fish Feces</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-94 tip" title="幻翎">幻翎</div>
								<div class="Image20 __sprite __spc20 __spc20-94 tip" title="幻翎">幻翎</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-42 tip" title="刀锋舞者">刀锋舞者</div>
								<div class="Image20 __sprite __spc20 __spc20-42 tip" title="刀锋舞者">刀锋舞者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=SlXTEN" class="Link" target='_blank'>SlXTEN</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-25 tip" title="时间刺客">时间刺客</div>
								<div class="Image20 __sprite __spc20 __spc20-25 tip" title="时间刺客">时间刺客</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Ekko+the+Neeko" class="Link" target='_blank'>Ekko the Neeko</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-37 tip" title="法外狂徒">法外狂徒</div>
								<div class="Image20 __sprite __spc20 __spc20-37 tip" title="法外狂徒">法外狂徒</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=SK+Alois" class="Link" target='_blank'>SK Alois</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-106 tip" title="星籁歌姬">星籁歌姬</div>
								<div class="Image20 __sprite __spc20 __spc20-106 tip" title="星籁歌姬">星籁歌姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Fabrik+Linus+" class="Link" target='_blank'>Fabrik Linus </a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-5 tip" title="殇之木乃伊">殇之木乃伊</div>
								<div class="Image20 __sprite __spc20 __spc20-5 tip" title="殇之木乃伊">殇之木乃伊</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=SirNukesAlott" class="Link" target='_blank'>SirNukesAlott</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																							<div class="Item">
								<a id="right_match_replay" href="#" class="Button Replay OpenSpectateButton">
									<span class="__spSite __spSite-159"></span></a>
							</div>
																<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-194 Off"></span>
								<span class="__spSite __spSite-193 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Lose  "
	     data-summoner-id="135515503"
	     data-game-time="1633565748"
	     data-game-id="5494869160"
	     data-game-result="lose"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633565748' data-type='' data-interval='60'>2021-10-07 09:15:48</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											失败									</div>
									<div class="GameLength">28分 11秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/rell/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Rell.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="镕铁少女"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;引燃&lt;/b&gt;&lt;br&gt;&lt;span&gt;引燃是对单体敌方目标施放的持续性伤害技能，在5秒的持续时间里造成70-410（取决于英雄等级）真实伤害，获得目标的视野，并减少目标所受的治疗和回复效果。&lt;/span&gt;" alt="引燃">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8439.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;余震&lt;/b&gt;&lt;br&gt;&lt;span&gt;在定身住一名敌方英雄后，使你的护甲和魔法抗性提升35+你80%的额外双抗，持续2.5秒。随后会爆炸，对附近的敌人造成魔法伤害。&lt;br&gt;&lt;br&gt;伤害值：25 - 120 (+你8%的额外生命值)&lt;br&gt;冷却时间：20秒&lt;br&gt;&lt;br&gt;来自余震的双抗加成封顶值：80-150(基于等级)&lt;br&gt;&lt;/span&gt;" alt="余震">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/rell/statistics" target="_blank">镕铁少女</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">1</span> /
					<span class="Death">4</span> /
					<span class="Assist">7</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">2.00:1</span> KDA				</div>
																							<div class="Badge"><span class="Text ACE">ACE</span></div>
												</div>
			<div class="Stats">
				<div class="Level">
					等级12
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 55  + 野怪 0&lt;br&gt;每分钟CS2个">55 (2)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  44%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Grandmaster</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3860.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;山脉壁垒&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;20&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;250&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础生命回复&lt;br&gt;&lt;attention&gt;3&lt;/attention&gt;金币/10秒&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存0个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt; &lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存4个侦察守卫，并在访问商店时补满。 &lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="山脉壁垒">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3190.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;钢铁烈阳之匣&lt;/b&gt;&lt;br&gt;&lt;span&gt;主动施放来为附近友军提供吸收伤害的护盾&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;护甲&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;魔法抗性&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;虔诚：&lt;/active&gt;为附近友军提供&lt;shield&gt;230 - 385(基于友军等级)护盾&lt;/shield&gt;，在2.5秒里持续衰减(90秒冷却时间)。&lt;br&gt;&lt;li&gt;&lt;passive&gt;奉献：&lt;/passive&gt;为附近友方英雄提供&lt;scaleArmor&gt;5护甲&lt;/scaleArmor&gt;和&lt;scaleMR&gt;魔法抗性&lt;/scaleMR&gt;。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;2&lt;/attention&gt;护甲/魔法抗性加成至&lt;passive&gt;奉献&lt;/passive&gt;。&lt;br&gt;&lt;br&gt;&lt;rules&gt;加成效果的强度是基于该友方英雄的等级。&lt;br&gt;20秒内的后续&lt;active&gt;奉献&lt;/active&gt;的护盾仅有25%效果。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2500 (200)&lt;/span&gt;" alt="钢铁烈阳之匣">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2055.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;控制守卫&lt;/b&gt;&lt;br&gt;&lt;span&gt;用来使范围内的守卫和隐形陷阱失效。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 消耗：&lt;/active&gt;放置一个强大的控制守卫来提供附近区域的视野。这个设备还会使&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;的陷阱显形，使&lt;keywordStealth&gt;伪装&lt;/keywordStealth&gt;的敌人们显形，并使敌方守卫显形和失效。 &lt;br&gt;&lt;br&gt;&lt;rules&gt;你至多可以携带2个控制守卫。控制守卫不会使其它控制守卫失效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;75 (75)&lt;/span&gt;" alt="控制守卫">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3364.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;神谕透镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;持续期间可瘫痪附近隐形的守卫和陷阱&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;扫描你的周围，预警隐藏的敌方单位，并使隐形的陷阱显形，并使附近的敌方侦察守卫显形(并暂时失效)10秒&lt;scaleLevel&gt;(90 - 60秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="神谕透镜">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3067.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;燃烧宝石&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升生命值和冷却缩减&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;10&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;800 (400)&lt;/span&gt;" alt="燃烧宝石">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3158.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;明朗之靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升移动速度和冷却缩减&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;br&gt;&lt;li&gt;提供12召唤师技能急速。&lt;br&gt;&lt;br&gt;&lt;flavorText&gt;“这个物品是为了庆祝在2010年12月10日艾欧尼亚和诺克萨斯的重赛中，艾欧尼亚取得胜利。”&lt;/flavorText&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;950 (650)&lt;/span&gt;" alt="明朗之靴">
													</div>
																							<div class="Item">
															<div class="Image NoItem"></div>
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-red.png">
												Control Ward <span class='wards vision'>15</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-107 tip" title="腕豪">腕豪</div>
								<div class="Image20 __sprite __spc20 __spc20-107 tip" title="腕豪">腕豪</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=borcigendale" class="Link" target='_blank'>borcigendale</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-59 tip" title="虚空掠夺者">虚空掠夺者</div>
								<div class="Image20 __sprite __spc20 __spc20-59 tip" title="虚空掠夺者">虚空掠夺者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Sticky+Pillar" class="Link" target='_blank'>Sticky Pillar</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-29 tip" title="远古恐惧">远古恐惧</div>
								<div class="Image20 __sprite __spc20 __spc20-29 tip" title="远古恐惧">远古恐惧</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=EUW+VILLAIN" class="Link" target='_blank'>EUW VILLAIN</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-103 tip" title="沙漠玫瑰">沙漠玫瑰</div>
								<div class="Image20 __sprite __spc20 __spc20-103 tip" title="沙漠玫瑰">沙漠玫瑰</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=my+13th+reason" class="Link" target='_blank'>my 13th reason</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-97 tip" title="镕铁少女">镕铁少女</div>
								<div class="Image20 __sprite __spc20 __spc20-97 tip" title="镕铁少女">镕铁少女</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-100 tip" title="放逐之刃">放逐之刃</div>
								<div class="Image20 __sprite __spc20 __spc20-100 tip" title="放逐之刃">放逐之刃</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=distant+star" class="Link" target='_blank'>distant star</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-37 tip" title="法外狂徒">法外狂徒</div>
								<div class="Image20 __sprite __spc20 __spc20-37 tip" title="法外狂徒">法外狂徒</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=2021Worlds" class="Link" target='_blank'>2021Worlds</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-118 tip" title="解脱者">解脱者</div>
								<div class="Image20 __sprite __spc20 __spc20-118 tip" title="解脱者">解脱者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Jas%CE%BFn+Bourne" class="Link" target='_blank'>Jasοn Bourne</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-75 tip" title="赏金猎人">赏金猎人</div>
								<div class="Image20 __sprite __spc20 __spc20-75 tip" title="赏金猎人">赏金猎人</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=chill+player123" class="Link" target='_blank'>chill player123</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-94 tip" title="幻翎">幻翎</div>
								<div class="Image20 __sprite __spc20 __spc20-94 tip" title="幻翎">幻翎</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Advienne" class="Link" target='_blank'>Advienne</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																							<div class="Item">
								<a id="right_match_replay" href="#" class="Button Replay OpenSpectateButton">
									<span class="__spSite __spSite-159"></span></a>
							</div>
																<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-198 Off"></span>
								<span class="__spSite __spSite-197 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Win  "
	     data-summoner-id="135515503"
	     data-game-time="1633563562"
	     data-game-id="5494946865"
	     data-game-result="win"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633563562' data-type='' data-interval='60'>2021-10-07 08:39:22</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											胜利									</div>
									<div class="GameLength">20分 15秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/nami/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Nami.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="唤潮鲛姬"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;引燃&lt;/b&gt;&lt;br&gt;&lt;span&gt;引燃是对单体敌方目标施放的持续性伤害技能，在5秒的持续时间里造成70-410（取决于英雄等级）真实伤害，获得目标的视野，并减少目标所受的治疗和回复效果。&lt;/span&gt;" alt="引燃">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8112.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;电刑&lt;/b&gt;&lt;br&gt;&lt;span&gt;在3秒内用3个&lt;b&gt;独立的&lt;/b&gt;攻击或技能命中一位英雄时，会造成额外的&lt;lol-uikit-tooltipped-keyword key=&#039;LinkTooltip_Description_AdaptiveDmg&#039;&gt;&lt;font color=&#039;#48C4B7&#039;&gt;自适应伤害&lt;/font&gt;&lt;/lol-uikit-tooltipped-keyword&gt;。&lt;br&gt;&lt;br&gt;伤害值：30 - 180 (+0.4额外攻击力, +0.25法术强度)。&lt;br&gt;&lt;br&gt;冷却时间：25 - 20秒&lt;br&gt;&lt;br&gt;&lt;hr&gt;&lt;i&gt;“我们曾称呼他们为“雷霆领主”，是因为他们的闪电招来了灾祸。”&lt;/i&gt;&lt;/span&gt;" alt="电刑">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/nami/statistics" target="_blank">唤潮鲛姬</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">2</span> /
					<span class="Death">1</span> /
					<span class="Assist">18</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">20.00:1</span> KDA				</div>
																								</div>
			<div class="Stats">
				<div class="Level">
					等级11
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 10  + 野怪 0&lt;br&gt;每分钟CS0.5个">10 (0.5)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  80%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Master</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3853.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;极冰碎片&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;40&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;75&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础法力回复&lt;br&gt;&lt;attention&gt;3&lt;/attention&gt;金币/10秒&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存0个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存4个侦察守卫，并在访问商店时补满。 &lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="极冰碎片">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/4642.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;班德尔玻璃镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;20&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;10&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;50%&lt;/attention&gt;基础法力回复&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;950 (265)&lt;/span&gt;" alt="班德尔玻璃镜">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2055.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;控制守卫&lt;/b&gt;&lt;br&gt;&lt;span&gt;用来使范围内的守卫和隐形陷阱失效。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 消耗：&lt;/active&gt;放置一个强大的控制守卫来提供附近区域的视野。这个设备还会使&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;的陷阱显形，使&lt;keywordStealth&gt;伪装&lt;/keywordStealth&gt;的敌人们显形，并使敌方守卫显形和失效。 &lt;br&gt;&lt;br&gt;&lt;rules&gt;你至多可以携带2个控制守卫。控制守卫不会使其它控制守卫失效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;75 (75)&lt;/span&gt;" alt="控制守卫">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3364.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;神谕透镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;持续期间可瘫痪附近隐形的守卫和陷阱&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;扫描你的周围，预警隐藏的敌方单位，并使隐形的陷阱显形，并使附近的敌方侦察守卫显形(并暂时失效)10秒&lt;scaleLevel&gt;(90 - 60秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="神谕透镜">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3158.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;明朗之靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升移动速度和冷却缩减&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;br&gt;&lt;li&gt;提供12召唤师技能急速。&lt;br&gt;&lt;br&gt;&lt;flavorText&gt;“这个物品是为了庆祝在2010年12月10日艾欧尼亚和诺克萨斯的重赛中，艾欧尼亚取得胜利。”&lt;/flavorText&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;950 (650)&lt;/span&gt;" alt="明朗之靴">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/4005.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;帝国指令&lt;/b&gt;&lt;br&gt;&lt;span&gt;将伤害延后。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;40&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础法力回复&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;协同开火：&lt;/passive&gt;技能在&lt;status&gt;减速&lt;/status&gt;或&lt;status&gt;定身&lt;/status&gt;一名英雄时会造成&lt;magicDamage&gt;45 - 75(基于等级)额外魔法伤害&lt;/magicDamage&gt;并将其标记4秒(每个敌方英雄有6秒冷却时间)。友方英雄的伤害会引爆标记，造成额外的&lt;magicDamage&gt;90 - 150(基于友军等级)魔法伤害&lt;/magicDamage&gt;并为你和该友军都提供&lt;speed&gt;20%移动速度&lt;/speed&gt;，持续2秒。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;15&lt;/attention&gt;法术强度。&lt;br&gt;&lt;br&gt;&lt;rules&gt;加成效果的强度是基于该友方英雄的等级。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2500 (750)&lt;/span&gt;" alt="帝国指令">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3916.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;湮灭宝珠&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升魔法伤害&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;30&lt;/attention&gt;法术强度&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;恶咒缠身：&lt;/passive&gt;对英雄造成魔法伤害时会施加持续3秒的&lt;status&gt;40%重伤&lt;/status&gt;效果。&lt;br&gt;&lt;br&gt;&lt;rules&gt;&lt;status&gt;重伤&lt;/status&gt;会降低治疗效果和生命回复的效能。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;800 (365)&lt;/span&gt;" alt="湮灭宝珠">
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildblue-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildblue-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-blue.png">
												Control Ward <span class='wards vision'>7</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-120 tip" title="河流之王">河流之王</div>
								<div class="Image20 __sprite __spc20 __spc20-120 tip" title="河流之王">河流之王</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=mangos1" class="Link" target='_blank'>mangos1</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-64 tip" title="盲僧">盲僧</div>
								<div class="Image20 __sprite __spc20 __spc20-64 tip" title="盲僧">盲僧</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=TTVlateroviann99" class="Link" target='_blank'>TTVlateroviann99</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-118 tip" title="解脱者">解脱者</div>
								<div class="Image20 __sprite __spc20 __spc20-118 tip" title="解脱者">解脱者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=2021Worlds0019" class="Link" target='_blank'>2021Worlds0019</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-68 tip" title="圣枪游侠">圣枪游侠</div>
								<div class="Image20 __sprite __spc20 __spc20-68 tip" title="圣枪游侠">圣枪游侠</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=VER+Yusa" class="Link" target='_blank'>VER Yusa</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
								<div class="Image20 __sprite __spc20 __spc20-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-128 tip" title="蛮族之王">蛮族之王</div>
								<div class="Image20 __sprite __spc20 __spc20-128 tip" title="蛮族之王">蛮族之王</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=PD+Zapdo" class="Link" target='_blank'>PD Zapdo</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-139 tip" title="破败之王">破败之王</div>
								<div class="Image20 __sprite __spc20 __spc20-139 tip" title="破败之王">破败之王</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=LngLng" class="Link" target='_blank'>LngLng</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-87 tip" title="发条魔灵">发条魔灵</div>
								<div class="Image20 __sprite __spc20 __spc20-87 tip" title="发条魔灵">发条魔灵</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=LGBTQJPGMD" class="Link" target='_blank'>LGBTQJPGMD</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-28 tip" title="探险家">探险家</div>
								<div class="Image20 __sprite __spc20 __spc20-28 tip" title="探险家">探险家</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=666+reverse+999" class="Link" target='_blank'>666 reverse 999</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-150 tip" title="魔法猫咪">魔法猫咪</div>
								<div class="Image20 __sprite __spc20 __spc20-150 tip" title="魔法猫咪">魔法猫咪</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=nrmn" class="Link" target='_blank'>nrmn</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
															<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-194 Off"></span>
								<span class="__spSite __spSite-193 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Lose  "
	     data-summoner-id="135515503"
	     data-game-time="1633561016"
	     data-game-id="5494863427"
	     data-game-result="lose"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633561016' data-type='' data-interval='60'>2021-10-07 07:56:56</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											失败									</div>
									<div class="GameLength">25分 39秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/lucian/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Lucian.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="圣枪游侠"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerExhaust.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;虚弱&lt;/b&gt;&lt;br&gt;&lt;span&gt;虚弱目标敌方英雄，降低其30%的移动速度，并使其造成的伤害减少40%，持续3秒。&lt;/span&gt;" alt="虚弱">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8005.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;强攻&lt;/b&gt;&lt;br&gt;&lt;span&gt;用3次连续的普攻命中一名敌方英雄时，将造成40 - 180的额外&lt;lol-uikit-tooltipped-keyword key=&#039;LinkTooltip_Description_AdaptiveDmg&#039;&gt;&lt;font color=&#039;#48C4B7&#039;&gt;自适应伤害&lt;/font&gt;&lt;/lol-uikit-tooltipped-keyword&gt;（基于等级）并使其进入易损状态，让其所受的来自任意来源的伤害提升8 - 12%，持续6秒。&lt;/span&gt;" alt="强攻">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/lucian/statistics" target="_blank">圣枪游侠</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">6</span> /
					<span class="Death">10</span> /
					<span class="Assist">11</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">1.70:1</span> KDA				</div>
																								</div>
			<div class="Stats">
				<div class="Level">
					等级12
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 124  + 野怪 0&lt;br&gt;每分钟CS4.8个">124 (4.8)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  61%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Grandmaster</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3508.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;夺萃之镰&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;45&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;20%&lt;/attention&gt;暴击几率&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;咒刃：&lt;/passive&gt;施放技能后，你的下一次普通攻击会因强化而附带额外的&lt;physicalDamage&gt;100%基础攻击力 + 40%额外攻击力的物理伤害&lt;/physicalDamage&gt;&lt;OnHit&gt;攻击特效&lt;/OnHit&gt;并回复相当于40%该伤害值的法力值(1.5秒冷却时间)。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2800 (400)&lt;/span&gt;" alt="夺萃之镰">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/1038.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;暴风之剑&lt;/b&gt;&lt;br&gt;&lt;span&gt;显著提升攻击力&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;40&lt;/attention&gt;攻击力&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1300 (1300)&lt;/span&gt;" alt="暴风之剑">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/6672.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;海妖杀手&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;65&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;25%&lt;/attention&gt;攻击速度&lt;br&gt;&lt;attention&gt;20%&lt;/attention&gt;暴击几率&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;放倒它：&lt;/passive&gt; 每第三次攻击造成额外的&lt;trueDamage&gt;(60+45%额外攻击力)真实伤害&lt;/trueDamage&gt;。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;10%&lt;/attention&gt;攻击速度。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;3400 (625)&lt;/span&gt;" alt="海妖杀手">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3363.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;远见改造&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升施放距离并揭示目标区域&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;显形4000码内的一个区域并放置一个可见且脆弱的守卫。友军无法将这个守卫作为召唤师技能或技能的目标&lt;scaleLevel&gt;(198 - 99秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="远见改造">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3006.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;狂战士胫甲&lt;/b&gt;&lt;br&gt;&lt;span&gt;增强移动速度和攻击速度&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;35%&lt;/attention&gt;攻击速度&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (500)&lt;/span&gt;" alt="狂战士胫甲">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/1055.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;多兰之刃&lt;/b&gt;&lt;br&gt;&lt;span&gt;普攻型英雄的优秀起始装备&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;8&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;80&lt;/attention&gt;生命值&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;好战者：&lt;/passive&gt;获得&lt;lifeSteal&gt;2.5%全能吸血&lt;/lifeSteal&gt;。&lt;br&gt;&lt;br&gt;&lt;rules&gt;在造成群体伤害或通过宠物造成伤害时，全能吸血只有33%效能。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;450 (450)&lt;/span&gt;" alt="多兰之刃">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/1018.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;灵巧披风&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升暴击几率&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;15%&lt;/attention&gt;暴击几率&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;600 (600)&lt;/span&gt;" alt="灵巧披风">
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-red.png">
												Control Ward <span class='wards vision'>1</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-37 tip" title="法外狂徒">法外狂徒</div>
								<div class="Image20 __sprite __spc20 __spc20-37 tip" title="法外狂徒">法外狂徒</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=IAimToMisbehave" class="Link" target='_blank'>IAimToMisbehave</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-83 tip" title="狂野女猎手">狂野女猎手</div>
								<div class="Image20 __sprite __spc20 __spc20-83 tip" title="狂野女猎手">狂野女猎手</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=SGE+SevenArmy" class="Link" target='_blank'>SGE SevenArmy</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-47 tip" title="未来守护者">未来守护者</div>
								<div class="Image20 __sprite __spc20 __spc20-47 tip" title="未来守护者">未来守护者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=David+Nalbandian" class="Link" target='_blank'>David Nalbandian</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-130 tip" title="瘟疫之源">瘟疫之源</div>
								<div class="Image20 __sprite __spc20 __spc20-130 tip" title="瘟疫之源">瘟疫之源</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Giant+Monster" class="Link" target='_blank'>Giant Monster</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-94 tip" title="幻翎">幻翎</div>
								<div class="Image20 __sprite __spc20 __spc20-94 tip" title="幻翎">幻翎</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=PARUS+2" class="Link" target='_blank'>PARUS 2</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-71 tip" title="熔岩巨兽">熔岩巨兽</div>
								<div class="Image20 __sprite __spc20 __spc20-71 tip" title="熔岩巨兽">熔岩巨兽</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=nap+ability" class="Link" target='_blank'>nap ability</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-92 tip" title="元素女皇">元素女皇</div>
								<div class="Image20 __sprite __spc20 __spc20-92 tip" title="元素女皇">元素女皇</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=JUNGKING1" class="Link" target='_blank'>JUNGKING1</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-140 tip" title="机械先驱">机械先驱</div>
								<div class="Image20 __sprite __spc20 __spc20-140 tip" title="机械先驱">机械先驱</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Smooth+Guy" class="Link" target='_blank'>Smooth Guy</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-68 tip" title="圣枪游侠">圣枪游侠</div>
								<div class="Image20 __sprite __spc20 __spc20-68 tip" title="圣枪游侠">圣枪游侠</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
								<div class="Image20 __sprite __spc20 __spc20-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=PQPAANLS" class="Link" target='_blank'>PQPAANLS</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																							<div class="Item">
								<a id="right_match_replay" href="#" class="Button Replay OpenSpectateButton">
									<span class="__spSite __spSite-159"></span></a>
							</div>
																<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-198 Off"></span>
								<span class="__spSite __spSite-197 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Lose  "
	     data-summoner-id="135515503"
	     data-game-time="1633559141"
	     data-game-id="5494819503"
	     data-game-result="lose"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633559141' data-type='' data-interval='60'>2021-10-07 07:25:41</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											失败									</div>
									<div class="GameLength">29分 22秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/leona/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Leona.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="曙光女神"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;引燃&lt;/b&gt;&lt;br&gt;&lt;span&gt;引燃是对单体敌方目标施放的持续性伤害技能，在5秒的持续时间里造成70-410（取决于英雄等级）真实伤害，获得目标的视野，并减少目标所受的治疗和回复效果。&lt;/span&gt;" alt="引燃">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8439.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;余震&lt;/b&gt;&lt;br&gt;&lt;span&gt;在定身住一名敌方英雄后，使你的护甲和魔法抗性提升35+你80%的额外双抗，持续2.5秒。随后会爆炸，对附近的敌人造成魔法伤害。&lt;br&gt;&lt;br&gt;伤害值：25 - 120 (+你8%的额外生命值)&lt;br&gt;冷却时间：20秒&lt;br&gt;&lt;br&gt;来自余震的双抗加成封顶值：80-150(基于等级)&lt;br&gt;&lt;/span&gt;" alt="余震">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/leona/statistics" target="_blank">曙光女神</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">3</span> /
					<span class="Death">9</span> /
					<span class="Assist">16</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">2.11:1</span> KDA				</div>
																								</div>
			<div class="Stats">
				<div class="Level">
					等级13
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 39  + 野怪 0&lt;br&gt;每分钟CS1.3个">39 (1.3)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  44%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Master</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3857.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;白岩肩铠&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;15&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;250&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础生命回复&lt;br&gt;&lt;attention&gt;3&lt;/attention&gt;金币/10秒&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存0个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt; &lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存4个侦察守卫，并在访问商店时补满。 &lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="白岩肩铠">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3190.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;钢铁烈阳之匣&lt;/b&gt;&lt;br&gt;&lt;span&gt;主动施放来为附近友军提供吸收伤害的护盾&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;护甲&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;魔法抗性&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;虔诚：&lt;/active&gt;为附近友军提供&lt;shield&gt;230 - 385(基于友军等级)护盾&lt;/shield&gt;，在2.5秒里持续衰减(90秒冷却时间)。&lt;br&gt;&lt;li&gt;&lt;passive&gt;奉献：&lt;/passive&gt;为附近友方英雄提供&lt;scaleArmor&gt;5护甲&lt;/scaleArmor&gt;和&lt;scaleMR&gt;魔法抗性&lt;/scaleMR&gt;。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;2&lt;/attention&gt;护甲/魔法抗性加成至&lt;passive&gt;奉献&lt;/passive&gt;。&lt;br&gt;&lt;br&gt;&lt;rules&gt;加成效果的强度是基于该友方英雄的等级。&lt;br&gt;20秒内的后续&lt;active&gt;奉献&lt;/active&gt;的护盾仅有25%效果。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2500 (200)&lt;/span&gt;" alt="钢铁烈阳之匣">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3143.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;兰顿之兆&lt;/b&gt;&lt;br&gt;&lt;span&gt;显著提升防御属性，主动施放来减速身边的敌人&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;250&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;80&lt;/attention&gt;护甲&lt;br&gt;&lt;attention&gt;10&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;谦卑：&lt;/active&gt;暂时使附近敌人&lt;status&gt;减速&lt;/status&gt;并使其&lt;scaleAD&gt;攻击力&lt;/scaleAD&gt;降低10%，暴击伤害降低 20%，持续4秒(60秒冷却时间)。&lt;br&gt;&lt;li&gt;&lt;passive&gt;坚如磐石：&lt;/passive&gt;使所受的来自普攻的伤害至多降低5+(0.35%最大生命值)，至多为该次攻击伤害的40%。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2700 (600)&lt;/span&gt;" alt="兰顿之兆">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3364.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;神谕透镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;持续期间可瘫痪附近隐形的守卫和陷阱&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;扫描你的周围，预警隐藏的敌方单位，并使隐形的陷阱显形，并使附近的敌方侦察守卫显形(并暂时失效)10秒&lt;scaleLevel&gt;(90 - 60秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="神谕透镜">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2055.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;控制守卫&lt;/b&gt;&lt;br&gt;&lt;span&gt;用来使范围内的守卫和隐形陷阱失效。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 消耗：&lt;/active&gt;放置一个强大的控制守卫来提供附近区域的视野。这个设备还会使&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;的陷阱显形，使&lt;keywordStealth&gt;伪装&lt;/keywordStealth&gt;的敌人们显形，并使敌方守卫显形和失效。 &lt;br&gt;&lt;br&gt;&lt;rules&gt;你至多可以携带2个控制守卫。控制守卫不会使其它控制守卫失效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;75 (75)&lt;/span&gt;" alt="控制守卫">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/1028.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;红水晶&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升生命值&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;150&lt;/attention&gt;生命值&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="红水晶">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3047.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;铁板靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;增强移动速度并减少即将到来的普攻伤害&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;20&lt;/attention&gt;护甲&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;br&gt;&lt;li&gt;使即将到来的攻击伤害降低12%。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (500)&lt;/span&gt;" alt="铁板靴">
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-red.png">
												Control Ward <span class='wards vision'>14</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-37 tip" title="法外狂徒">法外狂徒</div>
								<div class="Image20 __sprite __spc20 __spc20-37 tip" title="法外狂徒">法外狂徒</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Kimchi3" class="Link" target='_blank'>Kimchi3</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-85 tip" title="雪原双子">雪原双子</div>
								<div class="Image20 __sprite __spc20 __spc20-85 tip" title="雪原双子">雪原双子</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=PD+Zapdo" class="Link" target='_blank'>PD Zapdo</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-148 tip" title="封魔剑魂">封魔剑魂</div>
								<div class="Image20 __sprite __spc20 __spc20-148 tip" title="封魔剑魂">封魔剑魂</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=2021Worlds0019" class="Link" target='_blank'>2021Worlds0019</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-68 tip" title="圣枪游侠">圣枪游侠</div>
								<div class="Image20 __sprite __spc20 __spc20-68 tip" title="圣枪游侠">圣枪游侠</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Giant+Monster" class="Link" target='_blank'>Giant Monster</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
								<div class="Image20 __sprite __spc20 __spc20-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Targamas" class="Link" target='_blank'>Targamas</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-111 tip" title="炼金术士">炼金术士</div>
								<div class="Image20 __sprite __spc20 __spc20-111 tip" title="炼金术士">炼金术士</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Ragn%C3%A9r3" class="Link" target='_blank'>Ragnér3</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-96 tip" title="虚空遁地兽">虚空遁地兽</div>
								<div class="Image20 __sprite __spc20 __spc20-96 tip" title="虚空遁地兽">虚空遁地兽</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=asdfghjklqwe" class="Link" target='_blank'>asdfghjklqwe</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-6 tip" title="冰晶凤凰">冰晶凤凰</div>
								<div class="Image20 __sprite __spc20 __spc20-6 tip" title="冰晶凤凰">冰晶凤凰</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Walid+Georgey" class="Link" target='_blank'>Walid Georgey</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-75 tip" title="赏金猎人">赏金猎人</div>
								<div class="Image20 __sprite __spc20 __spc20-75 tip" title="赏金猎人">赏金猎人</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=WKR+Marth" class="Link" target='_blank'>WKR Marth</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-65 tip" title="曙光女神">曙光女神</div>
								<div class="Image20 __sprite __spc20 __spc20-65 tip" title="曙光女神">曙光女神</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																							<div class="Item">
								<a id="right_match_replay" href="#" class="Button Replay OpenSpectateButton">
									<span class="__spSite __spSite-159"></span></a>
							</div>
																<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-198 Off"></span>
								<span class="__spSite __spSite-197 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Lose  "
	     data-summoner-id="135515503"
	     data-game-time="1633557028"
	     data-game-id="5494854782"
	     data-game-result="lose"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633557028' data-type='' data-interval='60'>2021-10-07 06:50:28</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											失败									</div>
									<div class="GameLength">28分 25秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/nami/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Nami.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="唤潮鲛姬"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;引燃&lt;/b&gt;&lt;br&gt;&lt;span&gt;引燃是对单体敌方目标施放的持续性伤害技能，在5秒的持续时间里造成70-410（取决于英雄等级）真实伤害，获得目标的视野，并减少目标所受的治疗和回复效果。&lt;/span&gt;" alt="引燃">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8112.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;电刑&lt;/b&gt;&lt;br&gt;&lt;span&gt;在3秒内用3个&lt;b&gt;独立的&lt;/b&gt;攻击或技能命中一位英雄时，会造成额外的&lt;lol-uikit-tooltipped-keyword key=&#039;LinkTooltip_Description_AdaptiveDmg&#039;&gt;&lt;font color=&#039;#48C4B7&#039;&gt;自适应伤害&lt;/font&gt;&lt;/lol-uikit-tooltipped-keyword&gt;。&lt;br&gt;&lt;br&gt;伤害值：30 - 180 (+0.4额外攻击力, +0.25法术强度)。&lt;br&gt;&lt;br&gt;冷却时间：25 - 20秒&lt;br&gt;&lt;br&gt;&lt;hr&gt;&lt;i&gt;“我们曾称呼他们为“雷霆领主”，是因为他们的闪电招来了灾祸。”&lt;/i&gt;&lt;/span&gt;" alt="电刑">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/nami/statistics" target="_blank">唤潮鲛姬</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">1</span> /
					<span class="Death">5</span> /
					<span class="Assist">16</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">3.40:1</span> KDA				</div>
																								</div>
			<div class="Stats">
				<div class="Level">
					等级13
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 6  + 野怪 0&lt;br&gt;每分钟CS0.2个">6 (0.2)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  65%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Grandmaster</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3853.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;极冰碎片&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;40&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;75&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础法力回复&lt;br&gt;&lt;attention&gt;3&lt;/attention&gt;金币/10秒&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存0个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存4个侦察守卫，并在访问商店时补满。 &lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="极冰碎片">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2055.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;控制守卫&lt;/b&gt;&lt;br&gt;&lt;span&gt;用来使范围内的守卫和隐形陷阱失效。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 消耗：&lt;/active&gt;放置一个强大的控制守卫来提供附近区域的视野。这个设备还会使&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;的陷阱显形，使&lt;keywordStealth&gt;伪装&lt;/keywordStealth&gt;的敌人们显形，并使敌方守卫显形和失效。 &lt;br&gt;&lt;br&gt;&lt;rules&gt;你至多可以携带2个控制守卫。控制守卫不会使其它控制守卫失效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;75 (75)&lt;/span&gt;" alt="控制守卫">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2420.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;秒表&lt;/b&gt;&lt;br&gt;&lt;span&gt;主动施放来变得无敌但无法行动&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - &lt;/active&gt; &lt;active&gt;凝滞：&lt;/active&gt;一次性使用，在2.5秒里&lt;status&gt;免疫伤害&lt;/status&gt;且&lt;status&gt;不可被选取&lt;/status&gt;，但在此期间里无法采取任何其它行动(转变为一个&lt;rarityGeneric&gt;破损的秒表&lt;/rarityGeneric&gt;)。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;650 (650)&lt;/span&gt;" alt="秒表">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3364.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;神谕透镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;持续期间可瘫痪附近隐形的守卫和陷阱&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;扫描你的周围，预警隐藏的敌方单位，并使隐形的陷阱显形，并使附近的敌方侦察守卫显形(并暂时失效)10秒&lt;scaleLevel&gt;(90 - 60秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="神谕透镜">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/4005.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;帝国指令&lt;/b&gt;&lt;br&gt;&lt;span&gt;将伤害延后。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;40&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础法力回复&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;协同开火：&lt;/passive&gt;技能在&lt;status&gt;减速&lt;/status&gt;或&lt;status&gt;定身&lt;/status&gt;一名英雄时会造成&lt;magicDamage&gt;45 - 75(基于等级)额外魔法伤害&lt;/magicDamage&gt;并将其标记4秒(每个敌方英雄有6秒冷却时间)。友方英雄的伤害会引爆标记，造成额外的&lt;magicDamage&gt;90 - 150(基于友军等级)魔法伤害&lt;/magicDamage&gt;并为你和该友军都提供&lt;speed&gt;20%移动速度&lt;/speed&gt;，持续2秒。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;15&lt;/attention&gt;法术强度。&lt;br&gt;&lt;br&gt;&lt;rules&gt;加成效果的强度是基于该友方英雄的等级。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2500 (750)&lt;/span&gt;" alt="帝国指令">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3158.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;明朗之靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升移动速度和冷却缩减&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;br&gt;&lt;li&gt;提供12召唤师技能急速。&lt;br&gt;&lt;br&gt;&lt;flavorText&gt;“这个物品是为了庆祝在2010年12月10日艾欧尼亚和诺克萨斯的重赛中，艾欧尼亚取得胜利。”&lt;/flavorText&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;950 (650)&lt;/span&gt;" alt="明朗之靴">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3011.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;炼金科技纯化器&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;55&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础法力回复&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;芙顶之毒：&lt;/passive&gt;对英雄们造成魔法伤害时会施加&lt;status&gt;40%重伤&lt;/status&gt;效果，持续3秒。对另一名友方英雄提供治疗或护盾时，会使你和该英雄都获得强化，在下一次伤害敌方英雄时施加&lt;status&gt;60%重伤&lt;/status&gt;效果。&lt;br&gt;&lt;br&gt;&lt;rules&gt;&lt;status&gt;重伤&lt;/status&gt;会降低治疗效果和生命回复的效能。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2300 (550)&lt;/span&gt;" alt="炼金科技纯化器">
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-red.png">
												Control Ward <span class='wards vision'>14</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-0 tip" title="暗裔剑魔">暗裔剑魔</div>
								<div class="Image20 __sprite __spc20 __spc20-0 tip" title="暗裔剑魔">暗裔剑魔</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Firefl0wer" class="Link" target='_blank'>Firefl0wer</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-25 tip" title="时间刺客">时间刺客</div>
								<div class="Image20 __sprite __spc20 __spc20-25 tip" title="时间刺客">时间刺客</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=TwTv+J3kko1" class="Link" target='_blank'>TwTv J3kko1</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-152 tip" title="影流之主">影流之主</div>
								<div class="Image20 __sprite __spc20 __spc20-152 tip" title="影流之主">影流之主</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=TwTv+Ronges1" class="Link" target='_blank'>TwTv Ronges1</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-68 tip" title="圣枪游侠">圣枪游侠</div>
								<div class="Image20 __sprite __spc20 __spc20-68 tip" title="圣枪游侠">圣枪游侠</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=WTX+Scripter" class="Link" target='_blank'>WTX Scripter</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
								<div class="Image20 __sprite __spc20 __spc20-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-107 tip" title="腕豪">腕豪</div>
								<div class="Image20 __sprite __spc20 __spc20-107 tip" title="腕豪">腕豪</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=ANB+9eetoo" class="Link" target='_blank'>ANB 9eetoo</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-122 tip" title="刀锋之影">刀锋之影</div>
								<div class="Image20 __sprite __spc20 __spc20-122 tip" title="刀锋之影">刀锋之影</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=gaengsin" class="Link" target='_blank'>gaengsin</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-54 tip" title="虚空行者">虚空行者</div>
								<div class="Image20 __sprite __spc20 __spc20-54 tip" title="虚空行者">虚空行者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=I+Love+Winner" class="Link" target='_blank'>I Love Winner</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-28 tip" title="探险家">探险家</div>
								<div class="Image20 __sprite __spc20 __spc20-28 tip" title="探险家">探险家</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=HoIyPhoen%C3%AEx" class="Link" target='_blank'>HoIyPhoenîx</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-150 tip" title="魔法猫咪">魔法猫咪</div>
								<div class="Image20 __sprite __spc20 __spc20-150 tip" title="魔法猫咪">魔法猫咪</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=KwK+AlVaRo710" class="Link" target='_blank'>KwK AlVaRo710</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																							<div class="Item">
								<a id="right_match_replay" href="#" class="Button Replay OpenSpectateButton">
									<span class="__spSite __spSite-159"></span></a>
							</div>
																<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-198 Off"></span>
								<span class="__spSite __spSite-197 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Lose  "
	     data-summoner-id="135515503"
	     data-game-time="1633554773"
	     data-game-id="5494790996"
	     data-game-result="lose"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633554773' data-type='' data-interval='60'>2021-10-07 06:12:53</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											失败									</div>
									<div class="GameLength">20分 50秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/rell/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Rell.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="镕铁少女"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;引燃&lt;/b&gt;&lt;br&gt;&lt;span&gt;引燃是对单体敌方目标施放的持续性伤害技能，在5秒的持续时间里造成70-410（取决于英雄等级）真实伤害，获得目标的视野，并减少目标所受的治疗和回复效果。&lt;/span&gt;" alt="引燃">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8439.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;余震&lt;/b&gt;&lt;br&gt;&lt;span&gt;在定身住一名敌方英雄后，使你的护甲和魔法抗性提升35+你80%的额外双抗，持续2.5秒。随后会爆炸，对附近的敌人造成魔法伤害。&lt;br&gt;&lt;br&gt;伤害值：25 - 120 (+你8%的额外生命值)&lt;br&gt;冷却时间：20秒&lt;br&gt;&lt;br&gt;来自余震的双抗加成封顶值：80-150(基于等级)&lt;br&gt;&lt;/span&gt;" alt="余震">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/rell/statistics" target="_blank">镕铁少女</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">1</span> /
					<span class="Death">4</span> /
					<span class="Assist">9</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">2.50:1</span> KDA				</div>
																							<div class="Badge"><span class="Text ACE">ACE</span></div>
												</div>
			<div class="Stats">
				<div class="Level">
					等级9
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 32  + 野怪 4&lt;br&gt;每分钟CS1.7个">36 (1.7)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  63%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Grandmaster</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3859.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;巨神峰圆盾&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;10&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;100&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;50%&lt;/attention&gt;基础生命回复&lt;br&gt;&lt;attention&gt;3&lt;/attention&gt;金币/10秒&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存0个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt; &lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存3个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;li&gt;&lt;passive&gt;战利品：&lt;/passive&gt;附近有一名友方英雄时，普攻会处决低于50%最大生命值的小兵。击杀一位小兵会为距离最近的友方英雄提供等量的击杀金币。这些效果每35秒获得一层充能(最多拥有3层充能)。&lt;li&gt;&lt;passive&gt;任务：&lt;/passive&gt;使用这个装备赚取1000金币来将其转变为&lt;rarityLegendary&gt;山脉壁垒&lt;/rarityLegendary&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="巨神峰圆盾">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3190.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;钢铁烈阳之匣&lt;/b&gt;&lt;br&gt;&lt;span&gt;主动施放来为附近友军提供吸收伤害的护盾&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;护甲&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;魔法抗性&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;虔诚：&lt;/active&gt;为附近友军提供&lt;shield&gt;230 - 385(基于友军等级)护盾&lt;/shield&gt;，在2.5秒里持续衰减(90秒冷却时间)。&lt;br&gt;&lt;li&gt;&lt;passive&gt;奉献：&lt;/passive&gt;为附近友方英雄提供&lt;scaleArmor&gt;5护甲&lt;/scaleArmor&gt;和&lt;scaleMR&gt;魔法抗性&lt;/scaleMR&gt;。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;2&lt;/attention&gt;护甲/魔法抗性加成至&lt;passive&gt;奉献&lt;/passive&gt;。&lt;br&gt;&lt;br&gt;&lt;rules&gt;加成效果的强度是基于该友方英雄的等级。&lt;br&gt;20秒内的后续&lt;active&gt;奉献&lt;/active&gt;的护盾仅有25%效果。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2500 (200)&lt;/span&gt;" alt="钢铁烈阳之匣">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2055.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;控制守卫&lt;/b&gt;&lt;br&gt;&lt;span&gt;用来使范围内的守卫和隐形陷阱失效。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 消耗：&lt;/active&gt;放置一个强大的控制守卫来提供附近区域的视野。这个设备还会使&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;的陷阱显形，使&lt;keywordStealth&gt;伪装&lt;/keywordStealth&gt;的敌人们显形，并使敌方守卫显形和失效。 &lt;br&gt;&lt;br&gt;&lt;rules&gt;你至多可以携带2个控制守卫。控制守卫不会使其它控制守卫失效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;75 (75)&lt;/span&gt;" alt="控制守卫">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3364.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;神谕透镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;持续期间可瘫痪附近隐形的守卫和陷阱&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;扫描你的周围，预警隐藏的敌方单位，并使隐形的陷阱显形，并使附近的敌方侦察守卫显形(并暂时失效)10秒&lt;scaleLevel&gt;(90 - 60秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="神谕透镜">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/1028.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;红水晶&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升生命值&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;150&lt;/attention&gt;生命值&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="红水晶">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3111.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;水银之靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升移动速度并降低限制效果的时长&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;25&lt;/attention&gt;魔法抗性&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;br&gt;&lt;attention&gt;30%&lt;/attention&gt;韧性&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;rules&gt;韧性会减少&lt;status&gt;晕眩&lt;/status&gt;、&lt;status&gt;减速&lt;/status&gt;、&lt;status&gt;嘲讽&lt;/status&gt;、&lt;status&gt;恐惧&lt;/status&gt;、&lt;status&gt;沉默&lt;/status&gt;、&lt;status&gt;致盲&lt;/status&gt;、&lt;status&gt;变形&lt;/status&gt;和&lt;status&gt;定身&lt;/status&gt;效果的持续时间。它对&lt;status&gt;浮空&lt;/status&gt;或&lt;status&gt;压制&lt;/status&gt;效果无效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (350)&lt;/span&gt;" alt="水银之靴">
													</div>
																							<div class="Item">
															<div class="Image NoItem"></div>
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-red.png">
												Control Ward <span class='wards vision'>10</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-0 tip" title="暗裔剑魔">暗裔剑魔</div>
								<div class="Image20 __sprite __spc20 __spc20-0 tip" title="暗裔剑魔">暗裔剑魔</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=JBL+ABUSER" class="Link" target='_blank'>JBL ABUSER</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-139 tip" title="破败之王">破败之王</div>
								<div class="Image20 __sprite __spc20 __spc20-139 tip" title="破败之王">破败之王</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=2021Worlds" class="Link" target='_blank'>2021Worlds</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-6 tip" title="冰晶凤凰">冰晶凤凰</div>
								<div class="Image20 __sprite __spc20 __spc20-6 tip" title="冰晶凤凰">冰晶凤凰</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=PEWPEWPEWPEWPEWP" class="Link" target='_blank'>PEWPEWPEWPEWPEWP</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-126 tip" title="麦林炮手">麦林炮手</div>
								<div class="Image20 __sprite __spc20 __spc20-126 tip" title="麦林炮手">麦林炮手</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=its+all+a+joke" class="Link" target='_blank'>its all a joke</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-97 tip" title="镕铁少女">镕铁少女</div>
								<div class="Image20 __sprite __spc20 __spc20-97 tip" title="镕铁少女">镕铁少女</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-37 tip" title="法外狂徒">法外狂徒</div>
								<div class="Image20 __sprite __spc20 __spc20-37 tip" title="法外狂徒">法外狂徒</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Le+petit+baguett" class="Link" target='_blank'>Le petit baguett</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-29 tip" title="远古恐惧">远古恐惧</div>
								<div class="Image20 __sprite __spc20 __spc20-29 tip" title="远古恐惧">远古恐惧</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=EUW+VILLAIN" class="Link" target='_blank'>EUW VILLAIN</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-92 tip" title="元素女皇">元素女皇</div>
								<div class="Image20 __sprite __spc20 __spc20-92 tip" title="元素女皇">元素女皇</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=I+Love+Winner" class="Link" target='_blank'>I Love Winner</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-68 tip" title="圣枪游侠">圣枪游侠</div>
								<div class="Image20 __sprite __spc20 __spc20-68 tip" title="圣枪游侠">圣枪游侠</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=WTX+Scripter" class="Link" target='_blank'>WTX Scripter</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
								<div class="Image20 __sprite __spc20 __spc20-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Frank+Horrigan" class="Link" target='_blank'>Frank Horrigan</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																							<div class="Item">
								<a id="right_match_replay" href="#" class="Button Replay OpenSpectateButton">
									<span class="__spSite __spSite-159"></span></a>
							</div>
																<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-198 Off"></span>
								<span class="__spSite __spSite-197 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Win  "
	     data-summoner-id="135515503"
	     data-game-time="1633553155"
	     data-game-id="5494746446"
	     data-game-result="win"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633553155' data-type='' data-interval='60'>2021-10-07 05:45:55</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											胜利									</div>
									<div class="GameLength">20分 50秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/kaisa/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Kaisa.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="虚空之女"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerExhaust.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;虚弱&lt;/b&gt;&lt;br&gt;&lt;span&gt;虚弱目标敌方英雄，降低其30%的移动速度，并使其造成的伤害减少40%，持续3秒。&lt;/span&gt;" alt="虚弱">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/9923.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;丛刃&lt;/b&gt;&lt;br&gt;&lt;span&gt;在攻击敌方英雄时，提供110%攻击速度给最先的3次攻击。&lt;br&gt;&lt;br&gt;每次攻击的间隔不能超过3秒，否则这个效果就会结束。&lt;br&gt;&lt;br&gt;冷却时间：12秒。&lt;br&gt;&lt;br&gt;&lt;rules&gt;被重置的攻击会使攻击次数上限提升1。&lt;br&gt;&lt;br&gt;允许你暂时溢出你的攻击速度上限。&lt;/rules&gt;&lt;/span&gt;" alt="丛刃">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/kaisa/statistics" target="_blank">虚空之女</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">7</span> /
					<span class="Death">3</span> /
					<span class="Assist">14</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">7.00:1</span> KDA				</div>
																								</div>
			<div class="Stats">
				<div class="Level">
					等级12
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 134  + 野怪 8&lt;br&gt;每分钟CS6.8个">142 (6.8)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  50%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Grandmaster</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/6671.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;狂风之力&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;60&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;20%&lt;/attention&gt;攻击速度&lt;br&gt;&lt;attention&gt;20%&lt;/attention&gt;暴击几率&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;暴雨：&lt;/active&gt;朝着目标方向冲刺，同时对你终点附近生命值最低的敌人(优先英雄)发射3个弹体。共造成&lt;magicDamage&gt;(180 - 220(基于等级) + 45%额外攻击力)魔法伤害&lt;/magicDamage&gt;，对低生命值的目标时至多提升50%(90秒冷却时间)。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;2%&lt;/attention&gt;移动速度&lt;br&gt;&lt;br&gt;&lt;rules&gt;弹体伤害在敌人生命值低于30%时达到最大值。&lt;br&gt;【暴雨】的冲刺无法穿过地形。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;3400 (625)&lt;/span&gt;" alt="狂风之力">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3085.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;卢安娜的飓风&lt;/b&gt;&lt;br&gt;&lt;span&gt;远程攻击会对目标身边的2个敌人发射弩箭&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;45%&lt;/attention&gt;攻击速度&lt;br&gt;&lt;attention&gt;20%&lt;/attention&gt;暴击几率&lt;br&gt;&lt;attention&gt;7%&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;风怒：&lt;/passive&gt;你的普通攻击会朝目标附近的至多2个敌人发射弩箭，每支弩箭造成&lt;physicalDamage&gt;(40%攻击力)物理伤害&lt;/physicalDamage&gt;。这些弩箭能够附带攻击特效并且可以暴击。&lt;br&gt;&lt;br&gt;&lt;rules&gt;这件装备仅远程英雄可用。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2600 (950)&lt;/span&gt;" alt="卢安娜的飓风">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/6676.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;收集者&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;55&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;20%&lt;/attention&gt;暴击几率&lt;br&gt;&lt;attention&gt;12&lt;/attention&gt;穿甲&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;死与税：&lt;/passive&gt;如果你造成的伤害将使一名敌方英雄的生命值跌到5%以下，那么会直接将其处决。击杀英雄时会为你提供额外的25金币。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;3000 (425)&lt;/span&gt;" alt="收集者">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3363.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;远见改造&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升施放距离并揭示目标区域&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;显形4000码内的一个区域并放置一个可见且脆弱的守卫。友军无法将这个守卫作为召唤师技能或技能的目标&lt;scaleLevel&gt;(198 - 99秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="远见改造">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3006.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;狂战士胫甲&lt;/b&gt;&lt;br&gt;&lt;span&gt;增强移动速度和攻击速度&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;35%&lt;/attention&gt;攻击速度&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (500)&lt;/span&gt;" alt="狂战士胫甲">
													</div>
																							<div class="Item">
															<div class="Image NoItem"></div>
													</div>
																							<div class="Item">
															<div class="Image NoItem"></div>
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildblue-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildblue-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-blue.png">
												Control Ward <span class='wards vision'>2</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-0 tip" title="暗裔剑魔">暗裔剑魔</div>
								<div class="Image20 __sprite __spc20 __spc20-0 tip" title="暗裔剑魔">暗裔剑魔</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Chres" class="Link" target='_blank'>Chres</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-57 tip" title="影流之镰">影流之镰</div>
								<div class="Image20 __sprite __spc20 __spc20-57 tip" title="影流之镰">影流之镰</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=2021Worlds" class="Link" target='_blank'>2021Worlds</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-118 tip" title="解脱者">解脱者</div>
								<div class="Image20 __sprite __spc20 __spc20-118 tip" title="解脱者">解脱者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=agdang" class="Link" target='_blank'>agdang</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-50 tip" title="虚空之女">虚空之女</div>
								<div class="Image20 __sprite __spc20 __spc20-50 tip" title="虚空之女">虚空之女</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
								<div class="Image20 __sprite __spc20 __spc20-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Gilius1" class="Link" target='_blank'>Gilius1</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-42 tip" title="刀锋舞者">刀锋舞者</div>
								<div class="Image20 __sprite __spc20 __spc20-42 tip" title="刀锋舞者">刀锋舞者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=dofaminu" class="Link" target='_blank'>dofaminu</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-29 tip" title="远古恐惧">远古恐惧</div>
								<div class="Image20 __sprite __spc20 __spc20-29 tip" title="远古恐惧">远古恐惧</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=EUW+VILLAIN" class="Link" target='_blank'>EUW VILLAIN</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-47 tip" title="未来守护者">未来守护者</div>
								<div class="Image20 __sprite __spc20 __spc20-47 tip" title="未来守护者">未来守护者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=152cm187kg24cm" class="Link" target='_blank'>152cm187kg24cm</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-130 tip" title="瘟疫之源">瘟疫之源</div>
								<div class="Image20 __sprite __spc20 __spc20-130 tip" title="瘟疫之源">瘟疫之源</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Pinky+windy" class="Link" target='_blank'>Pinky windy</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-150 tip" title="魔法猫咪">魔法猫咪</div>
								<div class="Image20 __sprite __spc20 __spc20-150 tip" title="魔法猫咪">魔法猫咪</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Calmsky" class="Link" target='_blank'>Calmsky</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																							<div class="Item">
								<a id="right_match_replay" href="#" class="Button Replay OpenSpectateButton">
									<span class="__spSite __spSite-159"></span></a>
							</div>
																<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-194 Off"></span>
								<span class="__spSite __spSite-193 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Win  "
	     data-summoner-id="135515503"
	     data-game-time="1633551592"
	     data-game-id="5494661965"
	     data-game-result="win"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633551592' data-type='' data-interval='60'>2021-10-07 05:19:52</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											胜利									</div>
									<div class="GameLength">23分 34秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/nautilus/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Nautilus.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="深海泰坦"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;引燃&lt;/b&gt;&lt;br&gt;&lt;span&gt;引燃是对单体敌方目标施放的持续性伤害技能，在5秒的持续时间里造成70-410（取决于英雄等级）真实伤害，获得目标的视野，并减少目标所受的治疗和回复效果。&lt;/span&gt;" alt="引燃">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8439.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;余震&lt;/b&gt;&lt;br&gt;&lt;span&gt;在定身住一名敌方英雄后，使你的护甲和魔法抗性提升35+你80%的额外双抗，持续2.5秒。随后会爆炸，对附近的敌人造成魔法伤害。&lt;br&gt;&lt;br&gt;伤害值：25 - 120 (+你8%的额外生命值)&lt;br&gt;冷却时间：20秒&lt;br&gt;&lt;br&gt;来自余震的双抗加成封顶值：80-150(基于等级)&lt;br&gt;&lt;/span&gt;" alt="余震">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/nautilus/statistics" target="_blank">深海泰坦</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">1</span> /
					<span class="Death">2</span> /
					<span class="Assist">21</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">11.00:1</span> KDA				</div>
																							<div class="Badge"><span class="Text MVP">MVP</span></div>
												</div>
			<div class="Stats">
				<div class="Level">
					等级13
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 23  + 野怪 4&lt;br&gt;每分钟CS1.1个">27 (1.1)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  58%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Grandmaster</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3857.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;白岩肩铠&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;15&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;250&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础生命回复&lt;br&gt;&lt;attention&gt;3&lt;/attention&gt;金币/10秒&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存0个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt; &lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存4个侦察守卫，并在访问商店时补满。 &lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="白岩肩铠">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3190.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;钢铁烈阳之匣&lt;/b&gt;&lt;br&gt;&lt;span&gt;主动施放来为附近友军提供吸收伤害的护盾&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;护甲&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;魔法抗性&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;虔诚：&lt;/active&gt;为附近友军提供&lt;shield&gt;230 - 385(基于友军等级)护盾&lt;/shield&gt;，在2.5秒里持续衰减(90秒冷却时间)。&lt;br&gt;&lt;li&gt;&lt;passive&gt;奉献：&lt;/passive&gt;为附近友方英雄提供&lt;scaleArmor&gt;5护甲&lt;/scaleArmor&gt;和&lt;scaleMR&gt;魔法抗性&lt;/scaleMR&gt;。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;2&lt;/attention&gt;护甲/魔法抗性加成至&lt;passive&gt;奉献&lt;/passive&gt;。&lt;br&gt;&lt;br&gt;&lt;rules&gt;加成效果的强度是基于该友方英雄的等级。&lt;br&gt;20秒内的后续&lt;active&gt;奉献&lt;/active&gt;的护盾仅有25%效果。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2500 (200)&lt;/span&gt;" alt="钢铁烈阳之匣">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2055.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;控制守卫&lt;/b&gt;&lt;br&gt;&lt;span&gt;用来使范围内的守卫和隐形陷阱失效。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 消耗：&lt;/active&gt;放置一个强大的控制守卫来提供附近区域的视野。这个设备还会使&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;的陷阱显形，使&lt;keywordStealth&gt;伪装&lt;/keywordStealth&gt;的敌人们显形，并使敌方守卫显形和失效。 &lt;br&gt;&lt;br&gt;&lt;rules&gt;你至多可以携带2个控制守卫。控制守卫不会使其它控制守卫失效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;75 (75)&lt;/span&gt;" alt="控制守卫">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3364.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;神谕透镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;持续期间可瘫痪附近隐形的守卫和陷阱&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;扫描你的周围，预警隐藏的敌方单位，并使隐形的陷阱显形，并使附近的敌方侦察守卫显形(并暂时失效)10秒&lt;scaleLevel&gt;(90 - 60秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="神谕透镜">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2421.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;破损的秒表&lt;/b&gt;&lt;br&gt;&lt;span&gt;升级为秒表&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;支离破碎的时间：&lt;/passive&gt;【秒表】目前是破损状态，但仍然可以用于升级。&lt;br&gt;&lt;br&gt;&lt;rules&gt;在打破一个【秒表】后，商店主人就只会卖给你&lt;rarityGeneric&gt;破损的秒表&lt;/rarityGeneric&gt;了。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;650 (650)&lt;/span&gt;" alt="破损的秒表">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3111.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;水银之靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升移动速度并降低限制效果的时长&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;25&lt;/attention&gt;魔法抗性&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;br&gt;&lt;attention&gt;30%&lt;/attention&gt;韧性&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;rules&gt;韧性会减少&lt;status&gt;晕眩&lt;/status&gt;、&lt;status&gt;减速&lt;/status&gt;、&lt;status&gt;嘲讽&lt;/status&gt;、&lt;status&gt;恐惧&lt;/status&gt;、&lt;status&gt;沉默&lt;/status&gt;、&lt;status&gt;致盲&lt;/status&gt;、&lt;status&gt;变形&lt;/status&gt;和&lt;status&gt;定身&lt;/status&gt;效果的持续时间。它对&lt;status&gt;浮空&lt;/status&gt;或&lt;status&gt;压制&lt;/status&gt;效果无效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (350)&lt;/span&gt;" alt="水银之靴">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3067.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;燃烧宝石&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升生命值和冷却缩减&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;10&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;800 (400)&lt;/span&gt;" alt="燃烧宝石">
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildblue-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildblue-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-blue.png">
												Control Ward <span class='wards vision'>10</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-42 tip" title="刀锋舞者">刀锋舞者</div>
								<div class="Image20 __sprite __spc20 __spc20-42 tip" title="刀锋舞者">刀锋舞者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Venour" class="Link" target='_blank'>Venour</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-29 tip" title="远古恐惧">远古恐惧</div>
								<div class="Image20 __sprite __spc20 __spc20-29 tip" title="远古恐惧">远古恐惧</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=EUW+VILLAIN" class="Link" target='_blank'>EUW VILLAIN</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-25 tip" title="时间刺客">时间刺客</div>
								<div class="Image20 __sprite __spc20 __spc20-25 tip" title="时间刺客">时间刺客</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Ekko+the+Neeko" class="Link" target='_blank'>Ekko the Neeko</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-75 tip" title="赏金猎人">赏金猎人</div>
								<div class="Image20 __sprite __spc20 __spc20-75 tip" title="赏金猎人">赏金猎人</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=HoIyPhoen%C3%AEx" class="Link" target='_blank'>HoIyPhoenîx</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-150 tip" title="魔法猫咪">魔法猫咪</div>
								<div class="Image20 __sprite __spc20 __spc20-150 tip" title="魔法猫咪">魔法猫咪</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=srysry" class="Link" target='_blank'>srysry</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-30 tip" title="无双剑姬">无双剑姬</div>
								<div class="Image20 __sprite __spc20 __spc20-30 tip" title="无双剑姬">无双剑姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=chance+no+exist" class="Link" target='_blank'>chance no exist</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-92 tip" title="元素女皇">元素女皇</div>
								<div class="Image20 __sprite __spc20 __spc20-92 tip" title="元素女皇">元素女皇</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Expecto+Patrounm" class="Link" target='_blank'>Expecto Patrounm</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-102 tip" title="符文法师">符文法师</div>
								<div class="Image20 __sprite __spc20 __spc20-102 tip" title="符文法师">符文法师</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=UOL+Cryptodir" class="Link" target='_blank'>UOL Cryptodir</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-68 tip" title="圣枪游侠">圣枪游侠</div>
								<div class="Image20 __sprite __spc20 __spc20-68 tip" title="圣枪游侠">圣枪游侠</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=KIA+MVP" class="Link" target='_blank'>KIA MVP</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-81 tip" title="深海泰坦">深海泰坦</div>
								<div class="Image20 __sprite __spc20 __spc20-81 tip" title="深海泰坦">深海泰坦</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																							<div class="Item">
								<a id="right_match_replay" href="#" class="Button Replay OpenSpectateButton">
									<span class="__spSite __spSite-159"></span></a>
							</div>
																<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-194 Off"></span>
								<span class="__spSite __spSite-193 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Lose  "
	     data-summoner-id="135515503"
	     data-game-time="1633549264"
	     data-game-id="5494644316"
	     data-game-result="lose"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633549264' data-type='' data-interval='60'>2021-10-07 04:41:04</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											失败									</div>
									<div class="GameLength">27分 12秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/ezreal/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Ezreal.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="探险家"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerHeal.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;治疗术&lt;/b&gt;&lt;br&gt;&lt;span&gt;为你和目标友军英雄回复95-345（取决于英雄等级）生命值，并为你和目标友军英雄提供30%移动速度加成，持续1秒。若目标近期已受到过其它治疗术的影响，则治疗术对目标产生的治疗效果减半。&lt;/span&gt;" alt="治疗术">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8010.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;征服者&lt;/b&gt;&lt;br&gt;&lt;span&gt;普通攻击或伤害型技能在命中一名敌方英雄时会提供2层【征服者】效果，持续6秒，每层效果提供2-5&lt;lol-uikit-tooltipped-keyword key=&#039;LinkTooltip_Description_Adaptive&#039;&gt;&lt;font color=&#039;#48C4B7&#039;&gt;适应之力&lt;/font&gt;&lt;/lol-uikit-tooltipped-keyword&gt;。至多可叠加12次。远程英雄的每次普攻只会提供1层效果。&lt;br&gt;&lt;br&gt;在叠满层数后，你对英雄造成的9%伤害会转化为对自身的治疗效果(远程英雄的转化率为6%)。&lt;/span&gt;" alt="征服者">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8200.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;巫术&lt;/b&gt;&lt;br&gt;&lt;span&gt;强化技能和资源控制&lt;/span&gt;" alt="巫术">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/ezreal/statistics" target="_blank">探险家</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">4</span> /
					<span class="Death">7</span> /
					<span class="Assist">5</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">1.29:1</span> KDA				</div>
									<div class="MultiKill">
						<span class="Kill">双杀</span>
					</div>
																								</div>
			<div class="Stats">
				<div class="Level">
					等级13
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 214  + 野怪 5&lt;br&gt;每分钟CS8.1个">219 (8.1)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  50%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Grandmaster</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/6694.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;赛瑞尔达的怨恨&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;45&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;30%&lt;/attention&gt;护甲穿透&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;严寒：&lt;/passive&gt;伤害型技能会使敌人&lt;status&gt;减速&lt;/status&gt;30%，持续1秒。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;3200 (650)&lt;/span&gt;" alt="赛瑞尔达的怨恨">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3078.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;三相之力&lt;/b&gt;&lt;br&gt;&lt;span&gt;成吨的伤害&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;35&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;30%&lt;/attention&gt;攻击速度&lt;br&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;三重打击：&lt;/passive&gt;攻击会提供&lt;speed&gt;20移动速度&lt;/speed&gt;，持续3秒。如果目标是英雄，则提升你&lt;scaleAD&gt;6%基础攻击力&lt;/scaleAD&gt;，持续3秒，至多可叠加5次(最多提升：&lt;scaleAD&gt;30%攻击力&lt;/scaleAD&gt;)。&lt;li&gt;&lt;passive&gt;咒刃：&lt;/passive&gt;施放技能后，你的下一次攻击因强化而附带额外的&lt;physicalDamage&gt;(200%基础攻击力)物理伤害&lt;/physicalDamage&gt;&lt;OnHit&gt;攻击特效&lt;/OnHit&gt;(1.5秒冷却时间)。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得 &lt;attention&gt;3&lt;/attention&gt; 攻击力，&lt;attention&gt;3&lt;/attention&gt;技能急速和&lt;attention&gt; 3&lt;/attention&gt;移动速度&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;3333 (733)&lt;/span&gt;" alt="三相之力">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3042.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;魔切&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;35&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;860&lt;/attention&gt;法力&lt;br&gt;&lt;attention&gt;15&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;敬畏：&lt;/passive&gt;提供&lt;scaleAD&gt;相当于2.5%最大法力值的额外攻击力&lt;/scaleAD&gt;。&lt;li&gt;&lt;passive&gt;冲击：&lt;/passive&gt;对英雄发起的攻击会造成额外的&lt;physicalDamage&gt;1.5%最大法力值的物理伤害&lt;/physicalDamage&gt;(&lt;OnHit&gt;攻击特效&lt;/OnHit&gt;)。对英雄发起的伤害型技能会造成额外的&lt;physicalDamage&gt;(近战携带者为3.5% | 远程携带者为2.7%)最大法力值+6%总攻击力的物理伤害&lt;/physicalDamage&gt;.。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;3000 (3000)&lt;/span&gt;" alt="魔切">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3363.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;远见改造&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升施放距离并揭示目标区域&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;显形4000码内的一个区域并放置一个可见且脆弱的守卫。友军无法将这个守卫作为召唤师技能或技能的目标&lt;scaleLevel&gt;(198 - 99秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="远见改造">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/1029.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;布甲&lt;/b&gt;&lt;br&gt;&lt;span&gt;略微提升护甲&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;15&lt;/attention&gt;护甲&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;300 (300)&lt;/span&gt;" alt="布甲">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3158.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;明朗之靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升移动速度和冷却缩减&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;br&gt;&lt;li&gt;提供12召唤师技能急速。&lt;br&gt;&lt;br&gt;&lt;flavorText&gt;“这个物品是为了庆祝在2010年12月10日艾欧尼亚和诺克萨斯的重赛中，艾欧尼亚取得胜利。”&lt;/flavorText&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;950 (650)&lt;/span&gt;" alt="明朗之靴">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/1029.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;布甲&lt;/b&gt;&lt;br&gt;&lt;span&gt;略微提升护甲&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;15&lt;/attention&gt;护甲&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;300 (300)&lt;/span&gt;" alt="布甲">
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-red.png">
												Control Ward <span class='wards vision'>3</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-42 tip" title="刀锋舞者">刀锋舞者</div>
								<div class="Image20 __sprite __spc20 __spc20-42 tip" title="刀锋舞者">刀锋舞者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Aurora+time" class="Link" target='_blank'>Aurora time</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-25 tip" title="时间刺客">时间刺客</div>
								<div class="Image20 __sprite __spc20 __spc20-25 tip" title="时间刺客">时间刺客</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=RabbIe+Arouser" class="Link" target='_blank'>RabbIe Arouser</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-47 tip" title="未来守护者">未来守护者</div>
								<div class="Image20 __sprite __spc20 __spc20-47 tip" title="未来守护者">未来守护者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=MID444444" class="Link" target='_blank'>MID444444</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-28 tip" title="探险家">探险家</div>
								<div class="Image20 __sprite __spc20 __spc20-28 tip" title="探险家">探险家</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-150 tip" title="魔法猫咪">魔法猫咪</div>
								<div class="Image20 __sprite __spc20 __spc20-150 tip" title="魔法猫咪">魔法猫咪</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=BotIsLavaPathTop" class="Link" target='_blank'>BotIsLavaPathTop</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-38 tip" title="灵罗娃娃">灵罗娃娃</div>
								<div class="Image20 __sprite __spc20 __spc20-38 tip" title="灵罗娃娃">灵罗娃娃</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Stargazer7" class="Link" target='_blank'>Stargazer7</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-37 tip" title="法外狂徒">法外狂徒</div>
								<div class="Image20 __sprite __spc20 __spc20-37 tip" title="法外狂徒">法外狂徒</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=korea+bbq" class="Link" target='_blank'>korea bbq</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-102 tip" title="符文法师">符文法师</div>
								<div class="Image20 __sprite __spc20 __spc20-102 tip" title="符文法师">符文法师</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=152cm187kg24cm" class="Link" target='_blank'>152cm187kg24cm</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-75 tip" title="赏金猎人">赏金猎人</div>
								<div class="Image20 __sprite __spc20 __spc20-75 tip" title="赏金猎人">赏金猎人</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Uzi+mode1" class="Link" target='_blank'>Uzi mode1</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
								<div class="Image20 __sprite __spc20 __spc20-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Mike+Waz%CE%BFwski" class="Link" target='_blank'>Mike Wazοwski</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																							<div class="Item">
								<a id="right_match_replay" href="#" class="Button Replay OpenSpectateButton">
									<span class="__spSite __spSite-159"></span></a>
							</div>
																<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-198 Off"></span>
								<span class="__spSite __spSite-197 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Win  "
	     data-summoner-id="135515503"
	     data-game-time="1633542541"
	     data-game-id="5494458477"
	     data-game-result="win"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633542541' data-type='' data-interval='60'>2021-10-07 02:49:01</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											胜利									</div>
									<div class="GameLength">22分 1秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/nami/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Nami.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="唤潮鲛姬"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;引燃&lt;/b&gt;&lt;br&gt;&lt;span&gt;引燃是对单体敌方目标施放的持续性伤害技能，在5秒的持续时间里造成70-410（取决于英雄等级）真实伤害，获得目标的视野，并减少目标所受的治疗和回复效果。&lt;/span&gt;" alt="引燃">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8112.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;电刑&lt;/b&gt;&lt;br&gt;&lt;span&gt;在3秒内用3个&lt;b&gt;独立的&lt;/b&gt;攻击或技能命中一位英雄时，会造成额外的&lt;lol-uikit-tooltipped-keyword key=&#039;LinkTooltip_Description_AdaptiveDmg&#039;&gt;&lt;font color=&#039;#48C4B7&#039;&gt;自适应伤害&lt;/font&gt;&lt;/lol-uikit-tooltipped-keyword&gt;。&lt;br&gt;&lt;br&gt;伤害值：30 - 180 (+0.4额外攻击力, +0.25法术强度)。&lt;br&gt;&lt;br&gt;冷却时间：25 - 20秒&lt;br&gt;&lt;br&gt;&lt;hr&gt;&lt;i&gt;“我们曾称呼他们为“雷霆领主”，是因为他们的闪电招来了灾祸。”&lt;/i&gt;&lt;/span&gt;" alt="电刑">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/nami/statistics" target="_blank">唤潮鲛姬</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">4</span> /
					<span class="Death">3</span> /
					<span class="Assist">21</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">8.33:1</span> KDA				</div>
																								</div>
			<div class="Stats">
				<div class="Level">
					等级12
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 8  + 野怪 0&lt;br&gt;每分钟CS0.4个">8 (0.4)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  64%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Grandmaster</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3853.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;极冰碎片&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;40&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;75&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础法力回复&lt;br&gt;&lt;attention&gt;3&lt;/attention&gt;金币/10秒&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存0个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存4个侦察守卫，并在访问商店时补满。 &lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="极冰碎片">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/4005.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;帝国指令&lt;/b&gt;&lt;br&gt;&lt;span&gt;将伤害延后。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;40&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础法力回复&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;协同开火：&lt;/passive&gt;技能在&lt;status&gt;减速&lt;/status&gt;或&lt;status&gt;定身&lt;/status&gt;一名英雄时会造成&lt;magicDamage&gt;45 - 75(基于等级)额外魔法伤害&lt;/magicDamage&gt;并将其标记4秒(每个敌方英雄有6秒冷却时间)。友方英雄的伤害会引爆标记，造成额外的&lt;magicDamage&gt;90 - 150(基于友军等级)魔法伤害&lt;/magicDamage&gt;并为你和该友军都提供&lt;speed&gt;20%移动速度&lt;/speed&gt;，持续2秒。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;15&lt;/attention&gt;法术强度。&lt;br&gt;&lt;br&gt;&lt;rules&gt;加成效果的强度是基于该友方英雄的等级。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2500 (750)&lt;/span&gt;" alt="帝国指令">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2055.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;控制守卫&lt;/b&gt;&lt;br&gt;&lt;span&gt;用来使范围内的守卫和隐形陷阱失效。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 消耗：&lt;/active&gt;放置一个强大的控制守卫来提供附近区域的视野。这个设备还会使&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;的陷阱显形，使&lt;keywordStealth&gt;伪装&lt;/keywordStealth&gt;的敌人们显形，并使敌方守卫显形和失效。 &lt;br&gt;&lt;br&gt;&lt;rules&gt;你至多可以携带2个控制守卫。控制守卫不会使其它控制守卫失效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;75 (75)&lt;/span&gt;" alt="控制守卫">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3364.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;神谕透镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;持续期间可瘫痪附近隐形的守卫和陷阱&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;扫描你的周围，预警隐藏的敌方单位，并使隐形的陷阱显形，并使附近的敌方侦察守卫显形(并暂时失效)10秒&lt;scaleLevel&gt;(90 - 60秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="神谕透镜">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3158.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;明朗之靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升移动速度和冷却缩减&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;br&gt;&lt;li&gt;提供12召唤师技能急速。&lt;br&gt;&lt;br&gt;&lt;flavorText&gt;“这个物品是为了庆祝在2010年12月10日艾欧尼亚和诺克萨斯的重赛中，艾欧尼亚取得胜利。”&lt;/flavorText&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;950 (650)&lt;/span&gt;" alt="明朗之靴">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3011.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;炼金科技纯化器&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;55&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础法力回复&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;芙顶之毒：&lt;/passive&gt;对英雄们造成魔法伤害时会施加&lt;status&gt;40%重伤&lt;/status&gt;效果，持续3秒。对另一名友方英雄提供治疗或护盾时，会使你和该英雄都获得强化，在下一次伤害敌方英雄时施加&lt;status&gt;60%重伤&lt;/status&gt;效果。&lt;br&gt;&lt;br&gt;&lt;rules&gt;&lt;status&gt;重伤&lt;/status&gt;会降低治疗效果和生命回复的效能。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2300 (550)&lt;/span&gt;" alt="炼金科技纯化器">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3114.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;禁忌雕像&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升治疗和护盾强度、法力回复和冷却缩减&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;50%&lt;/attention&gt;基础法力回复&lt;br&gt;&lt;attention&gt;10%&lt;/attention&gt;治疗和护盾强度&lt;/stats&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;800 (550)&lt;/span&gt;" alt="禁忌雕像">
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildblue-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildblue-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-blue.png">
												Control Ward <span class='wards vision'>10</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-37 tip" title="法外狂徒">法外狂徒</div>
								<div class="Image20 __sprite __spc20 __spc20-37 tip" title="法外狂徒">法外狂徒</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=h%CE%BFt+girl+bummer" class="Link" target='_blank'>hοt girl bummer</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-45 tip" title="德玛西亚皇子">德玛西亚皇子</div>
								<div class="Image20 __sprite __spc20 __spc20-45 tip" title="德玛西亚皇子">德玛西亚皇子</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Keule183" class="Link" target='_blank'>Keule183</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-87 tip" title="发条魔灵">发条魔灵</div>
								<div class="Image20 __sprite __spc20 __spc20-87 tip" title="发条魔灵">发条魔灵</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Boukada" class="Link" target='_blank'>Boukada</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-68 tip" title="圣枪游侠">圣枪游侠</div>
								<div class="Image20 __sprite __spc20 __spc20-68 tip" title="圣枪游侠">圣枪游侠</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=not+a+chat+user" class="Link" target='_blank'>not a chat user</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
								<div class="Image20 __sprite __spc20 __spc20-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-30 tip" title="无双剑姬">无双剑姬</div>
								<div class="Image20 __sprite __spc20 __spc20-30 tip" title="无双剑姬">无双剑姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=TTV+Potent213" class="Link" target='_blank'>TTV Potent213</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-92 tip" title="元素女皇">元素女皇</div>
								<div class="Image20 __sprite __spc20 __spc20-92 tip" title="元素女皇">元素女皇</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=sejun1" class="Link" target='_blank'>sejun1</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-118 tip" title="解脱者">解脱者</div>
								<div class="Image20 __sprite __spc20 __spc20-118 tip" title="解脱者">解脱者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=gaengsin" class="Link" target='_blank'>gaengsin</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-8 tip" title="残月之肃">残月之肃</div>
								<div class="Image20 __sprite __spc20 __spc20-8 tip" title="残月之肃">残月之肃</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=141414ADADAD" class="Link" target='_blank'>141414ADADAD</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-125 tip" title="魂锁典狱长">魂锁典狱长</div>
								<div class="Image20 __sprite __spc20 __spc20-125 tip" title="魂锁典狱长">魂锁典狱长</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=BIazingFire" class="Link" target='_blank'>BIazingFire</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																							<div class="Item">
								<a id="right_match_replay" href="#" class="Button Replay OpenSpectateButton">
									<span class="__spSite __spSite-159"></span></a>
							</div>
																<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-194 Off"></span>
								<span class="__spSite __spSite-193 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Lose  "
	     data-summoner-id="135515503"
	     data-game-time="1633477567"
	     data-game-id="5493375695"
	     data-game-result="lose"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633477567' data-type='' data-interval='60'>2021-10-06 08:46:07</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											失败									</div>
									<div class="GameLength">30分 13秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/braum/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Braum.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="弗雷尔卓德之心"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;引燃&lt;/b&gt;&lt;br&gt;&lt;span&gt;引燃是对单体敌方目标施放的持续性伤害技能，在5秒的持续时间里造成70-410（取决于英雄等级）真实伤害，获得目标的视野，并减少目标所受的治疗和回复效果。&lt;/span&gt;" alt="引燃">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/9923.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;丛刃&lt;/b&gt;&lt;br&gt;&lt;span&gt;在攻击敌方英雄时，提供110%攻击速度给最先的3次攻击。&lt;br&gt;&lt;br&gt;每次攻击的间隔不能超过3秒，否则这个效果就会结束。&lt;br&gt;&lt;br&gt;冷却时间：12秒。&lt;br&gt;&lt;br&gt;&lt;rules&gt;被重置的攻击会使攻击次数上限提升1。&lt;br&gt;&lt;br&gt;允许你暂时溢出你的攻击速度上限。&lt;/rules&gt;&lt;/span&gt;" alt="丛刃">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/braum/statistics" target="_blank">弗雷尔卓德之心</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">1</span> /
					<span class="Death">9</span> /
					<span class="Assist">14</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">1.67:1</span> KDA				</div>
																								</div>
			<div class="Stats">
				<div class="Level">
					等级12
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 32  + 野怪 0&lt;br&gt;每分钟CS1.1个">32 (1.1)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  58%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Grandmaster</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3857.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;白岩肩铠&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;15&lt;/attention&gt;攻击力&lt;br&gt;&lt;attention&gt;250&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础生命回复&lt;br&gt;&lt;attention&gt;3&lt;/attention&gt;金币/10秒&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存0个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt; &lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存4个侦察守卫，并在访问商店时补满。 &lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="白岩肩铠">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3190.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;钢铁烈阳之匣&lt;/b&gt;&lt;br&gt;&lt;span&gt;主动施放来为附近友军提供吸收伤害的护盾&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;护甲&lt;br&gt;&lt;attention&gt;30&lt;/attention&gt;魔法抗性&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;虔诚：&lt;/active&gt;为附近友军提供&lt;shield&gt;230 - 385(基于友军等级)护盾&lt;/shield&gt;，在2.5秒里持续衰减(90秒冷却时间)。&lt;br&gt;&lt;li&gt;&lt;passive&gt;奉献：&lt;/passive&gt;为附近友方英雄提供&lt;scaleArmor&gt;5护甲&lt;/scaleArmor&gt;和&lt;scaleMR&gt;魔法抗性&lt;/scaleMR&gt;。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;2&lt;/attention&gt;护甲/魔法抗性加成至&lt;passive&gt;奉献&lt;/passive&gt;。&lt;br&gt;&lt;br&gt;&lt;rules&gt;加成效果的强度是基于该友方英雄的等级。&lt;br&gt;20秒内的后续&lt;active&gt;奉献&lt;/active&gt;的护盾仅有25%效果。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2500 (200)&lt;/span&gt;" alt="钢铁烈阳之匣">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2055.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;控制守卫&lt;/b&gt;&lt;br&gt;&lt;span&gt;用来使范围内的守卫和隐形陷阱失效。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 消耗：&lt;/active&gt;放置一个强大的控制守卫来提供附近区域的视野。这个设备还会使&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;的陷阱显形，使&lt;keywordStealth&gt;伪装&lt;/keywordStealth&gt;的敌人们显形，并使敌方守卫显形和失效。 &lt;br&gt;&lt;br&gt;&lt;rules&gt;你至多可以携带2个控制守卫。控制守卫不会使其它控制守卫失效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;75 (75)&lt;/span&gt;" alt="控制守卫">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3364.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;神谕透镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;持续期间可瘫痪附近隐形的守卫和陷阱&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;扫描你的周围，预警隐藏的敌方单位，并使隐形的陷阱显形，并使附近的敌方侦察守卫显形(并暂时失效)10秒&lt;scaleLevel&gt;(90 - 60秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="神谕透镜">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/2420.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;秒表&lt;/b&gt;&lt;br&gt;&lt;span&gt;主动施放来变得无敌但无法行动&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - &lt;/active&gt; &lt;active&gt;凝滞：&lt;/active&gt;一次性使用，在2.5秒里&lt;status&gt;免疫伤害&lt;/status&gt;且&lt;status&gt;不可被选取&lt;/status&gt;，但在此期间里无法采取任何其它行动(转变为一个&lt;rarityGeneric&gt;破损的秒表&lt;/rarityGeneric&gt;)。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;650 (650)&lt;/span&gt;" alt="秒表">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3111.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;水银之靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升移动速度并降低限制效果的时长&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;25&lt;/attention&gt;魔法抗性&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;br&gt;&lt;attention&gt;30%&lt;/attention&gt;韧性&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;rules&gt;韧性会减少&lt;status&gt;晕眩&lt;/status&gt;、&lt;status&gt;减速&lt;/status&gt;、&lt;status&gt;嘲讽&lt;/status&gt;、&lt;status&gt;恐惧&lt;/status&gt;、&lt;status&gt;沉默&lt;/status&gt;、&lt;status&gt;致盲&lt;/status&gt;、&lt;status&gt;变形&lt;/status&gt;和&lt;status&gt;定身&lt;/status&gt;效果的持续时间。它对&lt;status&gt;浮空&lt;/status&gt;或&lt;status&gt;压制&lt;/status&gt;效果无效。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (350)&lt;/span&gt;" alt="水银之靴">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3109.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;骑士之誓&lt;/b&gt;&lt;br&gt;&lt;span&gt;与一名友方英雄搭档来保护彼此&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;400&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;10&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;300%&lt;/attention&gt;基础生命回复&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;立誓：&lt;/active&gt;指定一名友方英雄作为你的&lt;attention&gt;誓约者&lt;/attention&gt;(60秒冷却时间)。&lt;br&gt;&lt;li&gt;&lt;passive&gt;牺牲：&lt;/passive&gt;当你的&lt;attention&gt;誓约者&lt;/attention&gt;友军在附近时，将其所受的15%伤害转移到你身上，并且如果其生命值低于50%，你就会在朝着其移动时获得&lt;speed&gt;35%移动速度&lt;/speed&gt;。&lt;br&gt;&lt;br&gt;&lt;rules&gt;同一个英雄同一时间只能被一个【骑士之誓】所连接。如果你的生命值低于30%，伤害转移就会停止。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2300 (700)&lt;/span&gt;" alt="骑士之誓">
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-red.png">
												Control Ward <span class='wards vision'>15</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-38 tip" title="灵罗娃娃">灵罗娃娃</div>
								<div class="Image20 __sprite __spc20 __spc20-38 tip" title="灵罗娃娃">灵罗娃娃</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=dofaminu" class="Link" target='_blank'>dofaminu</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-57 tip" title="影流之镰">影流之镰</div>
								<div class="Image20 __sprite __spc20 __spc20-57 tip" title="影流之镰">影流之镰</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=SRB+Jungler+47" class="Link" target='_blank'>SRB Jungler 47</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-129 tip" title="卡牌大师">卡牌大师</div>
								<div class="Image20 __sprite __spc20 __spc20-129 tip" title="卡牌大师">卡牌大师</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=zo%C3%ADr" class="Link" target='_blank'>zoír</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-8 tip" title="残月之肃">残月之肃</div>
								<div class="Image20 __sprite __spc20 __spc20-8 tip" title="残月之肃">残月之肃</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=FB+Neramin1" class="Link" target='_blank'>FB Neramin1</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-15 tip" title="弗雷尔卓德之心">弗雷尔卓德之心</div>
								<div class="Image20 __sprite __spc20 __spc20-15 tip" title="弗雷尔卓德之心">弗雷尔卓德之心</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-58 tip" title="狂暴之心">狂暴之心</div>
								<div class="Image20 __sprite __spc20 __spc20-58 tip" title="狂暴之心">狂暴之心</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=chance+no+exist" class="Link" target='_blank'>chance no exist</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-92 tip" title="元素女皇">元素女皇</div>
								<div class="Image20 __sprite __spc20 __spc20-92 tip" title="元素女皇">元素女皇</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Raz%C3%B8rk+Activoo" class="Link" target='_blank'>Razørk Activoo</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-37 tip" title="法外狂徒">法外狂徒</div>
								<div class="Image20 __sprite __spc20 __spc20-37 tip" title="法外狂徒">法外狂徒</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Fressko" class="Link" target='_blank'>Fressko</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-28 tip" title="探险家">探险家</div>
								<div class="Image20 __sprite __spc20 __spc20-28 tip" title="探险家">探险家</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Paulaeal" class="Link" target='_blank'>Paulaeal</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-94 tip" title="幻翎">幻翎</div>
								<div class="Image20 __sprite __spc20 __spc20-94 tip" title="幻翎">幻翎</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=ight" class="Link" target='_blank'>ight</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																							<div class="Item">
								<a id="right_match_replay" href="#" class="Button Replay OpenSpectateButton">
									<span class="__spSite __spSite-159"></span></a>
							</div>
																<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-198 Off"></span>
								<span class="__spSite __spSite-197 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>					<div class="GameItemWrap">
	<div class="GameItem Lose  "
	     data-summoner-id="135515503"
	     data-game-time="1633475337"
	     data-game-id="5493333562"
	     data-game-result="lose"
	>
				<div class="Content">
			<div class="GameStats">
				<div class="GameType" title="单人排位">
					单人排位
				</div>
				<div class="TimeStamp"><span class=' _timeago _timeCount' data-datetime='1633475337' data-type='' data-interval='60'>2021-10-06 08:08:57</span></div>
				<div class="Bar"></div>
				<div class="GameResult">
											失败									</div>
									<div class="GameLength">30分 7秒</div>
				
							</div>
			<div class="GameSettingInfo">
				<div class="ChampionImage">
					<a href="/champion/nami/statistics" target="_blank"><img src="//opgg-static.akamaized.net/images/lol/champion/Nami.png?image=c_scale,q_auto,w_46&amp;v=1633482212" class="Image" alt="唤潮鲛姬"></a>
				</div>

				<div class="SummonerSpell">
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerExhaust.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;虚弱&lt;/b&gt;&lt;br&gt;&lt;span&gt;虚弱目标敌方英雄，降低其30%的移动速度，并使其造成的伤害减少40%，持续3秒。&lt;/span&gt;" alt="虚弱">
						</div>
											<div class="Spell">
							<img src="//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;闪现&lt;/b&gt;&lt;br&gt;&lt;span&gt;使英雄朝着你的指针所停的区域瞬间传送一小段距离。&lt;/span&gt;" alt="闪现">
						</div>
									</div>
									<div class="Runes">
																			<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perk/8465.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;守护者&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;i&gt;守护&lt;/i&gt;距离你350码内的友军，以及被你选为技能目标的友军2.5秒。当&lt;i&gt;守护&lt;/i&gt;持续时，如果你或该友军在&lt;i&gt;守护&lt;/i&gt;持续期间承受的伤害超过一定数额，那么你们两个都会获得一层持续1.5秒的护盾。&lt;br&gt;&lt;br&gt;冷却时间：&lt;scaleLevel&gt;70 ~40&lt;/scaleLevel&gt;秒&lt;br&gt;护盾值：&lt;scaleLevel&gt;70~150&lt;/scaleLevel&gt;+你&lt;scaleAP&gt;15%&lt;/scaleAP&gt;法术强度+你&lt;scalehealth&gt;9%&lt;/scalehealth&gt;额外生命值。&lt;br&gt;触发阈值：&lt;scaleLevel&gt;90~250&lt;/scaleLevel&gt;折后伤害。&lt;/span&gt;" alt="守护者">
							</div>
																									<div class="Rune">
								<img src="//opgg-static.akamaized.net/images/lol/perkStyle/8300.png?image=c_scale,q_auto,w_22&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #ffc659&#039;&gt;启迪&lt;/b&gt;&lt;br&gt;&lt;span&gt;创造性的工具并弯曲规则&lt;/span&gt;" alt="启迪">
							</div>
											</div>
								<div class="ChampionName">
					<a href="/champion/nami/statistics" target="_blank">唤潮鲛姬</a>
				</div>
			</div>
			<div class="KDA">
				<div class="KDA">
					<span class="Kill">2</span> /
					<span class="Death">9</span> /
					<span class="Assist">28</span>
				</div>
				<div class="KDARatio">
					<span class="KDARatio ">3.33:1</span> KDA				</div>
																								</div>
			<div class="Stats">
				<div class="Level">
					等级14
				</div>
				<div class="CS">
					<span class="CS tip" title="小兵击杀总数 18  + 野怪 0&lt;br&gt;每分钟CS0.6个">18 (0.6)</span> CS
				</div>
									<div class="CKRate tip" title="击杀贡献率">
						击杀参与率  79%
					</div>
													<div class="MMR">
						<span>Tier Average</span>
						<br />
						<b>Grandmaster</b>
					</div>
							</div>
			<div class="Items">
				<div class="ItemList">
											<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3853.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;极冰碎片&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;40&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;75&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础法力回复&lt;br&gt;&lt;attention&gt;3&lt;/attention&gt;金币/10秒&lt;/stats&gt;&lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存0个侦察守卫，并在访问商店时补满。 &lt;br&gt;&lt;br&gt;&lt;active&gt;主动 - &lt;/active&gt;&lt;active&gt;守卫：&lt;/active&gt;在地上放置一个侦察守卫，对敌方&lt;keywordStealth&gt;隐形&lt;/keywordStealth&gt;但会为你的队伍提供附近区域的视野。至多可储存4个侦察守卫，并在访问商店时补满。 &lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;400 (400)&lt;/span&gt;" alt="极冰碎片">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3011.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;炼金科技纯化器&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;55&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础法力回复&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;芙顶之毒：&lt;/passive&gt;对英雄们造成魔法伤害时会施加&lt;status&gt;40%重伤&lt;/status&gt;效果，持续3秒。对另一名友方英雄提供治疗或护盾时，会使你和该英雄都获得强化，在下一次伤害敌方英雄时施加&lt;status&gt;60%重伤&lt;/status&gt;效果。&lt;br&gt;&lt;br&gt;&lt;rules&gt;&lt;status&gt;重伤&lt;/status&gt;会降低治疗效果和生命回复的效能。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2300 (550)&lt;/span&gt;" alt="炼金科技纯化器">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/4643.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;警觉眼石&lt;/b&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;150&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;15&lt;/attention&gt;技能急速&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;奥术窖藏：&lt;/passive&gt;这件装备至多可储存3个已购买的控制守卫。&lt;li&gt;&lt;passive&gt;注视：&lt;/passive&gt;使你的侦察守卫和控制守卫的放置上限提升1。&lt;li&gt;&lt;passive&gt;以绪塔尔的祝福：&lt;/passive&gt;提供12%提升至额外生命值、额外攻击力、技能急速和法术强度。&lt;br&gt;&lt;br&gt;&lt;rules&gt;由&lt;rarityLegendary&gt;戒备眼石&lt;/rarityLegendary&gt;升级而成。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;1100 (0)&lt;/span&gt;" alt="警觉眼石">
													</div>
																				<div class="Item">
																	<img src="//opgg-static.akamaized.net/images/lol/item/3364.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;神谕透镜&lt;/b&gt;&lt;br&gt;&lt;span&gt;持续期间可瘫痪附近隐形的守卫和陷阱&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;/stats&gt;&lt;active&gt;主动 - 饰品：&lt;/active&gt;扫描你的周围，预警隐藏的敌方单位，并使隐形的陷阱显形，并使附近的敌方侦察守卫显形(并暂时失效)10秒&lt;scaleLevel&gt;(90 - 60秒冷却时间)&lt;/scaleLevel&gt;。&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;" alt="神谕透镜">
															</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/4005.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;帝国指令&lt;/b&gt;&lt;br&gt;&lt;span&gt;将伤害延后。&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;40&lt;/attention&gt;法术强度&lt;br&gt;&lt;attention&gt;200&lt;/attention&gt;生命值&lt;br&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;100%&lt;/attention&gt;基础法力回复&lt;/stats&gt;&lt;br&gt;&lt;li&gt;&lt;passive&gt;协同开火：&lt;/passive&gt;技能在&lt;status&gt;减速&lt;/status&gt;或&lt;status&gt;定身&lt;/status&gt;一名英雄时会造成&lt;magicDamage&gt;45 - 75(基于等级)额外魔法伤害&lt;/magicDamage&gt;并将其标记4秒(每个敌方英雄有6秒冷却时间)。友方英雄的伤害会引爆标记，造成额外的&lt;magicDamage&gt;90 - 150(基于友军等级)魔法伤害&lt;/magicDamage&gt;并为你和该友军都提供&lt;speed&gt;20%移动速度&lt;/speed&gt;，持续2秒。&lt;br&gt;&lt;br&gt;&lt;rarityMythic&gt;神话被动：&lt;/rarityMythic&gt;你每装备一件&lt;rarityLegendary&gt;传说&lt;/rarityLegendary&gt;装备，就会获得&lt;attention&gt;15&lt;/attention&gt;法术强度。&lt;br&gt;&lt;br&gt;&lt;rules&gt;加成效果的强度是基于该友方英雄的等级。&lt;/rules&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;2500 (750)&lt;/span&gt;" alt="帝国指令">
													</div>
																							<div class="Item">
															<img src="//opgg-static.akamaized.net/images/lol/item/3158.png?image=q_auto:best&amp;v=1633482212" class="Image tip" title="&lt;b style=&#039;color: #00cfbc&#039;&gt;明朗之靴&lt;/b&gt;&lt;br&gt;&lt;span&gt;提升移动速度和冷却缩减&lt;/span&gt;&lt;br&gt;&lt;span&gt;&lt;mainText&gt;&lt;stats&gt;&lt;attention&gt;20&lt;/attention&gt;技能急速&lt;br&gt;&lt;attention&gt;45&lt;/attention&gt;移动速度&lt;/stats&gt;&lt;br&gt;&lt;li&gt;提供12召唤师技能急速。&lt;br&gt;&lt;br&gt;&lt;flavorText&gt;“这个物品是为了庆祝在2010年12月10日艾欧尼亚和诺克萨斯的重赛中，艾欧尼亚取得胜利。”&lt;/flavorText&gt;&lt;/mainText&gt;&lt;br&gt;&lt;/span&gt;&lt;br&gt;&lt;span&gt;价格:&lt;/span&gt; &lt;span style=&#039;color: #ffc659&#039;&gt;950 (650)&lt;/span&gt;" alt="明朗之靴">
													</div>
																							<div class="Item">
															<div class="Image NoItem"></div>
													</div>
																											<button class="Button OpenBuildButton tip" title="Build" type="button">
																			<img class="On" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
										<img class="Off" src="//opgg-static.akamaized.net/css3/sprite/images/icon-buildred-p.png">
																	</button>
																						</div>
									<div class="Trinket">
													<img src="//opgg-static.akamaized.net/images/site/summoner/icon-ward-red.png">
												Control Ward <span class='wards vision'>14</span></div>
							</div>
			<div class="FollowPlayers Names">
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-141 tip" title="猩红收割者">猩红收割者</div>
								<div class="Image20 __sprite __spc20 __spc20-141 tip" title="猩红收割者">猩红收割者</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=lennylennylenny" class="Link" target='_blank'>lennylennylenny</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-92 tip" title="元素女皇">元素女皇</div>
								<div class="Image20 __sprite __spc20 __spc20-92 tip" title="元素女皇">元素女皇</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Sticky+Pillar" class="Link" target='_blank'>Sticky Pillar</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-63 tip" title="诡术妖姬">诡术妖姬</div>
								<div class="Image20 __sprite __spc20 __spc20-63 tip" title="诡术妖姬">诡术妖姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Chamana1" class="Link" target='_blank'>Chamana1</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-68 tip" title="圣枪游侠">圣枪游侠</div>
								<div class="Image20 __sprite __spc20 __spc20-68 tip" title="圣枪游侠">圣枪游侠</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=lucker3" class="Link" target='_blank'>lucker3</a>
															</div>
						</div>
											<div class="Summoner Requester">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
								<div class="Image20 __sprite __spc20 __spc20-79 tip" title="唤潮鲛姬">唤潮鲛姬</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=songqingliu+gdlk" class="Link" target='_blank'>songqingliu gdlk</a>
															</div>
						</div>
									</div>
				<div class="Team">
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-58 tip" title="狂暴之心">狂暴之心</div>
								<div class="Image20 __sprite __spc20 __spc20-58 tip" title="狂暴之心">狂暴之心</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=JBL+ABUSER" class="Link" target='_blank'>JBL ABUSER</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-84 tip" title="永恒梦魇">永恒梦魇</div>
								<div class="Image20 __sprite __spc20 __spc20-84 tip" title="永恒梦魇">永恒梦魇</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=asdfghjklqwe" class="Link" target='_blank'>asdfghjklqwe</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-148 tip" title="封魔剑魂">封魔剑魂</div>
								<div class="Image20 __sprite __spc20 __spc20-148 tip" title="封魔剑魂">封魔剑魂</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=%CE%A4reasure+Hunter" class="Link" target='_blank'>Τreasure Hunter</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-105 tip" title="涤魂圣枪">涤魂圣枪</div>
								<div class="Image20 __sprite __spc20 __spc20-105 tip" title="涤魂圣枪">涤魂圣枪</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=Namex" class="Link" target='_blank'>Namex</a>
															</div>
						</div>
											<div class="Summoner ">
							<div class="ChampionImage">
								<div class="Image16 __sprite __spc16 __spc16-5 tip" title="殇之木乃伊">殇之木乃伊</div>
								<div class="Image20 __sprite __spc20 __spc20-5 tip" title="殇之木乃伊">殇之木乃伊</div>
							</div>
							<div class="SummonerName">
																	<a href="//euw.op.gg/summoner/userName=O3I" class="Link" target='_blank'>O3I</a>
															</div>
						</div>
									</div>
			</div>
			<div class="StatsButton">
				<div class="Content">
																							<div class="Item">
								<a id="right_match_replay" href="#" class="Button Replay OpenSpectateButton">
									<span class="__spSite __spSite-159"></span></a>
							</div>
																<div class="Item">
						<a id="right_match" href="#" class="Button MatchDetail">
															<span class="__spSite __spSite-198 Off"></span>
								<span class="__spSite __spSite-197 On"></span>
													</a>
					</div>
				</div>
			</div>
		</div>
		<div class="GameDetail"></div>
	</div>
</div>			</div>
			<div class="GameMoreButton Box">
			<a href="#" onclick="$.OP.GG.matches.list.loadMore($(this)); return false;" class="Button">更多</a>
		</div>
		<script>
		$(function(){
			var activeTabClassName = $(".SummonerLayout .MenuList .active").data("tab-show-class");
			var $gameListContainer = $(".SummonerLayoutContent." + activeTabClassName).find(".GameListContainer");
			$.OP.GG.matches.list.updateSummaryByJson({"wins":7,"losses":13,"kills":65,"deaths":115,"assists":270,"contributionsSum":11.32,"contributionsCount":20,"champions":{"Nami":{"name":"\u5524\u6f6e\u9c9b\u59ec","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Nami.png?image=c_scale,q_auto,w_30&v=1633482212","games":4,"kills":9,"deaths":18,"assists":83,"wins":2,"losses":2},"Rell":{"name":"\u9555\u94c1\u5c11\u5973","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Rell.png?image=c_scale,q_auto,w_30&v=1633482212","games":3,"kills":3,"deaths":13,"assists":26,"wins":1,"losses":2},"Lucian":{"name":"\u5723\u67aa\u6e38\u4fa0","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Lucian.png?image=c_scale,q_auto,w_30&v=1633482212","games":2,"kills":8,"deaths":15,"assists":14,"wins":0,"losses":2},"Nautilus":{"name":"\u6df1\u6d77\u6cf0\u5766","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Nautilus.png?image=c_scale,q_auto,w_30&v=1633482212","games":2,"kills":6,"deaths":7,"assists":42,"wins":1,"losses":1},"Kaisa":{"name":"\u865a\u7a7a\u4e4b\u5973","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Kaisa.png?image=c_scale,q_auto,w_30&v=1633482212","games":2,"kills":11,"deaths":10,"assists":20,"wins":1,"losses":1},"Leona":{"name":"\u66d9\u5149\u5973\u795e","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Leona.png?image=c_scale,q_auto,w_30&v=1633482212","games":2,"kills":5,"deaths":17,"assists":26,"wins":0,"losses":2},"Ezreal":{"name":"\u63a2\u9669\u5bb6","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Ezreal.png?image=c_scale,q_auto,w_30&v=1633482212","games":1,"kills":4,"deaths":7,"assists":5,"wins":0,"losses":1},"Braum":{"name":"\u5f17\u96f7\u5c14\u5353\u5fb7\u4e4b\u5fc3","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Braum.png?image=c_scale,q_auto,w_30&v=1633482212","games":1,"kills":1,"deaths":9,"assists":14,"wins":0,"losses":1},"Rakan":{"name":"\u5e7b\u7fce","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Rakan.png?image=c_scale,q_auto,w_30&v=1633482212","games":1,"kills":4,"deaths":11,"assists":24,"wins":1,"losses":0},"Sylas":{"name":"\u89e3\u8131\u8005","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Sylas.png?image=c_scale,q_auto,w_30&v=1633482212","games":1,"kills":10,"deaths":5,"assists":11,"wins":1,"losses":0},"Sett":{"name":"\u8155\u8c6a","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Sett.png?image=c_scale,q_auto,w_30&v=1633482212","games":1,"kills":4,"deaths":3,"assists":5,"wins":0,"losses":1}},"championsList":[{"name":"\u5524\u6f6e\u9c9b\u59ec","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Nami.png?image=c_scale,q_auto,w_30&v=1633482212","games":4,"kills":9,"deaths":18,"assists":83,"wins":2,"losses":2},{"name":"\u9555\u94c1\u5c11\u5973","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Rell.png?image=c_scale,q_auto,w_30&v=1633482212","games":3,"kills":3,"deaths":13,"assists":26,"wins":1,"losses":2},{"name":"\u5723\u67aa\u6e38\u4fa0","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Lucian.png?image=c_scale,q_auto,w_30&v=1633482212","games":2,"kills":8,"deaths":15,"assists":14,"wins":0,"losses":2},{"name":"\u6df1\u6d77\u6cf0\u5766","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Nautilus.png?image=c_scale,q_auto,w_30&v=1633482212","games":2,"kills":6,"deaths":7,"assists":42,"wins":1,"losses":1},{"name":"\u865a\u7a7a\u4e4b\u5973","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Kaisa.png?image=c_scale,q_auto,w_30&v=1633482212","games":2,"kills":11,"deaths":10,"assists":20,"wins":1,"losses":1},{"name":"\u66d9\u5149\u5973\u795e","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Leona.png?image=c_scale,q_auto,w_30&v=1633482212","games":2,"kills":5,"deaths":17,"assists":26,"wins":0,"losses":2},{"name":"\u63a2\u9669\u5bb6","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Ezreal.png?image=c_scale,q_auto,w_30&v=1633482212","games":1,"kills":4,"deaths":7,"assists":5,"wins":0,"losses":1},{"name":"\u5f17\u96f7\u5c14\u5353\u5fb7\u4e4b\u5fc3","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Braum.png?image=c_scale,q_auto,w_30&v=1633482212","games":1,"kills":1,"deaths":9,"assists":14,"wins":0,"losses":1},{"name":"\u5e7b\u7fce","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Rakan.png?image=c_scale,q_auto,w_30&v=1633482212","games":1,"kills":4,"deaths":11,"assists":24,"wins":1,"losses":0},{"name":"\u89e3\u8131\u8005","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Sylas.png?image=c_scale,q_auto,w_30&v=1633482212","games":1,"kills":10,"deaths":5,"assists":11,"wins":1,"losses":0},{"name":"\u8155\u8c6a","imageUrl":"\/\/opgg-static.akamaized.net\/images\/lol\/champion\/Sett.png?image=c_scale,q_auto,w_30&v=1633482212","games":1,"kills":4,"deaths":3,"assists":5,"wins":0,"losses":1}],"filteredGameCount":19,"positions":[{"games":14,"wins":5,"position":"SUPPORT","positionName":"\u8f85\u52a9","iconClass":"__spSite __spSite-145","iconClass2X":"__spSite __spSite-146","losees":9,"losses":9},{"games":5,"wins":1,"position":"ADC","positionName":"\u4e0b\u8def","iconClass":"__spSite __spSite-139","iconClass2X":"__spSite __spSite-140","losees":4,"losses":4}]}, $gameListContainer, 0);
		});
	</script>
''')
game_list = soup.find('div', {'class': 'GameItemList'})
time.sleep(0.5)

# writer.writerow((name, points, views, danmakus, rating_score, rating_num, follows, share, reply, tags))
# print(name + " success!")
# fp.close()

