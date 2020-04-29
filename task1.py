def ask_to(prompt, retries=3):
    while True:
        ok = input(prompt)
        if ok in ['yes', 'y', 'Yes', 'Y']:
            return True
        elif ok in ['n', 'no', 'N', 'nope']:
            return False
        retries -= 1
        if retries < 1:
            return None

print(ask_to('ok?', retries=2))

