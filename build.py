#!/usr/bin/env python3
"""Gera todas as páginas do Night Level (PT na raiz, EN em /en).
Uso: python build.py   — edite os textos aqui e rode de novo."""
import os
from html import escape as esc

ROOT = os.path.dirname(os.path.abspath(__file__))
L = ("pt", "en")

UI = {
    "pt": dict(html="pt-br", tag="Melhore o nível da sua noite!", news="NOTÍCIAS", n=("Últimas Notícias", "Reviews e Análises", "Lançamentos e Eventos"),
               cats="CATEGORIAS", cur="CURIOSIDADES", contact="CONTATO", login="ENTRAR", other="EN", otheralt="English", otherflag="america-flag.png",
               skip="Pular para o conteúdo", menu="Abrir menu", top="Voltar ao topo", about="Portal de notícias, curiosidades e novidades do universo geek. Melhore o nível da sua noite!",
               topics="Tópicos", socials="Redes", rights="Todos os direitos reservados.", home="Início", meta="Notícias, reviews e curiosidades do universo geek."),
    "en": dict(html="en", tag="Level up your night!", news="NEWS", n=("Latest News", "Reviews & Analysis", "Releases & Events"),
               cats="CATEGORIES", cur="CURIOSITIES", contact="CONTACT", login="SIGN IN", other="PT", otheralt="Português", otherflag="brazil-flag.png",
               skip="Skip to content", menu="Open menu", top="Back to top", about="News, curiosities and updates from the geek universe. Level up your night!",
               topics="Topics", socials="Socials", rights="All rights reserved.", home="Home", meta="News, reviews and curiosities from the geek universe."),
}
TITLES = {
    "index": ("Início", "Home"), "noticias-ultimas": ("Notícias", "News"), "noticias-reviews": ("Reviews e Análises", "Reviews & Analysis"),
    "noticias-lancamentos": ("Lançamentos e Eventos", "Releases & Events"), "categorias": ("Categorias", "Categories"),
    "curiosidades": ("Curiosidades", "Curiosities"), "contato": ("Contato", "Contact"), "login": ("Login", "Sign in"),
    "registro": ("Criar Conta", "Create Account"), "jogos": ("Jogos", "Games"), "filmes": ("Filmes", "Movies"), "series": ("Séries", "Series"),
    "animes": ("Animes", "Anime"), "livros": ("Livros", "Books"), "mangas": ("Mangás", "Manga"),
}

# ---------------------------------------------------------------- dados
CATS = [  # arquivo, ícone, nome pt/en, descrição pt/en
    ("jogos", "🎮", "Jogos", "Games", "Trailers, gameplays e lançamentos.", "Trailers, gameplay and releases."),
    ("filmes", "🎬", "Filmes", "Movies", "Do cinema às estreias da semana.", "From cinema to this week's premieres."),
    ("series", "📺", "Séries", "Series", "Maratonas e histórias que prendem.", "Binge-worthy stories."),
    ("animes", "🌸", "Animes", "Anime", "Os animes mais assistidos.", "The most-watched anime."),
    ("livros", "📚", "Livros", "Books", "Leituras que marcaram gerações.", "Reads that shaped generations."),
    ("mangas", "📖", "Mangás", "Manga", "Os mangás mais lidos do mundo.", "The world's most-read manga."),
]
LEVEL = {"pt": {5: "Muito alta", 4: "Alta", 3: "Média"}, "en": {5: "Very high", 4: "High", 3: "Medium"}}

