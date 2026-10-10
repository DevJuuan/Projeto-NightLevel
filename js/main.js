/* Night Level — interações e efeitos */
(() => {
  "use strict";
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const en = document.documentElement.lang === "en";
  const t = (pt, ing) => (en ? ing : pt);
  const reduz = matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- imagens que falham não quebram o layout ---------- */
  $$("img").forEach((img) => {
    const falhou = () => {
      if (img.closest(".banner")) return img.closest(".banner").remove();
      if (img.classList.contains("hero-bg") || img.closest(".idioma")) return img.remove();
      if (img.classList.contains("logo") || img.classList.contains("logo-rodape")) return;
      const box = document.createElement("div");
      box.className = "img-falha";
      box.textContent = img.alt || "Night Level";
      img.replaceWith(box);
    };
    img.addEventListener("error", falhou, { once: true });
    if (img.complete && img.naturalWidth === 0) falhou();
  });

  /* ---------- toast ---------- */
  const toastEl = document.createElement("div");
  toastEl.id = "toast";
  toastEl.setAttribute("role", "status");
  document.body.append(toastEl);
  let toastTimer;
  const toast = (msg, erro = false) => {
    toastEl.textContent = msg;
    toastEl.classList.toggle("erro", erro);
    toastEl.classList.add("visivel");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toastEl.classList.remove("visivel"), 3800);
  };

  /* ---------- menu: mobile + dropdown ---------- */
  const menu = $("#menu"), burger = $(".hamburguer");
  if (menu && burger) {
    burger.addEventListener("click", () => {
      const aberto = menu.classList.toggle("aberto");
      burger.setAttribute("aria-expanded", aberto);
    });
    $$("a", menu).forEach((a) => a.addEventListener("click", () => {
      menu.classList.remove("aberto");
      burger.setAttribute("aria-expanded", "false");
    }));
  }
  $$(".dropdown").forEach((dd) => {
    const btn = $(".dd-btn", dd);
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      const aberto = dd.classList.toggle("aberto");
      btn.setAttribute("aria-expanded", aberto);
    });
  });
  document.addEventListener("click", () => $$(".dropdown.aberto").forEach((d) => { d.classList.remove("aberto"); $(".dd-btn", d).setAttribute("aria-expanded", "false"); }));
  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    $$(".dropdown.aberto").forEach((d) => d.classList.remove("aberto"));
    menu && menu.classList.remove("aberto");
    burger && burger.setAttribute("aria-expanded", "false");
  });

  /* ---------- rolagem: barra de XP, cabeçalho compacto, botão de topo ---------- */
  const xp = $("#xp"), cab = $(".cabecalho"), topo = $("#topo");
  const aoRolar = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    const p = max > 0 ? scrollY / max : 0;
    if (xp) xp.style.width = p * 100 + "%";
    if (cab) cab.classList.toggle("compacto", scrollY > 40);
    if (topo) {
      topo.classList.toggle("visivel", scrollY > 500);
      $("b", topo).textContent = 1 + Math.floor(p * 9.99);
    }
    const bg = $(".hero-bg");
    if (bg && !reduz) bg.style.transform = `translateY(${scrollY * 0.12}px) scale(1.08)`;
  };
  addEventListener("scroll", aoRolar, { passive: true });
  aoRolar();
  if (topo) topo.addEventListener("click", () => scrollTo({ top: 0, behavior: reduz ? "auto" : "smooth" }));

  /* ---------- revelar ao entrar na tela ---------- */
  const io = new IntersectionObserver((es) => es.forEach((e) => {
    if (e.isIntersecting) { e.target.classList.add("revelado"); io.unobserve(e.target); }
  }), { threshold: 0.12 });
  $$(".rev").forEach((el, i) => {
    el.style.setProperty("--d", (i % 4) * 0.08 + "s");
    io.observe(el);
  });

  /* ---------- cards: inclinação 3D e brilho que segue o mouse ---------- */
  if (!reduz && matchMedia("(hover: hover)").matches) {
    $$(".card").forEach((c) => {
      c.addEventListener("pointermove", (e) => {
        const r = c.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
        c.style.setProperty("--mx", x * 100 + "%");
        c.style.setProperty("--my", y * 100 + "%");
        c.style.transform = `perspective(800px) rotateX(${(0.5 - y) * 7}deg) rotateY(${(x - 0.5) * 9}deg) translateY(-4px)`;
      });
      c.addEventListener("pointerleave", () => (c.style.transform = ""));
    });
  }

  /* ---------- estrelas no fundo ---------- */
  const cv = $("#estrelas");
  if (cv && !reduz) {
    const ctx = cv.getContext("2d");
    let w, h, pts = [], raf;
    const iniciar = () => {
      w = cv.width = innerWidth; h = cv.height = innerHeight;
      const n = Math.min(90, Math.floor((w * h) / 20000));
      pts = Array.from({ length: n }, () => ({
        x: Math.random() * w, y: Math.random() * h, r: Math.random() * 1.4 + 0.3,
        v: Math.random() * 0.25 + 0.05, c: Math.random() > 0.6 ? "0,240,255" : "181,123,255", f: Math.random() * 6.28,
      }));
    };
    const desenhar = (ms) => {
      ctx.clearRect(0, 0, w, h);
      pts.forEach((p) => {
        p.y -= p.v; if (p.y < -4) { p.y = h + 4; p.x = Math.random() * w; }
        ctx.fillStyle = `rgba(${p.c},${0.35 + 0.35 * Math.sin(ms / 800 + p.f)})`;
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, 6.28); ctx.fill();
      });
      raf = requestAnimationFrame(desenhar);
    };
    iniciar(); raf = requestAnimationFrame(desenhar);
    addEventListener("resize", iniciar);
    document.addEventListener("visibilitychange", () => {
      cancelAnimationFrame(raf);
      if (!document.hidden) raf = requestAnimationFrame(desenhar);
    });
  }

  /* ---------- efeito de digitação (hero) ---------- */
  const dig = $(".digitando");
  if (dig) {
    const frases = dig.dataset.frases.split("|");
    if (reduz) dig.textContent = frases[0];
    else {
      let f = 0, i = 0, apagando = false;
      const passo = () => {
        const frase = frases[f];
        dig.textContent = frase.slice(0, i);
        if (!apagando && i === frase.length) { apagando = true; return setTimeout(passo, 1800); }
        if (apagando && i === 0) { apagando = false; f = (f + 1) % frases.length; }
        i += apagando ? -1 : 1;
        setTimeout(passo, apagando ? 28 : 65);
      };
      passo();
    }
  }

  /* ---------- contadores animados ---------- */
  const cont = new IntersectionObserver((es) => es.forEach((e) => {
    if (!e.isIntersecting) return;
    cont.unobserve(e.target);
    const alvo = +e.target.dataset.count, ini = performance.now();
    const rodar = (ms) => {
      const k = Math.min((ms - ini) / 1200, 1);
      e.target.textContent = Math.round(alvo * (1 - Math.pow(1 - k, 3)));
      if (k < 1) requestAnimationFrame(rodar);
    };
    reduz ? (e.target.textContent = alvo) : requestAnimationFrame(rodar);
  }), { threshold: 0.6 });
  $$("[data-count]").forEach((el) => cont.observe(el));

  /* ---------- notícias: filtro + busca + "ler mais" ---------- */
  const grade = $("#grade-noticias");
  if (grade) {
    const cards = $$(".card", grade), chips = $$(".chip[data-filtro]"), busca = $("#busca"), vazio = $(".vazio");
    let filtro = (location.hash || "#todos").slice(1);
    if (!chips.some((c) => c.dataset.filtro === filtro)) filtro = "todos";
    const aplicar = () => {
      const q = busca ? busca.value.trim().toLowerCase() : "";
      let n = 0;
      cards.forEach((c) => {
        const ok = (filtro === "todos" || c.dataset.categoria === filtro) && c.textContent.toLowerCase().includes(q);
        const estavaOculto = c.classList.contains("oculto");
        c.classList.toggle("oculto", !ok);
        if (ok) { n++; c.classList.add("revelado"); if (estavaOculto) { c.classList.remove("entrando"); void c.offsetWidth; c.classList.add("entrando"); } }
      });
      chips.forEach((c) => c.setAttribute("aria-pressed", c.dataset.filtro === filtro));
      vazio.classList.toggle("visivel", n === 0);
    };
    chips.forEach((c) => c.addEventListener("click", () => { filtro = c.dataset.filtro; history.replaceState(null, "", "#" + filtro); aplicar(); }));
    busca && busca.addEventListener("input", aplicar);
    $$(".btn-ler", grade).forEach((b) => b.addEventListener("click", () => {
      const card = b.closest(".card"), aberto = card.classList.toggle("aberto");
      b.textContent = aberto ? t("Mostrar menos", "Show less") : t("Ler mais", "Read more");
      b.setAttribute("aria-expanded", aberto);
    }));
    aplicar();
  }

  /* ---------- curiosidades: destaque da seção atual ---------- */
  const links = $$(".nav-secoes a");
  if (links.length) {
    const spy = new IntersectionObserver((es) => es.forEach((e) => {
      if (e.isIntersecting) links.forEach((a) => a.classList.toggle("ativo", a.getAttribute("href") === "#" + e.target.id));
    }), { rootMargin: "-35% 0px -60% 0px" });
    $$(".secao").forEach((s) => spy.observe(s));
  }

  /* ---------- formulários ---------- */
  const emailOk = (v) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v);
  const marcar = (campo, erro) => {
    campo.classList.toggle("erro", !!erro);
    campo.classList.toggle("ok", !erro);
    const m = $(".msg-erro", campo); if (m) m.textContent = erro || "";
    return !erro;
  };
  const regras = {
    nome: (v) => (v.trim().length < 3 ? t("Digite seu nome (mínimo 3 letras).", "Enter your name (at least 3 letters).") : ""),
    email: (v) => (emailOk(v.trim()) ? "" : t("Use um e-mail válido, como nome@site.com.", "Use a valid email, like name@site.com.")),
    mensagem: (v) => (v.trim().length < 10 ? t("Escreva pelo menos 10 caracteres.", "Write at least 10 characters.") : ""),
    senha: (v) => (v.length < 8 ? t("A senha precisa ter 8 caracteres ou mais.", "Password must be 8 characters or more.") : ""),
    confirmar: (v, f) => (v !== $("#senha", f).value ? t("As senhas não são iguais.", "Passwords do not match.") : ""),
    password: (v) => (v ? "" : t("Digite sua senha.", "Enter your password.")),
  };
  $$("form[data-form]").forEach((f) => {
    const campos = $$(".campo", f);
    const checar = (c) => {
      const i = $("input,textarea", c), r = regras[i.id];
      return r ? marcar(c, r(i.value, f)) : true;
    };
    campos.forEach((c) => {
      const i = $("input,textarea", c);
      i.addEventListener("blur", () => checar(c));
      i.addEventListener("input", () => { if (c.classList.contains("erro")) checar(c); });
    });
    $$(".ver-senha", f).forEach((b) => b.addEventListener("click", () => {
      const i = $("input", b.parentElement), mostrar = i.type === "password";
      i.type = mostrar ? "text" : "password";
      b.textContent = mostrar ? "🙈" : "👁️";
    }));
    const senha = $("#senha", f), barra = $(".forca i", f), txt = $(".forca-txt", f);
    if (senha && barra) senha.addEventListener("input", () => {
      const v = senha.value;
      const pts = [v.length >= 8, /[A-Z]/.test(v), /[0-9]/.test(v), /[^A-Za-z0-9]/.test(v), v.length >= 12].filter(Boolean).length;
      const nomes = en ? ["Very weak", "Weak", "Fair", "Good", "Strong", "Excellent"] : ["Muito fraca", "Fraca", "Razoável", "Boa", "Forte", "Excelente"];
      barra.style.width = pts * 20 + "%";
      barra.style.background = ["#ff5d73", "#ff5d73", "#ffb020", "#c8d94a", "#3ddc97", "#00f0ff"][pts];
      txt.textContent = v ? t("Força da senha: ", "Password strength: ") + nomes[pts] : "";
    });
    const msg = $("textarea", f), cnt = $(".contador", f);
    if (msg && cnt) msg.addEventListener("input", () => (cnt.textContent = `${msg.value.length}/500`));
    f.addEventListener("submit", (e) => {
      e.preventDefault();
      const validos = campos.map(checar);
      if (validos.includes(false)) {
        const primeiro = $(".campo.erro input, .campo.erro textarea", f);
        primeiro && primeiro.focus();
        return toast(t("Corrija os campos destacados.", "Fix the highlighted fields."), true);
      }
      const tipo = f.dataset.form;
      toast({
        contato: t("Mensagem enviada! Responderemos em breve.", "Message sent! We'll reply soon."),
        login: t("Login realizado. Bem-vindo de volta!", "Signed in. Welcome back!"),
        registro: t("Conta criada! Agora é só entrar.", "Account created! You can sign in now."),
      }[tipo]);
      f.reset();
      campos.forEach((c) => c.classList.remove("ok", "erro"));
      if (barra) { barra.style.width = 0; txt.textContent = ""; }
      if (cnt) cnt.textContent = "0/500";
      if (tipo === "registro") setTimeout(() => (location.href = "login.html"), 1600);
    });
  });

  /* ---------- ano do rodapé ---------- */
  $$("[data-ano]").forEach((el) => (el.textContent = new Date().getFullYear()));
})();
