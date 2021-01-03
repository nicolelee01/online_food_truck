def create_dict(file_content):
    sections = {}
    lines = file_content.splitlines()
    truck_name = lines[0]
    curr = None
    for line in lines[1:]:
        if line[0] == '.':
            curr = line[1:]
            sections[curr] = []
        else:
            # split into tuple (entree name, price, image link)
            i = 0
            name = ""
            price = 0
            img = None
            split = line.split()
            for word in split:
                if '.png' in word or '.jpeg' in word or '.jpg' in word:
                    img = word
                elif word[0].isalpha():
                    name += word + ' '
                else:
                    price = '{:.2f}'.format(float(word))
            sections[curr].append((name[:len(name)-1], price, img))
    return sections, truck_name

def add(cart, item, count, price):
    changed = False
    for i in range(len(cart)):
        if cart[i][0] == item:
            changed = True
            newCount = int(cart[i][1]) + int(count)
            cart[i] = (item, newCount, price)
    if not changed:
        cart.append((item, count, price))
    return cart

def calculate_total(cart):
    total = 0.0
    for item in cart:
        total += int(item[1]) * float(item[2])
    return '{:.2f}'.format(total)