PAGES_CAT = {  # banner, cabeçalhos, linhas (pt, en, nível, exemplo pt, exemplo en), cards (img, tpt, ten, dpt, den)
    "filmes": dict(banner="NightLevel-Filmes.png",
        t=("Filmes em Destaque", "Featured Movies"),
        d=("Os filmes mais assistidos, curiosidades e novidades do cinema.", "The most-watched movies, fun facts and the latest from cinema."),
        th=(("Gênero", "Popularidade", "Exemplo de filme"), ("Genre", "Popularity", "Example movie")),
        ts=("Gêneros mais assistidos", "Most-watched genres"), ch=("Destaques da semana", "Highlights of the week"),
        rows=[("Ação", "Action", 5, "John Wick 4", "John Wick 4"), ("Ficção Científica", "Science Fiction", 4, "Duna: Parte 2", "Dune: Part Two"),
              ("Terror", "Horror", 4, "Invocação do Mal", "The Conjuring"), ("Comédia", "Comedy", 3, "Superbad", "Superbad"),
              ("Animação", "Animation", 3, "Divertida Mente 2", "Inside Out 2")],
        cards=[("avatar-filmes.jpg", "Avatar: Fogo e Cinzas", "Avatar: Fire and Ash", "Conflitos intensos em Pandora entre tribos Na'vi e novos inimigos humanos poderosos.", "Intense conflicts on Pandora between the Na'vi tribes and powerful new human enemies."),
               ("superman-filmes.webp", "Superman (2025)", "Superman (2025)", "Reboot mostra Clark equilibrando humanidade e heroísmo enquanto enfrenta ameaças e desconfiança mundial.", "The reboot shows Clark balancing humanity and heroism while facing threats and global distrust."),
               ("mickey-filme.jpg", "Mickey 17", "Mickey 17", "Clone descartável enfrenta dilemas existenciais ao coexistir com outra versão de si mesmo.", "A disposable clone faces existential dilemmas as he coexists with another version of himself.")]),
    "series": dict(banner="NightLevel-Series.png",
        t=("Séries em Destaque", "Featured Series"),
        d=("As séries mais assistidas, suas curiosidades e as últimas novidades.", "The most-watched series, their trivia and the latest updates."),
        th=(("Gênero", "Popularidade", "Exemplo de série"), ("Genre", "Popularity", "Example series")),
        ts=("Gêneros mais assistidos", "Most-watched genres"), ch=("Séries para maratonar", "Series to binge"),
        rows=[("Ação", "Action", 5, "The Boys", "The Boys"), ("Drama", "Drama", 4, "Breaking Bad", "Breaking Bad"),
              ("Ficção Científica", "Science Fiction", 4, "Stranger Things", "Stranger Things"),
              ("Terror", "Horror", 3, "The Haunting of Hill House", "The Haunting of Hill House"), ("Comédia", "Comedy", 3, "Brooklyn Nine-Nine", "Brooklyn Nine-Nine")],
        cards=[("TheBoys-series.jpg", "The Boys", "The Boys", "Uma sátira sombria sobre super-heróis e o poder da mídia.", "A dark satire about superheroes and the power of media."),
               ("StrangerThings-series.jpg", "Stranger Things", "Stranger Things", "Aventura e mistério em uma cidade marcada por fenômenos sobrenaturais.", "Adventure and mystery in a town plagued by supernatural phenomena."),
               ("BreakingBad-series.webp", "Breaking Bad", "Breaking Bad", "Um professor de química se transforma em um dos maiores criminosos da cidade.", "A chemistry teacher becomes one of the city's most feared criminals."),
               ("PeakyBlinders-series.jpg", "Peaky Blinders", "Peaky Blinders", "Uma gangue inglesa dominando as ruas com estilo e brutalidade.", "An English gang ruling the streets with style and brutality.")]),
    "animes": dict(banner="NightLevel-Animes.png",
        t=("Animes em Destaque", "Featured Anime"),
        d=("Os animes mais assistidos, suas curiosidades e as últimas novidades.", "The most-watched anime, their trivia and the latest news."),
        th=(("Gênero", "Popularidade", "Exemplo de anime"), ("Genre", "Popularity", "Example anime")),
        ts=("Gêneros mais assistidos", "Most-watched genres"), ch=("Animes para começar", "Anime to start with"),
        rows=[("Shounen", "Shounen", 5, "One Piece", "One Piece"), ("Ação / Fantasia", "Action / Fantasy", 4, "Attack on Titan", "Attack on Titan"),
              ("Isekai", "Isekai", 4, "Re:Zero", "Re:Zero"), ("Romance", "Romance", 3, "Your Name", "Your Name"),
              ("Terror / Psicológico", "Horror / Psychological", 3, "Tokyo Ghoul", "Tokyo Ghoul")],
        cards=[("AoT-animes.webp", "Attack on Titan", "Attack on Titan", "A humanidade luta pela sobrevivência em um mundo dominado por titãs gigantes.", "Humanity fights for survival in a world ruled by gigantic titans."),
               ("OnePiece-animes.jpg", "One Piece", "One Piece", "Um pirata sonhador e sua tripulação em busca do lendário tesouro One Piece.", "A dreamer pirate and his crew sail the seas in search of the legendary One Piece."),
               ("Jujutsu-animes.jpg", "Jujutsu Kaisen", "Jujutsu Kaisen", "Feiticeiros enfrentam maldições poderosas em batalhas de tirar o fôlego.", "Sorcerers face powerful curses in breathtaking battles."),
               ("DemonSlayer-anime.jpg", "Demon Slayer", "Demon Slayer", "Tanjiro busca vingança contra demônios enquanto protege sua irmã Nezuko.", "Tanjiro seeks revenge against demons while protecting his sister Nezuko.")]),
    "livros": dict(banner="NightLevel-Livros.jpg",
        t=("Livros em Destaque", "Featured Books"),
        d=("Os livros mais lidos, suas curiosidades e as novidades das livrarias.", "The most-read books, their trivia and the latest from bookstores."),
        th=(("Gênero", "Popularidade", "Exemplo de obra"), ("Genre", "Popularity", "Example book")),
        ts=("Gêneros mais lidos", "Most-read genres"), ch=("Leituras em destaque", "Featured reads"),
        rows=[("Fantasia", "Fantasy", 5, "Harry Potter", "Harry Potter"), ("Ficção Científica", "Science Fiction", 4, "Duna", "Dune"),
              ("Romance", "Romance", 3, "Orgulho e Preconceito", "Pride and Prejudice"), ("Suspense / Mistério", "Thriller / Mystery", 3, "O Código Da Vinci", "The Da Vinci Code"),
              ("Terror", "Horror", 3, "It: A Coisa", "It")],
        cards=[("Duna-livros.jpg", "Duna", "Dune", "Uma das maiores obras da ficção científica, explorando política, ecologia e poder em um planeta desértico.", "One of sci-fi's greatest works, exploring politics, ecology and power on a desert planet."),
               ("HP-livros.jpg", "Harry Potter e a Pedra Filosofal", "Harry Potter and the Philosopher's Stone", "O início da jornada do jovem bruxo que conquistou gerações.", "The beginning of the young wizard's journey that captivated generations."),
               ("SdA-livros.jpg", "O Senhor dos Anéis", "The Lord of the Rings", "Uma aventura épica que redefiniu a fantasia e inspirou gerações de leitores.", "An epic adventure that redefined fantasy and inspired generations of readers."),
               ("IT-livros.jpg", "It: A Coisa", "It", "O terror de Stephen King ganha vida em uma narrativa intensa e sombria.", "Stephen King's horror comes alive in an intense, chilling narrative.")]),
    "mangas": dict(banner="NightLevel-Manga.png",
        t=("Mangás em Destaque", "Featured Manga"),
        d=("Os mangás mais lidos, suas curiosidades e os últimos lançamentos.", "The most-read manga, their trivia and the latest releases."),
        th=(("Gênero", "Popularidade", "Exemplo de mangá"), ("Genre", "Popularity", "Example manga")),
        ts=("Gêneros mais lidos", "Most-read genres"), ch=("Mangás para ler agora", "Manga to read now"),
        rows=[("Shounen", "Shounen", 5, "One Piece", "One Piece"), ("Seinen", "Seinen", 4, "Berserk", "Berserk"), ("Isekai", "Isekai", 4, "That Time I Got Reincarnated as a Slime", "That Time I Got Reincarnated as a Slime"),
              ("Shoujo", "Shoujo", 3, "Sailor Moon", "Sailor Moon"), ("Josei", "Josei", 3, "Nana", "Nana")],
        cards=[("onepiece-manga.jpg", "One Piece", "One Piece", "As aventuras de Luffy em busca do lendário tesouro dos piratas, o One Piece.", "Luffy's adventures in search of the legendary pirate treasure, the One Piece."),
               ("berserk-manga.webp", "Berserk", "Berserk", "Uma jornada sombria e brutal em um mundo medieval repleto de monstros e tragédias.", "A dark, brutal journey through a medieval world of monsters and tragedy."),
               ("tokioghoul-manga.jpg", "Tokyo Ghoul", "Tokyo Ghoul", "Um jovem que se torna meio-ghoul e precisa sobreviver entre humanos e monstros.", "A young man becomes half-ghoul and must survive between humans and monsters."),
               ("DemonSlayer-manga.webp", "Demon Slayer", "Demon Slayer", "O mangá que conquistou o mundo com arte impecável e uma história emocionante.", "The manga that conquered the world with stunning art and an emotional story.")]),
}
JOGOS = dict(t=("Jogos", "Games"), d=("Trailers, gameplays e novidades do universo dos jogos.", "Trailers, gameplay and the latest news from the gaming universe."),
    vt=("Grand Theft Auto VI | 2º Trailer", "Grand Theft Auto VI | Trailer 2"),
    vx=("Os melhores trailers e análises de jogos que estão movimentando o mundo gamer. Fique ligado para descobrir novos títulos, easter eggs e segredos dos games mais esperados do ano.",
        "The best trailers and game analyses shaking the gaming world. Stay tuned for new titles, easter eggs and secrets from the most anticipated games of the year."),
    ch=("Últimas notícias de jogos", "Latest gaming news"),
    cards=[("hades-jogos.jfif", "Hades II", "Hades II", "Melinoë enfrenta Cronos em um roguelike veloz, com narrativa sombria e progressão viciante.", "Melinoë faces Cronos in a fast roguelike with a dark narrative and addictive progression."),
           ("hollow-jogos.jpeg", "Hollow Knight: Silksong", "Hollow Knight: Silksong", "Hornet explora um novo reino cheio de perigos, com agilidade aprimorada e desafios metroidvania profundos.", "Hornet explores a new realm full of dangers, with sharper agility and deep Metroidvania challenges."),
           ("monster-jogos.jfif", "Monster Hunter Wilds", "Monster Hunter Wilds", "Caçadas intensas em um mundo dinâmico, com clima imprevisível, monstros gigantes e estratégia contínua.", "Intense hunts in a dynamic world with unpredictable weather, giant monsters and constant strategy.")])

