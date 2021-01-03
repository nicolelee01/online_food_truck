def create_dict(file_content):
    sections = {}
    lines = file_content.splitlines()
    curr = None
    for line in lines:
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
    return sections