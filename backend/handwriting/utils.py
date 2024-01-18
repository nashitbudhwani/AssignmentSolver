from PIL import Image

def writee(BG, char, gap, _):
    if char == '\n':
        pass
    else:
        char = char.lower()
        cases = Image.open("static/myfont/%s.png" % char)
        BG.paste(cases, (gap, _))
        size = cases.width
        gap += size
        del cases
    return gap, _

def letterwrite(BG, allowed_chars, gap, _, word):
    if gap > BG.width - 95 * (len(word)):
        gap = 0
        _ += 200
    for letter in word:
        if letter in allowed_chars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter = letter.lower()
                letter += 'upper'
            elif letter == '.':
                letter = "fullstop"
            elif letter == '!':
                letter = 'exclamation'
            elif letter == '?':
                letter = 'question'
            elif letter == ',':
                letter = 'comma'
            elif letter == '(':
                letter = 'braketop'
            elif letter == ')':
                letter = 'braketcl'
            elif letter == '-':
                letter = 'hyphen'
            gap, _ = writee(BG, letter, gap, _)
    return gap, _

def worddd(BG, allowed_chars, gap, _, input_text):
    wordlist = input_text.split(' ')
    for i in wordlist:
        gap, _ = letterwrite(BG, allowed_chars, gap, _, i)
        gap, _ = writee(BG, 'space', gap, _)
    return gap, _

def pdf_creation(png_file, flag=False):
    rgba = Image.open(png_file)
    rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
    rgb.paste(rgba, mask=rgba.split()[3])  # paste using alpha channel as mask
    rgb.save('final_output.pdf', append=flag)  # Now save multiple images in the same pdf file

def convert_handwriting(text):
    gap, _ = 0, 0
    p = []
    BG = Image.open("static/myfont/bg.png")  # Create a new instance for each request
    try:
        text = text.replace('\n', '')
        l = len(text)
        nn = len(text) // 600
        chunks, chunk_size = len(text), len(text) // (nn + 1)
        p = [text[i:i + chunk_size] for i in range(0, chunks, chunk_size)]

        for i in range(0, len(p)):
            gap, _ = worddd(BG, 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890', gap, _, p[i])
            gap, _ = writee(BG, '\n', gap, _)
            BG.save('%doutt.png' % i)
            BG1 = Image.open("static/myfont/bg.png")
            BG = BG1
            gap = 0
            _ = 0
    except ValueError as e:
        print("{}\nTry again".format(e))

    imagelist = ['%doutt.png' % i for i in range(len(p))]

    # Converting images to pdf
    # Source: https://datatofish.com/images-to-pdf-python/

    # First create a pdf file if not created
    pdf_creation(imagelist.pop(0))

    # Now I am opening each image and converting them to pdf
    # Appending them to pdfs
    for png_file in imagelist:
        pdf_creation(png_file, flag=True)
