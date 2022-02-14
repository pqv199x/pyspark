def parsing_txraw(dict):
    import json
    parser= json.loads(dict.read())
    trans_status = 1
    if (parser.get('meta', {}) and parser.get('meta', {}).get('err') or not parser.get('meta',{})):
            trans_status = 0
    # parsing slot
    try:
        list_slot = [k.get('parsed', {}).get('info', {}).get('vote', {}).get('slots', []) for k in
            parser.get('transaction', {}).get('message', {}).get('instructions', [])]
        # list_slot = [k.get('pubkey', '') for k in
        #     parser.get('transaction', {}).get('message', {}).get('accountKeys', [])]
        print(list_slot)
    except:
        list_slot = []
    slot = []
    for ins in list_slot:
        slot = slot + ins
    slot = list(set(slot))
    print(slot)
f = open("text.json", "r")
parsing_txraw(f)