/* ============================================================
   MOBILE NAV — the hamburger.

   Below 520px the desktop .tb-nav is hidden, which left no way to reach
   Ad concepts or the landing pages on a phone at all. This adds the burger
   and the drawer.

   It BUILDS the drawer from the .tb-nav that's already in the page, plus the
   phone link and the CTA button. Nothing is hard-coded here, so the menu can
   never drift out of sync with the desktop nav — add a link to .tb-nav in the
   HTML and it appears in the drawer too.

   Loaded on all five pages. The landing pages don't load sabre.js, so this
   deliberately lives in its own file rather than inside it.
   ============================================================ */
(function () {
  'use strict';

  var bar = document.querySelector('.topbar');
  if (!bar) return;
  var nav = bar.querySelector('.tb-nav');
  if (!nav) return;

  /* ---------- burger button ---------- */
  var burger = document.createElement('button');
  burger.className = 'tb-burger';
  burger.type = 'button';
  burger.setAttribute('aria-label', 'Menu');
  burger.setAttribute('aria-expanded', 'false');
  burger.innerHTML = '<i></i><i></i><i></i>';

  var right = bar.querySelector('.tb-right') || bar;
  right.appendChild(burger);

  /* ---------- drawer, built from what's already on the page ---------- */
  var drawer = document.createElement('div');
  drawer.className = 'navdrawer';
  drawer.id = 'navdrawer';
  burger.setAttribute('aria-controls', 'navdrawer');

  var links = document.createElement('nav');
  links.className = 'nd-links';
  Array.prototype.forEach.call(nav.querySelectorAll('a'), function (a) {
    var c = document.createElement('a');
    c.href = a.getAttribute('href');
    c.textContent = a.textContent.trim();
    if (a.classList.contains('active')) c.className = 'on';
    links.appendChild(c);
  });
  drawer.appendChild(links);

  var foot = document.createElement('div');
  foot.className = 'nd-foot';
  var phone = bar.querySelector('.tb-phone');
  if (phone) {
    foot.innerHTML =
      '<a class="nd-phone" href="' + phone.getAttribute('href') + '">' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round">' +
        '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.4 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.4 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg>' +
        '07 3823 3200</a>';
  }
  var cta = bar.querySelector('.tb-right .btn');
  if (cta) {
    var b = document.createElement('a');
    b.className = 'btn nd-cta';
    b.href = cta.getAttribute('href');
    b.textContent = cta.textContent.trim();
    foot.appendChild(b);
  }
  drawer.appendChild(foot);
  bar.appendChild(drawer);

  /* ---------- open / close ---------- */
  function setOpen(on) {
    bar.classList.toggle('menu-open', on);
    burger.setAttribute('aria-expanded', on ? 'true' : 'false');
    document.body.classList.toggle('nav-lock', on);
  }
  function close() { setOpen(false); }

  burger.addEventListener('click', function (e) {
    e.stopPropagation();
    setOpen(!bar.classList.contains('menu-open'));
  });

  // any link closes it — including same-page anchors, which otherwise leave
  // the drawer sitting over the thing you just jumped to
  drawer.addEventListener('click', function (e) {
    if (e.target.closest('a')) close();
  });

  document.addEventListener('click', function (e) {
    if (bar.classList.contains('menu-open') && !bar.contains(e.target)) close();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') close();
  });
  window.addEventListener('resize', function () {
    if (window.innerWidth > 520) close();
  });
})();
