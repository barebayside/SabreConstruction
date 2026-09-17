# Phase 5, part C — Spiral 1 without Nathan: R17, R20, R21, R22.
# Sources read 2026-09-17:
#   Energex — "Remove your connection": contact your retailer; "Building demolition or removal cannot, under any circumstances, start until
#     Energex has confirmed in writing that the work to remove the connection has been completed"; Energex removes the service line and its
#     assets; the NMI is cancelled
#   Brisbane City Council — "Demolition or removal": plumbing approval may be needed to cap the sanitary drain on the property, by a licensed plumber
#   QBCC — Consumer Building Guide v3: licence check; contract price and allowances; cooling-off 5 business days; deposits 5%/10%/20%;
#     commencement notice within 10 business days; variations in writing before work; implied warranties 6 years structural / 1 year other;
#     practical completion and the defects document; extensions of time; liquidated damages; "Deposits and progress payments" (27 Jun 2025)
# Rule 1: no prices, no bands, no timelines. R20 is FACTORS ONLY.

POSTS = {}

# ---------------------------------------------------------------- R17 · moving out and services
POSTS["r17-move-out-services"] = dict(
    slug="do-we-need-to-move-out-before-demolition-and-when-do-the-services-get-cut",
    section="rebuild",
    title="Do we need to move out before demolition, and when do the services get cut?",
    h1="Do we need to move out before demolition,<br>and when do the services get cut?",
    description="Yes, and earlier than most people plan for. The order the power, water, sewer, gas and internet come off an old house, who arranges each one, and Energex's rule that demolition can't start until the disconnection is confirmed in writing.",
    lede="The house has to be empty and dead before the excavator arrives: no power, no water, the sewer capped, the gas gone. Each of those is arranged by a different person on a different timetable, and one of them can hold up the whole job. Here's the order, and who does what.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/do-we-need-to-move-out-before-demolition-and-when-do-the-services-get-cut.jpg",
    image_alt="An emptied Bayside house with the power meter box open and tagged, a removals truck pulling away",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real job.",
    label=("The order things come off", "Moving out"),
    card_title="Do we need to move out before demolition, and when do the services get cut?",
    card_blurb="Yes, and earlier than most people plan. The order the power, water, sewer, gas and internet come off, who arranges each, and the rule that stops demolition until Energex confirms in writing.",
    about=["Demolition", "Disconnecting services", "Energex", "Knockdown rebuild"],
    related=["what-asbestos-removal-means-for-a-knockdown-rebuild", "what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane", "can-we-keep-the-pool-the-shed-or-the-front-fence-in-a-knockdown-rebuild"],
    cta="Nathan will give you the sequence for your job in writing, with who's responsible for each disconnection, so nothing surprises you in the last fortnight.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Yes. The family moves out before anyone touches the house, and the house is fully disconnected before demolition starts. The order is roughly: you move out and clear the house; asbestos is removed by a licensed contractor; the electricity connection is removed by Energex through your retailer; the gas is disconnected and the meter removed; the water is turned off and the sewer drain capped by a licensed plumber under a plumbing approval; the phone and internet are cancelled. Then the demolition contractor starts.</p>
        <p>The one that can hold everything up is the power. Energex's rule is that building demolition or removal cannot, under any circumstances, start until Energex has confirmed in writing that the connection has been removed. That request goes through your electricity retailer, not to Energex directly, and it takes time.</p>
        <p>Who arranges what varies by builder. Ask for the list in writing, with names against each line.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#moving-out">When do we actually have to be out?</a></li>
          <li><a href="#power">How does the power come off?</a></li>
          <li><a href="#water-sewer">What about water and the sewer?</a></li>
          <li><a href="#gas-internet">Gas, phone and internet</a></li>
          <li><a href="#who-arranges">Who arranges each one?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="moving-out">When do we actually have to be out?</h2>
      <p>Before the asbestos removalists arrive, which is before demolition. Removal happens in an empty house with the area sealed, and it's the first trade on site. So the moving date is set by the asbestos date, not the demolition date, and the two can be some way apart.</p>
      <p>Clear everything you want. Anything left in the house when the removalists seal it is gone. That includes the shed, the under-house storage and the things in the roof. Then the house is locked and the keys go to the builder.</p>

      <h2 class="h2" id="power">How does the power come off?</h2>
      <p>This is the one with a hard rule and a lead time.</p>
      <ol>
        <li>You (or the builder, on your behalf) contact your <strong>electricity retailer</strong> and ask for the network connection to be removed for demolition. The retailer raises the service order with Energex.</li>
        <li>Energex removes the service line and its own assets from the house. The property's meter identifier (the NMI) is cancelled.</li>
        <li>Energex confirms in writing that the connection has been removed. <strong>Nothing is demolished until that letter exists.</strong></li>
      </ol>

      <blockquote class="proof">
        <p><b>&ldquo;Building demolition or removal cannot, under any circumstances, start until Energex has confirmed in writing that the work to remove the connection has been completed.&rdquo;</b> Energex adds that you may be at risk of electrocution if demolition starts without that written confirmation.</p>
        <cite>Energex, <em>Remove your connection</em>. The request goes through your retailer, not Energex, and the retailer's timeframe is the one to ask about.</cite>
      </blockquote>

      <p>Ask your retailer, in the same call, about a temporary builder's supply for the new build. It's a separate connection, and the builder usually arranges it.</p>

      <h2 class="h2" id="water-sewer">What about water and the sewer?</h2>
      <p>The water is turned off at the meter and the meter is dealt with through the water utility. The sewer is the part people don't know about: the sanitary drain on the property has to be capped so the demolition doesn't leave an open sewer connection on the block.</p>
      <p>Council's demolition page says a plumbing approval may be needed to cap off the sanitary drain within your property, and it must be done by a licensed plumber. That's arranged before demolition and inspected. The new house connects to the same point later.</p>

      <h2 class="h2" id="gas-internet">Gas, phone and internet</h2>
      <p>If the house has reticulated gas, the gas retailer disconnects and the meter is removed before demolition. Bottled gas is simply collected. Phone and internet are cancelled with the provider; the nbn connection to the old house is abolished and a new one is ordered for the new house late in the build. None of these stop demolition the way the power does, but a live gas meter on a demolition site is not something anyone wants to find.</p>

      <h2 class="h2" id="who-arranges">Who arranges each one?</h2>
      <p>It depends on the builder and the contract, and the honest answer is: ask, and get it in writing. Some builders handle every disconnection as part of the demolition package. Some ask the owner to cancel the retail accounts (the retailer will only talk to the account holder) while the builder manages the plumber, the demolition contractor and the timing.</p>
      <p>What matters is that one person owns the list. The last fortnight before demolition is where a job slips if the power letter hasn't come through, and that's a fortnight of paying for somewhere else to live.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>You're out before the asbestos removalists, not before the excavator.</b> Plan the move around the earlier date.</li>
          <li><b>Power comes off through your retailer, and Energex must confirm in writing</b> before demolition can start. It's the item that holds jobs up.</li>
          <li><b>The sewer drain is capped by a licensed plumber</b> under a plumbing approval.</li>
          <li><b>Gas, phone and internet are cancelled with their providers.</b> A live gas meter on site is the thing to avoid.</li>
          <li><b>One person owns the list, in writing.</b> Ask who.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">How long before demolition should we start the disconnections?</p>
          <p>Ask your retailer for their current timeframe when you make the request; it isn't ours to promise. Start it as soon as the demolition date is pencilled in, not the week before.</p>
        </div>
        <div>
          <p class="q">Can we stay in the house until the day before?</p>
          <p>Not usually. The asbestos removal comes first and the house is sealed for it. Once the power is off, the house isn't liveable anyway.</p>
        </div>
        <div>
          <p class="q">Does the builder need power on site during the build?</p>
          <p>Yes, and it's a separate temporary connection, usually a builder's pole, arranged through a retailer for the site. It isn't the old house's connection.</p>
        </div>
        <div>
          <p class="q">What about the letterbox and the mail?</p>
          <p>Redirect it. The block will have no letterbox for months. Small thing; it's the one people forget.</p>
        </div>
      </div>

      <p class="small sources">Sources: Energex, <em>Remove your connection</em> (residential and commercial connections); Brisbane City Council, <a href="https://www.brisbane.qld.gov.au/building-and-planning/getting-started-on-your-project/residential-projects/demolition-or-removal" rel="noopener">Demolition or removal</a>; Queensland Government, <em>asbestos.qld.gov.au</em>. Read 17 September 2026. Retailer and utility processes change; confirm the current process with yours. This is a plain-English guide from a builder, not legal advice.</p>
''')

# ---------------------------------------------------------------- R20 · rebuild vs buy new
POSTS["r20-rebuild-vs-buy"] = dict(
    slug="knockdown-rebuild-vs-buying-a-new-house-which-actually-costs-less",
    section="rebuild",
    title="Knockdown rebuild vs buying a new house: which actually costs less?",
    h1="Knockdown rebuild vs buying a new house:<br>which actually costs less?",
    description="No number, because nobody honest has one for your family. The factors that decide it: what you'd pay to move, what the block you already own is worth to you, the school and the street, the build, and the house you'd end up in either way.",
    lede="This is the real decision most Bayside families are making, and it isn't a sum. It's two lists. Here's what goes on each, without a single made-up figure, so you can do the comparison with your own numbers and your own street.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/knockdown-rebuild-vs-buying-a-new-house-which-actually-costs-less.jpg",
    image_alt="A family at the kitchen table with two piles of paper: a real estate listing on one side, house plans on the other",
    image_caption="Illustration in the style of Sabre's story frames.",
    label=("The two lists", "Rebuild or move?"),
    card_title="Knockdown rebuild vs buying a new house: which actually costs less?",
    card_blurb="No number, because nobody honest has one for your family. The factors that decide it, on both sides, so you can run the comparison with your own figures and your own street.",
    about=["Knockdown rebuild vs moving", "Cost of moving house", "Brisbane Bayside", "Knockdown rebuild"],
    related=["what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane", "why-are-so-many-bayside-houses-being-knocked-down", "schools-on-the-bayside-catchments"],
    cta="Bring both lists to the walk-through. Nathan will fill in the build side honestly, including the things that would make it the wrong choice.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>It depends on two things that are different for every family: what it costs you to move, and what the block you already own is worth to you. Neither is on any calculator.</p>
        <p>Moving has a list of costs that are easy to forget because they don't come in one bill: the selling costs on the old house, the buying costs on the new one, the stamp duty, the move itself, and the gap between what you sell for and what you'd have to pay for a new house in a street as good as the one you're in. Rebuilding has its own list: demolition and everything in the old house, the build, the design and approvals, and the months living somewhere else.</p>
        <p>The honest comparison isn't &ldquo;rebuild cost versus purchase price.&rdquo; It's <em>total cost of ending up in a house that works, in a street you're happy with</em>, on both sides. Do that sum with your own figures and the answer is usually clearer than people expect.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#moving-list">What's on the moving list?</a></li>
          <li><a href="#rebuild-list">What's on the rebuild list?</a></li>
          <li><a href="#the-block">What is the block you own worth to you?</a></li>
          <li><a href="#the-house">What house do you end up in?</a></li>
          <li><a href="#when-to-move">When is moving the right answer?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="moving-list">What's on the moving list?</h2>
      <p>Write these down with your own numbers. A conveyancer and an agent can give you the first three for your situation.</p>
      <ul class="pts">
        <li><strong>Selling the old house:</strong> agent's commission, marketing, conveyancing, and any work to get it presentable.</li>
        <li><strong>Buying the new one:</strong> transfer (stamp) duty, conveyancing, inspections, loan costs if the mortgage changes.</li>
        <li><strong>The move itself,</strong> and the overlap if the dates don't line up.</li>
        <li><strong>The price gap.</strong> What a new or near-new house in a street as good as yours actually costs, against what yours would sell for as an old house. On the Bayside, that gap is usually the biggest number on either list.</li>
        <li><strong>What you give up:</strong> the school catchment, the walk to the water, the neighbours. Not a dollar figure, and not nothing.</li>
      </ul>

      <h2 class="h2" id="rebuild-list">What's on the rebuild list?</h2>
      <ul class="pts">
        <li><strong>The old house coming down:</strong> asbestos removal, demolition, the disconnections. <a href="../what-asbestos-removal-means-for-a-knockdown-rebuild/">What asbestos means is here.</a></li>
        <li><strong>The site:</strong> the soil test, any retaining or earthworks the slope needs, and whatever the overlays add.</li>
        <li><strong>Design and approvals:</strong> the designer, the certifier, a development application if an overlay triggers one.</li>
        <li><strong>The build itself.</strong> Size, storeys and finish, on a fixed price contract with as few allowances as the block allows.</li>
        <li><strong>Living somewhere else</strong> for the length of the build, with the practical completion date in the contract as your planning number.</li>
        <li><strong>What you keep:</strong> the street, the school, the neighbours, and a block you already own with no duty to pay on it.</li>
      </ul>
      <p><a href="../what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane/">The nine things that move the build number are here.</a> None of them is a price; all of them are on your block.</p>

      <h2 class="h2" id="the-block">What is the block you own worth to you?</h2>
      <p>This is the item people miss, and it's the one that tips most Bayside comparisons.</p>
      <p>You already own the land. You don't pay duty on it again. You don't pay an agent to sell it or a conveyancer to buy it. And it's in the street you chose, which on the Bayside usually means the water, the train and the school are already sorted. The whole reason so many houses come down here is that the block is worth staying on and the house isn't worth keeping. <a href="../why-are-so-many-bayside-houses-being-knocked-down/">That post is here.</a></p>

      <h2 class="h2" id="the-house">What house do you end up in?</h2>
      <p>Different houses, and it matters.</p>
      <p>Buy, and you get what's on the market: a house someone else designed for a block that isn't yours, with whatever compromises they made. Rebuild, and you get a house drawn for your block, your flood level, your slope, your view and your family's next twenty years, with new footings, new wiring and the statutory warranties that come with new work.</p>
      <p>That's not a reason to rebuild by itself. It's a reason to compare like with like. A new house on your block against an old house on someone else's isn't the same comparison as new against new.</p>

      <h2 class="h2" id="when-to-move">When is moving the right answer?</h2>
      <p>Often, and we'll say so.</p>
      <ul class="pts">
        <li>When the street isn't the reason you're staying &mdash; the school's done, the commute's changed, the water isn't part of your week.</li>
        <li>When the block itself is the problem: too small for what you need, an overlay that won't let the house come down, ground that would cost more to fix than it's worth.</li>
        <li>When a year of the family somewhere else isn't something you can do right now.</li>
        <li>When the house you'd buy really is the house you'd build, at a price that beats the rebuild list with the duty and the agents on top.</li>
      </ul>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>It's two lists, not one number.</b> Total cost of ending up in a house that works, on both sides.</li>
          <li><b>Moving's list hides in separate bills:</b> selling, buying, duty, the move, and the price gap to a street as good as yours.</li>
          <li><b>Rebuilding's list is on your block:</b> the old house, the site, the approvals, the build, and living elsewhere.</li>
          <li><b>The block you own is the item people miss.</b> No duty, no agent, and the street already chosen.</li>
          <li><b>Compare like with like:</b> a new house on your block against a new house somewhere else.</li>
          <li><b>Moving is often right.</b> Run the lists honestly and you'll know.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Why won't you just tell us which is cheaper?</p>
          <p>Because we'd be inventing your selling price, your buying price, your duty and your rent, and we'd be wrong. The lists are the honest version. Your agent, your conveyancer and a walk-through fill in the numbers.</p>
        </div>
        <div>
          <p class="q">Does a rebuild add more value than it costs?</p>
          <p>Ask an agent who knows your street, not a builder. What we can say is that the value is in a new house on a block in a street people want, and the Bayside has the street part covered.</p>
        </div>
        <div>
          <p class="q">What about renovating instead of either?</p>
          <p>A third list, and sometimes the right one. <a href="../knockdown-rebuild-or-renovate-how-to-tell-which-one-your-house-is/">How to tell is here.</a></p>
        </div>
        <div>
          <p class="q">Can we get the build side priced before we decide?</p>
          <p>Yes. The walk-through is the first step, and Nathan will tell you what he'd need to give you a real figure rather than an estimate with allowances in it.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <em>Consumer Building Guide</em> v3 (contract price, allowances, practical completion); Queensland Revenue Office, transfer duty (that it applies to a purchase and not to building on land you own). Read 17 September 2026. This is a plain-English guide from a builder. It is not financial, tax or property advice, and it contains no figures because the honest ones are yours.</p>
''')

