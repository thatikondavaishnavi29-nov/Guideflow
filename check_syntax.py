import sys, ast
sys.stdout.reconfigure(encoding='utf-8')

files = [
    'app.py',
    'services/ai_service.py',
    'services/web_service.py',
    'services/gov_catalogue.py',
    'components/guidance.py',
    'utils/config.py',
    'test_flows.py',
]

all_ok = True
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            ast.parse(fh.read())
        print(f'  OK  {f}')
    except SyntaxError as e:
        print(f'  SYNTAX ERROR in {f}: {e}')
        all_ok = False
    except Exception as e:
        print(f'  ERROR reading {f}: {e}')
        all_ok = False

print()
print('All files OK' if all_ok else 'SOME FILES HAVE ISSUES')
