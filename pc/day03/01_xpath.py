from lxml import etree
from urllib import request
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html='''
<div class="main-nav" data-sudaclick="blk_mainnav">
<div class="nav-mod-1">
                <ul>
                    <li><a href="http://news.sina.com.cn/" target="_blank"><b>新闻</b></a></li>
					<li><a href="http://mil.news.sina.com.cn/" target="_blank">军事</a></li>
                    <li><a href="https://news.sina.com.cn/china/" target="_blank">国内</a></li>
                    <li><a href="http://news.sina.com.cn/world/" target="_blank">国际</a></li>
                </ul>
                <ul>
                    <li><a href="http://finance.sina.com.cn/" target="_blank"><b>财经</b></a></li>
                    <li><a href="http://finance.sina.com.cn/stock/" target="_blank">股票</a></li>
                    <li><a href="http://finance.sina.com.cn/fund/" target="_blank">基金</a></li>
                    <li><a href="http://finance.sina.com.cn/forex/" target="_blank">外汇</a></li>
                </ul>
                <ul>
                    <li><a href="http://tech.sina.com.cn/" target="_blank"><b>科技</b></a></li>
                    <li><a href="http://mobile.sina.com.cn/" target="_blank">手机</a></li>
                    <li><a href="http://tech.sina.com.cn/discovery/" target="_blank">探索</a></li>
                    <li><a href="http://zhongce.sina.com.cn/" target="_blank">众测</a></li>
                </ul>
            </div>
            <div class="nav-mod-1 nav-w">
                <ul>
					<li><a href="http://sports.sina.com.cn/" target="_blank"><b>体育</b></a></li>
					<li style="width:36px;"><a href="http://sports.sina.com.cn/nba/" target="_blank">NBA</a></li>
					<li><a href="http://sports.sina.com.cn/g/premierleague/" target="_blank">英超</a></li>
                    <li><a href="http://sports.sina.com.cn/csl/" target="_blank">中超</a></li>

                    
                </ul>
                <ul>
                    <li><a href="http://ent.sina.com.cn/" target="_blank"><b>娱乐</b></a></li>
                    <li style="width:36px;"><a href="http://ent.sina.com.cn/star/" target="_blank">明星</a></li>
                    <li><a href="http://ent.sina.com.cn/film/" target="_blank">电影</a></li>
                    <li><a href="http://astro.sina.com.cn/" target="_blank">星座</a></li>
                </ul>
                <ul>
                    <li><a href="http://auto.sina.com.cn/" target="_blank"><b>汽车</b></a></li>
                    <li style="width:36px;"><a href="http://dealer.auto.sina.com.cn/price/" target="_blank">报价</a></li>
                    <li><a href="http://db.auto.sina.com.cn/" target="_blank">买车</a></li>
                    <li><a href="http://auto.sina.com.cn/newcar/index.d.html" target="_blank">新车</a></li>
                </ul>
            </div>
            <div class="nav-mod-1 nav-w">
                <ul>
                    <li><a href="http://blog.sina.com.cn/" target="_blank"><b>博客</b></a></li>
                    <li style="width:36px;"><a href="http://zhuanlan.sina.com.cn/" target="_blank">专栏</a></li>
                    <li><a href="http://blog.sina.com.cn/lm/history" target="_blank">历史</a></li>
                    <li><a href="http://weather.sina.com.cn/" target="_blank">天气</a></li>
                </ul>
                <ul>
                    <li><a href="http://video.sina.com.cn/" target="_blank"><b>视频</b></a></li>
                    <li style="width:36px;"><a href="http://ent.sina.com.cn/zongyi/" target="_blank">综艺</a></li>
                    <li><a href="http://vr.sina.com.cn/" target="_blank">VR</a></li>
                    <li><a href="http://video.sina.com.cn/l/pub" target="_blank">直播</a></li>
                </ul>
                <ul>
					<li><a href="http://www.leju.com/#source=pc_sina_tydh1&amp;source_ext=pc_sina" target="_blank"><b>房产</b></a></li>
                    <li style="width:36px;"><a href="http://esf.leju.com/?bi=tg&amp;type=sina-pc&amp;pos=index-dh" target="_blank">二手房</a></li>
                    <li><a href="http://jiaju.sina.com.cn/" target="_blank">家居</a></li>
                    <li><a href="http://collection.sina.com.cn/" target="_blank">收藏</a></li>
                </ul>
            </div>
            <div class="nav-mod-1">
                <ul>
                    <li><a href="http://fashion.sina.com.cn/" target="_blank"><b>时尚</b></a></li>
                    <li><a href="http://eladies.sina.com.cn/" target="_blank">女性</a></li>
                    <li><a href="http://med.sina.com/" target="_blank">医药</a></li>
                    <li><a href="http://baby.sina.com.cn/" target="_blank">育儿</a></li>
                </ul>
                <ul>
                    <li><a href="http://edu.sina.com.cn/" target="_blank"><b>教育</b></a></li>
					<li><a href="http://edu.sina.com.cn/gaokao" target="_blank" style="color:red">高考</a></li>
                    <li><a href="http://gongyi.sina.com.cn/" target="_blank">公益</a></li>
                    <li><a href="http://fo.sina.com.cn/" target="_blank">佛学</a></li>
                </ul>
                <ul>
                    <li><a href="http://photo.sina.com.cn/" target="_blank"><b>图片</b></a></li>
                    <li><a href="http://book.sina.com.cn/" target="_blank">读书</a></li>
                    <li><a href="http://tousu.sina.com.cn/" target="_blank">黑猫</a></li>
                    <li><a href="http://sifa.sina.com.cn/" target="_blank">司法</a></li>
                </ul>
            </div>
            <div class="nav-mod-1 nav-mod-s">
                <ul>
                    <li><a href="https://weibo.com/" target="_blank"><b>微博</b></a></li>
                    <li><a href="http://city.sina.com.cn/" target="_blank">城市</a></li>
                    <li id="SI_Nav_City"><a target="_blank" href="http://zj.sina.com.cn">浙江</a></li>
                    <li><a href="http://tzxy.sina.com.cn" target="_blank">学投资</a></li>
                </ul>
                <ul>
                    <li><a href="http://travel.sina.com.cn/" target="_blank"><b>旅游</b></a></li>
                    <li><a href="http://cul.news.sina.com.cn/" target="_blank">文化</a></li>
                    <li><a href="http://lottery.sina.com.cn/" target="_blank">彩票</a></li>
                    <li><a href="http://golf.sina.com.cn/" target="_blank">高尔夫</a></li>
                </ul>
                <ul>
                    <li><a href="http://games.sina.com.cn/" target="_blank"><b>游戏</b></a></li>
                    <li><a href="http://www.97973.com" target="_blank">手游</a></li>
                    <li><a href="http://mail.sina.com.cn/" target="_blank">邮箱</a></li>
                    <li><a href="http://english.sina.com/" target="_blank">English</a></li>
                </ul>
            </div>
            <div class="nav-mod-1 nav-w nav-hasmore">
                <ul class="nav-out">
                    <li><a href="http://jiaoyi.sina.com.cn/jy/from=langshou" target="_blank">交易</a></li>
                    <li><a href="http://jr.sina.com.cn/web/main/index?source=sinatop" target="_blank">理财</a></li>
                    <li class="more">
                        <a href="javascript:;">更多<i></i></a>
                        <ul class="more-list">
							<li><a href="http://gov.sina.com.cn/" target="_blank">政务</a></li>
                            <li><a href="http://chexian.sina.com/" target="_blank">车险</a></li>
                            <li><a href="http://game.weibo.com/" target="_blank">页游</a></li>
                           <li><a id="navLinkShow" href="http://show.sina.com.cn/" target="_blank">SHOW</a></li>
                            <li><a href="http://search.sina.com.cn/?c=more" target="_blank">搜索</a></li>
                            <li><a href="http://help.sina.com.cn/" target="_blank">客服</a></li>
                            <li><a href="http://news.sina.com.cn/guide/" target="_blank">导航</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        
        </div>
'''


#创建解析对象
parse_html=etree.HTML(html)
# r_list=parse_html.xpath('//a/@href') #//a匹配全部/@href提取全部href的值
r_list=parse_html.xpath('//a/text()') #//a匹配全部/text()提取a节点中的文本
# print(r_list)

# r_list=parse_html.xpath('//div[@class="nav-mod-1"]/ul/li/a/@href')
r_lists=parse_html.xpath('//div[@class="nav-mod-1"]/ul/li/a/text()')
for r in r_lists:
    print(r)
