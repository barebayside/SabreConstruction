# Phase 5, part D — Spiral 3 (dealing with a builder), first six: S13, S14, S15, R36, R37, R39.
# Sources read 2026-09-17:
#   QBCC — Consumer Building Guide v3 (effective July 2023): licence; cost-plus warning; contract price s2; cooling-off ss35-39 (5 business
#     days, generally $100 plus reasonable out-of-pocket costs); Home Warranty (work over $3,300; non-completion, defective work and subsidence
#     for up to 6 years from completion; premium collected by the contractor and paid within 10 business days); deposits ss33-34 (10% under
#     $20,000, 5% at $20,000+, 20% where over half the work is off site; progress payments directly related to and proportionate to work on
#     site); commencement notice s16 (within 10 business days); building approvals and inspections (certificates of inspection; certifier must
#     give documents within 5 business days); variations ss40-41 (in writing before work; price increase not payable until work starts);
#     dispute resolution (write first; QBCC Early Dispute Resolution; QBCC letter before QCAT); EOTs s42; liquidated damages; practical
#     completion and the defects document; implied warranties ss19-29 (6 years structural, 1 year other; proceedings within the period or
#     a further 6 months if apparent in the last 6 months)
#   QBCC — "Deposits and progress payments" (27 Jun 2025); "Contract variations" (27 Jun 2025): written before the earlier of work starting
#     or 5 business days after agreement; urgent exception; must state description, date requested, delay estimate, price change; owner responds
#     in writing; contractor amends home warranty cover; "Contracts and agreement types" (27 Jun 2025)
#   QBCC — "Time limits for cover and claims" (23 Sep 2021): 6 years 6 months from the earlier of premium/contract/start; structural claim
#     within 3 months of first becoming aware; non-structural noticed within 6 months of substantial completion and claimed within 7 months;
#     non-completion claim within 3 months of the contract ending; cover may be extended where work takes longer than 6 months
#   Master Builders Queensland — Code of Conduct (members "conduct their business dealings in a fair, reasonable and honest manner"); over
#     10,000 members, nine offices (mbqld.com.au, via search excerpts — the site blocks automated reads)
#   Sabre publishes QBCC licence 15486557 and Master Builders Queensland No. 00352 in every footer (docs/client-facts.md)
# Rule 1: no prices, no bands, no timelines beyond the statutory ones quoted.

POSTS = {}

