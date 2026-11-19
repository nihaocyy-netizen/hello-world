# -*- coding: utf-8 -*-
# NX 2506 插件：把对象改成“黄色”（颜色号 6）
# 未选中任何对象时，先让用户原生选择；仍为空则确认后对当前零件的全部实体执行。
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import Htet_common as c
import Htet_lang as _L

TARGET_COLOR = 6


def main():
    session, ui, part, lw = c.ctx(open_listing=False)
    if not c.require_part(lw, part):
        return
    targets = c.resolve_targets(ui, part, lw, solid_only=False)
    if targets is None:
        return
    if not targets:
        c.notice(lw, _L.T("msg.no_bodies_color"))
        return

    if not c.apply_with_undo(session, ui, lw, _L.T("undo.color_yellow"),
                             lambda: c.apply_color(session, targets, TARGET_COLOR),
                             "msg.color_failed"):
        return



if __name__ == '__main__':
    main()
