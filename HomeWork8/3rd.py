params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'

import pdb
pdb.set_trace()
params_list = [f'{key}={value}' for key, value in params.items()]

result_link = initial_str + '&'.join(params_list)
print(result_link)
