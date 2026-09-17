# Phase 5, part E — Spiral 3 (dealing with a builder), last six: R40, R41, R42, R43, R44, R45.
# Sources read 2026-09-17:
#   QBCC — "Home warranty for non-completion claims" (reviewed 25 Oct 2021): available where a fixed-price contract ends because of valid
#     termination for contractor default, contractor death, company deregistration, or the contractor is insolvent AND the QBCC has cancelled
#     the licence; claim within 3 months of the contract ending; contract must end within 2 years of the contract date / work start; pays the
#     deposit back if no work started, otherwise the difference between the unpaid contract balance and the reasonable cost to complete;
#     payment reduced if the owner paid more than the maximum deposit or ahead of the contract; cost-plus contracts excluded
#   QBCC — "About owner-building" (reviewed 7 May 2024): permit needed over $11,000; owner-builder course; you become the head contractor;
#     licensed trades still required for restricted work; owner-builders are not eligible for Home Warranty insurance; one permit per 6 years;
#     a notice sits on the title for 7 years; selling within 6 years of completion requires written disclosure to the buyer with the statutory
#     warning that the work is not covered by insurance under the QBCC Act
#   Queensland Building Regulation 2021 / Department guideline for inspection of class 1a buildings: mandatory stages — excavation, footings,
#     slab, frame, final (certificates such as termite protection, wet-area membranes, glazing, smoke alarms, energy efficiency at final)
#   QBCC — Consumer Building Guide v3: building approvals and inspections (certifier engaged by you or, more commonly, the builder; copies of
#     certificates of inspection as soon as practicable; certifier must give inspection documents within 5 business days of a written request;
#     the owner can ask for additional certifying functions at the owner's expense); contract price and allowances; deposits and progress payments
# Rule 1: no prices, no bands, no timelines beyond the statutory ones quoted. R44 is the SHAPE of a loan only — no product, no rate, no advice.

POSTS = {}

