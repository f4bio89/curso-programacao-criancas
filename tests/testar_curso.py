from pathlib import Path
import ast
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
miss = sorted(root.glob('missao_[0-9][0-9]'))
assert len(miss) == 24, f'Esperadas 24 missões; encontrei {len(miss)}'
for folder in miss:
    for name in ['README.md', 'guia_professor.md', 'missao.md']:
        p = folder / name
        assert p.is_file() and len(p.read_text(encoding='utf-8').strip()) > 100, p
for py in root.glob('missao_*/materiais/*.py'):
    if py.name != 'bug.py':  # bug.py é propositalmente quebrado para a atividade.
        ast.parse(py.read_text(encoding='utf-8'), filename=str(py))
inputs = {
    '12': '', '13': 'Ana\nazul\ngato\n', '14': 'Lia\nvoar\nnas nuvens\n',
    '15': '7\n', '16': '\n', '17': 'ponte\n', '18': 'pronto\n',
    '19': 'pedra\nsair\n', '20': 'Vou aprender?\n', '21': 'Lia\n',
    '22': 'oi\nsair\n',
}
for py in root.glob('missao_*/materiais/solucao.py'):
    numero = py.parents[1].name.split('_')[1]
    result = subprocess.run([sys.executable, str(py)], input=inputs[numero], text=True, capture_output=True, timeout=5)
    assert result.returncode == 0, f'{py}: {result.stderr}'
portal = (root / 'docs' / 'portal' / 'index.html').read_text(encoding='utf-8')
for required in ['role="dialog"', 'aria-modal="true"', 'aria-live="polite"', 'role="img"', 'prefers-reduced-motion', 'function unlocked(n){return n===1', 'function openModal']:
    assert required in portal, f'Contrato do portal ausente: {required}'
print(f'OK: {len(miss)} missões, Markdown obrigatório, códigos Python e contrato do portal verificados.')
