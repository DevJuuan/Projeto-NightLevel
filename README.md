# 🌙 Night Level

Portal geek bilíngue (PT-BR / EN) com notícias, reviews, lançamentos, categorias e curiosidades sobre **jogos, filmes, séries, animes, livros e mangás**. Projeto front-end feito com HTML, CSS e JavaScript puro, sem frameworks.

> Melhore o nível da sua noite!

## Funcionalidades

- **15 páginas em 2 idiomas** (português e inglês), com troca de idioma que leva para a mesma página no outro idioma
- **Notícias** com filtro por categoria, busca em tempo real e botão "Ler mais"
- **Curiosidades** com menu fixo que destaca a seção que você está lendo
- **Categorias** (jogos, filmes, séries, animes, livros e mangás), cada uma com tabela de popularidade por gênero e cards de destaque
- **Reviews** e **Lançamentos e Eventos**
- **Login, cadastro e contato** com validação de campos, medidor de força de senha e avisos na tela (front-end)
- **Efeitos visuais:** barra de XP que acompanha a rolagem, fundo de estrelas animado, hero com efeito neon e texto digitado, cards com inclinação 3D e brilho que segue o mouse, animações ao rolar a página
- **Responsivo:** menu hambúrguer no celular e grades que se adaptam a qualquer tela

## Acessibilidade e boas práticas

Link "pular para o conteúdo", foco visível para navegação por teclado, textos alternativos nas imagens, `prefers-reduced-motion` respeitado, imagens com fallback quando faltam e meta tags de SEO com `hreflang` entre os idiomas.

## Tecnologias

HTML5 semântico · CSS3 (variáveis, Grid, Flexbox, animações) · JavaScript (ES6+, Intersection Observer, Canvas) · Python (gerador das páginas)

## Estrutura

```
index.html, noticias-*.html, ...   páginas em português
en/                                páginas em inglês (mesmos nomes de arquivo)
css/style.css                      estilos de todo o site
js/main.js                         interações, efeitos e validação de formulários
imagens/                           imagens do projeto
build.py                           gera as 30 páginas (PT e EN) a partir de um só lugar
```

## Como rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/DevJuuan/NightLevel.git
   ```
2. Abra o `index.html` no navegador, ou use um servidor local (por exemplo, a extensão Live Server do VS Code).

### Editando o conteúdo

Os textos e cards ficam no `build.py`. Depois de editar, regenere as páginas:

```bash
python build.py
```

##  Autor

**Juan Vicente de Oliveira** · [@DevJuuan](https://github.com/DevJuuan)
