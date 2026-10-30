def very_busy_expressions(cfg, universal_expressions):
    In = {s: set(universal_expressions) for s in cfg}
    Out = {s: set() for s in cfg}

    changed = True
    while changed:
        changed = False
        for s in cfg:
            succs = cfg[s]['succ']
            if len(succs) == 0:
                novo_out = set()
            else:
                novo_out = set(In[succs[0]])
                for p in succs[1:]:
                    novo_out &= In[p]

            novo_in = cfg[s]['gen'] | (novo_out - cfg[s]['kill'])

            Out[s] = novo_out
            if novo_in != In[s]:
                In[s] = novo_in
                changed = True

    return In, Out
