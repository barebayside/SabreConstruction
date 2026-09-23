# Phase 6 — the three hub (pillar) pages, one per spiral, written 2026-09-23 after every spoke existed.
# A hub claims nothing its spokes don't: every fact below is summarised from a live post, and every proof quote is
# copied word for word from a spoke that read the source (QBCC Consumer Building Guide v3; Brisbane City Council
# Heritage and character properties / FloodWise / Severe Weather Alert; Energex; ABS 2021 Census QuickStats;
# State Library of Queensland 2014; qld.gov.au school catchments). Rule 1 held: no prices, bands or build times.
# Links are written [[slug-key|anchor text]] and expanded by link() at the bottom; build_post.py verify() then
# checks every one resolves on disk.

POSTS = {}

SLUGS = {
    # Spiral 1 — rules + rebuild
    "r1": "can-we-knock-down-our-house",
    "r2": "check-if-your-street-is-in-the-character-overlay",
    "r15": "what-is-a-knockdown-rebuild-package",
    "wm": "rebuilding-in-wynnum-or-manly",
    "r9": "what-asbestos-removal-means-for-a-knockdown-rebuild",
    "r19": "rebuilding-on-a-flood-overlay-block-on-the-bayside",
    "s9": "what-are-bayside-houses-made-of",
    "r33": "why-are-so-many-bayside-houses-being-knocked-down",
    "s1": "what-decides-the-cost-of-a-knockdown-rebuild-in-brisbane",
    "s2": "knockdown-rebuild-or-renovate-how-to-tell-which-one-your-house-is",
    "r4": "does-a-knockdown-rebuild-need-a-development-application",
    "r6": "what-happens-to-the-trees-on-the-block-in-a-knockdown-rebuild",
    "r11": "fixed-price-or-cost-plus-what-do-builders-mean",
    "r18": "what-is-a-soil-test-and-why-does-it-change-the-price",
    "s4": "buying-an-old-house-in-wynnum-or-manly-to-knock-down-what-to-check-before-you-sign",
    "s6": "can-you-knock-down-and-rebuild-on-a-small-or-narrow-block-in-brisbane",
    "r7": "can-we-keep-the-pool-the-shed-or-the-front-fence-in-a-knockdown-rebuild",
    "r12": "what-does-highset-mean-on-a-bayside-block",
    "r13": "can-we-build-a-two-storey-house-on-our-block-in-manly",
    "r14": "how-much-of-the-old-house-can-be-reused",
    "r17": "do-we-need-to-move-out-before-demolition-and-when-do-the-services-get-cut",
    "r20": "knockdown-rebuild-vs-buying-a-new-house-which-actually-costs-less",
    "r21": "what-questions-should-we-ask-a-builder-before-we-sign",
    "r22": "weve-outgrown-the-house-but-we-love-the-street-what-are-the-options",
    # Spiral 2 — suburbs + living
    "s7": "is-wynnum-a-good-place-to-live",
    "s8": "wynnum-vs-manly-vs-lota-which-bayside-suburb-suits-which-family",
    "s10": "schools-on-the-bayside-catchments",
    "r23": "how-far-is-wynnum-from-brisbane-cbd",
    "r24": "does-wynnum-flood",
    "r25": "what-to-do-in-wynnum-and-manly-with-kids",
    "r27": "whats-the-difference-between-manly-and-manly-west",
    "r28": "lota-the-quiet-one-between-wynnum-and-manly",
    "r29": "wakerley-and-gumdale-the-newer-bayside",
    "r31": "bayside-storm-season-roof-trees-insurance",
    "r35": "ransome-tingalpa-and-gumdale-the-acreage-edge-of-the-bayside",
    "s11": "moving-to-brisbanes-bayside-from-interstate-what-nobody-tells-you",
    "r30": "what-is-the-wynnum-manly-foreshore-actually-like-to-live-near",
    "r32": "is-the-bayside-a-good-place-to-retire",
    # Spiral 3 — builder
    "s12": "what-is-the-qbcc-and-what-to-check-on-a-builders-licence",
    "r16": "who-are-the-small-independent-builders-on-brisbanes-bayside",
    "s13": "what-does-master-builders-membership-actually-mean-for-you",
    "s14": "progress-payments-what-you-pay-and-when-on-a-queensland-house-build",
    "s15": "variations-why-the-price-changed-and-when-it-shouldnt-have",
    "r36": "what-insurance-should-a-builder-have-and-what-does-it-cover-you-for",
    "r37": "what-is-a-defects-liability-period",
    "r39": "whats-in-a-queensland-building-contract-in-plain-english",
    "r40": "what-happens-if-a-builder-goes-under-mid-build",
    "r41": "should-we-be-an-owner-builder",
    "r42": "how-do-progress-inspections-and-certifiers-work-in-queensland",
    "r43": "what-is-a-building-and-pest-inspection-worth-on-a-house-you-plan-to-knock-down",
    "r44": "can-you-get-a-construction-loan-for-a-knockdown-rebuild",
    "r45": "what-should-be-in-a-builders-quote-line-by-line",
    # the hubs themselves (they link to each other)
    "hub1": "knockdown-rebuild-on-brisbanes-bayside-the-whole-path",
    "hub2": "living-on-brisbanes-bayside-an-honest-guide",
    "hub3": "how-to-choose-a-builder-in-queensland-the-whole-checklist",
}