# ---------------------------------------------------------------- R40 · builder goes under
POSTS["r40-builder-goes-under"] = dict(
    slug="what-happens-if-a-builder-goes-under-mid-build",
    section="builder",
    title="What happens if a builder goes under mid-build?",
    h1="What happens if a builder<br>goes under mid-build?",
    description="The fear behind every other question, answered straight: the Queensland Home Warranty Scheme's non-completion cover, when it applies, the three-month claim window, what it pays, and the two things that shrink it &mdash; paying ahead of the contract, and a cost-plus contract.",
    lede="It's the question nobody asks the builder to their face and everybody asks the internet at midnight. In Queensland the answer is better than most states, because there's a scheme built for exactly this. It has conditions, it has a clock, and there are two ways to weaken it before you ever need it. Here's the whole thing, in the QBCC's words.",
    date="2026-09-17", category="Dealing with a builder", image="blog/what-happens-if-a-builder-goes-under-mid-build.jpg",
    image_alt="A house stopped at frame stage, the site fence padlocked, weeds coming up through the slab, a quiet Bayside street",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real job.",
    label=("The fear behind every question", "If the builder goes under"),
    card_title="What happens if a builder goes under mid-build?",
    card_blurb="The Home Warranty Scheme's non-completion cover: when it applies, the three-month window, what it pays, and the two things that shrink it before you ever need it.",
    about=["Builder insolvency", "Queensland Home Warranty Scheme", "Non-completion claim", "QBCC"],
    related=["what-insurance-should-a-builder-have-and-what-does-it-cover-you-for", "progress-payments-what-you-pay-and-when-on-a-queensland-house-build", "what-is-the-qbcc-and-what-to-check-on-a-builders-licence"],
    cta="Ask Nathan the uncomfortable question at the walk-through. The right answer includes the licence history, the payment schedule and the Notice of Cover, and he'll give you all three.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>If a licensed builder on a fixed-price contract can't finish your house, the <strong>Queensland Home Warranty Scheme</strong> can pay to get it finished. The QBCC lists when a non-completion claim is available: the contract has validly ended because of the contractor's default, the contractor has died, the company has been deregistered, or the contractor is insolvent <em>and</em> the QBCC has cancelled their licence.</p>
        <p>The clock is strict: the claim must be lodged within three months of the contract ending, and the contract itself has to have ended within two years of the contract date or the start of work. If no work started, the scheme refunds the deposit up to the legal maximum. If work started, it pays the difference between what's left unpaid under your contract and the reasonable cost of finishing, within the scheme's limits, plus limited amounts for accommodation and for storm or fire damage to the incomplete work.</p>
        <p>Two things shrink it before you ever need it: paying more than the contract allowed, or earlier than it required &mdash; the payout is reduced by that amount &mdash; and signing a cost-plus contract, where non-completion cover isn't available at all.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#when">When does the non-completion cover apply?</a></li>
          <li><a href="#clock">What's the clock?</a></li>
          <li><a href="#what-it-pays">What does it pay?</a></li>
          <li><a href="#shrink">What shrinks it?</a></li>
          <li><a href="#signs">What are the warning signs before it happens?</a></li>
          <li><a href="#the-day">What do you do on the day?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="when">When does the non-completion cover apply?</h2>
      <p>The QBCC's own list, for a fixed-price contract with a licensed contractor:</p>
      <ul class="pts">
        <li>The contract has been <strong>validly terminated</strong> because of the contractor's default.</li>
        <li>The <strong>contractor has died</strong>.</li>
        <li>The contracting <strong>company has been deregistered</strong>.</li>
        <li>The contractor is <strong>insolvent and</strong> the QBCC has <strong>cancelled their licence</strong>.</li>
      </ul>
      <p>Note the word <em>validly</em>. The Consumer Building Guide warns that incorrect termination may have serious legal and financial consequences and reduce your protection under the scheme. If a builder stops turning up, the way you end the contract matters. Get advice before you send the letter.</p>

      <h2 class="h2" id="clock">What's the clock?</h2>

      <blockquote class="proof">
        <p><b>The claim must be lodged &ldquo;within 3 months from the date the contract ends,&rdquo; and the contract itself must end within two years of the contract date or the date work started.</b></p>
        <cite>Queensland Building and Construction Commission, <em>Home warranty for non-completion claims</em>. Three months is not long when a family is dealing with a stalled house. Start the paperwork the week the contract ends.</cite>
      </blockquote>

      <h2 class="h2" id="what-it-pays">What does it pay?</h2>
      <ul class="pts">
        <li><strong>If no work began:</strong> your deposit back, up to the maximum the law allowed the builder to take.</li>
        <li><strong>If work began:</strong> the difference between the unpaid balance of your contract and the reasonable cost of completing the work, within the scheme's maximum. In plain words: the scheme is there to get you to the house you contracted for, not to hand over cash.</li>
        <li><strong>Extras:</strong> a capped amount for alternative accommodation (higher if optional additional cover was taken), and cover up to a stated limit for fire or storm damage to the incomplete work, and for vandalism or theft with an excess per incident.</li>
      </ul>
      <p>The current caps are on the QBCC's page and change from time to time; read the live figures rather than a blog.</p>

      <h2 class="h2" id="shrink">What shrinks it?</h2>
      <p>Two things, both within your control on the day you sign.</p>
      <p><strong>Paying ahead.</strong> The QBCC says the payment is reduced if you paid more than the maximum deposit required by law, or paid ahead of schedule under the contract. The scheme assumes you paid as the contract said. If you paid the frame stage before the frame was up, that money is yours to lose. <a href="../progress-payments-what-you-pay-and-when-on-a-queensland-house-build/">The payment rules are here.</a></p>
      <p><strong>A cost-plus contract.</strong> Protection for non-completion under the scheme is not available on cost-plus or construction management contracts. The regulator says so on its own pages, and it's the biggest single reason to be wary of them. <a href="../fixed-price-or-cost-plus-what-do-builders-mean/">Why is here.</a></p>

      <h2 class="h2" id="signs">What are the warning signs before it happens?</h2>
      <ul class="pts">
        <li><strong>The licence.</strong> The QBCC register shows status and history. A suspension, or conditions, is a flag before you sign. Check it again if the job goes quiet.</li>
        <li><strong>Requests to pay early or outside the contract.</strong> The QBCC has published a public warning about exactly this. A builder asking for the next stage before the stage is done is a builder with a cash problem.</li>
        <li><strong>Trades disappearing.</strong> Subcontractors who stop coming are often subcontractors who haven't been paid.</li>
        <li><strong>Silence.</strong> A builder who stops answering the phone is telling you something. Write to them, dated, so the record starts.</li>
      </ul>

      <h2 class="h2" id="the-day">What do you do on the day?</h2>
      <ol>
        <li><strong>Don't pay anything further.</strong></li>
        <li><strong>Write to the builder</strong> asking for their position in writing, with a reasonable time to respond.</li>
        <li><strong>Call the QBCC</strong> (139 333) and describe the situation. Ask about the non-completion process and the licence status.</li>
        <li><strong>Get legal advice before terminating.</strong> The guide says so twice, and the validity of the termination decides the claim.</li>
        <li><strong>Lodge the claim within three months</strong> of the contract ending, with your contract, your payment records and your Notice of Cover.</li>
      </ol>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>The Home Warranty Scheme covers non-completion</b> on a fixed-price contract with a licensed builder, in the situations the QBCC lists.</li>
          <li><b>Three months from the contract ending to lodge.</b> The contract must end within two years.</li>
          <li><b>It pays to finish the house,</b> not to hand over cash, within the scheme's caps.</li>
          <li><b>Paying ahead shrinks the payout. Cost-plus removes it.</b> Both are decided the day you sign.</li>
          <li><b>Terminate correctly, with advice.</b> An invalid termination can cost you the claim.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Does the scheme pay for the defects in the work the failed builder did?</p>
          <p>Defective work is a separate head of cover with its own time limits. The non-completion claim deals with finishing; a defects claim deals with fixing. <a href="../what-is-a-defects-liability-period/">The defects clocks are here.</a></p>
        </div>
        <div>
          <p class="q">Can we just hire another builder and keep going?</p>
          <p>Talk to the QBCC first. The scheme's process involves assessing the work and the cost to complete, and moving ahead without it can affect the claim. It's a phone call before it's a decision.</p>
        </div>
        <div>
          <p class="q">What if we signed a cost-plus contract?</p>
          <p>Then the non-completion cover isn't available, and your options are legal ones. The regulator's warning about cost-plus exists for this moment. Get advice.</p>
        </div>
        <div>
          <p class="q">How do we check a builder's history before it gets to this?</p>
          <p>The QBCC's online licence search shows the class, the status and the history for any licence number. <a href="../what-is-the-qbcc-and-what-to-check-on-a-builders-licence/">How to read it is here.</a> Ours is 15486557.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/complaints-disputes/building-work-issue/non-completion-building-work/home-warranty-non-completion" rel="noopener">Home warranty for non-completion claims</a> (reviewed 25 October 2021), <em>Time limits for cover and claims</em>, <em>Contracts and agreement types</em> (reviewed 27 June 2025), <em>Warning about making payments outside of building contract terms</em>, and the <a href="https://www.qbcc.qld.gov.au/sites/default/files/2021-09/guide-qbcc-consumer-building-v3.pdf" rel="noopener">Consumer Building Guide</a> (version 3). Read 17 September 2026. Caps and conditions change; read the QBCC's current page before relying on any of this. Not legal advice.</p>
''')

# ---------------------------------------------------------------- R41 · owner-builder
POSTS["r41-owner-builder"] = dict(
    slug="should-we-be-an-owner-builder",
    section="builder",
    title="Should we be an owner-builder in Queensland?",
    h1="Should we be an owner-builder<br>in Queensland?",
    description="Maybe, and here's the honest version from a builder who'd lose the job. What an owner-builder permit is (needed over $11,000), the course, what you take on, why the Home Warranty Scheme doesn't cover you, and the six-year rule that follows the house when you sell.",
    lede="Being your own builder sounds like the way to save the margin. Sometimes it is. It's also a legal role with a permit, a course, a list of responsibilities that are yours the moment you sign the form, and a warning that travels with the house for six years if you sell. Here's what the QBCC says it involves, so the decision is an informed one.",
    date="2026-09-17", category="Dealing with a builder", image="blog/should-we-be-an-owner-builder.jpg",
    image_alt="A homeowner in a hi-vis vest seen from behind, standing alone on a slab with a clipboard, a delivery of frames beside them",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real person.",
    label=("The honest version", "Owner-builder?"),
    card_title="Should we be an owner-builder in Queensland?",
    card_blurb="Maybe, and here's the honest version from a builder who'd lose the job. The permit, the course, what you take on, why Home Warranty doesn't cover you, and the six-year rule when you sell.",
    about=["Owner-builder Queensland", "Owner-builder permit", "QBCC", "Home Warranty Scheme"],
    related=["what-is-the-qbcc-and-what-to-check-on-a-builders-licence", "what-insurance-should-a-builder-have-and-what-does-it-cover-you-for", "how-do-progress-inspections-and-certifiers-work-in-queensland"],
    cta="If you're weighing it up, tell Nathan. He'll tell you honestly which parts of a rebuild an owner-builder can run and which ones bite.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>An owner-builder is a property owner who takes the builder's legal role on their own home. In Queensland you need an <strong>owner-builder permit</strong> from the QBCC for work worth more than $11,000, and most applicants must complete an owner-builder course first. With the permit, you become the head contractor: you engage and coordinate every trade, obtain the approvals and inspections, meet the safety obligations, use licensed contractors for restricted work like plumbing and electrical, and rectify any defective work.</p>
        <p>Two consequences decide most cases. <strong>Owner-builders are not eligible for the Queensland Home Warranty Scheme</strong>, so there's no cover for non-completion or defects. And if you <strong>sell within six years</strong> of completion, you must tell the buyer in writing that the work isn't covered by insurance under the QBCC Act; a notice sits on the title for seven years.</p>
        <p>It can be right for a capable person with time, on a simple job. On a knockdown rebuild with asbestos, a flood level and a sloping block, it's a full-time job with your own money as the safety net.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#what-it-is">What is an owner-builder, legally?</a></li>
          <li><a href="#the-permit">What does the permit involve?</a></li>
          <li><a href="#you-take-on">What do you take on?</a></li>
          <li><a href="#no-warranty">Why does the Home Warranty Scheme not apply?</a></li>
          <li><a href="#selling">What happens when you sell?</a></li>
          <li><a href="#when-it-works">When does it make sense?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="what-it-is">What is an owner-builder, legally?</h2>
      <p>Someone who carries out, or manages, building work on their own land without holding a QBCC contractor's licence, under a permit instead. The QBCC's eligibility: you must be an owner named on the title, a director of the company that owns it, or an occupier with the owner's written consent.</p>
      <p>The key word is <em>manages</em>. Most owner-builders don't swing the hammer. They hire the trades and run the job, which is the part a licensed builder is licensed for.</p>

      <h2 class="h2" id="the-permit">What does the permit involve?</h2>
      <ul class="pts">
        <li><strong>The threshold.</strong> A permit is required if the project is worth more than $11,000 (a higher threshold applies to farm buildings).</li>
        <li><strong>The course.</strong> Most applicants must complete an owner-builder course, or hold an exemption (current QBCC licensees and certain professionals).</li>
        <li><strong>The frequency.</strong> The QBCC issues one permit per six years, with exemptions possible in some circumstances.</li>
        <li><strong>The record.</strong> An administrative notice attaches to the property title and stays there for seven years.</li>
      </ul>

      <h2 class="h2" id="you-take-on">What do you take on?</h2>
      <p>The QBCC's list, in its words, is that you become the head contractor and must:</p>
      <ul class="pts">
        <li>Engage and coordinate all contractors.</li>
        <li>Obtain the necessary building approvals and inspections.</li>
        <li>Ensure compliance with safety standards on site.</li>
        <li>Use licensed trades for restricted work &mdash; plumbing, gas fitting and the like.</li>
        <li>Rectify any defective work.</li>
      </ul>
      <p>Add to that what a builder does that doesn't appear on any list: sequencing forty trades so none of them waits on another, buying materials at the right time, reading the certifier's requirements, and being the one who answers when the concrete truck is at the gate and the pump hasn't arrived.</p>

      <h2 class="h2" id="no-warranty">Why does the Home Warranty Scheme not apply?</h2>

      <blockquote class="proof">
        <p><b>&ldquo;Owner-builders are not eligible for insurance through the Queensland Home Warranty Scheme.&rdquo;</b></p>
        <cite>Queensland Building and Construction Commission, <em>About owner-building</em>, reviewed 7 May 2024. The scheme insures work done by licensed contractors. An owner-builder is neither, and nobody underwrites the gap.</cite>
      </blockquote>

      <p>In practice that means there's no cover if a trade walks off, no cover for defects in the work you managed, and no scheme to help finish if you can't. Your individual licensed trades carry their own obligations for their own work, but the house as a whole is yours.</p>

      <h2 class="h2" id="selling">What happens when you sell?</h2>
      <p>If you sell within six years of completing the work, you must give the buyer a written notice that includes the statutory warning that the building work is not covered by insurance under the QBCC Act. Buyers, and their solicitors, read that, and it tends to show up in the price. The notice on the title makes it hard to miss.</p>

      <h2 class="h2" id="when-it-works">When does it make sense?</h2>
      <p>Honestly: for a person with building or project experience, time to be on site most days, a simple job on a straightforward block, and the financial room to carry the risk the scheme would otherwise carry. A shed, a straightforward extension, a small lowset on a flat clear lot.</p>
      <p>A knockdown rebuild on the Bayside is usually not that. It has licensed asbestos removal, demolition, disconnections, a flood level, a soil test with a letter on it, a two-storey frame, and a certifier who wants the right certificate at every stage. That's the job a builder's licence is for, and the one where the margin you'd save is also the thing standing between you and the risk.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Permit over $11,000, course first, one permit per six years,</b> notice on the title for seven.</li>
          <li><b>You become the head contractor:</b> trades, approvals, inspections, safety, rectification.</li>
          <li><b>No Home Warranty Scheme cover.</b> Non-completion and defects are on you.</li>
          <li><b>Sell within six years and the buyer gets a written warning.</b></li>
          <li><b>Right for a simple job and a capable person with time.</b> A Bayside rebuild usually isn't that job.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Can we owner-build and still hire a builder for the hard parts?</p>
          <p>You can engage licensed contractors for any part; that's what an owner-builder does. What you can't do is hand the head-contractor role to someone else while holding the permit. If a builder is running the whole job, they should be the licensed contractor on a contract, with the scheme cover that brings.</p>
        </div>
        <div>
          <p class="q">Is the course hard?</p>
          <p>It's an approved course covering the responsibilities above. Passing it makes you eligible for the permit; it doesn't make you a builder. The QBCC publishes the list of course providers.</p>
        </div>
        <div>
          <p class="q">Do we save the builder's margin?</p>
          <p>You avoid paying it. Whether you save it depends on what your time is worth, what the trades charge someone who isn't a repeat customer, what you buy wrong, and what the scheme would have covered. Nobody can put a number on that for you, and we won't.</p>
        </div>
        <div>
          <p class="q">Will Sabre quote for part of an owner-built job?</p>
          <p>Ask. Some parts of a job are sensible to contract out as their own licensed job. Nathan will tell you which, and he'll also tell you if he thinks the whole thing should be one contract.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/home-owner-hub/owner-build/about-owner-building" rel="noopener">About owner-building</a> (reviewed 7 May 2024), <em>Apply for an owner-builder permit</em> and <em>Sell an owner-builder property</em>. Read 17 September 2026. Thresholds and rules change; check the QBCC's current pages. This is a plain-English guide, not legal or financial advice.</p>
''')