NEWS = [  # categoria, imagem, título pt, texto pt, título en, texto en
    ("jogos", "NVIDIA-ultimas.jpg", "Novidade nos jogos", "A NVIDIA anunciou na Gamescom 2025 que vários jogos usarão a tecnologia DLSS 4 com ray tracing e path tracing para melhorar drasticamente os gráficos. Alguns desses títulos chegarão por meio do serviço de nuvem GeForce NOW.",
     "New in games", "NVIDIA announced at Gamescom 2025 that several games will use DLSS 4 with ray tracing and path tracing to dramatically improve graphics. Some of these titles will arrive through the GeForce NOW cloud service."),
    ("filmes", "cinemacon-ultimas.jpg", "CinemaCon 2025 revela grandes novidades", "No evento CinemaCon, estúdios anunciaram novos títulos como Avatar: Fire & Ash, o reboot do Superman por James Gunn e M3GAN 2.0.",
     "CinemaCon 2025 reveals big news", "At CinemaCon, studios announced new titles such as Avatar: Fire & Ash, the Superman reboot by James Gunn, and M3GAN 2.0."),
    ("animes", "chainsaw-ultimas.jpeg", "Chainsaw Man: The Movie – Arco Reze estreia em 19 de setembro de 2025", "A continuação canônica do anime adapta o arco “Bomb Girl” do mangá e foca na relação de Denji com Reze.",
     "Chainsaw Man: The Movie – Reze Arc premieres September 19, 2025", "The canonical continuation of the anime adapts the “Bomb Girl” arc from the manga and focuses on Denji's relationship with Reze."),
    ("series", "blackmirror-ultimas.jpg", "Black Mirror retorna em 2025 com 6 novos episódios, incluindo sequência de “USS Callister”", "A série antológica da Netflix lança novas histórias e, pela primeira vez, um episódio será continuação direta de um capítulo anterior.",
     "Black Mirror returns in 2025 with 6 new episodes, including a “USS Callister” sequel", "The Netflix anthology series launches new stories and, for the first time, an episode will be a direct continuation of a previous one."),
    ("series", "911-ultimas.jpg", "Chris O’Donnell estrela o novo spin-off “9-1-1: Nashville” em 2025", "O ator entra na franquia “9-1-1” como capitão de um corpo de bombeiros em Nashville, na nova série da ABC.",
     "Chris O’Donnell stars in new spin-off “9-1-1: Nashville” in 2025", "The actor joins the “9-1-1” franchise as a fire captain in Nashville, in the new ABC series."),
    ("filmes", "D23-ultimas.jpg", "Disney faz anúncios no Destination D23 2025", "Na convenção D23, a Disney revelou um teaser de Avengers: Doomsday, novidades de Toy Story 5 e outras produções futuras.",
     "Disney makes announcements at Destination D23 2025", "At the D23 convention, Disney revealed a teaser for Avengers: Doomsday, news about Toy Story 5, and other upcoming productions."),
    ("livros", "jogosvorazes-ultimas.jpeg", "Suzanne Collins lança novo romance de ‘Jogos Vorazes’: Sunrise on the Reaping", "O livro se passa 24 anos antes da trilogia original e foca no 50º Jogos Vorazes, com Haymitch Abernathy como protagonista. Estreia em 18 de março de 2025.",
     "Suzanne Collins releases new ‘Hunger Games’ novel: Sunrise on the Reaping", "The book takes place 24 years before the original trilogy and focuses on the 50th Hunger Games, with Haymitch Abernathy as the protagonist. It debuts March 18, 2025."),
    ("manga", "crunchyroll-ultimas.jpg", "Crunchyroll anuncia novo app para leitura de mangás", "A plataforma vai lançar o app Crunchyroll Manga, inicialmente nos EUA e Canadá, para Android, iOS e, futuramente, web.",
     "Crunchyroll announces new manga reading app", "The platform will launch the Crunchyroll Manga app, initially in the US and Canada, for Android, iOS and, later, web."),
]
TAGS = {"jogos": ("Jogos", "Games"), "filmes": ("Filmes", "Movies"), "series": ("Séries", "Series"), "animes": ("Animes", "Anime"), "livros": ("Livros", "Books"), "manga": ("Mangá", "Manga")}

