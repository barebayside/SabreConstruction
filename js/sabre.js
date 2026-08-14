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

  /* ---------- before / after drag slider ---------- */
  var ba = document.getElementById('ba');
  if (ba) {
    var dragging = false;

    function setPos(clientX) {
      var r = ba.getBoundingClientRect();
      var pct = ((clientX - r.left) / r.width) * 100;
      pct = Math.max(2, Math.min(98, pct));
      ba.style.setProperty('--pos', pct + '%');
    }

    ba.addEventListener('pointerdown', function (e) {
      dragging = true;
      ba.setPointerCapture(e.pointerId);
      setPos(e.clientX);
    });
    ba.addEventListener('pointermove', function (e) {
      if (dragging) setPos(e.clientX);
    });
    ['pointerup', 'pointercancel'].forEach(function (ev) {
      ba.addEventListener(ev, function () { dragging = false; });
    });

    // nudge it open once it scrolls into view, so people see it's draggable
    if (!STILL && !REDUCED && 'IntersectionObserver' in window) {
      new IntersectionObserver(function (es, obs) {
        if (!es[0].isIntersecting) return;
        obs.disconnect();
        var from = 50, to = 22, t0 = null;
        function sweep(ts) {
          if (t0 === null) t0 = ts;
          var p = Math.min((ts - t0) / 900, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          ba.style.setProperty('--pos', (from + (to - from) * eased) + '%');
          if (p < 1) requestAnimationFrame(sweep);
        }
        setTimeout(function () { requestAnimationFrame(sweep); }, 350);
      }, { threshold: 0.45 }).observe(ba);
    }
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