# ================================================================ HUB 1 · the whole path
POSTS["hub1-knockdown-rebuild"] = dict(
    slug=SLUGS["hub1"],
    section="rebuild",
    title="Knocking down and rebuilding on Brisbane's Bayside: the whole path, in plain words",
    h1="Knocking down and rebuilding on Brisbane's Bayside:<br>the whole path, in plain words.",
    description="Every step of a knockdown rebuild on Brisbane's Bayside, in the order it happens: whether it's the right move, whether the house can come down, what the block decides, what decides the cost, choosing the builder, demolition and the build. With a link to the full answer at every step.",
    lede="Most families come to a knockdown rebuild one question at a time: can we, should we, what will it cost, who do we trust with it. This page puts all the questions in the order they actually arrive, with the short answer to each and a link to the long one. It's the map. The other posts are the ground.",
    date="2026-09-23", category="Knockdown rebuild", image="blog/knockdown-rebuild-on-brisbanes-bayside-the-whole-path.jpg",
    image_alt="A flat Bayside street running down to the water, an old timber house on one block and a new house going up on the next",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real street.",
    label=("The whole guide", "Knockdown rebuild"),
    card_title="Knocking down and rebuilding on Brisbane's Bayside: the whole path, in plain words",
    card_blurb="Every step in the order it happens, from &lsquo;should we?&rsquo; to handover, with the short answer to each and a link to the long one. Start here.",
    about=["Knockdown rebuild", "Brisbane Bayside", "Building approval", "Character overlay", "Flood overlay", "Building a house in Queensland"],
    related=[SLUGS["s1"], SLUGS["r1"], SLUGS["s2"]],
    cta="Every step on this page gets easier once someone has stood on your block. Nathan will walk the house and the block with you and tell you which of these questions matter for yours.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>A knockdown rebuild on the Bayside runs in eight steps, and the first three decide whether the rest happen at all. <strong>One:</strong> decide it's the right move, against renovating, extending or moving. <strong>Two:</strong> check the house can legally come down. If it was built in 1946 or earlier and your street is in council's character overlay, demolition needs a development application. <strong>Three:</strong> read the block. Flood levels, protected trees, the lot size, the slope and the soil all shape the new house.</p>
        <p><strong>Four:</strong> understand what decides the cost. It's mostly the old house and the block, not the floor plan. <strong>Five:</strong> choose who draws it and who builds it. <strong>Six:</strong> move out, disconnect and remove the asbestos. <strong>Seven:</strong> demolition. <strong>Eight:</strong> the build, paid in stages, inspected by a certifier and covered by statutory warranties. The first two checks are free, public and take about fifteen minutes. Do those before anything else.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#right-move">Is a knockdown rebuild the right move?</a></li>
          <li><a href="#can-it-come-down">Can your house legally come down?</a></li>
          <li><a href="#the-block">What does the block decide?</a></li>
          <li><a href="#buying">Buying a house to knock down?</a></li>
          <li><a href="#the-cost">What decides the cost?</a></li>
          <li><a href="#the-builder">Who draws it, and who builds it?</a></li>
          <li><a href="#before-demolition">What happens before demolition?</a></li>
          <li><a href="#the-build">What happens during the build?</a></li>
          <li><a href="#where-to-start">Where do you actually start?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="right-move">Is a knockdown rebuild the right move for your family?</h2>
      <p>Start with the reason you're asking. On the Bayside it's nearly always the same one: the family has outgrown the house but not the street. The school is right, the neighbours are right, the water is at the end of the road. The house is the problem.</p>
      <p>That's worth saying out loud, because it means a rebuild is one answer among several. The honest list has six: extend, raise and build under, renovate inside the walls you've got, knock down and rebuild, add a secondary dwelling, or move. [[r22|All six, and what decides between them, are here.]]</p>
      <p>Between the two big ones, renovating and rebuilding, six checks do most of the work: the structure, the year the house was built, what you want it to become, the block, the ground under it, and what each path would cost you in money and in the house you end up with. A pre-1947 house in the character overlay can tip the answer toward renovating on its own. A post-war lowset with a cracked slab and rooms too small for the family usually tips the other way. [[s2|How to tell which one your house is.]]</p>
      <p>Then there's the comparison nobody can do for you: rebuilding against selling up and buying something newer. Moving has a list of costs that never arrive in one bill: selling costs, buying costs, stamp duty, the move, and the gap between what you'd sell for and what a new house in a street this good would cost. Rebuilding has its own list. The honest sum is the total cost of ending up in a house that works, in a street you're happy with, on both sides. [[r20|How to do that sum with your own figures.]]</p>

      <h3 class="h3">Why are so many of your neighbours doing it?</h3>
      <p>Because four things arrived at once. The post-war houses that fill the Bayside were built fast and small during a national housing shortage, and they're now around seventy years old. A great many are clad in fibro from the asbestos era. The blocks under them are some of the best in Brisbane. And the families in them want to stay. [[r33|The whole story is here]], and [[s9|what the houses are actually made of]] explains why the year of your house matters so much for what happens next.</p>

      <h2 class="h2" id="can-it-come-down">Can your house legally come down?</h2>
      <p>This is the check that can end the conversation, so it goes first. Brisbane City Council draws a line at 1946.</p>
      <ul class="pts">
        <li><strong>Built after 1946?</strong> The character rules almost certainly don't stop you knocking it down. Other approvals still apply.</li>
        <li><strong>Built in 1946 or earlier, and your street is in the Traditional building character overlay?</strong> Demolition needs a development application, and council decides. It isn't automatically no. It isn't automatically yes.</li>
        <li><strong>Built before 1911?</strong> Council's position is that the house is to be kept.</li>
      </ul>

      <blockquote class="proof">
        <p><b>The overlay applies to &ldquo;some areas and streets of older suburbs that have a distinct identity based on building character, materials, layouts and setbacks.&rdquo;</b> Its purpose is &ldquo;to maintain the traditional, pre-1947 streetscape.&rdquo;</p>
        <cite>Brisbane City Council, <em>Heritage and character properties</em>, Brisbane City Plan 2014. Council's own words. The line it draws is 1946, which is why the year of your house matters as much as the map.</cite>
      </blockquote>

      <p>You need two answers, and both are free. Whether your street is in the overlay is on council's City Plan online mapping. The year your house was built is in Brisbane City Archives' building records. [[r2|The fifteen-minute method for both is here]], and [[r1|the rules themselves, in council's own words, are here]].</p>
      <p>Every knockdown rebuild also needs building approval, for the new house and for the demolition, issued by a licensed building certifier. That's not the same thing as a development application. A DA is only needed when something on your lot triggers one: a code-assessable overlay for the new house, or a protected old house for the demolition. [[r4|Which overlays trigger what.]] If you're in Wynnum or Manly specifically, [[wm|the five things to know first are here]].</p>

      <h3 class="h3">What if the answer is no?</h3>
      <p>Then the street is still there and so are the other five options. A protected pre-1947 house can often be raised and built under, extended at the back, or renovated inside the walls you've got. A secondary dwelling for a parent or a teenager is part of the definition of a house in Brisbane's City Plan, not an exception to it. A &ldquo;no&rdquo; on demolition is the start of a different design conversation, not the end of staying. [[r22|The six options, again.]]</p>

      <h2 class="h2" id="the-block">What does the block decide?</h2>
      <p>More than the house does. Two families can pick the same floor plan and end up with very different jobs, because the block underneath is different. These are the things a builder reads off it.</p>

      <h3 class="h3">The flood level</h3>
      <p>A flood overlay on a Bayside block usually doesn't stop a rebuild. It sets rules for the new house, mainly how high the habitable floor has to sit. Council's free FloodWise Property Report gives the levels for your lot, including the minimum habitable floor level. Near the water, storm tide and overland flow are the ones that matter. [[r19|What changes on a flood overlay block.]]</p>

      <h3 class="h3">Highset or lowset</h3>
      <p>That floor level is what most often decides whether the new house goes up or stays on the ground. The slope and the breeze off the bay are the other two reasons. [[r12|What &ldquo;highset&rdquo; means, and when a new house is designed that way.]]</p>

      <h3 class="h3">The trees</h3>
      <p>Some trees on your block may be protected under council's Natural Assets Local Law, and penalties apply for interfering with them without a permit, including lopping, on your own land. You can ask council for a protected vegetation report on your property. [[r6|What happens to the trees.]]</p>

      <h3 class="h3">The size and the shape</h3>
      <p>Under Brisbane City Plan 2014, a lot under 450 square metres is a small lot, and the house is assessed against its own code. Small and narrow blocks get built on all the time; the code shapes the house rather than ruling it out. [[s6|Rebuilding on a small or narrow block.]] Two storeys is the ordinary outcome in the low density residential zone, not an exception. [[r13|Going up on a Manly block, as an example.]]</p>

      <h3 class="h3">The ground</h3>
      <p>A soil test classifies your site under AS 2870, from A for stable sand or rock to E for extremely reactive clay and P for problem sites. The higher the class, the stiffer and deeper the footings, and the more they cost. A quote written without the test has an allowance where the footings should be. [[r18|What a soil test is and why it moves the price.]]</p>

      <h2 class="h2" id="buying">Buying a house to knock down?</h2>
      <p>If you don't own the block yet, the checks are the same, only earlier, and the order matters more because the first two can end the purchase. Check the block, not the house: the year and the overlay, the FloodWise report, protected trees, the slope and access, the ground, the boundaries and any easements, and what the contract lets you do if a check fails. [[s4|The full checklist before you sign.]]</p>
      <p>And think about what a standard building and pest inspection is for. It's written for a buyer who'll live in the house. If the house is coming down, the bathroom leak is a fact you'll bulldoze. Keep the inspection condition in the contract, but tell the inspector what you're really buying. [[r43|What a building and pest inspection is worth on a knockdown.]]</p>

      <h2 class="h2" id="the-cost">What decides the cost?</h2>
      <p>This is the question most families search first, and it's the one we answer differently from most builders. We don't publish a price. Here's why.</p>
      <p>Nine things decide the cost of a knockdown rebuild. Only two are the ones people expect: the size of the new house and the level of finish. The other seven belong to the old house and the block. What the old house is made of, and whether there's asbestos in it. How it comes down. The slope and access of the block. Which overlays apply. What the soil test says. How the new house meets the ground. And where you live while it happens. [[s1|All nine, one at a time.]]</p>
      <p>Anyone who gives you a figure before they've checked those seven is pricing the house, not the job. That's also why the quote matters more than the number at the bottom of it.</p>

      <blockquote class="proof">
        <p><b>&ldquo;Allowances (items or services for which the price is not fixed when the contract is signed) should be kept to a minimum as the final cost often exceeds the estimate in the contract.&rdquo;</b></p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023. The regulator's own warning: a price with a lot of allowances in it isn't a price yet.</cite>
      </blockquote>

      <ul class="pts">
        <li><strong>Read the quote line by line.</strong> A complete one covers before the house, the site, the structure, the inside, and the outside and paperwork, with every allowance listed separately. [[r45|What should be in a builder's quote.]]</li>
        <li><strong>Know which kind of contract it is.</strong> Fixed price puts the risk on the builder; cost-plus puts it on you, and the QBCC is blunt about which it prefers. [[r11|Fixed price or cost-plus.]]</li>
        <li><strong>Talk to a lender or broker early.</strong> Construction loans are usually paid in stages as the house goes up. We're builders, so we describe the shape and leave the decision to them. [[r44|Construction loans for a knockdown rebuild.]]</li>
      </ul>

      <h2 class="h2" id="the-builder">Who draws it, and who builds it?</h2>
      <p>There are two broad ways to build. A <strong>package</strong> starts with a builder's existing plan and fits it to your block, usually at an advertised price. A <strong>custom build</strong> starts with the block and the family and draws the house to them. Neither is right for everybody. What matters is knowing which one you're being offered, and what the advertised number assumes about your block. [[r15|What a knockdown rebuild package is.]]</p>
      <p>Whoever you talk to, check them the same way. Their QBCC licence number goes into the public register, and you check three things: that it's current, that its class covers your job, and that the name on it is the entity you're signing with. [[s12|How to check a builder's licence.]] Then ask the questions the QBCC's own guide suggests, plus the two that aren't in any guide: who you'll be talking to when something goes wrong, and who's on the phone in month four. [[r21|The questions to ask before you sign.]]</p>
      <p>On the Bayside you'll also find small independent builders: locally owned, usually a family, building a handful of homes at a time. Sabre is one of them. [[r16|Who they are and how to compare them]], us included.</p>
      <p>The whole process of choosing a builder, from licence to contract to handover, has its own guide: [[hub3|how to choose a builder in Queensland, the whole checklist]].</p>

      <h2 class="h2" id="before-demolition">What happens before demolition?</h2>
      <p>More than people expect, and in a fixed order. The family moves out before anyone touches the house. Then:</p>
      <ul class="pts">
        <li><strong>The asbestos comes out.</strong> Asbestos was used in Australian building materials from the 1940s to the late 1980s, so most Bayside houses from that era have it somewhere. In Queensland removing it is licensed work: class B for bonded asbestos, class A for the crumbly kind. [[r9|What asbestos removal means for your rebuild.]]</li>
        <li><strong>The services are disconnected.</strong> Electricity, gas, water and sewer, phone and internet, each with its own process. The electricity is the one that holds everything up. [[r17|Moving out and cutting the services.]]</li>
        <li><strong>Decide what stays.</strong> A pool, a shed or a front fence can sometimes stay, if it's sound, it isn't in the way, and the design is drawn around it. Keeping things isn't free. [[r7|What you can keep.]]</li>
        <li><strong>Salvage what's worth saving.</strong> Very little of the old house goes into the new one's structure, but hardwood floors, VJ boards, doors and windows can go to salvage or come back as a feature. [[r14|How much of the old house can be reused.]]</li>
      </ul>

      <blockquote class="proof">
        <p><b>&ldquo;Building demolition or removal cannot, under any circumstances, start until Energex has confirmed in writing that the work to remove the connection has been completed.&rdquo;</b></p>
        <cite>Energex, <em>Remove your connection</em>. The request goes through your electricity retailer, not Energex, and it takes time. Start it early.</cite>
      </blockquote>

      <h2 class="h2" id="the-build">What happens during the build?</h2>
      <p>Once the old house is gone, the job becomes an ordinary Queensland house build, with the protections that come with one. Four things are worth understanding before you sign, because they decide how the next stretch feels.</p>
      <ul class="pts">
        <li><strong>You pay in stages.</strong> The deposit is capped at 5% on a contract of $20,000 or more, and every progress claim after it has to match work done on site. [[s14|Progress payments, and what you pay when.]]</li>
        <li><strong>A certifier inspects the key stages.</strong> For a new house: excavation, footings, slab, frame and final. [[r42|How inspections and certifiers work.]]</li>
        <li><strong>Changes go in writing first.</strong> A variation must be agreed in writing before the work starts. [[s15|Variations, and when the price shouldn't have changed.]]</li>
        <li><strong>The work is warranted after handover.</strong> Six years for structural defects and one year for everything else, whether the contract mentions it or not. [[r37|Defects, warranties and the clocks that run after handover.]]</li>
      </ul>
      <p>How long the whole thing takes is the question we get asked most after cost, and it's the one we won't answer on a web page. Builders' published figures contradict each other, because the block, the approvals and the demolition decide most of it. Ask any builder for a sequence for your job, in writing, once they've seen the block.</p>

      <h2 class="h2" id="where-to-start">Where do you actually start?</h2>
      <p>With the two free checks, tonight, from the couch.</p>
      <ul class="pts">
        <li><strong>First:</strong> put your address into council's City Plan online mapping and turn on the overlays. Note whether you're in the character overlay and whether a flood overlay applies.</li>
        <li><strong>Second:</strong> find the year your house was built. Brisbane City Archives hold the records.</li>
        <li><strong>Third:</strong> pull the FloodWise Property Report for your address. It's free and it takes a minute.</li>
      </ul>
      <p>If none of those stops you, the next step is someone walking the house and the block with you. That's where the other seven cost drivers get answered, and where the honest answer is sometimes &ldquo;renovate&rdquo; or &ldquo;stay as you are.&rdquo;</p>
      <p>And if the question underneath all this is really whether to stay on the Bayside at all, [[hub2|the honest guide to living here]] is the place to start.</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>A rebuild is one of six options</b> for a family that's outgrown the house but not the street. Weigh all six.</li>
          <li><b>1946 is the line.</b> A pre-1947 house in the character overlay needs a development application to come down.</li>
          <li><b>The block decides more than the plan.</b> Flood level, trees, lot size, slope and soil all shape the new house.</li>
          <li><b>Seven of the nine cost drivers belong to the old house and the block.</b> A price before a site visit is a price for the house, not the job.</li>
          <li><b>Asbestos removal and disconnections come before demolition,</b> and the power can't be cut without Energex's written confirmation.</li>
          <li><b>The build is paid in stages, inspected by a certifier and warranted for six years</b> for structural defects.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">What is a knockdown rebuild?</p>
          <p>Demolishing the house you own and building a new one on the same block. You keep the land, the street and the school, and replace the house. It needs building approval for the demolition and the new house, and sometimes a development application.</p>
        </div>
        <div>
          <p class="q">Can any house on the Bayside be knocked down?</p>
          <p>Most post-war houses can. A house built in 1946 or earlier in Brisbane's Traditional building character overlay needs a development application to be demolished, and council may refuse it. A pre-1911 house is to be kept. Check your address on council's mapping first.</p>
        </div>
        <div>
          <p class="q">How much does a knockdown rebuild cost in Brisbane?</p>
          <p>It depends on nine things, and seven of them are about the old house and the block: asbestos, demolition, slope and access, overlays, soil, how the house meets the ground, and where you live meanwhile. We don't publish a figure; any honest number needs someone to have looked at the block.</p>
        </div>
        <div>
          <p class="q">Do we need a development application?</p>
          <p>Every knockdown rebuild needs building approval from a certifier. A DA is only needed if something on your lot triggers it, such as certain overlays for the new house, or a pre-1947 house in the character overlay for the demolition.</p>
        </div>
        <div>
          <p class="q">What's the first thing we should do?</p>
          <p>Check your address on council's City Plan mapping for the character and flood overlays, find the year your house was built, and pull the free FloodWise report. Those three take about fifteen minutes and tell you whether the rest of the path is open.</p>
        </div>
      </div>

      <p class="small sources">Sources: Brisbane City Council, <em>Heritage and character properties</em>, <em>Building a new house: approvals and requirements</em>, <em>FloodWise Property Reports</em>, <em>Protected vegetation</em> and Brisbane City Plan 2014; Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3 (July 2023); Queensland Government, asbestos.qld.gov.au; Energex, <em>Remove your connection</em>; Standards Australia, AS 2870. Each linked post lists its own sources and the date they were read. Plain-English guidance from a builder; not legal, financial or planning advice.</p>
''')


# ================================================================ HUB 2 · living on the Bayside
POSTS["hub2-living"] = dict(
    slug=SLUGS["hub2"],
    section="living",
    title="Living on Brisbane's Bayside: an honest guide to Wynnum, Manly, Lota and the suburbs around them",
    h1="Living on Brisbane's Bayside:<br>an honest guide to Wynnum, Manly, Lota and the suburbs around them.",
    description="An honest guide to living on Brisbane's Bayside from a family builder based at Ransome since 1990: the suburbs one by one, schools and catchments, the train, flooding, storms, the foreshore, and the houses themselves, which is where the real decision usually sits.",
    lede="Most guides to the Bayside are written by someone selling a house here. This one is written by a family that builds them. It covers the suburbs, the schools, the train, the water, the weather and the storms, honestly, including the annoying parts. Then it turns to the houses, because that's usually where the real decision is.",
    date="2026-09-23", category="Living on the Bayside", image="blog/living-on-brisbanes-bayside-an-honest-guide.jpg",
    image_alt="The Wynnum foreshore at low tide with a timber jetty, Norfolk pines and a row of old timber houses facing the bay",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph of a real street.",
    label=("The honest guide", "Living on the Bayside"),
    card_title="Living on Brisbane's Bayside: an honest guide to Wynnum, Manly, Lota and the suburbs around them",
    card_blurb="The suburbs one by one, the schools, the train, the tide, the storms, and the houses, honestly and including the annoying parts. Start here.",
    about=["Brisbane Bayside", "Wynnum", "Manly", "Lota", "Manly West", "Wakerley", "Gumdale", "Ransome", "Tingalpa", "Living in Brisbane"],
    related=[SLUGS["s7"], SLUGS["s8"], SLUGS["s9"]],
    cta="If you love the street and it's the house that isn't working, that's the conversation Nathan has most. He'll walk it with you and tell you honestly what your options are.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Brisbane's Bayside is the string of suburbs along Moreton Bay east of the city, plus the newer and leafier ones behind them. <strong>Wynnum</strong> is the town, with a centre, three stations and the wading pool. <strong>Manly</strong> is the harbour and the village. <strong>Lota</strong> is the quiet one, almost entirely houses. <strong>Manly West</strong> is bigger, flatter and younger. <strong>Wakerley</strong> and <strong>Gumdale</strong> are the newer estates and the acreage. <strong>Ransome</strong> and <strong>Tingalpa</strong> sit on the edge.</p>
        <p>The good parts don't change: the bay at the end of the street, the Cleveland line to the city, walkable villages, and family-sized blocks. The annoying parts are real too: the tide goes out a long way, salt air works on everything, storm season runs October to March, and some streets are mapped for flooding. And most of the houses were built between the 1940s and the 1970s. For many families, the suburb is right and the house is the problem.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#what-is-the-bayside">What is &ldquo;the Bayside&rdquo;?</a></li>
          <li><a href="#the-suburbs">Which suburb is which?</a></li>
          <li><a href="#schools">How do schools work here?</a></li>
          <li><a href="#getting-around">How do you get to the city?</a></li>
          <li><a href="#the-water">What's it like living near the water?</a></li>
          <li><a href="#weekends">What do families do on weekends?</a></li>
          <li><a href="#stages">Is it a place to stay for life?</a></li>
          <li><a href="#before-you-buy">What should you check before you buy?</a></li>
          <li><a href="#the-houses">What are the houses actually like?</a></li>
          <li><a href="#stay-or-go">So do you stay or go?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="what-is-the-bayside">What is &ldquo;the Bayside&rdquo;?</h2>
      <p>In Brisbane, &ldquo;the Bayside&rdquo; means the suburbs on the western shore of Moreton Bay, east of the city: Wynnum, Manly, Lota and the suburbs around them. People stretch it to include Manly West, Wakerley, Gumdale, Tingalpa and Ransome inland, and the Redlands to the south.</p>
      <p>What ties them together is the bay and the housing. The old bayside suburbs grew up along the Cleveland railway line and filled in after the Second World War, when Brisbane's suburbs &ldquo;became populated with low-set timber houses on quarter acre blocks.&rdquo; The newer ones behind them grew up much later, on bigger lots and curved streets.</p>
      <p>We've built across these suburbs since 1990, and Sabre is now based at Ransome. That's why this guide spends as long on the houses as it does on the cafes.</p>

      <h2 class="h2" id="the-suburbs">Which suburb is which?</h2>
      <p>They're close together and they feel very different. Here's the short version of each, with the long version linked.</p>

      <h3 class="h3">Wynnum: the town</h3>
      <p>The biggest and most complete of the bayside suburbs: a town centre, three stations, the wading pool, the high school, and the widest mix of houses and flats. At the 2021 Census it had 14,036 people, and seven in ten dwellings were still separate houses. [[s7|Is Wynnum a good place to live? The good and the annoying.]]</p>

      <h3 class="h3">Manly: the harbour</h3>
      <p>Smaller and older in median age, built around the boat harbour and the esplanade, with a village on Cambridge Parade. Its blocks climb the hill away from the water, which is why people want to build up there. Manly and Manly West get confused constantly. They're different suburbs with different housing and different rules on the block. [[r27|The difference between Manly and Manly West.]]</p>

      <p>Manly West is the much larger suburb inland of Manly: 12,436 people at the 2021 Census against Manly's 4,273, a median age of 41 against 46, more families with children and more separate houses. It was part of Manly until it was gazetted as its own suburb in 1975. Same postcode, same train line, and a flatter, later and more often brick housing stock.</p>

      <h3 class="h3">Lota: the quiet one</h3>
      <p>The smallest of the three bayside suburbs, and the most purely residential: 95.3% of dwellings are separate houses, and it has the highest share of couple families with children. It has a station, one state primary, and some of the flattest blocks on the Bayside. It was a pastoral estate in the 1860s, got its railway in 1889, was the end of the line from 1960 until the 1980s, and filled in during the post-war decades with small timber and fibro houses. [[r28|Lota, the quiet one between Wynnum and Manly.]]</p>

      <blockquote class="proof">
        <p><b>Lota: 95.3% separate houses, 0.7% flats or apartments, 48.8% couple families with children. Wynnum and Manly: about seven in ten separate houses and one in six flats.</b></p>
        <cite>Australian Bureau of Statistics, 2021 Census QuickStats: Wynnum, Manly (Qld) and Lota. One table explains most of the difference in how the three feel.</cite>
      </blockquote>

      <p>If you're choosing between those three, [[s8|the side-by-side comparison is here]]: Wynnum if you want to walk to everything, Manly for the harbour and the cafes, Lota for a quiet street where the kids ride bikes.</p>

      <h3 class="h3">Wakerley and Gumdale: the newer Bayside</h3>
      <p>The inland, newer half. Wakerley is the estate suburb, with houses mostly from the last thirty years on curved streets. Gumdale is the acreage next door, with blocks measured in acres. Wakerley had 8,718 people at the 2021 Census and has grown by close to a thousand in a decade; Gumdale had 2,298 and has its own state primary. You get space and newer houses. You give up the water at the end of the street, the train and the walkable village. [[r29|What you get and what you give up.]]</p>

      <h3 class="h3">Ransome, Tingalpa and the acreage edge</h3>
      <p>Ransome is tiny, 429 people at the last census, much of it reserve along the bay, and it's where Sabre is based. Tingalpa is a proper post-war suburb, closer to the city than any of the bayside suburbs. It had 8,461 people at the 2021 Census and nearly tripled in size between 1954 and 1980, which tells you what most of its houses are. What they share with Gumdale is the edge: big blocks, older subdivisions, creeks and bushland. [[r35|Ransome, Tingalpa and Gumdale.]]</p>

      <h2 class="h2" id="schools">How do schools work here?</h2>
      <p>For most families this is the question that decides the street. In Queensland, every state school has a catchment, and if your home is inside it, your child is entitled to a place. Outside it, you're applying, and a school with an enrolment management plan can say no.</p>
      <p>It's the address that counts, not the suburb. A street can sit in one catchment and the next street in another. You check yours on the Department of Education's EdMap by typing in the address.</p>

      <blockquote class="proof">
        <p><b>&ldquo;A school catchment area is the geographical location where a state school's core intake of students must live.&rdquo;</b> &ldquo;Catchment areas ensure every Queensland student from Prep to Year 12 is able to enrol at their local state school.&rdquo;</p>
        <cite>Queensland Government, <em>School catchment areas</em>, qld.gov.au. The entitlement is to your local school. Anywhere else is an application.</cite>
      </blockquote>

      <p>On the Bayside the state primaries are Wynnum State School, Manly State School, Lota State School, Manly West, Wondall Heights and Wynnum West. For secondary there's Wynnum State High and Brisbane Bayside State College, with Iona College and the Moreton Bay colleges as the independent options.</p>
      <p>The catchment is also the single biggest reason families stay in a house they've outgrown, because it ties the school to the block. [[s10|The Bayside's schools, the catchments, and what &ldquo;in catchment&rdquo; is worth.]]</p>

      <h2 class="h2" id="getting-around">How do you get to the city?</h2>
      <p>By train, mostly. Wynnum, Manly and Lota are on the Cleveland line. On a midday all-stops service we read on the timetable, Central to Wynnum Central took forty minutes, and Lota forty-six. Peak services stop at fewer stations and can be quicker.</p>
      <p>By car there's no honest fixed number. Wynnum is 19.6 kilometres by road from the Brisbane GPO, and the rest depends entirely on the time you leave. The only reliable figure is your own trial run at the hour you'd actually drive. [[r23|How far Wynnum really is from the CBD.]]</p>
      <p>The newer suburbs inland, Wakerley and Gumdale, have no station of their own. That's part of the trade.</p>

      <h2 class="h2" id="the-water">What's it like living near the water?</h2>
      <p>Wonderful, mostly, and it asks things of you. Four things come off the bay and into your life.</p>
      <ul class="pts">
        <li><strong>The tide.</strong> Moreton Bay is shallow, and at low tide the water goes out a long way from the Wynnum and Manly foreshore, leaving sand and mudflats, twice a day. People who expected a beach are surprised. People who stay love it.</li>
        <li><strong>The salt.</strong> Salt air works on steel, fixings, roofing and paint faster than anywhere inland.</li>
        <li><strong>The wind.</strong> The afternoon breeze that makes summer bearable becomes a real wind in a storm.</li>
        <li><strong>The weather.</strong> Council puts storm season at October to March. Heavy rain, strong winds and hail are part of a Brisbane summer, not a rare event.</li>
      </ul>
      <p>[[r30|What the foreshore is really like to live near]] covers all four, and [[r31|what storm season means for an old house's roof, trees and insurance]] covers the part that costs money.</p>

      <p>Before each storm season, the state's Get Ready Queensland checklist is short: check the roof and repair it, keep gutters and downpipes clear, trim trees near the buildings, fix rust and rotting or termite-affected timber, secure loose items, and check the insurance. On an old Bayside house, the roof and the timber are the lines that cost money, because salt air rusts roofing screws and gutters, and timber rots where the paint has failed.</p>

      <h3 class="h3">Does it flood?</h3>
      <p>Parts of the Bayside are mapped for flooding, and the source isn't the Brisbane River. The water council models here comes from storm tide off the bay, from the creeks that drain into it, and from overland flow, which is rain running across the land before it reaches a drain. Many lots aren't affected at all. The ones that are usually still get built on, just higher.</p>
      <p>Council publishes the answer for every address. The Flood Awareness Map shows the likelihood of each type of flooding, and the free FloodWise Property Report gives the levels. [[r24|Does Wynnum flood? What council's maps show.]] Read the map for your address before you believe anyone, including us.</p>

      <h2 class="h2" id="weekends">What do families do on weekends?</h2>
      <p>Mostly the water, and mostly for free. The Wynnum Wading Pool on the esplanade, with a playground and water park beside it. Pandanus Beach by the jetty. The boat harbour at Manly and the esplanade to walk or ride. The Bayside Parklands, which run sixteen kilometres along the shore through mangroves and wetlands where migratory birds land every year. [[r25|What there is to do in Wynnum and Manly with kids.]]</p>
      <p>Moreton Bay is a Ramsar site, listed under the international treaty that protects important wetlands, which is why the shorebirds come every year and why the mangroves along the parklands are left as they are. It's an unusual thing to have at the end of a suburban street, and most families here stop noticing it within a year. Try not to.</p>
      <p>The families who do this every Saturday are the ones who don't leave. When the house stops fitting, they change the house.</p>

      <h2 class="h2" id="stages">Is it a place to stay for life?</h2>
      <p>For a lot of people, yes, and the census agrees. Manly's median age is 46 and Wynnum's 43, older than the newer suburbs behind them.</p>
      <ul class="pts">
        <li><strong>Moving here from interstate?</strong> The humidity, the tide, the storm season, the catchments, the word &ldquo;highset&rdquo;, and what a seventy-year-old timber house is really like to live in. [[s11|What nobody tells you.]]</li>
        <li><strong>Thinking about retiring here?</strong> The flat esplanade path, the train and the village are the reasons to stay. The stairs are the reason people leave. Since 1 October 2023, every new home in Queensland has had to meet the Livable Housing Design Standard, with a step-free entry and wider doors on the entry level. [[r32|Retiring on the Bayside, and whether to stay in the house.]]</li>
      </ul>

      <h2 class="h2" id="before-you-buy">What should you check before you buy here?</h2>
      <p>Six checks, all free or close to it, and all about the address rather than the suburb. Do them before you fall for a kitchen.</p>
      <ul class="pts">
        <li><strong>The school.</strong> Type the address into EdMap. The catchment line can run down the middle of a street.</li>
        <li><strong>The flood report.</strong> Pull council's FloodWise Property Report. It tells you which kinds of flooding apply and the floor level anything new would need.</li>
        <li><strong>The year and the overlay.</strong> If the house was built in 1946 or earlier and the street is in the character overlay, you may not be allowed to knock it down later. [[r2|The fifteen-minute check.]]</li>
        <li><strong>The commute.</strong> Drive it at the hour you'd leave, once, before you sign. Nothing else tells you the truth about the car.</li>
        <li><strong>The roof and the timber.</strong> On a house near the water, these are the parts the salt and the storms have been working on.</li>
        <li><strong>The house's era.</strong> Pre-1990 fibro almost always contains asbestos, which matters the day you want to change anything.</li>
      </ul>
      <p>If you're buying the house for the block and planning to knock it down, the list is longer and the order matters more. [[s4|What to check before you sign.]]</p>

      <h2 class="h2" id="the-houses">What are the houses actually like?</h2>
      <p>This is the part the other guides skip, and it's the part that matters for the next ten years. You can date most Bayside houses from the footpath. There are four kinds.</p>
      <ul class="pts">
        <li><strong>Pre-1947:</strong> timber on stumps, tin roof, vertical-joint walls inside. The Queenslander and its cousins. Some are protected by council's character overlay.</li>
        <li><strong>Late 1940s to 1950s:</strong> the post-war cottage. Lowset timber or fibro, small and simple, built fast during a national housing shortage.</li>
        <li><strong>1960s to 1970s:</strong> the highset, chamferboard or brick upstairs, often with rooms built in underneath later.</li>
        <li><strong>1970s onward:</strong> brick veneer on a concrete slab.</li>
      </ul>
      <p>What they're made of decides what can happen to them next. Timber on stumps can be raised, moved and opened up. Fibro from before 1990 almost always contains asbestos. Brick on a slab can't be lifted. [[s9|What the Bayside's houses are made of, and what each is like to change.]] If you keep hearing the word, [[r12|here's what &ldquo;highset&rdquo; means]].</p>

      <blockquote class="proof">
        <p><b>&ldquo;In 1946, Brisbane architect Robert Cummings estimated that there was a shortfall of 300,000 houses nationwide.&rdquo;</b> Brisbane suburbs &ldquo;became populated with low-set timber houses on quarter acre blocks.&rdquo;</p>
        <cite>State Library of Queensland, <em>Housing a growing state</em>, 2014. The shortage is why the post-war cottage is small, plain and built from whatever could be had, and why so many of them sit on good blocks.</cite>
      </blockquote>

      <h3 class="h3">What does a house built for the Bayside do differently?</h3>
      <p>The old houses got a lot right: up off the ground for air, wide eaves, verandahs, windows on opposite walls for the afternoon breeze off the bay. A new house here keeps those instincts and adds what seventy years of salt, storms and flood mapping have taught.</p>
      <ul class="pts">
        <li><strong>Materials rated for the coast.</strong> Roofing, gutters, fixings and hardware specified for a marine environment, especially in the streets nearest the water.</li>
        <li><strong>A wind design to suit the exposure.</strong> Tie-downs, roof fixings and openings engineered for the site.</li>
        <li><strong>The floor level from council's report.</strong> Living areas up where the FloodWise report says they need to be.</li>
        <li><strong>Facing the breeze, shading the west.</strong> Openings toward the bay breeze, protection from the afternoon sun.</li>
        <li><strong>Built for the next thirty years.</strong> Since 1 October 2023, a step-free entry, wider doors and corridors on the entry level, and bathroom walls ready for grabrails are the law for new homes in Queensland.</li>
      </ul>
      <p>[[r30|Building near the foreshore]] goes into the first four in more detail.</p>

      <h2 class="h2" id="stay-or-go">So do you stay or go?</h2>
      <p>Put all of that together and you see the Bayside's particular problem. The suburbs are some of the best places in Brisbane to raise a family. The blocks are flat, near the water, near the train and the schools. And the houses on them were built for the families of the 1950s, and they're now around seventy years old.</p>
      <p>That's why so many of them are coming down. When the house is worth little, the land is worth a lot and the family wants to stay, starting again on the same block becomes the honest option. Not always, but often enough that you'll see it in your own street. [[r33|Why so many Bayside houses are being knocked down.]]</p>
      <p>If you're at that fork, there are six options, and a rebuild is only one of them. [[r22|We've outgrown the house but we love the street: all six options.]] If you're leaning toward starting again, [[hub1|the whole knockdown rebuild path is here]], step by step. And if you're about to buy an old house to knock down, [[s4|check the block before you sign]].</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Wynnum is the town, Manly the harbour, Lota the quiet one.</b> Manly West, Wakerley and Gumdale are newer and further from the water.</li>
          <li><b>The address decides the state school.</b> Check EdMap before you fall for a house.</li>
          <li><b>The train is the Cleveland line,</b> about forty minutes to Wynnum Central on an all-stops service.</li>
          <li><b>Salt, wind, tide and storms all come off the bay.</b> Council's free maps tell you what applies to your address.</li>
          <li><b>Most of the houses are 1940s to 1970s,</b> on blocks worth more than the house. That's the real decision.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">Which suburbs are on Brisbane's Bayside?</p>
          <p>The core is Wynnum, Manly and Lota on the bay, with Manly West, Wakerley, Gumdale, Tingalpa and Ransome inland and around them. The Redlands continue to the south.</p>
        </div>
        <div>
          <p class="q">Is the Bayside a good place to raise a family?</p>
          <p>For most families, yes: the bay, the train, walkable villages and family-sized blocks. Lota has the highest share of couple families with children of the three bayside suburbs. The catch is usually the house, not the suburb.</p>
        </div>
        <div>
          <p class="q">Does the Bayside flood?</p>
          <p>Some lots are mapped for storm tide, creek or overland flow flooding; many aren't. Council's free FloodWise Property Report gives the answer and the levels for any address.</p>
        </div>
        <div>
          <p class="q">How long is the train to the city?</p>
          <p>On an all-stops midday service we read, Central to Wynnum Central took forty minutes. Peak services can be quicker. Check Translink for the one you'd catch.</p>
        </div>
        <div>
          <p class="q">Why are so many old houses being knocked down?</p>
          <p>The post-war houses are small, around seventy years old and often contain asbestos, while the blocks under them are some of the best in Brisbane. Families who want to stay in the street often end up rebuilding.</p>
        </div>
      </div>

      <p class="small sources">Sources: Australian Bureau of Statistics, 2021 Census QuickStats (Wynnum, Manly, Lota, Manly West, Wakerley, Gumdale, Ransome, Tingalpa); State Library of Queensland, <em>Housing a growing state</em>, 2014; Queensland Government, <em>School catchment areas</em> (EdMap); Translink, Cleveland line timetable (one midday service read 17 September 2026); Brisbane City Council, <em>FloodWise Property Reports</em>, <em>Brisbane Severe Weather Alert</em>. Each linked post lists its own sources and the date they were read. Plain-English guidance from a builder; not property, financial or planning advice.</p>
''')


# ================================================================ HUB 3 · choosing a builder
POSTS["hub3-choose-a-builder"] = dict(
    slug=SLUGS["hub3"],
    section="builder",
    title="How to choose a builder in Queensland: the whole checklist, in plain words",
    h1="How to choose a builder in Queensland:<br>the whole checklist, in plain words.",
    description="The whole checklist for choosing a builder in Queensland: the QBCC licence, Master Builders membership, the quote, fixed price or cost-plus, the contract, the deposit and progress payments, variations, insurance, inspections, defects, and what happens if a builder goes under. Every step sourced from the QBCC.",
    lede="Choosing a builder is the biggest decision in a house build, and most families make it on a feeling. The feeling matters. But Queensland also gives you a set of checks, most of them in the QBCC's own guide, that sort a good builder from a risky one before you've paid a cent. This is all of them, in the order you'll need them.",
    date="2026-09-23", category="Dealing with a builder", image="blog/how-to-choose-a-builder-in-queensland-the-whole-checklist.jpg",
    image_alt="A family's hands and a builder's hands over a building contract on a kitchen table, a house plan rolled beside it",
    image_caption="Illustration in the style of Sabre's story frames, not a photograph.",
    label=("The whole checklist", "Choosing a builder"),
    card_title="How to choose a builder in Queensland: the whole checklist, in plain words",
    card_blurb="The licence, the quote, the contract, the deposit, the insurance, the inspections and the defects, in the order you'll need them. Start here.",
    about=["Choosing a builder", "QBCC", "Queensland Home Warranty Scheme", "Building contract", "Progress payments", "Building in Queensland"],
    related=[SLUGS["s12"], SLUGS["r21"], SLUGS["r45"]],
    cta="Run every check on this page on us too. Our QBCC licence is 15486557. Then book a walk-through and ask Nathan the hard questions face to face.",
    body='''
      <aside class="answer">
        <p class="eyebrow">The short answer</p>
        <p>Choose a Queensland builder in five stages. <strong>Before you talk:</strong> search their licence on the QBCC register and check it's current, covers your work and is in the name you'll sign with. Read their reviews, all of them. <strong>Before you compare:</strong> get a quote with every line and every allowance shown, and know whether it's fixed price or cost-plus. The QBCC strongly prefers fixed price.</p>
        <p><strong>Before you sign:</strong> read the contract with the QBCC's Consumer Building Guide beside you, and check the deposit. On a contract of $20,000 or more it can't be more than 5%. <strong>During the build:</strong> pay only what the contract says, when it says, agree every variation in writing first, and expect a certifier at each stage. <strong>After handover:</strong> know your warranty clocks, six years for structural defects and one year for the rest, and that the Queensland Home Warranty Scheme sits behind a licensed builder. Ask every builder the same questions, including us.</p>
      </aside>

      <nav class="onpage" aria-label="On this page">
        <p class="eyebrow">On this page</p>
        <ol>
          <li><a href="#the-licence">Is the builder licensed for your job?</a></li>
          <li><a href="#memberships">What do memberships and reviews tell you?</a></li>
          <li><a href="#the-shortlist">How do you find builders worth comparing?</a></li>
          <li><a href="#the-quote">What should the quote show?</a></li>
          <li><a href="#contract-type">Fixed price or cost-plus?</a></li>
          <li><a href="#the-contract">What's in the contract?</a></li>
          <li><a href="#the-money">How much do you pay, and when?</a></li>
          <li><a href="#insurance">What insurance protects you?</a></li>
          <li><a href="#during">What should happen during the build?</a></li>
          <li><a href="#after">What happens after handover?</a></li>
          <li><a href="#if-it-goes-wrong">What if the builder goes under?</a></li>
          <li><a href="#owner-builder">Should you build it yourself?</a></li>
          <li><a href="#takeaways">Key takeaways</a></li>
          <li><a href="#questions">Common questions</a></li>
        </ol>
      </nav>

      <h2 class="h2" id="the-licence">Is the builder licensed for your job?</h2>
      <p>This is the first check, and it takes five minutes. The Queensland Building and Construction Commission (QBCC) is the state body that regulates building. It licenses builders, keeps a public register of every licence, handles complaints about defective work, and runs the Queensland Home Warranty Scheme.</p>
      <p>Search the builder's licence number on the QBCC register and check three things:</p>
      <ul class="pts">
        <li><strong>It's current.</strong> Not suspended, not cancelled, not expired.</li>
        <li><strong>Its class covers your job.</strong> A licence for one kind of work doesn't cover every kind.</li>
        <li><strong>The name matches.</strong> The licensee must be the same entity whose name is on the contract you'll sign.</li>
      </ul>
      <p>The register also shows the licensee's history, including any disciplinary action. [[s12|What the QBCC is and how to check a licence.]]</p>

      <blockquote class="proof">
        <p><b>&ldquo;Search the QBCC licensee register to check the history of your builder before you sign the contract on your next repair, renovation or build.&rdquo;</b></p>
        <cite>Queensland Building and Construction Commission, <em>Our lists and registers</em>. Their words, not ours. Do it before the deposit, not after. Sabre's licence is 15486557.</cite>
      </blockquote>

      <h2 class="h2" id="memberships">What do memberships and reviews tell you?</h2>
      <p>Less than the licence, and still something.</p>
      <p><strong>Master Builders Queensland</strong> is the state's building industry association. A member has joined, pays to belong, and has agreed to the association's Code of Conduct, which requires members to conduct their business dealings in a fair, reasonable and honest manner. It's not a licence, it's not a regulator, and it's not insurance. Those come from the QBCC whether or not the builder is a member. [[s13|What Master Builders membership actually means.]] For the record, Sabre is a Master Builders Queensland member, No. 00352, and our QBCC licence is 15486557. Check both before you believe either.</p>
      <p><strong>Reviews</strong> tell you what it was like to deal with the builder, which no register can. Read all of them, including the bad ones, and look at how the builder responded. Look for names. A review that names the person who picked up the phone tells you who you'll be dealing with.</p>

      <h2 class="h2" id="the-shortlist">How do you find builders worth comparing?</h2>
      <p>Broadly, you'll meet two kinds of offer. A <strong>package</strong> is a builder's existing plan sold at an advertised price and fitted to your block. A <strong>custom build</strong> starts with your block and your family. Know which one you're being offered and what the advertised number assumes. [[r15|What a knockdown rebuild package is.]]</p>
      <p>You'll also meet two kinds of builder: the national and volume brands, and the small independents, locally owned and building a handful of homes at a time. Find the independents on the QBCC register by suburb, on the Google map for &ldquo;builders&rdquo; plus your suburb, and on the fences in your own street. [[r16|The small independent builders on Brisbane's Bayside.]]</p>
      <p>Then run the same checks on every one of them. A small builder is held to exactly the same licence and the same insurance as a national one.</p>

      <h2 class="h2" id="the-quote">What should the quote show?</h2>
      <p>Everything, line by line, and the allowances separately. For a knockdown rebuild a complete quote has five groups of lines:</p>
      <ul class="pts">
        <li><strong>Before the house:</strong> asbestos removal, demolition, disconnections, the soil test, engineering, design, approvals and the certifier.</li>
        <li><strong>The site:</strong> earthworks, retaining, drainage, service connections.</li>
        <li><strong>The structure:</strong> footings and slab or subfloor, frame, roof, external walls and windows.</li>
        <li><strong>The inside:</strong> plumbing, electrical, linings, joinery, tiling, painting, floors, fit-off.</li>
        <li><strong>The outside and the paperwork:</strong> driveway, fencing, landscaping, the Home Warranty premium, insurances, margin and GST.</li>
      </ul>
      <p>Then the <strong>allowances and provisional sums</strong>: the items the price can't fix yet, each with its estimate. The QBCC's guide says to keep them to a minimum because the final cost often exceeds the estimate, and to check what proportion of the total they make up. Compare the lines, not the totals. [[r45|What should be in a builder's quote, line by line.]]</p>
      <p>On a knockdown rebuild, most of the difference between two quotes comes from the old house and the block. [[s1|What decides the cost of a knockdown rebuild]] explains why an honest builder won't give you a number before seeing it.</p>

      <h3 class="h3">When is the cheapest quote the wrong one?</h3>
      <p>When it's cheap because something is missing. Quotes are usually thin in three places:</p>
      <ul class="pts">
        <li><strong>The site.</strong> Earthworks and retaining are where a sloping or awkward block costs money, and where a quote written from a plan rather than a visit is lightest.</li>
        <li><strong>The allowances.</strong> A long list of them means a large part of the price isn't fixed yet. Add them up and ask why each one is there.</li>
        <li><strong>What simply isn't there.</strong> The driveway, the landscaping, the fencing, the certifier. Lay two quotes side by side and look for the lines one has and the other doesn't.</li>
      </ul>
      <p>The cheapest total and the cheapest house are often different quotes.</p>

      <h2 class="h2" id="contract-type">Fixed price or cost-plus?</h2>
      <p>A <strong>fixed price</strong> contract states the price up front, and the builder carries the risk of getting it wrong, within the limits of the variations and allowances written in. A <strong>cost-plus</strong> contract is one where the amount the builder receives can't be accurately calculated when you sign. You pay what the job costs plus a margin, and you carry the risk.</p>

      <blockquote class="proof">
        <p><b>&ldquo;QBCC strongly recommends home owners obtain formal legal advice before signing either of these types of contracts which increase your legal risk, reduce your Home Warranty Scheme protection and often result in disputes and cost overruns.&rdquo;</b></p>
        <cite>Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3, effective July 2023, on cost-plus and construction management contracts.</cite>
      </blockquote>

      <p>The QBCC also reports final costs under cost-plus often running 50% to 100% higher than anticipated, and says non-completion cover under the Home Warranty Scheme isn't available on a cost-plus contract at all. [[r11|Fixed price or cost-plus, and which protects you.]]</p>

      <h2 class="h2" id="the-contract">What's in the contract?</h2>
      <p>Every Queensland domestic building contract of $20,000 or more has four parts: the <strong>schedule</strong> (your job's details and numbers), the <strong>general conditions</strong> (the standard rules), any <strong>special conditions</strong> (changes agreed for your job), and the <strong>plans and specifications</strong> (what's actually being built).</p>
      <p>The law requires certain things in there: the price shown prominently on the first page of the schedule if it's fixed; a warning about anything that can change the price; the start date and practical completion date, or how they're worked out; the deposit and progress payments; and the rules on variations and extensions of time. If the price isn't on the front page, ask why. [[r39|What's in a Queensland building contract, in plain English.]]</p>
      <p>The builder must give you the QBCC's Consumer Building Guide before you sign a contract of $20,000 or more. Read the contract with it beside you. Then ask the questions it suggests, and a few more. [[r21|The questions to ask a builder before you sign.]]</p>

      <h3 class="h3">What should you ask before you sign?</h3>
      <p>Group your questions into five: the licence, the contract, the money, the time and the people. Most come straight from the QBCC's guide, and a good builder answers them without blinking because the answers are already in the contract.</p>
      <ul class="pts">
        <li><strong>The licence:</strong> what's your licence number, and is it in the same name as this contract?</li>
        <li><strong>The contract:</strong> is it fixed price? Where's the price on the schedule? What can change it?</li>
        <li><strong>The money:</strong> what's the deposit, what are the stages, and what are the allowances, one by one?</li>
        <li><strong>The time:</strong> how are the start date and practical completion date set, and what extends them?</li>
        <li><strong>The people:</strong> who do we call when something goes wrong, and who's on the phone in month four?</li>
      </ul>
      <p>A builder who bristles at the licence question, or can't tell you what the allowances are, has told you something useful for free.</p>

      <h2 class="h2" id="the-money">How much do you pay, and when?</h2>
      <p>Three rules do most of the work.</p>
      <ul class="pts">
        <li><strong>The deposit is capped.</strong> On a contract of $20,000 or more, the most a builder can take before work starts on site is 5%. Under $20,000 it's 10%. Up to 20% is allowed only where more than half the work is done off site.</li>
        <li><strong>Progress claims follow the work.</strong> After the deposit, each claim must be directly related to work on site and proportionate to it.</li>
        <li><strong>The final payment waits for practical completion.</strong></li>
      </ul>
      <p>Never pay more than the contract says, or earlier than it says. Doing so reduces your protection under the Home Warranty Scheme, and it's the mistake families make with a builder they like. [[s14|Progress payments: what you pay, and when.]]</p>
      <p>If a lender is involved, construction loans are usually paid in stages too, after the lender's valuer confirms each stage is done, and that lines up with the progress payment rules. The loan decision belongs to the lender or a broker. [[r44|Construction loans for a knockdown rebuild.]]</p>

      <h2 class="h2" id="insurance">What insurance protects you?</h2>
      <p>Four policies matter on a house build, and only one of them is really about you.</p>
      <ul class="pts">
        <li><strong>The Queensland Home Warranty Scheme.</strong> Compulsory for residential work over $3,300 by a licensed contractor. It protects you against non-completion, defective work and subsidence for up to six years from completion. You should receive a Notice of Cover within two weeks of signing. If you don't, ask why.</li>
        <li><strong>Contract works insurance</strong> covers the half-built house against fire, storm, theft and damage.</li>
        <li><strong>Public liability</strong> covers injury or damage to third parties.</li>
        <li><strong>Workers' compensation</strong> covers the people on site.</li>
      </ul>
      <p>The last three protect the builder and the job. You want to see that they exist, because if they don't, problems on site become your problems. Ask for the certificates of currency before work starts. It's an ordinary request, and a builder who has them won't mind sending them over. [[r36|What insurance a builder should have.]]</p>

      <h2 class="h2" id="during">What should happen during the build?</h2>
      <p><strong>Variations in writing, first.</strong> A variation is any change to the work or materials after the contract is signed. In Queensland, every variation must be agreed in writing by you before the variation work starts, and any price increase can't be required until that work has started. When shouldn't the price have changed? When the &ldquo;variation&rdquo; was already in the contract, when it's fixing the builder's own error, or when it was never agreed in writing. [[s15|Variations, and when the price shouldn't have changed.]]</p>
      <p><strong>A certifier at each stage.</strong> A building certifier, licensed by the QBCC, issues the approval and inspects the mandatory stages. For a new house those are excavation, footings, slab, frame and final. The builder must give you copies of inspection certificates as soon as practicable, and you can ask the certifier for them in writing. If you ask the certifier in writing for the inspection documents, they have to provide them within five business days. The certifier checks the house against the approved plans and the code. It isn't a quality check of the finishes. That's your handover walk. [[r42|How progress inspections and certifiers work.]]</p>

      <h2 class="h2" id="after">What happens after handover?</h2>
      <p>Three clocks start running, and they're different lengths.</p>
      <ul class="pts">
        <li><strong>The defects liability period</strong> in your contract: the window in which the builder comes back to fix defects. Its length is whatever your contract says, and it's usually the shortest of the three.</li>
        <li><strong>The statutory warranties</strong> in Schedule 1B of the QBCC Act: six years for structural defects and one year for everything else. They're part of every regulated domestic building contract, whether it mentions them or not.</li>
        <li><strong>The Home Warranty Scheme</strong>, with its own time limits for noticing and claiming a defect.</li>
      </ul>
      <p>The details are worth knowing before you need them. For a breach of the statutory warranties, legal proceedings have to be started within the warranty period, or within a further six months if the problem shows up in its last six months. Under the Home Warranty Scheme, a structural defect has to be claimed within three months of first becoming aware of it, and a non-structural defect has to be noticed within six months of substantial completion and claimed within seven. Keep a folder, date everything, and report early.</p>
      <p>[[r37|What a defects liability period is, and what protects you after it.]]</p>

      <h2 class="h2" id="if-it-goes-wrong">What if the builder goes under?</h2>
      <p>It's the fear behind every other question, so here's the straight answer. If a licensed builder on a fixed-price contract can't finish your house, the Home Warranty Scheme can pay to get it finished, within its limits. The claim has to be lodged within three months of the contract ending.</p>
      <p>The QBCC lists when a non-completion claim is available: the contract has validly ended because of the builder's default, the builder has died, the company has been deregistered, or the builder is insolvent and the QBCC has cancelled their licence. If no work had started, the scheme refunds the deposit up to the legal maximum. If work had started, it pays the difference between what's left unpaid under your contract and the reasonable cost of finishing, within the scheme's limits, plus limited amounts for accommodation and for storm or fire damage to the unfinished work.</p>
      <p>Two things shrink that protection before you ever need it: paying more than the contract allowed, or earlier than it required, and signing a cost-plus contract, where non-completion cover isn't available at all. Both are choices you make at the start. [[r40|What happens if a builder goes under mid-build.]]</p>

      <h3 class="h3">The warning signs, all in one place</h3>
      <ul class="pts">
        <li>The licence doesn't match the name on the contract, or the builder is vague about it.</li>
        <li>A deposit of more than 5% on a contract of $20,000 or more, before work starts on site.</li>
        <li>No price on the first page of the schedule, or a quote that's mostly allowances.</li>
        <li>Being steered toward cost-plus when the job could be priced.</li>
        <li>Requests to pay ahead of the contract &ldquo;to keep things moving.&rdquo;</li>
        <li>Variations agreed on site with a nod instead of in writing.</li>
        <li>No Notice of Cover from the Home Warranty Scheme within two weeks of signing.</li>
      </ul>
      <p>Any one of these is a question to ask. Two or three together are a reason to stop.</p>

      <h2 class="h2" id="owner-builder">Should you build it yourself?</h2>
      <p>Some people do. In Queensland you need an owner-builder permit from the QBCC for work worth more than $11,000, and most applicants must complete a course first. You then take on the builder's legal role: every trade, every approval, every inspection, the safety obligations and the defects.</p>
      <p>Owner-builders aren't eligible for the Home Warranty Scheme, and if you sell within six years you must tell the buyer in writing that the work isn't covered. It can suit a capable person with time, on a simple job. On a knockdown rebuild with asbestos, a flood level and a sloping block, it's a full-time job with your own money as the safety net. [[r41|Should we be an owner-builder?]]</p>
      <p>If you're buying an old house to knock down, the checks start even earlier, with the block itself. [[r43|What a building and pest inspection is worth on a knockdown]], and [[hub1|the whole knockdown rebuild path, step by step]].</p>

      <aside class="takeaways" id="takeaways">
        <p class="eyebrow">Key takeaways</p>
        <ul>
          <li><b>Licence first.</b> Current, the right class, the same name as the contract. Five minutes on the QBCC register.</li>
          <li><b>Compare quotes line by line,</b> and count the allowances.</li>
          <li><b>Fixed price protects you;</b> cost-plus shifts the risk to you and loses non-completion cover.</li>
          <li><b>The deposit is capped at 5%</b> on a contract of $20,000 or more, and every claim after it follows the work.</li>
          <li><b>Every variation is agreed in writing</b> before the work starts.</li>
          <li><b>Six years for structural defects, one year for the rest,</b> whatever your contract says.</li>
        </ul>
      </aside>

      <h2 class="h2" id="questions">Common questions</h2>
      <div class="qa">
        <div>
          <p class="q">How do I check if a builder is licensed in Queensland?</p>
          <p>Search their licence number or name on the QBCC's online licensee register. Check the licence is current, that its class covers your work, and that the name matches the entity on your contract. The register also shows their history.</p>
        </div>
        <div>
          <p class="q">What is the maximum deposit a builder can ask for in Queensland?</p>
          <p>For a contract of $20,000 or more, 5% before work starts on site. Under $20,000 it's 10%. Up to 20% is allowed only where more than half the work is done off site.</p>
        </div>
        <div>
          <p class="q">Is a Master Builders member better than a non-member?</p>
          <p>Membership means the builder has agreed to the association's Code of Conduct. It isn't a licence or insurance; those come from the QBCC for every licensed builder. Check the licence first either way.</p>
        </div>
        <div>
          <p class="q">What protects me if the builder doesn't finish?</p>
          <p>The Queensland Home Warranty Scheme, for residential work over $3,300 by a licensed contractor on a fixed-price contract. Paying ahead of the contract reduces the payout, and a cost-plus contract has no non-completion cover.</p>
        </div>
        <div>
          <p class="q">How many quotes should we get?</p>
          <p>Enough to compare line by line. What matters is that every quote covers the same lines and lists its allowances separately, so you're comparing the same job, not just the totals.</p>
        </div>
      </div>

      <p class="small sources">Sources: Queensland Building and Construction Commission, <em>Consumer Building Guide</em>, version 3 (July 2023), <em>Our lists and registers</em>, <em>Contracts and agreement types</em>, <em>Deposits and progress payments</em>, <em>Home warranty for non-completion claims</em>, <em>About owner-building</em>; Master Builders Queensland, <em>Code of Conduct</em>; Schedule 1B, Queensland Building and Construction Commission Act 1991. Each linked post lists its own sources and the date they were read. Plain-English guidance from a builder; not legal or financial advice.</p>
''')


# ---------------------------------------------------------------- [[key|text]] -> relative link
import re as _re


def link(body):
    def rep(m):
        k, t = m.group(1), m.group(2)
        assert k in SLUGS, f"unknown link key {k}"
        return f'<a href="../{SLUGS[k]}/">{t}</a>'
    out = _re.sub(r"\[\[([a-z0-9]+)\|(.*?)\]\]", rep, body, flags=_re.S)
    assert "[[" not in out, "unexpanded link marker"
    return out


for _p in POSTS.values():
    _p["body"] = link(_p["body"])
