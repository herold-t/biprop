import os
from contextlib import redirect_stdout

directories = [os.path.join('tests', path) for path in os.listdir('tests/')
               if os.path.isdir(os.path.join('tests', path))]

total_tests     = 0
total_successes = 0

for directory in directories:
    tests = [os.path.join(directory, file) for file in os.listdir(directory)
             if file[-3:]=='.py']
    successes    = 0
    print(f'Running {os.path.basename(directory)} ({len(tests)} tests).')
    
    for n, test in enumerate(tests):
        print(f'\rCompleted {n}/{len(tests)} tests.', end='')
        try:
            with open('tests/temp_stdout.txt', 'x') as temp_out:
                with redirect_stdout(temp_out):
                    with open(test, 'r') as t:
                        exec(t.read())
                        successes += 1
        except Exception as e:
            print(f'\rFailed {os.path.basename(test)} in line {e.__traceback__.tb_next.tb_lineno} with {type(e).__name__}:\n    {e}')
        os.remove('tests/temp_stdout.txt')
    
    total_tests     += len(tests)
    total_successes += successes
    print(f'\rCompleted {os.path.basename(directory)} with {successes} successes and {len(tests)-successes} failures.\n')

print('Test Results\n------------')
print(f'Total tests: {total_tests:>3}')
print(f'Successes  : {total_successes:>3}')
print(f'Failures   : {total_tests-total_successes:>3}')