REVIEWS = [
    ("echoes-reviews.jpg", "Review – “Echoes of Eternity”: um RPG que redefine o gênero", "Com trilha sonora épica e combate estratégico, Echoes of Eternity entrega uma experiência nostálgica e moderna ao mesmo tempo.",
     "Review – “Echoes of Eternity”: an RPG that redefines the genre", "With an epic soundtrack and strategic combat, Echoes of Eternity delivers a nostalgic and modern experience at once."),
    ("horizonte-reviews.jpg", "Análise – “O Horizonte Perdido”: ficção científica com alma", "Uma obra visualmente deslumbrante que equilibra drama humano e questões existenciais em um futuro colapsado.",
     "Review – “The Lost Horizon”: science fiction with soul", "A visually stunning work that balances human drama and existential questions in a collapsed future."),
    ("crimsom-reviews.jpg", "Review – “Crimson Tower”: mistério, poder e traição", "Uma série que mistura suspense e fantasia em um universo sombrio e elegante. Vale a maratona!",
     "Review – “Crimson Tower”: mystery, power and betrayal", "A series that blends suspense and fantasy in a dark, elegant universe. Totally binge-worthy!"),
    ("blazespirits-reviews.jpg", "Análise – “Ghost Rider: Blaze Spirits”: quando a fúria encontra o sobrenatural", "Visual brutal, atmosfera infernal e ação frenética: Blaze Spirits entrega um Motoqueiro Fantasma mais visceral e intenso do que nunca.",
     "Review – “Ghost Rider: Blaze Spirits”: when fury meets the supernatural", "Brutal visuals, infernal atmosphere and frenetic action: Blaze Spirits delivers a Ghost Rider more visceral and intense than ever."),
]

LANC = dict(
    h=(("Próximos lançamentos", "Upcoming releases"), ("Eventos imperdíveis", "Must-see events")),
    d=("Datas, locais e destaques dos próximos lançamentos e eventos geek, gamer e de cinema.", "Dates, places and highlights of upcoming geek, gaming and film releases and events."),
    rel=[("🎮", "TheEnd-Lancamentos.png", "“The End of History”: estratégia, combate e alma de RPG com decisões que mudam a história", "O jogador entra em um mundo aberto numa Europa feudal fictícia, onde decisões, alianças, traições e guerras determinam o destino de uma sociedade à beira do colapso.",
          "“The End of History”: strategy, combat and RPG spirit with decisions that change history", "The player enters an open world in a fictional feudal Europe, where decisions, alliances, betrayals and wars decide the fate of a society on the brink of collapse."),
         ("🎬", "eclipse-lancamentos.webp", "“Eclipse of Illusion”: magia proibida, guerras antigas e o renascimento de um poder esquecido", "Kael desperta após um século selado e encontra um mundo transformado, onde a magia foi banida e criaturas sombrias governam as ruínas da civilização.",
          "“Eclipse of Illusion”: forbidden magic, ancient wars and the rebirth of a forgotten power", "Kael awakens after a century sealed away and finds a transformed world where magic is banned and dark creatures rule the ruins of civilization."),
         ("🌸", "bullet-lancamentos.webp", "“Bullet/Bullet”: distopia pós-apocalíptica, risco constante e laços improváveis de sobrevivência", "Num futuro devastado, o garoto Gear, o apostador White Bear e o robô Qu-0213 vivem de resgates, até aceitarem o pedido da misteriosa Noah e entrarem numa trama de poder, traição e redenção.",
          "“Bullet/Bullet”: post-apocalyptic dystopia, constant risk and unlikely bonds of survival", "In a devastated future, the boy Gear, the gambler White Bear and the robot Qu-0213 live off rescues, until the mysterious Noah's request drags them into a plot of power, betrayal and redemption.")],
    ev=[("🎮", "gameverse-lancamentos.png", "GameVerse Expo 2025", "O maior evento de games da América Latina acontece em São Paulo, de 10 a 13 de dezembro. Painéis, demos e convidados especiais.",
         "GameVerse Expo 2025", "The largest gaming event in Latin America takes place in São Paulo, December 10–13. Panels, demos and special guests."),
        ("🎬", "cinecon-lancamentos.jfif", "CineCon Experience", "Festival internacional de cinema geek com pré-estreias exclusivas e workshops com diretores. De 25 a 28 de novembro, no Rio de Janeiro.",
         "CineCon Experience", "International geek film festival with exclusive premieres and workshops with directors. November 25–28, in Rio de Janeiro."),
        ("🌸", "animespirit-lancamentos.jfif", "Anime Spirit 2025", "Encontro nacional da cultura otaku com atrações exclusivas, competições temáticas e experiências imersivas.",
         "Anime Spirit 2025", "National gathering of otaku culture with exclusive attractions, themed competitions and immersive experiences.")])

