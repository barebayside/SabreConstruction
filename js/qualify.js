/* ============================================================
   QUALIFYING FLOW — five questions, one per screen.

   Renders in two places off one state machine:
     · INLINE  — <div data-qualify-inline></div> sits on the page, visible
                 and startable with no click. This is the primary.
     · MODAL   — fallback only. Fires once if they reach the bottom without
                 having started, or from any [data-qualify] button.

   Answers are shared, so someone who starts inline and then hits the modal
   picks up where they left off.

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
      hint: 'A ballpark is fine. It stops us wasting your time.',
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
  var started = false;
  var finished = false;
  var openedAt = Date.now();
  var hosts = [];          // {root, bar, body, back, isModal}
  var modal = null;

  /* ---------- shell markup, shared by inline and modal ---------- */
  function shell(isModal) {
    return (isModal ? '<div class="qm-sheet" role="dialog" aria-modal="true" aria-label="Book a site visit">' : '') +
      '<div class="qm-top">' +
        '<button class="qm-back" type="button" aria-label="Back">' +
          '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>' +
        '</button>' +
        '<div class="qm-bar"><i></i></div>' +
        (isModal ?
          '<button class="qm-close" type="button" aria-label="Close">' +
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>' +
          '</button>' : '') +
      '</div>' +
      '<div class="qm-body"></div>' +
      (isModal ? '</div>' : '');
  }

  function wire(root, isModal) {
    var scope = isModal ? root.querySelector('.qm-sheet') : root;
    var h = {
      root: root,
      scope: scope,
      body: scope.querySelector('.qm-body'),
      bar: scope.querySelector('.qm-bar i'),
      back: scope.querySelector('.qm-back'),
      isModal: isModal
    };
    h.back.addEventListener('click', function () {
      if (h.at > 0) draw(h, h.at - 1);
    });
    hosts.push(h);
    return h;
  }

  /* ---------- the step machine ---------- */
  function draw(h, i) {
    h.at = i;
    var s = STEPS[i];
    h.bar.style.width = (i / STEPS.length * 100) + '%';
    h.back.style.visibility = i === 0 ? 'hidden' : 'visible';

    var html =
      '<span class="qm-step">Question ' + (i + 1) + ' of ' + STEPS.length + '</span>' +
      '<h3 class="qm-q">' + s.q + '</h3>' +
      '<p class="qm-hint">' + s.hint + '</p>';

    if (s.type === 'choice') {
      html += '<div class="qm-opts">';
      s.options.forEach(function (o) {
        html += '<button class="qm-opt' + (answers[s.key] === o ? ' on' : '') +
                '" type="button" data-v="' + o + '">' + o + '</button>';
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

    h.body.innerHTML = html;

    if (s.type === 'choice') {
      h.body.querySelectorAll('.qm-opt').forEach(function (b) {
        b.addEventListener('click', function () {
          started = true;
          answers[s.key] = b.dataset.v;
          step(h);
        });
      });
    } else {
      var input = h.body.querySelector('.qm-in');
      var err = h.body.querySelector('.qm-err');
      function go() {
        var v = input.value.trim();
        if (!v) { err.textContent = 'Just need this one.'; input.focus(); return; }
        if (s.validate && !s.validate(v)) { err.textContent = s.error; input.focus(); return; }
        started = true;
        answers[s.key] = v;
        step(h);
      }
      h.body.querySelector('.qm-next').addEventListener('click', go);
      input.addEventListener('keydown', function (e) { if (e.key === 'Enter') go(); });
      input.addEventListener('input', function () { started = true; });
      // only pull the keyboard up mid-flow, never on first paint
      if (i > 0 && (h.isModal || h.userDriven)) {
        setTimeout(function () { input.focus({ preventScroll: true }); }, 300);
      }
    }
    h.userDriven = true;
  }

  function step(h) {
    if (h.at < STEPS.length - 1) { draw(h, h.at + 1); return; }
    submit(h);
  }

  function submit(h) {
    finished = true;
    h.bar.style.width = '100%';
    h.body.innerHTML = '<div class="qm-sending"><span class="qm-spin"></span><p>Sending…</p></div>';

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
    var url = new URL(window.location.href);
    ['utm_source','utm_medium','utm_campaign','utm_content','utm_term','fbclid','gclid'].forEach(function (k) {
      var v = url.searchParams.get(k);
      if (v) payload[k] = v;
    });

    fetch(RELAY, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(payload)
    })
      .then(function (r) { return r.json(); })
      .then(function (d) { (d && (d.success === true || d.success === 'true')) ? done(h) : fail(h); })
      .catch(function () { fail(h); });
  }

  function done(h) {
    h.body.innerHTML =
      '<div class="qm-done">' +
        '<div class="qm-tick"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></div>' +
        '<h3 class="qm-q">Got it — thanks.</h3>' +
        '<p class="qm-hint">Stewart will give you a ring within one business day. If you\'d rather talk now, we\'re on <a href="tel:0738233200">07 3823 3200</a>.</p>' +
      '</div>';
    h.back.style.visibility = 'hidden';
  }

  function fail(h) {
    h.body.innerHTML =
      '<div class="qm-done">' +
        '<h3 class="qm-q">That didn\'t send.</h3>' +
        '<p class="qm-hint">Sorry — please ring us on <a href="tel:0738233200">07 3823 3200</a> and we\'ll sort it out.</p>' +
      '</div>';
    h.back.style.visibility = 'hidden';
  }

  /* ---------- inline ---------- */
  document.querySelectorAll('[data-qualify-inline]').forEach(function (el) {
    el.classList.add('qm-inline');
    el.innerHTML = shell(false);
    var h = wire(el, false);
    h.userDriven = false;
    draw(h, 0);
  });

  /* ---------- [data-qualify] buttons ----------
     Always scroll to the form that's already on the page. Never stack a popup
     on top of the identical thing. */
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-qualify]');
    if (!t) return;
    var inline = document.querySelector('.qm-inline');
    if (!inline) return;
    e.preventDefault();
    inline.scrollIntoView({ behavior: 'smooth', block: 'center' });
    inline.classList.add('flash');
    setTimeout(function () { inline.classList.remove('flash'); }, 1400);
  });

  /* ---------- NO POPUP ----------
     There used to be a bottom-of-page catch here that threw the form up as a
     modal once you scrolled far enough without filling it in. It's gone, and
     the modal machinery with it.

     The form is embedded and open on question one on every landing page. A
     popup of the same five questions interrupts someone who is already looking
     at them, which is the opposite of helping. Do not put it back. */
})();
