def reaching_definitions(cfg):
    In = {s: set() for s in cfg}
    Out = {s: set() for s in cfg}

    changed = True
    while changed:
        changed = False
        for s in cfg:
            novo_in = set()
            for p in cfg[s]['pred']:
                novo_in |= Out[p]

            novo_out = cfg[s]['gen'] | (novo_in - cfg[s]['kill'])

            In[s] = novo_in
            if novo_out != Out[s]:
                Out[s] = novo_out
                changed = True

    return In, Out
