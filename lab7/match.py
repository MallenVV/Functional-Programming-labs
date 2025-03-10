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
    # print(search(['--',['författare', ['&', 'zelle']],'--'],db))

    assert (search([['författare', ['john', 'zelle']],
                    ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']],
                    ['År', 2010]],db)
                 == [[['författare', ['john', 'zelle']],
                    ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']],
                    ['År', 2010]]])
    assert (search(['--',['titel',['&','&','&']],['År',1993]],db) ==   # "--" som kategori och & som namn
                    [[['författare', ['anders', 'haraldsson']],
                    ['titel', ['programmering', 'i', 'lisp']],
                    ['År', 1993]]])
    assert (search(['--',['År',2010],'--'],db) == 
                    [[['författare', ['john', 'zelle']],
                    ['titel', ['python', 'programming', 'an', 'introduction', 'to','computer', 'science']],
                    ['År', 2010]]])
    assert (search(['--',['författare', ['&', 'zelle']],'--'],db) == 
                    [[['författare', ['john', 'zelle']],
                    ['titel', ['python', 'programming', 'an', 'introduction', 'to','computer', 'science']],
                    ['År', 2010]],
                    [['författare', ['john', 'zelle']],
                    ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']],
                    ['År', 2009]]])
    assert (search(['--',['titel',['&','&','&']],['År','--']],db) == 
                    [[['författare', ['anders', 'haraldsson']],
                    ['titel', ['programmering', 'i', 'lisp']],
                    ['År', 1993]]])
    assert (search(['--'],db) ==                                            # endast '--'
                    [[['författare', ['john', 'zelle']],
                    ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']],
                    ['År', 2010]],
                    [['författare', ['armen', 'asratian']],
                    ['titel', ['diskret', 'matematik']],
                    ['År', 2012]],
                    [['författare', ['j', 'glenn', 'brookshear']],
                    ['titel', ['computer', 'science', 'an', 'overview']],
                    ['År', 2011]],
                    [['författare', ['john', 'zelle']],
                    ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']],
                    ['År', 2009]],
                    [['författare', ['anders', 'haraldsson']],
                    ['titel', ['programmering', 'i', 'lisp']],
                    ['År', 1993]]])
    assert (search([],db) == [])                                             # tom lista
    assert (search((['författare',['j', 'glenn', 'brookshear']],'--'),db) == # tuple
                    [[['författare', ['j', 'glenn', 'brookshear']],
                    ['titel', ['computer', 'science', 'an', 'overview']],
                    ['År', 2011]]])
    assert (search(['&',['titel',['&','&']],'&'],db) ==               # & som categori
                    [[['författare', ['armen', 'asratian']],
                    ['titel', ['diskret', 'matematik']],
                    ['År', 2012]]])
    assert (search(['&','&',['År', 2012]],db) ==                      # & som categori
                    [[['författare', ['armen', 'asratian']],
                    ['titel', ['diskret', 'matematik']],
                    ['År', 2012]]])
    assert (search([['författare', ['adam', 'wille']],                  # hittepÃ¥ bok
                    ['titel', ['programmering', 'och', 'misfÃ¶rstÃ¥nd']], 
                    ['År', 2024]],db) == [])                   


if __name__ == '__main__':
    test_func()
