/* Sabre Constructions LP — motion + interaction
   Scroll-reveal system copied from the BBL site pattern (IntersectionObserver
   + `?still` escape hatch for full-page screenshots), extended with pop/slide
   variants, count-up numbers, a drag before/after slider and an FAQ accordion. */
(function () {
  'use strict';

  var STILL = location.search.indexOf('still') > -1;
  var REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- year ---------- */
  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---------- scroll reveal ---------- */
  var animated = document.querySelectorAll('.reveal, .pop, .slide-l, .slide-r, .zoom');

  function showAll() {
    Array.prototype.forEach.call(animated, function (el) { el.classList.add('in'); });
  }

  if (STILL || REDUCED || !('IntersectionObserver' in window)) {
    showAll();
    if (STILL) {
      var s = document.createElement('style');
      s.textContent = '.hero{min-height:auto!important;padding-top:40px}';
      document.head.appendChild(s);
    }
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        io.unobserve(e.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    Array.prototype.forEach.call(animated, function (el) { io.observe(el); });
  }

  /* ---------- sticky bar appears after the hero ---------- */
  var topbar = document.getElementById('topbar');
  var hero = document.querySelector('.hero');
  if (topbar && hero) {
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) {
        topbar.classList.toggle('show', !es[0].isIntersecting);
      }, { threshold: 0, rootMargin: '-70% 0px 0px 0px' }).observe(hero);
    } else {
      topbar.classList.add('show');
    }
  }

  /* ---------- count-up numbers ---------- */
  function countUp(el) {
    var target = parseInt(el.dataset.count, 10);
    var suffix = el.dataset.suffix || '';
    if (isNaN(target)) return;
    if (REDUCED || STILL) { el.textContent = target + suffix; return; }
    var start = null;
    var dur = 1200;
    function tick(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  var counters = document.querySelectorAll('[data-count]');
  if (counters.length) {
    if (STILL || REDUCED || !('IntersectionObserver' in window)) {
      Array.prototype.forEach.call(counters, countUp);
    } else {
      var cio = new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (!e.isIntersecting) return;
          countUp(e.target);
          cio.unobserve(e.target);
        });
      }, { threshold: 0.6 });
      Array.prototype.forEach.call(counters, function (el) { cio.observe(el); });
    }
  }

  /* ---------- click-to-play videos (testimonials, concept clips) ---------- */
  Array.prototype.forEach.call(document.querySelectorAll('.vwrap'), function (wrap) {
    var vid = wrap.querySelector('video');
    var btn = wrap.querySelector('.vplay');
    if (!vid || !btn) return;

    btn.addEventListener('click', function () {
      // only one testimonial talking at a time
      Array.prototype.forEach.call(document.querySelectorAll('.vwrap video'), function (other) {
        if (other !== vid) { other.pause(); other.parentNode.classList.remove('playing'); }
      });
      wrap.classList.add('playing');
      vid.controls = true;
      var p = vid.play();
      if (p && p.catch) p.catch(function () { wrap.classList.remove('playing'); });
    });

    vid.addEventListener('pause', function () { wrap.classList.remove('playing'); });
    vid.addEventListener('ended', function () {
      wrap.classList.remove('playing');
      vid.controls = false;
      vid.currentTime = 0;
    });
  });

  /* ---------- testimonial carousel ---------- */
  var carousel = document.getElementById('carousel');
  if (carousel) {
    var track = carousel.querySelector('.car-track');
    var slides = carousel.querySelectorAll('.car-slide');
    var dotWrap = carousel.querySelector('.car-dots');
    var index = 0;

    function pauseAll() {
      Array.prototype.forEach.call(carousel.querySelectorAll('video'), function (v) {
        v.pause();
        v.parentNode.classList.remove('playing');
      });
    }

    function go(i) {
      index = (i + slides.length) % slides.length;
      pauseAll();                                   // don't leave audio playing off-screen

      // Peek layout: each slide is SLIDE_W% wide, so centring slide i means
      // shifting the track by (50 - SLIDE_W/2) - i*SLIDE_W.
      var slideW = parseFloat(getComputedStyle(slides[0]).flexBasis);
      if (isNaN(slideW)) slideW = 68;
      var offset = (50 - slideW / 2) - index * slideW;
      track.style.transform = 'translateX(' + offset + '%)';

      Array.prototype.forEach.call(slides, function (s, n) {
        s.classList.toggle('active', n === index);
      });
      Array.prototype.forEach.call(dotWrap.children, function (d, n) {
        d.classList.toggle('on', n === index);
      });
    }

    Array.prototype.forEach.call(slides, function (s, n) {
      var d = document.createElement('button');
      d.type = 'button';
      d.setAttribute('aria-label', 'Testimonial ' + (n + 1));
      d.addEventListener('click', function () { go(n); });
      dotWrap.appendChild(d);
    });

    carousel.querySelector('.prev').addEventListener('click', function () { go(index - 1); });
    carousel.querySelector('.next').addEventListener('click', function () { go(index + 1); });

    // swipe
    var x0 = null;
    carousel.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    carousel.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 45) go(index + (dx < 0 ? 1 : -1));
      x0 = null;
    });

    // clicking a neighbouring slide brings it to the middle
    Array.prototype.forEach.call(slides, function (s, n) {
      s.addEventListener('click', function () {
        if (n !== index) go(n);
      }, true);
    });

    go(0);
    window.addEventListener('resize', function () { go(index); });
  }

  /* ---------- gallery lightbox ---------- */
  var lb = document.getElementById('lightbox');
  var gallery = document.getElementById('gallery');
  if (lb && gallery) {
    var tiles = gallery.querySelectorAll('.tile');
    var lbImg = document.getElementById('lbImg');
    var lbTitle = document.getElementById('lbTitle');
    var lbSub = document.getElementById('lbSub');
    var at = 0;

    function show(i) {
      at = (i + tiles.length) % tiles.length;
      var t = tiles[at];
      lbImg.src = t.dataset.full;
      lbImg.alt = t.querySelector('img').alt;
      lbTitle.textContent = t.dataset.title;
      lbSub.textContent = t.dataset.sub;
    }

    function open(i) {
      show(i);
      lb.classList.add('open');
      document.body.classList.add('lb-lock');
    }

    function close() {
      lb.classList.remove('open');
      document.body.classList.remove('lb-lock');
      lbImg.removeAttribute('src');   // '' would resolve to the page URL
    }

    Array.prototype.forEach.call(tiles, function (t, i) {
      t.addEventListener('click', function () { open(i); });
    });

    lb.querySelector('.lb-close').addEventListener('click', close);
    lb.querySelector('.lb-prev').addEventListener('click', function (e) { e.stopPropagation(); show(at - 1); });
    lb.querySelector('.lb-next').addEventListener('click', function (e) { e.stopPropagation(); show(at + 1); });

    // click the backdrop (but not the image or a button) to close
    lb.addEventListener('click', function (e) {
      if (e.target === lb) close();
    });

    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowLeft') show(at - 1);
      else if (e.key === 'ArrowRight') show(at + 1);
    });

    // swipe between images on touch
    var lx = null;
    lb.addEventListener('touchstart', function (e) { lx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) {
      if (lx === null) return;
      var dx = e.changedTouches[0].clientX - lx;
      if (Math.abs(dx) > 45) show(at + (dx < 0 ? 1 : -1));
      lx = null;
    });
  }

  /* ---------- replay the reveal video ---------- */
  var replay = document.getElementById('replayBtn');
  var vid = document.getElementById('revealVid');
  if (replay && vid) {
    replay.addEventListener('click', function () {
      vid.currentTime = 0;
      var p = vid.play();
      if (p && p.catch) p.catch(function () {});
    });
  }

  /* ---------- FAQ accordion ---------- */
  Array.prototype.forEach.call(document.querySelectorAll('.fq'), function (fq) {
    var btn = fq.querySelector('button');
    var ans = fq.querySelector('.a');
    if (!btn || !ans) return;
    btn.addEventListener('click', function () {
      var open = fq.classList.toggle('open');
      ans.style.maxHeight = open ? ans.scrollHeight + 'px' : '0px';
    });
  });

  /* ---------- form ---------- */
  var form = document.getElementById('sabreForm');
  if (form) {
    var errEl = form.querySelector('[data-form-error]');
    var successEl = document.getElementById('formSuccess');
    var renderedAt = Date.now();

    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (errEl) errEl.style.display = 'none';
      if (!form.checkValidity()) { form.reportValidity(); return; }

      // honeypot — bots fill hidden fields
      if (form.querySelector('input[name="website"]').value) return;

      var btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }

      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      data.submitted_at = new Date().toISOString();
      data.fill_seconds = Math.round((Date.now() - renderedAt) / 1000);
      data.landing_page = window.location.href;
      data.referrer = document.referrer || '';

      function done() {
        form.style.display = 'none';
        if (successEl) successEl.classList.add('show');
      }

      var webhook = form.dataset.webhookUrl;
      if (!webhook) {
        // No endpoint wired yet — the page is being shown as a demo.
        console.warn('[sabre] No data-webhook-url set on #sabreForm — this submission was NOT sent anywhere.', data);
        done();
        return;
      }

      fetch(webhook, {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'text/plain' },
        body: JSON.stringify(data)
      })
        .then(done)
        .catch(function (err) {
          console.error('[sabre] submit failed:', err);
          if (errEl) errEl.style.display = 'block';
          if (btn) { btn.disabled = false; btn.textContent = 'Book my site visit'; }
        });
    });
  }
})();