# ---------------------------------------------------------------- R21 · questions to ask a builder
POSTS["r21-questions-to-ask"] = dict(
    slug="what-questions-should-we-ask-a-builder-before-we-sign",
    section="builder",
    title="What questions should we ask a builder before we sign?",
    h1="What questions should we ask a<br>builder before we sign?",
    description="Fifteen questions, most of them lifted from the QBCC's own checklist and the rules in Schedule 1B: the licence, the contract type, the allowances, the deposit, the dates, the cooling-off, the variations, the warranty, and who you'll actually be talking to in month four.",
    lede="You get one conversation before the contract where every question is free. Here are the fifteen worth asking, in the order they matter, with the rule behind each one so you know what a good answer sounds like. Ask us all of them.",
    date="2026-09-17", category="Dealing with a builder", image="blog/what-questions-should-we-ask-a-builder-before-we-sign.jpg",
    image_alt="A couple across a verandah table from a builder, a printed list of questions between them, no faces",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of real people.",
    label=("Fifteen questions", "Before you sign"),
    card_title="What questions should we ask a builder before we sign?",
    card_blurb="Fifteen questions, most from the QBCC's own checklist: the licence, the contract type, the allowances, the deposit, the dates, the cooling-off, the variations, the warranty, and who you'll talk to in month four.",
    about=["Questions to ask a builder", "QBCC", "Building contract Queensland", "Choosing a builder"],
    related=["what-is-the-qbcc-and-what-to-check-on-a-builders-licence", "fixed-price-or-cost-plus-what-do-builders-mean", "who-are-the-small-independent-builders-on-brisbanes-bayside"],
    cta="Print the list and bring it. Nathan would rather answer all fifteen at the table than have you wonder about one of them in month four.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Ask about five things: the licence, the contract, the money, the time, and the people. Most of the questions below come straight from the QBCC's Consumer Building Guide, which a builder must give you before you sign a contract of $20,000 or more, and from the rules in Schedule 1B of the QBCC Act that sit behind every domestic building contract in Queensland.</p>
        <p>A good builder answers them without blinking, because the answers are already in the contract. A builder who bristles at the licence question, or can't say what the allowances are, has told you something useful for free.</p>
        <p>The last two questions aren't in any guide. They're about who you'll be talking to when something goes wrong, and they're the ones families wish they'd asked.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#licence">The licence (questions 1&ndash;3)</a></li>
          <li><a href="#contract">The contract (4&ndash;7)</a></li>
          <li><a href="#money">The money (8&ndash;10)</a></li>
          <li><a href="#time">The time (11&ndash;13)</a></li>
          <li><a href="#people">The people (14&ndash;15)</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="licence">The licence (questions 1&ndash;3)</h2>
      <ol>
        <li><strong>What's your QBCC licence number, and what class is it?</strong> Then look it up yourself on the QBCC's online licence search. <a href="../what-is-the-qbcc-and-what-to-check-on-a-builders-licence/">How is here.</a></li>
        <li><strong>Who holds the licence &mdash; the company, or a person?</strong> And is that person the one running your job?</li>
        <li><strong>Has the licence ever been suspended, or had conditions on it?</strong> The register shows history. Ask anyway, and see whether the answer matches.</li>
      </ol>

      <blockquote class="proof">
        <p><b>&ldquo;Before committing, check the contractor's licence and history via the QBCC Online Licence Search or by calling the QBCC.&rdquo;</b> If you engage an unlicensed contractor, your work may not be covered under the Queensland Home Warranty Scheme.</p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023. First item on the regulator's own checklist.</cite>
      </blockquote>

      <h2 class="h2" id="contract">The contract (4&ndash;7)</h2>
      <ol start="4">
        <li><strong>Is this a fixed price contract, cost-plus, or construction management?</strong> The QBCC warns against the second two in plain words. <a href="../fixed-price-or-cost-plus-what-do-builders-mean/">Why is here.</a></li>
        <li><strong>Which standard contract is it, and can we have a copy to read before we sign?</strong> The guide says not to sign before you've received the full contract, plans and specifications.</li>
        <li><strong>What are the allowances and provisional sums, and why is each one there?</strong> The guide: keep allowances to a minimum, because the final cost often exceeds the estimate. Ask what proportion of the price they are.</li>
        <li><strong>What happens if we want to change something after signing?</strong> The right answer: a written variation, agreed by you before the work starts, stating the change to the price and any delay. That's the law, not a courtesy.</li>
      </ol>

      <h2 class="h2" id="money">The money (8&ndash;10)</h2>
      <ol start="8">
        <li><strong>What's the deposit?</strong> For a contract of $20,000 or more the maximum before work starts on site is 5%, or up to 20% only where more than half the work is done off site. A builder asking for more is asking for something the law doesn't allow.</li>
        <li><strong>What are the progress payments tied to?</strong> The guide says claims must be directly related to work progress on site and proportionate to it &mdash; you shouldn't pay 50% until at least half the work is done.</li>
        <li><strong>When is the final payment due, and what's a &ldquo;defects document&rdquo;?</strong> You're not required to pay the final payment until the work is complete under the contract, with at most minor defects listed in a defects document compiled at the handover inspection.</li>
      </ol>

      <h2 class="h2" id="time">The time (11&ndash;13)</h2>
      <ol start="11">
        <li><strong>What's the date for practical completion, and how is it set?</strong> The contract must state it, or how it's calculated. The builder must also give you a commencement notice within 10 business days of starting on site, stating the start date and the completion date.</li>
        <li><strong>What can move the completion date?</strong> Extensions of time for the reasons the Act allows &mdash; delays you cause, variations, more rain than could reasonably be expected &mdash; each claimed in writing for you to consider.</li>
        <li><strong>Are there liquidated damages if you're late?</strong> The guide says to consider what amount is appropriate and make sure it's recorded in the contract. Many contracts leave it blank.</li>
      </ol>

      <h2 class="h2" id="people">The people (14&ndash;15)</h2>
      <ol start="14">
        <li><strong>Who will we be talking to in month four, and how do we reach them?</strong> Not the salesperson. The person who'll be on your site and on the end of your phone when the frame is up and a question can't wait.</li>
        <li><strong>Can we speak to a family you built for last year?</strong> Not a testimonial page. A phone number, with their permission.</li>
      </ol>
      <p>If you ask us, the answer to fourteen is Nathan, and the answer to fifteen is yes.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Check the licence yourself,</b> on the QBCC register, before anything else.</li>
          <li><b>Fixed price, with few allowances.</b> Ask why each allowance is there.</li>
          <li><b>Deposit no more than 5% on a contract of $20,000 or more;</b> progress payments tied to work on site.</li>
          <li><b>Practical completion date in the contract,</b> commencement notice within 10 business days, extensions of time in writing.</li>
          <li><b>Variations in writing, before the work.</b> It's the law.</li>
          <li><b>Ask who you'll talk to in month four.</b> Then ask for a phone number of a family from last year.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Is it rude to ask about the licence?</p>
          <p>No. It's the first thing on the regulator's checklist, and a builder who's proud of their licence will show you the number before you ask. Sabre's is in the footer of every page on this site.</p>
        </div>
        <div>
          <p class="q">Can we take the contract home before signing?</p>
          <p>You should. The QBCC's guide says not to sign before you've received the full contract, plans and specifications, and there's a five-business-day cooling-off period after you receive the signed contract and the guide. Read it at the kitchen table, not at the builder's.</p>
        </div>
        <div>
          <p class="q">What if the builder won't give us the Consumer Building Guide?</p>
          <p>They must, before you sign a contract at or over $20,000. If they haven't, don't sign. It's a two-page document and it's free on the QBCC's website.</p>
        </div>
        <div>
          <p class="q">Should we get a solicitor to read it?</p>
          <p>The guide suggests it if you still have concerns after asking the builder, and says so twice for cost-plus contracts. For a fixed price standard contract, many families read it themselves with the guide beside it. Either is reasonable.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <a href="https://www.qbcc.qld.gov.au/sites/default/files/2021-09/guide-qbcc-consumer-building-v3.pdf" rel="noopener">Consumer Building Guide</a> (version 3, effective July 2023) and <a href="https://www.qbcc.qld.gov.au/home-owner-hub/build-renovate/contracts-payments/deposits-progress-payments" rel="noopener">Deposits and progress payments</a> (reviewed 27 June 2025); Schedule 1B, <em>Queensland Building and Construction Commission Act 1991</em>. Read 17 September 2026. Thresholds and rules change; check the QBCC's current pages. This is a plain-English guide, not legal advice.</p>
''')

# ---------------------------------------------------------------- R22 · outgrown the house, love the street
POSTS["r22-outgrown"] = dict(
    slug="weve-outgrown-the-house-but-we-love-the-street-what-are-the-options",
    section="rebuild",
    title="We've outgrown the house but we love the street. What are the options?",
    h1="We've outgrown the house but we love<br>the street. What are the options?",
    description="All of them, honestly: extend, raise and build under, renovate, knock down and rebuild, add a secondary dwelling, or move. What each one suits, what rules it, and how to tell which is yours.",
    lede="This is the sentence we hear most, and it has more than one answer. Here are all six options for a family that's run out of house on a Bayside block they don't want to leave, including the ones that aren't a rebuild and the one that is a move. Which one is yours depends on the house, the block and the rules, in that order.",
    date="2026-09-17", category="Knockdown rebuild", image="blog/weve-outgrown-the-house-but-we-love-the-street-what-are-the-options.jpg",
    image_alt="A family's bikes and a pram crowding the front steps of a small Bayside cottage, a jacaranda over the street",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real street.",
    label=("All six options, honestly", "Outgrown the house"),
    card_title="We've outgrown the house but we love the street. What are the options?",
    card_blurb="All six, honestly: extend, raise and build under, renovate, knock down and rebuild, add a secondary dwelling, or move. What each suits, what rules it, and how to tell which is yours.",
    about=["Outgrown the house", "Extend or rebuild", "Raise and build under", "Brisbane Bayside"],
    related=["knockdown-rebuild-or-renovate-how-to-tell-which-one-your-house-is", "knockdown-rebuild-vs-buying-a-new-house-which-actually-costs-less", "why-are-so-many-bayside-houses-being-knocked-down"],
    cta="Nathan walks the house and the block and tells you which of the six is yours, including if it's the one that isn't a job for him.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Six options, and the honest list has all of them: <strong>extend</strong> outward or upward; <strong>raise and build under</strong> if it's a highset with good bones; <strong>renovate</strong> the plan inside the walls you've got; <strong>knock down and rebuild</strong> a house drawn for the block; add a <strong>secondary dwelling</strong> for the parent or the teenager; or <strong>move</strong>.</p>
        <p>Which one fits depends on three things in order: the house (its bones and its year), the block (its size, slope, overlays and ground), and the rules (Brisbane's codes for height, setbacks and site cover, and the character overlay if the house is pre-1947).</p>
        <p>What every option has in common is that the street stays. That's the whole reason the question gets asked this way, and it's worth saying out loud: on the Bayside, the street is usually the thing worth keeping.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#extend">1. Extend</a></li>
          <li><a href="#raise">2. Raise and build under</a></li>
          <li><a href="#renovate">3. Renovate inside the walls</a></li>
          <li><a href="#rebuild">4. Knock down and rebuild</a></li>
          <li><a href="#secondary">5. A secondary dwelling</a></li>
          <li><a href="#move">6. Move</a></li>
          <li><a href="#which">Which one is yours?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="extend">1. Extend</h2>
      <p>Add rooms at the back, or a floor on top. It suits a house with sound bones, a block with room behind it (or a frame that can carry a second storey), and a plan that works once the new rooms are there.</p>
      <p>What rules it: site cover and setbacks under the Dwelling house codes, the height envelope for a second storey, and the character overlay if the house is pre-1947 (extensions at the back are generally easier than changes to the front). A second storey on an old house also means a structural check of the frame and the footings, and often a soil test.</p>

      <h2 class="h2" id="raise">2. Raise and build under</h2>
      <p>The Bayside classic. Lift a highset higher, then build a proper ground floor beneath it. It suits a timber highset with a good upstairs, a level or gently sloping block, and a family that wants the living downstairs and the bedrooms up, or the reverse.</p>
      <p>What rules it: the height envelope (the raised house still has to fit), the flood level (raising can be the way to meet it), the ground (a new slab under an old house needs the soil test and engineering), and whether the existing built-in-under has asbestos, which most 1970s ones do. <a href="../what-does-highset-mean-on-a-bayside-block/">What highset means is here.</a></p>

      <h2 class="h2" id="renovate">3. Renovate inside the walls</h2>
      <p>Change the plan without changing the footprint: open the kitchen to the living, turn a sleepout into a bedroom, add a bathroom. It suits a house that's big enough but badly arranged, which describes a lot of 1960s highsets.</p>
      <p>What rules it: mostly the building code and the certifier for structural changes, plus asbestos wherever a wall is opened in a pre-1990 house. It's the least disruptive option and the one most likely to be done with the family still in the house. <a href="../knockdown-rebuild-or-renovate-how-to-tell-which-one-your-house-is/">How to tell renovate from rebuild is here.</a></p>

      <h2 class="h2" id="rebuild">4. Knock down and rebuild</h2>
      <p>Start again with a house drawn for the block. It suits a house whose bones are tired, a plan that can only get where it needs to by replacing most of the house anyway, or a block that wants a different house from the one on it: a flood level the old floor doesn't meet, a slope the old house ignores, a view it turns its back on.</p>
      <p>What rules it: the character overlay first (a pre-1947 house in the overlay may not be allowed down), then the codes and overlays for the new house, then the ground. <a href="../can-we-knock-down-our-house/">The character rules are here</a> and <a href="../what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane/">what moves the cost is here</a>.</p>

      <h2 class="h2" id="secondary">5. A secondary dwelling</h2>
      <p>A second, smaller dwelling on the same lot: a granny flat for a parent, a studio for a teenager who isn't leaving, or a place for the family to live while the main house is rebuilt. Brisbane City Plan's definition of a house allows two dwellings on a lot where one is secondary to the other.</p>
      <p>What rules it: the Dwelling house code's provisions for secondary dwellings (size, and its relationship to the main house), site cover, setbacks, and the same overlays as anything else. It solves a space problem without touching the main house, and on a big Bayside block it's often the quiet answer.</p>

      <h2 class="h2" id="move">6. Move</h2>
      <p>Sometimes the right one, and we'll say so. It suits a family for whom the street has stopped being the reason, a block that can't take what's needed, or a year somewhere else that can't happen right now. <a href="../knockdown-rebuild-vs-buying-a-new-house-which-actually-costs-less/">The honest comparison, without a number, is here.</a></p>

      <h2 class="h2" id="which">Which one is yours?</h2>
      <p>Run it in order.</p>
      <ol>
        <li><strong>The house.</strong> Good bones and pre-1947 in the overlay lean toward 1, 2 or 3. Tired bones lean toward 4.</li>
        <li><strong>The block.</strong> Room behind it favours 1 or 5. A slope or a flood level favours 2 or 4. A small lot favours going up: 1 or 4.</li>
        <li><strong>The rules.</strong> The codes and overlays on your lot decide what each option can actually be. City Plan online shows them by address.</li>
        <li><strong>The family.</strong> Who has to live where while it happens, and for how long. That's the question that rules out an option more often than the block does.</li>
      </ol>

      <blockquote class="proof">
        <p><b>Under Brisbane City Plan 2014 a house is &ldquo;a dwelling house used by one household&rdquo; comprising either one dwelling plus domestic outbuildings, or two dwellings, one being secondary, plus associated outbuildings.</b></p>
        <cite>Brisbane City Council, <em>Building a new house: approvals and requirements</em>. The secondary dwelling is in the definition of a house, not an exception to it.</cite>
      </blockquote>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Six options:</b> extend, raise and build under, renovate, rebuild, a secondary dwelling, or move.</li>
          <li><b>The house decides first, then the block, then the rules.</b> Then the family.</li>
          <li><b>Good bones and a pre-1947 date in the overlay steer you away from a rebuild.</b> Tired bones steer you toward one.</li>
          <li><b>A secondary dwelling is inside City Plan's definition of a house.</b> It's the quiet option on a big block.</li>
          <li><b>Moving is on the list on purpose.</b> Sometimes it's the answer.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Can we do the secondary dwelling first and rebuild the main house later?</p>
          <p>It's a real sequence and it's been done: build the small dwelling, live in it through the main rebuild. It depends on the lot having room for both within the codes, and on the family fitting in the small one for the length of the build. Worth asking about early.</p>
        </div>
        <div>
          <p class="q">Is raising and building under cheaper than rebuilding?</p>
          <p>Not always, and nobody can tell you without the house and the ground. It keeps the top and replaces the bottom, so it depends on what the top is worth and what the bottom needs. Ask for both to be looked at.</p>
        </div>
        <div>
          <p class="q">Will a builder who does rebuilds recommend one?</p>
          <p>Some will. The list above has six options and one of them isn't a building job at all. That's deliberate.</p>
        </div>
        <div>
          <p class="q">How long does it take to find out which is ours?</p>
          <p>One walk-through. Nathan looks under the house, in the roof, at the block and the overlays, and tells you which options are open and which he'd choose.</p>
        </div>
      </div>

      <p class="small sources">Sources: Brisbane City Council, <a href="https://www.brisbane.qld.gov.au/building-and-planning/getting-started-on-your-project/residential-projects/new-house" rel="noopener">Building a new house: approvals and requirements</a> (definition of a house; Dwelling house code); Brisbane City Plan 2014, traditional building character overlay and Dwelling house codes; Queensland Government, <em>asbestos.qld.gov.au</em>. Read 17 September 2026. Plain-English guidance from a builder, not planning, structural or financial advice.</p>
''')
