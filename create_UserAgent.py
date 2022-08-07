"""
随机产生一个User-Agent
User-Agent: Mozilla/<version> (<system-information>) <platform> (<platform-details>) <extensions>
"""

from random import choice

# 系统版本
system_information_list = ['(Windows NT 10.0; Win64; x64)',
                           '(Windows NT 6.1; Win64; x64)',
                           '(Windows NT 6.3; Win64; x64)']

# 浏览器内核版本
chrome_list = ['91.0.4472.77',
               '88.0.4324.11',
               '87.0.4280.63',
               '87.0.4280.60',
               '87.0.4280.47',
               '86.0.4240.198',
               '86.0.4240.193',
               '86.0.4240.183',
               '86.0.4240.111',
               '86.0.4240.75',
               '85.0.4183.121',
               '85.0.4183.83',
               '84.0.4147.135']


def random_UserAgent(edge=False):  # 随机产生一个U-A 输出
    """

    :param edge: True:伪装成edge浏览器 False:伪装成chrome浏览器
    :return: header: 请求头字典
    """
    system_information = choice(system_information_list)
    chrome = choice(chrome_list)
    if not edge:  # 不需要edge标  默认无edge标
        edg = ''
        user_agent = 'Mozilla/5.0 ' \
                     f'{system_information} ' \
                     'AppleWebKit/537.36 ' \
                     '(KHTML, like Gecko) ' \
                     f'Chrome/{chrome} ' \
                     'Safari/537.36' \
                     f'{edg}'
    else:  # 需要edge标
        edg_list = [' Edg/91.0.864.41',
                    'Edg/103.0.1264.49']
        edg = choice(edg_list)
        user_agent = 'Mozilla/5.0 ' \
                     f'{system_information} ' \
                     'AppleWebKit/537.36 ' \
                     '(KHTML, like Gecko) ' \
                     f'Chrome/{chrome} ' \
                     'Safari/537.36' \
                     f'{edg}'
    header = {
        'User-Agent': f'{user_agent}'
    }
    return header


if __name__ == '__main__':
    print(random_UserAgent())
    print(random_UserAgent(edge=True))