CURIO = [  # id, (nome pt, en), itens (img, título pt, en, texto pt, en)
    ("jogos", ("Jogos", "Games"), [
        ("minecraft-curiosidade.jpg", "Minecraft", "Minecraft", "O primeiro protótipo de Minecraft foi feito por Markus “Notch” Persson em apenas seis dias.", "The first Minecraft prototype was built by Markus “Notch” Persson in just six days."),
        ("konami-curiosidades.webp", "Código Konami", "The Konami Code", "O famoso Código Konami nasceu quando um desenvolvedor achou Gradius difícil demais durante os testes e criou um atalho para facilitar o jogo.", "The famous Konami Code was born when a developer found Gradius too hard while testing and built a shortcut to make it easier."),
        ("elderscrolls-curiosidades.jfif", "Elder Scrolls", "Elder Scrolls", "The Elder Scrolls II: Daggerfall tem um dos maiores mapas já feitos, com mais de 15 mil cidades, vilas e dungeons.", "The Elder Scrolls II: Daggerfall has one of the largest maps ever made, with over 15,000 towns, villages and dungeons."),
        ("adventure-curiosidades.webp", "Adventure", "Adventure", "O primeiro easter egg famoso dos games está em Adventure (1980), da Atari: uma sala secreta com o nome do programador.", "The first famous video game easter egg is in Adventure (1980), by Atari: a secret room with the programmer's name.")]),
    ("filmes", ("Filmes", "Movies"), [
        ("toystory-curiosidades.jpg", "Toy Story", "Toy Story", "Toy Story (1995) foi o primeiro longa-metragem totalmente feito por computação gráfica.", "Toy Story (1995) was the first feature film made entirely with computer animation."),
        ("MagicoOz-curiosidades.jpg", "O Mágico de Oz", "The Wizard of Oz", "O primeiro Homem de Lata, Buddy Ebsen, foi hospitalizado pela maquiagem de pó de alumínio e substituído por Jack Haley.", "The first Tin Man, Buddy Ebsen, was hospitalized by the aluminum-dust makeup and replaced by Jack Haley."),
        ("avatar-curiosidades.jpg", "Avatar", "Avatar", "Durante a produção, o filme de James Cameron teve o título provisório “Project 880”.", "During production, James Cameron's film had the working title “Project 880”."),
        ("dartvader-curiosidades.jpg", "Darth Vader", "Darth Vader", "A respiração de Darth Vader foi criada pelo sound designer Ben Burtt com um regulador de mergulho real.", "Darth Vader's breathing was created by sound designer Ben Burtt using a real scuba regulator.")]),
    ("series", ("Séries", "Series"), [
        ("BreakingBad-curiosidades.jpg", "Breaking Bad", "Breaking Bad", "Matthew Broderick chegou a ser cogitado para viver Walter White antes de Bryan Cranston ser escolhido.", "Matthew Broderick was reportedly considered for Walter White before Bryan Cranston got the role."),
        ("friends-curiosidades.jpg", "Friends", "Friends", "Nas duas últimas temporadas, cada um dos seis protagonistas de Friends recebia US$ 1 milhão por episódio.", "In the last two seasons, each of the six Friends leads earned $1 million per episode."),
        ("GoT-curiosidade.jfif", "Game of Thrones", "Game of Thrones", "Game of Thrones ganhou 59 prêmios Emmy ao longo de sua exibição, recorde entre séries dramáticas.", "Game of Thrones won 59 Emmy Awards during its run, a record for a drama series."),
        ("Mandalorian-curiosidades.jfif", "The Mandalorian", "The Mandalorian", "The Mandalorian popularizou o StageCraft, com telas de LED gigantes no lugar do chroma key.", "The Mandalorian popularized StageCraft, using giant LED walls instead of green screen.")]),
    ("animes", ("Animes", "Anime"), [
        ("naruto-curiosidade.png", "Naruto", "Naruto", "Naruto nasceu de um one-shot publicado em 1997, antes de virar série semanal em 1999.", "Naruto began as a one-shot published in 1997, before becoming a weekly series in 1999."),
        ("onepunch-curiosidade.jpeg", "One Punch Man", "One Punch Man", "One Punch Man começou como um webcomic de traço simples do autor ONE, depois redesenhado por Yusuke Murata.", "One Punch Man began as a simply drawn webcomic by ONE, later redrawn by Yusuke Murata."),
        ("aot-curiosidades.jpg", "Attack on Titan", "Attack on Titan", "Antes de ser publicado, o mangá de Attack on Titan foi recusado pela Shonen Jump e acabou na Bessatsu Shonen Magazine.", "Before being published, the Attack on Titan manga was turned down by Shonen Jump and ended up in Bessatsu Shonen Magazine."),
        ("Akira-curiosidades.jpg", "Akira", "Akira", "Akira (1988) usou cerca de 160 mil quadros desenhados à mão, um recorde para a época.", "Akira (1988) used around 160,000 hand-drawn cels, a record at the time.")]),
    ("livros", ("Livros", "Books"), [
        ("domquixote-curiosidades.jfif", "Dom Quixote", "Don Quixote", "Dom Quixote, de Miguel de Cervantes, costuma ser apontado como o livro de ficção mais vendido da história.", "Don Quixote, by Miguel de Cervantes, is often cited as the best-selling work of fiction ever."),
        ("agatha-curiosidades.png", "Agatha Christie", "Agatha Christie", "Agatha Christie é a autora mais traduzida do mundo, com obras publicadas em mais de 100 idiomas.", "Agatha Christie is the most translated author in the world, with works published in over 100 languages."),
        ("carrie-curiosidades.jfif", "Carrie", "Carrie", "Stephen King jogou o rascunho de Carrie no lixo; sua esposa o resgatou e o incentivou a continuar.", "Stephen King threw the Carrie draft in the trash; his wife rescued it and urged him to keep going."),
        ("pequenoprincipe-curiosidades.jpg", "O Pequeno Príncipe", "The Little Prince", "O Pequeno Príncipe está entre os livros mais traduzidos da história, com versões em centenas de idiomas e dialetos.", "The Little Prince is among the most translated books in history, with editions in hundreds of languages and dialects.")]),
    ("manga", ("Mangás", "Manga"), [
        ("OnePiece-curiosidades.jpg", "One Piece", "One Piece", "One Piece é o mangá mais vendido do mundo, com mais de 500 milhões de cópias em circulação.", "One Piece is the best-selling manga in the world, with over 500 million copies in circulation."),
        ("dragonball-curiosidades.jpg", "Dragon Ball", "Dragon Ball", "Akira Toriyama se inspirou no clássico chinês Jornada ao Oeste para criar Dragon Ball.", "Akira Toriyama drew on the Chinese classic Journey to the West to create Dragon Ball."),
        ("tokioghoul-curiosidades.jpg", "Tokyo Ghoul", "Tokyo Ghoul", "Tokyo Ghoul foi serializado na Weekly Young Jump entre 2011 e 2014, antes de continuar em Tokyo Ghoul:re.", "Tokyo Ghoul ran in Weekly Young Jump from 2011 to 2014, before continuing as Tokyo Ghoul:re."),
        ("mangaka-curiosidades.avif", "Prazos apertados", "Tight deadlines", "Com publicações semanais, muitos mangakás relatam semanas de trabalho muito longas e dormem no próprio estúdio.", "With weekly releases, many mangaka report extremely long work weeks and sleeping at their studios.")]),
]