# ---------------------------------------------------------------- R42 · inspections and certifiers
POSTS["r42-certifiers"] = dict(
    slug="how-do-progress-inspections-and-certifiers-work-in-queensland",
    section="builder",
    title="How do progress inspections and certifiers work in Queensland?",
    h1="How do progress inspections and<br>certifiers work in Queensland?",
    description="A private building certifier approves the plans and inspects the house at the mandatory stages: excavation, footings, slab, frame and final. Who engages them, what each stage checks, what a certificate of inspection is, and the rights you have to see the paperwork.",
    lede="Somewhere between the plans and the keys, a person you've probably never met signs off your house five times. That's the building certifier, and the stages they inspect are set by regulation, not by the builder. Here's who they are, what they look at, and the paperwork you're entitled to along the way.",
    date="2026-09-17", category="Dealing with a builder", image="blog/how-do-progress-inspections-and-certifiers-work-in-queensland.jpg",
    image_alt="A certifier in a white shirt and hard hat seen from behind, checking a timber frame with a clipboard, the roof trusses above",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real person.",
    label=("Five sign-offs", "The certifier"),
    card_title="How do progress inspections and certifiers work in Queensland?",
    card_blurb="A private building certifier approves the plans and inspects at the mandatory stages: excavation, footings, slab, frame and final. Who engages them, what each stage checks, and the paperwork you can ask for.",
    about=["Building certifier", "Mandatory inspections Queensland", "Building Regulation 2021", "Certificate of inspection"],
    related=["does-a-knockdown-rebuild-need-a-development-application", "progress-payments-what-you-pay-and-when-on-a-queensland-house-build", "what-is-a-defects-liability-period"],
    cta="Ask Nathan who Sabre's certifier is and to see the inspection certificates as they come in. He'll send them without being asked.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>A <strong>building certifier</strong> is a licensed private professional (licensed by the QBCC) who issues the building approval for your house and inspects it at the stages the regulation makes mandatory. For a new detached house those stages are: <strong>excavation</strong> (after digging, before concrete), <strong>footings</strong> (formwork and steel in place, before the pour), <strong>slab</strong> (same, for the slab), <strong>frame</strong>, and <strong>final</strong>, where the certifier checks the outstanding items and collects the certificates for things like termite protection, wet-area waterproofing, glazing, smoke alarms and energy efficiency.</p>
        <p>The certifier can be engaged by you or, more commonly, by your builder. Either way, the builder must give you copies of any certificates of inspection as soon as practicable after receiving them, and you can ask the certifier in writing for inspection documents, which they must provide within five business days.</p>
        <p>The certifier is the independent check that the house you're paying for is being built to the approved plans and the code. It isn't a quality inspection of the finishes. That's your handover walk.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#who">Who is the certifier, and who engages them?</a></li>
          <li><a href="#stages">What are the mandatory stages?</a></li>
          <li><a href="#what-they-check">What does each stage actually check?</a></li>
          <li><a href="#paperwork">What paperwork are you entitled to?</a></li>
          <li><a href="#not-quality">What the certifier doesn't do</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="who">Who is the certifier, and who engages them?</h2>
      <p>Since private certification came in, most house approvals in Queensland are issued by private building certifiers rather than council. The certifier assesses your plans against the Building Code of Australia and the Queensland Development Code, issues the building approval, carries out the mandatory inspections, and issues the final certificate.</p>

      <blockquote class="proof">
        <p><b>&ldquo;Building approvals and inspections are the responsibility of a building certifier who may be engaged by you or, more commonly, your builder. Mandatory building inspections may be required at certain stages of construction.&rdquo;</b> You can check a certifier's licence via the QBCC's online licence search.</p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023. The certifier is licensed and searchable, like the builder.</cite>
      </blockquote>

      <h2 class="h2" id="stages">What are the mandatory stages?</h2>
      <p>The Building Regulation sets them for a single detached house (a class 1a building):</p>
      <ul class="pts">
        <li><strong>Excavation</strong> &mdash; after the foundation material is excavated and before concrete for the footings or slab.</li>
        <li><strong>Footings</strong> &mdash; if the house has footings, after the formwork and reinforcement are placed and before the concrete is poured.</li>
        <li><strong>Slab</strong> &mdash; if the house has a slab, after the formwork and reinforcement are placed and before the pour.</li>
        <li><strong>Frame</strong> &mdash; the structural frame, before it's covered.</li>
        <li><strong>Final</strong> &mdash; outstanding items, and the collection of certificates such as termite protection, wet-area membranes, glazing, smoke alarms and energy efficiency.</li>
      </ul>
      <p>On a highset on posts, the &ldquo;footings&rdquo; and &ldquo;frame&rdquo; stages cover the posts, bearers and floor frame in the same way. The principle is the same: the structure is checked before it's hidden.</p>

      <h2 class="h2" id="what-they-check">What does each stage actually check?</h2>
      <ul class="pts">
        <li><strong>Excavation, footings and slab:</strong> that the ground and the footings match the engineer's design for the soil class, the reinforcement is the right size in the right place, the membrane and termite management are in, and the levels are right. <a href="../what-is-a-soil-test-and-why-does-it-change-the-price/">Why the soil class matters is here.</a></li>
        <li><strong>Frame:</strong> that the timber or steel frame matches the approved plans and the engineer's details: sizes, bracing, tie-downs for wind, lintels over openings. This is the one that decides whether the house stands up in a storm.</li>
        <li><strong>Final:</strong> that the house is complete to the approval, and that the required certificates exist from the trades who did that work. When the final certificate issues, the house can be lawfully occupied.</li>
      </ul>
      <p>A builder can't lawfully pour a slab or cover a frame until the stage has been inspected and passed. That sequence is what protects you.</p>

      <h2 class="h2" id="paperwork">What paperwork are you entitled to?</h2>
      <ul class="pts">
        <li><strong>Copies of certificates of inspection</strong>, from the builder, as soon as practicable after they receive them from the certifier.</li>
        <li><strong>Inspection documentation from the certifier</strong>, on written request, within five business days.</li>
        <li><strong>Additional inspections.</strong> If your builder engaged the certifier, you can still ask, via a notice to the builder, for the certifier to perform additional certifying functions at your expense.</li>
        <li><strong>The final certificate</strong> at the end, which you'll want for your own records and for any future sale.</li>
      </ul>
      <p>The practical use: a progress payment claim for the frame should come with a frame inspection certificate. If it doesn't, ask.</p>

      <h2 class="h2" id="not-quality">What the certifier doesn't do</h2>
      <p>The certifier checks compliance with the approval and the code. They don't check whether the paint is even, the tiles are straight or the door handles are the ones you chose. That's the handover inspection you do with the builder, and the defects document that comes out of it. If you want an independent eye on quality, a private building inspector at lock-up or before handover is a separate service you engage yourself.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>The certifier approves the plans and inspects at five mandatory stages:</b> excavation, footings, slab, frame, final.</li>
          <li><b>Usually engaged by the builder, licensed by the QBCC,</b> and searchable on the register.</li>
          <li><b>Nothing is poured or covered until its stage passes.</b> That sequence is the protection.</li>
          <li><b>You're entitled to the certificates:</b> from the builder as they come, from the certifier within five business days of asking.</li>
          <li><b>Compliance, not finish quality.</b> The handover walk and the defects document cover the rest.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Can we choose our own certifier?</p>
          <p>Yes. The guide says the certifier may be engaged by you or by the builder. Most families let the builder engage one they work with regularly; if you'd rather engage your own, say so before the approval is lodged.</p>
        </div>
        <div>
          <p class="q">Does council inspect anything?</p>
          <p>Council issues planning approvals where a development application is needed, and may be involved with plumbing and drainage inspections. The building inspections at the stages above are the certifier's.</p>
        </div>
        <div>
          <p class="q">What if a stage fails?</p>
          <p>The certifier issues a notice of what has to be fixed, the builder fixes it, and the stage is re-inspected. It's normal and it's the system working. Ask to see the paperwork either way.</p>
        </div>
        <div>
          <p class="q">Who engages Sabre's certifier?</p>
          <p>Ask Nathan. He'll tell you who they are, and the inspection certificates will come to you as they're issued, with the progress claims they support.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/sites/default/files/2021-09/guide-qbcc-consumer-building-v3.pdf" rel="noopener">Consumer Building Guide</a> (version 3, effective July 2023, on building approvals and inspections under the <em>Building Act 1975</em>); Queensland <em>Building Regulation 2021</em> and the Department of Housing's <em>Guidelines for inspection of class 1a and 10 buildings and structures</em> (mandatory stages). Read 17 September 2026. This is a plain-English guide, not legal advice.</p>
''')

# ---------------------------------------------------------------- R43 · building and pest on a knockdown
POSTS["r43-building-and-pest"] = dict(
    slug="what-is-a-building-and-pest-inspection-worth-on-a-house-you-plan-to-knock-down",
    section="builder",
    title="What is a building and pest inspection worth on a house you plan to knock down?",
    h1="What is a building and pest inspection<br>worth on a house you plan to knock down?",
    description="Less than you'd think for the house, more than you'd think for the block. What a standard inspection is written for, what it tells a family who's demolishing anyway, and the four checks that matter more: the year, the overlay, the flood report and the ground.",
    lede="You're buying a house to knock it down, and the contract has the usual building and pest condition in it. Do you bother? Yes, but not for the reason the inspector thinks. Here's what a standard report is for, what it tells you when the house is coming down regardless, and what to spend the money on instead.",
    date="2026-09-17", category="Dealing with a builder", image="blog/what-is-a-building-and-pest-inspection-worth-on-a-house-you-plan-to-knock-down.jpg",
    image_alt="An inspector's torch beam under an old highset, lighting up the stumps and the bearers, a moisture meter in hand",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real house.",
    label=("The house or the block?", "Building and pest"),
    card_title="What is a building and pest inspection worth on a house you plan to knock down?",
    card_blurb="Less than you'd think for the house, more for the block. What a standard inspection is written for, what it tells a family who's demolishing anyway, and the four checks that matter more.",
    about=["Building and pest inspection", "Buying to knock down", "Termites Queensland", "Knockdown rebuild"],
    related=["buying-an-old-house-in-wynnum-or-manly-to-knock-down-what-to-check-before-you-sign", "what-asbestos-removal-means-for-a-knockdown-rebuild", "what-is-a-soil-test-and-why-does-it-change-the-price"],
    cta="If you're buying to knock down, tell Nathan before the inspection is booked. He'll tell you what to ask the inspector to look at, and what to skip.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>A standard building and pest inspection is written for a buyer who's going to live in the house. It reports on the condition of the building &mdash; the roof, the frame, the wet areas, the termite activity, the things that would cost money to fix. If the house is coming down, almost none of that matters, and paying to learn the bathroom leaks is paying for a fact you'll bulldoze.</p>
        <p>What matters to a knockdown buyer is the block and the demolition: whether the house can legally come down (the year and the character overlay), what's in it (asbestos), what's under it (the ground, old fill, a septic, cracked slabs that hint at reactive clay), and the trees. Some of that an inspector can look at if you ask. Most of it comes from council's maps and reports, free, and from a builder on the block.</p>
        <p>So keep the inspection condition in the contract (it's your right to walk away), but tell the inspector what you're actually buying, and spend the real effort on the four checks below.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#what-it-is">What is a standard inspection for?</a></li>
          <li><a href="#what-it-tells">What does it still tell a knockdown buyer?</a></li>
          <li><a href="#what-matters">The four checks that matter more</a></li>
          <li><a href="#the-condition">Should the contract still have the inspection condition?</a></li>
          <li><a href="#if-renovating">What if you might keep the house after all?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="what-it-is">What is a standard inspection for?</h2>
      <p>Two reports, usually done on the same visit. The <strong>building inspection</strong> is a visual assessment of the accessible parts of the house: roof, exterior, interior, subfloor, wet areas, with defects graded and safety hazards flagged. The <strong>pest inspection</strong> looks for evidence of termites and other timber pests, active or past, and the conditions that invite them.</p>
      <p>Both are written for someone who's going to own and live in the building. They tell you what it would cost to keep it. That's a different question from what it will cost to remove it.</p>

      <h2 class="h2" id="what-it-tells">What does it still tell a knockdown buyer?</h2>
      <p>A few useful things, if you read it for the block rather than the house:</p>
      <ul class="pts">
        <li><strong>Cracking, movement and moisture in the subfloor.</strong> Cracked slabs, stumps that have moved, doors out of square. Hints of reactive clay or fill under the house, which the soil test will later confirm. <a href="../what-is-a-soil-test-and-why-does-it-change-the-price/">Why that matters is here.</a></li>
        <li><strong>Termite activity in the ground.</strong> Active nests on the block are a fact for the new house's termite management, not just the old one's.</li>
        <li><strong>Drainage and where the water goes.</strong> Damp under the house tells you about the block.</li>
        <li><strong>The built-in-under and the sheds.</strong> Sometimes an inspector notes suspected asbestos materials. That's not an asbestos audit, but it's a flag.</li>
      </ul>

      <h2 class="h2" id="what-matters">The four checks that matter more</h2>
      <ol>
        <li><strong>The year and the character overlay.</strong> If the house is pre-1947 and the street is in the overlay, demolition needs a development application and council may refuse it. Nothing an inspector writes changes that. <a href="../can-we-knock-down-our-house/">The rules are here.</a></li>
        <li><strong>The flood report.</strong> Council's FloodWise report on the lot sets the minimum floor level for the new house. Free, and it decides what you can build. <a href="../rebuilding-on-a-flood-overlay-block-on-the-bayside/">Here.</a></li>
        <li><strong>Asbestos.</strong> Any Bayside house built before 1990 likely has it somewhere. A licensed asbestos assessor can do an audit if you want the scope before you sign; otherwise, budget for licensed removal as a certainty. <a href="../what-asbestos-removal-means-for-a-knockdown-rebuild/">Here.</a></li>
        <li><strong>The trees and the ground.</strong> Council's protected vegetation report for the trees; a walk under the house and around the block for the ground, with the soil test after settlement.</li>
      </ol>
      <p><a href="../buying-an-old-house-in-wynnum-or-manly-to-knock-down-what-to-check-before-you-sign/">The full eight-point list for buying to knock down is here.</a></p>

      <h2 class="h2" id="the-condition">Should the contract still have the inspection condition?</h2>
      <p>Yes, and that's a conversation with your solicitor rather than us. The condition gives you a way out if the inspection turns up something you can't live with, and there's no reason to give that up. What you can do is tell the inspector what you're buying and ask them to spend their time on the subfloor, the ground, the trees and the outbuildings, and to note suspected asbestos materials. A good inspector will adjust.</p>

      <h2 class="h2" id="if-renovating">What if you might keep the house after all?</h2>
      <p>Then the standard report earns its money, because now you're deciding between renovating and rebuilding and you need to know what the house is worth keeping. A pre-1947 house in the overlay is exactly this case: the inspection tells you what the bones are like, and the bones decide the path. <a href="../knockdown-rebuild-or-renovate-how-to-tell-which-one-your-house-is/">How to decide is here.</a></p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>A standard inspection is written for someone who'll live in the house.</b> If it's coming down, most of it is a fact you'll bulldoze.</li>
          <li><b>Read it for the block:</b> cracking, movement, damp, termites in the ground, suspected asbestos.</li>
          <li><b>The four checks that matter more:</b> the year and overlay, the flood report, asbestos, the trees and ground.</li>
          <li><b>Keep the inspection condition in the contract.</b> Tell the inspector what you're actually buying.</li>
          <li><b>If you might keep the house, the full report earns its money.</b></li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Can we skip the inspection and save the fee?</p>
          <p>You can, and your solicitor will tell you what it does to the contract condition. Our view: keep the condition, and point the inspector at the things that matter for a rebuild. The fee is small against the block.</p>
        </div>
        <div>
          <p class="q">Is an asbestos audit worth doing before we buy?</p>
          <p>If you want the removal scope before you commit, a licensed assessor can do one. If you're happy to treat removal as a certainty on a pre-1990 house, it can wait until you own it.</p>
        </div>
        <div>
          <p class="q">Will the inspector tell us if we can knock it down?</p>
          <p>No. That's a planning question, answered by the year of the house and council's overlay map. Check both yourself; it takes minutes.</p>
        </div>
        <div>
          <p class="q">Can a builder do the walk instead?</p>
          <p>Nathan walks blocks that are on the market and tells you what he sees: the slope, the access, the ground, what the house would cost to remove and what the block would let you build. It's not a building and pest report, and it's the one that answers the rebuild question.</p>
        </div>
      </div>

      <p class="small sources">Sources: Brisbane City Council, <em>Demolition or removal</em>, <em>FloodWise Property Reports</em>, <em>Protected vegetation</em>; Queensland Government, <em>asbestos.qld.gov.au</em>; Standards Australia AS 4349.1 (pre-purchase building inspections) for what a standard report covers. Read 17 September 2026. This is a plain-English guide from a builder, not legal or conveyancing advice. Talk to your solicitor about contract conditions.</p>
''')

