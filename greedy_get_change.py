# Uses python2

def get_change(m):
    if m == 0:
        return 0
    else:
        coins = [10, 5, 1]
        n_coin = 0
        m_left = m
        #print m_left
        for i in range(3):
            n_coin += m_left / coins[i]
            #print n_coin
            m_left = m_left % coins[i] 
            #print m_left
            if m_left == 0:
                break
        return n_coin

print(get_change(input()))