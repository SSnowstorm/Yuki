# 关于bilibili的功能都在这里
# 功能列表：
# 1、根据user_id查询最近一条动态
from bilibili_api import user, dynamic, sync, Credential

uid = [6027188]
usr_ins = user.User(uid[0])
# credential_dict = {
#     "bili_jct": "d463ee24cad94b1408e028185cc7e0ca",
#     "buvid3": "53D31444-E4A2-4928-88AF-115327D5803F155836infoc",
#     "sessdata": "68bc4f0e%2C1642912464%2Ccdbf6%2A71",
# }
credential = Credential(bili_jct="d463ee24cad94b1408e028185cc7e0ca",
                        buvid3="53D31444-E4A2-4928-88AF-115327D5803F155836infoc",
                        sessdata="68bc4f0e%2C1642912464%2Ccdbf6%2A71")


async def get_dynamic_from_user():
    page = await usr_ins.get_dynamics(0)
    # 给某条动态点赞(需要输入credential)
    dyna_id = page["cards"][0]["desc"]['dynamic_id']
    print(dyna_id)
    # d = dynamic.Dynamic(dynamic_id=dyna_id, credential=credential)
    # d_info = await d.get_info()
    # await d.set_like(True)
    # print(d_info)
    print(page["cards"][0]["card"])
    print(page["cards"][0]["card"]["item"]["content"])  # 第一条动态的正文
    if page["cards"][0]["card"]["item"]["orig_dy_id"]:
        d = dynamic.Dynamic(dynamic_id=page["cards"][0]["card"]["item"]["orig_dy_id"], credential=credential)
        orig_d_info = await d.get_info()
        print("origin_dynamic_with_video:"+str(orig_d_info["card"]))
        # print("origin_dynamic_info:"+str(orig_d_info))
        pass
    # print(page["cards"][0]["card"]["item"])
    # print(page["cards"][1]["card"]["item"]["content"])


if __name__ == "__main__":
    url = "https://space.bilibili.com/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.100 Safari/537.36 '
    }
    function = {
        "homepage": "",
        "dynamic": "/dynamic",
        "submission": {
            "video": "/video",
            "audio": "/audio",
            "article": "/article",
            "album": "/album"
        },
        "video_list": "/channel/series"
    }
    sync(get_dynamic_from_user())
    # r = requests.get(url=url + uid[0] + function["dynamic"], headers=headers)
    # # print(r.text)
    # html = etree.HTML(r.text)
    # print(html)
    # dynamic = html.xpath("//*[@id=\"page-dynamic\"]/div[1]/div/div/div[1]")
    # print(dynamic)
# 动态层级div //*[@id="page-dynamic"]/div[1]/div/div/
# 动态 第一条 //*[@id="page-dynamic"]/div[1]/div/div/div[1]
# 动态 第二条 //*[@id="page-dynamic"]/div[1]/div/div/div[2]
