from books import db

def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    if not pattern:
        return not seq
    
    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
    elif not seq:
        return False

    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])

    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])

    elif isinstance(pattern[0],list) and isinstance(seq[0],list):
        return match(seq[0],pattern[0]) and match(seq[1:],pattern[1:])

    else:
        return False


def search(pattern, db):
    matching_books = []

    for book in db:
        if match(book,pattern):
            matching_books.append(book)

    return matching_books

def test_func():
    """specific funciton for testing"""
    # print(search(['--',['f�rfattare', ['&', 'zelle']],'--'],db))

    assert (search([['f�rfattare', ['john', 'zelle']],
                    ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']],
                    ['�r', 2010]],db)
                 == [[['f�rfattare', ['john', 'zelle']],
                    ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']],
                    ['�r', 2010]]])
    assert (search(['--',['titel',['&','&','&']],['�r',1993]],db) ==   # "--" som kategori och & som namn
                    [[['f�rfattare', ['anders', 'haraldsson']],
                    ['titel', ['programmering', 'i', 'lisp']],
                    ['�r', 1993]]])
    assert (search(['--',['�r',2010],'--'],db) == 
                    [[['f�rfattare', ['john', 'zelle']],
                    ['titel', ['python', 'programming', 'an', 'introduction', 'to','computer', 'science']],
                    ['�r', 2010]]])
    assert (search(['--',['f�rfattare', ['&', 'zelle']],'--'],db) == 
                    [[['f�rfattare', ['john', 'zelle']],
                    ['titel', ['python', 'programming', 'an', 'introduction', 'to','computer', 'science']],
                    ['�r', 2010]],
                    [['f�rfattare', ['john', 'zelle']],
                    ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']],
                    ['�r', 2009]]])
    assert (search(['--',['titel',['&','&','&']],['�r','--']],db) == 
                    [[['f�rfattare', ['anders', 'haraldsson']],
                    ['titel', ['programmering', 'i', 'lisp']],
                    ['�r', 1993]]])
    assert (search(['--'],db) ==                                            # endast '--'
                    [[['f�rfattare', ['john', 'zelle']],
                    ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']],
                    ['�r', 2010]],
                    [['f�rfattare', ['armen', 'asratian']],
                    ['titel', ['diskret', 'matematik']],
                    ['�r', 2012]],
                    [['f�rfattare', ['j', 'glenn', 'brookshear']],
                    ['titel', ['computer', 'science', 'an', 'overview']],
                    ['�r', 2011]],
                    [['f�rfattare', ['john', 'zelle']],
                    ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']],
                    ['�r', 2009]],
                    [['f�rfattare', ['anders', 'haraldsson']],
                    ['titel', ['programmering', 'i', 'lisp']],
                    ['�r', 1993]]])
    assert (search([],db) == [])                                             # tom lista
    assert (search((['f�rfattare',['j', 'glenn', 'brookshear']],'--'),db) == # tuple
                    [[['f�rfattare', ['j', 'glenn', 'brookshear']],
                    ['titel', ['computer', 'science', 'an', 'overview']],
                    ['�r', 2011]]])
    assert (search(['&',['titel',['&','&']],'&'],db) ==               # & som categori
                    [[['f�rfattare', ['armen', 'asratian']],
                    ['titel', ['diskret', 'matematik']],
                    ['�r', 2012]]])
    assert (search(['&','&',['�r', 2012]],db) ==                      # & som categori
                    [[['f�rfattare', ['armen', 'asratian']],
                    ['titel', ['diskret', 'matematik']],
                    ['�r', 2012]]])
    assert (search([['f�rfattare', ['adam', 'wille']],                  # hittepå bok
                    ['titel', ['programmering', 'och', 'misförstånd']], 
                    ['�r', 2024]],db) == [])                   


if __name__ == '__main__':
    test_func()
