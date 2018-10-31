def remove_non_ascii(text): 
    return ''.join(c for c in text if ord(c) < 128)

def process(r):
    print '{o}/{n}   (watchers: {w}, forks: {f}, updated: {u})'.format(o=r['owner'], 
                                                                       n=r['name'], 
                                                                       w=r['watchers'], 
                                                                       f=r['forks'],
                                                                       u=r['pushed'][:10])
    desc = '\n'.join(textwrap.wrap(remove_non_ascii(r['description']), WIDTH))
    print '{d}'.format(d=desc)
    print '{url}'.format(url=r['url']),
    if r.has_key('homepage') and r['homepage']:
        print '/  {hp}'.format(hp=r['homepage'])
    else:
print
