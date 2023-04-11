BOOK_PATH = r'C:\Users\Admin\.vscode\projects\Bookbot\book\book.txt'
PAGE_SIZE = 1050

book: dict[int: str] = {}

def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    n=page_size
    counter=0
    if page_size+start<len(text):
        while text[page_size+start] in ',.!:;?…':
            if page_size+start+1>=len(text):
                page_size+=1
                break
            page_size+=1
            counter+=1
    text=text[start:page_size+start]
    if ('...' in text or '?..' in text or '!..' in text) and len(text)>n:
        text=text[:-3]
    elif (',' in text or '.' in text or '!' in text or ':' in text or ';' in text or '?' in text) and len(text)>n:
        text=text[:-1]
    largest=0
    for c in ',.!:;?…':
        if text.rfind(c)>largest:
            largest=text.rfind(c)
    if largest==0:
        return '',0
    text= text[:largest+1]
    return text, len(text)

def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as file:
        content=file.read()
        counter=1
        start=0
        while content.strip():
            m,n =_get_part_text(content, start, PAGE_SIZE)
            book[counter], start = m.lstrip(), n
            content=content[start:]
            start=0
            counter+=1

prepare_book(BOOK_PATH)
