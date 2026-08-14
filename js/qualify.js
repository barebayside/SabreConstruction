/* ============================================================
   QUALIFYING POPUP — five questions, one per screen.
   Shared by all three ad landing pages.

   Five fields in one screen would cost 10–25% of completions, so this is a
   multi-step with a progress bar instead: easy first, phone number last,
   and only two of the five need typing. Everything else is a tap target.

   Leads go out through a form relay (no server on GitHub Pages).
   Change LEAD_EMAIL and nothing else.
   ============================================================ */
(function () {
  'use strict';

  var LEAD_EMAIL = 'edasturner@gmail.com';   // → admin@sabreconstructions.com.au when live
  var RELAY = 'https://formsubmit.co/ajax/' + LEAD_EMAIL;

  var STEPS = [
    {
      key: 'project_type',
      q: 'What are you looking to do?',
      hint: 'Pick the closest one.',
      type: 'choice',
      options: ['Knockdown rebuild', 'House raise', 'Renovation or bathroom reno', 'Not sure yet']
    },
    {
      key: 'has_plans',
      q: 'Do you have plans drawn?',
      hint: 'Either way is fine — it just tells us where to start.',
      type: 'choice',
      options: ['Yes, plans are done', 'Started, not finished', 'No, not yet']
    },
    {
      key: 'suburb',
      q: "Where's the block?",
      hint: 'Suburb is enough.',
      type: 'text',
      placeholder: 'e.g. Thornlands',
      inputmode: 'text',
      autocomplete: 'address-level2'
    },
    {
      key: 'budget',
      q: 'Roughly what budget are you working to?',
      hint: "A ballpark is fine. It stops us wasting your time.",
      type: 'choice',
      // ⚠️ PLACEHOLDER BANDS — confirm against Sabre's actual job sizes
      options: ['Under $300k', '$300k – $450k', '$450k – $650k', '$650k+', 'Still working it out']
    },
    {
      key: 'mobile',
      q: 'Best mobile to reach you on?',
      hint: "Stewart will ring you — we won't add you to anything.",
      type: 'text',
      placeholder: '04__ ___ ___',
      inputmode: 'tel',
      autocomplete: 'tel',
      validate: function (v) { return v.replace(/\D/g, '').length >= 8; },
      error: 'That looks a bit short — check the number?'
    }
  ];

  var answers = {};
  var at = 0;
  var openedAt = 0;
  var modal, body, bar, backBtn, root;

  function build() {
    root = document.createElement('div');
    root.className = 'qm';
    root.innerHTML =
      '<div class="qm-sheet" role="dialog" aria-modal="true" aria-label="Book a site visit">' +
        '<div class="qm-top">' +
          '<button class="qm-back" type="button" aria-label="Back">' +
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>' +
          '</button>' +
          '<div class="qm-bar"><i></i></div>' +
          '<button class="qm-close" type="button" aria-label="Close">' +
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>' +
          '</button>' +
        '</div>' +
        '<div class="qm-body"></div>' +
      '</div>';
    document.body.appendChild(root);

    modal = root.querySelector('.qm-sheet');
    body = root.querySelector('.qm-body');
    bar = root.querySelector('.qm-bar i');
    backBtn = root.querySelector('.qm-back');

    root.addEventListener('click', function (e) { if (e.target === root) close(); });
    root.querySelector('.qm-close').addEventListener('click', close);
    backBtn.addEventListener('click', function () { if (at > 0) render(at - 1); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && root.classList.contains('open')) close();
    });
  }

  function render(i) {
    at = i;
    var s = STEPS[i];
    bar.style.width = ((i) / STEPS.length * 100) + '%';
    backBtn.style.visibility = i === 0 ? 'hidden' : 'visible';

    var html =
      '<span class="qm-step">Question ' + (i + 1) + ' of ' + STEPS.length + '</span>' +
      '<h3 class="qm-q">' + s.q + '</h3>' +
      '<p class="qm-hint">' + s.hint + '</p>';

    if (s.type === 'choice') {
      html += '<div class="qm-opts">';
      s.options.forEach(function (o) {
        var on = answers[s.key] === o ? ' on' : '';
        html += '<button class="qm-opt' + on + '" type="button" data-v="' + o + '">' + o + '</button>';
      });
      html += '</div>';
    } else {
      html +=
        '<input class="qm-in" type="text" inputmode="' + s.inputmode + '" ' +
        'autocomplete="' + s.autocomplete + '" placeholder="' + s.placeholder + '" ' +
        'value="' + (answers[s.key] || '') + '">' +
        '<p class="qm-err"></p>' +
        '<button class="qm-next" type="button">' +
        (i === STEPS.length - 1 ? 'Book my site visit' : 'Next') + '</button>';
    }

    body.innerHTML = html;
    body.scrollTop = 0;

    if (s.type === 'choice') {
      body.querySelectorAll('.qm-opt').forEach(function (b) {
        b.addEventListener('click', function () {
          answers[s.key] = b.dataset.v;
          advance();
        });
      });
    } else {
      var input = body.querySelector('.qm-in');
      var next = body.querySelector('.qm-next');
      var err = body.querySelector('.qm-err');

      function go() {
        var v = input.value.trim();
        if (!v) { err.textContent = 'Just need this one.'; input.focus(); return; }
        if (s.validate && !s.validate(v)) { err.textContent = s.error; input.focus(); return; }
        answers[s.key] = v;
        advance();
      }
      next.addEventListener('click', go);
      input.addEventListener('keydown', function (e) { if (e.key === 'Enter') go(); });
      // don't autofocus on the first paint — it yanks the mobile keyboard up
      // before they've read the question
      if (i > 0) setTimeout(function () { input.focus(); }, 320);
    }
  }

  function advance() {
    if (at < STEPS.length - 1) { render(at + 1); return; }
    submit();
  }

  function submit() {
    bar.style.width = '100%';
    body.innerHTML =
      '<div class="qm-sending"><span class="qm-spin"></span><p>Sending…</p></div>';

    var payload = {
      _subject: 'Site visit request — ' + (answers.suburb || '') + ' — ' + (answers.project_type || ''),
      _template: 'table',
      project_type: answers.project_type,
      has_plans: answers.has_plans,
      suburb: answers.suburb,
      budget: answers.budget,
      mobile: answers.mobile,
      page: window.location.pathname,
      landing_page: window.location.href,
      referrer: document.referrer || '(direct)',
      fill_seconds: Math.round((Date.now() - openedAt) / 1000)
    };

    // carry ad tracking through if it's on the URL
    var url = new URL(window.location.href);
    ['utm_source','utm_medium','utm_campaign','utm_content','utm_term','fbclid'].forEach(function (k) {
      var v = url.searchParams.get(k);
      if (v) payload[k] = v;
    });

    fetch(RELAY, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(payload)
    })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        if (d && (d.success === true || d.success === 'true')) done();
        else fail();
      })
      .catch(fail);
  }

  function done() {
    body.innerHTML =
      '<div class="qm-done">' +
        '<div class="qm-tick"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></div>' +
        '<h3 class="qm-q">Got it — thanks.</h3>' +
        '<p class="qm-hint">Stewart will give you a ring within one business day. If you\'d rather talk now, we\'re on <a href="tel:0738233200">07 3823 3200</a>.</p>' +
      '</div>';
  }

  function fail() {
    body.innerHTML =
      '<div class="qm-done">' +
        '<h3 class="qm-q">That didn\'t send.</h3>' +
        '<p class="qm-hint">Sorry — please ring us on <a href="tel:0738233200">07 3823 3200</a> and we\'ll sort it out.</p>' +
      '</div>';
  }

  function open() {
    if (!root) build();
    openedAt = Date.now();
    answers = {};
    render(0);
    root.classList.add('open');
    document.body.classList.add('qm-lock');
  }

  function close() {
    root.classList.remove('open');
    document.body.classList.remove('qm-lock');
  }

  // any [data-qualify] element opens it
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-qualify]');
    if (!t) return;
    e.preventDefault();
    open();
  });

  window.SabreQualify = { open: open, close: close };
})();