MAP = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3658.0924662438088!2d-46.635720725022196!3d-23.529176460409868!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce585fbb047051%3A0x1ad799a7c61cd5f3!2sETEC%20de%20S%C3%A3o%20Paulo%20-%20Luz!5e0!3m2!1spt-BR!2sbr!4v1761195459774!5m2!1spt-BR!2sbr"


# ---------------------------------------------------------------- blocos
def img(p, name, alt, extra=""):
    return f'<img src="{p}imagens/{name}" alt="{esc(alt)}" loading="lazy" {extra}>'


def card(p, image, title, text, tag="h3", href=None, more=""):
    inner = (f'<div class="thumb">{img(p, image, title)}</div><div class="card-info"><{tag}>{esc(title)}</{tag}><p>{esc(text)}</p>{more}</div>')
    return f'<a class="card rev" href="{href}">{inner}</a>' if href else f'<article class="card rev">{inner}</article>'


def head(i, lang, key, title, desc, p, auth=False):
    u = UI[lang]
    other = ("en/" + key + ".html") if lang == "pt" else ("../" + key + ".html")
    here = key + ".html"
    alt = f'<link rel="alternate" hreflang="{"en" if lang == "pt" else "pt-br"}" href="{other}">'
    return f'''<!DOCTYPE html>
<html lang="{u["html"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Night Level - {esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#0a0612">
<meta property="og:title" content="Night Level - {esc(title)}">
<meta property="og:description" content="{esc(desc)}">
{alt}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800&family=Poppins:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}css/style.css">
<link rel="icon" href="{p}imagens/NightLevel-ICO.ico">
</head>
<body{' class="auth"' if auth else ''}>
'''


def header(lang, key, p):
    u = UI[lang]
    ac = lambda k: ' aria-current="page"' if key == k else ""
    n = [("noticias-ultimas", u["n"][0]), ("noticias-reviews", u["n"][1]), ("noticias-lancamentos", u["n"][2])]
    dd = "".join(f'<a href="{k}.html"{ac(k)}>{esc(t)}</a>' for k, t in n)
    other = ("en/" + key + ".html") if lang == "pt" else ("../" + key + ".html")
    return f'''<a class="skip" href="#conteudo">{u["skip"]}</a>
<div id="xp" aria-hidden="true"></div>
<canvas id="estrelas" aria-hidden="true"></canvas>
<header class="cabecalho">
<a class="container-logo" href="index.html" aria-label="Night Level - {u["home"]}"><img class="logo" src="{p}imagens/Logo.png" alt="Night Level"><span class="logo-texto">{u["tag"]}</span></a>
<button class="hamburguer" aria-label="{u["menu"]}" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
<nav class="menu" id="menu" aria-label="Menu">
<div class="dropdown"><button class="dd-btn" aria-haspopup="true" aria-expanded="false">{u["news"]} <span class="seta">▾</span></button><div class="dropdown-conteudo">{dd}</div></div>
<a href="categorias.html"{ac("categorias")}>{u["cats"]}</a>
<a href="curiosidades.html"{ac("curiosidades")}>{u["cur"]}</a>
<a href="contato.html"{ac("contato")}>{u["contact"]}</a>
<a class="btn-entrar" href="login.html"{ac("login")}>{u["login"]}</a>
<a class="idioma" href="{other}" hreflang="{"en" if lang == "pt" else "pt-br"}"><img src="{p}imagens/{u["otherflag"]}" alt="{u["otheralt"]}" width="18" height="18"> {u["other"]}</a>
</nav>
</header>
<main id="conteudo">
'''


def footer(lang, p):
    u = UI[lang]
    links = [("curiosidades", u["cur"].title()), ("contato", u["contact"].title()), ("categorias", u["cats"].title()), ("noticias-ultimas", u["n"][0])]
    li = "".join(f'<li><a href="{k}.html">{esc(t)}</a></li>' for k, t in links)
    return f'''</main>
<footer class="rodape">
<div class="rodape-grid">
<div><img class="logo-rodape" src="{p}imagens/Logo.png" alt="Night Level"><p>{u["about"]}</p></div>
<div><h3>{u["topics"]}</h3><ul>{li}</ul></div>
<div><h3>{u["socials"]}</h3><ul><li><a href="#" rel="noopener">Instagram</a></li><li><a href="#" rel="noopener">YouTube</a></li><li><a href="#" rel="noopener">X</a></li></ul></div>
</div>
<p class="copyright">© <span data-ano>2025</span> Night Level - {u["rights"]}</p>
</footer>
<button id="topo" aria-label="{u["top"]}">LV<b>1</b></button>
<script src="{p}js/main.js"></script>
</body>
</html>
'''


def titulo(h, d):
    return f'<h1 class="titulo">{esc(h)}</h1><p class="descricao">{esc(d)}</p>'


def field(id_, label, typ="text", ph="", pw=False, ac="", area=False):
    ctl = (f'<textarea id="{id_}" name="{id_}" rows="5" maxlength="500" placeholder="{esc(ph)}"></textarea>' if area
           else f'<input type="{typ}" id="{id_}" name="{id_}" placeholder="{esc(ph)}" autocomplete="{ac}">')
    eye = '<button type="button" class="ver-senha" aria-label="Show/Hide">👁️</button>' if pw else ""
    return f'<div class="campo"><label for="{id_}">{esc(label)}</label>{ctl}{eye}<span class="msg-erro" role="alert"></span></div>'