# ---------------------------------------------------------------- R44 · construction loan (shape only)
POSTS["r44-construction-loan"] = dict(
    slug="can-you-get-a-construction-loan-for-a-knockdown-rebuild",
    section="builder",
    title="Can you get a construction loan for a knockdown rebuild?",
    h1="Can you get a construction loan<br>for a knockdown rebuild?",
    description="Generally yes, and this is the shape of one, not advice: the lender pays the builder in stages as the house goes up, its valuer checks each stage, and the loan is sized on the land plus the finished house. What that means for your contract, and why a broker or lender decides the rest.",
    lede="We're builders, not lenders, and this post is careful about that. What we can tell you is the shape of the thing: how a construction loan pays for a house differently from a mortgage on one that already exists, what that means for the contract you sign with us, and the three things lenders will ask you for that a builder can help with. The rest is a conversation with a broker or a bank.",
    date="2026-09-17", category="Dealing with a builder", image="blog/can-you-get-a-construction-loan-for-a-knockdown-rebuild.jpg",
    image_alt="A house at lock-up stage seen through a car windscreen, a valuer's clipboard on the passenger seat",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real job.",
    label=("The shape of it, not advice", "The construction loan"),
    card_title="Can you get a construction loan for a knockdown rebuild?",
    card_blurb="Generally yes. The shape of one, not advice: staged payments to the builder, the lender's valuer at each stage, the loan sized on land plus finished house, and what that means for your contract.",
    about=["Construction loan", "Knockdown rebuild finance", "Progress payments", "Brisbane Bayside"],
    related=["progress-payments-what-you-pay-and-when-on-a-queensland-house-build", "what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane", "whats-in-a-queensland-building-contract-in-plain-english"],
    cta="Nathan can give your lender or broker what they usually ask a builder for: a fixed-price contract, plans and specifications, and a stage schedule. The lending decision is theirs.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Generally, yes. Lenders offer construction loans for building a new house on land you own, and a knockdown rebuild is that with a demolition at the front. Whether <em>you</em> can get one, for how much, and on what terms, is a decision for a lender or a mortgage broker, based on your finances. We're builders. We don't know, and we won't guess.</p>
        <p>What we can describe is the shape. A construction loan usually isn't paid to you in a lump. The lender pays the builder in stages as the house goes up, after its own valuer confirms the stage is done. The loan is usually sized on the value of the land plus the finished house, and it usually wants a fixed-price contract, plans and specifications, and a stage payment schedule before it's approved.</p>
        <p>That shape lines up neatly with Queensland's rules on progress payments, which already require claims to match work done on site. A fixed-price contract with a sensible stage schedule is what both the law and the lender want.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#shape">What does a construction loan look like?</a></li>
          <li><a href="#knockdown">What's different about a knockdown rebuild?</a></li>
          <li><a href="#what-they-ask">What will a lender ask the builder for?</a></li>
          <li><a href="#contract">What does it mean for the contract?</a></li>
          <li><a href="#who-decides">Who decides, and when to talk to them</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="shape">What does a construction loan look like?</h2>
      <p>In general terms, and every lender is different:</p>
      <ul class="pts">
        <li><strong>Staged drawdowns.</strong> The loan is released in parts that match the builder's stage claims &mdash; base, frame, lock-up, fixing, completion, or whatever the contract names.</li>
        <li><strong>The lender's valuer.</strong> Before each stage is paid, the lender typically sends a valuer to confirm the work is done. That's a second check, alongside the certifier, that a claim matches the house.</li>
        <li><strong>Valuation on completion.</strong> The lender usually values the project as if complete &mdash; land plus finished house &mdash; and lends against that.</li>
        <li><strong>Paperwork up front.</strong> A signed fixed-price building contract, council-approved plans and specifications, and the stage schedule are commonly required before approval.</li>
      </ul>

      <h2 class="h2" id="knockdown">What's different about a knockdown rebuild?</h2>
      <p>Three things a lender tends to notice.</p>
      <p><strong>The house that's there now goes away.</strong> If there's a mortgage on the existing house, the security changes when it's demolished. Lenders have processes for this; it's a conversation to have before demolition, not after.</p>
      <p><strong>There's a demolition and site stage before the build.</strong> Asbestos removal, demolition and disconnections are real costs before the first stage of the new house. Some lenders treat them as a stage; some expect them to be funded another way. Ask.</p>
      <p><strong>You're living somewhere else.</strong> Rent during the build isn't in the building contract and lenders know it's there. Have your plan for it.</p>

      <h2 class="h2" id="what-they-ask">What will a lender ask the builder for?</h2>
      <ul class="pts">
        <li>A <strong>fixed-price building contract</strong>, signed, with the price on the front page as Schedule 1B requires.</li>
        <li><strong>Plans and specifications</strong>, and the building approval once issued.</li>
        <li>The <strong>stage payment schedule</strong> from the contract.</li>
        <li>The builder's <strong>QBCC licence</strong> details and, often, evidence of the Home Warranty cover.</li>
        <li>Sometimes a <strong>builder's questionnaire</strong> or the lender's own form.</li>
      </ul>
      <p>Every one of those is a normal thing for a builder to produce, and a builder who can't is telling you something.</p>

      <blockquote class="proof">
        <p><b>Progress claims under a Queensland domestic building contract must be &ldquo;directly related to work progress on site and proportionate to (or less than) the value of the work that relates to the claim.&rdquo;</b></p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023. The lender's valuer and the QBCC's rule are asking the same question of every claim.</cite>
      </blockquote>

      <h2 class="h2" id="contract">What does it mean for the contract?</h2>
      <p>That a fixed price with few allowances isn't just the safer contract for you; it's usually the one a lender will fund. Cost-plus contracts, with no fixed total, are harder to lend against as well as riskier to sign. And the stage schedule in the contract should be one a valuer can walk up and verify: a frame stage means a frame you can see.</p>
      <p>It also means the timeline has a second audience. Variations that move the price, and extensions that move the date, may need to be communicated to the lender too.</p>

      <h2 class="h2" id="who-decides">Who decides, and when to talk to them</h2>
      <p>A mortgage broker or your lender, and early &mdash; before the design is finished, ideally before the walk-through. Knowing what you can borrow shapes what gets drawn. Bring them the block, the rough brief and the fact that it's a knockdown; bring us their questions about the contract and the stages. We'll answer the building ones. We won't answer the lending ones, because we'd be guessing.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Construction loans for knockdown rebuilds exist.</b> Whether you get one is a lender's decision, not ours.</li>
          <li><b>The shape: staged payments to the builder,</b> the lender's valuer at each stage, sized on land plus finished house.</li>
          <li><b>A knockdown adds three wrinkles:</b> the existing mortgage, the demolition stage, and rent during the build.</li>
          <li><b>Lenders want the fixed-price contract, plans, stage schedule and licence.</b> All normal for a builder to supply.</li>
          <li><b>Talk to a broker or lender early,</b> before the design is fixed.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Can Sabre recommend a broker or a bank?</p>
          <p>We'd rather not steer you. Ask people you trust, and ask any broker how they're paid. What we'll do is give whoever you choose the building paperwork quickly and completely.</p>
        </div>
        <div>
          <p class="q">Does the lender pay the deposit?</p>
          <p>Ask them. The deposit under the contract is capped by law at 5% for contracts of $20,000 or more, and how it's funded is between you and your lender.</p>
        </div>
        <div>
          <p class="q">What if the valuer disagrees with a stage claim?</p>
          <p>Then the stage isn't paid until it's resolved, which is the system working. The certifier's inspection certificate for the stage usually settles it.</p>
        </div>
        <div>
          <p class="q">Will you talk to our broker directly?</p>
          <p>Yes, with your say-so, about the contract, the stages and the timeline. Not about your finances, which we don't need to know.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/sites/default/files/2021-09/guide-qbcc-consumer-building-v3.pdf" rel="noopener">Consumer Building Guide</a> (version 3, effective July 2023), on contract price, deposits and progress payments. Read 17 September 2026. <strong>This post describes the general shape of construction lending only. It is not financial, credit or lending advice, it names no product, lender or rate, and Sabre Constructions is not a credit provider or adviser.</strong> Talk to a licensed mortgage broker or your lender.</p>
''')

# ---------------------------------------------------------------- R45 · what's in a quote
POSTS["r45-quote"] = dict(
    slug="what-should-be-in-a-builders-quote-line-by-line",
    section="builder",
    title="What should be in a builder's quote, line by line?",
    h1="What should be in a builder's quote,<br>line by line?",
    description="The lines a complete knockdown rebuild quote carries, from the asbestos and the demolition through the slab, the frame, the fit-out and the driveway, to the allowances, the certifier, the Home Warranty premium and GST. What to look for, and the three places a quote is usually thin.",
    lede="Two quotes for the same house can be a long way apart, and the difference is usually in what one of them left out. Here's what a complete quote for a knockdown rebuild should have in it, line by line, so you can compare like with like and see where a number is thin before you sign.",
    date="2026-09-17", category="Dealing with a builder", image="blog/what-should-be-in-a-builders-quote-line-by-line.jpg",
    image_alt="A multi-page quote laid out on a site table, a finger running down the lines, a coffee and a hard hat beside it",
    image_caption="Illustration.",
    label=("Compare like with like", "The quote"),
    card_title="What should be in a builder's quote, line by line?",
    card_blurb="The lines a complete knockdown rebuild quote carries, from asbestos and demolition through the slab, frame, fit-out and driveway, to allowances, the certifier, the Home Warranty premium and GST. And the three places a quote is usually thin.",
    about=["Builder's quote", "Knockdown rebuild quote", "Allowances", "QBCC"],
    related=["what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane", "fixed-price-or-cost-plus-what-do-builders-mean", "what-questions-should-we-ask-a-builder-before-we-sign"],
    cta="Bring the other quote. Nathan will lay Sabre's beside it, line for line, and show you where they differ and why.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>A complete quote for a knockdown rebuild has five groups of lines: <strong>before the house</strong> (asbestos removal, demolition, disconnections, the soil test, engineering, design, approvals and the certifier); <strong>the site</strong> (earthworks, retaining, drainage, the services connections); <strong>the structure</strong> (footings and slab or subfloor, frame, roof, external walls and windows); <strong>the inside</strong> (plumbing, electrical, linings, joinery, tiling, painting, floors, fit-off); and <strong>the outside and the paperwork</strong> (driveway, fencing, landscaping, the Home Warranty premium, insurances, the builder's margin and GST).</p>
        <p>Then, separately and clearly, the <strong>allowances and provisional sums</strong>: the items the price can't fix yet, each with its estimate. The QBCC's guide says these should be kept to a minimum because the final cost often exceeds the estimate.</p>
        <p>The three places a quote is usually thin: the site (earthworks and retaining), the allowances (a long list of them), and what's simply not there (the driveway, the landscaping, the certifier). Compare the lines, not the totals.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#before">Before the house</a></li>
          <li><a href="#site">The site</a></li>
          <li><a href="#structure">The structure</a></li>
          <li><a href="#inside">The inside</a></li>
          <li><a href="#outside">The outside and the paperwork</a></li>
          <li><a href="#allowances">The allowances</a></li>
          <li><a href="#thin">Where a quote is usually thin</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="before">Before the house</h2>
      <ul class="pts">
        <li><strong>Asbestos removal</strong> by a licensed contractor, with disposal.</li>
        <li><strong>Demolition</strong> and site clearance, including old slabs, footings, sheds, the driveway.</li>
        <li><strong>Disconnections</strong>: power, sewer capping by a licensed plumber, gas.</li>
        <li><strong>Soil test</strong> and <strong>structural engineering</strong> for the footings and frame.</li>
        <li><strong>Design</strong> and drawings, and any <strong>development application</strong> the overlays require.</li>
        <li><strong>The certifier's fees</strong> for the building approval and the mandatory inspections.</li>
      </ul>
      <p>Some builders show these as a separate &ldquo;preliminaries&rdquo; or &ldquo;site&rdquo; section; some leave demolition and asbestos to you. Either is fine as long as it's written down. What isn't fine is a quote that doesn't mention them.</p>

      <h2 class="h2" id="site">The site</h2>
      <ul class="pts">
        <li><strong>Earthworks</strong>: cut and fill, and the removal of spoil.</li>
        <li><strong>Retaining walls</strong>, engineered where they hold a slope.</li>
        <li><strong>Stormwater</strong> drainage to the street or the easement, and any on-site detention required.</li>
        <li><strong>Service connections</strong>: sewer, water, power to the new house, and the temporary builder's supply.</li>
        <li><strong>Temporary fencing, site toilet, skips</strong> and the like.</li>
      </ul>
      <p>On a sloping Bayside block the site section is where the honest quote and the optimistic quote part company. <a href="../what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane/">Why is here.</a></p>

      <h2 class="h2" id="structure">The structure</h2>
      <ul class="pts">
        <li><strong>Footings and slab</strong> to the engineer's design for the soil class, with termite management and the membrane; or <strong>posts, bearers and floor frame</strong> on a highset.</li>
        <li><strong>Wall and roof frame</strong>, timber or steel, with bracing and tie-downs.</li>
        <li><strong>Roofing</strong>, gutters, downpipes, fascia.</li>
        <li><strong>External walls</strong>: cladding, brick, render, as specified.</li>
        <li><strong>Windows and external doors</strong>, with the glazing certificate the certifier wants at the end.</li>
        <li><strong>Stairs, decks and balustrades.</strong></li>
      </ul>

      <h2 class="h2" id="inside">The inside</h2>
      <ul class="pts">
        <li><strong>Plumbing and drainage</strong>, and the hot water system.</li>
        <li><strong>Electrical</strong>, switchboard, lighting, data, smoke alarms.</li>
        <li><strong>Insulation</strong> to the energy efficiency requirements.</li>
        <li><strong>Internal linings</strong>, cornices, doors, architraves and skirtings.</li>
        <li><strong>Waterproofing</strong> to the wet areas, with its certificate.</li>
        <li><strong>Joinery</strong>: kitchen, bathrooms, laundry, wardrobes.</li>
        <li><strong>Tiling, painting, floor coverings, fit-off</strong> (tapware, fittings, appliances if included).</li>
      </ul>

      <h2 class="h2" id="outside">The outside and the paperwork</h2>
      <ul class="pts">
        <li><strong>Driveway and crossover</strong>, paths, clothesline, letterbox.</li>
        <li><strong>Fencing</strong> and basic <strong>landscaping</strong>, or a clear statement that they're excluded.</li>
        <li><strong>The Home Warranty premium</strong>, which the builder collects and pays to the QBCC.</li>
        <li><strong>Insurances</strong>: contract works, public liability.</li>
        <li><strong>The builder's margin</strong> and <strong>GST</strong>, and whether the total includes them.</li>
      </ul>

      <h2 class="h2" id="allowances">The allowances</h2>
      <p>Listed separately, each with its estimate: tiles, tapware, appliances, lighting, sometimes the site works if the soil test isn't in yet. This is the part of the quote that behaves like an estimate rather than a price, and the QBCC's advice is direct.</p>

      <blockquote class="proof">
        <p><b>&ldquo;Allowances (items or services for which the price is not fixed when the contract is signed) should be kept to a minimum as the final cost often exceeds the estimate in the contract.&rdquo;</b> The QBCC's checklist asks you to check what proportion of the total is allowances.</p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023. Count them. Ask why each one is there.</cite>
      </blockquote>

      <h2 class="h2" id="thin">Where a quote is usually thin</h2>
      <ul class="pts">
        <li><strong>The site.</strong> Earthworks and retaining priced as if the block were flat, or as an allowance.</li>
        <li><strong>The allowances.</strong> A cheap quote is often a quote with the real prices moved into a long allowance list.</li>
        <li><strong>What's missing.</strong> No driveway, no fencing, no certifier, no Home Warranty line, no GST line. Every one of those turns up later as a cost.</li>
      </ul>
      <p>The check is simple: put two quotes side by side and tick the lines above against each. The cheaper total is usually the shorter list.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Five groups of lines:</b> before the house, the site, the structure, the inside, the outside and the paperwork.</li>
          <li><b>Allowances listed separately with their estimates.</b> Keep them few; the QBCC says why.</li>
          <li><b>A quote is usually thin in three places:</b> the site, the allowances, and what it doesn't mention.</li>
          <li><b>Compare the lines, not the totals.</b> The cheaper total is usually the shorter list.</li>
          <li><b>The quote becomes the contract's price and specification.</b> If it isn't in there, it isn't in the price.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Should the quote have a total on the front?</p>
          <p>The contract must, if the price is fixed: prominently, on the first page of the schedule. The quote is the working document that gets you there, and it should be clear whether its total includes GST and the allowances.</p>
        </div>
        <div>
          <p class="q">Is a longer quote always better?</p>
          <p>A more complete one is. Length for its own sake isn't the point; the point is that every line above has an answer, even if the answer is &ldquo;excluded, you're arranging it.&rdquo;</p>
        </div>
        <div>
          <p class="q">Why do two builders' allowances differ so much?</p>
          <p>Because an allowance is a guess about what you'll choose. One builder guesses low to win the job; another guesses at what families actually pick. Ask each one what their allowance would buy, in a shop you can walk into.</p>
        </div>
        <div>
          <p class="q">Will Sabre's quote have all of these lines?</p>
          <p>Ask Nathan to lay it out against this list. Anything excluded will say so in writing, and every allowance will have a reason.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/sites/default/files/2021-09/guide-qbcc-consumer-building-v3.pdf" rel="noopener">Consumer Building Guide</a> (version 3, effective July 2023), on contract price, allowances and the Home Warranty premium; Queensland <em>Building Regulation 2021</em> (mandatory inspection stages and certificates). Read 17 September 2026. This is a plain-English guide to the shape of a quote, from a builder. It contains no prices, and it is not financial or legal advice.</p>
''')