# ---------------------------------------------------------------- S13 · Master Builders membership
POSTS["s13-master-builders"] = dict(
    slug="what-does-master-builders-membership-actually-mean-for-you",
    section="builder",
    title="What does Master Builders membership actually mean for you?",
    h1="What does Master Builders membership<br>actually mean for you?",
    description="Less than the logo suggests and more than nothing. What Master Builders Queensland is, what a member has agreed to, what it is not (a licence, a regulator, insurance), and how to check a builder's membership for yourself.",
    lede="Every second builder's ute has the Master Builders logo on it, and most families don't know what it means. It isn't a licence, and it isn't a guarantee. It is an association with a code of conduct, and a member has agreed to some things. Here's what it does and doesn't tell you, and how to check it in a minute.",
    date="2026-09-17", category="Dealing with a builder", image="blog/what-does-master-builders-membership-actually-mean-for-you.jpg",
    image_alt="A builder's site fence with a blank membership plaque beside a blank licence plate, a frame going up behind",
    image_caption="Illustration in the style of Sabre's story frames. Real plaques carry real numbers; ours are in the footer.",
    label=("The logo on the ute", "Master Builders"),
    card_title="What does Master Builders membership actually mean for you?",
    card_blurb="Less than the logo suggests and more than nothing. What the association is, what a member has agreed to, what it is not, and how to check a builder's membership yourself.",
    about=["Master Builders Queensland", "Choosing a builder", "QBCC", "Building industry associations"],
    related=["what-is-the-qbcc-and-what-to-check-on-a-builders-licence", "what-questions-should-we-ask-a-builder-before-we-sign", "who-are-the-small-independent-builders-on-brisbanes-bayside"],
    cta="Sabre's Master Builders number is 00352 and the QBCC licence is 15486557, both in the footer. Check them before you call &mdash; then call.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Master Builders Queensland is the state's building industry association: a membership body with more than ten thousand members and offices across the state. A member is a business that has joined, pays to belong, and has agreed to the association's Code of Conduct, which requires members to conduct their business dealings in a fair, reasonable and honest manner.</p>
        <p>What it is not: it is not a licence (the QBCC issues those), it is not a regulator (the QBCC is), and it is not insurance (the Queensland Home Warranty Scheme is, and it comes with a licensed builder whether or not they're a member).</p>
        <p>So membership tells you a builder has chosen to belong to the industry's body and be bound by its code. That's worth something. The licence check tells you whether they're allowed to build your house at all. Do that one first.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#what-it-is">What is Master Builders Queensland?</a></li>
          <li><a href="#what-members-agree">What has a member agreed to?</a></li>
          <li><a href="#what-it-isnt">What membership is not</a></li>
          <li><a href="#how-to-check">How do you check a builder's membership?</a></li>
          <li><a href="#how-to-weigh">How much should it weigh in your choice?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="what-it-is">What is Master Builders Queensland?</h2>
      <p>An industry association. It represents builders and trade contractors to government, runs training and licensing courses, publishes standard contracts, and provides its members with advice on contracts, disputes, workplace law and the QBCC's financial requirements.</p>
      <p>It's a Queensland body with a long history and a large membership. Joining is voluntary. Plenty of good builders belong; some good builders don't.</p>

      <h2 class="h2" id="what-members-agree">What has a member agreed to?</h2>
      <p>The Code of Conduct. Its core obligation is the one that matters to a family:</p>

      <blockquote class="proof">
        <p><b>Master Builders members agree to &ldquo;conduct their business dealings in a fair, reasonable and honest manner&rdquo; and to conduct themselves in a way that does not harm the association's reputation or that of other members.</b></p>
        <cite>Master Builders Queensland, <em>Code of Conduct</em>. An association's code is a promise to the association; the law's protections come from the QBCC Act. Both exist. They aren't the same thing.</cite>
      </blockquote>

      <p>Members also have access to the association's standard building contracts, which are among the common forms used for Queensland homes, and to its advice on getting the paperwork right. That tends to show up as a tidier contract on your kitchen table.</p>

      <h2 class="h2" id="what-it-isnt">What membership is not</h2>
      <ul class="pts">
        <li><strong>Not a licence.</strong> The QBCC licenses builders under the <em>Queensland Building and Construction Commission Act 1991</em>. A member without a current licence in the right class cannot lawfully build your house. <a href="../what-is-the-qbcc-and-what-to-check-on-a-builders-licence/">How to check the licence is here.</a></li>
        <li><strong>Not a regulator.</strong> If the work is defective or the builder walks off, your complaint goes to the QBCC, not the association. The association can hear a concern about a member's conduct; it can't order rectification.</li>
        <li><strong>Not insurance.</strong> The Queensland Home Warranty Scheme covers residential work over $3,300 done by a licensed contractor, member or not. The premium is collected by the builder and paid to the QBCC.</li>
        <li><strong>Not a quality mark.</strong> Membership says the builder joined and agreed to the code. It doesn't inspect their work.</li>
      </ul>

      <h2 class="h2" id="how-to-check">How do you check a builder's membership?</h2>
      <p>Ask for the membership number and check it with Master Builders Queensland: the association has a member search on its website and answers the phone. Then do the check that matters more: put the QBCC licence number into the QBCC's online licence search and read the class, the status and the history.</p>
      <p>A builder who puts both numbers in plain sight, on the site sign, the contract and the website, has made your job easy. Ours are in the footer of every page.</p>

      <h2 class="h2" id="how-to-weigh">How much should it weigh in your choice?</h2>
      <p>As a tie-breaker and a signal, not a decider.</p>
      <p>The things that should decide it are the licence and its history, the contract and its allowances, the deposit and payment terms, the dates, and the person you'll be dealing with when the frame is up. <a href="../what-questions-should-we-ask-a-builder-before-we-sign/">Those fifteen questions are here.</a> Membership sits behind all of them: a builder who has chosen to be bound by an industry code and to use the industry's contracts is, on the whole, a builder who takes the paperwork seriously. That's a reasonable thing to like.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Master Builders Queensland is an association, not a licence, a regulator or an insurer.</b></li>
          <li><b>A member has agreed to a code:</b> fair, reasonable and honest dealings.</li>
          <li><b>The QBCC licence is the check that decides whether they can build your house.</b> Do it first.</li>
          <li><b>Home Warranty cover comes with any licensed builder,</b> member or not.</li>
          <li><b>Membership is a signal and a tie-breaker.</b> Weigh it after the licence, the contract, the money, the dates and the person.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Is a Master Builders contract better than a QBCC or HIA one?</p>
          <p>They're all standard forms that have to comply with Schedule 1B of the QBCC Act. The differences are in the general conditions. Read whichever one you're handed with the QBCC's Consumer Building Guide beside it, and ask about anything that isn't clear.</p>
        </div>
        <div>
          <p class="q">Can we complain to Master Builders about a member?</p>
          <p>You can raise a conduct concern with the association. For defective or incomplete work, the QBCC is the body with the power to act, and the Consumer Building Guide sets out its dispute process.</p>
        </div>
        <div>
          <p class="q">Should we avoid a builder who isn't a member?</p>
          <p>Not on that alone. Check the licence, read the contract, ask the questions. Membership is one signal among several.</p>
        </div>
        <div>
          <p class="q">Is Sabre a member?</p>
          <p>Yes. Master Builders Queensland No. 00352, QBCC licence 15486557, both in the footer. Look them up before you ring.</p>
        </div>
      </div>

      <p class="small sources">Sources: Master Builders Queensland, <em>Code of Conduct</em> and <em>Membership</em> (mbqld.com.au); Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/sites/default/files/2021-09/guide-qbcc-consumer-building-v3.pdf" rel="noopener">Consumer Building Guide</a> (version 3, effective July 2023); <em>Queensland Building and Construction Commission Act 1991</em>. Read 17 September 2026. This is a plain-English guide, not legal advice.</p>
''')

# ---------------------------------------------------------------- S14 · progress payments
POSTS["s14-progress-payments"] = dict(
    slug="progress-payments-what-you-pay-and-when-on-a-queensland-house-build",
    section="builder",
    title="Progress payments: what you pay, and when, on a Queensland house build",
    h1="Progress payments: what you pay,<br>and when, on a Queensland house build.",
    description="The rules in plain words: the deposit limits (5% at $20,000 and over), claims that must match work done on site, the commencement notice, what practical completion means, and the QBCC's warning that paying early or paying more cuts your Home Warranty protection.",
    lede="You don't pay for a house in one go, and you shouldn't pay for it ahead of the work either. Queensland's rules on deposits and progress payments are short, specific and written to protect you. Here they are, with the regulator's own wording, so you know what a normal payment schedule looks like and what to refuse.",
    date="2026-09-17", category="Dealing with a builder", image="blog/progress-payments-what-you-pay-and-when-on-a-queensland-house-build.jpg",
    image_alt="A new house at frame stage, seen from the street, with a payment claim and a pen on the bonnet of a ute in the foreground",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real job.",
    label=("The rules, in plain words", "Progress payments"),
    card_title="Progress payments: what you pay, and when, on a Queensland house build",
    card_blurb="Deposit limits, claims that must match work on site, the commencement notice, practical completion, and the QBCC's warning that paying early cuts your Home Warranty protection.",
    about=["Progress payments", "Building deposit Queensland", "QBCC", "Home Warranty Scheme"],
    related=["fixed-price-or-cost-plus-what-do-builders-mean", "what-questions-should-we-ask-a-builder-before-we-sign", "what-is-the-qbcc-and-what-to-check-on-a-builders-licence"],
    cta="Ask Nathan to walk you through Sabre's payment schedule against these rules, line by line, before you sign.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Three rules do most of the work. <strong>One:</strong> the deposit is capped. For a contract of $20,000 or more, the most a builder can take before work starts on site is 5% of the contract price; under $20,000 it's 10%; and up to 20% only where more than half the work is done off site. <strong>Two:</strong> after the deposit, every progress claim must be directly related to work on site and proportionate to it &mdash; the QBCC's example is that you shouldn't pay 50% until at least half the work is done. <strong>Three:</strong> you're not required to make the final payment until practical completion.</p>
        <p>The regulator's warning is worth reading twice: never pay more than the contract says, or earlier than it says, because doing so reduces your protection under the Queensland Home Warranty Scheme.</p>
        <p>A normal schedule, then, is a small deposit and a handful of stage payments that follow the house going up. Anything front-loaded is a question to ask.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#deposit">How big can the deposit be?</a></li>
          <li><a href="#claims">What can a progress claim be for?</a></li>
          <li><a href="#stages">What does a normal schedule look like?</a></li>
          <li><a href="#notices">What paperwork should arrive along the way?</a></li>
          <li><a href="#final">When is the final payment due?</a></li>
          <li><a href="#the-warning">Why does paying early hurt you?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="deposit">How big can the deposit be?</h2>
      <p>The law sets the maximum, by contract value:</p>
      <ul class="pts">
        <li><strong>Under $20,000:</strong> 10% of the contract price.</li>
        <li><strong>$20,000 or more</strong> (every new house): <strong>5%</strong> of the contract price.</li>
        <li><strong>Any price, where more than half the work is done off site</strong> (prefabrication, substantial custom work away from the block): up to 20%.</li>
      </ul>

      <blockquote class="proof">
        <p><b>&ldquo;The maximum deposit allowed (before work starts on site) is: 10% where the total contract price is less than $20,000; 5% where the price is $20,000 or more; 20% for a contract of any price where the value of the work to be performed off-site is more than 50% of the contract price.&rdquo;</b></p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023 (sections 33&ndash;34 of Schedule 1B). A builder asking for more is asking for something the Act doesn't allow.</cite>
      </blockquote>

      <h2 class="h2" id="claims">What can a progress claim be for?</h2>
      <p>Work that's been done on your block, in proportion to its value. The guide says owners and contractors are free to choose the number and timing of progress payments, provided the amount claimed is directly related to work progress on site and proportionate to (or less than) the value of the work that relates to the claim.</p>
      <p>The QBCC's own example: the contractor can't claim more than 50% of the contract price, including the deposit, until at least 50% of the work on site has been completed. Where payments are at intervals rather than stages, the contractor has to support each claim with evidence of the work performed and its value.</p>

      <h2 class="h2" id="stages">What does a normal schedule look like?</h2>
      <p>Most fixed-price house contracts use stage payments that follow the build. The names vary between contract forms, but the shape is familiar:</p>
      <ul class="pts">
        <li><strong>Deposit</strong> &mdash; within the cap above.</li>
        <li><strong>Base</strong> &mdash; footings and slab (or the subfloor on a highset) done.</li>
        <li><strong>Frame</strong> &mdash; the frame up and inspected.</li>
        <li><strong>Enclosed (lock-up)</strong> &mdash; roof on, external walls and windows in, doors lockable.</li>
        <li><strong>Fixing</strong> &mdash; internal linings, joinery, fit-out largely complete.</li>
        <li><strong>Practical completion</strong> &mdash; the final payment.</li>
      </ul>
      <p>The percentages against each stage are set in the contract, and they're what to read against the rule above: does each one track the value of the work done to that point? If the &ldquo;base&rdquo; stage is a big share of the price on a house with a simple slab, ask why.</p>

      <h2 class="h2" id="notices">What paperwork should arrive along the way?</h2>
      <ul class="pts">
        <li><strong>The signed contract</strong>, with plans and specifications, within 5 business days of entering it.</li>
        <li><strong>A commencement notice</strong>, within 10 business days of work starting on site, stating the date work started and the date for practical completion.</li>
        <li><strong>Certificates of inspection</strong> from the certifier at the mandatory stages, which the builder must give you as soon as practicable after receiving them.</li>
        <li><strong>Written variations</strong> before any changed work starts, and <strong>written extension-of-time claims</strong> if the completion date moves.</li>
      </ul>
      <p>Each payment claim should line up with something on that list. A frame-stage claim with no frame inspection certificate is a question.</p>

      <h2 class="h2" id="final">When is the final payment due?</h2>
      <p>At practical completion. The guide says you're not required to make the final payment until all the contracted work is complete in accordance with the contract, plans and specifications, and either without defects or with only minor defects or omissions that won't unreasonably affect occupation. If there are minor items, the builder gives you a defects document listing what's agreed and what isn't, compiled with you at a handover inspection.</p>

      <h2 class="h2" id="the-warning">Why does paying early hurt you?</h2>
      <p>Because the Home Warranty Scheme's non-completion cover assumes you've paid according to the contract. If a builder can't finish and you've paid ahead of the work, the scheme's payout is reduced by what you paid that you shouldn't have.</p>

      <blockquote class="proof">
        <p><b>&ldquo;Never make a progress payment that is more than the amount outlined under the contract, or make the progress payment before the due date outlined under the contract, as this will reduce the protection available to you under the Queensland Home Warranty Scheme.&rdquo;</b></p>
        <cite>Queensland Building and Construction Commission, <em>Deposits and progress payments</em>, reviewed 27 June 2025. Paying early to be helpful is the mistake families make with a builder they like.</cite>
      </blockquote>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Deposit: 5% on a contract of $20,000 or more,</b> 10% under, 20% only if more than half the work is off site.</li>
          <li><b>Every claim must match work done on site,</b> in proportion. No 50% until half the work is done.</li>
          <li><b>Stage payments that follow the build are normal.</b> Read the percentages against the work.</li>
          <li><b>Commencement notice within 10 business days; inspection certificates as they come.</b> Claims should line up with them.</li>
          <li><b>Final payment at practical completion,</b> with a defects document for minor items.</li>
          <li><b>Never pay more or earlier than the contract says.</b> It reduces your Home Warranty protection.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Can the builder ask for money before the contract is signed?</p>
          <p>A deposit is paid under a contract, within the cap. Money for a soil test, a design or a quote is a separate arrangement and should be in writing with what it buys. Be careful with anything described as &ldquo;holding&rdquo; a price or a slot.</p>
        </div>
        <div>
          <p class="q">What if we disagree with a progress claim?</p>
          <p>Raise it in writing straight away and ask what work it relates to. The guide's dispute path starts with writing to the contractor, then the QBCC's free Early Dispute Resolution service. Don't withhold payment for completed stages without advice; don't pay for stages that aren't done.</p>
        </div>
        <div>
          <p class="q">Does the bank pay the progress claims?</p>
          <p>On a construction loan the lender usually pays each stage after its own valuer confirms the work, which is one more check on the claim matching the build. Ask your lender how they run it.</p>
        </div>
        <div>
          <p class="q">What's a &ldquo;retention&rdquo;?</p>
          <p>An amount held back from the final payment until a defects period has passed. Some contracts have one; many domestic ones don't. If yours does, it's in the contract schedule, and it's not a substitute for the defects document at practical completion.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/sites/default/files/2021-09/guide-qbcc-consumer-building-v3.pdf" rel="noopener">Consumer Building Guide</a> (version 3, effective July 2023) and <a href="https://www.qbcc.qld.gov.au/home-owner-hub/build-renovate/contracts-payments/deposits-progress-payments" rel="noopener">Deposits and progress payments</a> (reviewed 27 June 2025); Schedule 1B, <em>Queensland Building and Construction Commission Act 1991</em>. Read 17 September 2026. Thresholds change; check the QBCC's current pages. This is a plain-English guide, not legal or financial advice.</p>
''')

# ---------------------------------------------------------------- S15 · variations
POSTS["s15-variations"] = dict(
    slug="variations-why-the-price-changed-and-when-it-shouldnt-have",
    section="builder",
    title="Variations: why the price changed, and when it shouldn't have",
    h1="Variations: why the price changed,<br>and when it shouldn't have.",
    description="Queensland's rule is short: a variation must be in writing, agreed by you, before the work starts. What a variation document has to contain, the one urgent exception, when a change is the builder's cost rather than yours, and how to keep the number of them down.",
    lede="The number one complaint about builders in Australia isn't bad work. It's the price that moved. Most of the time it moved through a variation, and Queensland has clear rules about how those are supposed to happen. Here they are, plus the honest part: some variations are on us, not you.",
    date="2026-09-17", category="Dealing with a builder", image="blog/variations-why-the-price-changed-and-when-it-shouldnt-have.jpg",
    image_alt="A builder's hand and an owner's hand each holding a pen over a single-page document on a site table, the frame behind",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of real people.",
    label=("In writing, before the work", "Variations"),
    card_title="Variations: why the price changed, and when it shouldn't have",
    card_blurb="The rule is short: in writing, agreed by you, before the work starts. What the document must contain, the urgent exception, when a change is the builder's cost, and how to keep them down.",
    about=["Building contract variations", "QBCC", "Building disputes Queensland", "Cost overruns"],
    related=["progress-payments-what-you-pay-and-when-on-a-queensland-house-build", "fixed-price-or-cost-plus-what-do-builders-mean", "what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane"],
    cta="Ask Nathan how Sabre handles a variation, and what happens when the change is our fault. He'd rather tell you now than in month four.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>A variation is any change to the work or the materials under the contract after it's signed. Queensland's rule is that all variations must be agreed in writing by the home owner before the variation work starts, and the builder can't require any price increase from a variation to be paid until that work has started.</p>
        <p>The written document has to describe the change, state the date it was requested, give the builder's reasonable estimate of any delay, and state the change to the contract price or how it will be calculated. You respond in writing. The one exception is genuinely urgent work, where it isn't practicable to write it up first; even then it follows promptly.</p>
        <p>When shouldn't the price have changed? When the &ldquo;variation&rdquo; is something the contract already covered, when it's fixing the builder's own error, or when it was never agreed in writing before the work. Those are questions to ask, in writing, before you pay.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#what-is-one">What is a variation?</a></li>
          <li><a href="#the-rule">What does the law require?</a></li>
          <li><a href="#the-document">What must the variation document say?</a></li>
          <li><a href="#urgent">What's the urgent exception?</a></li>
          <li><a href="#whose-cost">When is it the builder's cost, not yours?</a></li>
          <li><a href="#fewer">How do you keep the number down?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="what-is-one">What is a variation?</h2>
      <p>The guide's definition: any change to the materials used or work to be performed under the contract. Three kinds turn up on a house build.</p>
      <ul class="pts">
        <li><strong>Ones you ask for.</strong> A different benchtop, a bigger deck, a window moved. Your call, your cost, in writing first.</li>
        <li><strong>Ones the site forces.</strong> Rock where the soil test didn't find it, an old septic tank nobody knew about, a council condition on the approval. Real, and the contract should say how they're priced.</li>
        <li><strong>Ones the builder creates.</strong> A measurement missed, a product ordered wrong, work that has to be redone. Those are not variations you pay for.</li>
      </ul>

      <h2 class="h2" id="the-rule">What does the law require?</h2>

      <blockquote class="proof">
        <p><b>&ldquo;All variations must be agreed in writing by the home owner before the variation work commences and any price increase due to the variation can not be required to be paid until the variation work is started.&rdquo;</b></p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023 (sections 40&ndash;41 of Schedule 1B). Not a courtesy. The rule.</cite>
      </blockquote>

      <p>The QBCC's variations page adds the timing: the builder has to give you the written variation before the earlier of the variation work starting, or five business days after you both agreed to it. In person, by post or by email all count.</p>

      <h2 class="h2" id="the-document">What must the variation document say?</h2>
      <p>The QBCC lists it. A variation document must include:</p>
      <ul class="pts">
        <li>A <strong>description</strong> of the variation.</li>
        <li>The <strong>date</strong> it was requested.</li>
        <li>The builder's <strong>reasonable estimate of any delay</strong> to the work.</li>
        <li>The <strong>change to the contract price</strong>, or the method for calculating it, and when the extra is payable or the credit is given.</li>
      </ul>
      <p>You respond in writing to say whether you agree. If the variation changes the value of the job, the builder is responsible for amending the Home Warranty cover.</p>
      <p>A text message saying &ldquo;yep go ahead&rdquo; is writing. It is not the document above. Ask for the document.</p>

      <h2 class="h2" id="urgent">What's the urgent exception?</h2>
      <p>If the variation work has to be done urgently and it isn't reasonably practicable to produce a written copy first &mdash; the QBCC's example is safety &mdash; the work can go ahead and the paperwork follows promptly. Think a collapsing trench or a live service found where it shouldn't be. Not a benchtop.</p>

      <h2 class="h2" id="whose-cost">When is it the builder's cost, not yours?</h2>
      <p>This is the part the rules don't spell out and a fair builder does.</p>
      <ul class="pts">
        <li><strong>Fixing the builder's own error.</strong> A wall in the wrong place, a beam undersized, a window ordered the wrong size. Rectifying that is the builder's obligation under the statutory warranties, not a variation to you.</li>
        <li><strong>Work the contract already covers.</strong> If it's in the plans and specifications, it's in the price. Read the specification before agreeing to pay for something &ldquo;extra.&rdquo;</li>
        <li><strong>Work done without the written agreement.</strong> If the variation wasn't agreed in writing before it started, the builder is on the wrong side of the rule. Get advice before paying.</li>
      </ul>
      <p>Site-forced variations sit in between. Rock is nobody's fault. What matters is that the contract said how unforeseen site conditions would be priced, and that the variation is documented the same way as any other.</p>

      <h2 class="h2" id="fewer">How do you keep the number down?</h2>
      <p>The QBCC's advice is to keep variations to a minimum because they're the most common cause of cost overruns and disputes. Practically:</p>
      <ul class="pts">
        <li><strong>Finish the design before you sign.</strong> Every decision made after the contract is a variation.</li>
        <li><strong>Choose the selections before you sign.</strong> Tiles, tapware, appliances. Allowances are where prices drift.</li>
        <li><strong>Get the soil test and the surveys done first.</strong> Fewer surprises in the ground.</li>
        <li><strong>Read the specification.</strong> Know what's in the price so you know what isn't.</li>
      </ul>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>In writing, agreed by you, before the work starts.</b> The extra isn't payable until the work begins.</li>
          <li><b>The document must have a description, a date, a delay estimate and the price change.</b> A text isn't it.</li>
          <li><b>Urgent means safety,</b> not selections.</li>
          <li><b>The builder's own errors and anything already in the specification are not your variations.</b></li>
          <li><b>Fewest variations: finish the design and the selections before you sign,</b> and test the ground.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">The builder did the extra work and is now asking us to pay. Do we have to?</p>
          <p>If it wasn't agreed in writing before the work started, the builder hasn't followed the rule. Write to them setting that out, and if it isn't resolved, the QBCC's Early Dispute Resolution service is free. Get advice before you refuse outright; the answer depends on what was said and when.</p>
        </div>
        <div>
          <p class="q">Can a variation move the completion date?</p>
          <p>Yes. The delay estimate is in the document for that reason, and a variation involving extra work is one of the grounds the Act allows for an extension of time. Agree the delay when you agree the price.</p>
        </div>
        <div>
          <p class="q">Can we get a credit for taking something out?</p>
          <p>A variation can reduce the price as well as increase it. The document should state the credit and when it's given.</p>
        </div>
        <div>
          <p class="q">How does Sabre handle a change that's our fault?</p>
          <p>Ask Nathan, and get the answer before you sign. The right answer is that a builder's error is the builder's cost, and you'll never see it on a variation.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/sites/default/files/2021-09/guide-qbcc-consumer-building-v3.pdf" rel="noopener">Consumer Building Guide</a> (version 3, effective July 2023) and <a href="https://www.qbcc.qld.gov.au/home-owner-hub/build-renovate/contracts-payments/contract-variations" rel="noopener">Contract variations</a> (reviewed 27 June 2025); Schedule 1B, <em>Queensland Building and Construction Commission Act 1991</em>. Read 17 September 2026. This is a plain-English guide, not legal advice.</p>
''')

# ---------------------------------------------------------------- R36 · builder's insurance
POSTS["r36-insurance"] = dict(
    slug="what-insurance-should-a-builder-have-and-what-does-it-cover-you-for",
    section="builder",
    title="What insurance should a builder have, and what does it cover you for?",
    h1="What insurance should a builder have,<br>and what does it cover you for?",
    description="Four kinds. The Queensland Home Warranty Scheme (compulsory, and it protects you), contract works insurance for the half-built house, public liability, and workers' compensation. What each one covers, who pays, and what to ask to see.",
    lede="&ldquo;Fully insured&rdquo; is on every builder's website and it means four different things. One of them is a state scheme that protects you if the builder can't finish or the work is defective. The others protect the house, the neighbours and the workers while it's being built. Here's what each one is and what to ask for.",
    date="2026-09-17", category="Dealing with a builder", image="blog/what-insurance-should-a-builder-have-and-what-does-it-cover-you-for.jpg",
    image_alt="A half-built house at lock-up stage under a dark afternoon sky, site fencing up, a certificate folder on the site table",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real job.",
    label=("Four kinds, one protects you", "The builder's insurance"),
    card_title="What insurance should a builder have, and what does it cover you for?",
    card_blurb="Four kinds. The Queensland Home Warranty Scheme protects you; contract works, public liability and workers' comp protect the house, the neighbours and the workers. What each covers and what to ask to see.",
    about=["Queensland Home Warranty Scheme", "Builder's insurance", "Contract works insurance", "QBCC"],
    related=["what-is-the-qbcc-and-what-to-check-on-a-builders-licence", "what-happens-if-a-builder-goes-under-mid-build", "what-is-a-defects-liability-period"],
    cta="Ask Nathan for the Notice of Cover and the certificates of currency. He'll have them, and he'll explain what each one does for your job.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Four policies matter on a house build, and only one of them is really about you.</p>
        <p><strong>The Queensland Home Warranty Scheme</strong> is compulsory for residential work over $3,300 by a licensed contractor. It protects <em>you</em> against non-completion, defective work and subsidence for up to six years from completion. The builder collects the premium from you and pays it to the QBCC, and you should receive a Notice of Cover within two weeks of signing.</p>
        <p><strong>Contract works insurance</strong> covers the half-built house against fire, storm, theft and damage. <strong>Public liability</strong> covers injury or damage to third parties &mdash; the neighbour's fence, a visitor. <strong>Workers' compensation</strong> covers the people on site. Those three protect the builder and the job; you want to see they exist, because if they don't, problems on site become your problems.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#home-warranty">The Home Warranty Scheme: what it covers</a></li>
          <li><a href="#contract-works">Contract works insurance</a></li>
          <li><a href="#liability">Public liability and workers' compensation</a></li>
          <li><a href="#what-to-ask">What should you ask to see?</a></li>
          <li><a href="#your-own">What about your own insurance?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="home-warranty">The Home Warranty Scheme: what it covers</h2>
      <p>It's run by the QBCC and it's the one policy on the list that exists for the owner.</p>

      <blockquote class="proof">
        <p><b>&ldquo;Residential construction work valued at more than $3,300 is covered by the Qld Home Warranty Scheme. The Scheme provides protection for home owners against non-completion, defective work and subsidence for up to 6 years from completion, provided a licensed contractor performs the work.&rdquo;</b> The builder must collect the premium and pay it to the QBCC within 10 business days of the contract or before work starts, whichever is earlier.</p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023. If you haven't received a Notice of Cover within two weeks of signing, ask why.</cite>
      </blockquote>

      <p>Three things to know about it:</p>
      <ul class="pts">
        <li><strong>It needs a licensed contractor.</strong> Work by an unlicensed builder may not be covered. That's the reason the licence check comes first.</li>
        <li><strong>It has time limits.</strong> Cover runs six years and six months from the earliest of the premium, the contract or the start of work; structural defect claims must be made within three months of first becoming aware; non-structural defects noticed within six months of substantial completion and claimed within seven. <a href="../what-is-a-defects-liability-period/">The periods are explained here.</a></li>
        <li><strong>It doesn't cover non-completion on cost-plus contracts.</strong> The QBCC says so directly. <a href="../fixed-price-or-cost-plus-what-do-builders-mean/">That's here.</a></li>
      </ul>

      <h2 class="h2" id="contract-works">Contract works insurance</h2>
      <p>Sometimes called construction or builder's risk insurance. It covers the works themselves while they're being built: the frame that blows over in a storm, the fire in the half-finished kitchen, materials stolen from the site. The builder holds it and it runs for the length of the job.</p>
      <p>Why it matters to you: until practical completion the house is the builder's responsibility, and if something destroys it, this is the policy that rebuilds it. Ask who carries it and confirm it's current. Some contracts require the owner to take it out instead; read the schedule.</p>

      <h2 class="h2" id="liability">Public liability and workers' compensation</h2>
      <p><strong>Public liability</strong> covers injury to people who aren't employees, and damage to property that isn't the works: the neighbour's car under a falling sheet, a visitor who trips on site. A builder without it is putting those risks onto whoever's nearest, which can be you as the owner of the land.</p>
      <p><strong>Workers' compensation</strong> is compulsory for employers in Queensland and covers the builder's employees if they're injured. Subcontractors carry their own. It's the builder's obligation, not yours, and it's the one you ask about so you know the builder runs a proper business.</p>

      <h2 class="h2" id="what-to-ask">What should you ask to see?</h2>
      <ul class="pts">
        <li><strong>The Home Warranty Notice of Cover</strong> for your contract, from the QBCC, within two weeks of signing.</li>
        <li><strong>Certificates of currency</strong> for contract works and public liability, showing the insurer, the period and the cover.</li>
        <li><strong>Confirmation of workers' compensation</strong> for the builder's own employees.</li>
      </ul>
      <p>A builder who runs a proper business has these in a folder and will send them without a fuss. It's a normal question. Sabre answers it before you ask.</p>

      <h2 class="h2" id="your-own">What about your own insurance?</h2>
      <p>Tell your home insurer before demolition. A vacant block and a building site are different risks from an occupied house, and the policy you had on the old house doesn't quietly become a policy on the new one. Ask them what they cover during the build and from when. We're builders, not insurers; that conversation is yours.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>The Home Warranty Scheme is the one that protects you:</b> non-completion, defects, subsidence, up to six years, licensed contractor required.</li>
          <li><b>Notice of Cover within two weeks of signing.</b> If it doesn't come, ask.</li>
          <li><b>Contract works insurance rebuilds the half-built house</b> if a storm or a fire takes it. Check who holds it.</li>
          <li><b>Public liability and workers' comp protect the neighbours and the workers.</b> Ask for certificates of currency.</li>
          <li><b>Tell your own insurer before demolition.</b> A building site isn't the house you insured.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Who pays the Home Warranty premium?</p>
          <p>You do, through the builder, who collects it and passes it to the QBCC. It's usually a line in the contract price. The Notice of Cover is your proof it was paid.</p>
        </div>
        <div>
          <p class="q">Does Home Warranty cover the builder's bad workmanship?</p>
          <p>Defective work is one of the three things it covers, within its time limits, after the QBCC's complaint and rectification process. The first step is always a written complaint to the builder.</p>
        </div>
        <div>
          <p class="q">Is &ldquo;fully insured&rdquo; on a website enough?</p>
          <p>No. Ask for the documents. A certificate of currency takes a builder five minutes to send.</p>
        </div>
        <div>
          <p class="q">What if a storm damages the frame?</p>
          <p>That's what contract works insurance is for, and it's the builder's claim, not yours. The Home Warranty Scheme also has limited cover for fire and storm damage to incomplete work in a non-completion claim.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/sites/default/files/2021-09/guide-qbcc-consumer-building-v3.pdf" rel="noopener">Consumer Building Guide</a> (version 3, effective July 2023); <em>Time limits for cover and claims</em> (reviewed 23 September 2021); <em>Home warranty for non-completion claims</em>; <em>Contracts and agreement types</em> (reviewed 27 June 2025). Read 17 September 2026. Cover amounts and limits change; check the QBCC's current pages. This is a plain-English guide, not insurance or legal advice.</p>
''')

# ---------------------------------------------------------------- R37 · defects liability period
POSTS["r37-defects-period"] = dict(
    slug="what-is-a-defects-liability-period",
    section="builder",
    title="What is a defects liability period, and what protects you after it?",
    h1="What is a defects liability period,<br>and what protects you after it?",
    description="Three layers, not one: the defects period in your contract, the statutory warranties in the QBCC Act (six years structural, one year for the rest), and the Home Warranty Scheme's cover and claim windows. What each does, when each ends, and what to do the day you notice a crack.",
    lede="The builder hands over the keys and, somewhere in the contract, a clock starts. Most families think there's one clock. There are three, they run for different lengths, and the longest of them isn't in the contract at all. Here's how the protection actually stacks up, in the regulator's words.",
    date="2026-09-17", category="Dealing with a builder", image="blog/what-is-a-defects-liability-period.jpg",
    image_alt="A hand running along a hairline crack in a new rendered wall beside a window, a set of keys on the sill",
    image_caption="Illustration in the style of Sabre's story frames.",
    label=("Three clocks, not one", "Defects period"),
    card_title="What is a defects liability period, and what protects you after it?",
    card_blurb="Three layers: the defects period in your contract, the statutory warranties in the QBCC Act, and the Home Warranty Scheme's windows. What each does, when each ends, and what to do when you notice a crack.",
    about=["Defects liability period", "Statutory warranties Queensland", "Home Warranty Scheme", "QBCC"],
    related=["what-insurance-should-a-builder-have-and-what-does-it-cover-you-for", "progress-payments-what-you-pay-and-when-on-a-queensland-house-build", "what-questions-should-we-ask-a-builder-before-we-sign"],
    cta="Ask Nathan what Sabre's defects period is, how to report something, and what happens on day one after you ring. Then hold him to it.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>A <strong>defects liability period</strong> is the window written into your contract, starting at practical completion, during which the builder comes back to fix defects that show up. Its length is set by the contract, so read yours.</p>
        <p>Behind it sit the <strong>statutory warranties</strong> in Schedule 1B of the QBCC Act, which are part of every regulated domestic building contract whether the contract mentions them or not: six years from completion for structural defects, one year for everything else, with legal proceedings to be started within the period or a further six months if the problem appears in the last six months.</p>
        <p>Behind that sits the <strong>Queensland Home Warranty Scheme</strong>: cover for six years and six months, with a structural defect claim to be made within three months of first becoming aware of it, and a non-structural defect to be noticed within six months of substantial completion and claimed within seven. The contract clock is the shortest of the three.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#contract">Layer one: the defects period in the contract</a></li>
          <li><a href="#statutory">Layer two: the statutory warranties</a></li>
          <li><a href="#scheme">Layer three: the Home Warranty Scheme</a></li>
          <li><a href="#structural">What counts as structural?</a></li>
          <li><a href="#the-day">What do you do the day you notice something?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="contract">Layer one: the defects period in the contract</h2>
      <p>This is the one people mean when they say &ldquo;the warranty.&rdquo; It starts at practical completion, runs for the period in the contract schedule, and obliges the builder to return and rectify defects you report during it. Minor items that were listed on the defects document at handover are fixed in the same way.</p>
      <p>What's in it is between you and the contract. Read the length, read how a defect has to be reported (usually in writing), and read what's excluded &mdash; normal shrinkage cracking in the first months is often called out. It's a service commitment. The law's protection is longer.</p>

      <h2 class="h2" id="statutory">Layer two: the statutory warranties</h2>

      <blockquote class="proof">
        <p><b>&ldquo;Schedule 1B of the Act sets out statutory warranties which are deemed to be part of all regulated domestic building contracts, even if not stated in the contract. The warranty period is 6 years from completion, termination or cessation of the work for breaches resulting in structural defects; 1 year for all other breaches. Legal proceedings for any breach must be started within the warranty period or a further 6 months if the breach becomes apparent within the last 6 months of the warranty period.&rdquo;</b></p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023 (sections 19&ndash;29 of Schedule 1B). These apply even if your contract never mentions them.</cite>
      </blockquote>

      <p>The warranties cover things like the work being done with reasonable care and skill, in accordance with the plans and specifications, with suitable materials, and in compliance with the law. A contract can't sign them away.</p>

      <h2 class="h2" id="scheme">Layer three: the Home Warranty Scheme</h2>
      <p>The scheme is the QBCC's insurance for owners, and it has its own clocks:</p>
      <ul class="pts">
        <li><strong>Cover runs six years and six months</strong> from the earliest of the premium being paid, the contract being agreed, or work starting &mdash; and may be extended where the work takes longer than six months.</li>
        <li><strong>Structural defects:</strong> claim within three months after the day you first become aware of the defect, inside the cover period.</li>
        <li><strong>Non-structural defects:</strong> noticed within six months after substantial completion, and claimed within seven months after that day.</li>
      </ul>
      <p>Those windows are strict. The guide's own warning: strict timeframes apply for notifying the QBCC about defects. Noticing something and waiting to see if it gets worse can cost you the claim.</p>

      <h2 class="h2" id="structural">What counts as structural?</h2>
      <p>In broad terms, a defect that affects the building's structural integrity or its health and safety: footings and slabs, the frame, the roof structure, waterproofing that lets water into the structure, and the like. Cosmetic and finishing problems &mdash; paint, a door that binds, a cracked tile &mdash; are non-structural. The QBCC's rectification guidance draws the line in detail and the distinction decides which clock you're on, so if you're not sure, treat it as urgent and ask.</p>

      <h2 class="h2" id="the-day">What do you do the day you notice something?</h2>
      <ol>
        <li><strong>Photograph it, with the date.</strong></li>
        <li><strong>Write to the builder</strong> describing it, and keep the email. This is the first step in the guide's dispute process and it starts the contract's defects procedure.</li>
        <li><strong>Give a reasonable time to respond and fix.</strong> A good builder's answer is a date.</li>
        <li><strong>If nothing happens,</strong> the QBCC's free Early Dispute Resolution service is next, and a complaint about defective work can lead to a direction to rectify. Do it inside the windows above.</li>
      </ol>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>The contract's defects period is the shortest clock.</b> Read its length and its reporting rule.</li>
          <li><b>The statutory warranties are six years structural, one year for the rest,</b> in every contract whether written or not.</li>
          <li><b>The Home Warranty Scheme runs six years and six months</b> with strict claim windows: three months from awareness for structural, seven months from completion for non-structural.</li>
          <li><b>Structural or not decides which clock.</b> If unsure, act as if it's urgent.</li>
          <li><b>Photograph, write, give a date, then the QBCC.</b> In that order, inside the windows.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Are hairline cracks in the first year a defect?</p>
          <p>Some cracking as a new house dries and settles is normal and many contracts say so. Cracks that widen, step through brickwork, or come with doors that stop closing are a different matter. Report it in writing either way; it costs nothing and it dates the observation.</p>
        </div>
        <div>
          <p class="q">Does the defects period restart after a repair?</p>
          <p>Not usually under the contract. The statutory warranties and the scheme run from completion regardless. Check your contract's wording.</p>
        </div>
        <div>
          <p class="q">What if the builder has closed down?</p>
          <p>That's one of the situations the Home Warranty Scheme exists for. <a href="../what-happens-if-a-builder-goes-under-mid-build/">What happens if a builder goes under is here.</a></p>
        </div>
        <div>
          <p class="q">What's Sabre's defects period?</p>
          <p>It's in the contract, and Nathan will show you the clause and explain how to report something before you sign. Ask him what happens on day one after you ring.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/sites/default/files/2021-09/guide-qbcc-consumer-building-v3.pdf" rel="noopener">Consumer Building Guide</a> (version 3, effective July 2023) and <a href="https://www.qbcc.qld.gov.au/your-property/queensland-home-warranty-scheme/time-limits-cover-claims" rel="noopener">Time limits for cover and claims</a> (reviewed 23 September 2021); Schedule 1B, <em>Queensland Building and Construction Commission Act 1991</em>. Read 17 September 2026. Time limits are strict and can change; check the QBCC's current pages. This is a plain-English guide, not legal advice.</p>
''')

# ---------------------------------------------------------------- R39 · what's in the contract
POSTS["r39-contract-plain-english"] = dict(
    slug="whats-in-a-queensland-building-contract-in-plain-english",
    section="builder",
    title="What's in a Queensland building contract, in plain English?",
    h1="What's in a Queensland building contract,<br>in plain English?",
    description="The standard forms (QBCC, HIA, Master Builders) all have the same skeleton because Schedule 1B of the QBCC Act requires it: the schedule, the general conditions, the plans and specifications, and the clauses on price, dates, payments, variations, extensions, completion and defects. A walk through each part.",
    lede="A building contract lands on the table as a stack of paper an inch thick, and most of it is the same in every builder's version, because the law says what has to be in it. Once you know the skeleton, the inch gets a lot less frightening. Here's each part, what it does, and where the important numbers live.",
    date="2026-09-17", category="Dealing with a builder", image="blog/whats-in-a-queensland-building-contract-in-plain-english.jpg",
    image_alt="A thick building contract open on a kitchen table, a hand flipping to the first page of the schedule, glasses beside it",
    image_caption="Illustration.",
    label=("The skeleton every form shares", "The contract"),
    card_title="What's in a Queensland building contract, in plain English?",
    card_blurb="QBCC, HIA and Master Builders forms all share one skeleton because the law requires it: schedule, general conditions, plans and specs, and the clauses on price, dates, payments, variations, completion and defects.",
    about=["Building contract Queensland", "HIA contract", "Master Builders contract", "QBCC contract"],
    related=["what-questions-should-we-ask-a-builder-before-we-sign", "fixed-price-or-cost-plus-what-do-builders-mean", "progress-payments-what-you-pay-and-when-on-a-queensland-house-build"],
    cta="Bring the contract you've been handed to the walk-through, whoever it's from. Nathan will go through it with you, page by page.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Every Queensland domestic building contract of $20,000 or more &mdash; whether it's the QBCC's own form, the HIA's or Master Builders' &mdash; has four parts: the <strong>contract schedule</strong> (the front pages where your job's details and numbers go), the <strong>general conditions</strong> (the standard rules), any <strong>special conditions</strong> (changes agreed for your job), and the <strong>plans and specifications</strong> (what's actually being built).</p>
        <p>The law, Schedule 1B of the QBCC Act, requires certain things to be in there: the price shown prominently on the first page of the schedule if it's fixed, or the method for calculating it if not; a warning about anything that can change the price; the start date or how it's set; the date for practical completion or how it's calculated; the deposit and progress payments; and the rules on variations, extensions of time and completion.</p>
        <p>The QBCC's Consumer Building Guide, which the builder must give you before you sign, is the two-page key to the whole stack. Read the contract with it beside you.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#schedule">The schedule: where your numbers live</a></li>
          <li><a href="#conditions">The general conditions: the rules</a></li>
          <li><a href="#special">Special conditions: what's been changed</a></li>
          <li><a href="#plans">The plans and specifications: what you're buying</a></li>
          <li><a href="#clauses">The clauses to read twice</a></li>
          <li><a href="#before-signing">What has to happen before you sign?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="schedule">The schedule: where your numbers live</h2>
      <p>The first few pages. This is the part filled in for your job, and it's where almost everything you'll ever need to check is written:</p>
      <ul class="pts">
        <li><strong>The parties</strong> &mdash; you, and the licensed contractor with their QBCC licence number.</li>
        <li><strong>The site</strong> &mdash; your address and lot.</li>
        <li><strong>The contract price</strong>, shown prominently on the first page if fixed, with any allowances and provisional sums listed.</li>
        <li><strong>The deposit</strong> and the <strong>progress payment</strong> stages and amounts.</li>
        <li><strong>The start date</strong> (or how it's set) and the <strong>date for practical completion</strong> (or how it's calculated, such as a number of days from commencement).</li>
        <li><strong>Liquidated damages</strong>, if any, per week of lateness.</li>
        <li><strong>The defects liability period.</strong></li>
        <li><strong>Insurances</strong>, including the Home Warranty premium.</li>
      </ul>

      <blockquote class="proof">
        <p><b>&ldquo;For contracts priced at $20,000 or more, the contract price, if fixed, must be shown prominently on the first page of the contract schedule. If the contract price is not fixed, the method for calculating it, including any allowances, must be stated in the contract schedule.&rdquo;</b> The contract must also contain a warning about any provisions that may alter the price.</p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023 (section 2 of Schedule 1B). If the price isn't on the front page, ask why.</cite>
      </blockquote>

      <h2 class="h2" id="conditions">The general conditions: the rules</h2>
      <p>The thick part. These are the standard terms the form's publisher wrote, and they cover the same ground in every form because Schedule 1B sets the minimum: how variations work, how extensions of time are claimed, what practical completion means, how defects are reported, what happens if either side wants to end the contract, and how disputes are handled. They change little from job to job. What changes is the schedule and the special conditions.</p>

      <h2 class="h2" id="special">Special conditions: what's been changed</h2>
      <p>A short section, sometimes empty, where the parties agree to alter or add to the general conditions for this job. Read every word of it. A special condition can move risk from the builder to you &mdash; on site conditions, on delays, on who pays for what &mdash; and the QBCC's checklist asks you to confirm you've read the special conditions before signing. If one isn't clear, ask what it's for.</p>

      <h2 class="h2" id="plans">The plans and specifications: what you're buying</h2>
      <p>The drawings and the written specification are part of the contract, and they define the house. The specification lists the materials, the fittings, the finishes, the brands and the standards. If something isn't in the plans or the specification, it isn't in the price, and adding it later is a variation.</p>
      <p>This is the section families skim and shouldn't. The guide's words: do not sign before receiving the contract, plans and specifications. Read the specification against what you think you're getting.</p>

      <h2 class="h2" id="clauses">The clauses to read twice</h2>
      <ul class="pts">
        <li><strong>Allowances and provisional sums.</strong> Where the price can move. <a href="../fixed-price-or-cost-plus-what-do-builders-mean/">Why is here.</a></li>
        <li><strong>Deposit and progress payments.</strong> Against the legal caps and the work-on-site rule. <a href="../progress-payments-what-you-pay-and-when-on-a-queensland-house-build/">Here.</a></li>
        <li><strong>Variations.</strong> In writing, before the work. <a href="../variations-why-the-price-changed-and-when-it-shouldnt-have/">Here.</a></li>
        <li><strong>Extensions of time.</strong> The grounds, and how quickly you must respond to a claim.</li>
        <li><strong>Practical completion and defects.</strong> What it means, the defects document, the defects liability period. <a href="../what-is-a-defects-liability-period/">Here.</a></li>
        <li><strong>Termination.</strong> How and when either side can end it. The guide's warning: incorrect termination can have serious consequences and reduce your Home Warranty protection. Get advice before you use it.</li>
      </ul>

      <h2 class="h2" id="before-signing">What has to happen before you sign?</h2>
      <ol>
        <li>The builder gives you the <strong>Consumer Building Guide</strong> (required for contracts at or over $20,000).</li>
        <li>You receive the <strong>full contract, plans and specifications</strong>.</li>
        <li>You check the <strong>licence</strong> on the QBCC register.</li>
        <li>You sign, and within 5 business days the builder gives you the signed copy.</li>
        <li>Your <strong>cooling-off period</strong> of five business days runs from the day you receive both the signed contract and the guide. Withdrawing costs, in the guide's words, generally $100 plus the contractor's reasonable out-of-pocket expenses.</li>
      </ol>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Four parts: schedule, general conditions, special conditions, plans and specifications.</b> Every form.</li>
          <li><b>Your numbers are in the schedule:</b> price, allowances, deposit, stages, dates, damages, defects period.</li>
          <li><b>Read every special condition.</b> That's where risk gets moved.</li>
          <li><b>If it isn't in the plans and specification, it isn't in the price.</b></li>
          <li><b>Guide, full documents, licence check, then sign.</b> Five business days to change your mind.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Does it matter which form the builder uses?</p>
          <p>Less than people think. QBCC, HIA and Master Builders forms all have to comply with Schedule 1B. The differences are in the general conditions and are worth reading, but the schedule and the specification are where your job actually lives.</p>
        </div>
        <div>
          <p class="q">Can we change the general conditions?</p>
          <p>Through special conditions, by agreement. Be careful in both directions: a change that helps you can be reasonable; a change that shifts risk to you deserves a question and sometimes a solicitor.</p>
        </div>
        <div>
          <p class="q">What if the plans change after we sign?</p>
          <p>That's a variation, in writing, before the work. The contract's plans are the contract's plans until both of you agree to alter them.</p>
        </div>
        <div>
          <p class="q">Which form does Sabre use?</p>
          <p>Ask Nathan and he'll show you the actual document, blank, before you've committed to anything. Read it at home with the guide beside it.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/sites/default/files/2021-09/guide-qbcc-consumer-building-v3.pdf" rel="noopener">Consumer Building Guide</a> (version 3, effective July 2023) and <em>Domestic building contracts</em> (reviewed 26 June 2024); Schedule 1B, <em>Queensland Building and Construction Commission Act 1991</em>. Read 17 September 2026. This is a plain-English guide, not legal advice; a solicitor reads contracts for a living and the guide suggests one if you still have concerns.</p>
''')