# ---------------------------------------------------------------- páginas
def pg_index(lang, p):
    i = L.index(lang)
    hero_img = "hero-night.svg"
    frases = ("Notícias, reviews e curiosidades geek|Jogos, filmes, séries e animes|Suba de nível a cada noite" if lang == "pt"
              else "Geek news, reviews and trivia|Games, movies, series and anime|Level up every night")
    cta = ("Ver notícias", "Explorar categorias") if lang == "pt" else ("Read the news", "Explore categories")
    last = "".join(card(p, NEWS[k][1], NEWS[k][2 + 2 * i], NEWS[k][3 + 2 * i], href="noticias-ultimas.html") for k in (7, 3, 1, 2))
    h2 = ("Últimas notícias", "Latest news") if lang == "pt" else ("Latest news", "")
    return (f'<section class="hero"><img class="hero-bg" src="{p}imagens/{hero_img}" alt="">'
            f'<div><h1>NIGHT LEVEL</h1><p class="digitando" data-frases="{frases}"></p><div class="hero-acoes">'
            f'<a class="btn" href="noticias-ultimas.html">{cta[0]}</a><a class="btn sec" href="categorias.html">{cta[1]}</a></div></div></section>'
            f'<h2 class="subtitulo">📰 {h2[0]}</h2><div class="cards">{last}</div>'), UI[lang]["meta"]


def pg_news(lang, p):
    i = L.index(lang)
    t = TITLES["noticias-ultimas"][i]
    chips = [("todos", "Todos" if lang == "pt" else "All")] + [(k, v[i]) for k, v in TAGS.items()]
    ch = "".join(f'<button class="chip" data-filtro="{k}" aria-pressed="false">{esc(n)}</button>' for k, n in chips)
    ph = "Buscar notícias…" if lang == "pt" else "Search news…"
    cards = ""
    for c in NEWS:
        more = f'<button class="btn-ler" aria-expanded="false">{"Ler mais" if lang == "pt" else "Read more"}</button>'
        cards += (f'<article class="card rev" data-categoria="{c[0]}"><div class="thumb">{img(p, c[1], c[2 + 2 * i])}</div><div class="card-info">'
                  f'<span class="tag {c[0]}">{TAGS[c[0]][i]}</span><h2>{esc(c[2 + 2 * i])}</h2><p class="resumo">{esc(c[3 + 2 * i])}</p>{more}</div></article>')
    empty = "Nenhuma notícia encontrada. Tente outra busca ou categoria." if lang == "pt" else "No news found. Try another search or category."
    return (titulo(t, "Acompanhe o que acontece em jogos, filmes, séries, animes, livros e mangás." if lang == "pt" else "Follow what's happening in games, movies, series, anime, books and manga.")
            + f'<div class="ferramentas"><div class="chips">{ch}</div><input class="busca" id="busca" type="search" placeholder="{ph}" aria-label="{ph}"></div>'
              f'<div class="grid" id="grade-noticias">{cards}</div><p class="vazio">{empty}</p>'), UI[lang]["meta"]


def pg_reviews(lang, p):
    i = L.index(lang)
    t = TITLES["noticias-reviews"][i]
    d = ("Análises detalhadas de jogos, filmes, séries e muito mais, para você escolher o que vale seu tempo." if lang == "pt"
         else "Detailed reviews of games, movies, series and more, to help you pick what's worth your time.")
    return titulo(t, d) + '<div class="grid">' + "".join(card(p, r[0], r[1 + 2 * i], r[2 + 2 * i], tag="h2") for r in REVIEWS) + "</div>", d


def pg_lanc(lang, p):
    i = L.index(lang)
    d = LANC["d"][i]
    out = titulo(TITLES["noticias-lancamentos"][i], d)
    for h, items in zip(LANC["h"], (LANC["rel"], LANC["ev"])):
        out += f'<h2 class="subtitulo">{h[i]}</h2><div class="grid">' + "".join(
            card(p, c[1], f"{c[0]} {c[2 + 2 * i]}", c[3 + 2 * i], tag="h3") for c in items) + "</div>"
    return out, d


def pg_cats(lang, p):
    i = L.index(lang)
    d = "Escolha uma categoria para ver destaques, gêneros populares e novidades." if lang == "pt" else "Pick a category to see highlights, popular genres and news."
    cs = "".join(f'<a class="card cat rev" href="{c[0]}.html"><span class="icone" aria-hidden="true">{c[1]}</span><h2>{c[2 + i]}</h2><p>{c[4 + i]}</p></a>' for c in CATS)
    return titulo("Mapa de Categorias" if lang == "pt" else "Category Map", d) + f'<div class="mapa">{cs}</div>', d


def pg_curio(lang, p):
    i = L.index(lang)
    d = "Fatos incríveis e curiosos sobre o universo geek." if lang == "pt" else "Amazing and fun facts about the geek universe."
    nav = "".join(f'<a class="chip" href="#{c[0]}">{c[1][i]}</a>' for c in CURIO)
    secs = ""
    for cid, nome, items in CURIO:
        cs = "".join(card(p, it[0], it[1 + i], it[3 + i]).replace('class="card rev"', 'class="card curio rev"') for it in items)
        secs += f'<section id="{cid}" class="secao"><h2 class="subtitulo">{nome[i]}</h2><div class="grid">{cs}</div></section>'
    return titulo(TITLES["curiosidades"][i], d) + f'<nav class="nav-secoes" aria-label="Seções">{nav}</nav>{secs}', d


