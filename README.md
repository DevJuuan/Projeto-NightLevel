# Night Level

Portal geek bilíngue (PT-BR / EN) com notícias, reviews, lançamentos, categorias e curiosidades sobre jogos, filmes, séries, animes, livros e mangás.

## Estrutura

```
index.html ... (páginas em português)
en/            páginas em inglês (mesmos nomes de arquivo)
css/style.css  único arquivo de estilos
js/main.js     interações, efeitos e validação de formulários
imagens/       coloque aqui as suas imagens (mesmos nomes de antes)
build.py       gera todas as páginas PT e EN a partir de um só lugar
```

## Como editar

Textos e cards ficam em `build.py`. Depois de editar, rode `python build.py` para regenerar as 30 páginas.
Para ver o site, abra `index.html` ou use um servidor local (ex.: extensão Live Server).

## Recursos

- Menu responsivo com hambúrguer, dropdown acessível e página atual destacada
- Barra de XP no topo que acompanha a rolagem e botão "LV" para voltar ao topo
- Fundo de estrelas animado, hero com efeito neon e frases digitadas
- Cards com inclinação 3D e brilho que segue o mouse
- Notícias com filtro por categoria, busca ao vivo e "ler mais"
- Curiosidades com menu fixo que destaca a seção atual
- Tabelas de popularidade com barras animadas
- Formulários com validação, medidor de força de senha e avisos (toast)
- Troca de idioma que leva para a mesma página no outro idioma
- Respeita `prefers-reduced-motion`, foco visível e imagens com fallback

## Tecnologias

HTML5, CSS3 (variáveis, grid, flexbox) e JavaScript puro.
