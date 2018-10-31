istep = _int(step)
        if istep != step:
            raise ValueError("non-integer step for randrange()")
        if istep > 0:
            n = (width + istep - 1) // istep
        elif istep < 0:
            n = (width + istep + 1) // istep
        else:
            raise ValueError("zero step for randrange()")

        if n <= 0:
            raise ValueError("empty range for randrange()")


return ''.join(random.choice(chars) for i in range(size))return istart + istep*self._randbelow(n)
