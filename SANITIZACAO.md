# Sanitização desta versão pública

Esta é uma cópia sanitizada de um sistema em uso real num contrato de infraestrutura. Nenhum dado do cliente está aqui; tudo o que aparece como exemplo é inventado.

## O que foi removido

- Arquivos de proveniência/governança interna (`PROVENANCE.md`, `OWNERSHIP.md`).

## O que foi trocado

- Nome do programa/contrato → `Programa`; script renomeado para `criar_pastas_produtos.py`.
- Caminho local → variável `PROG_PRODUTOS_DIR` (padrão `./produtos`).
- Títulos reais dos produtos → títulos genéricos (os mesmos do `gerador-de-dossies`).

## O que é fictício

- Não há dado versionado: o script só cria pastas vazias.

## Como verificar

Sem suíte automatizada. Smoke:

```bat
py criar_pastas_produtos.py
```

Cria a árvore em `.\produtos\` (ignorada pelo Git).

Varreduras da versão pública (2026-11-19): gitleaks `dir` sem achados; busca por caminho local, e-mail, nomes do cliente e links privados sem ocorrências.
