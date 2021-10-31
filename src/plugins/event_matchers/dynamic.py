from bilibili_api import sync
from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State

from src.plugins.bilibili.bili import get_dynamic_from_user

dyn_monitoring = on_command("视奸", rule=to_me(), priority=5)


@dyn_monitoring.handle()
async def parse_dyn_m(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    # uid匹配数据库，没查到直接返回
    print(args)
    state["UID"] = args


@dyn_monitoring.got("UID", prompt="要视奸谁呢？")
async def handle(bot: Bot, event: Event, state: T_State):
    msg = sync(get_dynamic_from_user(state["UID"]))
    await dyn_monitoring.finish(msg)