def pg_contato(lang, p):
    i = L.index(lang)
    t = ("Entre em contato", "Get in touch")[i]
    d = ("Tem sugestão, parceria ou quer falar com a equipe do Night Level? Envie sua mensagem." if lang == "pt"
         else "Have a suggestion, partnership idea, or want to talk to the Night Level team? Send a message.")
    f = [("Nome", "Name"), ("E-mail", "Email"), ("Mensagem", "Message")]
    btn = ("Enviar mensagem", "Send message")[i]
    form = (f'<form class="form rev" data-form="contato" novalidate><h1>📬 {t}</h1><p>{d}</p>' + field("nome", f[0][i], ac="name") + field("email", f[1][i], "email", ac="email")
            + field("mensagem", f[2][i], area=True) + '<p class="contador">0/500</p>' + f'<button class="btn" type="submit">{btn}</button></form>')
    mapa = f'<div class="mapa-local rev"><iframe src="{MAP}" title="{"Localização" if lang == "pt" else "Location"} - ETEC São Paulo Luz" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>'
    return f'<div class="contato-grid">{form}{mapa}</div>', d


def auth_top(lang, key):
    other = ("en/" + key + ".html") if lang == "pt" else ("../" + key + ".html")
    return f'<div class="topo-auth"><a href="index.html">{UI[lang]["home"]}</a><a href="{other}">{UI[lang]["other"]}</a></div>'


def pg_login(lang, p):
    i = L.index(lang)
    body = (f'<div class="auth-card"><a href="index.html"><h1>Night Level</h1></a><p class="sub">{("Entre para continuar", "Sign in to continue")[i]}</p>'
            f'<form data-form="login" novalidate>' + field("email", "Email" if lang == "en" else "E-mail", "email", ("Digite seu e-mail", "Enter your email")[i], ac="email")
            + field("password", ("Senha", "Password")[i], "password", ("Digite sua senha", "Enter your password")[i], pw=True, ac="current-password")
            + f'<button class="btn" type="submit">{("Entrar", "Sign in")[i]}</button></form>'
              f'<div class="links"><a href="contato.html">{("Esqueceu a senha?", "Forgot your password?")[i]}</a><a href="registro.html">{("Criar conta", "Create account")[i]}</a></div></div>')
    return auth_top(lang, "login") + body


def pg_registro(lang, p):
    i = L.index(lang)
    body = (f'<div class="auth-card"><a href="index.html"><h1>Night Level</h1></a><p class="sub">{("Crie sua conta", "Create your account")[i]}</p>'
            f'<form data-form="registro" novalidate>' + field("nome", ("Nome completo", "Full name")[i], ph=("Digite seu nome", "Enter your full name")[i], ac="name")
            + field("email", "Email" if lang == "en" else "E-mail", "email", ("Digite seu e-mail", "Enter your email")[i], ac="email")
            + field("senha", ("Senha", "Password")[i], "password", ("Crie uma senha", "Create a password")[i], pw=True, ac="new-password")
            + '<div class="forca"><i></i></div><p class="forca-txt"></p>'
            + field("confirmar", ("Confirmar senha", "Confirm password")[i], "password", ("Repita sua senha", "Repeat your password")[i], pw=True, ac="new-password")
            + f'<button class="btn" type="submit">{("Criar conta", "Create account")[i]}</button></form>'
              f'<div class="links"><span>{("Já tem conta?", "Already have an account?")[i]}</span><a href="login.html">{("Entrar", "Sign in")[i]}</a></div></div>')
    return auth_top(lang, "registro") + body


def pg_category(key):
    def build(lang, p):
        i = L.index(lang)
        if key == "jogos":
            c = JOGOS
            out = titulo(c["t"][i], c["d"][i]) + (f'<div class="video-box rev"><iframe src="https://www.youtube.com/embed/IpSDW3Mq-7E" title="{esc(c["vt"][i])}" loading="lazy" '
                  f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>'
                  f'<p class="video-texto">{esc(c["vx"][i])}</p><h2 class="subtitulo">{c["ch"][i]}</h2>')
            return out + '<div class="cards">' + "".join(card(p, x[0], x[1 + 2 * 0 + i], x[3 + i]) for x in c["cards"]) + "</div>", c["d"][i]
        c = PAGES_CAT[key]
        th = c["th"][i]
        rows = "".join(f'<tr><td>{esc(r[i])}</td><td><div class="medidor"><span class="barra"><i style="--n:{r[2] * 20}%"></i></span>{LEVEL[lang][r[2]]}</div></td><td>{esc(r[3 + i])}</td></tr>'
                       for r in sorted(c["rows"], key=lambda r: -r[2]))
        out = titulo(c["t"][i], c["d"][i]) + f'<div class="banner rev">{img(p, c["banner"], c["t"][i])}</div>'
        out += (f'<h2 class="subtitulo">🍿 {c["ts"][i]}</h2><div class="tabela-wrap rev"><table><thead><tr><th>{th[0]}</th><th>{th[1]}</th><th>{th[2]}</th></tr></thead><tbody>{rows}</tbody></table></div>'
                f'<h2 class="subtitulo">{c["ch"][i]}</h2><div class="cards">' + "".join(card(p, x[0], x[1 + i], x[3 + i]) for x in c["cards"]) + "</div>")
        return out, c["d"][i]
    return build


BUILDERS = {"index": pg_index, "noticias-ultimas": pg_news, "noticias-reviews": pg_reviews, "noticias-lancamentos": pg_lanc,
            "categorias": pg_cats, "curiosidades": pg_curio, "contato": pg_contato}
BUILDERS.update({k: pg_category(k) for k in ("jogos", "filmes", "series", "animes", "livros", "mangas")})


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    for lang in L:
        p = "" if lang == "pt" else "../"
        outdir = ROOT if lang == "pt" else os.path.join(ROOT, "en")
        for key, (tpt, ten) in TITLES.items():
            title = (tpt, ten)[L.index(lang)]
            if key in ("login", "registro"):
                body = (pg_login if key == "login" else pg_registro)(lang, p)
                html = head(L.index(lang), lang, key, title, UI[lang]["meta"], p, auth=True) + body + f'\n<script src="{p}js/main.js"></script>\n</body>\n</html>\n'
            else:
                body, desc = BUILDERS[key](lang, p)
                html = head(L.index(lang), lang, key, title, desc, p) + header(lang, key, p) + body + footer(lang, p)
            write(os.path.join(outdir, key + ".html"), html)
    print("Páginas geradas:", len(TITLES) * 2)


if __name__ == "__main__":
    main()
